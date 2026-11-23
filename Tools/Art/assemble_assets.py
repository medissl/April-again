"""Slice production atlases without repainting, and bind every scripted asset."""
from pathlib import Path
import json, hashlib
from PIL import Image
ROOT = Path(__file__).resolve().parents[2]
ART = ROOT/'Assets/AprilAgain/Art'
NAR = ROOT/'Assets/AprilAgain/Narrative'
DOC = ROOT/'Documentation/Art'
CHARS = ['katya','akira','seoyun','mari','svea']

def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def production():
    rows = read(DOC/'production-catalog.json')
    p = DOC/'room-production-catalog.jsonl'
    if p.exists(): rows += [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    p = DOC/'supplemental-production-catalog.jsonl'
    if p.exists(): rows += [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    p = DOC/'continuation-production-catalog.jsonl'
    if p.exists(): rows += [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    p = DOC/'refinement-production-catalog.jsonl'
    if p.exists(): rows += [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    return list({r['id']: r for r in rows}.values())

def facts(path):
    with Image.open(path) as im:
        a = im.getchannel('A') if im.mode == 'RGBA' else None
        bbox = a.getbbox() if a else (0,0,*im.size)
        return dict(width=im.width,height=im.height,mode=im.mode,alphaBounds=bbox,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest())

def export_atlases(rows):
    assets = {}
    replacements=DOC/'release-101-replacements.json'
    standalone={a['file'] for a in read(replacements)['assets']} if replacements.exists() else set()
    for j in rows:
        p = ART/j['target']
        item = dict(id=j['id'],file=j['target'],category=j['category'],method=j['method'],**facts(p))
        if j.get('grid'):
            im = Image.open(p)
            cols, nr = j['grid']
            item['grid'] = j['grid']
            item['sprites'] = []
            for i, cell in enumerate(j['cells']):
                x,y = i%cols, i//cols
                rect = (round(x*im.width/cols),round(y*im.height/nr),round((x+1)*im.width/cols),round((y+1)*im.height/nr))
                category = j['category']
                if category == 'expressions':
                    who = j['id'].split('_')[1]; dest = Path('Characters')/who/'Expressions'/f'{cell}.png'
                    sid = f'expr_{who}_{cell}'
                elif category == 'placement':
                    who = j['id'].split('_')[1]; dest = Path('Characters')/who/'Poses'/f'{cell}.png'
                    sid = f'pose_{who}_{cell}'
                elif category == 'wardrobe':
                    who = j['id'].split('_')[1]; outfit = j['id'][len('wardrobe_'+who+'_'):]
                    dest = Path('Characters')/who/'Wardrobes'/outfit/f'{cell}.png'
                    sid = f'wardrobe_{who}_{outfit}_{cell}'
                elif category == 'mc':
                    dest = Path('Characters/mc/Poses')/f'{cell}.png'; sid = 'mc_'+cell
                elif category == 'illustrated_pages':
                    dest = Path('Props/Pages')/f'{cell}.png'; sid = cell
                else:
                    dest = Path('Props/Items')/f'{cell}.png'; sid = cell
                (ART/dest).parent.mkdir(parents=True,exist_ok=True)
                if dest.as_posix() in standalone:
                    if not (ART/dest).exists():raise FileNotFoundError('Missing approved HD sprite: '+str(dest))
                    sprite=dict(id=sid,file=dest.as_posix(),category='sprite_export',method='individual HD production sprite',**facts(ART/dest))
                else:
                    im.crop(rect).save(ART/dest)
                    sprite = dict(id=sid,file=dest.as_posix(),category='sprite_export',atlas=j['target'],rectTopLeft=list(rect),**facts(ART/dest))
                assets[sid] = sprite
                item['sprites'].append(sid)
        assets[j['id']] = item
    for source in ['native-catalog.json','UI/ui-theme.json']:
        d = read(ART/source)
        for a in (d['assets'] if isinstance(d,dict) else d):
            assets['ui_'+a['id'] if source.startswith('UI/') else 'native_'+a['id']] = {**a, 'category':'native_graphic',**facts(ART/a['file'])}
    return assets

# Exact semantic aliases. Quantity variants instantiate the same reusable sprite.
PHYSICAL = {
 'visitor_chair':('chair',1),'hoop':('bg_field_day',1),
 'backing_card':('native_backing_card',1),
 'cat':('cat',1),'dark_chocolate':('dark_chocolate',1),'delivery_box':('delivery_box',1),
 'fencing_bag':('fencing_bag',1),'fencing_mask':('fencing_mask',1),'floor_markers':('native_floor_markers',3),
 'floor_tape':('floor_tape',1),'folder':('folder',1),'glue':('glue',1),'melonpan':('melonpan',1),
 'pen':('pen',1),'phone':('phone',1),'photo_prints':('photo_prints',1),
 'reference_books':('reference_books',1),'stapler':('stapler',1),'tea_bottle':('tea_bottle',1),'two_melonpan':('melonpan',2),
 'backup_envelope':('envelope',1),'bento':('bento',1),'calculator':('calculator',1),
 'headphones':('headphones',1),'laptop':('laptop',1),'lunch_trays':('lunch_tray',2),
 'notebook':('blue_journal',1),'phone_message':('native_phone_message',1),'satchel_keychains':('satchel',1),
 'spare_container':('spare_container',1),'strategy_game_screen':('native_strategy_game_screen',1),
 'survey_envelopes':('envelope',3),'three_request_messages':('native_three_request_messages',1),'two_coffee_cans':('coffee_can',2),
 'alternate_photo':('alternate_photo',1),'atlas':('open_atlas',1),'atlases':('closed_atlas',3),
 'blue_journal':('blue_journal',1),'blurred_photo':('blurred_photo',1),'bookmark':('bookmark',1),
 'camera':('camera',1),'dictionary':('book',1),'display_board':('display_board',1),
 'drying_display':('display_board',1),'finished_display':('display_board',1),'folded_sketch':('folded_sketch',1),
 'fruit_cup':('fruit_cup',1),'noodle_bowl':('noodle_bowl',1),'paperweight':('paperweight',1),
 'photo_print':('sky_photo',1),'sealed_letter':('envelope',1),'sky_photo':('sky_photo',1),
 'two_blank_bookmarks':('bookmark',2),'window_chairs':('chair',2),
 'apron':('wardrobe_mari_uniform_with_apron_full_body',1),'book':('book',1),'clean_blankets':('clean_blankets',1),
 'custard_dessert':('custard_dessert',1),'fabric_backing':('fabric_backing',1),'folded_cloth':('folded_cloth',1),
 'gate_bench':('bench',1),'her_tea_cup':('tea_cup',1),'leaflet_rack':('leaflet_rack',1),
 'loose_button':('loose_button',1),'lunch_plate':('lunch_tray',1),'practice_mat':('practice_mat',1),
 'red_bean_dessert':('red_bean_dessert',1),'sewing_kit':('sewing_kit',1),'sports_bag':('sports_bag',1),
 'squeaky_chair':('chair',1),'supply_box':('supply_box',1),'tea_tin':('tea_tin',1),'thermos':('thermos',1),
 'two_bento':('bento',2),'two_cups':('tea_cup',2),'two_tea_cups':('tea_cup',2),'visitor_chairs':('chair',2),
 'basketball':('basketball',1),'closed_bag':('sports_bag',1),'court_cones':('court_cone',3),
 'cozy_game_screen':('native_cozy_game_screen',1),'equipment_cart':('equipment_cart',1),
 'field_bench':('bench',1),'handheld_game':('handheld_game',1),'lunch_tray':('lunch_tray',1),
 'neighborhood_dog':('neighborhood_dog',1),'pencil':('pencil',1),'pencil_case':('pencil_case',1),
 'plush_dog_keychain':('plush_dog_keychain',1),'strawberry_milk':('strawberry_milk',1),
 'supply_boxes':('delivery_box',2),'two_strawberry_milk':('strawberry_milk',2),
 'sandwich_wrapper':('sandwich_wrapper',1),'keychain_satchel':('satchel',1),'journal':('blue_journal',1),'sketchbook':('blue_journal',1),
}
# Distinct paper treatments use authored readable document art.
DOCUMENT_ALIASES = {'sticky_notes':'paper_labels','sandwich_wrapper':'paper_labels'}
OUTFIT_ACTIVE = {'school_tracksuit':'determined','fencing_kit_with_mask':'annoyed','aikido_gi_and_trousers':'determined',
                 'uniform_with_apron':'concerned','school_sports_jacket_and_trousers':'annoyed'}
EXPR_ALIAS = {'composed':'neutral','downcast':'sad','blushing':'flustered','focused':'determined','unbothered':'neutral','attentive':'neutral'}

def bind_props(assets, routes, common):
    required = set()
    for d in routes.values():
        for s in d['scenes']: required.update(s['props'])
    for o in common['observations']: required.update(o.get('props',[]))
    bindings, missing = {}, []
    for key in sorted(required):
        aid,count = PHYSICAL.get(key,('native_'+DOCUMENT_ALIASES.get(key,key),1))
        if aid not in assets:
            missing.append(key); continue
        bindings[key] = dict(asset=aid,file=assets[aid]['file'],count=count)
        if key=='hoop': bindings[key].update(embedded=True,region=[0.44,0.20,0.14,0.38])
        if key in ['finished_display','drying_display']:
            bindings[key]['layers'] = ['sky_photo','alternate_photo','native_window_essay']
        if key == 'finished_reading_corner':
            bindings[key]['layers'] = ['leaflet_rack','book','native_reading_list']
    return bindings, missing

def make_bindings(assets, rows):
    routes = {c:read(NAR/(c+'.json')) for c in CHARS}
    common = read(NAR/'common.json')
    acting_aliases = read(ART/'Characters/expression-aliases.json')['aliases']
    props, missing = bind_props(assets,routes,common)
    rooms = {(j['character'],j['location'],j['wardrobe']):j['id'] for j in rows if j['category']=='room_placement'}
    scenes, gaps = {}, []
    for c,d in routes.items():
        for s in d['scenes']:
            outfit = s.get('wardrobe','school_uniform')
            key = f'{c}.{s["number"]:02}'
            room = rooms.get((c,s['location'],outfit))
            expr = acting_aliases[c].get(s['expression'], EXPR_ALIAS.get(s['expression'],s['expression']))
            # Outfit-specific busts must match their full-body costume.
            if outfit != 'school_uniform':
                exprs = {OUTFIT_ACTIVE[outfit]:'active','soft_smile':'soft_smile','neutral':'neutral'}
                face = f'wardrobe_{c}_{outfit}_{exprs.get(expr,"neutral")}'
            else: face = f'expr_{c}_{expr}'
            if c=='mari' and outfit!='school_uniform' and expr=='warm': face=f'wardrobe_{c}_{outfit}_soft_smile'
            if c=='svea' and outfit!='school_uniform' and expr=='flustered': face='wardrobe_svea_sports_flustered'
            if c=='katya' and s['number']==5: room='room_katya_corridor_rain'
            bg = 'bg_corridor_rain' if c=='katya' and s['number']==5 else 'bg_'+s['location']+'_day'
            entry = dict(cleanBackground=bg,explorationRoom=room,dialoguePortrait=face,wardrobe=outfit,
                         props={p:props.get(p) for p in s['props']},dialogueFrame='ui_dialogue_panel',
                         choiceFrame='ui_choice_idle',audio='bgm_daily')
            if not room or face not in assets or bg not in assets: gaps.append(key)
            scenes[key] = entry
        for e in d['endings']:
            key=f'{c}.ending.{e["kind"]}'
            scenes[key]=dict(cg=f'cg_{c}_{e["kind"]}',audio='bgm_ending_'+e['kind'],dialogueFrame='ui_dialogue_panel')
            if scenes[key]['cg'] not in assets: gaps.append(key)
    observations = {}
    for o in common['observations']:
        c=o['girl']; room='observation_'+c if 'observation_'+c in assets else rooms.get((c,o['location'],'school_uniform'))
        # Svea's sports-day observation uses the sports costume at the court.
        if not room and c=='svea': room=rooms.get((c,o['location'],'school_sports_jacket_and_trousers'))
        observations[o['id']] = dict(explorationRoom=room,portrait=f'expr_{c}_{acting_aliases[c].get(o["expression"], EXPR_ALIAS.get(o["expression"],o["expression"]))}',
                                      props={p:props.get(p) for p in o['props']},observationOnly=True)
        if not room: gaps.append(o['id'])
    return dict(schemaVersion=1,scenes=scenes,observations=observations,props=props,
                copySource='Assets/AprilAgain/Narrative',missingProps=missing,missingScenes=gaps)

def main():
    rows=production()
    assets=export_atlases(rows)
    bindings=make_bindings(assets,rows)
    manifest=dict(schemaVersion=1,referenceCanvas=[1920,1080],coordinateOrigin='top-left',
        originals=len(rows),assets=assets,notes=[
          'PNG source resolutions are reported honestly; no artificial 4K upscaling.',
          'Transparent atlas exports are crops only. Source illustrations are preserved.',
          'Room views already contain the girl. Do not also draw her placement sprite over that image.',
          'Use clean backgrounds plus transparent placement sprites when composing multiple people.',
          'Use the standalone expression bust in dialogue portrait mode; do not splice faces onto full-body art.',
          'Outfits have neutral, active and soft-smile busts. Other emotions use text acting with the neutral bust.',
          'UI text is live; editable document/wordmark SVGs and raster fallbacks are provided.'])
    (ART/'asset-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    (ART/'scene-bindings.json').write_text(json.dumps(bindings,indent=2),encoding='utf-8')
    report=dict(originalIllustrations=len(rows),exportedAssets=len(assets),sceneBindings=len(bindings['scenes']),
                observations=len(bindings['observations']),propBindings=len(bindings['props']),
                missingProps=bindings['missingProps'],missingScenes=bindings['missingScenes'])
    (DOC/'asset-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
