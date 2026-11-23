from story_schema import c, s, e

ID = "akira"
NAME = "Akira Seojin"
VOICE = "Quick, curious, friendly; connects ordinary problems to economics or games. Talks past her own fatigue. Earnest technical competence, shaky privacy instincts, and difficulty distinguishing romance from friendship. Never a walking list of references."
SCENES = [
s(1, "The Girl With Three Plans", "class_a", """
Stage: A teacher pairs the MC with Akira to collect ideas for a first-year information project.
Akira: You're the map guy! From orientation. I'm Akira Seojin. Either name is fine, except during roll call, apparently.
MC: I was hoping the map thing wouldn't become my entire reputation.
Akira: Too late. Good news: you have a memorable brand.
Stage: Her glasses slip down. She pushes them up with a finger still holding a sticky note.
Akira: We need a project people will actually use. I have a room finder, a lunch queue tracker and a system for borrowing stationery.
MC: Is that one project or three?
Akira: That's what I need a second person for. My ideas don't tell each other no.
""", [
c("neutral", "The room finder sounds useful.", """Akira: Because of your tragic map history?
MC: I prefer 'relevant experience.'
Akira: Excellent. We already have a test user."""),
c("good", "Which problem have people actually asked you about? Let's start there.", """Akira: Lunch queues. Constantly. Usually while we're standing in one.
MC: Then we can ask what information would help.
Akira: Yes! A small test before we build anything. You're useful, map guy."""),
c("bad", "Pick whatever will make our project look the most impressive.", """Akira: A live queue tracker would look pretty good...
MC: There you go.
Akira: Though we should probably find out whether the canteen would even let us use it.""")], """
Stage: We spend the activity block making a short survey. Akira fits her first idea on one page, then puts the other two on a separate sheet.
Stage: The teacher approves the anonymous canteen-queue pilot as the first test. The room finder and lending system remain ideas to revisit later, not alternate projects the player has secretly committed to.
MC: Saving those for later?
Akira: For later me. She has unlimited time and better cable management.
""", ["sticky_notes", "project_notebook"]),
s(2, "The Price of a Sandwich", "canteen", """
Stage: We observe the canteen queue with permission from the staff. Akira has made a table of waiting times.
Akira: The cheapest bread sells out first. Then everyone spends five minutes deciding whether they can afford to be disappointed.
MC: That's a very specific market.
Akira: Scarcity is emotional. I know. I missed the chicken sandwich.
Stage: She checks the notes and discovers that she timed two different queues as if they were the same one.
Akira: Well. My beautiful data is mostly lunch fiction.
MC: We still have time to do another round.
""", [
c("bad", "Use the numbers we have. Nobody's going to check.", """Akira: They might not, but the canteen staff will know if it's wrong.
MC: It's only a class project.
Akira: It's still got our names on it."""),
c("good", "Let's separate the queues and mark what we didn't measure.", """Akira: Less dramatic graph. More honest graph.
MC: We can survive a boring graph.
Akira: Speak for yourself. But yes, give me a clean page."""),
c("neutral", "Let's ask the staff which queue matters most.", """Akira: Right. We might be timing something they can't change.
MC: And maybe they'll tell us when the sandwiches arrive.
Akira: Research has benefits.""")], """
Stage: We finish the new observations and put a question mark beside the uncertain numbers.
Akira: My dad does this with store orders. He says guessing is fine if you remember you guessed.
MC: Your dad sounds helpful.
Akira: He is. Also embarrassingly good at spotting when I haven't eaten lunch.
""", ["queue_survey", "sandwich_wrapper"]),
s(3, "One More Turn", "class_a", """
Stage: A supervised club block gives us time to mock up the project on Akira's laptop. During a break, a strategy-game map is still open in the corner.
MC: That doesn't look like the canteen.
Akira: Only because nobody's flanking the vending machine. Yet.
Stage: She shows me a practice match. Her explanation becomes faster as soon as I ask about the map.
Akira: You can't defend everything. Pick what matters, leave yourself a way out, and don't panic because one number is red.
MC: Is that advice for the game or school?
Akira: Depends how badly school is going.
""", [
c("good", "Can you show me one decision? I'm losing track of the whole map.", """Akira: Right. Sorry. This bridge, then. Ignore everything else for a minute.
MC: That's much better.
Akira: I forget that my internal tutorial doesn't come with subtitles."""),
c("neutral", "I don't really play these, but you seem good at it.", """Akira: That's okay. We don't have to share every hobby.
MC: You sound surprised.
Akira: I'm reminding myself too."""),
c("bad", "Can you skip the explanation and just tell me how to win?", """Akira: Winning is the explanation. The decisions are the fun part.
MC: I thought the fun part was beating someone.
Akira: Sometimes. It gets old if that's all you're doing.""")], """
Stage: The game break ends on time. We return to the mock-up with a simpler idea of what belongs on the screen.
Akira: One useful thing at a time. The bridge method.
MC: I'm claiming credit for the name.
Akira: Negotiable. We haven't agreed on licensing.
""", ["laptop", "strategy_game_screen"]),
s(4, "Not My Story to Tell", "library", """
Stage: We are reading survey comments at a library table. Akira starts explaining why a classmate has been avoiding the canteen.
Akira: She told me her family is having money problems, so I thought we could make sure she—
Stage: She stops. The survey page is still open between us.
Akira: She didn't put that in the survey. She told me yesterday.
MC: Does she know you're telling me?
Akira: No. I was trying to work out a way to help.
Narration: For once, she doesn't rush to fill the silence.
""", [
c("neutral", "We don't need her name in the project.", """Akira: I'll take it out of my notes too.
MC: We can talk about affordable options generally.
Akira: Right. That would actually help more people."""),
c("bad", "Tell me the rest. Maybe I can work out what she needs.", """Akira: I don't think I should.
MC: It's only us.
Akira: That's probably what she thought when she told me."""),
c("good", "Let's leave her details out. You can ask her privately what help she wants.", """Akira: And tell her I mentioned it?
MC: She deserves to know. You can keep the apology simple.
Akira: I hate that you're right about the difficult part.""")], """
Stage: We replace the personal example with an anonymous survey total. Akira closes her notebook before speaking again.
Akira: I know lots of people. That doesn't mean every story I hear becomes mine to pass on.
MC: You caught yourself.
Akira: A bit late. Still worth catching.
""", ["anonymous_survey", "notebook"], "worried"),
s(5, "The Bag That Knows Everyone", "lobby", """
Stage: We sort survey returns near the lobby noticeboard. A keychain catches on Akira's chair and drops to the floor.
MC: Is that little astronaut yours?
Akira: A friend gave it to me when I won a software contest. She said I needed a person who looked more stressed than me.
MC: It does look worried.
Akira: Strong likeness. This one came from a gaming friend. This pin's from my cousin. That rabbit used to be attached to my glasses, but it attacked my ear.
Narration: She knows the story of every charm. Her phone lights up three times before she finishes the second one.
Akira: Sorry. Lots of people need little things today.
""", [
c("bad", "That's what happens when you collect friends like contacts.", """Akira: I don't collect them. I like them.
MC: You did say connections matter.
Akira: People can matter for more than what they can do for me."""),
c("good", "You can answer after we finish. Anyone who needs you urgently can call.", """Akira: Ten minutes of not replying won't ruin my entire social life?
MC: I can't promise the astronaut will forgive you.
Akira: He's seen worse. Phone goes in the bag."""),
c("neutral", "We can take a break while you reply.", """Akira: Thanks. I'll set a timer or we'll be here forever.
MC: Two minutes?
Akira: Three. I know my weaknesses.""")], """
Stage: The block ends with the survey envelopes sorted and the astronaut safely reattached.
Akira: I told one person I couldn't help today. They said, 'No problem.'
MC: Shocking development.
Akira: Honestly? A little.
""", ["satchel_keychains", "phone", "survey_envelopes"], variants={
"warm": "Akira: You're getting good at noticing when I need a pause.",
"mixed": "Akira: I can't tell if we're organized or just lucky today.",
"cool": "Akira: Let's get the envelopes finished. I don't want to turn anyone else's business into our afternoon."}),
s(6, "A Spare Portion", "canteen", """
Stage: We compare the survey totals over lunch. Akira opens a homemade lunch box and notices the MC's bread roll.
Akira: That's your whole lunch?
MC: It was going to be two rolls. One escaped into breakfast.
Akira: Here. I made too much.
MC: You cook?
Akira: My dad owns a grocery shop. There's a long family tradition of bringing home something that needs cooking tonight.
Stage: She holds out a clean spare container, then hesitates.
Akira: You don't have to take it. I do that thing where offering turns into deciding.
""", [
c("good", "I'd like some. Tell me what's in it first, though.", """Akira: Chicken, egg, spring onion. Nothing spicy. I prefer my lunch without a boss fight.
MC: Then yes, please.
Akira: See? An offer with actual information. I'm learning."""),
c("bad", "You're going to make someone a perfect wife.", """Akira: That's a weirdly large job offer for some chicken.
MC: I meant you're good at cooking.
Akira: You can just say that bit. I like that bit."""),
c("neutral", "Thanks, but I'll stick with the roll today.", """Akira: Okay. I'll save it for after the club block.
MC: It does look good.
Akira: Review accepted. No purchase required.""")], """
Stage: The survey calculation takes longer than lunch. Akira catches two arithmetic mistakes and draws a tiny disappointed face beside the calculator.
MC: You know that's not the calculator's fault.
Akira: I know. It needed a colleague.
""", ["bento", "calculator", "spare_container"]),
s(7, "Useful Information", "class_a", """
Stage: The prototype can now suggest a quieter canteen period. Akira wants to personalize it.
Akira: If people enter their class and usual lunch time, we can make better suggestions. Their names would help us remember who tried it.
MC: Do we need the names for it to work?
Akira: Not technically. It would make follow-ups easier.
MC: It would also tell us quite a lot about where they are.
Narration: She leans back from the laptop. This is her favorite part of the work, and I've put a problem directly in it.
Akira: I want the project to be useful. I don't want to build something so cautious it does nothing.
""", [
c("neutral", "Let's show both versions to the teacher before collecting anything.", """Akira: A review before a launch. Sensible, slightly less exciting.
MC: We could survive slightly less exciting.
Akira: We keep saying that. Suspicious trend."""),
c("good", "We can test anonymous time bands first. Ask for more only if we can explain why.", """Akira: So we still test it. We just make the small version prove it needs to grow.
MC: Exactly.
Akira: Fine. That's annoyingly good product advice."""),
c("bad", "People click through forms anyway. Add the names and launch it.", """Akira: That would be faster.
MC: And we can fix it later.
Akira: Unless what needs fixing is that people trusted us with too much.""")], """
Stage: Teacher review is mandatory regardless of the choice. The approved pilot uses anonymous time bands and deletes test entries afterwards.
Akira: I argued for speed. I still think speed matters.
MC: We can be quick about the things we understand.
Akira: And careful about the things we don't. Okay. Put that in the notes before I make it sound like my idea.
""", ["laptop", "anonymous_form", "teacher_approval"]),
s(8, "Offline", "class_a", """
Stage: We arrive for a trial during a school network outage. Akira refreshes the page once, then makes herself stop.
Akira: The internet has chosen personal violence.
MC: It may not know we're here.
Akira: Then this is an appalling coincidence.
Stage: She checks the clock. The volunteer testers will arrive shortly.
Akira: I could use my phone hotspot, but I don't know whether everyone will connect in time.
MC: What can we show without a connection?
Akira: The screen mock-ups. The anonymous totals. My ability to complain in several categories.
""", [
c("bad", "Say the school broke our demo. That's basically true.", """Akira: The outage is real. Having no backup is ours.
MC: Nobody asked for a backup.
Akira: That's not a great reason to make the testers waste their time."""),
c("neutral", "We can postpone and explain why.", """Akira: I'll message the teacher and ask the testers which time works.
MC: Better than making them wait for a loading screen.
Akira: We are aggressively proving the need for good information."""),
c("good", "Let's run the test on paper. We're testing whether the information helps, right?", """Akira: Right. We don't need a network to ask a good question.
MC: I'll get the prints.
Akira: And I'll put 'paper' in the backup plan before I forget it exists again.""")], """
Stage: The teacher arranges a short paper check and a later digital trial. We spend the remaining block writing what failed and what still worked.
Akira: I wanted a smooth demo.
MC: You got a useful test.
Akira: I'm allowing myself five more minutes of being annoyed before I appreciate that.
""", ["laptop", "paper_mockups", "offline_notice"], "puzzled"),
s(9, "The Favor Queue", "lobby", """
Stage: Our project block overlaps with three requests from Akira's friends: a poster, a spreadsheet and a club signup page.
Akira: They're all small. It's the combination that's developing teeth.
MC: Have you agreed to all three?
Akira: Technically, I said I could probably help.
MC: How did they hear that?
Akira: As yes. Correctly, to be fair.
Narration: She opens three message threads and can't seem to choose which one to answer.
Akira: I like being someone people can count on. I don't want them to think that was fake.
""", [
c("good", "Tell them what you can finish and what you can't. You don't need a crisis to have a limit.", """Akira: Even if someone is disappointed?
MC: They'll have better information than a late promise.
Akira: You're using my own project against me. That's low. Also fair."""),
c("neutral", "Which one has the earliest real deadline?", """Akira: The poster. The other two can wait if I actually say so.
MC: Start with that message.
Akira: Right. One bridge at a time."""),
c("bad", "If you want people around, doing them favors is part of the deal.", """Akira: I know I've said things like that.
MC: You can't have it both ways.
Akira: Maybe I don't like what the deal turns me into.""")], """
Stage: She sends three clear replies. One friend answers with a cheerful 'Next week is fine.' Another finds help elsewhere.
Akira: Nobody has removed my name from the friendship register.
MC: There's a register?
Akira: No. Terrible privacy policy. We rejected it.
""", ["phone", "three_request_messages"], "worried"),
s(10, "An Apology With No Pitch", "library", """
Stage: Akira has privately corrected the disclosure from the earlier survey session. The classmate agreed that she may discuss the lesson without sharing any more details.
Akira: She heard my apology. She hasn't said she trusts me with personal stuff again.
MC: That might take time.
Akira: I know. I nearly offered to fix her whole project to make it less awkward.
MC: Did you?
Akira: No. I could practically hear the terrible bargain forming.
Narration: She has written 'Don't turn apology into sales pitch' at the top of her notebook.
""", [
c("neutral", "Give her some time. You don't need to solve it today.", """Akira: I'm bad at leaving things unfinished.
MC: She isn't a task.
Akira: Right. I'm glad you said that."""),
c("bad", "If she accepted the apology, she should stop making it awkward.", """Akira: She didn't promise to make me feel better.
MC: You admitted you were wrong.
Akira: That was the part I owed her. It doesn't buy the next part."""),
c("good", "Keep doing what you promised, even when nobody thanks you for it.", """Akira: That sounds less satisfying than one big helpful gesture.
MC: Probably.
Akira: Okay. I can survive being unspectacular for a while.""")], """
Stage: We remove the last unnecessary personal fields from the pilot. Akira checks the consent text out loud before saving it.
Akira: Will you tell me if I start dressing up a bad idea with enough enthusiasm to make it sound good?
MC: I can try.
Akira: Don't let me finish the whole presentation first. You'll be trapped here for hours.
""", ["project_notebook", "consent_text"], variants={
"warm": "Akira: I can say the embarrassing version to you. You don't seem to need the impressive one every time.",
"mixed": "Akira: I'm still working out which of my clever ideas are actually excuses.",
"cool": "Akira: I want to be clear about this before we keep working. Private means private."}),
s(11, "The Song in the Headphones", "class_a", """
Stage: While the prototype loads, a bright old pop song leaks from Akira's headphones. She hums the keyboard line before noticing.
MC: You know the whole thing?
Akira: My mum plays it while she cooks. At this point it's part of the kitchen equipment.
MC: You make the keyboard part sound easy.
Akira: I learned it by getting it wrong a lot. Music is very efficient at telling you when you're wrong.
Stage: She taps the rhythm on the desk, then stops because another class is working nearby.
Akira: I'll send you the song, if you want. No required essay afterwards.
""", [
c("good", "Send the one you like, not the one you think I'll like.", """Akira: Dangerous. You might learn that I have embarrassing taste.
MC: I'm prepared for that risk.
Akira: Fine. The version with the ridiculous opening stays."""),
c("bad", "Pick something more romantic. Then I might listen properly.", """Akira: You could listen because I wanted to share it.
MC: I was trying to make that sound like a hint.
Akira: It sounded like a condition."""),
c("neutral", "Sure. I don't know much music from that time.", """Akira: Then I'll start with one song instead of twelve.
MC: A bold exercise in restraint.
Akira: Don't praise it until I actually press send.""")], """
Stage: We finish the loading test. My phone receives one song and, after a visible struggle across the desk, no long explanation.
Akira: I want it on record that I had context ready.
MC: I believe you.
Narration: Later, the chorus follows me all the way to the gate.
""", ["headphones", "phone", "laptop"], "delighted"),
s(12, "The Small Version", "class_a", """
Stage: Teacher feedback is simple: keep the reliable pilot and drop the features we cannot maintain. Akira's original three-idea sheet sits beside the laptop.
Akira: I wanted it to feel like the start of something big.
MC: It could still be a start.
Akira: I know. I just liked the version where I got to show everybody I could do all of it.
Narration: She doesn't throw the sheet away. She folds it and puts it behind the current plan.
Akira: My dad says opening a second shop won't fix the first one's broken fridge.
MC: Your dad gets a lot of good lines.
Akira: Years of practice. Captive audience.
""", [
c("neutral", "We can keep the extra ideas in the report as future work.", """Akira: Clearly marked as ideas. No accidental promises.
MC: You've learned to fear that word.
Akira: A healthy professional fear."""),
c("good", "Let's finish the version people can use without needing you beside it.", """Akira: A thing that works even when I'm not proving myself at it.
MC: That sounds like a good result.
Akira: Yeah. It does, actually. Let's make the instructions good."""),
c("bad", "Keep the big features in the slides. We don't have to demonstrate them.", """Akira: Then we'd be presenting something we don't have.
MC: Everybody makes a project sound better.
Akira: I'd rather make this one actually better.""")], """
Stage: We write a short maintenance guide and test it on someone who has never seen the prototype. Their first question reveals a button label neither of us understood.
Akira: One word. We argued over the architecture and got beaten by one word.
MC: Should we put that in the report?
Akira: Absolutely. It's the funniest useful thing we've learned.
Narration: A few minutes after she leaves, I send a message: 'I'd like to spend time together when this is finished.' I stare at it for a while, then make myself put the phone away instead of adding three increasingly confusing explanations.
""", ["feature_sheet", "maintenance_guide", "laptop"]),
s(13, "What Did You Mean?", "canteen", """
Stage: During a lunch break from the final project checks, Akira asks about an earlier message from the MC.
Akira: You wrote, 'I'd like to spend time together when this is finished.'
MC: I did.
Akira: I nearly invited the whole project group. Then a friend said I should ask what you meant first.
Narration: She looks directly at me. No joke arrives to rescue either of us.
Akira: I miss things when people expect me to understand a hint. I don't want to make you uncomfortable by guessing.
MC: I'm glad you asked.
""", [
c("bad", "I thought it was obvious. Everyone else figured it out.", """Akira: I didn't ask everyone else. I'm asking you.
MC: It just feels awkward explaining it.
Akira: It's awkward being told I should already know."""),
c("good", "I meant just us. I'm interested in you, and I'd like to see whether you feel the same.", """Akira: Okay. Thank you for saying it plainly.
MC: You don't have to answer while we're surrounded by lunch trays.
Akira: Good. I'd like to think without somebody asking me to pass the soy sauce."""),
c("neutral", "I was hoping for time with just you, but we can take it slowly.", """Akira: I can do slowly. I just need to know which conversation we're having.
MC: This one. No secret test.
Akira: That's a relief.""")], """
Stage: We agree to finish the school handover first and speak privately afterwards. She doesn't promise a romantic answer.
Akira: I do know that I want to be honest with you.
Narration: I can work with an honest answer. Waiting is harder, but it isn't unfair.
""", ["phone_message", "lunch_trays"], "flustered"),
s(14, "Handover", "class_a", """
Stage: The approved project is ready for its final class demonstration. Akira has written both names on the first slide.
MC: You remembered the paper backup.
Akira: It has its own envelope. I have developed an emotional attachment.
Stage: A tester asks a question Akira cannot answer immediately. She looks at the MC instead of filling the gap with a promise.
Akira: We haven't tested that. Did we put it in the follow-up notes?
MC: We did. It's still open.
Narration: She nods and writes down the question. Nothing collapses because she doesn't know everything.
""", [
c("good", "Let's explain the limits as clearly as the useful parts.", """Akira: 'Here's what it does. Here's what it doesn't.' That should fit on one slide.
MC: Your most ambitious small slide yet.
Akira: Don't tempt me. I'll add a graph."""),
c("neutral", "I'll handle the questions while you show the demo.", """Akira: Deal. Stop me if I'm going too fast.
MC: I'll use the agreed hand signal.
Akira: The normal one, please. We are still at school."""),
c("bad", "Promise the extra feature. We can work it out after they leave.", """Akira: No. I know how quickly 'later' turns into a pile of people waiting for me.
MC: It might win them over.
Akira: Then I'd be winning them over with something I haven't done.""")], """
Stage: The handover ends with a working pilot, a short guide and a few useful questions. The class applauds briefly, then asks about homework.
Akira: That's almost comforting. Our big moment and then algebra.
MC: Ordinary life continues.
Akira: Meet me in the canteen next time? Without bringing the laptop.
""", ["laptop", "backup_envelope", "presentation"], variants={
"warm": "Akira: When I picture the demo going well, you're in the picture. That's been true for a while.",
"mixed": "Akira: I've thought about what you said. I'd like to finish that conversation properly.",
"cool": "Akira: I want us to talk clearly about where we stand once the work is finished."}),
s(15, "No More Hints", "canteen", """
Stage: Finale encounter; show the route-ending warning first. The canteen is quiet after the supervised activity block. Akira has brought two canned coffees and no laptop.
Akira: I chose these without a survey. Personal growth.
MC: Brave.
Akira: Before I make six jokes and accidentally avoid the point: I did think about us.
Narration: She turns the can between her hands. Her glasses charm taps softly against the frame.
MC: I still want to ask you out. Clearly, this time.
Akira: Then ask. I promise not to invite the whole class by accident.
""", [
c("neutral", "Would you like to spend Saturday together and see how it feels?", """Akira: That's clear enough. I appreciate the lack of a five-year plan.
MC: I barely have a Saturday plan.
Akira: Good place to start."""),
c("bad", "I've waited while you figured it out. I need a yes now.", """Akira: You can ask for an answer. You can't choose which one I owe you.
MC: I didn't want to stay in the dark.
Akira: Then let me tell you the truth without trying to hurry it into something else."""),
c("good", "I'd like a date, just the two of us. Tell me what you actually want.", """Akira: Even if it isn't the answer you're hoping for?
MC: I'd rather hear you than keep guessing.
Akira: Okay. Here goes.""")], """
Stage: Apply the final score once. Compare effective good and bad totals and play exactly one epilogue. Her answer is supplied by the ending, never by a shared acceptance line.
""", ["two_coffee_cans"], variants={
"warm": "Akira: I've been looking forward to seeing you with nothing left to troubleshoot.",
"mixed": "Akira: We got good at working together. This part needs its own answer.",
"cool": "Akira: I'm glad we finished the project. I need to be honest about the rest."})
]

