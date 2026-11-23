from story_schema import c, s, e

ID = "svea"
NAME = "Kurokawa Svea"
VOICE = "Blunt, relaxed, short replies and dry humor. Gets animated about basketball; otherwise doesn't waste words. Boku self-reference in Japanese; light roughness without constant insults. Actions carry affection. Comfortable with strength and independence, awkward about choosing closeness."
SCENES = [
s(1, "Pass It Here", "field", """
Stage: During a supervised sports activity block, a basketball rolls toward the MC. Svea waits by the hardcourt line with one hand raised.
Svea: Here.
MC: You're very confident in my throwing.
Svea: Not anymore. Bounce it.
Stage: He does. She catches the ball and turns toward the hoop, then notices his attendance sheet.
Svea: You're helping with the practice count?
MC: Apparently. Takahashi.
Svea: Kurokawa Svea. Svea's fine. Write down who actually shows up, not who says they'll come.
MC: Does that happen a lot?
Svea: Enough to be a sentence.
""", [
c("good", "Got it. Tell me if there's a better place to stand.", """Svea: Outside the line. Unless you want the ball to introduce itself again.
MC: Once was enough.
Svea: Fast learner."""),
c("neutral", "I'll watch from here and check the names.", """Svea: Fine. Teacher's by the equipment cart if something's missing.
MC: Including my ability to recognize anyone?
Svea: Point. I'll tell you."""),
c("bad", "You're pretty good for a girl.", """Svea: Pretty good for someone you've watched for eight seconds.
MC: I meant—
Svea: Yeah. Leave the last part off next time.""")], """
Stage: The block passes in drills, names and the occasional ball sent too far. Svea stays to collect the equipment after everyone else starts leaving.
MC: Do you do everything yourself?
Svea: No. You're holding the sheet.
Narration: She says it without looking up. I can't decide whether I've been thanked or assigned a permanent position.
Stage: A ball gets stuck behind the equipment cart. Before he can reach around it blindly, she points out the wheel that will roll over his shoe.
MC: You could've let me discover that.
Svea: Could've. Then I'd have to listen to the noise.
Narration: She pushes the cart while I retrieve the ball. It is a very small job for two people. Neither of us makes it larger.
""", ["basketball", "attendance_sheet", "equipment_cart"]),
s(2, "The Second Tray", "canteen", """
Stage: A sports-activity lunch has put half the first-year group in the canteen. Svea sits with a large meal and a second small bowl.
MC: Hungry?
Svea: No. Building a model of lunch. Yes, I'm hungry.
Stage: She shifts her bag off the empty chair with her foot.
Svea: Sit if you're sitting. Don't hover.
MC: I was checking whether someone was coming back.
Svea: The bag? It's had enough.
Narration: A strawberry-milk carton is half hidden behind her water bottle.
""", [
c("bad", "That's a lot of food. Are you sure you should eat all that?", """Svea: I'm sure I know when I'm hungry.
MC: I was just surprised.
Svea: You can be surprised quietly."""),
c("neutral", "What's good today?", """Svea: Chicken. Rice. The small bowl is also rice.
MC: A focused review.
Svea: You asked what was good."""),
c("good", "I've got a side dish I won't finish. Want it, or are you set?", """Svea: If you actually don't want it. Don't give away your lunch to be polite.
MC: I actually don't want it.
Svea: Then yeah. Thanks.""")], """
Stage: We eat, then compare the equipment count for the next practice. She notices an absent name without checking the sheet.
MC: You remember everybody?
Svea: The ones who borrow balls and forget to return them. Useful talent.
""", ["lunch_trays", "strawberry_milk", "equipment_list"]),
s(3, "Five More Minutes", "class_c", """
Stage: A supervised independent-study block is quiet enough that Svea has fallen asleep over an open workbook. Her hair hides most of her face.
MC: Svea. The teacher said we have to turn the sheet in before the end.
Svea: Mm. Heard.
Stage: She has not, in any useful sense, woken up. The MC puts the spare worksheet on the desk where she can see it.
MC: You want a reminder in five minutes?
Svea: Two. Five turns into twenty.
Narration: Her phone is inside her closed bag. It would be easy to make this somebody else's entertainment.
""", [
c("neutral", "I'll leave the sheet here. The teacher's still at the front.", """Svea: Got it.
MC: Did you hear that one?
Svea: Annoyingly, yes."""),
c("good", "Two minutes. Then I'll wake you once and let you handle it.", """Svea: Deal. Don't shake the desk.
MC: Bad previous experience?
Svea: Brother. Coffee. Long story. Bad ending."""),
c("bad", "I should get a picture of this before you wake up.", """Svea: No.
MC: I was joking.
Svea: Great. Keep it imaginary.""")], """
Stage: She wakes, washes her face at the corridor sink and finishes the worksheet. The teacher checks it before the block ends.
Svea: Didn't miss anything important?
MC: Several thrilling minutes of me not understanding question four.
Svea: Show me. I was awake for that lesson. Mostly.
""", ["workbook", "worksheet", "closed_bag"], "sleepy"),
s(4, "The Carton", "canteen", """
Stage: We finish an equipment-budget exercise over lunch. Svea returns from the vending machine with strawberry milk and catches the MC looking.
Svea: What.
MC: Nothing.
Svea: That's an active-looking nothing.
Narration: She puts the carton behind her notebook, where it remains entirely recognizable.
MC: I was going to ask if it was good.
Svea: It's milk. Strawberry happened to it. You can work out the rest.
""", [
c("good", "Fair. I'll try one. You don't need to review it for me.", """Svea: Don't buy it because I did.
MC: I do occasionally want things on my own.
Svea: Useful quality. Keep it."""),
c("bad", "That's adorable. I didn't know you had such a cute side.", """Svea: It's a drink. Don't make it a whole event.
MC: I meant it nicely.
Svea: Then stop when I ask."""),
c("neutral", "I'll stick with coffee. Back to the numbers?", """Svea: Please. The calculator doesn't stare at my lunch.
MC: I'll learn from its example.
Svea: Good role model.""")], """
Stage: She finishes the milk and puts the empty carton with the recycling instead of hiding it in her bag.
Svea: The big pack of markers is cheaper per piece.
MC: We need six. The big pack has forty.
Svea: Right. My household's usually the big-pack version.
""", ["strawberry_milk", "notebook", "budget_exercise"], "flustered"),
s(5, "A Better Question", "field", """
Stage: The MC helps record a practice drill. Svea watches the numbers with more interest than the score.
MC: You made fewer shots than last time.
Svea: Different distance. Faster pass. Can't compare the total without that.
MC: Then what should I compare?
Stage: She takes the sheet and starts explaining foot position, shot selection and why a bad pass makes an ordinary catch look clumsy.
Narration: Three minutes pass before she realizes she has been talking without interruption.
Svea: ...You still listening?
""", [
c("neutral", "Most of it. I might need the short version for the sheet.", """Svea: Distance, attempts, clean catches. Three columns.
MC: That I can do.
Svea: Start there. Ask about the rest later."""),
c("bad", "You're more talkative when you're trying to show off.", """Svea: You asked a question.
MC: I didn't expect the lecture.
Svea: Fine. Write the number. I'll keep the rest."""),
c("good", "Yeah. Why does the clean catch matter more than the total?", """Svea: Because it tells me whether the next move started right. The shot's later.
MC: So we're checking the part you can fix first.
Svea: Exactly. See? Not that complicated.""")], """
Stage: The next set is easier to record and harder to shoot. Svea notices one improvement before checking the final total.
Svea: Better.
MC: You or my columns?
Svea: Both. Don't get greedy.
Stage: With the drill finished, she offers him one attempt from the same marker. The ball falls short enough that neither of them can pretend otherwise.
MC: I think the hoop moved.
Svea: Whole building must be in on it. Try bending your knees.
Narration: The second try touches the rim. She nods once, a more useful reaction than pretending it went in.
""", ["practice_statistics", "basketball"], variants={
"warm": "Svea: I thought of something to show you. Since you actually ask about this stuff.",
"mixed": "Svea: If you're helping, might as well know what we're counting.",
"cool": "Svea: Just tell me if you don't want the explanation. I don't do guessing games."}),
s(6, "The Line Was Out", "field", """
Stage: During a supervised practice game, a disputed ball gives Svea's side an extra possession. The MC saw the ball cross the line before she caught it.
Svea: It was out.
Classmate: Nobody called it. Keep playing.
Svea: I'm calling it now.
Stage: The instructor resets possession. Svea's side loses the short game by one point.
MC: That's an annoying margin.
Svea: Yeah. Still out.
Narration: She starts collecting the cones. Her movements are sharper than usual.
""", [
c("bad", "You could've kept quiet. Winning would've made everyone happier.", """Svea: Not everyone. Other team's in the game too.
MC: Your team would've liked it.
Svea: They can like a win we actually earned."""),
c("good", "You made the right call. You can still be annoyed about losing.", """Svea: Good. Because I'm annoyed.
MC: I noticed.
Svea: Subtle, wasn't I."""),
c("neutral", "Want to look at the last play once you've cooled down?", """Svea: Later. Need to be annoyed at the cones first.
MC: I'll take the innocent ones.
Svea: All innocent. That's what makes it difficult.""")], """
Stage: By the end of the block, she can point out the missed defensive switch without blaming the line call.
Svea: Next time I want a bigger margin.
MC: So one honest decision won't decide it?
Svea: So we play better. Same thing, if we're lucky.
""", ["court_cones", "basketball"], "annoyed"),
s(7, "Nothing on the Zip", "class_c", """
Stage: A quiet study block is interrupted when Svea's pencil case jams inside her sports bag. A tiny plush dog hangs from an inner zip.
MC: I think its ear is caught.
Svea: Don't pull. You'll rip it.
Stage: She carefully works the pencil case free, then catches herself holding the plush dog with both hands.
Svea: Brother gave it to me. Stupid joke.
Narration: The little dog is clean, repaired at one seam and very clearly not neglected.
MC: A long-running stupid joke, then.
""", [
c("neutral", "Glad you got it loose. Do you need the spare pen?", """Svea: Yeah. Mine's disappeared into the bag's other dimension.
MC: A common problem.
Svea: Terrible design. Holds everything except what I want."""),
c("good", "It looks well looked after. I'll leave it at that.", """Svea: ...Good.
MC: You don't have to explain everything you like.
Svea: Wasn't planning to. Thanks, though."""),
c("bad", "Come on, let me show the others. They'll love this.", """Svea: It's in the inside pocket for a reason.
MC: You don't need to be embarrassed.
Svea: I don't need you making that decision for me either.""")], """
Stage: The bag closes. We finish the worksheet with one borrowed pen and no audience for the little dog.
Svea: Your answer to five's wrong.
MC: I was trying a creative approach.
Svea: Math hates those.
""", ["sports_bag", "plush_dog_keychain", "pencil_case"], "flustered"),
s(8, "The Animal Schedule", "gate", """
Stage: A school volunteer block includes moving supplies from the gate store. Svea pauses to ask the groundskeeper about a neighborhood dog waiting outside with its owner.
MC: You know the dog?
Svea: It walks past around this time. Usually carries a stick that's too big for its own plans.
Stage: The owner permits a brief greeting. Svea crouches, lets the dog approach and gives its ears a careful rub.
MC: You watch for it?
Svea: It's a big dog with a tree branch. Hard to miss.
Narration: Today it has no branch. Svea has noticed that too.
""", [
c("good", "I'll take the light box. You can finish saying hello.", """Svea: Two minutes.
MC: Negotiating with me or the dog?
Svea: Dog's got better arguments."""),
c("bad", "You act tough, but you're secretly soft about everything.", """Svea: I'm not acting.
MC: You know what I mean.
Svea: I like dogs. Still me. Shouldn't be that confusing."""),
c("neutral", "I'll ask the groundskeeper where the boxes go.", """Svea: Store cupboard on the left. I'll get the heavy one.
MC: We can carry it together if it needs two people.
Svea: We'll check the box before getting philosophical.""")], """
Stage: The owner and dog leave. Svea helps carry the remaining boxes, accepts a second pair of hands for the awkward one and does not turn it into a competition.
Svea: Dog's back tomorrow, probably.
MC: With the branch?
Svea: Ambitious creature. I wouldn't rule it out.
MC: Would you want a dog of your own?
Svea: Yeah. When I've got time to look after it properly. Not fair to pick one up because it's cute and leave everyone else doing the work.
MC: Already thought about it, then.
Svea: Obviously. Next question.
""", ["supply_boxes", "neighborhood_dog"], "soft_smile"),
s(9, "How Was Practice?", "canteen", """
Stage: After a demanding supervised workshop, Svea eats more slowly than usual. The coach has already checked the group and told everyone to rest; nobody is injured.
MC: How was it?
Svea: Fine.
MC: Fine as in good, or fine as in you don't feel like talking?
Stage: She looks up from her tray. It is the question, not the food, that catches her off guard.
Svea: Tiring. Useful. Little bit irritating. Pick three.
MC: All three accepted.
""", [
c("bad", "You don't need to pretend you're strong with me.", """Svea: I'm not pretending. I'm tired.
MC: I meant you can be honest.
Svea: I just was. Don't invent a different answer."""),
c("neutral", "Want to leave the practice report until after lunch?", """Svea: Yeah. Food first. Numbers can survive a delay.
MC: They don't cool down as fast.
Svea: Finally, a useful difference."""),
c("good", "Want to talk about the irritating part, or eat in peace?", """Svea: Peace first. Maybe the rest after.
MC: Deal.
Svea: ...Thanks for asking like that.""")], """
Stage: After lunch, she explains a difficult drill in precise, enthusiastic detail. Nobody uncovers a secret wound. She had a hard practice and wanted someone to ask.
Narration: I almost make a joke about her talking more. I decide I'd rather hear the rest.
MC: For the record, my day was tiring and mostly not useful.
Svea: You asking me to pick three too?
MC: I haven't found the third one yet.
Svea: Hungry. Usually hungry.
Narration: She nudges the spare chopsticks toward me, then continues the story without making a ceremony out of the gesture.
""", ["lunch_tray", "practice_report"], "flustered"),
s(10, "Two Older Brothers", "class_c", """
Stage: An independent-study assignment asks students to describe a household routine. Svea has written 'Don't leave food unattended' at the top of her page.
MC: Is that a rule or a warning?
Svea: Family history. Two brothers. Anything without a name on it becomes public property.
MC: Yours must be peaceful when everyone's out.
Svea: Weirdly quiet. I like it. Then I miss the noise. Annoying system.
Stage: She draws three boxes for shared chores, then adds one for her father.
Svea: He taught us to handle ourselves. Doesn't mean we never eat together.
""", [
c("good", "What do you like doing with them when nobody's competing?", """Svea: We watch old games. Cook too much. Complain about who's blocking the screen.
MC: Sounds competitive anyway.
Svea: Yeah. Bad example. Good evening, though."""),
c("bad", "That explains why you're basically one of the guys.", """Svea: Explains why I have brothers. I'm still a girl, Takahashi.
MC: I didn't mean it as an insult.
Svea: Then say what you mean without replacing who I am."""),
c("neutral", "Your house sounds livelier than mine.", """Svea: Come by at dinner and you'll hear it from the street.
MC: Is that an invitation?
Svea: That's a noise warning. Don't sprint ahead.""")], """
Stage: She finishes the assignment with one unexpectedly fond paragraph about a meal that went wrong. The teacher asks for fewer complaints about stolen leftovers; she underlines 'fewer.'
MC: A negotiator.
Svea: Need room to work.
""", ["household_worksheet"], variants={
"warm": "Svea: You'd probably get along with them. Don't look pleased. That's also a warning.",
"mixed": "Svea: Don't read too much into the assignment. It's just what home's like.",
"cool": "Svea: I'd rather you ask than decide you already understand me."}),
s(11, "A Thing That Doesn't Need Winning", "class_c", """
Stage: During a club-day break, Svea takes a small handheld game from her bag. It features a tiny house, a vegetable patch and no obvious enemies.
MC: Where's the scoreboard?
Svea: There isn't one.
MC: Are you all right?
Svea: Give me that attitude again and you can weed the garden.
Stage: She shows him a crooked fence she has spent twenty minutes adjusting.
MC: You could just leave it.
Svea: Could. Don't want to.
""", [
c("neutral", "I like the little house. Did you choose the colors?", """Svea: Yeah. Roof took ages.
MC: Worth it?
Svea: Obviously. Look at the roof."""),
c("good", "Can I try for a minute? You can tell me if I mess up your fence.", """Svea: You can't ruin it permanently. Probably.
MC: Encouraging.
Svea: Save button's there. Use it before getting ambitious."""),
c("bad", "This is a weird game for you. I thought you liked a challenge.", """Svea: I like different things.
MC: It just doesn't fit the image.
Svea: Then fix the image. Game's fine.""")], """
Stage: They put the handheld away before the supervised activity resumes. The fence remains crooked by one small square.
MC: You're leaving it?
Svea: For now. Need something to be unreasonable about tomorrow.
Narration: She zips the game into the same inside pocket as the plush dog.
MC: You ever let your brothers play that one?
Svea: Once. One planted the whole field in turnips. Called it a business strategy.
MC: Did it work?
Svea: Worked for him. I had to water them.
Narration: She looks so sincerely offended by the memory that I laugh. Her mouth twitches. She has been waiting for that reaction.
""", ["handheld_game", "cozy_game_screen"], "smirk"),
s(12, "The Empty Afternoon", "field", """
Stage: The coach ends practice early, leaving a supervised free-activity period. Svea keeps holding the ball after the others head toward the building.
MC: Another set?
Svea: Could do. Don't need one.
MC: Is there something else you want to do?
Stage: She bounces the ball once. Her answer takes longer than any basketball explanation.
Svea: Was thinking we could sit for a bit. If you're not busy.
Narration: She studies the court line with intense and completely unnecessary attention.
""", [
c("bad", "Finally admitting you need me around?", """Svea: No. Asking if you want to sit down.
MC: I was teasing.
Svea: Pick a better target."""),
c("good", "I'd like that. You can just want company.", """Svea: Yeah. I know.
MC: I'll stop explaining the invitation you already made.
Svea: Good. Bench is over there."""),
c("neutral", "Sure. I have until the block ends.", """Svea: Same. We should return the ball first.
MC: Very responsible.
Svea: Don't sound shocked. I know where things belong.""")], """
Stage: They return the ball and sit at the field-side bench. Svea talks about a game she watched with her brothers, then asks the MC what he does at home.
MC: Mostly games. Homework, occasionally. Telling myself I'll go to bed before I start another video.
Svea: Great. At least one shared bad habit.
MC: Which one?
Svea: Sleep. Keep up.
Narration: It's an ordinary question. I still take a moment to enjoy being asked.
""", ["basketball", "field_bench"], "flustered"),
s(13, "The Blunt Part", "class_c", """
Stage: A group assignment ends with Svea telling a struggling classmate to stop making excuses. The classmate goes quiet. Later, she looks at the unfinished sheet.
Svea: That went badly.
MC: He'd been asking for help with the first step.
Svea: Sounded like he was giving up.
MC: Maybe both can sound the same when someone's embarrassed.
Stage: She taps her pencil against the desk, then stops before it becomes annoying.
Svea: I don't want to spend twenty minutes dressing up three words. Also don't want to be a jerk. Suggestions?
""", [
c("good", "Say what you got wrong, then ask if he still wants help with the step.", """Svea: Short apology. Actual question. Can do that.
MC: And let him answer.
Svea: Yeah. The difficult bit. Still can do it."""),
c("neutral", "Give him a minute before you go over.", """Svea: Fine. I'll make sure I don't use the minute to talk myself out of it.
MC: You know yourself.
Svea: Usually. Other people take longer."""),
c("bad", "He was too sensitive. You shouldn't have to change how you talk.", """Svea: I can mean something and still say it badly.
MC: You were trying to help.
Svea: Didn't help. That's the part I'm checking.""")], """
Stage: Svea apologizes plainly to the classmate and offers help. He chooses to finish the first step himself, then asks her to check it. She waits.
MC: How was that?
Svea: Awkward. Useful. Survived.
Narration: A fair review of the afternoon.
""", ["group_assignment", "pencil"], "annoyed"),
s(14, "After Practice", "field", """
Stage: The last scheduled practice-help block ends. Svea checks the equipment list and puts the final ball away before meeting the MC by the bench.
Svea: You don't need to keep helping with the count. Teacher's got the new rota.
MC: I'm retired?
Svea: From counting. Try to adjust.
Stage: She has two unopened strawberry-milk cartons in her bag. She takes one out, considers the second and leaves it where it can be seen.
Svea: I was going to ask you something. Another day, when we're not pretending it's equipment work.
MC: You can ask now if you want.
Svea: I can also take a minute. That's allowed, right?
""", [
c("neutral", "Sure. Tell me when you've worked out what you want to say.", """Svea: Next time we're here. After the supervised block.
MC: I'll come by the bench.
Svea: Good."""),
c("bad", "You bought two drinks. You can stop acting like you don't like me.", """Svea: I wasn't asking you to announce my answer for me.
MC: I thought it was pretty clear.
Svea: Then you can handle letting me say it."""),
c("good", "Take the minute. I'd rather hear what you choose to say.", """Svea: ...Yeah. Thanks.
MC: I can still accept the milk, if that one's for me.
Svea: It is. Don't make me regret the purchase.""")], """
Stage: She hands him the spare carton, or sets it on the bench with a brief 'If you want it' if he has made the exchange awkward. They leave before the gate closes.
Narration: The next conversation will happen without a sheet to fill in. I realize I've stopped looking forward to the sheet anyway.
""", ["equipment_list", "two_strawberry_milk"], variants={
"warm": "Svea: Kept thinking of things to tell you during practice. Distracting. Not entirely bad.",
"mixed": "Svea: We should figure out what we're doing. Preferably with actual words.",
"cool": "Svea: I want to clear a few things up. You don't have to guess the point before I get there."}),
s(15, "Your Choice, My Choice", "field", """
Stage: Finale encounter; show the route-ending warning. The hardcourt is quiet within the open-school block. Svea stands with the ball under one arm; the coach is collecting equipment in the distance.
Svea: Right. No attendance sheet. No homework. We can probably manage one conversation.
MC: I like you. I'd like to go on a date.
Svea: Good. Straight to it.
Narration: Her ears have gone slightly pink. She looks at the ball, then deliberately back at me.
Svea: I'm not great at this part. Doesn't mean somebody gets to do it for me.
""", [
c("good", "I'd like to be someone you choose to spend time with. Do you want that too?", """Svea: That's the question.
MC: Your answer, then.
Svea: Yeah. Let me get it out."""),
c("neutral", "We can try spending time together and be honest if it doesn't feel right.", """Svea: Fair. No pretending because someone asked nicely.
MC: Agreed.
Svea: Good. Here's where I'm at."""),
c("bad", "You don't have to act so independent. I'll be the one you rely on.", """Svea: I wasn't auditioning for someone to take over.
MC: I meant I'd be there for you.
Svea: Then be here and listen to what I'm saying.""")], """
Stage: Record this choice once, compare effective good and bad totals, and play only the corresponding ending. The shared scene does not assume she accepts.
""", ["basketball"], variants={
"warm": "Svea: Been looking forward to this. Don't grin. Makes it harder to say.",
"mixed": "Svea: Thought about it. A lot. Need to tell you properly.",
"cool": "Svea: I came to be clear. Let me finish, even if you don't like the answer."})
]

