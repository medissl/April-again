from story_schema import c, s, e

ID = "katya"
NAME = "Katya"
VOICE = "Formal and precise; dry humor. Sharpness protects her pride, but cruelty is not her whole personality. Russian slips are rare and understandable in context. She wants earned competence, not rescue or admiration of money."
SCENES = [
s(1, "The Missing Stapler", "class_b", """
Stage: Class B is preparing an information table for new students. A teacher assigns the MC and Katya to finish it during the activity block.
Katya: Those are the spare forms. The completed ones go on the right.
MC: Good thing you stopped me. I was about to invent a new filing system.
Katya: Most disasters begin with that sort of confidence.
MC: I'm Takahashi. We passed each other during orientation.
Katya: I remember. You were examining the map upside down.
MC: I hoped nobody noticed.
Katya: Ekaterina Romanova. Katya is sufficient. Now, do you know how to use a stapler?
Narration: She holds up an empty hand. The stapler is missing. For a moment, neither of us speaks.
""", [
c("good", "I'll check the supply list. You can show me how you want these sorted.", """Katya: Sensible. Ask before changing the order.
MC: Understood. I'll try to keep my dangerous confidence under control.
Katya: See that you do."""),
c("neutral", "Just give me a stack. I'll copy what you're doing.", """Katya: That will work, provided you watch carefully.
MC: Copying is one of my stronger school skills.
Katya: An unfortunate introduction, but a useful one."""),
c("bad", "You seem to have it handled. I'll stay out of your way.", """Katya: Standing aside is not the same as helping.
MC: I thought you'd prefer working alone.
Katya: I prefer people to complete the work they were assigned.""")], """
Stage: We work around the missing stapler with paper clips, then find it inside the empty forms box.
MC: At least we know it wasn't stolen.
Katya: Yes. A great relief to the international stationery market.
Narration: Her face stays serious. I'm almost certain that was a joke.
""", ["forms", "folder", "stapler"]),
s(2, "A Very Small Mistake", "class_b", """
Stage: The next shared activity is checking room signs against the class register.
MC: We have two signs for the library.
Katya: Impossible. I checked them yesterday.
Narration: She lays both signs on the desk. They are identical.
Katya: Then I checked the same pile twice.
MC: I've done worse before breakfast.
Katya: That is not the standard I was aiming for.
Narration: She reaches for every page at once. A corner tears under her thumb.
""", [
c("neutral", "Let's print another one and move on.", """Katya: Yes. There is no reason to make a performance of it.
MC: I'll get the paper.
Katya: The drawer on your left."""),
c("bad", "I thought you said you never miss anything.", """Katya: I said I checked them. Those are different claims.
MC: I was joking.
Katya: Then choose a better moment."""),
c("good", "I'll check half against the register. We can catch each other's mistakes.", """Katya: Including yours, presumably.
MC: There'll probably be more of those.
Katya: Fine. Start with the first-year rooms.""")], """
Stage: We finish the signs and compare our two lists. She finds my spelling error; I find a room number copied twice.
Katya: Both corrected. That is what the check is for.
Narration: She keeps the torn sheet for scrap instead of hiding it.
""", ["room_signs", "class_register"]),
s(3, "Tea Without Instructions", "canteen", """
Stage: A classroom task runs into lunch. We bring the final labels to a canteen table to finish them.
Katya: You have been looking at the drink machine for an unreasonable length of time.
MC: It's the first important decision I've made today.
Katya: Concerning.
MC: What do you usually get?
Katya: Tea. Without sugar.
MC: They have sweet lemon tea and something called Royal Milk.
Katya: A regrettable use of the word royal.
Narration: She checks her purse, then notices me watching.
""", [
c("bad", "You can pay for both. This probably costs nothing to you.", """Katya: My family is not a canteen payment plan.
MC: I didn't mean it seriously.
Katya: You meant it seriously enough to say it."""),
c("good", "I'm getting water. Want to complain about the tea while we finish these?", """Katya: An unusually specific invitation.
MC: I think it has potential.
Katya: I shall try the least offensive tea and fund my own portion of the complaint."""),
c("neutral", "I'll try the lemon one. You're welcome to the last tea bottle.", """Katya: Thank you. Though I was quite prepared to survive the shortage.
MC: I'll remember that during the next tea emergency.
Katya: Please do.""")], """
Stage: We cut labels between bites of lunch. She reads the tea bottle's ingredients with growing disapproval.
Katya: There is more sugar in this than tea.
MC: You sound betrayed.
Katya: I was promised tea. My expectations were hardly extravagant.
""", ["tea_bottle", "paper_labels"]),
s(4, "Not an Audience", "field", """
Stage: On a supervised club day, Katya helps demonstrate fencing footwork on the dry hardcourt edge. The MC has been asked to mark practice lanes.
Katya: The line needs to be straight.
MC: It looked straight when I was closer to it.
Katya: An argument that could support almost any mistake.
Stage: An older club member corrects her shoulder position. She repeats the movement without answering.
MC: Does that hurt your arm?
Katya: Only my dignity. Apparently my shoulder has been betraying me for years.
Narration: The instructor leaves us to reset the markers. She looks at the tape, not at me.
""", [
c("good", "Show me the step once more. I'll put the markers where you actually need them.", """Katya: Watch the front foot. The rear one follows; it does not chase.
MC: Like that?
Katya: Approximately. At least nobody is holding a weapon."""),
c("bad", "You looked perfect to me. The instructor was being picky.", """Katya: He was correct. That is why I listen to him.
MC: I meant it as a compliment.
Katya: Then compliment something you observed."""),
c("neutral", "I'll leave you to practice and finish the tape.", """Katya: Very well. Keep the spacing consistent.
MC: No dramatic curves this time.
Katya: I would appreciate the restraint.""")], """
Stage: Practice fills the afternoon. By the time we collect the markers, the line is straight and her movement is quieter.
Katya: Better.
MC: Your footwork or my tape?
Katya: Both. Do not force me to say it twice.
""", ["floor_tape", "fencing_bag"], "determined"),
s(5, "Melonpan", "corridor", """
Stage: Rain keeps the class inside. Katya is comparing two sets of committee notes by the corridor window.
MC: You missed the bread delivery at lunch.
Katya: I am aware.
MC: I bought an extra melonpan before they ran out. Do you want it?
Katya: Did I look particularly helpless today?
MC: You looked busy.
Narration: She glances at the wrapper, then checks whether anyone is listening.
Katya: I prefer not to owe people for small favors.
""", [
c("neutral", "You can buy me one another time.", """Katya: A clearly defined exchange. Acceptable.
MC: That's a serious way to discuss bread.
Katya: Bread is the subject you introduced."""),
c("good", "You don't owe me. If you don't want it, I'll keep it.", """Katya: You are making this very difficult to object to.
MC: It wasn't meant to be an argument.
Katya: Fine. Thank you. And leave the notes on the dry side of the windowsill."""),
c("bad", "Come on. Even an heiress can try cheap food for once.", """Katya: I have eaten bread before, Takahashi.
MC: You know what I meant.
Katya: Unfortunately, I think I do. Keep it.""")], """
Stage: The rain softens. We finish the notes before the final bell.
Narration: Whether she takes the bread or not, I put the wrapper in my own bag. Nothing about this needs an audience.
Katya: You missed a page number.
MC: There she is. I was worried you'd gone easy on me.
""", ["melonpan", "committee_notes"], variants={
"warm": "Katya: You remembered which bread I looked at. That was... observant.",
"mixed": "Katya: You have a habit of appearing when there is unfinished work.",
"cool": "Katya: We can finish the notes. I would prefer to keep this afternoon simple."}),
s(6, "The Smallest Witness", "gate", """
Stage: Our task is counting supplies returned through the lobby entrance. During a break, a cat slips under the gate hedge.
MC: You have company.
Katya: I noticed.
Narration: Her sleeve is caught in the cat's paws. She could pull away. She doesn't.
Katya: It is damaging an expensive piece of fabric.
MC: It seems very satisfied with its work.
Katya: Then one of us is.
Narration: Two classmates pass the gate. Katya straightens so quickly that the cat complains.
""", [
c("bad", "I should take a picture. Nobody will believe this.", """Katya: Put your phone away.
MC: I haven't taken anything yet.
Katya: Then this is an excellent moment not to start."""),
c("neutral", "I'll check whether anyone knows who feeds it.", """Katya: A practical question. It looks rather comfortable here.
MC: Maybe it owns the school.
Katya: That would explain several decisions."""),
c("good", "I'll finish the count. You can wait until it lets go.", """Katya: It should only take a moment.
MC: The cat or the count?
Katya: Do not be pleased with yourself.""")], """
Stage: We ask the groundskeeper about the cat and learn that it belongs to a nearby house. It leaves through the hedge on its own.
Katya: A terrible creature.
Narration: Before we go, she checks that nobody has closed the gap in the fence.
""", ["cat", "supply_clipboard"], "flustered"),
s(7, "The Name on the Form", "class_b", """
Stage: Class B needs a small budget for its first-year display. A classmate suggests asking Katya's father to pay.
Katya: We have a school allowance. We will work within it.
Classmate: It was just an idea.
Stage: The classmate leaves for another assignment. Katya crosses out a cost, pressing hard enough to mark the next page.
MC: We could use plain backing paper.
Katya: Yes. Or fewer printed photographs.
MC: You don't have to solve every part before the next meeting.
Katya: Apparently I do, or somebody will solve it by calling my father.
""", [
c("good", "Let's put the cheaper options beside the expensive ones. The class can decide.", """Katya: You would let them see an unfinished proposal?
MC: I'd let them help finish it.
Katya: That is... irritatingly reasonable. Start with the printing costs."""),
c("neutral", "Let's ask the teacher how much the allowance covers.", """Katya: We should confirm that before ordering anything.
MC: I'll write down the questions.
Katya: And I will try not to answer them all before we reach the staffroom."""),
c("bad", "Your father could help once. It would save everyone a lot of trouble.", """Katya: Including the trouble of taking our work seriously?
MC: I meant the money, not your effort.
Katya: People rarely bother to separate the two.""")], """
Stage: The budget is small enough to understand and large enough to argue about. We make a clean copy for the class.
Narration: Katya leaves her surname off the proposal title. Every member's name goes in the credits instead.
""", ["budget_sheet", "paper_samples"]),
s(8, "Three Signatures", "library", """
Stage: The library lends us a reference table. Katya has rewritten nearly the entire display plan overnight.
MC: There's a signature space for three people. Only yours is filled.
Katya: The other sections were incomplete.
MC: So you did them too?
Katya: I required a finished plan, not a lesson in patience.
Narration: She rubs her wrist, then immediately stops when she notices me looking.
Katya: I am not asking you to feel sorry for me.
MC: I was going to ask where the original drafts went.
""", [
c("neutral", "We can give everyone one last deadline.", """Katya: A specific one. Not 'whenever you have time.'
MC: Before the end of this block.
Katya: At least that can be measured."""),
c("bad", "If you want everything your way, you may as well do it all.", """Katya: I am aware of the option. I have been exercising it.
MC: Then why ask anyone else?
Katya: I begin to wonder the same thing."""),
c("good", "Put my section back. Tell me what's wrong with it and let me fix it.", """Katya: The image credits are missing, and the last paragraph repeats the first.
MC: Good. That's something I can actually fix.
Katya: I will check it when you are finished. Once.""")], """
Stage: We spend the block comparing drafts rather than replacing them. The final plan has three different sets of corrections.
Katya: That sentence is yours. It should stay in your voice.
Narration: Her pen hovers, then moves to the next page.
""", ["three_drafts", "reference_books"]),
s(9, "A Call in the Hall", "corridor", """
Stage: The MC returns from an errand and hears Katya speaking Russian near the stairwell. Her usual clipped certainty has gone quiet.
Katya: Yes. I understand. I will send it when it is finished.
Stage: She ends the call and sees the folder in the MC's hands.
Katya: How long have you been there?
MC: Long enough to know I should have made more noise.
Katya: It was my mother. That is all.
Narration: It clearly isn't all. It is, however, all she has offered.
MC: The teacher approved the cheaper paper.
""", [
c("bad", "Was she disappointed in you? You sounded different.", """Katya: You have mistaken hearing a conversation for being invited into it.
MC: I only wanted to understand.
Katya: Then understand that I do not wish to discuss it."""),
c("good", "Want the folder now, or a minute first?", """Katya: A minute would be useful.
MC: I'll be by the noticeboard.
Katya: Thank you. I will come over."""),
c("neutral", "I'll leave the folder on your desk.", """Katya: Very well. I will read it shortly.
MC: The note on top explains the changes.
Katya: I saw. Thank you.""")], """
Stage: Later, we attach paper samples to the display mock-up. The MC does not ask again about the call.
Katya: My mother was a dancer. She hears an unfinished plan and imagines a missed step.
Narration: She says it while measuring a margin. I keep my eyes on the ruler and let her decide whether to say more.
""", ["phone", "paper_samples"], "sad"),
s(10, "The Shortcut", "lobby", """
Stage: A supply delivery arrives under the wrong name. Someone has written 'Romanova donation' on a school-funded box.
Katya: It is an ordinary purchase. The receipt is inside.
MC: We'll correct the label.
Katya: After half the class has seen it.
Narration: A classmate asks if her family bought the display equipment. Katya's reply is so formal that the conversation stops.
MC: We still have the order sheet.
Katya: I know. I would prefer evidence to another sympathetic speech.
""", [
c("good", "Let's attach the school receipt and explain the mistake together.", """Katya: Keep it brief.
MC: Wrong label, school budget, corrected record. No speech.
Katya: An excellent length."""),
c("neutral", "The teacher can clear it up at the next meeting.", """Katya: That would be appropriate.
MC: I'll leave the receipt with the order sheet.
Katya: Please make a copy first."""),
c("bad", "People will believe what they want. We might as well use the reputation.", """Katya: You think I should benefit from something that is untrue?
MC: I think fighting it is exhausting you.
Katya: Then let me choose what is worth my effort.""")], """
Stage: The incorrect label comes off. The receipt stays with the supplies, where anyone can check it.
Narration: There is no grand apology from the whole school. By the next bell, most people are discussing lunch.
Katya: You were right about one thing. They do move on quickly.
""", ["delivery_box", "receipt"], variants={
"warm": "Katya: I trust you to explain your part. I would rather not speak for you.",
"mixed": "Katya: Let us be clear about what we are telling people.",
"cool": "Katya: We can correct the purchase record. My family is not part of the discussion."}),
s(11, "Second Place", "field", """
Stage: A supervised practice match has ended. Katya loses the last point, removes her mask and thanks her opponent before speaking to anyone else.
MC: Want me to carry the markers back?
Katya: In a moment. I am trying to remember when my foot stopped obeying me.
MC: The instructor said your recovery was better.
Katya: My recovery was necessary because I made the first mistake.
Narration: She watches the empty lane as if the last point might happen again.
MC: Is there a version of this afternoon where you're allowed to be disappointed?
Katya: I am testing it. The results are unpleasant.
""", [
c("neutral", "We could ask the instructor what to work on next.", """Katya: I already have. Distance and patience.
MC: Hard to mark those with tape.
Katya: A flaw in your otherwise excellent system."""),
c("good", "You can hate losing. You don't have to pretend the whole practice was worthless.", """Katya: I did not say the whole practice was worthless.
MC: You were making a strong case.
Katya: Hm. Perhaps I was."""),
c("bad", "It's only a school match. You're taking it too seriously.", """Katya: It matters to me. That should be enough information.
MC: I was trying to help you forget it.
Katya: I am trying to learn from it.""")], """
Stage: We reset the lane for the next group. Katya walks the movement slowly, then packs her equipment.
Katya: My opponent earned that last point.
MC: You'll tell her?
Katya: I already did. I can be unhappy without being unfair.
""", ["fencing_mask", "floor_markers"], "annoyed"),
s(12, "The Work She Didn't Do", "class_b", """
Stage: The display assembly has reached the part that never appears in photographs: cutting backing card and checking every caption.
Katya: This section is still blank.
MC: It belongs to Sato. He's collecting the prints.
Katya: I could complete it before he returns.
MC: You could.
Narration: She looks at the empty space, then at the scissors already in her hand.
Katya: You are waiting for me to have a revelation, aren't you?
MC: Mostly I'm waiting for the glue.
""", [
c("bad", "I'll fill it in while he's gone. We don't have to tell him.", """Katya: That would be efficient.
MC: See? Problem solved.
Katya: No. Put it down. I know exactly how that ends."""),
c("good", "Let's finish our section. We can check his when he gets back.", """Katya: And if it is late?
MC: Then we deal with a late section. We don't erase his part in advance.
Katya: Fine. Pass me the glue."""),
c("neutral", "I'll message him for an update.", """Katya: Ask whether he needs help collecting them.
MC: That's a better question than 'Where are you?'
Katya: It had better produce a better answer.""")], """
Stage: Sato returns with the prints and a reasonable explanation. Katya checks his captions without rewriting his introduction.
Katya: There. Finished.
Narration: She has done less of it herself than she intended. For once, that looks like part of the achievement.
""", ["backing_card", "glue", "photo_prints"]),
s(13, "An Ordinary Afternoon", "canteen", """
Stage: After the committee work, a teacher asks us to stay available in case the display needs changes. No changes arrive.
MC: We might be finished.
Katya: Do not say that too confidently. Work can hear you.
Stage: She has brought a small dark-chocolate bar. She places it between us, still wrapped.
Katya: For the table. Not a reward.
MC: I wasn't about to put it on my report card.
Katya: Good.
Narration: Without a folder between us, the table looks unexpectedly wide.
""", [
c("good", "What would you be doing today if nobody needed anything from you?", """Katya: Listening to music. Possibly walking somewhere without a destination.
MC: That sounds possible.
Katya: An alarming thought. I had become rather attached to being too busy."""),
c("neutral", "Want to review the display once more before we leave?", """Katya: We have checked it twice.
MC: Old habits.
Katya: Apparently contagious ones. Finish your chocolate first."""),
c("bad", "You'd probably be bored without people relying on you.", """Katya: Perhaps. That does not make it all I want.
MC: You never seemed interested in doing nothing.
Katya: You have rarely asked.""")], """
Stage: We talk about music until the teacher tells us there are no more changes. Katya recommends a piano recording, then spells the title so I can find it.
Katya: You do not have to enjoy it.
MC: Good. I'd hate to fail listening homework.
Katya: There is no exam. That is the point.
""", ["dark_chocolate", "music_note"], "soft_smile"),
s(14, "The Final Copy", "class_b", """
Stage: The class is submitting its display record. Katya has left the final signature space for the MC.
Katya: Read it before you sign. I am not asking for blind agreement.
Narration: The report credits the class, records the budget mistake and names the work that was corrected. It does not turn every problem into somebody else's fault.
MC: You left the changes in.
Katya: They happened. The first version was not the finished version.
MC: Sounds obvious when you say it like that.
Katya: Most difficult things do, afterwards.
""", [
c("neutral", "It looks accurate. I'll sign.", """Katya: Thank you. We can hand it in together.
MC: And finally retire the folder?
Katya: A dignified retirement. It has suffered enough."""),
c("bad", "Could we leave out the mistakes? The report would sound more impressive.", """Katya: It would sound less true.
MC: Nobody needs every awkward detail.
Katya: Then do not add any. But the corrections stay."""),
c("good", "Before I sign, I want to be honest about my part too.", """Katya: Then be specific. I can listen to specifics.
MC: Some days I helped. Some days I said what was easiest. I don't want the report to hide either.
Katya: All right. We will get the wording right.""")], """
Stage: We finish the record and leave it in the submission tray. The desk is suddenly clear.
Katya: I will be at the gate after dismissal next time. If you want to talk without a task attached.
Narration: It is an invitation to a conversation, not a promise about what she will say.
""", ["final_report", "pen"], variants={
"warm": "Katya: I have become accustomed to having you beside me. That is not a complaint.",
"mixed": "Katya: We have managed the work. I am still deciding what to make of the rest.",
"cool": "Katya: There are a few things I would rather settle directly than leave unspoken."}),
s(15, "Beside the Gate", "gate", """
Stage: Finale encounter. The UI warns that completing this conversation ends the current playthrough. Katya waits at the gate, holding an ordinary convenience-store bag.
MC: No folder?
Katya: I considered bringing one. It would have made this less conspicuous.
MC: Is that melonpan?
Katya: You are very observant when bread is involved.
Narration: She has bought two. It would be easy to treat that as an answer before asking the question.
MC: I wanted to say something properly. I like you, Katya. More than as a classmate.
Katya: Then let us be clear about what you are asking.
""", [
c("bad", "After all this time, I think I've proved I deserve a chance.", """Katya: My affection is not a prize for completing enough tasks.
MC: That came out wrong.
Katya: It came out clearly. Let me finish before you explain it away."""),
c("good", "I'd like to go out with you. You can tell me honestly if you don't want that.", """Katya: I intended to answer honestly in any case.
MC: I know. I wanted you to hear that I can accept it.
Katya: Good. Then listen."""),
c("neutral", "I'm not sure what happens next. I wanted you to know how I feel.", """Katya: A statement rather than a demand. I can work with that.
MC: It took me a while to get the wording right.
Katya: I noticed.""")], """
Stage: Record this choice once, then compare the route's total effective good and bad counts. Play exactly one ending below. Do not show a default acceptance before evaluating the score.
""", ["two_melonpan"], variants={
"warm": "Katya: I was hoping you would come. Try not to look so surprised by that.",
"mixed": "Katya: I am glad we can speak directly, whatever we decide.",
"cool": "Katya: I came because an honest conversation is better than another misunderstanding."})
]

