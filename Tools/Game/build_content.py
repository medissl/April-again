"""Compile the authored screenplay into Unity's small, dictionary-free content contract."""
import json
import shutil
import re
from pathlib import Path
from PIL import ImageFont

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'Assets/AprilAgain'
READING_FONT=ImageFont.truetype(str(BASE/'Art/Fonts/Nunito/Nunito-ExtraBold.ttf'),40)
def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))
def lines(items):
    # Stage directions are production notes, not dialogue to expose to players.
    result=[]
    for x in items:
        if x.get('kind')=='direction' or x.get('speaker')=='Stage':continue
        text=x['text']
        # Reading beats, not a rewrite: keep every word and punctuation mark.
        def page_end(value):
            row='';rows=1;end=0
            for match in re.finditer(r'\S+\s*',value):
                word=match.group().strip();trial=(row+' '+word).strip()
                if READING_FONT.getlength(trial)>1490:
                    if rows==2:return end
                    rows+=1;row=word
                else:row=trial
                end=match.end()
            return len(value)
        while page_end(text)<len(text):
            end=page_end(text)
            ends=[m.end() for m in re.finditer(r'[.!?](?:[\"\u201d\u2019])?\s+',text[:end]) if m.end()>=60]
            cut=ends[-1] if ends else end
            result.append(dict(x,text=text[:cut].strip()));text=text[cut:].strip()
        if text:result.append(dict(x,text=text))
    return result

def main():
    common = read(BASE/'Narrative/common.json')
    binding = read(BASE/'Art/scene-bindings.json')
    manifest = read(BASE/'Art/asset-manifest.json')['assets']
    hotspots = read(BASE/'Art/Rooms/room-hotspots.json')['rooms']
    aliases = read(BASE/'Art/Characters/expression-aliases.json')['aliases']
    data = dict(characters=[], scenes=[], sequences=[], endings=[], locations=[], assets=[])
    def sequence(id, items, location='bedroom', background='', portrait='', girl='', props=None):
        data['sequences'].append(dict(id=id, lines=lines(items), location=location,
                                     background=background or 'bg_'+location+'_day', portrait=portrait,girl=girl,props=props or []))
    for item in common['opening']:
        sequence(item['id'], item['lines'], item['location'])
    for item in common['observations']:
        b=binding['observations'][item['id']]
        sequence(item['id'],item['lines'],item['location'],b['explorationRoom'],b['portrait'],item['girl'],
            [dict(id=k,asset=v['asset'],label=k.replace('_',' ').capitalize()) for k,v in b['props'].items()])
    sequence('postTour',common['postTour'],'gate')
    sequence('firstNight',common['firstNight'],'bedroom','bg_bedroom_evening')
    for i,item in enumerate(common['morningVariations']): sequence('morning.'+str(i),item)
    for key,item in common['home'].items(): sequence('home.'+key,item,'bedroom','bg_bedroom_evening')
    idle = [['class_b','canteen','library'],['class_a','canteen','lobby'],['library','class_c','corridor'],['infirmary','class_b','canteen'],['field','class_c','gate']]
    for i,girl in enumerate(['katya','akira','seoyun','mari','svea']):
        route=read(BASE/f'Narrative/{girl}.json')
        data['characters'].append(dict(id=girl,name=route['name'],voice=route['voice'],idle=idle[i],
            busy=common['nonScoringBarks'][girl]['busy'],used=common['nonScoringBarks'][girl]['used'],
            aliases=[dict(id=k,value=v) for k,v in aliases[girl].items()]))
        sequence('repair.'+girl,route['finaleRepair']['lines'],girl=girl)
        for s in route['scenes']:
            b=binding['scenes'][s['id']]
            portrait=b['dialoguePortrait']
            temp=[dict(id=k,lines=lines(v)) for k,v in s['temperature'].items()]
            data['scenes'].append(dict(id=s['id'],girl=girl,number=s['number'],title=s['title'],location=s['location'],
                expression=s['expression'],wardrobe=s.get('wardrobe','school_uniform'),club=s.get('requiresClubDay',False),
                requiredBlock=s.get('requiredBlock') or '',background=b['cleanBackground'],room=b['explorationRoom'],portrait=portrait,
                setup=lines(s['setup']),closing=lines(s['closing']),temperature=temp,choices=[dict(x,response=lines(x['response'])) for x in s['choices']],
                props=[dict(id=k,asset=v['asset'],label=k.replace('_',' ').capitalize()) for k,v in b['props'].items()]))
        for e in route['endings']:
            data['endings'].append(dict(id=e['id'],girl=girl,kind=e['kind'],title=e['title'],cg=e['cg'],lines=lines(e['lines'])))
    maps={x['id']:x['hitRect'] for x in read(BASE/'Art/Map/map-layout.json')['locations']}
    doors=read(BASE/'Art/Map/door-hotspots.json')['locations']
    for id,loc in read(BASE/'Narrative/locations.json').items():
        data['locations'].append(dict(id=id,name=loc['name'],neighbors=loc['neighbors'],description=loc['purpose'],rect=maps.get(id,[.02,.88,.14,.08]),
            exits=[dict(destination=x['destination'],label=x['label'],kind=x['kind'],rect=x['hitRect']) for x in doors.get(id,[])]))
    for id,item in manifest.items():
        if item['file'].endswith('.png'):
            data['assets'].append(dict(id=id,path='Assets/AprilAgain/Art/'+item['file'],rect=hotspots.get(id,{}).get('hitRect',[.15,.2,.2,.7])))
    spring=BASE/'Art/UI/Spring/spring-manifest.json'
    if spring.exists():data['assets'].extend(read(spring)['assets'])
    final_ui=BASE/'Art/UI/Final/final-ui-manifest.json'
    if final_ui.exists():data['assets'].extend(read(final_ui)['assets'])
    conversation=ROOT/'Documentation/Art/ConversationSprites/conversation-manifest.json'
    if conversation.exists():data['assets'].extend(read(conversation)['assets'])
    out=BASE/'GameData';out.mkdir(exist_ok=True)
    (out/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    # Owned menu sounds reused with the user's explicit authorization. Other MENFENG
    # foley has incomplete upstream provenance and is deliberately not redistributed.
    src=Path('C:/Users/media/Documents/Codex/2026-11-14/i-wa/work/menfeng-audio-clean/assets/audio')
    audio=BASE/'Audio/Interface';audio.mkdir(exist_ok=True)
    for a,b in [('menu-hover.wav','hover.wav'),('menu-select.wav','select.wav'),('menu-open.wav','open.wav')]:
        if (src/a).exists():shutil.copy2(src/a,audio/b)
        elif not (audio/b).exists():raise FileNotFoundError(f'Missing vendored menu cue: {audio/b}')
    kenney=ROOT/'Documentation/AudioSources/kenney_interface-sounds_download/Audio'
    for a,b in [('back_001.ogg','back.ogg'),('confirmation_001.ogg','save.ogg'),('error_001.ogg','error.ogg')]:
        if (kenney/a).exists():shutil.copy2(kenney/a,audio/b)
        elif not (audio/b).exists():raise FileNotFoundError(f'Missing vendored interface cue: {audio/b}')
    print(f"Compiled {len(data['scenes'])} scenes, {len(data['endings'])} endings, {len(data['assets'])} art bindings")

if __name__ == '__main__': main()