ENDINGS = [
e("good", "One More Pass", "field", "Svea at the school hardcourt in clean late-afternoon light, feminine face and shaggy blue-black hair, rare soft smile while offering the basketball to a charcoal MC silhouette; loose blazer and uniform trousers, easy equal posture.", """
Svea: Yeah. I want that. A date. With you, before you come up with some terrible follow-up question.
MC: I was trying to think of a good one.
Svea: Dangerous use of time.
Stage: She offers him the ball. When he takes it, she keeps her fingers against his for a brief moment, then lets go with a flushed, annoyed glance at herself.
MC: We could get lunch on Saturday.
Svea: Actual lunch. Don't pick somewhere with decorative portions.
MC: I have learned at least one thing about you.
Svea: Hopefully more than one.
Narration: She takes the ball back and bounces it once, collecting herself. Her smile returns before she can hide it.
Svea: I was fine on my own. Still am.
MC: I know.
Svea: Good. I want you here anyway.
Stage: The coach calls for the last ball. They return it together, then walk toward the gate with time left to spare.
Narration: I don't need to find a weakness that makes her stay. She's beside me because she wants to be, and she's finally said it plainly enough that even I can't miss it.
Stage: Unlock Svea / Good. Credits, then title.
"""),
e("neutral", "Same Side of the Court", "field", "Svea and a charcoal MC silhouette exchange a relaxed friendly fist bump at the hardcourt boundary; sports bag between them, normal daylight, comfortable friendship without romantic framing.", """
Svea: I like you. Not in the dating way. Took a while to be sure, but I'm sure now.
MC: All right.
Svea: You can look disappointed. I'm not going to tell you how to take it.
Narration: That blunt permission is unexpectedly useful. I let out the breath I've been holding.
MC: I am disappointed. I still like being around you.
Svea: Then take the time you need. Court isn't going anywhere.
Stage: Several school days later, the MC joins a supervised casual game. Svea passes him the ball at an entirely reasonable speed and looks surprised when he catches it cleanly.
MC: Training paid off.
Svea: One catch. Don't give a speech.
Stage: Afterwards, she offers a fist bump. He returns it.
Narration: Nothing secret is being promised. I don't have to pretend I never wanted more, but I can enjoy being on the same side of the court without treating the game as another chance to win her over.
Svea: Lunch?
MC: Actual lunch?
Svea: Good. You remember.
Stage: Unlock Svea / Neutral. Credits, then title.
"""),
e("bad", "The Next Practice", "field", "Svea leaves the quiet hardcourt with a basketball under her arm, looking forward; an empty bench behind her, cool natural late light, steady resolved expression. She remains strong and self-directed.", """
Svea: No. I don't want to date you. I'd rather we stop meeting like this for a while.
MC: I didn't think things were that bad.
Svea: I kept telling you when something bothered me. Too often, you treated it like I was putting on an act you had to get past.
Narration: She shifts the ball under her arm and waits. There isn't a hidden smile underneath the answer.
MC: I understand. I'll give you space.
Svea: Good.
Stage: She returns the ball to the coach and collects her bag. The MC stays by the bench while she walks toward the building.
Narration: I had wanted to be the person who saw some secret softer version of her. She was showing me who she was all along: hungry after practice, bad at lying, kind to animals, tired some days, interested in her own life.
MC: Good luck at the next practice.
Svea: Thanks. Take care, Takahashi.
Stage: She leaves. He doesn't call after her or turn her refusal into one last challenge.
Narration: Tomorrow she'll still have a court, a team and things she wants to do. I need to learn how to care about somebody without making myself the reason for all of them.
Stage: Unlock Svea / Bad. Credits, then title.
""")]
