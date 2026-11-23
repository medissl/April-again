from story_schema import c, s, e

ID = "mari"
NAME = "Yasuko Mari"
VOICE = "Soft, attentive and gently practical. Notices sleeves, uneaten food and tired eyes. Deflects attention by caring for the other person. Small hesitations reveal uncertainty; her humor is quiet. A first-year peer, never the nurse or the MC's mother."
SCENES = [
s(1, "The Spare Chair", "infirmary", """
Stage: The nurse asks two first-years to prepare a public noticeboard outside the infirmary rest area. No patient records or medical tasks are involved.
Mari: You can use this chair. The other one makes a terrible noise.
MC: You know that from experience?
Mari: Everyone knows when someone uses it. That's the difficulty.
Stage: She moves her bag off the good chair and notices a loose thread on the MC's cuff.
Mari: Your sleeve is caught on the button. May I?
MC: Oh. Yes, thanks.
Narration: She frees the thread, then steps back before I can feel that I'm being inspected.
Mari: Yasuko Mari. Mari is fine. The nurse said we're sorting the public leaflets today.
""", [
c("neutral", "I'm Takahashi. Which pile should I take?", """Mari: The ones with the blue heading. They're easiest to mix up.
MC: I can probably manage that.
Mari: Good. If either of us gets confused, we can ask."""),
c("bad", "You seem good at this. I'll let you do the careful parts.", """Mari: I can do them, but we were both asked to help.
MC: I meant I don't want to get in your way.
Mari: Then take a pile. That would help more."""),
c("good", "Thanks for the sleeve. You don't have to look after me while we're working.", """Mari: I wasn't... Ah. I suppose I was.
MC: I can keep track of my own buttons. Usually.
Mari: Then we'll trust you with the blue leaflets too.""")], """
Stage: We sort the public information sheets and ask the nurse to check them. The chair squeaks once when the MC forgets which one to use.
Mari: That one.
MC: I understand the warning now.
Narration: She covers a small laugh with her hand, as if we're in a library rather than an office with very loud furniture.
""", ["public_leaflets", "squeaky_chair"]),
s(2, "The Extra Lunch", "canteen", """
Stage: We work on noticeboard headings during a long lunch/activity block. Mari has two cloth-wrapped lunch boxes.
MC: Expecting company?
Mari: I pack lunches for my siblings in the morning. Sometimes my hands keep going after I've counted everyone.
MC: So the second one is an administrative error?
Mari: A rather nice one, I hope. You may have it if you like.
Stage: She starts explaining every part of the meal before opening her own box.
Narration: Her tea is still sealed. I haven't seen her take a bite.
""", [
c("good", "I'd like some. Let's both eat before the headings take over the table.", """Mari: They do seem to be multiplying.
MC: I'll move the scissors. You rescue your lunch.
Mari: Thank you. I almost forgot it was getting cold."""),
c("bad", "You should bring an extra one for me every day.", """Mari: Every day?
MC: If you already make too much.
Mari: I can offer you this one. I don't want that to become a promise I haven't made."""),
c("neutral", "Thanks, but I brought lunch. Could you save it for yourself later?", """Mari: I could. That hadn't quite occurred to me.
MC: Afternoons are long.
Mari: They are. I'll put it somewhere cool.""")], """
Stage: We put the work aside for lunch, then finish the headings afterwards.
Mari: I used to be better at making small portions.
MC: You could practice on yourself.
Mari: That sounds oddly difficult when you say it. I'll try.
""", ["two_bento", "thermos", "paper_headings"]),
s(3, "The Tea She Likes", "infirmary", """
Stage: The nurse permits a break at the visitor table while the noticeboard materials dry. Mari opens a thermos.
Mari: Barley tea. Mugicha. No caffeine, if that helps you decide.
MC: You carry an entire drinks menu in there?
Mari: Only the part people ask about most often.
Stage: She pours a cup for herself and pauses over the spare one.
MC: Is it your favorite?
Mari: Everyone at home likes it.
MC: I asked whether you do.
""", [
c("bad", "Come on, that shouldn't be a difficult question.", """Mari: I heard the question. I was thinking.
MC: I didn't mean to put you on the spot.
Mari: Then please give me a moment."""),
c("good", "You can think about it. I'm not testing you.", """Mari: I like the roasted smell. Especially before the first sip.
MC: That sounds like an answer.
Mari: It is, isn't it? Yes. I like it."""),
c("neutral", "I'll try a little, if there's enough.", """Mari: There is. I brought a spare cup.
MC: Of course you did.
Mari: I may be predictable about a few things.""")], """
Stage: We drink while the paper dries. Mari closes her eyes for a brief, unguarded breath over the warm cup.
Narration: It is the first thing I've seen her enjoy without first checking whether someone else needs it.
Mari: Better while it's warm. We should stop talking about it and drink.
""", ["thermos", "two_tea_cups", "drying_paper"], "peaceful"),
s(4, "Ask the Nurse", "infirmary", """
Stage: We hang the noticeboard sheets. A classmate asks Mari to fetch medicine while the nurse is briefly in the adjoining office.
Mari: Please ask the nurse when she comes back. I can't give you that.
Classmate: But you know where everything is.
Mari: That doesn't make me qualified to use it.
Stage: The classmate waits outside the office. Mari checks that the noticeboard is straight, then checks it again.
MC: Does that happen often?
Mari: People see me here and assume I'm useful in every possible way.
Narration: She gives a small smile, but there is very little amusement in it.
""", [
c("neutral", "We can put a staff-only label on that cupboard.", """Mari: The nurse has one. It might need to be more visible.
MC: Public information project finally finds its subject.
Mari: A useful discovery."""),
c("good", "You answered clearly. I'll back you up if they ask me.", """Mari: Thank you. I don't need you to argue with them.
MC: Just say the same thing.
Mari: Yes. That would be enough."""),
c("bad", "It would've been quicker to fetch it and let the nurse check later.", """Mari: No. The nurse needs to decide what is appropriate.
MC: I thought it was a small thing.
Mari: Then waiting for the right person is a small thing too.""")], """
Stage: The nurse handles the request. We finish the public noticeboard and leave the medical cupboards alone.
Mari: I like helping here. I still want to be allowed to sit in the quiet chair sometimes.
MC: We should put that in the leaflet.
Mari: Perhaps not in quite those words.
""", ["noticeboard", "staff_only_sign"], "concerned"),
s(5, "One Preference", "canteen", """
Stage: The canteen offers two desserts. Mari studies them long enough for the MC to notice.
MC: Custard or red bean?
Mari: Which would you prefer?
MC: I was asking you.
Mari: Ah. Of course.
Stage: She looks at the display again. The queue moves behind us.
Mari: You choose. I don't mind either.
Narration: It sounds easy until I notice her eyes return to the custard.
""", [
c("good", "I'm getting red bean. You can choose separately.", """Mari: Then... custard, please.
MC: There we are. Two desserts, no difficult negotiations.
Mari: I may have made that more complicated than necessary."""),
c("bad", "Just pick one. I can't decide everything for you.", """Mari: I wasn't asking you to decide everything.
MC: It feels like you never say what you want.
Mari: I was trying not to make a small thing difficult. I see that didn't work."""),
c("neutral", "We can skip dessert if you're not in the mood.", """Mari: No, I'd like one. The custard, I think.
MC: Custard it is.
Mari: Yes. Thank you for waiting.""")], """
Stage: We use the remaining block to review which public leaflets need replacing. Mari keeps the dessert wrapper out of the paperwork.
MC: Worth the decision?
Mari: Very. I may recklessly choose the same one next time.
Narration: Her smile reaches her eyes before she lowers them to the list.
""", ["custard_dessert", "red_bean_dessert", "leaflet_list"], variants={
"warm": "Mari: You remembered I liked the roasted tea too. I wasn't expecting you to remember.",
"mixed": "Mari: I know you mean well when you ask. Sometimes I need a little time to answer.",
"cool": "Mari: Let's keep today simple. We can each choose for ourselves."}),
s(6, "The Button", "class_b", """
Stage: A class craft block becomes an opportunity to repair loose buttons on the fabric display backing. Mari has brought a small sewing kit.
MC: You look prepared for every possible fabric emergency.
Mari: Only ordinary ones. Please don't invent a difficult one.
Stage: The MC's own blazer button comes loose while he reaches for the thread. Mari immediately sets down her work.
Mari: I can do that before it falls off.
MC: What about your part of the backing?
Mari: I'll finish it afterwards.
Narration: There is already a small queue of repairs beside her.
""", [
c("bad", "Thanks. You really are everyone's mum here.", """Mari: I'm your classmate.
MC: I meant you're reliable.
Mari: You can call me reliable. I would prefer that."""),
c("neutral", "It can wait until the backing's finished.", """Mari: Put the button somewhere safe if it comes off.
MC: Front pocket. I have a system.
Mari: Then I won't interrupt your system."""),
c("good", "Could you show me instead? I'd like to manage the next one myself.", """Mari: You don't need to make the stitches perfect. They only need to hold.
MC: A refreshing school assessment.
Mari: Give it here. I'll show you the first stitch; you can do the rest.""")], """
Stage: With Mari's demonstration if he requested it, or the class sewing guide if he did not, the MC secures his own button. Mari returns to her own work. His stitches are noticeably less neat than the display backing.
MC: I think the button has character now.
Mari: It has a great deal of thread. We can call that character.
""", ["sewing_kit", "loose_button", "fabric_backing"]),
s(7, "The Message From Home", "lobby", """
Stage: While we carry spare materials to the lobby, Mari receives a message asking her to collect groceries and help a sibling with homework that evening.
Mari: I should have expected that. It is their difficult subject this term.
MC: And you have your own assignment due.
Mari: I can do it later.
Stage: She shifts the box, trying to type an answer with her free thumb. The lid slides.
MC: Let me set this down first.
Mari: Sorry. Yes. Thank you.
Narration: She apologizes again when a folded cloth falls out, although nobody was hurt and nothing was damaged.
""", [
c("good", "What can you realistically do tonight? You can answer with that, not the best possible version of you.", """Mari: I can collect the groceries. The homework will need to be tomorrow, or someone else can help.
MC: That sounds clear.
Mari: It sounds strange. I'll try writing it before I change my mind."""),
c("neutral", "Can we finish the school task another day?", """Mari: We can ask the teacher. I'd rather not quietly leave it for you.
MC: Then we ask.
Mari: All right."""),
c("bad", "They need you. Your assignment can wait one night.", """Mari: It already waited last night.
MC: I didn't know.
Mari: No. I haven't been saying so. That doesn't make the time appear.""")], """
Stage: We finish the carry together. Mari sends a specific reply and receives a short acknowledgment. It doesn't solve every expectation at home, but tonight now has a limit.
Mari: I keep expecting a clear answer to sound unkind.
Narration: She reads her own message once more, then puts the phone away.
""", ["phone", "supply_box", "folded_cloth"], "concerned"),
s(8, "The Chair Is for Sitting", "infirmary", """
Stage: The nurse tells the student volunteers to take a break before doing anything else. Mari reaches for an untidy stack of clean blankets anyway.
Nurse: Mari. Chair first. Those can wait.
Mari: I was only going to fold the top two.
Nurse: They will survive their current condition.
Stage: Mari sits. The MC takes the other visitor chair, the one that squeaks.
MC: I think the chair is pleased to be useful.
Mari: You don't have to keep me company if you have something to do.
""", [
c("neutral", "I'll read quietly here until the break's over.", """Mari: All right. I won't ask what you're reading every thirty seconds.
MC: I'd appreciate that. I might not know yet.
Mari: A difficult book, then."""),
c("bad", "You worry too much. I'll make sure you rest from now on.", """Mari: I don't need someone else deciding my whole day.
MC: You weren't going to stop by yourself.
Mari: I can accept a reminder without giving up every decision."""),
c("good", "Would you prefer company or a little quiet on your own?", """Mari: Company. Quiet company, if that's all right.
MC: I can attempt that.
Mari: A brave promise, in that chair.""")], """
Stage: The break ends when the nurse checks in. Mari is tired but well; there is no collapse or romanticized illness. They finish only the assigned public materials, not extra work.
Mari: I didn't fold a single blanket.
MC: A terrible afternoon for blankets.
Mari: They seem to have managed.
""", ["visitor_chairs", "clean_blankets", "book"], "peaceful"),
s(9, "Before the Bell", "field", """
Stage: A supervised open-campus activity block starts early. The MC finds Mari finishing slow aikido practice on the quiet field edge before a general exercise workshop.
MC: I didn't know you did martial arts.
Mari: I usually practice before the house gets busy. It helps me begin the day with one thing at a time.
MC: You're good at making it look calm.
Mari: You didn't see the mornings when I forget which foot I'm using.
Stage: The instructor calls for everyone to put away the mats. Mari carries one, leaving the others for the group.
Narration: She catches me noticing and almost smiles.
""", [
c("good", "What do you enjoy about it when nobody needs you to be good at it?", """Mari: The moment when the movement starts to feel continuous. I stop counting things I haven't done yet.
MC: I'd like to find something that does that for me.
Mari: You could try the beginner session. Nobody starts graceful."""),
c("bad", "Remind me never to annoy you. You look harmless until you do that.", """Mari: I would rather you listened because I asked, not because you imagined I might hurt you.
MC: It was supposed to be a compliment.
Mari: Then tell me what you actually liked."""),
c("neutral", "Can I help carry that mat?", """Mari: There's another one by the fence. This one's light enough.
MC: Right. Separate jobs.
Mari: We appear to be learning.""")], """
Stage: The workshop fills the block with ordinary beginner exercises. Mari makes a mistake in front of the group, laughs at herself and tries again.
Narration: For once, nobody seems to need anything from her except that she enjoy being here.
""", ["practice_mat", "sports_bag"], "warm"),
s(10, "And You?", "infirmary", """
Stage: We check the public reading corner after classes. Mari listens while the MC admits he has been nervous about making friends at the new school.
MC: I keep thinking everyone else received instructions I missed.
Mari: I don't think they did. Some people are very confident while being just as confused.
MC: Are you?
Mari: Oh, I could find you the information sheet about new-school anxiety. The nurse has—
Stage: She stops when she sees the MC's expression.
Mari: You were asking about me.
""", [
c("neutral", "Only if you feel like answering.", """Mari: I am still learning what that feels like.
MC: We can leave the question open.
Mari: Thank you. I might come back to it."""),
c("good", "Yes. I don't need another leaflet. I'm interested in how you're doing.", """Mari: Tired, sometimes. And relieved to be somewhere that doesn't already know who I am supposed to be.
MC: You don't have to have a finished version ready for me.
Mari: I would like to believe that."""),
c("bad", "You don't need to hide behind helping people. Tell me what's really wrong.", """Mari: Please don't decide what my answer should be before I give it.
MC: I thought you needed a push.
Mari: I needed enough room to speak.""")], """
Stage: She returns the leaflet to its rack. They finish checking the reading-corner list without turning the conversation into a diagnosis or a confession.
Mari: I was worried that if I had nothing useful to offer, I'd have nothing to say.
Narration: She has already said more than she seemed to expect. I don't ask her to prove the point again.
""", ["leaflet_rack", "reading_list"], variants={
"warm": "Mari: When I see you coming, I feel glad before I start wondering what you might need. That is new.",
"mixed": "Mari: I know we keep trying to understand each other. Some days it comes more easily than others.",
"cool": "Mari: I can listen for a little while. I would like you to listen when I answer too."}),
s(11, "One Portion", "canteen", """
Stage: A cooking assignment uses the canteen tables after service, under staff supervision. Everyone must plan a simple lunch for themselves.
Mari: My little brother dislikes these mushrooms. My sister won't eat—
Stage: She looks down at the worksheet heading.
Mari: For myself. It says it quite clearly.
MC: What did you want before the household meeting began?
Mari: Mushrooms. Apparently I have been arguing against my own lunch.
Narration: She crosses out one substitution, then two.
""", [
c("bad", "You could make what your siblings like and take it home. That would be more useful.", """Mari: The assignment is one meal for me.
MC: I thought you'd be happier helping them.
Mari: I'm trying to find out what makes me happy without guessing it for someone else."""),
c("good", "Keep the mushrooms. You don't have to justify liking your own lunch.", """Mari: Then I'm keeping the ginger too.
MC: A dangerous wave of personal opinions.
Mari: Someone should alert the kitchen."""),
c("neutral", "Let's follow the worksheet first. We can change things after the taste test.", """Mari: A practical defense against my own habits.
MC: Schoolwork occasionally helps.
Mari: Please don't sound too surprised. The teacher might hear.""")], """
Stage: Staff supervise the food preparation. Mari eats her own finished portion and writes a note about what she would change next time.
Mari: More ginger.
MC: That seems settled.
Mari: It is. I like knowing that.
""", ["meal_worksheet", "lunch_plate", "apron"], "warm"),
s(12, "Not Tonight", "class_b", """
Stage: During independent study, Mari tells the MC she asked her family to share two evening tasks. The first conversation was awkward.
Mari: My father said I had always managed before. I didn't know how to explain that managing and managing well weren't always the same.
MC: Did he listen afterwards?
Mari: A little. My mother suggested a weekly plan. My siblings were mostly concerned about who would cook.
Stage: She opens a notebook with both her homework and the household plan on separate pages.
Mari: I still feel guilty about leaving a blank space after my name.
""", [
c("good", "What would make the plan workable for you? You don't have to fill the blank just because it bothers you.", """Mari: Two evenings for my own work. And one morning when I don't make everyone's lunch.
MC: Those are things you can put on the page.
Mari: Yes. Specific things. I can ask for specific things."""),
c("neutral", "Try the plan for a week before deciding whether it works.", """Mari: I can keep track of what actually happens, instead of only what I hoped would happen.
MC: That sounds fair.
Mari: I think so too."""),
c("bad", "Your family sounds awful. You should stop helping them completely.", """Mari: I love them. I am trying to change something, not erase them.
MC: I don't like how much they ask of you.
Mari: Neither do I, sometimes. Please let the conversation be more complicated than that.""")], """
Stage: They use the rest of the block for their own assignments. Mari writes her available evenings on the household page before closing the notebook.
Narration: Nothing is solved by a single conversation. At least the next one will begin with something she actually wants.
""", ["homework", "household_plan"], "concerned"),
s(13, "No One to Feed", "gate", """
Stage: The public-information project is finished for the day. Mari takes a short break by the gate before going home. A familiar neighborhood cat sleeps under a hedge.
MC: It seems to have beaten everyone to the good seat.
Mari: It has a strict schedule. Sleep here, sleep somewhere else, inspect people carrying food.
MC: Did you bring anything for it?
Mari: Not today. The groundskeeper said its owner would prefer us not to feed it.
Stage: She sits on the nearby bench with empty hands. For a moment, she seems unsure what to do with them.
Mari: I can still stay a little while, can't I?
""", [
c("neutral", "I'll stay until the activity block ends too.", """Mari: All right. We can be available if the teacher needs the display moved.
MC: And otherwise do absolutely nothing useful.
Mari: A demanding assignment."""),
c("bad", "You look happier when you're taking care of something.", """Mari: Do I need to be doing that to be good company?
MC: I meant it suits you.
Mari: It is part of me. I don't want it to be the only part you want here."""),
c("good", "Yes. You don't need a job to have a place on the bench.", """Mari: I was hoping you would say something like that.
MC: Should I have made it sound more impressive?
Mari: No. This was exactly enough.""")], """
Stage: The cat wakes, decides neither person has anything worth investigating and goes home.
Mari: Well. We have been thoroughly assessed.
MC: Low scores for catering.
Narration: She laughs without hiding it this time. We remain on the bench after the cat has gone.
""", ["gate_bench", "cat"], "warm"),
s(14, "Her Own Cup", "infirmary", """
Stage: The nurse checks the completed reading corner and thanks both students. Mari has no extra duty assigned today.
Nurse: You can use the visitor table during the break, but go home when the block ends. Both of you.
Mari: Understood.
Stage: Mari brings one small bag of tea and looks at the two cups on the tray.
MC: What's the plan?
Mari: I want to make myself a cup. You may have one if you like, but I'm not going to spend the break checking whether everyone in the corridor wants tea.
MC: A clear plan.
""", [
c("good", "Make yours first. I'll handle my own cup.", """Mari: The spare tea is in the small tin.
MC: I have received the necessary training.
Mari: Then I shall stop supervising. Probably."""),
c("neutral", "I'll just have water. You enjoy yours.", """Mari: Thank you. I will.
MC: No looking guilty about it.
Mari: I'll try. You're allowed to enjoy the water without supervising me too."""),
c("bad", "But helping everyone is what makes you special.", """Mari: I don't want to earn a place with you by being endlessly available.
MC: I didn't say endlessly.
Mari: I need you to hear the difference, even when you don't mean harm.""")], """
Stage: They drink at the visitor table and leave on time. Mari puts her own cup away last, after she has finished it.
Mari: Next time, could we talk about us? I want to answer as myself, before I worry about making the answer comfortable for you.
Narration: I agree. She doesn't apologize for asking.
""", ["tea_tin", "two_cups", "finished_reading_corner"], variants={
"warm": "Mari: I've been choosing to spend these afternoons with you. I wanted you to know I notice that choice.",
"mixed": "Mari: I think we have learned some things about each other. I'm still working out what I feel.",
"cool": "Mari: I need to say a few things plainly. I don't want to hide them inside another offer to help."}),
s(15, "After the Tea", "infirmary", """
Stage: Finale encounter; show the route-ending warning. The nurse permits a quiet conversation at the open visitor table. No patients are present; the nurse remains in the adjacent office.
Mari: I nearly brought a spare lunch. Then I thought you might assume I had called you here because you looked hungry.
MC: I might still look hungry. It isn't why I came.
Stage: She tucks a loose strand of salmon hair behind her ear. Her cup is still full.
MC: I like you, Mari. I want to ask you out.
Mari: I know. I wanted to be able to answer without offering you something else instead.
""", [
c("bad", "I need someone like you. I know you'd always take care of me.", """Mari: I don't want that to be the reason you ask.
MC: I meant that I feel safe with you.
Mari: I understand. I need room to be tired and uncertain with someone too."""),
c("good", "I want to spend time with you, including the days when you have nothing to give.", """Mari: Even when I'm quiet, or don't know what I want yet?
MC: We can talk about it. You don't have to make every day easy for me.
Mari: All right. Let me tell you what I do know."""),
c("neutral", "You can answer honestly. I'll manage my feelings if it isn't what I hoped.", """Mari: Thank you. I needed to hear that.
MC: Take your time.
Mari: I think I've taken the time I need.""")], """
Stage: Apply this choice once and compare effective good and bad totals. Select the matching ending; do not write her acceptance into this shared closing.
""", ["her_tea_cup"], variants={
"warm": "Mari: I'm nervous. It's a rather nice kind of nervous, at least in part.",
"mixed": "Mari: I have thought about this carefully. I don't want to confuse gratitude with an answer.",
"cool": "Mari: Please let me finish what I want to say. I will try to be kind, but I need to be clear."})
]

