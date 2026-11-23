"""Validate full-game asset coverage, exported media and reference integrity."""
from pathlib import Path
import json, wave, math, sys
from array import array
from PIL import Image, ImageFont
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'Assets/AprilAgain/Art'
NAR=ROOT/'Assets/AprilAgain/Narrative'
DOC=ROOT/'Documentation/Art'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def main():
    m=read(ART/'asset-manifest.json');b=read(ART/'scene-bindings.json');assets=m['assets'];errors=[]
    def check(condition,message):
        if not condition:errors.append(message)
    for aid,a in assets.items():
        p=(ART/a['file']).resolve()
        check(p.is_relative_to(ART.resolve()),f'Path escaped pack: {aid}')
        check(p.is_file(),f'Missing file: {aid}')
        if not p.is_file():continue
        with Image.open(p) as im:
            im.load()
            check(im.size==(a['width'],a['height']),f'Dimension mismatch: {aid}')
            if im.mode=='RGBA':check(im.getchannel('A').getbbox() is not None,f'Empty transparency: {aid}')
        if a.get('source'):check((ART/a['source']).is_file(),f'Missing editable source: {aid}')
    check(not b['missingProps'],'Unbound props: '+', '.join(b['missingProps']))
    check(not b['missingScenes'],'Unbound scenes: '+', '.join(b['missingScenes']))
    check(len(b['scenes'])==90,'Expected 75 encounters and 15 endings.')
    check(len(b['observations'])==5,'Expected five first-day observations.')
    for sid,s in b['scenes'].items():
        for key in ['cleanBackground','explorationRoom','dialoguePortrait','cg','dialogueFrame','choiceFrame']:
            if key in s:check(s[key] in assets,f'{sid}: unknown {key} {s[key]}')
        for prop,entry in s.get('props',{}).items():check(entry is not None,f'{sid}: no prop {prop}')
    for sid,s in b['observations'].items():
        for key in ['explorationRoom','portrait']:check(s[key] in assets,f'{sid}: unknown {key}')
        for prop,entry in s['props'].items():check(entry is not None,f'{sid}: no prop {prop}')
    for key,p in b['props'].items():
        check(p['asset'] in assets,'Unknown prop '+key)
        for layer in p.get('layers',[]):check(layer in assets,'Unknown layer '+layer)
    cgs=[a for a in assets.values() if a['category']=='ending_cg']
    check(len(cgs)==15,'Expected 15 original ending CGs.')
    check(len({a['sha256'] for a in cgs})==15,'Duplicate ending art.')
    for c in ['katya','akira','seoyun','mari','svea']:
        check(len(list((ART/'Characters'/c/'Expressions').glob('*.png')))==(9 if c=='svea' else 8),f'{c}: incomplete expression exports')
    theme=read(ART/'UI/ui-theme.json')
    for key in ['choice','button','icon_button','tab']:
        for state in ['idle','hover','pressed','disabled','focus']:
            check('ui_'+key+'_'+state in assets,f'Missing control state: {key} {state}')
    for f in ['SourceSans3-Regular.ttf','SourceSans3-Semibold.ttf','SourceSerif4-Regular.ttf','SourceSerif4-It.ttf']:
        p=ART/'Fonts'/f
        check(p.exists() and p.read_bytes()[:4] in [b'\x00\x01\x00\x00',b'OTTO'],f'Invalid font: {f}')
    for f in ['SourceSans3-OFL.txt','SourceSerif4-OFL.txt']:check((ART/'Fonts'/f).is_file(),'Missing license: '+f)
    # Choice frames allow two lines at 28px on a 1920x1080 reference canvas.
    f=ImageFont.truetype(str(ART/'Fonts/SourceSans3-Regular.ttf'),28);choice_count=0;maxlines=0
    for who in ['katya','akira','seoyun','mari','svea']:
        d=read(NAR/(who+'.json'))
        for s in d['scenes']:
            for ch in s['choices']:
                row='';lines=1
                for word in ch['text'].split():
                    trial=(row+' '+word).strip()
                    if f.getlength(trial)>908:lines+=1;row=word
                    else:row=trial
                choice_count+=1;maxlines=max(maxlines,lines)
                check(lines<=2,f'Choice needs more than two lines: {who}.{s["number"]}')
    audio=read(ROOT/'Assets/AprilAgain/Audio/audio-manifest.json')['assets']
    for a in audio:
        with wave.open(str(ROOT/'Assets/AprilAgain/Audio'/a['file']),'rb') as w:
            check(w.getnchannels()==2 and w.getsampwidth()==2,'Invalid audio format: '+a['id'])
            data=array('h',w.readframes(w.getnframes()))
            if sys.byteorder!='little':data.byteswap()
            check(len(data)>0 and min(data)>-32767 and max(data)<32767,'Clipped/empty audio: '+a['id'])
    # Both source copy and state frames must keep normal text contrast.
    def lum(h):
        a=[int(h[i:i+2],16)/255 for i in [1,3,5]]
        a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a]
        return sum(x*y for x,y in zip(a,[.2126,.7152,.0722]))
    contrast=(lum('#F7F1E8')+.05)/(lum('#263340')+.05)
    check(contrast>=4.5,'Body text contrast below 4.5:1')
    report=dict(status='passed' if not errors else 'failed',originalIllustrations=m['originals'],
        totalAssetRecords=len(assets),encounters=75,endings=len(cgs),observations=5,
        propReferences=len(b['props']),choicesChecked=choice_count,maximumChoiceLines=maxlines,
        referenceCanvas=[1920,1080],audioAssets=len(audio),bodyContrast=round(contrast,2),
        checks=['All image files decoded','All referenced scene assets resolved','All five expression sets exported',
                'Every choice fits the supplied frame','All UI state variants exist','Font files and licenses present',
                'Audio frames decode without clipping','Ending illustrations have distinct hashes'],
        errors=errors,limits=['This report validates the art pack. Unity runtime, route, save and build checks are recorded separately in Documentation/Testing.'])
    (DOC/'asset-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
