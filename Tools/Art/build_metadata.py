"""Write coordinate/usage metadata. Geometry here is interface data, not art."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'Assets/AprilAgain/Art'
NAR=ROOT/'Assets/AprilAgain/Narrative'
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2),encoding='utf-8')
def main():
    locations=json.loads((NAR/'locations.json').read_text(encoding='utf-8'))
    regions={
      'infirmary':[.07,.155,.156,.30],'class_b':[.281,.079,.182,.224],
      'class_c':[.523,.077,.179,.227],'library':[.752,.133,.183,.303],
      'corridor':[.23,.305,.52,.075],'class_a':[.532,.378,.178,.163],
      'lobby':[.410,.553,.152,.244],'canteen':[.172,.551,.183,.281],
      'field':[.618,.563,.288,.29],'gate':[.437,.882,.098,.09]}
    roomdata=[]
    for key,rect in regions.items():
        x,y,w,h=rect
        roomdata.append(dict(id=key,label=locations[key]['name'].replace(' / hardcourt',''),
            hitRect=rect,labelPosition=[x+w/2,y+h/2],neighbors=locations[key]['neighbors'],
            travelCostsTime=False))
    write(ART/'Map/map-layout.json',dict(schemaVersion=1,art='Map/campus_illustration.png',
        coordinateSystem='normalized top-left; x,y,width,height',locations=roomdata,
        home=dict(id='bedroom',via='gate',label='Home',asset='UI/icon_home.png'),
        note='Navigation graph in Narrative/locations.json is authoritative; map geometry is a visual aid.'))
    aliases={
      'katya':{'composed':'neutral','smile':'soft_smile'},
      'akira':{'concerned':'worried','smile':'delighted'},
      'seoyun':{'smile':'warm'},
      'mari':{'smile':'warm'},
      'svea':{'smile':'soft_smile','unbothered':'neutral','focused':'neutral'}}
    write(ART/'Characters/expression-aliases.json',dict(
        aliases=aliases,policy='Aliases consolidate the screenplay acting directions; use canonical face assets, never random expressions.',
        wardrobe=dict(mari_warm='soft_smile',katya_tracksuit_determined='active',
          katya_fencing_annoyed='active',svea_sports_annoyed='active',svea_sports_flustered='flustered'),
        dialogueMode='Standalone head-and-shoulders portrait. Do not splice changing faces into full-body sprites.',
        heightCm=dict(katya=176,akira=167,seoyun=163,mari=176,svea=171,mc=173)))
    write(ART/'UI/screen-layouts.json',dict(referenceCanvas=[1920,1080],
        scaleMode='Scale With Screen Size; preserve illustration aspect ratio; width/height match 0.5',
        safeMargin=64,screens={
          'title':dict(background='Title/title_school.png',wordmark='Title/wordmark_ink.png',
            menu=['New game','Continue','Load game','Gallery','Settings','Quit']),
          'exploration':dict(day=[64,48,400,96],navigation=[1512,48,296,96],location=[64,918,384,88],
            normalSocialSlots=2,saturdaySocialSlots=3,slotIcons=['slot_open','slot_used'],durationHours=3,
            labels='Show character name and availability on hover/focus. Clicking empty scenery does nothing.'),
          'dialogue':dict(panel=[128,752,1664,272],name=[160,708,360,64],portrait=[1110,130,690,690],
            text=[176,812,1500,132],bodySize=32,lineHeight=44,maximumLines=3,
            footer=['History','Auto','Skip','Hide','Save'],pagination='Paginate at line limit without discarding text.'),
          'choices':dict(first=[128,294,1008,88],verticalStep=106,bodySize=28,textWidth=908,maximumLines=2,
            scoreVisibility='No good/bad/neutral labels on choice buttons.'),
          'bedroom':dict(background='Backgrounds/bg_bedroom_evening.png',menu=['Journal','Save game','Sleep / next day']),
          'save_load':dict(frame='journal_panel',slot='save_slot',slotCount=4,pages=True),
          'settings':dict(frame='journal_panel',controls=['slider_track','slider_fill','slider_handle','checkbox_empty','checkbox_checked'],
            values=['Master volume','Music','Text speed','Window mode','Reduced motion','Stop skip at unread text']),
          'journal':dict(frame='journal_panel',portraitSize=[220,220],show=['Known places','Encounter titles','Notes willingly shared']),
          'ending_gallery':dict(frame='journal_panel',locked='icon_lock',columns=3,unlockOn='Completed ending'),
          'history':dict(frame='journal_panel',scroll=['scroll_track','scroll_thumb']),
          'pause':dict(frame='journal_panel',menu=['Resume','Save game','Load game','Settings','Return to title']),
          'confirmation':dict(frame='modal_panel',actions=['Continue','Go back'],saveBeforeFinale=True)},
        interaction=dict(states=['idle','hover','pressed','disabled','focus'],minimumTarget=56,
            keyboard=['Tab or arrows: focus','Enter/Space: select','Escape: back/pause'],
            focusOutlinePx=3,skipStopsAtUnread=True,skipStopsAtChoices=True,
            reducedMotion='Disable fades and decorative transitions',cursorHotspot=[6,4])))

    # Hit regions are authored against the actual generated in-room views.
    # Rectangles are x,y,w,h, normalized; do not include the surrounding table.
    hit={
      'katya':{'class_b':[.66,.22,.14,.74],'canteen':[.49,.34,.10,.46],
               'corridor':[.17,.23,.16,.72],'gate':[.18,.28,.11,.58],
               'library':[.14,.38,.18,.46],'lobby':[.34,.30,.09,.44]},
      'akira':{'class_a':[.74,.35,.11,.43],'canteen':[.43,.34,.12,.46],
               'library':[.21,.38,.15,.44],'lobby':[.30,.30,.11,.55]},
      'seoyun':{'library':[.14,.37,.15,.50],'corridor':[.18,.26,.13,.68],
                'class_c':[.07,.38,.13,.48],'canteen':[.43,.34,.13,.48],'lobby':[.38,.32,.11,.50]},
      'mari':{'infirmary':[.03,.36,.20,.57],'canteen':[.44,.31,.12,.54],
              'class_b':[.66,.32,.18,.63],'lobby':[.35,.30,.11,.48],'gate':[.04,.40,.14,.39]},
      'svea':{'field':[.22,.24,.16,.72],'canteen':[.44,.31,.13,.57],
              'class_c':[.045,.34,.17,.58],'gate':[.41,.28,.12,.60]}}
    outfits={'katya_school_tracksuit':[.06,.30,.12,.63],
             'katya_fencing_kit_with_mask':[.78,.30,.13,.62],
             'mari_aikido_gi_and_trousers':[.21,.31,.12,.62],
             'mari_uniform_with_apron':[.12,.38,.18,.54],
             'svea_school_sports_jacket_and_trousers':[.24,.21,.16,.75]}
    obs={'katya':[.60,.20,.17,.70],'akira':[.36,.29,.15,.66],
         'seoyun':[.13,.38,.19,.46],'mari':[.08,.33,.12,.60],'svea':[.58,.25,.22,.68]}
    records=[]
    for fn in ['room-production-catalog.jsonl','supplemental-production-catalog.jsonl','refinement-production-catalog.jsonl']:
        path=ROOT/'Documentation/Art'/fn
        if path.exists():
            records += [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    room_hits={}
    for r in records:
        if r['category'] not in ['room_placement','room_weather','observation']:continue
        c=r['character'];loc=r['location'];outfit=r.get('wardrobe','school_uniform')
        rect=obs[c] if r['category']=='observation' else outfits.get(c+'_'+outfit,hit[c].get(loc))
        if r['id']=='room_katya_corridor_rain':rect=[.14,.27,.18,.69]
        if rect:
            room_hits[r['id']]=dict(file=r['target'],character=c,location=loc,hitRect=rect,
                label=dict(katya='Katya',akira='Akira',seoyun='Seo-yun',mari='Mari',svea='Svea')[c],
                interaction='Observe' if r['category']=='observation' else 'Talk / availability check',
                note='Keep labels live; respect scene availability and once-per-day state.')
    write(ART/'Rooms/room-hotspots.json',dict(coordinateSystem='normalized top-left x,y,width,height',
        assetMode='Character is already drawn into the room plate; hotspot is invisible until hover/focus.',
        rooms=room_hits,
        layeredMode='For a shared room with multiple available people, use its clean plate and separate transparent character poses. Do not stack complete room PNGs.'))
    doors={
      'bedroom':{'gate':[.20,.16,.065,.33]},
      'class_a':{'corridor':[.80,.23,.075,.31]},
      'class_b':{'corridor':[.88,.23,.10,.31]},
      'class_c':{'corridor':[.94,.23,.06,.32]},
      'library':{'corridor':[.75,.28,.105,.35]},
      'infirmary':{'corridor':[.76,.20,.11,.48]},
      'canteen':{'lobby':[.75,.25,.11,.38]},
      'field':{'lobby':[.19,.37,.09,.13],'gate':[.025,.64,.045,.16]},
      'gate':{'lobby':[.90,.30,.055,.40],'bedroom':[.39,.35,.32,.30],'field':[.025,.52,.045,.16]},
      'lobby':{'corridor':[.70,.27,.15,.38],'canteen':[.16,.24,.09,.39],
               'gate':[.47,.24,.20,.36],'field':[.88,.24,.12,.46]},
      'corridor':{'class_a':[.82,.19,.18,.75],'class_b':[.64,.24,.05,.37],
                  'class_c':[.54,.30,.04,.29],'library':[.455,.29,.05,.25],
                  'lobby':[.43,.38,.06,.19],'infirmary':[.02,.40,.045,.16]}}
    edge={('corridor','infirmary'),('gate','field'),('gate','lobby'),('field','gate')}
    write(ART/'Map/door-hotspots.json',dict(coordinateSystem='normalized top-left x,y,width,height',
      locations={src:[dict(destination=dest,hitRect=rect,
         kind='edge_navigation' if (src,dest) in edge else 'door_or_path',
         label='Home' if dest=='bedroom' else locations[dest]['name']) for dest,rect in entries.items()]
         for src,entries in doors.items()},
      note='Edge arrows represent a wing/path outside the camera view. Never put a door hotspot over a window. Navigation uses the authoritative reversible graph.'))

    write(ART/'import-settings.json',dict(
      referenceCanvas=[1920,1080],colorSpace='sRGB illustration and UI color textures',
      png=dict(maxSize=2048,filter='Bilinear',wrap='Clamp',mipmaps=False,
               preserveAspect=True,alpha='Straight alpha from input; enable Alpha Is Transparency for transparent sprites'),
      sprites=dict(textureType='Sprite (2D and UI)',mode='Single for exported PNGs',pixelsPerUnit=100,
                   pivot='Use alphaBounds from asset-manifest. Feet at lower visible bound for exploration.'),
      originals='Atlases are preserved masters; use the exported individual sprites or supplied rect metadata, not both.',
      ui='Apply nine-slice borders from UI/ui-theme.json; keep all dialogue and HUD text live.',
      fonts='Use unmodified supplied static TTFs. Create TextMeshPro font assets during runtime integration.',
      audio=dict(format='22050 Hz stereo 16-bit PCM WAV',music='Streaming, loop enabled where audio-manifest says loop',
                 shortEffects='Decompress on load; one-shot',levels='Keep music/ambience below dialogue and UI sounds.'),
      cautions=['Room-placement PNGs already include the character. Do not draw a second sprite on top.',
                'Do not treat review JPGs as production art or as evidence of a running Unity game.']))
    write(ART/'Fonts/font-sources.json',dict(
      body='Source Sans 3 Regular / Semibold',display='Source Serif 4 Regular / Italic',
      licenseFiles=['SourceSans3-OFL.txt','SourceSerif4-OFL.txt'],modified=False,
      sources=['https://github.com/adobe-fonts/source-sans/tree/release/TTF',
               'https://github.com/adobe-fonts/source-serif/tree/release/TTF',
               'https://github.com/google/fonts/tree/main/ofl/sourcesans3',
               'https://github.com/google/fonts/tree/main/ofl/sourceserif4']))
    print('Wrote map, expression, UI screen and Unity import metadata.')
if __name__=='__main__':main()
