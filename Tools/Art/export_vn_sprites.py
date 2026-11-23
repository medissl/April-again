"""Export aligned waist-up conversation sprites from generated 2x2 sheets."""
import json
import shutil
import hashlib
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
DOC=ROOT/'Documentation/Art/ConversationSprites'
OUT=ROOT/'Assets/AprilAgain/Art/Characters'
SOURCE=Path('C:/Users/media/.codex/generated_images/01a202a7-4f19-7883-b523-cefe2a4903b6')
JOBS=[
 dict(girl='katya',faces=['neutral','soft_smile','annoyed','flustered'],source='exec-ad9504f8-d0ab-4689-849a-1c9922dc4384.png'),
 dict(girl='akira',faces=['neutral','delighted','excited','flustered'],source='exec-fdbe91dc-1aa6-40ae-af94-19e32a85f8c4.png'),
 dict(girl='seoyun',faces=['neutral','warm','curious','flustered'],source='exec-3930723a-5421-4322-81d6-adaf013f09e8.png'),
]

def main():
    DOC.mkdir(parents=True,exist_ok=True);assets=[]
    extra=DOC/'additional-jobs.json'
    jobs=JOBS+(json.loads(extra.read_text()) if extra.exists() else [])
    for j in jobs:
        src=SOURCE/j['source'];shutil.copy2(src,DOC/j['source'])
        sheet=Image.open(src).convert('RGBA');folder=OUT/j['girl']/'Conversation';folder.mkdir(exist_ok=True)
        for i,face in enumerate(j['faces']):
            columns=j.get('columns',2);rows=j.get('rows',2)
            x=(i%columns)*sheet.width//columns;y=(i//columns)*sheet.height//rows
            # Crop below the waist consistently; the dialogue window hides the
            # lower edge. The original full sheet remains available for review.
            cell=sheet.crop((x,y,x+sheet.width//columns,y+int(sheet.height/rows*.81)))
            file=folder/(face+'.png');cell.save(file)
            assets.append(dict(id=f"vn_{j['girl']}_{face}",path=file.relative_to(ROOT).as_posix(),
                rect=[0,0,1,1],border=[0,0,0,0],width=cell.width,height=cell.height,
                method='built-in image_gen; aligned mechanical atlas crop',sha256=hashlib.sha256(file.read_bytes()).hexdigest()))
    (DOC/'conversation-manifest.json').write_text(json.dumps(dict(assets=assets,jobs=jobs),indent=2))
    print(f'Exported {len(assets)} aligned conversation sprites from {len(jobs)} masters.')

if __name__=='__main__':main()
