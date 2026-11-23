"""Export the authored VN screenplay, production bible and Unity content JSON.

Run this file to build and validate. It does not generate prose or artwork.
"""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import importlib
import json
import re

import common
from story_schema import lines
from voice_pass import all_blocks, perform

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "Narrative/Screenplay"
OUT = ROOT / "Assets/AprilAgain/Narrative"
ROUTES = ["katya", "akira", "seoyun", "mari", "svea"]
KINDS = {"good", "neutral", "bad"}
SPEAKERS = {"Stage", "Narration", "MC", "Katya", "Akira", "Seo-yun", "Mari", "Svea",
            "Teacher", "Nurse", "Classmate", "PA", "Librarian", "Coach"}

LOCATIONS = {
    "bedroom": {"name": "Your room", "neighbors": ["gate"], "purpose": "Home, save, journal and sleep. No girl appears here during a route."},
    "gate": {"name": "School gate", "neighbors": ["bedroom", "lobby", "field"], "purpose": "Entrance, leaving school and permitted supervised gate-side activity."},
    "lobby": {"name": "Lobby", "neighbors": ["gate", "corridor", "canteen", "field"], "purpose": "Shared noticeboard, supplies, open-campus display."},
    "corridor": {"name": "Main corridor", "neighbors": ["lobby", "infirmary", "class_b", "class_c", "library", "class_a"], "purpose": "A single readable hall links the academic rooms; windows on the left, classroom doors on the right."},
    "infirmary": {"name": "Infirmary", "neighbors": ["corridor"], "purpose": "Public visitor table and reading corner only. Nurse present; no patient notes or student medical work."},
    "class_b": {"name": "Class B", "neighbors": ["corridor"], "purpose": "Katya and Mari's homeroom, class display and craft activities."},
    "class_c": {"name": "Class C", "neighbors": ["corridor"], "purpose": "Seo-yun and Svea's homeroom, supervised study and reading."},
    "library": {"name": "Library", "neighbors": ["corridor"], "purpose": "Window table, atlas shelf, display preparation. Keep window/table placement consistent."},
    "class_a": {"name": "Class A", "neighbors": ["corridor"], "purpose": "MC and Akira's homeroom, supervised tech and survey project."},
    "canteen": {"name": "Canteen", "neighbors": ["lobby"], "purpose": "Lunch and staff-approved work at cleared tables. Food prep only with staff supervision."},
    "field": {"name": "Sports field / hardcourt", "neighbors": ["lobby", "gate"], "purpose": "One outdoor sports area includes a basketball hardcourt, near-side bench and safe separate supervised practice lane."}
}

CLUB_ONLY = {"katya.04", "akira.03", "seoyun.14", "mari.09", "svea.11"}
WARDROBES = {"katya.04": "school_tracksuit", "katya.11": "fencing_kit_with_mask",
             "mari.09": "aikido_gi_and_trousers", "mari.11": "uniform_with_apron",
             **{f"svea.{n:02d}": "school_sports_jacket_and_trousers" for n in [1, 5, 6, 12, 14]}}
REPAIRS = {
"katya": """MC: Wait. Saying I deserved a chance was unfair. You don't owe me a date. I'm sorry.
Katya: Good. I would rather not begin anything with an invoice attached. I know you can listen; do so now.""",
"akira": """MC: I shouldn't have pushed for a yes. I wanted an answer and got scared of the one I might hear.
Akira: Okay. I can hear the apology. Please don't make being clear mean agreeing with you. Let me choose my answer.""",
"seoyun": """MC: I shouldn't have asked you to promise to stay. Your plans are yours. I was afraid, and I made it your problem.
Seo-yun: Thank you for correcting it. I can care about someone without making myself smaller. Please remember that.""",
"mari": """MC: That sounded as if I was looking for someone to take care of me. I'm sorry. I want to know you, including what you need.
Mari: Then listen to this answer as mine. I don't want to earn it by being endlessly useful.""",
"svea": """MC: That came out like I wanted to take over. I don't. I'm sorry. I'll stop explaining and hear your answer.
Svea: Good. One terrible sentence doesn't erase everything else. Doesn't get a free pass either. Listen."""
}

def prose(block):
    output = []
    for line in block:
        speaker, text = line["speaker"], line["text"]
        output.append(f"*[{text}]*" if speaker == "Stage" else f"**{speaker}:** {text}")
    return "\n\n".join(output)


