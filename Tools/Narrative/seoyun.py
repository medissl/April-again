from story_schema import c, s, e

ID = "seoyun"
NAME = "Han Seo-yun"
VOICE = "Polite, observant, quietly funny and capable of firm disagreement. Concrete details before abstract feelings. Curiosity and creative work matter alongside family. Her origin is not an invitation for a rescue story."
SCENES = [
s(1, "A Place on the Page", "library", """
Stage: The librarian asks the MC and Seo-yun to check a shelf of donated atlases during an activity block.
MC: This one still has a country that isn't there anymore.
Seo-yun: Quite a few of them do. That's why we have to check the publication date.
MC: So it isn't a mistake?
Seo-yun: It depends whether you are using it to travel or to understand what somebody believed in 1987.
Narration: She turns the heavy book carefully, supporting the spine with both hands.
MC: I'm Takahashi. I saw you drawing during orientation.
Seo-yun: Han Seo-yun. And now I know I wasn't as invisible as I thought.
""", [
c("bad", "You looked lonely, so I thought you probably wanted someone to come over.", """Seo-yun: I was drawing a cloud.
MC: I thought you seemed sad.
Seo-yun: Sometimes I am just concentrating."""),
c("good", "What were you trying to catch in the drawing?", """Seo-yun: The shadow underneath the cloud. It kept changing before I finished.
MC: Did you get it?
Seo-yun: A cloud. Perhaps not that cloud."""),
c("neutral", "I'll check the dates if you sort them into groups.", """Seo-yun: That would help. Start with the stack beside you.
MC: Including the very old one?
Seo-yun: Especially the very old one. It has earned its own category.""")], """
Stage: We finish the shelf record. One atlas goes into a history-reference pile instead of the current maps.
Seo-yun: It still has a use. We just have to say what it is.
Narration: She writes the date on a neat paper slip and makes room for it beside the newer books.
""", ["atlases", "library_record"]),
s(2, "Please Leave the Page There", "library", """
Stage: We work on a library-window display about places students would like to learn about. A folded sketch slips out of Seo-yun's journal.
MC: You dropped something.
Seo-yun: Ah. Thank you.
Narration: There are mountains on the visible side. Some writing shows through the paper, but it is not addressed to me.
MC: Should I put it inside the book?
Seo-yun: The blue journal, please. Not the atlas. Someone might borrow that.
Stage: She reaches over a pile of reference cards, unable to get to it herself.
""", [
c("neutral", "I'll leave it face down beside your journal.", """Seo-yun: That's fine. I can put it away in a moment.
MC: No rush.
Seo-yun: Thank you for not balancing another book on top of it."""),
c("good", "Here. I haven't opened it.", """Seo-yun: You didn't need to explain, but I appreciate knowing.
MC: I guessed it wasn't part of the display.
Seo-yun: Correct. Some pages are only mine."""),
c("bad", "I only read the first bit. It sounded interesting.", """Seo-yun: I would rather you asked before reading any of it.
MC: It was right there.
Seo-yun: Yes. I dropped it. I didn't offer it.""")], """
Stage: The journal goes into her bag. We keep researching public material for the display.
Seo-yun: You can ask about the drawing. I may say no, but you can ask.
MC: Fair enough.
Narration: I return to the reference cards. There's plenty here that she has actually chosen to share.
""", ["blue_journal", "folded_sketch", "reference_cards"]),
s(3, "Three Seconds of Sky", "corridor", """
Stage: We have permission to photograph the corridor view for the library display. Seo-yun holds a small camera with a worn strap.
Seo-yun: Wait. The cloud is almost past the roof.
MC: I can wait.
Stage: She takes one picture, checks it, then moves half a step sideways.
MC: Does that little move make a difference?
Seo-yun: The drainpipe was growing out of the tree. I don't think the tree deserved it.
Narration: She shows me the second picture. The sky looks like the sky outside, but also like something she deliberately noticed.
Seo-yun: We can include someone in the foreground, if they agree.
""", [
c("good", "I'll stand there. Tell me where to look, and let me see it before we use it.", """Seo-yun: Of course. You can reject it.
MC: Even if the drainpipe looks good?
Seo-yun: A difficult sacrifice, but yes."""),
c("bad", "Take pictures of people when they don't notice. That's more natural.", """Seo-yun: A natural expression isn't worth making somebody uncomfortable.
MC: They might never know.
Seo-yun: I would know. That matters to me."""),
c("neutral", "I'd rather stay out of the picture. I'll hold the spare battery.", """Seo-yun: That helps too. Thank you for saying so.
MC: My modeling career ends before it begins.
Seo-yun: Very efficient of you.""")], """
Stage: We choose an unoccupied view for the public display and keep any approved test portrait private. Seo-yun labels the files before leaving.
MC: How long did the best shot take?
Seo-yun: Three seconds. And most of an afternoon of waiting for them.
""", ["camera", "sky_photo"], "curious"),
s(4, "An Unfamiliar Word", "class_c", """
Stage: Our classes share a reading activity. Seo-yun is adding a short English caption to one of her display photographs.
Seo-yun: Is 'faraway' one word here?
MC: I think so. I should probably check before I sound convincing.
Seo-yun: That would be a useful habit for both of us.
Stage: She has written three versions of a sentence and crossed out none of them.
MC: Which one do you like?
Seo-yun: The shortest. It doesn't sound impressive, but it says what I saw.
""", [
c("neutral", "Let's ask the English teacher to check it.", """Seo-yun: Yes. I want the meaning checked, not the whole thing rewritten.
MC: I'll say that when we ask.
Seo-yun: Thank you."""),
c("bad", "Use the longest one. Complicated English always looks better on a display.", """Seo-yun: Even if I wouldn't normally say it?
MC: Nobody has to know.
Seo-yun: I would like to recognize my own sentence."""),
c("good", "Keep the short one. We can check the grammar without changing your voice.", """Seo-yun: 'The same sky, somewhere else.'
MC: That makes sense to me.
Seo-yun: Good. It made sense in my head. Those aren't always the same result.""")], """
Stage: The teacher confirms the wording. Seo-yun copies it in her own handwriting and puts the other versions in her journal.
MC: Keeping the rejected lines?
Seo-yun: They were useful on the way here. I don't have to throw them away because they aren't the final one.
""", ["caption_drafts", "dictionary"]),
s(5, "The Quiet Table", "library", """
Stage: A long reading session leaves both of us quiet. A gust from the open window turns three pages of the atlas at once.
MC: Even the book wants to skip ahead.
Seo-yun: It has been on this continent for nearly an hour.
Stage: She finds the old page and rests a paperweight on the corner.
Narration: I have run out of harmless things to say. She seems perfectly capable of remaining here without them.
MC: Am I being boring?
Seo-yun: You are reading. It's allowed in a library.
""", [
c("good", "Then I'll stop worrying about filling every gap.", """Seo-yun: You can talk if you want to. You don't have to perform being good company.
MC: I may need practice at that.
Seo-yun: We have a very patient audience. Mostly books."""),
c("neutral", "I'll take a short walk and come back to the notes.", """Seo-yun: All right. Would you close the far window on your way past?
MC: For our impatient reader?
Seo-yun: Exactly."""),
c("bad", "You could help by talking a little more.", """Seo-yun: I didn't realize there was a target.
MC: I just can't tell what you're thinking.
Seo-yun: You can ask. That doesn't mean I will always have something ready to say.""")], """
Stage: By the end of the block, the display notes are finished. We leave a bookmark at the page we will need next.
Narration: The silence lasts another moment as we pack up. This time, I notice the sound of her pencil case closing instead of treating it as a problem.
""", ["atlas", "paperweight", "bookmark"], variants={
"warm": "Seo-yun: It is easier to concentrate when I know the person beside me doesn't mind the quiet.",
"mixed": "Seo-yun: We don't have to make every afternoon feel the same.",
"cool": "Seo-yun: I would like to finish the reading before we discuss anything personal."}),
s(6, "Sweet Enough", "canteen", """
Stage: A display-planning lunch gives Seo-yun an unexpected problem: the meal she ordered is much spicier than the description suggested.
Seo-yun: I made a mistake.
MC: With the noodles?
Seo-yun: I thought the little pepper symbol was decoration. An optimistic interpretation.
Stage: She reaches for water. The MC has plain rice and a small fruit cup.
MC: Want to ask for something milder?
Seo-yun: Yes. Before I try to prove a point that nobody has asked me to prove.
""", [
c("bad", "Aren't you supposed to be used to spicy food?", """Seo-yun: I don't think my birthplace ordered lunch for me.
MC: I didn't mean anything by it.
Seo-yun: I know. Please ask what I like next time."""),
c("good", "I'll watch your things while you ask. You can have the fruit afterwards if you want.", """Seo-yun: Thank you. Is that an offer or an attempt to keep me alive?
MC: Mostly an offer.
Seo-yun: Reassuringly specific."""),
c("neutral", "I can ask the staff whether there's a plain version.", """Seo-yun: We can ask together. I should learn how the menu works.
MC: No decorative peppers this time.
Seo-yun: A strict new policy.""")], """
Stage: The staff helps her choose a milder option. We finish the work with the menu safely out of reach.
Seo-yun: Sweet things are easier. Usually they warn you by looking sweet.
MC: You haven't met every school vending machine yet.
Seo-yun: Then my education continues.
""", ["noodle_bowl", "fruit_cup", "menu"]),
s(7, "Who Gets the Credit?", "class_c", """
Stage: The display photos are printed for a trial layout. A classmate has enlarged Seo-yun's sky picture and left the author line blank.
Classmate: We can just put the class name. It's a group project.
Stage: The classmate goes to collect another sheet. Seo-yun smooths the photograph with the side of her hand.
MC: Do you want your name on it?
Seo-yun: Yes. I think I do.
MC: Then we can say so.
Seo-yun: I am practicing saying that before I apologize for it.
""", [
c("neutral", "Let's check how the other photos are credited.", """Seo-yun: A consistent rule would be fair.
MC: Photographer under each image, class on the overall display?
Seo-yun: That would include both."""),
c("good", "Tell them you want the photo credited. I'll support you without speaking over you.", """Seo-yun: All right. Stay here a moment?
MC: Of course.
Seo-yun: I know it is a small thing. It still takes a little courage."""),
c("bad", "Don't make it awkward. Everyone knows you took it.", """Seo-yun: Then writing my name should not be a problem.
MC: I just don't want an argument.
Seo-yun: Neither do I. I still want to be credited.""")], """
Stage: The class agrees on a simple credit line for every contribution. Seo-yun writes her name beneath the sky photograph.
MC: How does it look?
Seo-yun: Like mine. And like part of the class. I was worried I had to choose.
""", ["photo_prints", "credit_labels"], "determined"),
s(8, "Questions With an Audience", "lobby", """
Stage: Students stop by the trial display. One asks Seo-yun where she is from, then follows the answer with several loud questions about her family.
Seo-yun: I don't want to discuss my family here.
Classmate: I was only curious.
Stage: A teacher redirects the group to the display captions. Afterwards, Seo-yun gathers the feedback sheets with careful, stiff movements.
MC: Do you want me to tell them to stop asking?
Seo-yun: I already asked. I would like that to have counted.
Narration: The remaining sheets can wait for a moment.
""", [
c("good", "It counted. If they ask me, I'll say you keep your family life private.", """Seo-yun: Thank you. You don't need to explain my reasons for me.
MC: I won't.
Seo-yun: Then we can get back to this. The display has become surprisingly crooked."""),
c("bad", "They didn't mean any harm. You could have answered a few things.", """Seo-yun: I answered the question I wanted to answer.
MC: I only meant they were interested.
Seo-yun: Being interested doesn't decide what someone else has to share."""),
c("neutral", "Want to take the feedback sheets somewhere quieter?", """Seo-yun: Yes. The library table would be better.
MC: I'll carry these.
Seo-yun: Leave the pens. Otherwise we'll be borrowing them for the rest of the term.""")], """
Stage: We finish the feedback count in a quiet place. Seo-yun asks the supervising teacher to handle further personal questions at the display.
Narration: She has a plan before I can offer one. I follow her lead.
""", ["feedback_sheets", "display_board"], "determined"),
s(9, "The Unsent Page", "library", """
Stage: During the research block, Seo-yun puts a sealed letter inside her journal. She chooses to explain that she was born in Pyongyang and moved to Japan with her parents before high school.
Seo-yun: I am writing to a relative. I keep starting again because I want to describe ordinary things without making them sound unimportant.
Seo-yun: I was born in Pyongyang. My parents and I moved here before high school, but some of our family stayed. I don't want a letter about my new life to sound as if I've stopped thinking about them.
MC: School lunches count as ordinary things.
Seo-yun: So do difficult classes. And a tree outside a window. It is strange how much there is once I begin.
Narration: She keeps the envelope closed. I don't ask who will read it or how it will get there.
Seo-yun: I worry that wanting a larger life will sound like I don't value the people in this one.
""", [
c("bad", "You should forget about going back and focus on the life you have here.", """Seo-yun: I didn't ask you to choose which part of my family I should care about.
MC: I thought it would be easier.
Seo-yun: Easier for whom?"""),
c("neutral", "You don't have to fit every feeling into this letter.", """Seo-yun: That's true. I keep treating it as my one chance to explain everything.
MC: It can just be a letter about this week.
Seo-yun: With a very careful paragraph about noodles."""),
c("good", "You can miss people and still want new things. The letter can hold both.", """Seo-yun: Both. Without one cancelling the other.
MC: That's how it sounds when you talk about them.
Seo-yun: I hope it sounds that way when I write it.""")], """
Stage: She writes a fresh page while the MC checks public reference captions. The letter never appears on screen as readable text.
Seo-yun: I put the tree in.
MC: Good.
Seo-yun: And the noodles. Future historians will have a complete picture.
""", ["sealed_letter", "blue_journal"], "sad"),
s(10, "Too Far From Here", "class_c", """
Stage: The class is researching future study options. Seo-yun has printed an overseas university page and placed it beneath her school worksheet.
MC: Are you thinking of applying someday?
Seo-yun: Someday is doing a lot of work in that sentence.
MC: That's allowed. We just started high school.
Seo-yun: The requirements are clear. The cost is less encouraging. My English still needs work. My parents worry about distance.
Narration: She says each problem carefully, as if putting them in order might make them smaller.
Seo-yun: I haven't even decided what I want to study. I just know I want the chance to decide.
""", [
c("good", "Which part can you learn about now? We don't have to solve the whole future today.", """Seo-yun: Language support. And whether there are scholarships later.
MC: Those sound like real questions.
Seo-yun: Much less dramatic than despair. I should try them first."""),
c("neutral", "The school adviser might know where to start.", """Seo-yun: I could ask for an appointment. Privately.
MC: You don't have to bring a finished plan.
Seo-yun: I may need to hear that again before I go."""),
c("bad", "If we get close, you might not want to leave anyway.", """Seo-yun: I don't want to make my future smaller to prove that I care about someone.
MC: I meant that things can change.
Seo-yun: They can. I want the change to include what I want too.""")], """
Stage: She writes two questions for the adviser. The university printout stays in the folder rather than going in the bin.
Narration: I don't know whether she'll ever study there. She doesn't either. At least the page can be a possibility instead of a verdict.
""", ["study_options", "adviser_questions"], variants={
"warm": "Seo-yun: I wanted to show you this before I talked myself out of wanting it.",
"mixed": "Seo-yun: You don't need to tell me it's certain. I know it isn't.",
"cool": "Seo-yun: I can discuss the practical questions. I need the decision to remain mine."}),
s(11, "The Blurred Picture", "corridor", """
Stage: Seo-yun's camera moved during the one shot she hoped to use for the final display. The leaves are sharp; the important patch of sky isn't.
Seo-yun: I checked everything except whether my hands were shaking.
MC: Can we take another?
Seo-yun: The weather will be different. That was the part I wanted.
Stage: She puts the camera down, then turns the screen away from herself.
MC: Want a break from looking at it?
Seo-yun: Maybe. I have been trying to dislike it into becoming a better photograph.
""", [
c("neutral", "Let's check the other shots before we choose anything.", """Seo-yun: There might be one I overlooked.
MC: No promises about hidden masterpieces.
Seo-yun: Sensible. My expectations need supervision."""),
c("bad", "It looks fine. You're worrying about something nobody else will notice.", """Seo-yun: I noticed. I wanted it to look a particular way.
MC: I was trying to reassure you.
Seo-yun: You don't have to agree with my standards. Please don't tell me they aren't there."""),
c("good", "It's a disappointing shot. We can decide what to do after you've had a minute.", """Seo-yun: Thank you for not trying to make it secretly perfect.
MC: It can just be annoying for a while.
Seo-yun: I would enjoy that permission.""")], """
Stage: After a break, she chooses an earlier image with a less dramatic sky and a composition she genuinely likes. The blurred one stays in her private archive.
Seo-yun: It happened. It doesn't need to be the picture on the wall.
Narration: She turns the camera screen back toward herself.
""", ["camera", "blurred_photo", "alternate_photo"], "sad"),
s(12, "A Story She Chose", "library", """
Stage: The display needs a short introduction. Seo-yun has written about the view from the school window rather than her personal history.
MC: Some people might expect a story about moving here.
Seo-yun: I know. I wanted to write about this window.
MC: What drew you to it?
Seo-yun: I can see the same hill from home. At school, the roof hides half of it. It took me a week to realize I knew it.
Narration: Her introduction is simple enough that I can picture the moment without seeing a photograph.
Seo-yun: Is it too ordinary?
""", [
c("good", "No. I can tell why this view matters because you actually want to describe it.", """Seo-yun: I was hoping that would be enough.
MC: We can tighten the last paragraph. The window stays.
Seo-yun: Good. It has been very cooperative."""),
c("bad", "Your background would get more attention. We should lead with that.", """Seo-yun: I am not choosing a story by how much attention it can get.
MC: The display is supposed to interest people.
Seo-yun: Then let this be interesting on its own terms."""),
c("neutral", "Let's show it to the librarian and ask whether the length works.", """Seo-yun: All right. I'd like feedback on the writing, not a different subject.
MC: I'll keep that clear.
Seo-yun: Thank you.""")], """
Stage: We edit two repeated sentences and leave the subject alone. Her name remains under the introduction and the photograph.
Narration: The final paragraph doesn't tell strangers everything about her. It gives them something she wanted them to see.
""", ["window_essay", "photo_print"]),
s(13, "The Other Side of the Glass", "library", """
Stage: The display is nearly ready. While the glue dries, Seo-yun moves two chairs to the window.
Seo-yun: You don't have to sit perfectly still. This isn't another portrait test.
MC: Good. I was about to develop a very formal posture.
Stage: She laughs, then watches a plane pass over the hill.
Seo-yun: When I was younger, I used to make up destinations for them.
MC: Do you still?
Seo-yun: Sometimes. More often now I wonder what somebody on it is seeing.
Narration: She leaves the thought there. It doesn't sound like a request for an answer.
""", [
c("bad", "I'd go anywhere with you. You wouldn't need to worry about anything.", """Seo-yun: That is a very large promise.
MC: Isn't it a nice one?
Seo-yun: I would rather know what you can honestly offer."""),
c("neutral", "Where do you imagine this one is going?", """Seo-yun: Somewhere with a very ordinary airport and disappointing sandwiches.
MC: A convincing destination.
Seo-yun: I am improving at realistic travel planning."""),
c("good", "I'd like to see what you draw next. Wherever your plans end up going.", """Seo-yun: Even if the plans change?
MC: Especially then. I don't know the ending in advance.
Seo-yun: Neither do I. That's beginning to feel less frightening.""")], """
Stage: The glue dries. We return the chairs before the library gets busy.
Seo-yun: Thank you for sitting with me.
MC: We got a lot of important airport planning done.
Seo-yun: And no one had to promise an entire life in one afternoon.
""", ["window_chairs", "drying_display"], "warm"),
s(14, "Under Her Name", "lobby", """
Stage: The finished library display is installed in the lobby for an open-campus afternoon. Seo-yun has chosen which pages to show and kept her journal in her bag.
MC: Your caption is getting more attention than the map.
Seo-yun: The map has had a long career. It can share.
Stage: A visitor praises the photograph and asks whether the MC took it. Seo-yun waits a beat before correcting them herself.
Seo-yun: It's mine. He helped prepare the display.
Narration: The visitor apologizes, then asks her about the composition. She answers without looking at me for permission.
""", [
c("good", "I'll take care of the handouts. You can talk about your work.", """Seo-yun: Are you sure?
MC: I know which way up the map goes now. I'm ready.
Seo-yun: A very strong qualification."""),
c("neutral", "We can answer the next questions together.", """Seo-yun: Yes. You know the preparation better than I do.
MC: You get the photography questions.
Seo-yun: A fair division."""),
c("bad", "You could have let it go. They were only trying to be nice.", """Seo-yun: I was nice when I corrected them.
MC: I didn't want it to be uncomfortable.
Seo-yun: I want us both to be comfortable with my name being on my work.""")], """
Stage: The open-campus block ends. We return the display to the library window where it will remain for the term.
Seo-yun: Could we talk here next time, after the work is done? There is something I would rather say without visitors.
Narration: I agree to come. I don't ask her to say it before she's ready.
""", ["finished_display", "handouts"], variants={
"warm": "Seo-yun: I wanted you to see it finished. You've seen so many of the unfinished parts.",
"mixed": "Seo-yun: I'm glad we kept the display true to the plan. I'd like the rest of our conversation to be clear too.",
"cool": "Seo-yun: We should finish the public work first. The personal conversation can wait until we have privacy."}),
s(15, "An Open Page", "library", """
Stage: Finale encounter; show the route-ending warning. Seo-yun sits by the library window with her closed journal and two blank bookmarks.
Seo-yun: I kept thinking about what I wanted to say. Then I worried I was preparing for a conversation you might not be having.
MC: I'm probably having it badly in my head too.
Stage: That earns a small smile. She turns one bookmark toward him but keeps the journal closed.
MC: I like you, Seo-yun. I would like to be more than friends.
Seo-yun: Then we should talk about what that means for both of us.
""", [
c("neutral", "We don't have to know everything yet. I'd like to understand what you feel now.", """Seo-yun: That is something I can answer.
MC: I'm listening.
Seo-yun: All right."""),
c("good", "I'd like to date you, without asking you to put your own plans aside.", """Seo-yun: And without promising that neither of us will ever change?
MC: I can't promise that. I can promise to be honest about it.
Seo-yun: Then I will be honest too."""),
c("bad", "If you feel the same, promise you'll stay here with me.", """Seo-yun: I won't make that promise to prove affection.
MC: I don't want to lose you before anything begins.
Seo-yun: I understand being afraid. I still need room to choose my own life.""")], """
Stage: Record the final choice exactly once and compare effective good and bad totals. Continue only to the matching ending.
""", ["blue_journal", "two_blank_bookmarks"], variants={
"warm": "Seo-yun: I look forward to the afternoons when I know I'll see you.",
"mixed": "Seo-yun: I've been trying to understand the difference between trusting somebody and wanting something more.",
"cool": "Seo-yun: I wanted us to talk directly. I don't want politeness to become another misunderstanding."})
]

