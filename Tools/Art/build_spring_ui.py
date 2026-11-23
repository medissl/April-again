"""Preserve generated UI masters and mechanically export their atlas cells."""
import hashlib
import json
import shutil
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
SOURCE=Path('C:/Users/media/.codex/generated_images/01a202a7-4f19-7883-b523-cefe2a4903b6')
OUT=ROOT/'Assets/AprilAgain/Art/UI/Spring'
DOC=ROOT/'Documentation/Art/SpringUI'
JOBS={'concept':'exec-5c17f7d2-9db4-4b4c-91a1-e1f26df1e1b8.png',
      'components':'exec-910804c9-38c5-4b10-8822-23216a92d930.png',
      'menu':'exec-5a72801b-382c-4115-9408-96beb7ba0416.png',
      'wordmark':'exec-7c2a7f1f-de41-426e-82dc-0cb4428669a9.png',
      'calendar':'exec-c890f9cc-8d3f-46cd-8ddc-9e31317d62ce.png'}

def trim(im):
    # Bounds only: preserve source pixels/alpha, including antialiased edges.
    b=im.getchannel('A').point(lambda v:255 if v>16 else 0).getbbox()
    x,y,r,bottom=b
    return im.crop((max(0,x-6),max(0,y-6),min(im.width,r+6),min(im.height,bottom+6)))

def main():
    OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
    for key,name in JOBS.items():shutil.copy2(SOURCE/name,DOC/(key+'-master.png'))
    sheet=Image.open(DOC/'components-master.png').convert('RGBA')
    names=['spring_dialogue','spring_name','spring_choice','spring_choice_hover','spring_date','spring_button']
    borders=[[64,145,165,22],[140,25,70,25],[70,30,55,30],[70,30,55,30],[0,0,0,0],[55,45,90,45]]
    records=[]
    def export(name,im,border):
        file=OUT/(name+'.png');im.save(file)
        records.append(dict(id=name,path=file.relative_to(ROOT).as_posix(),file=file.relative_to(ROOT/'Assets/AprilAgain/Art').as_posix(),
            width=im.width,height=im.height,border=border,category='generated_ui',method='built-in image_gen; mechanical alpha-bounds atlas crop',
            sha256=hashlib.sha256(file.read_bytes()).hexdigest(),rect=[0,0,1,1]))
    for i,name in enumerate(names):
        col=i%2;row=i//2
        export(name,trim(sheet.crop((col*sheet.width//2,row*sheet.height//3,(col+1)*sheet.width//2,(row+1)*sheet.height//3))),borders[i])
    export('spring_menu',trim(Image.open(DOC/'menu-master.png').convert('RGBA')),[150,200,150,150])
    export('spring_wordmark',trim(Image.open(DOC/'wordmark-master.png').convert('RGBA')),[0,0,0,0])
    calendar=trim(Image.open(DOC/'calendar-master.png').convert('RGBA'))
    calendar=calendar.resize((480,round(calendar.height*480/calendar.width)),Image.Resampling.LANCZOS)
    export('spring_calendar',calendar,[12,20,96,12])
    # Reuse the project's original editable icon geometry, with white ink so the
    # engine can tint the same consistent line system for each surface.
    import build_ui
    build_ui.OUT=OUT/'Icons';build_ui.P['ink']='#FFFFFF';build_ui.CATALOG=[];build_ui.icons()
    knob=build_ui.Art('slider_knob',64,64);knob.ellipse((3,3,58,58),'#FFFFFF');knob.save()
    eye=build_ui.Art('icon_inspect',64,64);eye.ellipse((8,8,34,34),stroke='#FFFFFF',weight=3);eye.line([(38,38),(55,55)],'#FFFFFF',3);eye.save()
    menu=build_ui.Art('icon_menu',64,64)
    for y in [16,32,48]:menu.line([(12,y),(52,y)],'#FFFFFF',4)
    menu.save()
    chat=build_ui.Art('icon_chat',64,64)
    chat.line([(17,12),(47,12),(56,21),(56,36),(47,45),(29,45),(16,55),(18,44),(8,36),(8,21),(17,12)],'#FFFFFF',3)
    for x in [21,32,43]:chat.ellipse((x-2,26,4,4),'#FFFFFF')
    chat.save()
    upload=build_ui.Art('icon_upload',64,64)
    upload.line([(12,42),(12,54),(52,54),(52,42)],'#FFFFFF',3)
    upload.line([(32,41),(32,9),(20,21)],'#FFFFFF',3);upload.line([(32,9),(44,21)],'#FFFFFF',3);upload.save()
    import math
    gear=build_ui.Art('icon_settings',64,64);outline=[]
    for i in range(64):
        angle=2*math.pi*i/64;radius=26 if i%8 in [1,2,3,4] else 21
        outline.append((32+math.cos(angle)*radius,32+math.sin(angle)*radius))
    gear.line(outline+[outline[0]],'#FFFFFF',3);gear.ellipse((22,22,20,20),stroke='#FFFFFF',weight=3);gear.save()
    for a in build_ui.CATALOG:
        file=build_ui.OUT/(a['id']+'.png')
        records.append(dict(id='spring_'+a['id'],path=file.relative_to(ROOT).as_posix(),
            file=file.relative_to(ROOT/'Assets/AprilAgain/Art').as_posix(),width=a['width'],height=a['height'],
            border=[0,0,0,0],category='native_ui_icon',method='original project vector geometry, white-ink export',
            sha256=hashlib.sha256(file.read_bytes()).hexdigest(),rect=[0,0,1,1]))
    (OUT/'spring-manifest.json').write_text(json.dumps(dict(assets=records,sourceMasters=JOBS),indent=2),encoding='utf-8')
    # A review composite demonstrates actual straight alpha, not hidden source RGB.
    review=Image.new('RGBA',(1600,1050),'#e7e0dc')
    for i,a in enumerate(records[:6]):
        im=Image.open(ROOT/a['path']).convert('RGBA');im.thumbnail((740,290))
        review.alpha_composite(im,((i%2)*800+30,(i//2)*350+35))
    review.convert('RGB').save(DOC/'components-review.jpg',quality=94)
    print(f'Exported 9 generated spring UI sprites and {len(records)-9} original vector icons; preserved {len(JOBS)} masters.')

if __name__=='__main__':main()