def add_kinds(value):
    if isinstance(value, dict):
        if "speaker" in value and "text" in value:
            value["kind"] = "direction" if value["speaker"] == "Stage" else "narration" if value["speaker"] == "Narration" else "dialogue"
        for child in value.values():
            add_kinds(child)
    elif isinstance(value, list):
        for child in value:
            add_kinds(child)


def write_json(path, value):
    add_kinds(value)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_route(name):
    module = importlib.import_module(name)
    route = {"schemaVersion": 1, "id": name, "name": module.NAME, "voice": module.VOICE,
             "scenes": deepcopy(module.SCENES), "endings": deepcopy(module.ENDINGS),
             "finaleRepair": {"when": "ending == good AND finalChoice == bad", "lines": lines(REPAIRS[name])}}
    perform(route)
    for scene in route["scenes"]:
        scene["id"] = f"{name}.{scene['number']:02d}"
        scene["previousScene"] = None if scene["number"] == 1 else f"{name}.{scene['number']-1:02d}"
        scene["background"] = "bg_" + scene["location"] + "_day"
        scene["requiresClubDay"] = scene["id"] in CLUB_ONLY
        scene["requiredBlock"] = "late" if scene["number"] == 15 else "morning" if scene["id"] == "mari.09" else None
        scene["wardrobe"] = WARDROBES.get(scene["id"], "school_uniform")
        scene["temperatureTiming"] = "after_setup_before_choice_using_pre_scene_counts"
        scene["onlyAfterOpening"] = True
        scene["oncePerGirlPerDay"] = True
        scene["isFinale"] = scene["number"] == 15
        for index, choice in enumerate(scene["choices"], 1):
            choice["id"] = scene["id"] + f".choice{index}"
            choice["rawDelta"] = {"good": int(choice["kind"] == "good"), "bad": int(choice["kind"] == "bad"), "neutral": int(choice["kind"] == "neutral")}
            choice["next"] = "route_ending" if scene["isFinale"] else "shared_closing"
    for ending in route["endings"]:
        ending["id"] = name + ".ending." + ending["kind"]
        ending["cg"] = f"cg_{name}_{ending['kind']}"
        ending["next"] = "credits_then_title"
    return route


def route_markdown(route):
    chunks = [f"# {route['name']} — complete route", route["voice"],
              "Production labels in brackets identify score categories; hide them in the game. Read the setup, then the current relationship-temperature beat, one chosen response, and the shared closing. Do not display all alternatives to the player.",
              "Relationship temperature is calculated BEFORE this scene: warm when raw good minus raw bad is at least 3; cool when it is at most -3; mixed otherwise. These lines change delivery, never unlock or skip scenes."]
    for scene in route["scenes"]:
        chunks += [f"## {scene['id']} — {scene['title']}",
                   f"**Location:** {LOCATIONS[scene['location']]['name']} · **Time:** 3-hour activity block · **Initial expression:** {scene['expression']}",
                   f"**Props:** {', '.join(scene['props']) or 'None'} · **Outfit:** {scene['wardrobe']}" + (" · **Open-campus day only**" if scene["requiresClubDay"] else "") + (f" · **Required block:** {scene['requiredBlock']}" if scene["requiredBlock"] else "")]
        chunks += ["### Scene", prose(scene["setup"])]
        if scene["temperature"]:
            chunks += ["### Relationship beat — after setup, before decision"]
            for name, block in scene["temperature"].items():
                chunks += [f"**If {name}:**", prose(block)]
        chunks += ["### Decision"]
        for i, choice in enumerate(scene["choices"], 1):
            chunks += [f"#### {i}. {choice['text']} [{choice['kind'].upper()}]", prose(choice["response"])]
        chunks += ["### Continue", prose(scene["closing"])]
    chunks += ["## Finale continuity bridge", "Only if the route total selects GOOD while the scene-15 choice itself was BAD, play this short repair before the good epilogue. It does not change the score. A mostly positive history may survive a badly worded final sentence, but that sentence is not silently ignored.", prose(route["finaleRepair"]["lines"])]
    for ending in route["endings"]:
        chunks += [f"## {ending['kind'].upper()} ENDING — {ending['title']}", f"**CG:** `{ending['cg']}`", f"**Art direction:** {ending['cgBrief']}", prose(ending["lines"])]
    return "\n\n".join(chunks) + "\n"