ENDINGS = [
e("good", "Stay a Little", "infirmary", "Mari with a salmon feathered low ponytail and cyan eyes rests beside the infirmary visitor window with her own tea; a charcoal MC silhouette sits quietly at an equal distance beside her. Warm natural light, relaxed posture, ordinary modest uniform; she is well and awake.", """
Mari: I would like to go out with you. I wanted to know I could say that without also promising to be easy to love.
MC: You don't have to promise that.
Mari: Good. Because I expect I'll still try to feed you when I'm avoiding a difficult conversation.
MC: Can we have the conversation and the food?
Stage: She laughs, then reaches for his hand. He waits until she has offered it.
Mari: Yes. Though some days I may ask you to bring lunch.
MC: I'll learn something that survives the trip to school.
Narration: The nurse passes the open doorway and reminds us when the block ends. Mari answers without letting go of my hand.
Mari: We know. We're leaving on time.
Stage: For the remaining few minutes, she leans back in the visitor chair and drinks her tea while it is still warm.
Mari: Stay a little. Not because I need help with anything.
MC: I'd like that.
Narration: She closes her eyes for one peaceful breath. I don't have to turn the moment into a promise about fixing her life. Today she has chosen something for herself, and I'm glad it includes me.
Stage: Unlock Mari / Good. Credits, then title.
"""),
e("neutral", "Tea for Two", "infirmary", "Mari and the MC silhouette share a calm tea break across two visitor chairs, balanced composition and independent cups, gentle cordial expression, open infirmary doorway in the background.", """
Mari: I care about you, but I don't want a romantic relationship. It took me a while to separate wanting you to be happy from knowing my own answer.
MC: I'm glad you did.
Mari: Are you all right?
Stage: She catches the question before turning it into three more.
MC: Disappointed. I'll be all right. You don't have to pour tea over the whole problem.
Mari: That would be a terrible use of tea.
Narration: We both smile, a little awkwardly. Her answer remains what it is.
Stage: On a later school day, they meet at the visitor table after returning some public leaflets. Mari asks whether the MC wants company. He says yes.
Mari: I brought one tea bag. The spare tin is there if you want some.
MC: I remember where it is.
Narration: We make our own cups. The conversation is ordinary and occasionally uneven. I don't pretend that being her friend was my plan all along, and she doesn't try to repay my disappointment by doing more for me.
Mari: It's nice to see you.
MC: It's nice to see you too.
Stage: Unlock Mari / Neutral. Credits, then title.
"""),
e("bad", "A Cup Left Full", "infirmary", "Mari calmly gathers her school bag to leave the infirmary visitor table; her full tea cup remains in the foreground, cool late light, her expression tired but resolved. No collapse, injury or helpless framing.", """
Mari: I don't want to date you. I need some distance from the way things have been between us.
MC: I thought you liked looking after me.
Mari: Sometimes I did. I wanted you to be interested in the rest of me too. When I tried to say what I needed, I often felt I was making our time together less convenient for you.
Narration: The cup in front of her is still full. I almost tell her to drink it, then stop. She has already told me what matters.
MC: I'm sorry. I won't try to talk you out of it.
Mari: Thank you.
Stage: She collects her bag. The nurse takes care of the visitor table after they leave; Mari does not stay to tidy away the conversation.
Narration: I go home without an extra lunch or an offer to check my homework. Those things were never proof that she owed me more.
MC: Take care, Mari.
Mari: You too.
Stage: She leaves by her own route. The MC does not follow.
Stage: Unlock Mari / Bad. Credits, then title.
""")]
