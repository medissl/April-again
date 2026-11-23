"""Original editable UI geometry: clean buttons, tags and the game monogram."""
import json,hashlib
from pathlib import Path
from html import escape
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'Assets/AprilAgain/Art/UI/Final';OUT.mkdir(parents=True,exist_ok=True)
INK='#6E3C50';PAPER='#FFF7F2';ROSE='#B9426C';EDGE='#CF8AA6'
assets=[]
for name,w,h,fill,stroke,radius in [
    ('final_button',320,72,PAPER,EDGE,12),
    ('final_button_primary',320,72,ROSE,'#A6335C',12),
    ('final_choice',960,126,PAPER,EDGE,14),
    ('final_map_label',220,48,PAPER,EDGE,8),
    ('final_map_current',220,48,'#F3D6E2',ROSE,8),
    ('final_tooltip',320,56,PAPER,EDGE,10),
]:
    im=Image.new('RGBA',(w*3,h*3));d=ImageDraw.Draw(im)
    d.rounded_rectangle((3,3,w*3-4,h*3-4),radius=radius*3,fill=fill,outline=stroke,width=4)
    im=im.resize((w,h),Image.Resampling.LANCZOS);path=OUT/(name+'.png');im.save(path)
    (OUT/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/></svg>')
    assets.append(dict(id=name,path=path.relative_to(ROOT).as_posix(),rect=[0,0,1,1],border=[16,16,16,16],width=w,height=h,
        method='Original editable vector interface geometry',sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
(OUT/'final-ui-manifest.json').write_text(json.dumps(dict(assets=assets),indent=2))
icon=Image.new('RGBA',(1024,1024));d=ImageDraw.Draw(icon)
d.rounded_rectangle((12,12,1012,1012),radius=220,fill=ROSE)
font=ImageFont.truetype(str(ROOT/'Assets/AprilAgain/Art/Fonts/Nunito/Nunito-ExtraBold.ttf'),810)
box=d.textbbox((0,0),'A',font=font)
d.text((512-(box[2]-box[0])/2-box[0],492-(box[3]-box[1])/2-box[1]),'A',font=font,fill=PAPER)
icon=icon.resize((512,512),Image.Resampling.LANCZOS)
icon.save(ROOT/'Assets/AprilAgain/Art/Title/app_icon_final.png')
icon.save(ROOT/'Assets/AprilAgain/Art/Title/app_icon_final.ico',sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
print('Built six clean UI sprites with SVG sources and the 512px game icon.')