def common_markdown():
    chunks = [f"# {common.TITLE} — shared screenplay", f"**School:** fictional {common.SCHOOL}, Fukuoka. **MC:** {common.MC['displayName']}. First-person narration; no defined MC face.",
              "Day one contains observation only. The five girls can speak to other people in overheard vignettes; they do not hold conversations with the MC. Their names are heard naturally, not granted through an unexplained character dossier."]
    for scene in common.OPENING:
        chunks += [f"## {scene['title']}", prose(scene["lines"])]
    chunks += ["## Free campus tour", "Visit the following five scenes in any order. The map and journal preserve the checklist. Repeated clicks use the short repeat line, never replay or score an observation."]
    for scene in common.OBSERVATIONS:
        chunks += [f"### {scene['title']} — {LOCATIONS[scene['location']]['name']}", prose(scene["lines"]), f"**Repeat click:** {scene['repeat']}"]
    chunks += ["## Tour complete", prose(common.POST_TOUR), "## First night", prose(common.HOME_FIRST), "## Later mornings"]
    for i, block in enumerate(common.MORNING, 1):
        chunks += [f"### Morning variation {i}", prose(block)]
    chunks += ["## Home transitions"]
    for label, block in common.HOME.items():
        chunks += ["### " + label.replace("_", " ").title(), prose(block)]
    chunks += ["## Non-scoring acknowledgements"]
    for girl, barks in common.BARKS.items():
        chunks += [f"### {girl}"] + [f"**{kind}:** {text}" for kind, text in barks.items()]
    chunks += ["## Player-facing system copy"]
    for key, value in common.SYSTEM.items():
        chunks += [f"**{key}:** " + (" / ".join(value) if isinstance(value, list) else value)]
    return "\n\n".join(chunks) + "\n"


def contracts():
    return {
        "openingDay": {"observationsRequired": 5, "scoredEncounters": 0, "travelCostsTime": False},
        "normalBlocks": [{"id": "midday", "start": "12:00", "end": "15:00"}, {"id": "late", "start": "15:00", "end": "18:00"}],
        "clubExtraBlock": {"id": "morning", "start": "09:00", "end": "12:00"},
        "playableWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "clubDay": "Saturday", "sunday": "brief non-scoring home transition",
        "schedule": "On school day d, route index i has its story window at midday if (d+i)%5 < 3, otherwise late. Indices: katya0,akira1,seoyun2,mari3,svea4. Saturday also exposes pending eligible scenes in morning. A scene's requiredBlock overrides rotation and the extra Saturday window: all finales are late, Mari09 is Saturday morning only. Club-only scenes require Saturday. Story appointment room is the next scene's location; other windows use idle routine locations. Show appointment before player commits time.",
        "temperature": {"warmAtMargin": 3, "coolAtMargin": -3, "default": "mixed"},
        "endingRule": {"good": "rawGood + rawNeutral", "bad": "rawBad + rawNeutral", "select": "compare; equality means neutral", "evaluateAfter": "scene15 choice commits"},
        "sameGirlDailyLimit": 1, "sceneHours": 3, "travelHours": 0,
        "commit": "Check expected route scene, available block, open room and girl not used today. Display choice, then atomically store choice ID, raw counter delta, next scene index, used-today set and spent block. Reject duplicate choice IDs. Save all of that in one snapshot.",
        "saveFields": ["schemaVersion", "schoolDay", "weekday", "block", "location", "openingObservationFlags", "routeNextIndices", "rawGoodBadNeutral", "completedChoiceIds", "girlsUsedToday", "lastChoice", "pendingEnding", "galleryUnlocks"],
        "gallery": "Global unlocks are separate from session saves and survive New Game.",
        "finaleSave": "Write a separate pre-finale snapshot before entering scene15, after warning confirmation. Never overwrite the only manual save. If saving fails, show the failure and allow cancelling the finale.",
        "postEnding": "Unlock only the actual selected CG, show credits, return to title. Other routes do not continue in this playthrough.",
        "wait": "Waiting spends a block without score. Home/sleep remains reachable if no eligible scene is available. Offer explicit fast-forward when every pending scene is waiting for Saturday. Never silently skip a pending scene.",
        "implementationStatus": "Screenplay and validated content contract only; runtime saving, scheduling and scoring have not yet been implemented in Unity."
    }


