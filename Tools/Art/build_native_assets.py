"""Author original interface/document graphics; never draw character illustrations.

PNG exports match editable SVG sources. Fonts are unmodified OFL distributions.
Run before assemble_assets.py. All coordinates are pixels with a top-left origin.
"""
from pathlib import Path
from html import escape
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'Assets/AprilAgain/Art'
FONT = ART / 'Fonts'
INK, PAPER, ACCENT, MUTED, LINE = '#263340', '#F7F1E8', '#8F4D5B', '#66716E', '#D8CEC1'
CAT = []


class Canvas:
    def __init__(self, name, size, background=None):
        self.name, self.size = name, size
        self.im = Image.new('RGBA', size, background)
        self.d = ImageDraw.Draw(self.im)
        self.parts = []
        if background:
            self.rect((0, 0, *size), background)

    def rect(self, box, color, outline=None, width=2, radius=0):
        x, y, w, h = box
        self.d.rounded_rectangle((x, y, x+w, y+h), radius, color, outline, width)
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{color or "none"}" stroke="{outline or "none"}" stroke-width="{width}"/>')

    def line(self, xy, color=LINE, width=2):
        self.d.line(xy, fill=color, width=width)
        pts = ' '.join(f'{x},{y}' for x, y in xy)
        self.parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    def text(self, xy, text, size=26, color=INK, serif=False, bold=False):
        fn = 'SourceSerif4-Regular.ttf' if serif else ('SourceSans3-Semibold.ttf' if bold else 'SourceSans3-Regular.ttf')
        font = ImageFont.truetype(str(FONT / fn), size)
        self.d.text(xy, text, fill=color, font=font, anchor='lt')
        family = 'Source Serif 4' if serif else 'Source Sans 3'
        self.parts.append(f'<text x="{xy[0]}" y="{xy[1]}" dominant-baseline="text-before-edge" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{600 if bold else 400}">{escape(text)}</text>')

    def save(self):
        dest = ART / self.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        self.im.save(dest.with_suffix('.png'))
        w, h = self.size
        dest.with_suffix('.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + ''.join(self.parts) + '</svg>\n', encoding='utf-8')
        CAT.append(dict(id=dest.stem, file=self.name+'.png', source=self.name+'.svg', width=w, height=h, method='original editable vector graphic'))


# Paper graphics are inspection layers. Their wording is available separately
# for accessible live text; no generated gibberish is used in the illustrations.
DOCUMENTS = {
 'backing_card': ('Display backing', ['Library-window project', 'Cut to fit the agreed layout.', 'Check the edges before mounting.']),
 'budget_sheet': ('Display budget', ['Paper and backing card', 'Printing and labels', 'Check the school supply list first.']),
 'class_register': ('Class register', ['Class B / first-year project', 'Room labels checked', 'Return this copy to the teacher.']),
 'committee_notes': ('Committee notes', ['Confirm the room signs.', 'Keep the doorway clear.', 'Check captions before printing.']),
 'final_report': ('Project record', ['First-year display committee', 'Materials checked and returned', 'Prepared by: Katya / Classmate']),
 'forms': ('Information table', ['Seiran High School', 'First-year activity information', 'Please return completed forms to staff.']),
 'music_note': ('A song to remember', ['A small note about a song.', 'Some things are easier to write down.']),
 'paper_labels': ('Display labels', ['Room / subject / author', 'Check each label against the register.']),
 'paper_samples': ('Paper samples', ['Cream / white / pale blue', 'Compare under ordinary daylight.']),
 'receipt': ('School supply receipt', ['Paid from the school project budget.', 'Check the box against the supply list.']),
 'room_signs': ('Room signs', ['Class A / Class B / Class C', 'Library / Infirmary', 'Follow the main corridor.']),
 'supply_clipboard': ('Supply return list', ['Folders', 'Display materials', 'Mark only items actually returned.']),
 'three_drafts': ('Display plan / draft', ['Keep the introduction short.', 'Leave space for the photographs.', 'Agree the final version together.']),
 'anonymous_form': ('Your canteen experience', ['No name required.', 'Which lunch period is easiest for you?', 'You may leave any question unanswered.']),
 'anonymous_survey': ('Anonymous feedback', ['Please discuss the ideas, not the people.', 'Keep personal details private.']),
 'consent_text': ('Before we share', ['May we use this comment anonymously?', 'You can change your mind.', 'No personal details will be published.']),
 'feature_sheet': ('Pilot scope', ['One reliable canteen-time suggestion', 'No student profiles', 'Extra features can wait.']),
 'maintenance_guide': ('Keeping it working', ['Use the approved local copy.', 'Check the source schedule.', 'If it fails, use the paper notice.']),
 'offline_notice': ('Working offline', ['The school network is unavailable.', 'The paper information still works.', 'Please check again later.']),
 'paper_mockups': ('Canteen pilot / layout', ['Choose a lunch period.', 'Read the current suggestion.', 'No login or personal profile.']),
 'presentation': ('A quieter lunch', ['First-year canteen pilot', 'Akira Seojin / Project team', 'A small tool we can keep working.']),
 'project_notebook': ('Project notebook', ['Ideas / feedback / next steps', 'Check the simple version first.', 'Leave room for another opinion.']),
 'queue_survey': ('Canteen queue check', ['Lunch period', 'Approximate waiting time', 'No names or individual tracking.']),
 'teacher_approval': ('Pilot approval', ['Supervised first-year activity', 'Anonymous feedback only', 'Keep a working paper alternative.']),
 'adviser_questions': ('Questions for the adviser', ['What can I study?', 'What support could I apply for?', 'Which step can I take this year?']),
 'caption_drafts': ('A view from our window', ['A familiar place, seen carefully.', 'Photo and caption by Seo-yun', 'Ask before changing the author line.']),
 'credit_labels': ('Author credit', ['Photograph: Han Seo-yun', 'Ask the author before making changes.']),
 'feedback_sheets': ('What did you notice?', ['One thing that caught your eye', 'One question about the display', 'Personal questions are optional.']),
 'handouts': ('The view from here', ['First-year library-window display', 'Small photographs of ordinary places', 'Please return reference books to the desk.']),
 'library_record': ('Donated atlas check', ['Title / condition / shelf', 'Flag loose pages for the librarian.', 'Do not repair books without asking.']),
 'menu': ('Today in the canteen', ['Noodles / rice / seasonal vegetables', 'Fruit cup', 'Ask the staff about spice and ingredients.']),
 'reference_cards': ('Places to learn about', ['Find an atlas entry.', 'Compare two reliable sources.', 'Write down what you still want to know.']),
 'study_options': ('Study options', ['Courses and entry requirements', 'Language preparation', 'Scholarships and adviser appointment']),
 'window_essay': ('The view from here', ['The window is the same each day.', 'The light never quite is.', 'Looking carefully is a place to begin.']),
 'drying_paper': ('Visitor information', ['Please let the ink dry.', 'The nurse can answer health questions.']),
 'finished_reading_corner': ('A quiet reading corner', ['Books and public information', 'Please ask before borrowing.', 'The visitor chairs are for resting, too.']),
 'homework': ('Independent study', ['Work through one question at a time.', 'Ask if an instruction is unclear.']),
 'household_plan': ('Sharing the evening tasks', ['Choose tasks together.', 'Leave time for homework and rest.', 'No one has to do everything.']),
 'leaflet_list': ('Public information checklist', ['Check the dates.', 'Replace damaged copies.', 'Ask the nurse before adding new material.']),
 'meal_worksheet': ('A lunch for yourself', ['Choose a main dish.', 'Add vegetables and something you enjoy.', 'Plan a portion that suits you.']),
 'noticeboard': ('Visitor information', ['Ask the nurse for medical help.', 'Please keep the doorway clear.', 'Public reading materials are by the window.']),
 'paper_headings': ('Reading-corner headings', ['Visitor information', 'Books to borrow', 'A place to take a break']),
 'public_leaflets': ('School visitor information', ['For questions, please ask the nurse.', 'These copies contain public information.']),
 'reading_list': ('Reading list', ['A short story', 'A book about gardens', 'Something you choose for yourself']),
 'staff_only_sign': ('Staff only', ['Please ask the nurse.', 'Students must not enter the medicine store.']),
 'attendance_sheet': ('Sports activity / attendance', ['First-year supervised session', 'Report to the coach before leaving.']),
 'budget_exercise': ('Equipment budget exercise', ['Check what we already have.', 'Replace damaged equipment first.', 'Show how you reached the total.']),
 'equipment_list': ('Equipment return', ['Basketballs', 'Cones and practice markers', 'Return the cart to the marked space.']),
 'group_assignment': ('Group study', ['Explain your approach.', 'Give everyone time to answer.', 'Check the unfinished questions together.']),
 'household_worksheet': ('An ordinary routine', ['Describe one household task.', 'What helps it run smoothly?', 'What would you change?']),
 'practice_report': ('Practice reflection', ['What worked?', 'What needs another try?', 'Leave time to rest.']),
 'practice_statistics': ('Practice record', ['Attempts / completed passes', 'Look for a pattern, not one bad result.', 'Check the notes with the player.']),
 'workbook': ('Independent study', ['Read the question carefully.', 'Show your working.', 'Take the next question when ready.']),
 'worksheet': ('Class worksheet', ['Name / class', 'One problem at a time.', 'Use the space below for your working.']),
 'orientation_sign': ('First-year orientation', ['Classrooms / main corridor', 'Ask at the lobby if you need help.']),
 'booklet': ('Welcome to Seiran', ['Classrooms are on the main corridor.', 'The lobby connects the shared spaces.', 'Take your time learning the way.']),
}


def documents():
    for key, (title, lines) in DOCUMENTS.items():
        c = Canvas('Documents/'+key, (640, 880), PAPER)
        c.rect((20, 20, 600, 840), None, LINE)
        c.text((52, 52), 'SEIRAN  /  FIRST YEAR', 20, MUTED, bold=True)
        c.line([(52, 98), (588, 98)], ACCENT, 3)
        # Wrap headings with measured type, preserving accessible source text.
        font = ImageFont.truetype(str(FONT/'SourceSerif4-Regular.ttf'), 36)
        words, rows, row = title.split(), [], ''
        for word in words:
            trial = (row+' '+word).strip()
            if font.getlength(trial) > 530:
                rows.append(row); row = word
            else:
                row = trial
        if row: rows.append(row)
        for i, text in enumerate(rows): c.text((52, 130+i*48), text, 36, serif=True)
        y = 156+len(rows)*48
        for line in lines:
            # Each authored line fits a normal form column at this type size.
            c.text((52, y), line, 22)
            y += 53
        for y2 in range(max(420, y+24), 790, 54): c.line([(52, y2), (588, y2)])
        c.text((52, 818), 'Please return shared materials after use.', 18, MUTED)
        c.save()
    (ART/'Documents/copy.json').write_text(json.dumps(DOCUMENTS, ensure_ascii=False, indent=2), encoding='utf-8')


def screens():
    for key, title, lines in [
        ('phone_message', 'Messages', ['Thanks for today.', 'Can we talk when you have a moment?', 'There is no hurry.']),
        ('three_request_messages', 'Three requests', ['Could you help with a poster?', 'Do you have time for a spreadsheet?', 'Can you make our club signup page?']),
        ('consent_screen', 'Before we share', ['Anonymous comments only.', 'No names or personal profiles.', 'You can withdraw your comment.']),
        ('pilot_screen', 'A quieter lunch', ['Choose a lunch period.', 'Current suggestion: later lunch', 'Paper notice available at the canteen.']),
        ('offline_screen', 'Working offline', ['The network is unavailable.', 'Use the paper notice for now.', 'Your work has not been lost.'])]:
        c = Canvas('Screens/'+key, (960, 600), PAPER)
        c.rect((0, 0, 960, 70), INK)
        c.text((32, 22), 'SEIRAN', 24, PAPER, bold=True)
        c.text((48, 112), title, 42, serif=True)
        for i, text in enumerate(lines):
            c.rect((48, 194+i*104, 864, 80), '#FFFFFF', LINE, radius=8)
            c.text((72, 218+i*104), text, 28)
        c.save()
    # Two original abstract game-screen interfaces. These are small device
    # displays, not replacement illustrations for school environments.
    for key in ['strategy_game_screen', 'cozy_game_screen']:
        c = Canvas('Screens/'+key, (960, 600), '#DCE6D8')
        for y in range(5):
            for x in range(9):
                c.rect((24+x*78, 92+y*86, 74, 80), '#CAD9BD' if (x+y)%2 else '#D7E2CB', '#A9BA9C')
        if key == 'strategy_game_screen':
            c.text((24, 24), 'FIELD NOTES / practice map', 26, bold=True)
            for x,y in [(2,2),(4,3),(6,1)]:
                c.rect((43+x*78, 114+y*86, 34, 34), '#657D8D', INK, radius=5)
            c.text((754, 118), 'Turn 03', 26)
            c.text((754, 174), 'Observe', 24)
            c.text((754, 224), 'Plan', 24)
            c.text((754, 274), 'Wait', 24)
        else:
            c.text((24, 24), 'SMALL DAYS / garden', 26, bold=True)
            c.rect((110, 125, 170, 142), '#EEE2CD', INK)
            c.rect((160, 205, 44, 62), '#9A8065')
            for x in range(3):
                for y in range(2):
                    c.rect((360+x*85, 170+y*100, 60, 64), '#927B62', radius=5)
                    c.line([(390+x*85, 220+y*100),(390+x*85, 182+y*100)], '#59774D', 8)
            c.text((750, 118), 'Spring 04', 26)
            c.text((750, 174), 'Water', 24)
            c.text((750, 224), 'Plant', 24)
            c.text((750, 274), 'Rest', 24)
        c.save()


def title_and_overlays():
    for key, color in [('wordmark_ink', INK), ('wordmark_paper', PAPER)]:
        c = Canvas('Title/'+key, (1000, 330))
        c.text((16, 12), 'April,', 150, color, serif=True)
        c.text((242, 148), 'again', 150, color, serif=True)
        c.line([(26, 306), (213, 306)], ACCENT, 5)
        c.save()
    c = Canvas('Title/app_icon', (512, 512), PAPER)
    c.rect((24, 24, 464, 464), None, ACCENT, 5, 38)
    c.text((92, 64), 'A', 304, ACCENT, serif=True)
    c.text((312, 302), ',', 140, INK, serif=True)
    c.line([(96, 426), (416, 426)], ACCENT, 5)
    c.save()
    for key, color in [('fade_black', '#000000'), ('fade_paper', PAPER)]:
        Canvas('UI/'+key, (8, 8), color).save()
    c = Canvas('UI/floor_markers', (320, 320))
    c.rect((44, 140, 232, 36), '#9CB8C5')
    c.rect((142, 44, 36, 232), '#9CB8C5')
    c.save()


if __name__ == '__main__':
    documents(); screens(); title_and_overlays()
    (ART/'native-catalog.json').write_text(json.dumps(CAT, indent=2), encoding='utf-8')
    print(f'Authored {len(CAT)} editable native graphics and PNG exports.')
