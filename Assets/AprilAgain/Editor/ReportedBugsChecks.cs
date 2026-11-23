using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using TMPro;
using UnityEditor;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

namespace AprilAgain.Editor
{
    public static class ReportedBugsChecks
    {
        const string Output="Documentation/Testing/ReportedBugs";
        static AprilAgainGame Game=>UnityEngine.Object.FindAnyObjectByType<AprilAgainGame>();
        static readonly List<string> Issues=new List<string>();
        static int checks;
        static void Check(bool value,string description){checks++;if(!value)Issues.Add(description);}
        static Button PointerTarget(float x,float y)
        {
            Canvas.ForceUpdateCanvases();
            var world=GameObject.Find("World").GetComponent<RectTransform>();
            var point=RectTransformUtility.WorldToScreenPoint(Camera.main,world.TransformPoint(new Vector3(x*1920,-y*1080,0)));
            return TargetAt(point);
        }
        static Button TargetAt(Vector2 point)
        {
            var data=new PointerEventData(EventSystem.current){position=point,button=PointerEventData.InputButton.Left};
            var hits=new List<RaycastResult>();EventSystem.current.RaycastAll(data,hits);
            return hits.FirstOrDefault().gameObject?.GetComponentInParent<Button>();
        }
        static void CheckExits(AprilAgainGame g)
        {
            foreach(var destination in g.Content.locations.First(l=>l.id==g.State.location).neighbors)
            {
                string name=destination=="bedroom"?"My room":destination=="field"?"Sports field":g.Content.locations.First(l=>l.id==destination).name;
                var target=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).FirstOrDefault(b=>b.gameObject.activeInHierarchy&&(b.name=="Door "+name||b.name==name+" ›"));
                bool reachable=false;
                if(target!=null)
                {
                    var r=target.GetComponent<RectTransform>();
                    foreach(float x in new[]{.15f,.5f,.85f})foreach(float y in new[]{.15f,.5f,.85f})
                    {
                        var p=RectTransformUtility.WorldToScreenPoint(Camera.main,r.TransformPoint(new Vector3(r.rect.xMin+r.rect.width*x,r.rect.yMin+r.rect.height*y)));
                        if(TargetAt(p)==target)reachable=true;
                    }
                }
                Check(reachable,g.State.location+": visible navigation to "+destination+" is missing or blocked");
            }
        }
        static void Click(Button button)
        {
            if(button==null)return;
            ExecuteEvents.Execute(button.gameObject,new PointerEventData(EventSystem.current){button=PointerEventData.InputButton.Left},ExecuteEvents.pointerClickHandler);
        }
        public static string Start()
        {
            checks=0;Issues.Clear();Directory.CreateDirectory(Output);Game.StartCoroutine(Run());return "Reported bug reproduction started";
        }
        public static string ReadingOptions()
        {
            var g=Game;const BindingFlags flags=BindingFlags.Instance|BindingFlags.NonPublic;var type=typeof(AprilAgainGame);
            var prefs=(Preferences)type.GetField("prefs",flags).GetValue(g);
            bool instant=prefs.instantText,afterClick=prefs.autoAfterClick,afterChoice=prefs.skipAfterChoices;
            int assertions=0;
            void Assert(bool condition,string message){assertions++;if(!condition)throw new Exception(message);}
            void Set(string name,bool value)=>type.GetField(name,flags).SetValue(g,value);
            bool Get(string name)=>(bool)type.GetField(name,flags).GetValue(g);
            try
            {
                prefs.instantText=true;g.NewGame();
                var body=(TextMeshProUGUI)type.GetField("body",flags).GetValue(g);
                Assert(body.maxVisibleCharacters>=body.textInfo.characterCount,"Instant text still animates");
                prefs.autoAfterClick=false;Set("auto",true);type.GetMethod("AdvanceInput",flags).Invoke(g,null);Assert(!Get("auto"),"Click does not stop auto");
                prefs.autoAfterClick=true;Set("auto",true);type.GetMethod("AdvanceInput",flags).Invoke(g,null);Assert(Get("auto"),"Keep-auto setting ignored");
                foreach(bool resume in new[]{false,true})
                {
                    g.NewGame();g.State.opening=false;g.State.day=2;
                    var character=g.Content.characters.First(c=>GameRules.Eligible(g.Content,g.State,c.id));var scene=GameRules.Next(g.Content,g.State,character.id);
                    g.State.location=scene.location;g.BeginEncounter(character.id);prefs.skipAfterChoices=resume;Set("skip",true);g.TestFinishDialogue();
                    Assert(g.State.mode=="choices"&&!Get("skip"),"Skip does not wait at choices");
                    Assert(g.State.choices.Count==0,"Skip chooses an answer automatically");
                    g.Choose(scene.choices[0].id);Assert(Get("skip")==resume,"Resume-skip preference ignored");
                }
                g.NewGame();string legacy=System.Text.RegularExpressions.Regex.Replace(JsonUtility.ToJson(g.State),"\"(?:firstName|lastName)\":\"[^\"]*\",?","");
                File.WriteAllText(Path.Combine(SaveStore.Root,"reported-legacy.json"),legacy);g.TestLoad("reported-legacy");
                Assert(GameRules.Valid(g.Content,g.State),"Legacy save no longer loads");
                Assert((string)type.GetProperty("PlayerFirst",flags).GetValue(g)=="Ren","Legacy save has no default player name");
                string result=assertions+" reading/legacy-save checks passed";File.WriteAllText(Output+"/reading-options.txt",result);return result;
            }
            finally{prefs.instantText=instant;prefs.autoAfterClick=afterClick;prefs.skipAfterChoices=afterChoice;g.TestTitle();type.GetMethod("PersistPreferences",flags).Invoke(g,null);}
        }
        public static string StartNavigationReview()
        {
            checks=0;Issues.Clear();Directory.CreateDirectory(Output);Game.StartCoroutine(NavigationReview());return "All-scene navigation review started";
        }
        static IEnumerator NavigationReview()
        {
            var g=Game;int scenes=0;
            foreach(var asset in g.Content.assets.Where(a=>a.id.StartsWith("bg_")||a.id.StartsWith("room_")||a.id.StartsWith("observation_")))
            {
                string girl="",location;
                if(asset.id.StartsWith("observation_"))
                {var sequence=g.Content.sequences.First(q=>q.background==asset.id);girl=sequence.girl;location=sequence.location;}
                else
                {
                    if(asset.id.StartsWith("room_"))girl=g.Content.characters.First(c=>asset.id.StartsWith("room_"+c.id+"_")).id;
                    string prefix=girl==""?"bg_":"room_"+girl+"_";
                    location=g.Content.locations.OrderByDescending(l=>l.id.Length).First(l=>asset.id.StartsWith(prefix+l.id+"_")).id;
                }
                g.TestWorldArtwork(asset.id,location,girl);yield return null;yield return null;CheckExits(g);scenes++;
            }
            g.NewGame();g.State.opening=false;g.State.day=3;g.State.mode="explore";g.Explore();
            foreach(var location in g.Content.locations.Where(l=>l.id!="bedroom"))
            {
                g.TestMap();yield return null;yield return null;
                var button=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).First(b=>b.gameObject.activeInHierarchy&&b.name=="Map room "+location.id);
                var filter=button.GetComponent<MapHitRegion>();var center=filter.regions[0].center;
                var point=RectTransformUtility.WorldToScreenPoint(Camera.main,filter.space.TransformPoint(new Vector3(center.x,-center.y)));
                var target=TargetAt(point);Check(target==button,"Map room pointer blocked: "+location.id);int block=g.State.block;
                Click(target);yield return null;
                Check(g.State.location==location.id,"Map click does not reach "+location.id);Check(g.State.block==block,"Map travel consumes activity time");
                g.TestCloseMenu();
            }
            File.WriteAllLines(Output+"/navigation-issues.txt",Issues);File.WriteAllText(Output+"/navigation-status.txt",scenes+" world scenes; "+checks+" pointer/navigation checks; "+Issues.Count+" failures");g.TestTitle();
        }
        static IEnumerator Run()
        {
            var g=Game;
            var centers=new Dictionary<string,Vector2>{{"katya",new Vector2(.66f,.48f)},{"akira",new Vector2(.45f,.56f)},{"seoyun",new Vector2(.18f,.58f)},{"mari",new Vector2(.245f,.56f)},{"svea",new Vector2(.67f,.57f)}};
            foreach(var girl in g.Content.characters)
            {
                g.NewGame();g.TestFinishDialogue();g.TestFinishDialogue();g.TestFinishDialogue();
                var sequence=g.Content.sequences.First(q=>q.id=="observe."+girl.id);g.Travel(sequence.location);yield return null;yield return null;
                CheckExits(g);
                var center=centers[girl.id];var target=PointerTarget(center.x,center.y);
                Check(target!=null&&target.name.Contains(girl.id=="seoyun"?"Seo-yun":girl.id=="akira"?"Akira":girl.id=="katya"?"Katya":girl.id=="mari"?"Mari":"Svea"),girl.id+": pointer over visible character does not select her");
                Click(target);yield return null;
                Check(g.State.mode=="dialogue"&&g.State.segment==sequence.id,girl.id+": pointer click does not start introduction");
                PresentationChecks.Capture("reported-intro-"+girl.id);
            }
            foreach(var location in g.Content.locations)
            {
                foreach(var next in location.neighbors)
                    Check(location.exits.Any(e=>e.destination==next),location.id+": scene navigation missing "+next);
                g.TestWorldArtwork("bg_"+location.id+"_day",location.id,"");yield return null;yield return null;CheckExits(g);
            }
            Check(g.Content.locations.First(l=>l.id=="lobby").exits.Any(e=>e.destination=="class_a"&&e.kind=="door_or_path"),"Lobby classroom door is labelled as a canteen");
            foreach(var asset in g.Content.assets.Where(a=>a.id.StartsWith("wardrobe_")&&a.id.EndsWith("_full_body")))
            {
                var texture=AssetDatabase.LoadAssetAtPath<Texture2D>(asset.path);
                Check(texture.height>=1280,asset.id+": only "+texture.width+"x"+texture.height+" for a large dialogue sprite");
            }
            g.NewGame();yield return null;
            var advance=PointerTarget(.5f,.3f);Check(advance!=null&&advance.name=="Advance story","Clicking scenery outside the text does not advance dialogue");
            if(advance!=null&&advance.name=="Advance story")
            {
                foreach(var text in UnityEngine.Object.FindObjectsByType<TextMeshProUGUI>(FindObjectsSortMode.None))text.maxVisibleCharacters=int.MaxValue;
                int line=g.State.lineIndex;Click(advance);Check(g.State.lineIndex==line+1,"Background click advances more or less than one line");
            }
            Check(new Preferences().fullscreen,"Fresh settings do not default to fullscreen");
            Check(typeof(Preferences).GetField("skipUnread")!=null,"Skip unread option missing");
            g.TestTitle();yield return null;
            var newGame=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).First(b=>b.gameObject.activeInHierarchy&&b.name=="New game");Click(newGame);yield return null;
            var fields=UnityEngine.Object.FindObjectsByType<TMP_InputField>(FindObjectsSortMode.None);
            Check(fields.Length==2,"New game has no first-name / last-name entry");
            if(fields.Length==2)
            {
                var first=fields.First(f=>f.name=="First name input");var last=fields.First(f=>f.name=="Last name input");
                first.text="<broken>";last.text="Name";
                Click(UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).First(b=>b.name=="Start story"));
                Check(first.gameObject.activeInHierarchy,"Invalid name bypasses validation");
                first.text="Alexanderthebest";last.text="Montgomery-Smith";
                PresentationChecks.Capture("name-entry");
                Click(UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).First(b=>b.name=="Start story"));yield return null;
                Check(g.State.firstName=="Alexanderthebest"&&g.State.lastName=="Montgomery-Smith","Entered name is not used by the game");
                Check(g.TestSave("reported-name"),"Named story cannot save");g.TestLoad("reported-name");
                Check(g.State.firstName=="Alexanderthebest"&&g.State.lastName=="Montgomery-Smith","Name lost on load");
                var method=typeof(AprilAgainGame).GetMethod("PersonalizedLines",BindingFlags.Instance|BindingFlags.NonPublic);
                var authored="Ren Takahashi. "+string.Join(" ",Enumerable.Repeat("Ren and Takahashi checked the display together.",14));
                var lines=(Line[])method.Invoke(g,new object[]{new[]{new Line{speaker="MC",text=authored,kind="dialogue"}}});
                Check(lines.Length>1,"Long custom names do not paginate");
                Check(string.Join(" ",lines.Select(l=>l.text))==authored.Replace("Ren","Alexanderthebest").Replace("Takahashi","Montgomery-Smith"),"Pagination loses text or substitutes names incorrectly");
                var probe=new GameObject("Name text probe",typeof(RectTransform),typeof(TextMeshProUGUI)).GetComponent<TextMeshProUGUI>();probe.font=g.catalog.bodyFont;probe.fontSize=40;
                Check(lines.All(l=>probe.GetPreferredValues(l.text,1560,10000).y<=112),"Custom name text overflows dialogue");UnityEngine.Object.Destroy(probe.gameObject);
                var pref=(Preferences)typeof(AprilAgainGame).GetField("prefs",BindingFlags.Instance|BindingFlags.NonPublic).GetValue(g);
                foreach(int page in Enumerable.Range(0,3))
                {
                    typeof(AprilAgainGame).GetMethod("SettingsPage",BindingFlags.Instance|BindingFlags.NonPublic).Invoke(g,new object[]{page});yield return null;
                    PresentationChecks.Capture("settings-"+new[]{"reading","sound","display"}[page]);
                    foreach(var text in UnityEngine.Object.FindObjectsByType<TextMeshProUGUI>(FindObjectsSortMode.None).Where(t=>!string.IsNullOrEmpty(t.text)))
                        Check(text.GetPreferredValues(text.text,text.rectTransform.rect.width,10000).y<=text.rectTransform.rect.height+2,"Settings text overflow: "+text.text);
                }
                g.TestCloseMenu();
                g.NewGame();yield return null;int initial=g.State.lineIndex;
                pref.skipUnread=false;typeof(AprilAgainGame).GetField("skip",BindingFlags.Instance|BindingFlags.NonPublic).SetValue(g,true);
                typeof(AprilAgainGame).GetField("lineKey",BindingFlags.Instance|BindingFlags.NonPublic).SetValue(g,"unread-regression-"+Guid.NewGuid().ToString("N"));yield return new WaitForSecondsRealtime(.2f);
                Check(g.State.lineIndex==initial,"Read-only skip passes unread text");
                pref.skipUnread=true;typeof(AprilAgainGame).GetField("skip",BindingFlags.Instance|BindingFlags.NonPublic).SetValue(g,true);yield return new WaitForSecondsRealtime(.25f);
                Check(g.State.lineIndex>initial,"Skip unread does not advance unread text");pref.skipUnread=false;
            }
            File.WriteAllLines(Output+"/issues.txt",Issues);File.WriteAllText(Output+"/status.txt",checks+" checks, "+Issues.Count+" failures.");g.TestTitle();
        }
    }
}
