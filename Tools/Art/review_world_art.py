"""Mechanical contact sheets for inspecting every location/room illustration."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[2]
data=json.loads((ROOT/'Assets/AprilAgain/GameData/content.json').read_text(encoding='utf-8'))
assets=[a for a in data['assets'] if a['id'].startswith(('bg_','room_','observation_'))]
out=ROOT/'Documentation/Testing/WorldArtReview';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype(str(ROOT/'Assets/AprilAgain/Art/Fonts/Nunito/Nunito-ExtraBold.ttf'),15)
for start in range(0,len(assets),8):
    board=Image.new('RGB',(1600,516),'#efe4e8');draw=ImageDraw.Draw(board)
    for i,a in enumerate(assets[start:start+8]):
        im=Image.open(ROOT/a['path']).convert('RGB');im.thumbnail((400,225))
        x=(i%4)*400;y=(i//4)*258
        board.paste(im,(x,y));draw.text((x+5,y+229),a['id'],font=font,fill='#6e3c50')
    board.save(out/f'world-{start//8+1:02d}.jpg',quality=95)
(out/'index.json').write_text(json.dumps(assets,indent=2))
print(f'{len(assets)} world illustrations in {(len(assets)+7)//8} review sheets.')
