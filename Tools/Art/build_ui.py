"""Author the game's editable vector UI and matching transparent raster exports.

Only interface geometry is drawn here. Character/background/CG illustrations
are generated separately. Run with the Codex bundled Python (Pillow required).
"""
from pathlib import Path
from html import escape
import json
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Assets/AprilAgain/Art/UI"
P = dict(paper="#F7F1E8", ink="#263340", maroon="#8F4D5B", muted="#66716E",
         sage="#8C9B8D", brass="#B8A17A", line="#D8CEC1", white="#FFFFFF")
CATALOG = []


class Art:
    def __init__(self, name, width, height, border=None):
        self.name, self.size, self.border = name, (width, height), border
        self.image = Image.new("RGBA", (width * 2, height * 2))
        self.draw = ImageDraw.Draw(self.image)
        self.svg = []

    def rect(self, xy, fill, stroke=None, weight=1, radius=0):
        x, y, w, h = xy
        coords = (x * 2, y * 2, (x + w) * 2, (y + h) * 2)
        self.draw.rounded_rectangle(coords, radius * 2, fill, stroke, weight * 2)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{weight}"/>')

    def line(self, points, color, weight=2):
        self.draw.line([(x * 2, y * 2) for x, y in points], fill=color, width=weight * 2, joint="curve")
        pts = " ".join(f"{x},{y}" for x, y in points)
        self.svg.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{weight}" stroke-linecap="round" stroke-linejoin="round"/>')

    def poly(self, points, color):
        self.draw.polygon([(x * 2, y * 2) for x, y in points], fill=color)
        pts = " ".join(f"{x},{y}" for x, y in points)
        self.svg.append(f'<polygon points="{pts}" fill="{color}"/>')

    def ellipse(self, xy, fill=None, stroke=None, weight=2):
        x, y, w, h = xy
        self.draw.ellipse((x * 2, y * 2, (x + w) * 2, (y + h) * 2), fill=fill, outline=stroke, width=weight * 2)
        self.svg.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{weight}"/>')

    def save(self):
        OUT.mkdir(parents=True, exist_ok=True)
        self.image.resize(self.size, Image.Resampling.LANCZOS).save(OUT / f"{self.name}.png")
        w, h = self.size
        (OUT / f"{self.name}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + "".join(self.svg) + "</svg>\n", encoding="utf-8")
        CATALOG.append(dict(id=self.name, file=f"UI/{self.name}.png", source=f"UI/{self.name}.svg", width=w, height=h, border=self.border))


def panels():
    for name, size, border in [
        ("dialogue_panel", (1664, 272), [24, 24, 24, 24]),
        ("modal_panel", (960, 560), [24, 24, 24, 24]),
        ("menu_panel", (640, 880), [24, 24, 24, 24]),
        ("journal_panel", (1408, 832), [24, 24, 24, 24]),
        ("save_slot", (520, 288), [16, 16, 16, 16]),
        ("tooltip_panel", (384, 88), [12, 12, 12, 12]),
        ("day_time_plate", (400, 96), [16, 16, 16, 16]),
        ("nameplate", (360, 64), [16, 16, 16, 16]),
    ]:
        w, h = size
        a = Art(name, w, h, border)
        a.rect((2, 2, w - 5, h - 5), P["paper"], P["line"], 2, 10)
        a.line([(24, 4), (w - 24, 4)], P["brass"], 2)
        if name == "dialogue_panel":
            a.rect((28, 30, 5, 36), P["maroon"])
        a.save()


def controls():
    states = {"idle": (P["paper"], P["line"]), "hover": ("#EEE2DC", P["maroon"]),
              "pressed": ("#E0CCC5", P["maroon"]), "disabled": ("#E3DFD8", "#B8B4AD"),
              "focus": (P["paper"], P["maroon"])}
    for state, (fill, edge) in states.items():
        for family, size in [("choice", (1008, 88)), ("button", (320, 72)), ("icon_button", (72, 72)), ("tab", (240, 64))]:
            w, h = size
            a = Art(f"{family}_{state}", w, h, [14, 14, 14, 14])
            a.rect((3, 3, w - 7, h - 7), fill, edge, 3 if state == "focus" else 2, 7)
            if state == "hover":
                a.rect((13, h // 2 - 10, 3, 20), P["maroon"])
            a.save()
    for checked in (False, True):
        a = Art("checkbox_" + ("checked" if checked else "empty"), 48, 48)
        a.rect((6, 6, 35, 35), P["paper"], P["maroon"] if checked else P["muted"], 2, 4)
        if checked:
            a.line([(13, 24), (21, 32), (35, 15)], P["maroon"], 4)
        a.save()
    for name, fill, size in [("slider_track", P["line"], (384, 8)), ("slider_fill", P["maroon"], (384, 8)),
                             ("scroll_track", P["line"], (8, 384)), ("scroll_thumb", P["muted"], (8, 96))]:
        a = Art(name, *size, [3, 3, 3, 3]); a.rect((0, 0, size[0] - 1, size[1] - 1), fill, radius=3); a.save()
    a = Art("slider_handle", 40, 40); a.ellipse((5, 5, 29, 29), P["paper"], P["maroon"], 3); a.save()
    for state, color in [("available", P["maroon"]), ("visited", P["sage"]), ("unavailable", P["muted"]), ("focus", P["ink"])]:
        a = Art(f"hotspot_{state}", 80, 80)
        for pts in [[(8, 26), (8, 8), (26, 8)], [(54, 8), (72, 8), (72, 26)],
                    [(8, 54), (8, 72), (26, 72)], [(54, 72), (72, 72), (72, 54)]]:
            a.line(pts, color, 3)
        if state == "visited": a.line([(24, 41), (35, 52), (57, 28)], color, 4)
        elif state == "unavailable": a.line([(25, 40), (55, 40)], color, 4)
        else: a.ellipse((33, 33, 14, 14), color)
        a.save()
    for name, color in [("slot_open", P["paper"]), ("slot_used", P["sage"])]:
        a = Art(name, 28, 28); a.ellipse((3, 3, 21, 21), color, P["muted"], 2); a.save()


def icons():
    # Original simple line icons, kept in one 64 px system; no external icon dependency.
    geometry = {
        "map": [[(10, 16), (24, 10), (40, 16), (54, 10), (54, 48), (40, 54), (24, 48), (10, 54), (10, 16)], [(24, 10), (24, 48)], [(40, 16), (40, 54)]],
        "journal": [[(14, 10), (48, 10), (48, 54), (14, 54), (14, 10)], [(21, 10), (21, 54)], [(28, 23), (40, 23)], [(28, 33), (40, 33)]],
        "home": [[(8, 29), (32, 10), (56, 29)], [(15, 25), (15, 54), (49, 54), (49, 25)], [(27, 54), (27, 37), (38, 37), (38, 54)]],
        "door": [[(16, 54), (16, 10), (49, 10), (49, 54)], [(22, 54), (22, 15), (43, 19), (43, 54)], [(34, 35), (37, 35)]],
        "back": [[(32, 14), (14, 32), (32, 50)], [(15, 32), (54, 32)]],
        "next": [[(26, 14), (44, 32), (26, 50)]],
        "close": [[(16, 16), (48, 48)], [(48, 16), (16, 48)]],
        "pause": [[(23, 14), (23, 50)], [(41, 14), (41, 50)]],
        "play": [[(22, 13), (49, 32), (22, 51), (22, 13)]],
        "skip": [[(12, 16), (30, 32), (12, 48), (12, 16)], [(33, 16), (51, 32), (33, 48), (33, 16)]],
        "save": [[(12, 10), (46, 10), (54, 18), (54, 54), (12, 54), (12, 10)], [(21, 10), (21, 26), (43, 26), (43, 10)], [(22, 54), (22, 37), (44, 37), (44, 54)]],
        "load": [[(12, 42), (12, 54), (52, 54), (52, 42)], [(32, 9), (32, 41)], [(20, 29), (32, 41), (44, 29)]],
        "history": [[(11, 28), (11, 12), (27, 12)], [(11, 12), (18, 8), (43, 8), (55, 23), (55, 43), (43, 55), (23, 55), (12, 45)], [(33, 17), (33, 33), (44, 39)]],
        "gallery": [[(10, 12), (54, 12), (54, 52), (10, 52), (10, 12)], [(12, 45), (25, 31), (35, 41), (42, 34), (53, 46)]],
        "calendar": [[(12, 16), (52, 16), (52, 54), (12, 54), (12, 16)], [(12, 27), (52, 27)], [(22, 9), (22, 22)], [(42, 9), (42, 22)]],
        "clock": [[(32, 16), (32, 33), (44, 39)]],
        "sleep": [[(46, 11), (35, 13), (27, 22), (27, 35), (36, 44), (49, 45), (41, 53), (25, 53), (13, 42), (11, 27), (19, 15), (32, 9), (46, 11)]],
        "volume": [[(10, 26), (22, 26), (35, 14), (35, 50), (22, 38), (10, 38), (10, 26)], [(43, 23), (48, 32), (43, 41)], [(50, 15), (57, 32), (50, 49)]],
        "check": [[(13, 33), (26, 46), (52, 18)]],
        "lock": [[(15, 29), (49, 29), (49, 54), (15, 54), (15, 29)], [(22, 29), (22, 17), (27, 11), (37, 11), (42, 17), (42, 29)]],
        "info": [[(32, 28), (32, 47)]],
        "wait": [[(16, 10), (48, 10)], [(16, 54), (48, 54)], [(20, 10), (20, 21), (44, 43), (44, 54)], [(44, 10), (44, 21), (20, 43), (20, 54)]],
        "classroom": [[(9, 13), (55, 13), (55, 42), (9, 42), (9, 13)], [(23, 42), (20, 55)], [(41, 42), (44, 55)], [(19, 24), (43, 24)]],
        "library": [[(12, 12), (23, 12), (23, 53), (12, 53), (12, 12)], [(28, 9), (39, 9), (39, 53), (28, 53), (28, 9)], [(43, 15), (51, 13), (59, 51), (50, 53), (43, 15)]],
        "infirmary": [[(25, 10), (39, 10), (39, 25), (54, 25), (54, 39), (39, 39), (39, 54), (25, 54), (25, 39), (10, 39), (10, 25), (25, 25), (25, 10)]],
        "canteen": [[(14, 11), (14, 29), (24, 29), (24, 11)], [(19, 11), (19, 53)], [(48, 11), (39, 22), (39, 31), (48, 31), (48, 53)], [(48, 11), (48, 31)]],
        "field": [[(8, 14), (56, 14), (56, 50), (8, 50), (8, 14)], [(32, 14), (32, 50)], [(8, 24), (18, 24), (18, 40), (8, 40)], [(56, 24), (46, 24), (46, 40), (56, 40)]],
    }
    for name, lines in geometry.items():
        a = Art(f"icon_{name}", 64, 64)
        for points in lines: a.line(points, P["ink"], 3)
        if name in ("clock", "info"): a.ellipse((8, 8, 48, 48), stroke=P["ink"], weight=3)
        if name == "info": a.ellipse((29, 17, 6, 6), P["ink"])
        if name == "gallery": a.ellipse((37, 20, 7, 7), stroke=P["ink"], weight=2)
        a.save()
    a = Art("cursor_pointer", 40, 48)
    a.poly([(6, 4), (6, 36), (15, 28), (23, 43), (29, 40), (21, 25), (33, 25)], P["paper"])
    a.line([(6, 4), (6, 36), (15, 28), (23, 43), (29, 40), (21, 25), (33, 25), (6, 4)], P["ink"], 2); a.save()
    a = Art("continue_marker", 32, 24); a.poly([(6, 6), (26, 6), (16, 18)], P["maroon"]); a.save()


def main():
    panels(); controls(); icons()
    theme = {"referenceCanvas": [1920, 1080], "safeMargin": 64, "colors": P,
             "type": {"body": 32, "speaker": 28, "hud": 24, "metadata": 22, "bodyFont": "Fonts/SourceSans3-Regular.ttf", "emphasisFont": "Fonts/SourceSans3-Semibold.ttf", "displayFont": "Fonts/SourceSerif4-Regular.ttf", "italicFont": "Fonts/SourceSerif4-It.ttf"},
             "dialogueRectTopLeft": [128, 752, 1664, 272], "minimumTarget": 56,
             "textBakedIntoArt": False, "borderOrder": "left,bottom,right,top",
             "assets": CATALOG}
    (OUT / "ui-theme.json").write_text(json.dumps(theme, indent=2), encoding="utf-8")
    for item in CATALOG:
        path = OUT / (item["id"] + ".png")
        with Image.open(path) as image:
            assert image.size == (item["width"], item["height"])
            assert image.mode == "RGBA"
            assert image.getextrema()[3][0] == 0, path
        assert (OUT / (item["id"] + ".svg")).exists()
    assert len({item["id"] for item in CATALOG}) == len(CATALOG)
    print(f"Verified {len(CATALOG)} transparent UI PNGs, matching SVG sources and ui-theme.json.")


if __name__ == "__main__":
    main()
