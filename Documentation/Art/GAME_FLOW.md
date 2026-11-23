# April, again — rules that the asset pack supports

Status: early planning note, superseded by the completed screenplay and `Narrative/Screenplay/06_Production_Notes.md`. Use `Assets/AprilAgain/Narrative/asset-plan.json` for current story-derived requirements. In particular, Saturday-only appointments, exact scene wardrobes and the written epilogues now take precedence over these initial CG ideas.

## Premise

An ordinary, unlucky-in-love boy enters a prestigious Japanese high school. His first lesson is to notice people before imagining a romance with them. The five girls are fellow first-year students with their own interests, responsibilities and routines.

## Opening day

Entrance ceremony and a guided campus walk introduce school life. The player observes all five girls once, in any order. Katya quietly corrects an orientation display in the corridor; Akira helps a confused student in the lobby; Seo-yun sketches the sky by a library window; Mari sets an extra bento beside a resting classmate in the infirmary; Svea practices a free throw on the sports field. These are observation vignettes, not conversations and not scored route scenes. A five-entry journal checklist prevents missing a girl. Observation never consumes daily interaction slots. After all five, the MC can go home and sleep.

## Days and time

Normal school days have two social blocks, 12:00–15:00 and 15:00–18:00; morning classes are automatic. Club/open-campus days add 09:00–12:00, for three. A three-hour encounter includes the surrounding shared lesson, work or activity and travel; it does not mean three hours of standing in a corridor talking. Classroom attendance remains part of the story. The calendar spans the first term; the title names the beginning, not a forced 30-day limit.

Navigation, looking at scenery, checking schedules and non-scoring acknowledgements cost no block. An encounter confirmation explicitly displays '+3 hours' and remaining blocks. Each girl's next numbered scene can occur at most once per day. Every meaningful encounter consumes one block even after a bad choice. The player can go home early; otherwise the final block leads to an evening home prompt. Sleep advances exactly one day and resets the daily interaction set, not route progress or scores. No overnight school roaming.

No missed-scene failure: a girl's next scene waits for the next appropriate scheduled location. The journal shows where she is expected and whether a story encounter is available. Scene-specific appointments override her normal routine and appear in the journal. Never silently place two versions of the same girl in different rooms in the same block. No paid gifts, random affinity decay, or grind interactions.

## Weekly routine template

| Girl | Morning / club block | Midday | Late afternoon |
|---|---|---|---|
| Katya | Class B / orientation organization | Corridor or Class B | Class B council preparation; field-side fencing conditioning on club days |
| Akira | Class A / tech-project group | Canteen or lobby | Class A project work; library research on alternate days |
| Seo-yun | Class C / quiet reading | Library | Library or corridor window sketching |
| Mari | Class B / study | Infirmary or canteen | Infirmary reading/rest; lobby before leaving |
| Svea | Class C / open court | Canteen | Sports field basketball; classroom on rainy days |

All locations in the template exist in the supplied campus. Infirmary scenes require nurse permission and do not turn Mari into staff. Fencing drills stay away from basketball play. The outdoor sports field includes a fenced hardcourt at its near edge. Club-day third slots add variety, not mandatory progress. The final implementation must provide at least two available unvisited girls per normal day and three per club day, with a wait/home option if the player declines them.

## Routes, scoring and endings

Each girl has exactly 15 numbered, one-time scored scenes. Each scene contains one consequential choice with three authored responses and distinct immediate reactions. Choices represent listening/boundaries, indifference/misunderstanding and disregard/manipulation in context; the good choice must not simply mean agreeing with everything she says. A neutral choice is plausible, not a joke answer. Bad outcomes are distance or a broken relationship, not punishment through injury/death.

Store raw G, B, N counts. Effective good = G + N; effective bad = B + N. After scene 15, good > bad selects the good CG/epilogue, bad > good selects the bad CG/epilogue, equality selects the neutral CG/epilogue. Neutral adds one to BOTH categories, exactly as requested; it cancels from the comparison. All-neutral choices therefore yield neutral. Do not accidentally count neutral as two extra interactions or use percentage thresholds inconsistent with this rule.

The first completed route ends the current playthrough after its epilogue. Show a confirmation before starting scene 15, and create an automatic pre-finale save during gameplay implementation. Global ending gallery unlocks survive starting a new game. Save files preserve day, slot, location, observed-girl flags, route scene indices, raw counts and today's encountered IDs. Reloading restores the snapshot without duplicating a score. Completed scenes are not farmable through Back or repeated clicks. No implementation of these rules is claimed by this art milestone.

## Ending art briefs

Each route receives three separate full illustrations, not one image tinted three ways. The MC appears only as a neutral dark-grey uniformed silhouette where useful; faces remain unidentified. No explicit intimacy.

| Route | Good ending | Neutral ending | Bad ending |
|---|---|---|---|
| Katya | She accepts an ordinary melonpan beside the gate, sincere small smile, MC beside her | An orderly desk with her fencing/council folder between them; cordial farewell | She closes the folder alone in Class B, a second chair empty in cool late light |
| Akira | Side-by-side class project demo, her glasses and grin unmistakable, two hands meeting over a shared notebook | Friendly canteen project wrap-up across a table, friendly distance | Empty project seat beside her in Class A; she quietly puts away a disconnected laptop |
| Seo-yun | Library window, she shares her sky sketch with MC, open future and equal companionship | She leaves a handwritten bookmark on a returned library book, kind friendship | By the library window, she closes her journal and turns away toward her own future |
| Mari | Infirmary window bench, she finally rests with her own tea while MC sits quietly beside her | She and MC share a courteous tea break across two chairs, balanced and unhurried | She leaves the infirmary alone with her untouched cup, deciding to protect her boundaries |
| Svea | Court after practice, she offers MC the ball and chooses to stay, rare soft smile | A relaxed friendly fist bump at the court boundary, sports bag between them | She leaves the quiet court with ball under arm, looking forward rather than back |

## Writing milestone completed

The complete 75-encounter screenplay and 15 epilogues have been authored, reread and given a separate performed voice pass. Read `Narrative/Screenplay/April_Again_Complete_Screenplay.md`. Story-derived art production and a small playable opening-day slice follow; the current content exports are not a running game.