def asset_plan(routes):
    assets = []
    for loc, info in LOCATIONS.items():
        used = [scene["id"] for route in routes for scene in route["scenes"] if scene["location"] == loc]
        assets.append({"id": f"bg_{loc}_day", "type": "background", "requiredBy": used or ["common"], "brief": info["purpose"], "status": "planned_after_script_review"})
    assets += [
        {"id": "bg_bedroom_evening", "type": "background_variant", "requiredBy": ["common.home"], "brief": "Same modest room geography as morning; evening desk lamp, visible bed, desk and school bag. Do not redesign the room.", "status": "planned_after_script_review"},
        {"id": "bg_corridor_rain", "type": "background_variant", "requiredBy": ["katya.05"], "brief": "Same corridor and doors as daytime; ordinary rainy overcast outside, no dramatic storm effects.", "status": "planned_after_script_review"},
        {"id": "campus_map", "type": "map", "requiredBy": ["common.navigation"], "brief": "Preserve user's topology: infirmary west, B northwest, C north/northeast, library east, A southeast of corridor, lobby south-center, canteen southwest, field southeast, gate south. Bedroom via Home. Live labels, no invented rooms.", "status": "planned_after_script_review"},
        {"id": "mc_silhouette", "type": "character", "requiredBy": ["ending_cgs", "common"], "brief": "Unidentifiable charcoal-grey male first-year uniform silhouette. No detailed face.", "status": "planned_after_script_review"}]
    for route in routes:
        expressions = sorted({s["expression"] for s in route["scenes"]} | {"neutral", "smile", "flustered", "sad", "concerned", "surprised"})
        assets.append({"id": "char_"+route["id"]+"_expressions", "type": "expression_set", "requiredBy": [s["id"] for s in route["scenes"]], "brief": {"expressions": expressions, "note": "Expression names are acting directions; consolidate synonymous names into a consistent final atlas only after story review. No random substitutions."}, "status": "planned_after_script_review"})
        assets.append({"id": "char_"+route["id"]+"_exploration", "type": "placement_poses", "requiredBy": ["observe."+route["id"]]+[s["id"] for s in route["scenes"]], "brief": {"observationPose": next(x["pose"] for x in common.OBSERVATIONS if x["girl"] == route["id"]), "everyday": "Full-body standing and seated neutral school-life poses; refer to scene props. Handheld props must match the scene, not appear permanently in all portraits."}, "status": "planned_after_script_review"})
        for wardrobe in sorted({s["wardrobe"] for s in route["scenes"]} - {"school_uniform"}):
            assets.append({"id": "char_"+route["id"]+"_"+wardrobe, "type": "wardrobe_variant", "requiredBy": [s["id"] for s in route["scenes"] if s["wardrobe"] == wardrobe], "brief": "Same character identity and clean anime rendering, practical modest activity clothes. Preserve visible face and hairstyle. No glamour sports poses.", "status": "planned_after_script_review"})
        props = sorted({p for s in route["scenes"] for p in s["props"]})
        for prop in props:
            assets.append({"id": "prop_"+route["id"]+"_"+prop, "type": "prop", "requiredBy": [s["id"] for s in route["scenes"] if prop in s["props"]], "brief": "May be staged in a background, a character pose or a simple insert. It is not automatically a separate required texture.", "status": "planned_after_script_review"})
        for ending in route["endings"]:
            assets.append({"id": ending["cg"], "type": "ending_cg", "requiredBy": [ending["id"]], "brief": ending["cgBrief"], "status": "planned_after_script_review"})
    assets += [
        {"id": "amb_school", "type": "audio", "requiredBy": ["common.exploration"], "brief": "Low-key school room tone and distant footsteps. Leave speech readable.", "status": "planned_after_script_review"},
        {"id": "bgm_daily", "type": "audio", "requiredBy": ["common", "route_daily"], "brief": "Original restrained acoustic/piano school-day loop. Do not use a copyrighted song mentioned in dialogue.", "status": "planned_after_script_review"},
        {"id": "bgm_reflection", "type": "audio", "requiredBy": ["home", "route_reflection"], "brief": "Original quiet reflective loop with a comfortable fade point.", "status": "planned_after_script_review"},
        {"id": "bgm_endings", "type": "audio_set", "requiredBy": ["ending_cgs"], "brief": "Original good/neutral/bad ending variations. Bad is reflective, not horror or tragedy.", "status": "planned_after_script_review"},
        {"id": "sfx_story", "type": "audio_set", "requiredBy": ["common", "routes"], "brief": "Alarm, school bell, light rain, paper/zip/cup sounds, basketball bounce and rim, short generic PA bed. Simple UI confirm/cancel. No mandatory voice acting.", "status": "planned_after_script_review"}]
    return assets


