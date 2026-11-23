"""Contact sheets from real camera captures; no regenerated/mock UI."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[2]
mirror=Path((ROOT/'Documentation/Testing/build-mirror-path.txt').read_text().strip())
src=mirror/'Documentation/Testing/Production'
out=ROOT/'Documentation/Testing/ProductionReview';out.mkdir(exist_ok=True)
font=ImageFont.truetype(str(ROOT/'Assets/AprilAgain/Art/Fonts/Nunito/Nunito-ExtraBold.ttf'),14)
groups={
 'menus':[p for p in sorted(src.glob('*-1080.jpg')) if not p.name.startswith(('bg_','room_','observation_')) and not any(x in p.name for x in ['-dialogue','-choices','.ending.'])],
 'world':[p for p in sorted(src.glob('*-1080.jpg')) if p.name.startswith(('bg_','room_','observation_'))],
 'cg':[p for p in sorted(src.glob('*.ending.*-1080.jpg')) if '-credits' not in p.name],
 'credits':list(sorted(src.glob('*-credits-1080.jpg'))),
 'dialogue':list(sorted(src.glob('*-dialogue-1080.jpg'))),
 'choices':list(sorted(src.glob('*-choices-1080.jpg'))),
 'hovers':list(sorted(src.glob('*hover*-720.jpg'))),
}
for group,files in groups.items():
 for start in range(0,len(files),8):
  board=Image.new('RGB',(1600,960),'#eee4e8');d=ImageDraw.Draw(board)
  for i,p in enumerate(files[start:start+8]):
   im=Image.open(p).convert('RGB');im.thumbnail((800,450))
   # Four half-scale frames: legible enough to find misplaced geometry.
   if i>=4:break
   x=(i%2)*800;y=(i//2)*480;board.paste(im,(x,y));d.text((x+5,y+453),p.stem,font=font,fill='#6e3c50')
  board.save(out/f'{group}-{start//8+1:02d}-a.jpg',quality=94)
  if len(files[start:start+8])>4:
   board=Image.new('RGB',(1600,960),'#eee4e8');d=ImageDraw.Draw(board)
   for i,p in enumerate(files[start+4:start+8]):
    im=Image.open(p).convert('RGB');im.thumbnail((800,450));x=(i%2)*800;y=(i//2)*480
    board.paste(im,(x,y));d.text((x+5,y+453),p.stem,font=font,fill='#6e3c50')
   board.save(out/f'{group}-{start//8+1:02d}-b.jpg',quality=94)
print({k:len(v) for k,v in groups.items()})
