using System;
using System.IO;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace AprilAgain.Editor
{
    public static class RuntimeChecks
    {
        static AprilAgainGame Game=>UnityEngine.Object.FindAnyObjectByType<AprilAgainGame>();
        public static string Smoke()
        {
            var game=Game;int assertions=0;
            void Check(bool ok,string name){assertions++;if(!ok)throw new Exception("Runtime regression: "+name);}
            Check(game.catalog.sprites.All(x=>x.sprite!=null),"all catalog sprite references survive import");
            game.NewGame();game.TestFinishDialogue();game.TestFinishDialogue();game.TestFinishDialogue();
            Check(game.State.mode=="explore"&&game.State.opening,"opening reaches exploration");
            foreach(var c in game.Content.characters)
            {
                var q=game.Content.sequences.First(x=>x.id=="observe."+c.id);game.Travel(q.location);game.Talk(c.id);game.TestFinishDialogue();
            }
            Check(game.State.observed.Count==5,"all first-day observations");
            game.TestFinishDialogue();Check(game.State.mode=="explore","post-tour returns to room");
            // Exercise the real Home and Sleep buttons rather than a parallel state path.
            void Click(string name)
            {
                var b=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).FirstOrDefault(x=>x.gameObject.activeInHierarchy&&x.name==name);
                Check(b!=null&&b.interactable,"clickable "+name);b.onClick.Invoke();
            }
            Click("Home");game.TestFinishDialogue();Check(!game.State.opening&&game.State.location=="bedroom","first night complete");
            Click("Sleep • next day");game.TestFinishDialogue();
            Check(game.State.day==2&&game.State.location=="gate","day two begins");
            var girl=game.Content.characters.First(c=>GameRules.Eligible(game.Content,game.State,c.id));
            var scene=GameRules.Next(game.Content,game.State,girl.id);game.Travel(scene.location);game.Talk(girl.id);
            game.TestFinishDialogue();Check(game.State.mode=="choices","choice prompt reached");
            var choice=scene.choices.First(x=>x.kind=="good");game.Choose(choice.id);
            Check(game.State.choices.Count==1&&game.State.Route(girl.id).good==1,"real choice commits exactly once");
            Check(game.TestSave("smoke-roundtrip"),"save mid-response");
            game.TestFinishDialogue();game.TestLoad("smoke-roundtrip");Check(game.State.mode=="dialogue"&&game.State.choices.Count==1,"mid-response resume");
            game.TestFinishDialogue();game.Talk(girl.id);Check(game.State.choices.Count==1,"busy click awards nothing");game.TestFinishDialogue();
            game.TestMap();Click("Close");game.TestJournal();Click("Close");game.TestSettings();Click("Sound");
            Canvas.ForceUpdateCanvases();
            var sliders=UnityEngine.Object.FindObjectsByType<Slider>(FindObjectsSortMode.None);
            Check(sliders.All(x=>x.fillRect.rect.width<=535&&x.handleRect.rect.height<=57),"slider geometry stays within track");
            var music=sliders.First(x=>x.name=="Music slider");float oldMusic=music.value;music.value=0;
            Check(game.GetComponent<GameAudio>().GetComponents<AudioSource>()[0].volume==0,"music mute reaches source");music.value=oldMusic;
            Click("Done");game.TestGallery();Click("Close");
            // A backup must recover a malformed primary save without resetting progress.
            Check(game.TestSave("smoke-recovery")&&game.TestSave("smoke-recovery"),"atomic replacement creates backup");
            File.WriteAllText(Path.Combine(SaveStore.Root,"smoke-recovery.json"),"{ damaged");
            var restored=SaveStore.Load("smoke-recovery",game.Content);Check(restored!=null&&restored.choices.Count==1,"corrupt primary recovers backup");
            var result="Runtime smoke passed: "+assertions+" assertions; intro, 5 observations, home/sleep, encounter, mid-response load, menus, corruption recovery.";
            Directory.CreateDirectory("Documentation/Testing");File.WriteAllText("Documentation/Testing/runtime-smoke.txt",result);return result;
        }
        public static string TextFit()
        {
            var game=Game;var go=new GameObject("Text layout probe",typeof(RectTransform),typeof(TextMeshProUGUI));
            var text=go.GetComponent<TextMeshProUGUI>();text.font=game.catalog.titleFont;text.fontSize=40;text.richText=false;
            var c=game.Content;
            var lines=c.sequences.SelectMany(s=>s.lines).Concat(c.scenes.SelectMany(s=>s.setup.Concat(s.closing).Concat(s.temperature.SelectMany(t=>t.lines)).Concat(s.choices.SelectMany(x=>x.response)))).Concat(c.endings.SelectMany(e=>e.lines)).ToArray();
            float max=0;string longest="";
            foreach(var l in lines){var size=text.GetPreferredValues(l.text,1560,10000);if(size.y>max){max=size.y;longest=l.text;}}
            UnityEngine.Object.DestroyImmediate(go);
            var result="Checked "+lines.Length+" spoken/narration lines. Maximum dialogue height at 40px / 1560px: "+max+". Available: 112. Longest: "+longest;
            File.WriteAllText("Documentation/Testing/dialogue-fit.txt",result);
            if(max>112)throw new Exception(result);return result;
        }
        public static string Endings()
        {
            var game=Game;int completed=0;
            foreach(var c in game.Content.characters)
            foreach(var kind in new[]{"good","neutral","bad"})
            {
                game.NewGame();var s=game.State;s.opening=false;s.day=2;s.mode="explore";
                var r=s.Route(c.id);r.next=15;if(kind=="good")r.good=14;else if(kind=="bad")r.bad=14;else r.neutral=14;
                for(int n=1;n<15;n++)s.choices.Add(game.Content.scenes.First(x=>x.girl==c.id&&x.number==n).choices.First(ch=>ch.kind==kind).id);
                int guard=0;while(!GameRules.Eligible(game.Content,s,c.id))
                { if(s.block<GameRules.Blocks(s))s.block++;else GameRules.AdvanceDay(s);if(++guard>200)throw new Exception("Finale unavailable"); }
                var scene=GameRules.Next(game.Content,s,c.id);s.location=scene.location;game.Explore();game.BeginEncounter(c.id);
                var before=SaveStore.Load("pre-finale",game.Content);if(before==null||before.Route(c.id).next!=15)throw new Exception("Pre-finale save missing");
                game.TestFinishDialogue();game.Choose(scene.choices.First(ch=>ch.kind==kind).id);game.TestFinishDialogue();
                string id=c.id+".ending."+kind;
                if(s.pendingEnding!=id||s.background!="cg_"+c.id+"_"+kind||!SaveStore.Read<Preferences>("preferences").gallery.Contains(id))throw new Exception("Wrong or missing ending "+id);
                game.TestFinishDialogue();if(s.mode!="ended")throw new Exception("Credits not reached");
                game.TestCloseMenu();completed++;
            }
            var result="Runtime ending checks passed: "+completed+" finales, independent checkpoints, CG unlocks and credits transitions.";
            File.WriteAllText("Documentation/Testing/ending-smoke.txt",result);return result;
        }
    }
}