def validate(routes, plan):
    ids, choice_ids = set(), set()
    sizes, score_orders = {}, Counter()
    assert {x["girl"] for x in common.OBSERVATIONS} == set(ROUTES)
    assert len({x["id"] for x in common.OBSERVATIONS}) == 5
    assert all(x["location"] in LOCATIONS for x in common.OPENING + common.OBSERVATIONS)
    for route in routes:
        assert [s["number"] for s in route["scenes"]] == list(range(1, 16))
        assert {e["kind"] for e in route["endings"]} == KINDS
        assert len(route["endings"]) == 3
        for block in all_blocks(route):
            for line in block:
                assert line["speaker"] in SPEAKERS, line
                assert line["text"].strip(), line
                assert not re.search(r"\b(TODO|TBD|PLACEHOLDER|LOREM IPSUM)\b", line["text"]), line
        for scene in route["scenes"]:
            assert scene["location"] in LOCATIONS
            assert scene["hours"] == 3 and scene["id"] not in ids
            assert scene["requiredBlock"] in {None, "morning", "midday", "late"}
            assert scene["number"] != 15 or scene["requiredBlock"] == "late"
            ids.add(scene["id"])
            assert set(scene["temperature"]) in (set(), {"warm", "mixed", "cool"})
            assert len(scene["choices"]) == 3 and {c["kind"] for c in scene["choices"]} == KINDS
            assert len(scene["setup"]) >= 6, scene["id"]
            assert len(scene["closing"]) >= 1
            score_orders[tuple(c["kind"] for c in scene["choices"])] += 1
            for choice in scene["choices"]:
                assert choice["id"] not in choice_ids
                choice_ids.add(choice["id"])
                assert len(choice["response"]) >= 2
                assert sum(choice["rawDelta"].values()) == 1
            expected_previous = None if scene["number"] == 1 else f"{route['id']}.{scene['number']-1:02d}"
            assert scene["previousScene"] == expected_previous
        dialogue = " ".join(line["text"] for block in all_blocks(route) for line in block if line["speaker"] != "Stage")
        sizes[route["id"]] = len(re.findall(r"\b[\w'-]+\b", dialogue))
        assert sizes[route["id"]] >= 2500, sizes
    assert len(ids) == 75 and len(choice_ids) == 225
    assert len(score_orders) >= 4, "Choices must not always put GOOD first"
    assert len({x["id"] for x in plan}) == len(plan)
    assert sum(x["type"] == "ending_cg" for x in plan) == 15
    cg_ids = {x["id"] for x in plan if x["type"] == "ending_cg"}
    assert all(ending["cg"] in cg_ids for route in routes for ending in route["endings"])
    for loc, info in LOCATIONS.items():
        for neighbor in info["neighbors"]:
            assert loc in LOCATIONS[neighbor]["neighbors"], (loc, neighbor)
    # All possible raw-count totals after 15 choices; neutral adds to both sides.
    outcomes = Counter()
    for good in range(16):
        for bad in range(16 - good):
            neutral = 15 - good - bad
            effective = (good + neutral) - (bad + neutral)
            assert effective == good - bad
            outcomes["good" if effective > 0 else "bad" if effective < 0 else "neutral"] += 1
    assert outcomes["neutral"] > 0
    # Verify every scene can be reached under the proposed calendar without a
    # deadline, including club-only gates. This is content reachability, not a
    # test of a Unity implementation that does not exist yet.
    completion_days = {}
    for ri, route in enumerate(routes):
        next_index = 0
        for day in range(2, 122):
            club = (day - 1) % 6 == 5
            scene = route["scenes"][next_index]
            if scene["requiresClubDay"] and not club:
                continue
            available_blocks = ["morning", "midday", "late"] if club else ["midday", "late"]
            required = scene["requiredBlock"]
            if required and required not in available_blocks:
                continue
            next_index += 1
            if next_index == 15:
                completion_days[route["id"]] = day
                break
        assert next_index == 15, route["id"]
    report = {"routes": 5, "encounters": 75, "writtenChoices": 225, "endings": 15,
              "observationVignettes": len(common.OBSERVATIONS), "scoreTotalCasesChecked": sum(outcomes.values()),
              "choiceOrderPatterns": len(score_orders), "allBranchWordCounts": sizes,
              "soloRouteCompletionSchoolDays": completion_days,
              "checks": ["All scene chains contiguous", "Three written reactions per encounter", "Three endings per route", "One neutral delta, added to both effective categories", "15 distinct ending CG briefs", "Connected reversible map graph", "All authored scene locations exist", "All routes reachable with club gates", "Every voice edit target matched", "No placeholder markers"],
              "notVerified": ["Unity runtime scheduling, saves and duplicate-input guards are a written contract, not implemented", "B2-C1 is an editorial target, not a certified language assessment", "Native-language performance review and player playtesting remain useful before final voice recording"]}
    return report


