"""Render asset-layout proofs and an offline searchable review gallery.

These are asset compositions, not a running game or Unity screenshots.
"""
from pathlib import Path
from html import escape
import json, math
from PIL import Image, ImageDraw, ImageFont, ImageOps
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'Assets/AprilAgain/Art'
OUT=ROOT/'Documentation/Art/Review'
OUT.mkdir(parents=True,exist_ok=True)
INK,PAPER,MAROON,MUTED='#263340','#F7F1E8','#8F4D5B','#66716E'
SIZES=(1920,1080)

def font(size,serif=False,bold=False):
    return ImageFont.truetype(str(ART/'Fonts'/('SourceSerif4-Regular.ttf' if serif else ('SourceSans3-Semibold.ttf' if bold else 'SourceSans3-Regular.ttf'))),size)

def text(im,xy,s,size=30,color=INK,serif=False,bold=False):
    ImageDraw.Draw(im).text(xy,s,font=font(size,serif,bold),fill=color,anchor='lt')

def load(rel): return Image.open(ART/rel).convert('RGBA')

def paste(im,rel,xy,size=None):
    a=load(rel)
    if size: a=a.resize(size,Image.Resampling.LANCZOS)
    im.alpha_composite(a,xy)

def bg(rel):
    return ImageOps.fit(load(rel),SIZES,method=Image.Resampling.LANCZOS)

def frame(im,name,xy,size=None): paste(im,'UI/'+name+'.png',xy,size)

def wrap(s,width,size=32):
    rows=[]; row=''
    f=font(size)
    for word in s.split():
        trial=(row+' '+word).strip()
        if f.getlength(trial)>width:
            rows.append(row);row=word
        else:row=trial
    if row:rows.append(row)
    return rows

def button(im,label,xy,width=320,state='idle'):
    frame(im,'button_'+state,xy,(width,72))
    text(im,(xy[0]+24,xy[1]+22),label,28)

def hud(im,room='Class B',show_location=True):
    frame(im,'day_time_plate',(64,48))
    text(im,(88,66),'APRIL 9  /  THURSDAY',24,bold=True)
    text(im,(88,102),'12:00 - 15:00  /  2 blocks left',22)
    for i,(icon,label) in enumerate([('map','Map'),('journal','Journal'),('pause','Menu')]):
        x=1512+i*112
        frame(im,'icon_button_idle',(x,48))
        frame(im,'icon_'+icon,(x+4,52))
        ImageDraw.Draw(im).rounded_rectangle((x-8,122,x+88,162),6,fill=PAPER)
        text(im,(x+4,130),label,22)
    if show_location:
        frame(im,'tooltip_panel',(64,918),(384,88))
        text(im,(88,950),room,28)

def save(im,name):
    im.convert('RGB').save(OUT/(name+'.jpg'),quality=93,subsampling=0)
    im.resize((1280,720),Image.Resampling.LANCZOS).convert('RGB').save(OUT/(name+'-1280.jpg'),quality=92)
    return dict(id=name,file=name+'.jpg',category='layout_proof',width=1920,height=1080)

