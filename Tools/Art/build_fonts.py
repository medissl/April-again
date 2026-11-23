"""Pin the approved Nunito weights as static TTFs for Unity/TMP."""
import hashlib
import json
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / 'Assets/AprilAgain/Art/Fonts/Nunito'
source = FOLDER / 'Nunito-Variable.ttf'
for name, weight in [('SemiBold', 600), ('ExtraBold', 800)]:
    font = instantiateVariableFont(TTFont(source), {'wght': weight}, inplace=True)
    font.save(FOLDER / f'Nunito-{name}.ttf')
(FOLDER / 'font-sources.json').write_text(json.dumps({
    'family': 'Nunito', 'license': 'SIL Open Font License 1.1; see OFL.txt',
    'source': 'https://raw.githubusercontent.com/google/fonts/main/ofl/nunito/Nunito%5Bwght%5D.ttf',
    'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'process': 'FontTools 4.68.0 static instances, wght 600 and 800; no outline edits',
    'weights': {'game_default': 800, 'archived_comparison': 600}
}, indent=2), encoding='utf-8')
print('Built Nunito SemiBold and ExtraBold static TTFs.')
