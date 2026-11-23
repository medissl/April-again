from story_schema import lines

TITLE = "April, again"
SCHOOL = "Seiran High School"
MC = {"displayName": "Ren Takahashi", "presentation": "First-person narrator; ordinary male first-year. Peers initially use Takahashi; good epilogues can use Ren. Any visible body is an unidentifiable charcoal uniform silhouette.", "voice": "Self-aware and sometimes awkward, with dry everyday humor. He can make mistakes without every bad choice turning him into a deliberate bully. Rejection is disappointment, not proof that love or women are unfair."}

OPENING = [
{"id": "opening.bedroom", "title": "A New Uniform", "location": "bedroom", "lines": lines("""
Stage: Morning in a modest Japanese bedroom. School bag beside the desk; a new blazer hangs from the chair. The MC is not shown with a defined face.
Narration: The alarm goes off while I'm checking whether the alarm is set. A strong start.
MC: All right. I'm awake. We can both stop trying so hard.
Narration: Seiran High School. The name still looks strange on my admission papers. I checked the acceptance list twice, then a third time in case the first two were a shared misunderstanding.
Narration: Mum called it a fresh start. My old classmate called it 'a place where even the vending machines probably get better grades than us.'
Stage: He picks up a plain school tie and tries the knot again.
Narration: I also promised myself I wouldn't spend high school replaying junior high. The confession I postponed until she was already dating someone. The message I rewrote so many times that I sent it to the wrong group. The perfectly ordinary rejection I somehow turned into an entire season of embarrassment.
MC: No speeches this time. Learn people's names. Say hello like a normal person.
Narration: Manageable goals. I put on the blazer before I can add any more.
Stage: Continue to school gate. No player choice affects route scores.
""")},
{"id": "opening.gate", "title": "Seiran", "location": "gate", "lines": lines("""
Stage: A believable school gate on a spring morning. A few cherry branches, ordinary student silhouettes, tidy grounds; no palace-like campus.
Narration: The school is large enough to make me walk a little straighter. Not because anyone is watching. Because I can't quite believe they're letting me in.
Narration: Students move past in new uniforms and small nervous groups. I recognize nobody. Several people look as if they recognize nobody with more confidence than I do.
MC: Main entrance. Lobby. Ceremony. I can manage three destinations.
Stage: A teacher points incoming students toward the lobby. Only the lobby door is active until this transition finishes.
""")},
{"id": "opening.orientation", "title": "Keep the Map", "location": "class_a", "lines": lines("""
Stage: The entrance ceremony is represented by the seated classroom view, a brief fade and the public-address sound. Do not add a separate auditorium set for one transition.
PA: Welcome to Seiran High School. Please keep your orientation booklet with you during today's campus walk.
Narration: The ceremony contains advice about responsibility, opportunity and where to put indoor shoes. I write down the last part. It seems immediately useful.
Teacher: Takahashi, Ren? Good. You have a guided activity day. Visit the marked areas, learn the routes and return any forms before you leave. Ask staff if a door is closed.
Narration: I turn the little campus map the wrong way up, correct it and hope the student beside me hasn't noticed.
Teacher: Classrooms A, B and C share the main corridor. The library is at the east end, the infirmary at the west. Canteen, lobby and sports field are downstairs. Home is through the main gate, not through a classroom window.
Narration: A few people laugh. I decide I like teachers who plan for that possibility.
Stage: Unlock the campus map and free navigation. Five observation markers appear. No girl can be invited into a route encounter today.
""")}
]