def production_notes(routes, plan, report):
    text = """# Production notes — script-first milestone

## Fixed story and scope

Fictional Seiran High School in Fukuoka, beginning in April and continuing through the first term. All five girls and the ordinary male MC are new first-years. The original dossiers' age-18/final-secondary framing was adapted to the user's first-year setting; no explicit romance or body-emphasis direction is included. Ren Takahashi is the default MC name, with surname-first address until a naturally closer exchange. The title remains **April, again**. A complete playthrough ends at the first finished girl's fifteenth scene.

The source profiles remain authoritative for personality, interests and appearance. Katya's council role is a first-year ambition; she does class display/committee preparation rather than inexplicably becoming vice president on arrival. Mari is a student, never a nurse. Svea is a basketball ace in the making, not a secretly helpless boyish stereotype. Seo-yun's family relocated before high school so she can attend this school; her birthplace is not a sensational twist or a problem the MC solves. Akira keeps genuine technical/economics interests and learns to question whether a useful shortcut respects people.

## Readable language and performed voices

The English is written as readable VN dialogue, with contractions, incomplete thoughts, everyday jokes and room for silence. Story actions and gestures carry meaning rather than a paragraph explaining every feeling. The text is aimed at B2–C1 readers; this is an editorial target, not a test-score claim.

The game uses an English presentation of conversations at a Japanese school. Selective Japanese expressions and heritage-language slips are retained for performance flavor. They are not an assertion that all characters literally speak English at school. Accent is visualized primarily in pacing, formal/informal vocabulary, hesitations and physical acting. Avoid phonetic nationality caricatures, random missing articles, or replacing all r/l/th sounds. A native speaker may refine delivery before recorded localization, but the written emotional meaning is accessible now.

- **Katya:** clipped, deliberate schoolroom formality; the surname gets precise attention. Russian slips appear when her composure genuinely cracks. Arms fold defensively; the hair tuck often contradicts her denial. Dry wit, fair competition, tea and ordinary sweets add warmth. Use 'Bozhe moy' sparingly; 'durak' appears teasingly only in the good ending, not as her whole personality.
- **Akira:** connected bursts of thought, self-interruptions, explanations she catches herself giving, technical/economics tangents that respond to what is happening. She adjusts her glasses or fusses with a charm when she cannot hide in another explanation. Casual Korean/Japanese slips follow excitement, frustration or family associations. Serious boundaries are allowed to slow her down.
- **Seo-yun:** careful words, soft starts, thoughtful pauses and gentle dry humor. A low voice does not mean an inability to disagree. Korean slips belong to gratitude or emotional admission. Her humor is concrete: a rude cloud, an uncooperative English word, a disappointing airport sandwich. The journal is private unless she chooses a specific page.
- **Mari:** soft requests, small hesitations, a reflexive glance at other people's food or sleeves. She starts caring for the MC instead of answering a personal question, catches herself, then learns to answer. 'Ano' is a hesitation, not a catchphrase. 'Daijoubu' needs an immediate readable context. Keep warmth without a fetishized older-woman act.
- **Svea:** short answers, dropped subjects, quick corrections, dry exaggeration; basketball opens a longer and more precise speaking rhythm. 'Oi' attracts attention, not contempt. 'Betsuni' is a deflection; boku self-reference is retained in two emotional moments. Blush begins in the ears, her gaze moves to an unimportant object, and she becomes unnecessarily blunt. She doesn't need a hidden trauma to make choosing company meaningful.

### Small language glossary

Bozhe moy (Russian): 'my God'/an exasperated 'oh, honestly'; durak: fool/idiot, here teasing only after mutual affection. Jamkkanman (Korean): hold on/a moment. Eomma: mum. Aish: frustrated interjection. Daebak: excited 'wow'/great. Gomawoyo: polite thanks. Geureom: then/in that case. Joahaeyo: I like you/it, clarified by the confession context. Chotto matte (Japanese): wait a moment. Ano: hesitant 'um'. Daijoubu: okay/all right. Otsukaresama deshita: appreciation after shared work. Oi: hey. Betsuni: 'not particularly'/a defensive 'it's nothing'. Mou: an exasperated 'oh, come on'. Boku: a Japanese first-person pronoun, used by Svea as specified in her dossier.

Reference checks: [Japan Foundation Irodori grammar](https://www.irodori.jpf.go.jp/assets/data/Grammar_all.pdf), [National Institute of Korean Language entry/examples for a moment](https://krdict.korean.go.kr/eng/dicSearch/SearchView?ParaWordNo=57313&nation=eng&nationCode=6), [Gramota on Russian exclamations](https://gramota.ru/biblioteka/spravochniki/pravila-russkoy-orfografii-i-punktuatsii/nazvaniya-svyazannye-s-religiey). These support basic expressions, not a claim to reproduce a specific regional accent.

## Time and routine contract

Opening day is an unscored tour: five observations in any order, no conversation with the girls. All five are required before Home unlocks. Repeat clicks use an acknowledgement. Days after that have automatic morning classes followed by **12:00–15:00** and **15:00–18:00** activity blocks. Saturday open-campus days add **09:00–12:00**. The school runs a fictional first-term activity/study program; encounters encompass shared schoolwork, study, breaks and the relevant conversation. They are not three uninterrupted hours flirting while class is skipped.

Each girl can advance exactly one scene per playable school day. Travel, looking, reading schedules and brief acknowledgement lines cost no time. A scene invitation shows the three-hour cost before acceptance. Waiting deliberately spends a block. Going home ends today's activity opportunities after a clear confirmation. No score changes for early departure. Sleep advances the day; Sunday is a brief ordinary-home transition, then Monday. Today's used-girl set resets only when the next playable day begins.

To give routines predictability without offering the same girl in every slot, index girls Katya0, Akira1, Seo-yun2, Mari3, Svea4. On school day d, a girl's story window is midday when **(d + index) mod 5 < 3**, otherwise late. This gives three midday candidates and two late candidates, rotating across days. Saturday additionally offers all eligible pending scenes in the morning; after one morning encounter there is still a candidate in each later group. Club-only scenes may temporarily reduce candidates, so waiting/home are always legal and no day promises that every slot must be filled.

The next scene's room is a scheduled shared activity, recorded in the journal before the day begins. It overrides the girl's idle location for that block only. Outside that story window, show her ordinary routine location and a non-scoring busy line. Never display her in both locations simultaneously. Normal idle patterns: Katya Class B/corridor; Akira Class A/canteen; Seo-yun Class C/library; Mari Class B/infirmary; Svea Class C/canteen/field. Gate activity is supervised; rooms close at 18:00. No daytime character teleports to the MC's bedroom.

Katya04, Akira03, Seo-yun14, Mari09 and Svea11 need a Saturday open-campus block. Mari09 is specifically a morning workshop. All scene15 finales use the late block, overriding ordinary rotation so a confession never forces a post-closing visit. Other Saturday windows remain eligible only when no required-block restriction overrides them. These appointment overrides may reduce the usual three/two split; waiting and Home remain available. Scenes wait without expiring. The journal says so. If all pending encounters await Saturday, offer an explicit fast-forward rather than making the player click through empty days. There is no calendar deadline, random affection decay or gift grinding. Each route requires at least 15 separate encounter days; the actual schedule can require more. Balancing several routes cannot silently erase their scenes.

## Choice continuity and endings

Each of the 75 encounters has one scored decision and three fully written immediate reactions. Good does not always mean agreement: it can mean challenging a shortcut, accepting a refusal, sharing work or admitting uncertainty. Neutral is plausible and distinct from deliberately unkind behavior. The player menu hides category labels. Choice order varies across scenes.

Keep raw **G, B and N**. Effective good = **G + N**; effective bad = **B + N**. Compare them after the fifteenth decision: greater good gives good, greater bad gives bad, equality gives neutral. Neutral therefore cancels in the comparison. Fifteen neutrals is neutral; a mostly neutral route with one good and no bad is good under the user's requested rule. This is deliberate, not an unexplained threshold. No hidden 'perfect final answer' override or consent-forcing mechanic is added.

Scene15's warning offers a separate pre-finale save. A final bad sentence can coexist with a positive overall history; the screenplay provides a unique repair bridge before each good ending in that case. It acknowledges the sentence without secretly changing the score. A final polite sentence does not erase a negative history; bad epilogues address the whole relationship. All rejections remain valid, and no bad ending punishes a girl with injury, disappearance or death.

Before the first decision of each scene, choose any written warm/mixed/cool opening using the existing raw G−B margin: warm >=3, cool <=−3, mixed between. This prevents later scenes from assuming an intimacy a consistently unkind player never earned. Scenes with no temperature alternatives remain shared school activities, not automatic dates. Branches rejoin at the shared closing; props or favors mentioned only inside an optional branch never become a hidden mandatory acquisition.

Commit a choice once, storing its ID, raw score delta, next-scene index, used-today girl and consumed block atomically. Restoring a save restores all of those together. Backlog/skip cannot award points. Skip stops at unread text and decisions. A pending ending is saved before gallery unlock; reloading it must not add the final score again. Global ending unlocks persist independently of New Game. These are implementation requirements; this milestone has not implemented or tested them in Unity.

## Map continuity

Keep the user's map: infirmary west, B northwest, C north/northeast, library east, A below/right of the main hall, lobby south-center, canteen southwest, field southeast, gate south. One corridor joins the academic rooms; lobby joins corridor, canteen, field and gate. The gate has a permitted side path to the field. Bedroom is reached through the Home action at the gate. No rooftop, café interior, family home, gymnasium or foreign-city background is required just because a character mentions it. Off-campus dates in good epilogues are plans; the CG stays in an established school location.

Doors and map areas have labels, hover and focus states, and an unavailable cue. Clickable characters use natural room placement, not full-screen portraits glued into the perspective. Full VN portraits appear only after an encounter begins. Private journals and letters have no readable baked text. Public project text is rendered separately where needed.

## Art generation resumes after the writing review

The corrected clean anime reference remains the rendering direction: broad deliberate hair shapes, clear faces, bounded shadows and controlled light. Do not use the rejected textured first cast as a master. The 70 existing UI geometry PNG/SVG pairs are reusable UI material; they are not 70 completed character illustrations. Existing character studies do not count as locked story assets.

The machine-readable asset plan is `Assets/AprilAgain/Narrative/asset-plan.json`. Every planned CG has a unique ending reference; props name the scenes that use them. A prop may live inside a pose or background rather than become a needless separate texture. Keep school architecture, desk positions, character proportions and light directions consistent. Portrait props must be removable: a journal, ball or lunch box should not remain in every expression regardless of the scene.

## Validation performed

"""
    text += "\n".join(f"- {check}." for check in report["checks"])
    text += f"\n\n{report['encounters']} encounters, {report['writtenChoices']} authored choice reactions, {report['endings']} epilogues and {report['observationVignettes']} opening observations. All {report['scoreTotalCasesChecked']} possible raw-count totals after 15 decisions were checked.\n"
    text += "\n### Route content size\n\n| Route | Words across all branches and endings | Solo completion school day in calendar check |\n|---|---:|---:|\n"
    for route in routes:
        text += f"| {route['name']} | {report['allBranchWordCounts'][route['id']]} | {report['soloRouteCompletionSchoolDays'][route['id']]} |\n"
    text += "\nCounts include alternate reactions, not the word count of one playthrough. Automated checks establish content coverage and proposed scheduling reachability, not enjoyable pacing, certified CEFR level or runtime correctness. The next milestone is a playable opening plus one short route segment, then a reading/playtest pass before final illustration generation.\n"
    text += "\n## Ending CG list derived from the script\n\n"
    for route in routes:
        for ending in route["endings"]:
            text += f"- **{ending['cg']} — {ending['title']}:** {ending['cgBrief']}\n"
    return text