ENDINGS = [
e("good", "No Need to Keep Up", "gate", "Katya beside the gate in soft late-afternoon light, silver hair in broad clean locks, small sincere smile, offering a wrapped melonpan; the MC is a plain charcoal silhouette at equal height beside her. No glamour framing.", """
Katya: I like you too. I would have preferred to announce that without becoming this nervous.
MC: You hid it better than I did.
Katya: That is a very low standard.
Stage: She gives him one of the wrapped breads. Their hands briefly touch; neither pulls the other closer.
Katya: There is a café near the station. Saturday, if you are free.
MC: A date?
Katya: Yes, Takahashi. I am attempting to eliminate ambiguity.
MC: Saturday works.
Narration: I used to imagine that a confession would be the moment I finally said everything perfectly. Instead, I'm smiling so hard I can barely unwrap the bread.
Katya: And if you dislike the café, say so. I have no intention of dating somebody who agrees with me out of fear.
MC: What if I disagree out of terrible taste?
Katya: We shall have to see how terrible.
Stage: She falls into step beside him. Neither of them needs to set the pace for both.
Narration: The gate closes behind us. There are ordinary things to decide now: which street to take, whether it will rain, when I can see her again. I want the chance to learn them.
Stage: Unlock Katya / Good. Return to title after credits.
"""),
e("neutral", "The Seat Across From Her", "class_b", "A quiet Class B desk with the completed folder between two chairs; Katya offers a small cordial smile across the table. Open daytime light, respectful distance.", """
Katya: I value the time we have spent together. I cannot honestly call what I feel romance.
MC: All right.
Katya: You are allowed to look disappointed. I would prefer that to a very brave lie.
MC: I was hoping for a different answer. But I don't want one you have to force.
Stage: The next school day, they collect the spare display materials in Class B. Katya puts the familiar folder on the table.
Katya: Will sitting here be uncomfortable?
MC: A little, probably. Not forever.
Katya: Tell me if you need room. I can manage a direct answer.
Narration: There is no sudden trick that changes what she said. There is also no reason to pretend the afternoons meant nothing.
MC: You can still send me the name of that piano piece.
Katya: I already did. You spelled it incorrectly in your notes.
MC: Of course I did.
Stage: She smiles, small and uncomplicated, and pushes the spare scissors across the desk.
Narration: For now, I take the seat across from her. Friendship is a different answer. It is still an answer worth treating carefully.
Stage: Unlock Katya / Neutral. Return to title after credits.
"""),
e("bad", "A Closed Folder", "class_b", "Katya alone in Class B in cool late light, calmly closing the completed folder; second chair empty, her expression disappointed but steady. No tears as spectacle.", """
Katya: I do not want to date you. I also think we need some distance.
MC: Because of what I just said?
Katya: Because of more than one afternoon. I have tried to tell you when something mattered to me. Too often, you treated it as something to get around.
Narration: I start preparing an explanation. Hearing it in my head, I realize it would be another request for her to make this easier for me.
MC: I heard you. I won't keep asking.
Katya: Thank you.
Stage: The next day, the MC collects his remaining papers from Class B. Katya closes the committee folder and puts it with the finished work.
Katya: Your section is in the copy on the left. You should keep it.
MC: Right. Thank you for working with me.
Katya: We did finish it.
Narration: The empty chair does not accuse me. It is simply empty. She is allowed to decide who sits beside her, and I do not get to turn that into another test of her kindness.
Stage: He takes his papers and leaves. She returns to her own plans.
Narration: Next time I care about somebody, I want to listen before I'm afraid of losing them.
Stage: Unlock Katya / Bad. Return to title after credits.
""")]
