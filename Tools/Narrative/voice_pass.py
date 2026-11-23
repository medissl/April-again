"""A deliberate second writing pass: performed lines, gestures and code-switching.

Replacements are individually authored, not randomly sprinkled catchphrases.
The builder checks that every target still exists exactly once.
"""


def all_blocks(route):
    for scene in route["scenes"]:
        yield scene["setup"]
        yield scene["closing"]
        yield from scene["temperature"].values()
        for choice in scene["choices"]:
            yield choice["response"]
    for ending in route["endings"]:
        yield ending["lines"]


def replace(route, old, new):
    matches = [line for block in all_blocks(route) for line in block if line["text"] == old]
    assert len(matches) == 1, (route["id"], old, len(matches))
    matches[0]["text"] = new


def insert_after(route, number, field, needle, text):
    block = route["scenes"][number - 1][field]
    indexes = [i for i, line in enumerate(block) if line["text"] == needle]
    assert len(indexes) == 1, (number, needle)
    block.insert(indexes[0] + 1, {"speaker": "Stage", "text": text})


def perform(route):
    swaps = {
"katya": [
("I remember. You were examining the map upside down.", "Takahashi-san. Yes, I remember. You were examining the map upside down."),
("Ekaterina Romanova. Katya is sufficient. Now, do you know how to use a stapler?", "Ekaterina Romanova. Katya will do. Now—can you operate a stapler, or should I lower my expectations again?"),
("Then I checked the same pile twice.", "Bozhe moy... I checked the same pile twice. Very impressive, Katya."),
("A regrettable use of the word royal.", "Royal. Certainly. I am sure the royal family personally approved the milk powder."),
("An unusually specific invitation.", "A tea complaint. With company. You make a very strange social calendar, Takahashi-san."),
("It should only take a moment.", "It should only take a—no, little creature, that is my cuff. Bozhe moy."),
("You are making this very difficult to object to.", "You are making this difficult to object to. Deliberately, I suspect."),
("Fine. Thank you. And leave the notes on the dry side of the windowsill.", "F-fine. Thank you. The notes, Takahashi-san. Dry side of the windowsill. Please concentrate."),
("I have eaten bread before, Takahashi.", "I have eaten bread before, Takahashi-san. Russia does have bakeries."),
("It is damaging an expensive piece of fabric.", "This animal is damaging an expensive sleeve. It has absolutely no respect for tailoring."),
("Perhaps. That does not make it all I want.", "Perhaps. I would still like to discover whether I have a personality when nobody needs a budget."),
("I am trying to learn from it.", "I am trying to learn from it. Kindly allow me to be annoyed and competent at the same time."),
("I was hoping you would come. Try not to look so surprised by that.", "I was hoping you would come. No—do not look so pleased. I have not finished."),
("I like you too. I would have preferred to announce that without becoming this nervous.", "I like you too. There. An entirely ordinary sentence. Apparently beyond my ordinary capabilities."),
("Yes, Takahashi. I am attempting to eliminate ambiguity.", "Yes, Takahashi—Ren. Bozhe moy. I am attempting to eliminate ambiguity, not create more of it."),
("We shall have to see how terrible.", "We shall have to see how terrible. And don't smile like that, durak. You'll make me smile too.")],
"akira": [
("Too late. Good news: you have a memorable brand.", "Too late. Memorable brand, low customer-acquisition cost. Sorry—sorry, I'm doing the economics thing. Hi."),
("Yes! A small test before we build anything. You're useful, map guy.", "A small test before we build anything. Yes! Map guy joins the team. We should probably use your actual name before I print badges."),
("Well. My beautiful data is mostly lunch fiction.", "Jamkkanman—hold on. That's two different queues. Oh, my beautiful graph. I've committed lunch fraud."),
("Right. Sorry. This bridge, then. Ignore everything else for a minute.", "Chotto matte. Back up, Akira. One bridge. We're learning one bridge, not the entire history of strategy games."),
("I forget that my internal tutorial doesn't come with subtitles.", "I do this with WARNO too. Someone asks one question and suddenly I'm defending a thesis. Stop me at the second map."),
("I hate that you're right about the difficult part.", "Ugh. Right about the difficult part as well. Couldn't you have picked a less inconvenient talent?"),
("He's seen worse. Phone goes in the bag.", "He's seen worse. Phone. Bag. Zip. There. If I reach for it, make a disapproving calculator noise."),
("My dad owns a grocery shop. There's a long family tradition of bringing home something that needs cooking tonight.", "Dad owns a grocery shop. If something needs using today, surprise, it's dinner. Eomma calls it 'a flexible menu.' Mum's very diplomatic."),
("Fine. That's annoyingly good product advice.", "Aish. Fine. Good product advice. I reserve the right to grumble while I use it."),
("The internet has chosen personal violence.", "The internet is gone. Not slow. Gone. I'm taking this personally."),
("Okay. I can survive being unspectacular for a while.", "Okay. Quietly reliable. I can be that. It'll be weird without a little success sound, but I'll cope."),
("Fine. The version with the ridiculous opening stays.", "Fine. The ridiculous opening stays. Don't blame me when you're humming it in maths. I warned you with my entire personality."),
("That's a relief.", "Oh. Good. I was about to develop a flowchart for the hint. This is much nicer."),
("The normal one, please. We are still at school.", "The normal one. Please. Not the dramatic throat-cutting thing from rehearsal; I thought the projector was dying."),
("I want that. A date. I've been trying to imagine what makes it different from hanging out, and I keep coming back to one thing.", "I want that. A date. Just us. I tried practicing that without the giant smile, but the giant smile appears to be included."),
("What's that?", "Keep the smile. I like it."),
("I want you to know I chose it. Not because you helped me or because I want everyone happy. Because I like you.", "I like you, Ren. That's what I keep coming back to. No clever explanation. You, specifically. It's inconveniently hard to improve on."),
("Great. Excellent. We have successfully exchanged the relevant information.", "Daebak. Okay. Excellent. Two people. Same answer. Why was that harder than the whole demo?"),
("You're negotiating with the wrong girl.", "You're negotiating with the wrong girl. One topic has subtopics, Ren. You should have read the small print.")],
"seoyun": [
("Han Seo-yun. And now I know I wasn't as invisible as I thought.", "Han Seo-yun. Ah... so I wasn't as invisible as I thought. I should apologize to the cloud. It was our private meeting."),
("You didn't need to explain, but I appreciate knowing.", "Gomawoyo. Thank you. You didn't need to explain, but... I appreciate knowing."),
("Is 'faraway' one word here?", "'Faraway'... one word, in English? I know what I want it to mean. The spelling is being less cooperative."),
("I made a mistake.", "A... I have made a mistake. Quite a warm one."),
("I don't think my birthplace ordered lunch for me.", "I don't think my birthplace ordered lunch for me. I would have asked it to choose something milder."),
("A difficult sacrifice, but yes.", "A difficult sacrifice. But yes, the photographer will survive your artistic disagreement."),
("I hope it sounds that way when I write it.", "Geureom... then perhaps I can write it that way too. Both things, on the same page."),
("That is something I can answer.", "That is something I can answer. Let me... let me say it in the right order."),
("I wanted to show you this before I talked myself out of wanting it.", "I wanted to show you before I became very sensible and put it away again. I am sometimes much too sensible."),
("I would rather know what you can honestly offer.", "I would rather know what you can honestly offer. One walk, perhaps. We could begin with one walk."),
("I like you too. I haven't found a graceful way to say it, so that will have to do.", "I like you too. Joahaeyo... I practiced it in both languages. Neither version feels easier while you're looking at me."),
("Neither do I. That's beginning to feel less frightening.", "Neither do I. I think... yes. I think that is beginning to feel less frightening."),
("Yes. Somewhere with a view you like. I want to know what you notice too.", "Yes. And Ren? Somewhere with a view you like. I want to know what you notice too.")],
"mari": [
("Your sleeve is caught on the button. May I?", "Ano... your sleeve. It's caught on the button. May I?"),
("I'm your classmate.", "Your classmate, Takahashi-kun. I'd like to stay your classmate."),
("I wasn't... Ah. I suppose I was.", "I wasn't—ah. I was, wasn't I? You caught me before the leaflets even started."),
("You don't need to make the stitches perfect. They only need to hold.", "Slowly. The stitches don't need to be perfect; they need to hold. And please don't look at me while you're holding the needle."),
("I can do them, but we were both asked to help.", "I can. But we were both asked to help, Takahashi-kun. Here—this pile is yours."),
("I'm trying to find out what makes me happy without guessing it for someone else.", "I know. I am trying to find out what I like before somebody needs me to like something else. Just this once. Let me keep the mushrooms."),
("Company. Quiet company, if that's all right.", "Company. Quiet company, if that's... if that's all right. Stay where I can see you, but you don't have to keep talking."),
("I nearly brought a spare lunch. Then I thought you might assume I had called you here because you looked hungry.", "I nearly brought a spare lunch. Ano... don't laugh. I thought you might assume I'd called you here because you looked hungry."),
("I'm nervous. It's a rather nice kind of nervous, at least in part.", "I'm nervous. Daijoubu—I'm all right. A nice kind of nervous, I think. Mostly."),
("I would like to go out with you. I wanted to know I could say that without also promising to be easy to love.", "I would like that. Yes, Ren. A date. Oh... saying your name without the rest of it feels surprisingly bold."),
("You don't have to promise that.", "Ren is fine. And you don't have to worry about getting every word right."),
("Good. Because I expect I'll still try to feed you when I'm avoiding a difficult conversation.", "Good. You'll still have to tell me when I offer you lunch instead of answering a question. Gently, please. I'm likely to be embarrassed already."),
("I may be predictable about a few things.", "I may be predictable, Takahashi-kun. I have other qualities, I promise. Give me a minute to remember them."),
("We know. We're leaving on time.", "Yes. Otsukaresama deshita—thank you for today. We're leaving on time. I promise."),
("I care about you, but I don't want a romantic relationship. It took me a while to separate wanting you to be happy from knowing my own answer.", "I care about you, Takahashi-kun. But I don't want to date you. I kept trying to find a kinder sentence. I think... I think this is the kindest one I can actually mean.")],
"svea": [
("Here.", "Oi. Here. Bounce it."),
("Not anymore. Bounce it.", "Not anymore. Keep it low. I'd like my nose where it is."),
("I'm sure I know when I'm hungry.", "I know when I'm hungry, Takahashi. Got several years of experience."),
("What.", "...What. Oi. You want the ingredients or something?"),
("Brother gave it to me. Stupid joke.", "Brother gave it to me. Stupid joke. Betsuni—it's not a big deal. Give me the zip a second."),
("I'm not pretending. I'm tired.", "Boku wa daijoubu. I'm okay. Just tired. Big difference. You heard me, yeah?"),
("Usually. Other people take longer.", "Usually. Other people take longer. Nobody puts the instructions where you can see them."),
("I like different things.", "I like different things. Nobody's confiscating my basketball."),
("Yeah. I want that. A date. With you, before you come up with some terrible follow-up question.", "Yeah. I want that. A date. With you, Ren. ...There. Said it. Don't make the face."),
("I was trying to think of a good one.", "I'm trying not to grin. It's not going well."),
("Dangerous use of time.", "Yeah. I noticed."),
("Actual lunch. Don't pick somewhere with decorative portions.", "Actual lunch. Big plates. If somebody serves one leaf and calls it a concept, we're leaving."),
("Been looking forward to this. Don't grin. Makes it harder to say.", "Been looking forward to this. Mou... stop grinning. Makes it harder to get the words out."),
("I was fine on my own. Still am.", "Boku... I'm fine on my own. Always was. You get that, yeah?"),
("I like you. Not in the dating way. Took a while to be sure, but I'm sure now.", "I like you, Takahashi. Just... not like that. Took a while to be sure. Don't want to keep you guessing now I am.")]
    }
    for old, new in swaps[route["id"]]:
        replace(route, old, new)
    if route["id"] == "katya":
        insert_after(route, 5, "setup", "I prefer not to owe people for small favors.", "She folds her arms, then tucks a silver lock behind her ear. The gesture gives away more than her voice does.")
        insert_after(route, 9, "setup", "It was my mother. That is all.", "The clipped schoolroom rhythm returns, each word carefully placed. A trace of Russian still rounds the last vowel.")
    elif route["id"] == "akira":
        insert_after(route, 1, "setup", "That's what I need a second person for. My ideas don't tell each other no.", "Her sentences arrive in quick linked bursts. She starts a fourth thought, sees his expression and physically closes her mouth before it escapes.")
        insert_after(route, 13, "setup", "I miss things when people expect me to understand a hint. I don't want to make you uncomfortable by guessing.", "She adjusts the little charm on her glasses, then deliberately puts both hands on the table. No escape into another explanation.")
    elif route["id"] == "seoyun":
        insert_after(route, 1, "setup", "Han Seo-yun. Ah... so I wasn't as invisible as I thought. I should apologize to the cloud. It was our private meeting.", "Her consonants are careful and her voice soft, but the last sentence is dry enough to make it clear she is teasing.")
        insert_after(route, 10, "setup", "I haven't even decided what I want to study. I just know I want the chance to decide.", "She touches the edge of the paper, draws in a breath and says the next words more firmly than the first.")
    elif route["id"] == "mari":
        insert_after(route, 3, "setup", "Everyone at home likes it.", "She answers automatically, then watches his face. Her fingers tighten slightly around the lid of the thermos.")
        insert_after(route, 15, "setup", "I know. I wanted to be able to answer without offering you something else instead.", "She starts to straighten the cup, catches her hand and leaves it crooked. This time she keeps looking at him.")
    elif route["id"] == "svea":
        insert_after(route, 4, "setup", "It's milk. Strawberry happened to it. You can work out the rest.", "Her ears color before her face does. She gives the carton a fiercely unconvincing look of indifference.")
        insert_after(route, 12, "setup", "Was thinking we could sit for a bit. If you're not busy.", "The last few words lose volume. She clears her throat as if that might undo them.")
    route["voicePass"] = "Performed second pass: individual rhythm, meaningful pauses, physical tells and restrained contextual code-switching. English remains readable; no phonetic nationality caricatures."