OBSERVATIONS = [
{"id": "observe.katya", "girl": "katya", "title": "A Crooked Sign", "location": "corridor", "expression": "composed", "pose": "standing_with_folder", "props": ["orientation_sign", "folder"], "lines": lines("""
Stage: Katya stands beside a slightly crooked orientation sign. She is speaking to another student, not the MC.
Katya: The arrow points toward the stairs. The room is on this floor.
Classmate: It was like that when I got here.
Katya: Then we have discovered a problem without discovering a culprit. Hold this end, please.
Narration: Long silver hair, perfectly straight shoulders, a voice that makes fixing a paper sign sound like settling a formal dispute.
Stage: The sign comes loose. She catches it before it reaches the floor and immediately pretends that was the plan.
Katya: Bozhe moy... Slowly. We are moving paper, not launching it.
Narration: Someone calls her Katya. She checks that the arrow is right, then thanks the other student so quickly I nearly miss it.
MC: I'd better learn where that room is before she catches me following the old arrow.
Stage: The MC's last line is internal. Mark Katya observed; no conversation, score or time cost. Return to exploration.
"""), "repeat": "Narration: The sign is straight now. Katya is checking the next one. I leave her to the inspection."},
{"id": "observe.akira", "girl": "akira", "title": "Too Many Directions", "location": "lobby", "expression": "excited", "pose": "standing_with_satchel", "props": ["booklet", "keychain_satchel"], "lines": lines("""
Stage: Akira is showing a small group how to find their classrooms. Her glasses carry a tiny charm; her bag seems to carry a small shop's worth of souvenirs.
Akira: Left at the noticeboard, then the stairs. No, sorry—your left. I turned around halfway through my own instructions.
Classmate: Are you sure you're new here too?
Akira: Extremely new. I just got lost earlier than you did.
Stage: She laughs, flips the booklet and catches a loose keychain before it disappears under the bench.
Narration: Pink bob, brown eyes behind round glasses, three people listening and several explanations already waiting their turn.
Akira: I'm Akira. If we get lost together, it becomes a group activity.
Narration: The group goes with her. She hasn't noticed me standing by the vending machine, holding the same booklet as if it might eventually begin speaking.
Stage: Mark Akira observed. The MC doesn't join the group or speak to her. Return to exploration.
"""), "repeat": "Narration: Akira has found another group to help. Their map is facing the right way. Progress."},
{"id": "observe.seoyun", "girl": "seoyun", "title": "Before the Cloud Moves", "location": "library", "expression": "curious", "pose": "seated_sketching", "props": ["blue_journal", "pencil"], "lines": lines("""
Stage: Seo-yun sits by the library window with an open journal. Its writing is not readable from the MC's position.
Narration: The girl by the window draws a line, looks up and rubs it out again. Outside, a cloud moves beyond the edge of the roof.
Librarian: Seo-yun? We're putting the donated books over here.
Seo-yun: I'll be there in a moment. It keeps changing shape.
Librarian: The cloud?
Seo-yun: Yes. A rather inconsiderate subject.
Stage: She smiles to herself and closes the journal before standing. A small mole sits beneath her left eye.
Narration: I came in to find the library. For a moment, I forget to check what time it closes.
Stage: Mark Seo-yun observed. He does not approach or read the journal. Return to exploration.
"""), "repeat": "Narration: The journal is in her bag now. Seo-yun is helping the librarian sort a stack of books."},
{"id": "observe.mari", "girl": "mari", "title": "The Spare Lunch", "location": "infirmary", "expression": "warm", "pose": "standing_with_bento", "props": ["bento", "thermos", "visitor_chair"], "lines": lines("""
Stage: The infirmary door is open during orientation. Mari stands near the visitor table; the nurse is present. The MC remains at the public doorway.
Mari: If you haven't eaten, I have a spare lunch. You can say no. I brought it before I knew whether anyone would want it.
Classmate: Are you one of the older students helping today?
Mari: No. First year. Just as lost as everyone else, I suspect.
Nurse: Mari, eat yours too. I can see that lid is still closed.
Mari: Ah. Yes. In a moment.
Narration: Salmon-colored hair tied low, calm blue-green eyes, both hands carefully holding a lunch that isn't for her.
Stage: She sits at last. Before opening her own box, she moves a chair so the other student has somewhere to put their bag.
Narration: I check the infirmary mark on the map and keep walking. I don't need to invent a reason to go inside.
Stage: Mark Mari observed. No patient interaction, private information or conversation with the MC. Return to exploration.
"""), "repeat": "Narration: Mari is finally eating. The nurse seems satisfied with this particular medical outcome."},
{"id": "observe.svea", "girl": "svea", "title": "One Clean Shot", "location": "field", "expression": "focused", "pose": "standing_with_ball", "props": ["basketball", "sports_bag", "hoop"], "lines": lines("""
Stage: From the public path, the MC sees a supervised basketball orientation drill on the hardcourt beside the sports field.
Coach: One more, Svea. Then give the next group a turn.
Svea: Got it.
Stage: A girl with shaggy dark hair bounces the ball twice and shoots. It hits the rim. She catches the rebound without celebrating the effort or complaining about the miss.
Classmate: Thought you always got those.
Svea: You thought wrong. Watch your feet. They're over the line.
Narration: She passes the ball back and moves aside. A younger-looking student fumbles the next catch; she quietly slows the return pass.
Narration: Her shirt collar is loose, her blazer open, her expression hard to read. The careful pass tells me more than the expression does.
Stage: She picks up a sports bag, notices a small charm showing from the inner pocket and quickly zips it away.
Stage: Mark Svea observed. The MC stays off the court and does not talk to her. Return to exploration.
"""), "repeat": "Narration: Svea is collecting the balls. Even the ones she didn't send over the line."}
]