ENDINGS = [
e("good", "The Next View", "library", "Seo-yun with dark low-tied hair and her small left-eye mole by the library window, sharing an open sky-sketch page with a charcoal MC silhouette; equal side-by-side seating, clean daylight and a hopeful unforced smile.", """
Seo-yun: I like you too. I haven't found a graceful way to say it, so that will have to do.
MC: I think it did very well.
Stage: She opens the journal to a page she has marked herself. It holds a drawing of the library window and two chairs.
Seo-yun: You can look at this one.
Narration: The second chair isn't a promise that I'll always be there. It is a place she has chosen to draw for me now.
MC: Would you like to go for a walk after school? A proper date.
Seo-yun: Yes. Somewhere with a view you like. I want to know what you notice too.
MC: I may need to discover an interesting view first.
Seo-yun: We can start with an ordinary one. I have good evidence that those can work.
Stage: She slides a blank bookmark toward him. He writes the place and time; she adds a tiny cloud in the corner.
Narration: Her future is still wide and uncertain. Mine is too. For the first time, I don't feel that uncertainty as a question I have to answer before I'm allowed to be happy.
Stage: Unlock Seo-yun / Good. Credits, then title.
"""),
e("neutral", "A Bookmark", "library", "A handwritten-style bookmark without legible generated writing rests on a returned atlas; Seo-yun offers it across the library table, kind reserved smile, respectful friendship distance.", """
Seo-yun: I care about you. I don't think what I feel is the same as what you're asking for.
MC: Thank you for telling me.
Seo-yun: I don't want to lose a friendship by giving you a hopeful answer I can't mean.
Narration: I let the disappointment arrive without asking her to make it smaller.
MC: Can I have some time to get used to it?
Seo-yun: Of course.
Stage: Several school days later, the MC returns an atlas. A bookmark waits inside its cover, placed there with the librarian's permission. It has a small cloud and a note asking whether he would like to help check a new shelf.
MC: This is very careful recruiting.
Seo-yun: I wanted the invitation to be easy to decline.
MC: I can help for a while.
Narration: She hands me the list. I take it because I want to be here, not because I think the right number of afternoons will change her answer.
Stage: The library window is open a little. This time, she puts the paperweight on the atlas before the wind can turn the page.
Stage: Unlock Seo-yun / Neutral. Credits, then title.
"""),
e("bad", "Her Own Direction", "library", "Seo-yun at the library window closes her dark-blue journal, shoulders calm, gaze turned toward the exit and her own future; cool natural light, no dramatic distress or spectacle.", """
Seo-yun: I don't want a romantic relationship with you. I need more distance than we've had.
MC: Did I make you feel trapped?
Seo-yun: Too often, I felt that there was an answer you wanted and that my own answer was something we would have to get past.
Narration: Her hands rest on the closed journal. I know better than to ask to see the page that might explain everything in a way I prefer.
MC: I'm sorry. I won't ask you to reconsider.
Seo-yun: Thank you for hearing me now.
Stage: She collects the study-options sheet and her camera. The library display stays on the wall, under her name.
Narration: I had begun imagining a future with her before I learned how to leave space for the one she wanted. She isn't taking that future away from me. It was never mine to reserve.
MC: I hope the adviser appointment helps.
Seo-yun: It already has. I have a few things I can do next.
Stage: She leaves with her own plans. The MC returns the atlas to its shelf.
Stage: Unlock Seo-yun / Bad. Credits, then title.
""")]
