"""Read the supplied documents without modifying them; preserve provenance locally."""
from pathlib import Path
import json
import zipfile
import xml.etree.ElementTree as ET
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(r"C:\Users\media\Downloads\Gameprog data")
DEST = ROOT / "Documentation/SourceNotes"


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    inventory = []
    for path in sorted(SOURCE.iterdir()):
        if path.suffix.lower() == ".pdf":
            reader = PdfReader(path)
            sections = [f"# {path.name}", f"Source: {path}"]
            for index, page in enumerate(reader.pages, 1):
                # Some supplied PDFs put every word on a separate extracted line.
                sections.append(f"\n## Page {index}\n\n" + " ".join((page.extract_text() or "").split()))
            pages = len(reader.pages)
        elif path.suffix.lower() == ".docx":
            with zipfile.ZipFile(path) as archive:
                root = ET.fromstring(archive.read("word/document.xml"))
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            paragraphs = ["".join(t.text or "" for t in p.findall(".//w:t", ns)) for p in root.findall(".//w:p", ns)]
            sections = [f"# {path.name}", f"Source: {path}", *paragraphs]
            pages = None
        else:
            continue
        output = DEST / (path.stem + ".md")
        output.write_text("\n\n".join(sections), encoding="utf-8")
        inventory.append({"source": str(path), "notes": str(output.relative_to(ROOT)), "pdf_pages": pages})
    assert len(inventory) == 5, "Expected all five supplied character profiles"
    assert sum(x["pdf_pages"] or 0 for x in inventory) == 14
    (DEST / "sources.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Read and preserved all five profiles; 14 PDF pages plus one DOCX.")


if __name__ == "__main__":
    main()