POST_TOUR = lines("""
Stage: All five observation flags are set. A journal checklist confirms the campus tour is complete. Unvisited ordinary rooms remain optional; Home is unlocked.
Narration: By the time I finish the tour, I know where to eat, where to return a book and which corridor sign is least likely to be wrong.
Narration: I also have five names in my head. Katya. Akira. Seo-yun. Mari. Svea.
MC: Learn people's names. That part worked.
Narration: I haven't had a proper conversation with any of them. For once, I'm going to let that be the beginning instead of treating it as a failure.
Stage: The Home action leads to the bedroom. It cannot start another school day until the player chooses Sleep.
""")

HOME_FIRST = lines("""
Stage: Evening bedroom. The blazer is on the same chair, less carefully than this morning. The map lies open on the desk.
Narration: The school felt less impossible from the inside. Mostly it was doors, people trying to find other doors, and teachers pretending we all knew where we were going.
MC: Nobody fell in love with me on sight. Tragic. I suppose I'll have to become someone they actually know.
Narration: I fold the map along the wrong crease, open it and try again.
MC: Tomorrow, then. A normal hello. I can start there.
Stage: Show Journal, Save and Sleep actions. Sleep advances to school day two. No route score changes.
""")

MORNING = [
lines("""Narration: The uniform takes less time today. The tie has not improved at the same speed.
MC: Close enough. School has a lot of people in it; one of them can probably explain knots.
Stage: Automatically attend morning lessons on normal school days. Open the current schedule at the first free block."""),
lines("""Narration: I check my bag before leaving. Book, homework, lunch, the pen I thought I'd lost yesterday.
MC: A rare complete set.
Stage: Continue through ordinary classes to the first social block. No repeated entrance-ceremony dialogue."""),
lines("""Narration: The alarm sounds slightly less personal this morning. Maybe I'm getting used to it.
MC: Or the batteries are tired. We have that in common.
Stage: Normal lessons happen automatically before the first social block."""),
lines("""Narration: The map stays on the desk. I know the route now.
MC: That's one kind of progress.
Stage: Attend classes, then open exploration at the first free block.""")
]

HOME = {
"full": lines("""Stage: Evening bedroom. The final school activity block is over.
Narration: I put my bag down and finally stop carrying the whole day on one shoulder.
MC: Homework, shower, sleep. An ambitious schedule.
Narration: A few things went well. A few things will sound different when I replay them later. I write down what I actually need to remember before the imagined versions take over.
Stage: Journal reflects the real choices and next appointments. Sleep advances one school day; replaying this text never resets scores."""),
"early": lines("""Stage: The MC has chosen to leave with at least one free block remaining. Confirm that returning home ends today's school activities.
Narration: I could stay longer. Today, I'd rather go home while I still have the energy to finish my own work.
MC: Leaving early isn't the same thing as missing everything.
Stage: Bedroom, early evening. No extra scene or score is awarded for saving time. Journal, Save and Sleep remain available."""),
"none": lines("""Stage: No scored encounter was completed today. This is a valid day, not a failure.
Narration: Some days are mostly classes and ordinary errands. Not every afternoon needs a scene worth retelling.
MC: Tomorrow I can check the schedule before deciding I've missed my chance.
Stage: Offer the next available appointment in the journal. If all pending scenes require an open-campus day, offer an explicit calendar fast-forward to that day."""),
"after_good": lines("""Narration: I remember the moment when I stopped trying to sound useful and actually listened. I'd like to notice it sooner next time.
Stage: Use only if today's last choice was good. This is reflection, not visible affinity arithmetic."""),
"after_bad": lines("""Narration: I didn't like how that conversation ended. Explaining what I meant won't help much if I never look at what I actually said.
Stage: Use only if today's last choice was bad. No magical score refund or forced apology scene."""),
"after_neutral": lines("""Narration: I'm still not sure how that came across. People don't come with an answer sheet. I can try asking more clearly next time.
Stage: Use only if today's last choice was neutral."""),
"sunday": lines("""Stage: After Saturday sleep, a brief bedroom/calendar transition covers Sunday. It is not a playable school activity day and awards no route progress.
Narration: Sunday goes to laundry, homework and an attempt to convince my room it has a floor. By evening, I know where my school bag is again.
Stage: Continue to Monday morning, with the calendar updated and daily-use flags reset only for the new playable day.""")
}

