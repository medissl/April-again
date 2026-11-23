"""Resolve the original script-derived production plan and all common-game screens."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'Assets/AprilAgain/Art'
NAR=ROOT/'Assets/AprilAgain/Narrative'
DOC=ROOT/'Documentation/Art'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def main():
    m=read(ART/'asset-manifest.json');a=m['assets'];b=read(ART/'scene-bindings.json')
    aliases=read(ART/'Characters/expression-aliases.json')['aliases']
    audio=read(ROOT/'Assets/AprilAgain/Audio/audio-manifest.json')['assets']
    audio_by_id={x['id']:x for x in audio}
    coverage=[];missing=[]
    for p in read(NAR/'asset-plan.json'):
        kind=p['type'];ids=[];files=[];notes={}
        if kind=='map':ids=['map_campus']
        elif kind=='character':ids=['char_mc_silhouettes']
        elif kind=='expression_set':
            c=p['id'].split('_')[1]
            acting={}
            for expr in p['brief']['expressions']:
                canonical=aliases[c].get(expr,expr)
                sid=f'expr_{c}_{canonical}'
                acting[expr]=sid
                ids.append(sid)
            notes['actingAliases']=acting
        elif kind=='placement_poses':
            c=p['id'].split('_')[1]
            ids=[f'char_{c}_placement',f'observation_{c}']+[x for x in a if x.startswith('room_'+c+'_')]
        elif kind=='wardrobe_variant':
            ids=['wardrobe_'+p['id'][len('char_'):]]
        elif kind=='prop':
            _,c,prop=p['id'].split('_',2)
            binding=b['props'].get(prop)
            if binding:ids=[binding['asset']]+binding.get('layers',[])
        elif kind=='audio':
            if p['id'] in audio_by_id:files=['Assets/AprilAgain/Audio/'+audio_by_id[p['id']]['file']]
        elif kind=='audio_set':
            if p['id']=='bgm_endings':
                files=['Assets/AprilAgain/Audio/'+audio_by_id['bgm_ending_'+e]['file'] for e in ['good','neutral','bad']]
            else:
                files=['Assets/AprilAgain/Audio/'+x['file'] for x in audio if not x['id'].startswith(('bgm_','amb_'))]
        else:ids=[p['id']]
        ids=list(dict.fromkeys(ids))
        files+=['Assets/AprilAgain/Art/'+a[i]['file'] for i in ids if i in a]
        okay=bool(files) and all(i in a for i in ids) and all((ROOT/f).is_file() for f in files)
        if not okay:missing.append(p['id'])
        coverage.append(dict(id=p['id'],type=kind,status='covered' if okay else 'missing',
                             assets=ids,files=files,**notes))
    c=read(NAR/'common.json')
    common=dict(opening={s['id']:dict(background='bg_'+s['location']+'_day',dialogueFrame='ui_dialogue_panel',
                                     audio='bgm_daily' if s['location']!='bedroom' else 'bgm_reflection') for s in c['opening']},
        postTour=dict(backgroundPolicy='Keep current exploration location',dialogueFrame='ui_dialogue_panel'),
        firstNight=dict(background='bg_bedroom_evening',dialogueFrame='ui_dialogue_panel',audio='bgm_reflection',props=['mc_blazer_draped','folded_campus_map']),
        morningVariations=dict(background='bg_bedroom_day',dialogueFrame='ui_dialogue_panel',props=['mc_blazer_draped','alarm_clock','admission_envelope']),
        home=dict(background='bg_bedroom_evening',frame='ui_menu_panel',audio='bgm_reflection'),
        nonScoringBarks=dict(frame='ui_dialogue_panel',availabilityIcon='ui_icon_wait',scoreDelta=0),
        systemCopy=dict(frame='ui_modal_panel',buttons=['ui_button_idle','ui_button_focus'],textSource='Narrative/common.json'),
        navigation=dict(map='map_campus',layout='Map/map-layout.json',labelsAreLive=True),
        ambience=dict(default='amb_school',rain='light_rain'),
        sfx=dict(selection='ui_confirm',back='ui_cancel',alarm='alarm',bell='school_bell',rain='light_rain',
                 paper='paper',page='page_turn',zip='zip',cup='cup',bounce='basketball_bounce',
                 rim='basketball_rim',pa='pa_chime'))
    b['common']=common
    (ART/'scene-bindings.json').write_text(json.dumps(b,indent=2),encoding='utf-8')
    result=dict(total=len(coverage),covered=len(coverage)-len(missing),missing=missing,entries=coverage)
    (DOC/'plan-coverage.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='entries'},indent=2))
    if missing:raise SystemExit(1)
if __name__=='__main__':main()