def proofs():
    entries=[]
    a=bg('Title/title_school.png')
    ImageDraw.Draw(a).rounded_rectangle((64,72,690,1008),24,fill=PAPER+'E8')
    paste(a,'Title/wordmark_ink.png',(100,116),(540,178))
    text(a,(126,342),'A spring worth starting again.',28,MUTED)
    for i,label in enumerate(['New game','Continue','Load game','Gallery','Settings','Quit']):
        button(a,'Continue (no save yet)' if label=='Continue' else label,(126,438+i*82),500,'disabled' if label=='Continue' else 'idle')
    entries.append(save(a,'proof_title'))
    room=next(ART.glob('Rooms/seoyun/*library*.png'))
    a=bg(room.relative_to(ART));hud(a,'Library')
    frame(a,'hotspot_focus',(306,408),(112,112))
    frame(a,'tooltip_panel',(500,420),(384,88))
    text(a,(524,436),'Seo-yun',26,bold=True)
    text(a,(524,474),'Talk / 3 hours',22,MUTED)
    entries.append(save(a,'proof_exploration'))
    a=bg('Backgrounds/bg_class_b_day.png');hud(a,'Class B',False)
    # A standalone close portrait, rather than a mismatched face splice.
    paste(a,'Characters/katya/Expressions/annoyed.png',(1110,130),(690,690))
    frame(a,'dialogue_panel',(128,752))
    frame(a,'nameplate',(160,708))
    text(a,(190,727),'Katya',28,bold=True)
    lines=wrap('Most disasters begin with that sort of confidence.',1500)
    for i,line in enumerate(lines):text(a,(176,812+i*44),line,32)
    text(a,(180,964),'History     Auto     Skip     Hide     Save',24,MUTED)
    frame(a,'continue_marker',(1712,964))
    entries.append(save(a,'proof_dialogue'))
    # Actual choices from the finished screenplay.
    story=json.loads((ROOT/'Assets/AprilAgain/Narrative/katya.json').read_text(encoding='utf-8'))
    for i,ch in enumerate(story['scenes'][0]['choices']):
        frame(a,'choice_'+('focus' if i==0 else 'idle'),(128,294+i*106))
        for j,line in enumerate(wrap(ch['text'],908,28)):
            text(a,(168,316+i*106+j*34),line,28)
    entries.append(save(a,'proof_choices'))
    a=bg('Backgrounds/bg_bedroom_evening.png');hud(a,'Your room')
    frame(a,'menu_panel',(64,184))
    text(a,(104,230),'The day is yours to close.',34,serif=True)
    for i,label in enumerate(['Journal','Save game','Sleep / next day']):
        button(a,label,(104,338+i*102),530)
    text(a,(104,736),'Sleep starts the next day.',24,MUTED)
    text(a,(104,774),'Check your journal before sleeping.',24,MUTED)
    entries.append(save(a,'proof_bedroom'))
    for mode in ['save','settings','journal','gallery','pause','confirmation','backlog']:
        a=bg('Backgrounds/bg_bedroom_evening.png')
        shade=Image.new('RGBA',SIZES,(20,25,31,115));a.alpha_composite(shade)
        frame(a,'journal_panel',(256,124))
        text(a,(310,172),dict(save='Save game',settings='Settings',journal='Journal',gallery='Ending gallery',pause='Paused',confirmation='End this route?',backlog='Conversation history')[mode],46,serif=True)
        button(a,'Back',(1300,842))
        if mode=='save':
            for i in range(4):
                x=310+(i%2)*600;y=274+(i//2)*240
                frame(a,'save_slot',(x,y),(540,210))
                text(a,(x+28,y+24),f'Slot {i+1:02}',30,bold=True)
                text(a,(x+28,y+84),'April 9 / Library' if i==0 else 'Empty slot',28,MUTED)
                text(a,(x+28,y+136),'Manual save' if i==0 else 'Select to save here',24,MUTED)
        elif mode=='settings':
            for i,(label,value) in enumerate([('Master volume','80%'),('Music','60%'),('Text speed','Normal'),('Window mode','Borderless')]):
                y=286+i*100;text(a,(320,y),label,30)
                if i<2:
                    ratio=.8 if i==0 else .6
                    frame(a,'slider_track',(780,y+8),(470,18))
                    frame(a,'slider_fill',(780,y+8),(round(470*ratio),18))
                    frame(a,'slider_handle',(round(780+470*ratio-20),y-4))
                    text(a,(1320,y),value,28)
                else:
                    frame(a,'button_idle',(780,y-12),(470,72))
                    text(a,(804,y+8),value,28)
                    frame(a,'icon_next',(1196,y+4),(36,36))
            for i,label in enumerate(['Reduced motion','Stop skip at unread text']):
                frame(a,'checkbox_checked' if i else 'checkbox_empty',(320,704+i*66))
                text(a,(374,708+i*66),label,28)
        elif mode=='journal':
            for i,c in enumerate(['katya','akira','seoyun','mari','svea']):
                x=310+i*252
                paste(a,f'Characters/{c}/Expressions/neutral.png',(x,278),(220,220))
                text(a,(x,524),dict(katya='Katya',akira='Akira',seoyun='Seo-yun',mari='Mari',svea='Svea')[c],30,bold=True)
            text(a,(320,622),'Remember what she chose to share.',32,serif=True)
            text(a,(320,680),'Your notes show completed encounters and familiar places.',28,MUTED)
            text(a,(320,728),'Availability changes with the school routine.',28,MUTED)
        elif mode=='gallery':
            for i,c in enumerate(['katya','akira','seoyun']):
                for j,k in enumerate(['good','neutral','bad']):
                    x=320+i*420;y=268+j*170
                    paste(a,f'CG/cg_{c}_{k}.png',(x,y),(380,140))
            text(a,(320,806),'Reach an ending to add it to your gallery.',24,MUTED)
        elif mode=='pause':
            for i,label in enumerate(['Resume','Save game','Load game','Settings','Return to title']):
                button(a,label,(610,280+i*102),680)
        elif mode=='confirmation':
            for i,line in enumerate(['Finishing this conversation ends this playthrough.',
                                      'Your choices decide the ending.',
                                      'Make a save first if you want to return.']):
                text(a,(320,330+i*60),line,32)
            button(a,'Continue',(610,640),450)
            button(a,'Go back',(1120,640),450)
        else:
            for i,(speaker,line) in enumerate([('MC','I hoped nobody noticed.'),('Katya','Most disasters begin with that sort of confidence.'),('MC','I was about to invent a new filing system.')]):
                text(a,(320,300+i*155),speaker,28,MAROON,bold=True)
                text(a,(320,350+i*155),line,30)
        entries.append(save(a,'proof_'+mode))
    a=bg('Map/campus_illustration.png')
    # The labels are separate live layers in Unity; this is their rendered proof.
    m=json.loads((ART/'Map/map-layout.json').read_text(encoding='utf-8'))
    for p in m['locations']:
        x,y=p['labelPosition'];x=round(x*1920);y=round(y*1080)
        label=p['label'];w=math.ceil(font(26).getlength(label))+32
        ImageDraw.Draw(a).rounded_rectangle((x-w/2,y-22,x+w/2,y+30),8,fill=PAPER,outline='#D8CEC1',width=2)
        text(a,(round(x-w/2+16),y-10),label,26)
    entries.append(save(a,'proof_map'))
    return entries

def contact_sheets(manifest):
    assets=manifest['assets']
    for category in ['expressions','placement','wardrobe','background','background_variant','ending_cg','room_placement','prop_atlas','illustrated_pages','mc','map','title']:
        rows=[x for x in assets.values() if x['category']==category]
        if not rows:continue
        for start in range(0,len(rows),12):
            batch=rows[start:start+12];cols=3;cellw,cellh=520,360
            im=Image.new('RGB',(cols*cellw,math.ceil(len(batch)/cols)*cellh),PAPER)
            for i,a in enumerate(batch):
                src=load(a['file']);src.thumbnail((500,310),Image.Resampling.LANCZOS)
                x=(i%cols)*cellw+(cellw-src.width)//2;y=(i//cols)*cellh
                im.paste(src,(x,y),src)
                ImageDraw.Draw(im).text(((i%cols)*cellw+12,y+320),a['id'],font=font(18),fill=INK)
            im.save(OUT/f'contact-{category}-{start//12+1}.jpg',quality=94)
    # Inspect exported busts on paper with actual alpha, not misleading RGB fog.
    for c in ['katya','akira','seoyun','mari','svea']:
        rows=sorted((ART/'Characters'/c/'Expressions').glob('*.png'))
        im=Image.new('RGB',(1600,900),PAPER)
        for i,p in enumerate(rows):
            a=Image.open(p).convert('RGBA');a.thumbnail((390,390))
            x=(i%4)*400;y=(i//4)*450;im.paste(a,(x,y),a)
            ImageDraw.Draw(im).text((x+16,y+408),p.stem,font=font(24),fill=INK)
        im.save(OUT/f'expressions-{c}.jpg',quality=95)

def gallery(manifest,proofs):
    items=[]
    for a in manifest['assets'].values():
        items.append(dict(id=a['id'],category=a['category'],file='../../../Assets/AprilAgain/Art/'+a['file'],width=a['width'],height=a['height']))
    items+=proofs
    aud=json.loads((ROOT/'Assets/AprilAgain/Audio/audio-manifest.json').read_text(encoding='utf-8'))
    for a in aud['assets']:
        items.append(dict(id=a['id'],category='audio',file='../../../Assets/AprilAgain/Audio/'+a['file'],seconds=a['seconds']))
    html=r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>April, again / Asset review</title>
<style>@font-face{font-family:Source;src:url('../../../Assets/AprilAgain/Art/Fonts/SourceSans3-Regular.ttf')}@font-face{font-family:Serif;src:url('../../../Assets/AprilAgain/Art/Fonts/SourceSerif4-Regular.ttf')}*{box-sizing:border-box}body{margin:0;background:#f7f1e8;color:#263340;font:18px Source,sans-serif}header,nav,main{max-width:1500px;margin:auto;padding:24px 32px}header{padding-top:48px;border-bottom:1px solid #d8cec1}h1{font:52px Serif,serif;margin:0 0 8px}p{line-height:1.5;margin:8px 0}small{color:#66716e}nav{display:flex;flex-wrap:wrap;gap:10px;position:sticky;top:0;background:#f7f1e8;z-index:2}button,input,select{font:inherit;border:1px solid #b9b7ac;background:#fffaf3;color:inherit;padding:10px 16px;border-radius:5px}button{cursor:pointer}button:hover{background:#eee4d8}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #8f4d5b;outline-offset:3px}button[aria-pressed=true]{background:#8f4d5b;color:#fff}input{flex:1;min-width:180px}#count{margin:0 0 20px}#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:22px}.tile{text-align:left;padding:0;overflow:hidden;background:#fffaf3}.tile img{display:block;width:100%;height:230px;object-fit:contain;background:repeating-conic-gradient(#f7f1e8 0% 25%,#eae5dc 0% 50%) 50% / 20px 20px}.tile span{display:block;padding:12px;overflow-wrap:anywhere}.tile small{display:block;margin-top:5px}.tile audio{width:100%;padding:12px}dialog{width:min(1500px,96vw);max-height:96vh;border:1px solid #d8cec1;background:#f7f1e8;padding:20px;color:#263340}dialog::backdrop{background:#19232dde}dialog img{display:block;max-width:100%;max-height:76vh;margin:16px auto;object-fit:contain;background:repeating-conic-gradient(#f7f1e8 0% 25%,#eae5dc 0% 50%) 50% / 24px 24px}dialog h2{font:28px Source;margin:0;overflow-wrap:anywhere}.dialoghead{display:flex;justify-content:space-between;gap:16px}footer{padding:50px 32px;text-align:center;color:#66716e}@media(max-width:700px){h1{font-size:38px}header,nav,main{padding:20px}nav{position:static}.tile img{height:210px}}</style>
<header><h1>April, again</h1><p>Full-game production asset review</p><small>Illustrations, transparent sprites, scene bindings and interface components. Layout proofs are asset compositions; this page is not the playable Unity game.</small></header><nav><button data-cat="featured" aria-pressed="true">Overview</button><button data-cat="room_placement">In-room views</button><button data-cat="expressions">Expressions</button><button data-cat="character">Characters</button><button data-cat="wardrobe">Outfits</button><button data-cat="background">Locations</button><button data-cat="ending_cg">Endings</button><button data-cat="prop_atlas">Items</button><button data-cat="native_graphic">UI & documents</button><button data-cat="layout_proof">Screen proofs</button><button data-cat="audio">Audio</button><button data-cat="all">All files</button><input id="search" type="search" aria-label="Search assets" placeholder="Find a girl, room or item…"></nav><main><p id="count" aria-live="polite"></p><div id="grid"></div></main><dialog><div class="dialoghead"><h2 id="name"></h2><button id="close">Close</button></div><img id="large" alt=""><p id="meta"></p><a id="source">Open original file</a></dialog><footer>Original generation prompts and provenance: ../production-jobs.json · Exact scene coverage: ../asset-validation.json</footer><script>
const data=__DATA__;let cat='featured';const grid=document.getElementById('grid'),dialog=document.querySelector('dialog');
const featured=['room_katya_class_b_school_uniform','room_akira_class_a_school_uniform','room_seoyun_library_school_uniform','room_mari_infirmary_school_uniform','room_svea_field_school_uniform','map_campus','proof_title','proof_exploration','proof_dialogue','proof_choices'];
function render(){const q=document.getElementById('search').value.toLowerCase();const rows=data.filter(a=>(cat==='all'||(cat==='featured'?featured.includes(a.id):a.category===cat||(cat==='background'&&a.category==='background_variant')))&&a.id.toLowerCase().includes(q));document.getElementById('count').textContent=rows.length+' assets shown';grid.replaceChildren();for(const a of rows){const el=document.createElement(a.category==='audio'?'article':'button');el.className='tile';if(a.category==='audio'){const au=document.createElement('audio');au.controls=true;au.preload='none';au.src=a.file;au.setAttribute('aria-label',a.id);el.append(au)}else{const im=document.createElement('img');im.src=a.file;im.alt=a.id.replaceAll('_',' ');im.loading='lazy';el.append(im);el.onclick=()=>{document.getElementById('name').textContent=a.id;document.getElementById('large').src=a.file;document.getElementById('large').alt=im.alt;document.getElementById('meta').textContent=a.width+' × '+a.height+' pixels / '+a.category;document.getElementById('source').href=a.file;dialog.showModal()}}const label=document.createElement('span');label.textContent=a.id;const sub=document.createElement('small');sub.textContent=a.category==='audio'?a.seconds+' seconds':a.width+' × '+a.height+' / '+a.category;label.append(sub);el.append(label);grid.append(el)}}
document.querySelectorAll('[data-cat]').forEach(b=>b.onclick=()=>{cat=b.dataset.cat;document.querySelectorAll('[data-cat]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render()});document.getElementById('search').oninput=render;document.getElementById('close').onclick=()=>dialog.close();render();
</script></html>'''
    (OUT/'index.html').write_text(html.replace('__DATA__',json.dumps(items)),encoding='utf-8')

if __name__=='__main__':
    manifest=json.loads((ART/'asset-manifest.json').read_text(encoding='utf-8'))
    p=proofs();contact_sheets(manifest);gallery(manifest,p)
    (OUT/'layout-proofs.json').write_text(json.dumps(p,indent=2),encoding='utf-8')
    print(f'Rendered {len(p)} full-HD screen proofs, 1280px checks, contact sheets and offline gallery.')