BARKS = {
"katya": {"busy": "Katya: I have a scheduled activity now. The noticeboard has my next free block. Please check before reserving my afternoon.", "used": "Katya: We have done enough for today. You still have your own work, I assume.", "tomorrow": "Katya: The next task can wait until the next school day. I would prefer you awake for it."},
"akira": {"busy": "Akira: Bad timing! Actual assigned thing. Check my next free block on the schedule. Consult the schedule before trusting me.", "used": "Akira: We've used up our project time. Go do something else before I accidentally start another idea.", "tomorrow": "Akira: Tomorrow? I should write that down before tomorrow becomes six different promises."},
"seoyun": {"busy": "Seo-yun: I need to finish this first. My next free period is in the journal, if you want to check.", "used": "Seo-yun: Let's leave the next part for another day. I would like time to think about it.", "tomorrow": "Seo-yun: Next school day, then. I'll bring the page we need."},
"mari": {"busy": "Mari: I can't stop now. We can talk during the next free block. It should be on the schedule.", "used": "Mari: We should both have some time to ourselves now. I'll see you another day.", "tomorrow": "Mari: Next time. And please don't skip your own plans because you think I'm waiting."},
"svea": {"busy": "Svea: Busy. Check the schedule. I'll still exist when practice ends.", "used": "Svea: Tomorrow. We've got other things to do today.", "tomorrow": "Svea: Same plan next school day. Get some sleep before then."}
}

SYSTEM = {
"start_scene": "Spend this block with {girl}? This encounter includes the surrounding school activity and advances time by 3 hours.",
"start_scene_buttons": ["Spend time together", "Keep exploring"],
"finale": "This is {girl}'s final scene. Finishing it ends this playthrough. A separate pre-finale save will be created before it begins.",
"finale_buttons": ["Continue to the final scene", "Not yet"],
"go_home": "Go home for today? You have {remaining} activity block(s) left. You can meet people again on later school days.",
"go_home_buttons": ["Go home", "Stay at school"],
"last_block": "The school activity day is over. Head home before the gate closes.",
"sleep": "Sleep and start the next school day? Today's route progress and choices will be kept.",
"sleep_buttons": ["Sleep", "Stay up a little"],
"wait": "Wait until the next activity block? Waiting advances 3 hours and does not change anyone's score.",
"club_wait": "The next available story scenes are on an open-campus day. Skip ordinary days until then? No route progress will be lost.",
"closed": "This room is closed during this block. Check the map for another route.",
"day_one_locked": "Finish the five observation stops before going home. They're marked in your journal.",
"observed": "Observation added: {girl}. {count}/5 first impressions recorded.",
"journal_locked_route": "You haven't spoken properly yet. Start with the next school-day introduction.",
"journal_next": "Next: {scene_title} — {location}, {block}. No earlier scene can be skipped.",
"already_today": "You have already spent a story block with {girl} today. Her next scene is available on a later school day.",
"ending_unlock": "Ending unlocked: {girl} — {ending}. Your gallery keeps this memory across new playthroughs.",
"save_success": "Saved.", "save_error": "Couldn't save. Your current session is still open. Try another slot or try again.",
"load_confirm": "Load this save? Unsaved progress in the current session will be replaced.",
"new_game_confirm": "Start a new story? Saved slots and unlocked endings will be kept.",
"skip_hint": "Skip stops at unread dialogue and choices.",
"choices_policy": "Never reveal good/bad/neutral labels in the player-facing choice menu. Present each choice as authored, with keyboard focus and no time limit. Choices commit once; replaying a text line cannot score again."
}