ENDINGS = [
e("good", "Player Two", "class_a", "A clean warm Class A project desk after school; pink-bobbed Akira with brown eyes behind glasses grins as she and the charcoal-silhouette MC place their hands together on a shared notebook. Simple completed demo on the nearby laptop, no readable text.", """
Akira: I want that. A date. I've been trying to imagine what makes it different from hanging out, and I keep coming back to one thing.
MC: What's that?
Akira: I want you to know I chose it. Not because you helped me or because I want everyone happy. Because I like you.
Narration: I had a good reply ready. It leaves my head before I can use it.
MC: I like you too.
Akira: Great. Excellent. We have successfully exchanged the relevant information.
Stage: Later, they return the project notebook to Class A. She leaves her hand on the cover beside his, then turns her palm upward. He takes it.
Akira: Saturday. There's a café I'd like to show you. After that, maybe a walk. I will try not to turn it into a guided lecture.
MC: One topic allowed.
Akira: You're negotiating with the wrong girl.
Narration: She's laughing now, but she isn't rushing past what happened. Neither am I. Saturday is a date, and today is the first time holding her hand feels simple enough to enjoy.
Stage: Unlock Akira / Good. Credits, then title.
"""),
e("neutral", "A Good Teammate", "canteen", "Akira and the MC silhouette sit across a canteen table with the closed project notebook between them, warm ordinary daylight, friendly expressions and comfortable but distinct personal space.", """
Akira: I like being with you. I don't feel the part I think you're asking for. I kept checking because I didn't want to give you the wrong answer.
MC: Thanks for not giving me the easy one.
Akira: I'm not sure there was an easy one.
Stage: She slides the second coffee toward him and leaves her hand on her own side of the table.
Akira: If being friends is difficult right now, you can say so. I won't turn it into an emergency project.
MC: A little difficult. I'd like to try, with some room to be awkward.
Akira: Awkward I can handle. Unclear instructions are the real enemy.
Narration: A week later, we have lunch with the project group. She asks before showing anyone a photo, then catches me noticing.
Akira: What? Some features do make it into the final version.
MC: I'm glad that one did.
Narration: I don't secretly count the afternoon as progress toward changing her mind. We finished something useful together. I can let that be true without asking it to become something else.
Stage: Unlock Akira / Neutral. Credits, then title.
"""),
e("bad", "Disconnect", "class_a", "Akira alone at an ordinary Class A desk, short pink bob and glasses clear, closing a disconnected laptop; empty project chair beside her, expression thoughtful and resolved rather than shattered.", """
Akira: I don't want to date you. I'm going to say that plainly, because I've spent too long hoping a softer version would make this easier.
MC: I thought we were getting closer.
Akira: Sometimes we were. Other times, I felt like being useful was the part of me you were waiting for. I don't want to build a relationship around that feeling.
Narration: Her voice isn't loud. That makes it harder to pretend I misunderstood.
MC: All right. I'll give you space.
Akira: Thank you. We can keep the handover polite. We don't have to pretend nothing happened.
Stage: The following day, she closes the project laptop after returning the shared files. The spare chair stays pushed in.
Narration: The project will keep working without either of us beside it. I'm glad we managed that, even if I wish I'd handled the rest differently.
Akira: Your copy is in the class folder. The instructions are on the first page.
MC: Got it. Good luck with the next idea.
Akira: Thanks. I'm going to take a break before I start one.
Stage: Unlock Akira / Bad. Credits, then title.
""")]