def main():
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    routes = [load_route(name) for name in ROUTES]
    plan = asset_plan(routes)
    report = validate(routes, plan)
    common_data = {"schemaVersion": 1, "title": common.TITLE, "school": common.SCHOOL, "mc": common.MC,
                   "opening": common.OPENING, "observations": common.OBSERVATIONS, "postTour": common.POST_TOUR,
                   "firstNight": common.HOME_FIRST, "morningVariations": common.MORNING, "home": common.HOME,
                   "nonScoringBarks": common.BARKS, "systemCopy": common.SYSTEM}
    documents = [("00_Common.md", common_markdown())]
    for index, route in enumerate(routes, 1):
        documents.append((f"{index:02d}_{route['id'].title()}.md", route_markdown(route)))
        write_json(OUT / (route["id"] + ".json"), route)
    documents.append(("06_Production_Notes.md", production_notes(routes, plan, report)))
    for name, body in documents:
        (DOCS / name).write_text(body, encoding="utf-8")
    (DOCS / "April_Again_Complete_Screenplay.md").write_text("\n\n".join(body for _, body in documents), encoding="utf-8")
    write_json(OUT / "common.json", common_data)
    write_json(OUT / "rules.json", contracts())
    write_json(OUT / "locations.json", LOCATIONS)
    write_json(OUT / "asset-plan.json", plan)
    write_json(ROOT / "Narrative/validation-report.json", report)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
