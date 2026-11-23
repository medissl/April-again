using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.UI;
using UnityEngine.UI;
using static AprilAgain.NovelUI;

namespace AprilAgain
{
    public partial class AprilAgainGame : MonoBehaviour
    {
        public NovelCatalog catalog;
        public Session State => session;
        public ContentData Content => catalog.Data;
        Session session; Preferences prefs; GameAudio audioPlayer;
        RectTransform stage, world, hud, dialogue, overlay;
        TextMeshProUGUI body; bool modal, title=true, auto, skip, hidden, resumeSkipAfterChoice;
        Action overlayReturn;
        float reveal, finishedAt; string lineKey="";
        TMP_FontAsset Font => catalog.bodyFont;
        void Start()
        {
            Application.targetFrameRate=60; Application.runInBackground=true;
            prefs=SaveStore.Read<Preferences>("preferences")??new Preferences();
            prefs.read=prefs.read??new List<string>();prefs.gallery=prefs.gallery??new List<string>();
            prefs.master=Mathf.Clamp01(prefs.master);prefs.music=Mathf.Clamp01(prefs.music);prefs.sound=Mathf.Clamp01(prefs.sound);prefs.ambience=Mathf.Clamp01(prefs.ambience);
            prefs.textSpeed=Mathf.Clamp(prefs.textSpeed,15,100);prefs.autoDelay=Mathf.Clamp(prefs.autoDelay,1,6);
            if(!prefs.displayInitialized){prefs.fullscreen=true;prefs.displayInitialized=true;}
            ApplyDisplay();
            audioPlayer=gameObject.AddComponent<GameAudio>();audioPlayer.Init(catalog,prefs);
            NovelUI.Skin=catalog;MakeCanvas(); ShowTitle();
        }
        void MakeCanvas()
        {
            var camera=Camera.main;
            if(camera==null){var c=new GameObject("Novel Camera",typeof(Camera),typeof(AudioListener));camera=c.GetComponent<Camera>();c.tag="MainCamera";}
            camera.orthographic=true;camera.backgroundColor=Hex("261D2B");camera.clearFlags=CameraClearFlags.SolidColor;
            var go=new GameObject("April again UI",typeof(RectTransform),typeof(Canvas),typeof(CanvasScaler),typeof(GraphicRaycaster));
            var canvas=go.GetComponent<Canvas>();canvas.renderMode=RenderMode.ScreenSpaceCamera;canvas.worldCamera=camera;canvas.planeDistance=1;
            var scaler=go.GetComponent<CanvasScaler>();scaler.uiScaleMode=CanvasScaler.ScaleMode.ScaleWithScreenSize;scaler.referenceResolution=new Vector2(1920,1080);scaler.screenMatchMode=CanvasScaler.ScreenMatchMode.Expand;
            stage=Rect("16 by 9 stage",go.transform,0,0,1920,1080);stage.anchorMin=stage.anchorMax=new Vector2(.5f,.5f);stage.pivot=new Vector2(.5f,.5f);stage.anchoredPosition=Vector2.zero;
            stage.gameObject.AddComponent<RectMask2D>();
            NovelUI.Stage=stage;
            world=Rect("World",stage,0,0,1920,1080);dialogue=Rect("Dialogue",stage,0,0,1920,1080);hud=Rect("HUD",stage,0,0,1920,1080);overlay=Rect("Menus",stage,0,0,1920,1080);
            if(FindAnyObjectByType<EventSystem>()==null){new GameObject("Event System",typeof(EventSystem),typeof(InputSystemUIInputModule));}
        }
        void Update()
        {
            if(stage==null)return;
            var k=Keyboard.current;
            if(k!=null&&k.escapeKey.wasPressedThisFrame){if(hidden){hidden=false;dialogue.gameObject.SetActive(true);hud.gameObject.SetActive(true);}else if(modal)DismissOverlay();else if(!title)Pause();}
            if(hidden&&Mouse.current!=null&&Mouse.current.leftButton.wasPressedThisFrame){hidden=false;dialogue.gameObject.SetActive(true);hud.gameObject.SetActive(true);return;}
            if(title||session==null||modal||hidden)return;
            if(k!=null&&k.hKey.wasPressedThisFrame&&session.mode=="dialogue"){HideInterface();return;}
            if(k!=null&&k.f5Key.wasPressedThisFrame){Save("quick");return;}
            if(k!=null&&k.f9Key.wasPressedThisFrame){Confirm("Load the quick save?",()=>Load("quick"));return;}
            if(session.mode=="dialogue"&&body!=null)
            {
                reveal+=Time.unscaledDeltaTime*prefs.textSpeed;body.maxVisibleCharacters=Mathf.FloorToInt(reveal);
                bool complete=body.maxVisibleCharacters>=body.textInfo.characterCount;
                if(complete&&finishedAt<0)finishedAt=Time.unscaledTime;
                if(k!=null&&(k.spaceKey.wasPressedThisFrame||k.rightArrowKey.wasPressedThisFrame))AdvanceInput();
                else if(skip){if(prefs.skipUnread||prefs.read.Contains(lineKey)){reveal=100000;if(complete&&Time.unscaledTime-finishedAt>.06f)NextLine();}else {skip=false;RefreshReadingControls();}}
                else if(auto&&complete&&Time.unscaledTime-finishedAt>prefs.autoDelay+body.text.Length/75f)NextLine();
            }
        }
        void Background(string id)
        {
            Clear(world);Image(world,"Background",0,0,1920,1080,Color.white,catalog.Sprite(id),true);
        }
        Button Btn(Transform p,string label,float x,float y,float w,float h,Action action,bool enabled=true,bool accent=false)
            => Button(p,label,x,y,w,h,Font,()=>{audioPlayer.Sfx("select");action();},enabled,accent,()=>audioPlayer.Sfx("hover"));
        Button Quiet(Transform p,string label,float x,float y,float w,float h,Action action)
            => QuietButton(p,label,x,y,w,h,Font,()=>{audioPlayer.Sfx("select");action();},()=>audioPlayer.Sfx("hover"));
        Button Icon(Transform p,string label,string icon,float x,float y,float size,Action action,Color? tint=null)
            => IconButton(p,label,icon,x,y,size,Font,()=>{audioPlayer.Sfx("select");action();},()=>audioPlayer.Sfx("hover"),tint);
        string Familiar(string name)
        {
            if(name=="MC")return PlayerFirst;
            if(name.Contains("Seo-yun"))return "Seo-yun";
            if(name.Contains("Mari"))return "Mari";
            if(name.Contains("Svea"))return "Svea";
            if(name.Contains("Akira"))return "Akira";
            return name;
        }
        void ShowTitle()
        {
            title=true;modal=false;auto=skip=hidden=resumeSkipAfterChoice=false;body=null;
            hud.gameObject.SetActive(true);dialogue.gameObject.SetActive(true);
            Clear(hud);Clear(dialogue);Clear(overlay);Background("title_establishing");
            audioPlayer.Music("bgm_daily");audioPlayer.Ambience("");
            Image(hud,"Title stationery",62,100,710,880,new Color(1,1,1,.88f),catalog.Sprite("spring_menu"));
            Image(hud,"April again",110,135,620,350,Color.white,catalog.Sprite("spring_wordmark"),true);
            Btn(hud,"New game",182,520,480,70,NameEntry,true,true);
            Btn(hud,"Continue",182,608,480,70,()=>Load("autosave"),SaveStore.Load("autosave",Content)!=null);
            Btn(hud,"Load",182,696,225,66,()=>Saves(false));
            Btn(hud,"Gallery",433,696,229,66,Gallery);
            Btn(hud,"Settings",182,782,480,66,Settings);
            Quiet(hud,"Credits",190,885,190,48,()=>Credits(false));
            Quiet(hud,"Quit",470,885,190,48,()=>Confirm("Close April, again?",()=>Application.Quit()));
        }
        public void NewGame()
        {
            NewGame("Ren","Takahashi");
        }
        public void NewGame(string first,string last)
        {
            session=Session.New(Content);session.firstName=first;session.lastName=last;
            title=false;auto=skip=resumeSkipAfterChoice=false;StartSequence("opening.bedroom","intro.gate");
        }
        SequenceData Seq(string id)=>Content.sequences.First(x=>x.id==id);
        SceneData CurrentScene=>Content.scenes.First(x=>x.id==session.scene);
        void StartSequence(string id,string after)
        {
            var q=Seq(id);session.location=q.location;session.background=q.background;session.portrait=q.portrait;session.girl=q.girl;
            StartLines(q.lines,id,after);
        }
        void StartLines(IEnumerable<Line> lines,string segment,string after)
        {
            session.lines=PersonalizedLines(lines);session.segment=segment;session.lineIndex=0;session.after=after;session.mode="dialogue";
            title=false;CloseOverlay(false);DrawDialogue();Autosave();
        }
        void DrawDialogue()
        {
            Clear(hud);Clear(dialogue);Background(session.background);
            audioPlayer.Ambience(session.background.Contains("rain")?"rain_window":"");
            audioPlayer.Music(session.pendingEnding!=""?"bgm_ending_"+session.pendingEnding.Split('.').Last():session.location=="bedroom"?"bgm_reflection":"bgm_daily");
            DrawActor();
            if(string.IsNullOrEmpty(session.pendingEnding))DrawSchoolHud(true);
            HitArea(dialogue,"Advance story",0,0,1920,1080,AdvanceInput);
            var panel=Image(dialogue,"Dialogue paper",24,792,1872,264,new Color(1,1,1,.84f),catalog.Sprite("spring_dialogue"));panel.raycastTarget=true;
            var advance=panel.gameObject.AddComponent<Button>();advance.transition=Selectable.Transition.None;advance.onClick.AddListener(AdvanceInput);
            if(session.lineIndex>=session.lines.Length){FinishSegment();return;}
            var l=session.lines[session.lineIndex];
            uint hash=2166136261;foreach(char ch in l.text)hash=unchecked((hash^ch)*16777619);
            lineKey=session.segment+"."+session.lineIndex+"."+hash.ToString("x8");
            string speaker=l.speaker=="Narration"?"":Familiar(l.speaker);
            if(speaker!="")
            {
                Image(dialogue,"Name ribbon",40,736,400,128,Color.white,catalog.Sprite("spring_name"),true);
                var name=Text(dialogue,speaker,150,756,260,64,catalog.titleFont,38,Paper,TextAlignmentOptions.Center);name.enableAutoSizing=true;name.fontSizeMin=24;name.fontSizeMax=38;
            }
            body=Text(dialogue,l.text,164,844,1560,112,catalog.titleFont,40,Ink);body.margin=Vector4.zero;
            if(session.segment.StartsWith("observe.")&&l.speaker=="MC")body.fontStyle=FontStyles.Italic;
            body.ForceMeshUpdate();reveal=prefs.reducedMotion||prefs.instantText?100000:0;body.maxVisibleCharacters=(int)reveal;finishedAt=-1;
            string[] labels={"Log","Auto","Skip","Save","Load","Menu"};
            string[] icons={"chat","play","skip","load","upload","settings"};
            Action[] actions={History,()=>{auto=!auto;skip=false;RefreshReadingControls();},()=>{skip=!skip;auto=false;RefreshReadingControls();},()=>Saves(true),()=>Saves(false),Pause};
            for(int i=0;i<labels.Length;i++)
            {
                var button=Quiet(hud,labels[i],1240+i*86,958,82,82,actions[i]);
                if(i==2)button.name="Skip read";
                var caption=button.GetComponentInChildren<TextMeshProUGUI>();caption.fontSize=22;
                caption.rectTransform.anchoredPosition=new Vector2(0,-38);caption.rectTransform.sizeDelta=new Vector2(82,32);
                Image(button.transform,"Icon",22,2,38,38,Ink,catalog.Sprite("spring_icon_"+icons[i]),true);
                if(i<labels.Length-1)Image(hud,"Quick menu divider",1323+i*86,966,1,46,new Color(.8f,.3f,.45f,.3f));
                if(i==1&&auto||i==2&&skip)Image(button.transform,"Active",30,78,22,3,Rose);
            }
        }
        void HideInterface()
        {
            CloseOverlay(false);hidden=true;dialogue.gameObject.SetActive(false);hud.gameObject.SetActive(false);
        }
        void RefreshReadingControls()
        {
            foreach(var button in hud.GetComponentsInChildren<Button>())
            {
                if(button.name!="Auto"&&button.name!="Skip read")continue;
                var old=button.transform.Find("Active");if(old!=null)Destroy(old.gameObject);
                if(button.name=="Auto"&&auto||button.name=="Skip read"&&skip)Image(button.transform,"Active",30,78,22,3,Rose);
            }
        }
        void DrawActor()
        {
            if(string.IsNullOrEmpty(session.girl)||string.IsNullOrEmpty(session.portrait)||session.segment.StartsWith("observe."))return;
            string id="char_"+session.girl+"_base";
            var scene=Content.scenes.FirstOrDefault(x=>x.id==session.scene);
            if(scene!=null&&scene.wardrobe!="school_uniform")id="wardrobe_"+scene.girl+"_"+scene.wardrobe+"_full_body";
            string expression=session.portrait.StartsWith("expr_"+session.girl+"_")?session.portrait.Substring(("expr_"+session.girl+"_").Length):"neutral";
            var acted=scene==null||scene.wardrobe=="school_uniform"?catalog.Sprite("vn_"+session.girl+"_"+expression):null;
            // Neutral staging follows the approved three-quarter composition;
            // emotional beats use the closer expression sprites.
            if(acted!=null&&expression!="neutral"&&session.mode!="choices")Image(world,"Character sprite",760,32,650,790,Color.white,acted,true);
            else if(session.mode=="choices")Image(world,"Character sprite",990,20,670,1020,Color.white,catalog.Sprite(id)??catalog.Sprite(session.portrait),true);
            else Image(world,"Character sprite",520,0,1067,1600,Color.white,catalog.Sprite(id)??catalog.Sprite(session.portrait),true);
        }
        public void NextLine()
        {
            if(modal||hidden||title||session==null||session.mode!="dialogue")return;
            if(body!=null&&body.maxVisibleCharacters<body.textInfo.characterCount){reveal=100000;body.maxVisibleCharacters=100000;return;}
            if(session.lineIndex<session.lines.Length)
            {
                var l=session.lines[session.lineIndex];
                session.history.Add((l.speaker=="Narration"?"":l.speaker=="MC"?PlayerFirst+": ":l.speaker+": ")+l.text);
                if(session.history.Count>400)session.history.RemoveAt(0);
                if(!prefs.read.Contains(lineKey))prefs.read.Add(lineKey);
                session.lineIndex++;
            }
            if(session.lineIndex>=session.lines.Length)FinishSegment();else DrawDialogue();
        }
        void FinishSegment()
        {
            var after=session.after;
            switch(after)
            {
                case "intro.gate":StartSequence("opening.gate","intro.class");return;
                case "intro.class":StartSequence("opening.orientation","tour");return;
                case "tour":session.location="lobby";Explore();Toast("First day • Look around and notice all five classmates. No time passes.");return;
                case "morningDone":session.location="gate";Explore();return;
                case "tourDone":Explore();Toast("You have seen all five classmates. Head home when you are ready.");return;
                case "firstNight":session.opening=false;session.block=GameRules.Blocks(session);session.location="bedroom";Explore();return;
                case "choices":ShowChoices();return;
                case "encounter":
                    if(!string.IsNullOrEmpty(session.pendingEnding)){StartEnding();return;}
                    session.girl="";session.scene="";session.portrait="";Explore();
                    if(session.block>=GameRules.Blocks(session))Toast("The school day is over. Head home and get some rest.");return;
                case "credits":session.mode="ended";Autosave();Credits(true);return;
            }
            if(after.StartsWith("observe."))
            {
                var girl=after.Substring(8);if(!session.observed.Contains(girl))session.observed.Add(girl);
                if(session.observed.Count==5){StartSequence("postTour","tourDone");return;}
            }
            session.girl="";session.portrait="";Explore();
        }
        public void Talk(string girl)
        {
            if(session.opening)
            {
                if(session.observed.Contains(girl)){Message("You've already noticed her today. There will be time to introduce yourself tomorrow.");return;}
                StartSequence("observe."+girl,"observe."+girl);return;
            }
            var c=Content.characters.First(x=>x.id==girl);
            if(!GameRules.Eligible(Content,session,girl))
            {
                string bark=session.used.Contains(girl)?c.used:c.busy;
                int colon=bark.IndexOf(':');if(colon>=0)bark=bark.Substring(colon+1).Trim();
                session.girl=girl;session.portrait="expr_"+girl+"_neutral";session.background="bg_"+session.location+"_day";
                StartLines(new[]{new Line{speaker=c.name,text=bark,kind="dialogue"}},"bark."+girl,"explore");return;
            }
            var scene=GameRules.Next(Content,session,girl);
            if(session.location!=scene.location)return;
            if(scene.number==15)Confirm("This is the final scene of "+Familiar(c.name)+"'s route. It ends this playthrough. A pre-finale save will be kept.",()=>BeginEncounter(girl));
            else BeginEncounter(girl);
        }
        public void BeginEncounter(string girl)
        {
            if(!GameRules.Eligible(Content,session,girl))return;
            var scene=GameRules.Next(Content,session,girl);if(session.location!=scene.location)return;
            if(scene.number==15&&!Save("pre-finale",false))return;
            session.girl=girl;session.scene=scene.id;session.background=scene.background;session.portrait=scene.portrait;
            var temperature=scene.temperature.FirstOrDefault(x=>x.id==GameRules.Temperature(session.Route(girl)));
            StartLines(scene.setup.Concat(temperature?.lines??Array.Empty<Line>()),scene.id+".setup","choices");
        }
        void ShowChoices()
        {
            session.mode="choices";resumeSkipAfterChoice=skip&&prefs.skipAfterChoices;auto=skip=false;DrawDialogueBase();
            var scene=CurrentScene;var order=Enumerable.Range(0,scene.choices.Length).OrderBy(i=>(i+scene.number)%3).ToArray();
            for(int j=0;j<order.Length;j++)
            {
                var choice=scene.choices[order[j]];
                var b=Btn(dialogue,PlayerText(choice.text),112,390+j*148,960,126,()=>Choose(choice.id));
                var label=b.GetComponentInChildren<TextMeshProUGUI>();label.fontSize=27;label.enableAutoSizing=true;label.fontSizeMin=24;label.fontSizeMax=27;
                label.rectTransform.anchoredPosition=new Vector2(32,-8);label.rectTransform.sizeDelta=new Vector2(896,110);
                ((Image)b.targetGraphic).sprite=catalog.Sprite("final_choice");
            }
            Autosave();
        }
        void DrawDialogueBase()
        {
            Clear(hud);Clear(dialogue);Background(session.background);
            DrawActor();DrawSchoolHud(true);
        }
        public void Choose(string id)
        {
            if(session.mode!="choices")return;
            var scene=CurrentScene;var choice=scene.choices.FirstOrDefault(x=>x.id==id);if(choice==null)return;
            try{GameRules.Commit(Content,session,scene,choice);}
            catch(InvalidOperationException ex){Message(ex.Message);return;}
            StartLines(choice.response.Concat(scene.closing),choice.id+".response","encounter");
            skip=resumeSkipAfterChoice;resumeSkipAfterChoice=false;RefreshReadingControls();
        }
        void StartEnding()
        {
            var ending=Content.endings.First(x=>x.id==session.pendingEnding);
            session.background=ending.cg;session.portrait="";session.endingUnlocked=true;
            if(!prefs.gallery.Contains(ending.id))prefs.gallery.Add(ending.id);
            PersistPreferences();
            IEnumerable<Line> lines=ending.lines;
            if(ending.kind=="good"&&session.lastChoice=="bad")lines=Seq("repair."+ending.girl).lines.Concat(lines);
            StartLines(lines,ending.id,"credits");
        }
        void Autosave(){Save("autosave",false);PersistPreferences();}
        bool Save(string slot,bool feedback=true)
        {
            if(session==null)return false;
            try{SaveStore.Write(slot,session);if(feedback){audioPlayer.Sfx("save");Toast("Saved.");}return true;}
            catch(Exception ex) when(ex is IOException||ex is UnauthorizedAccessException){Message("The save could not be written. Your current story is still open.\n"+ex.Message);return false;}
        }
        void PersistPreferences()
        {
            try{SaveStore.Write("preferences",prefs);}catch(Exception ex) when(ex is IOException||ex is UnauthorizedAccessException){Debug.LogWarning("Preferences could not be saved: "+ex.Message);}
        }
        void Load(string slot)
        {
            var loaded=SaveStore.Load(slot,Content);if(loaded==null){Message("This save is missing or damaged. Its backup could not be recovered.");return;}
            session=loaded;title=false;auto=skip=resumeSkipAfterChoice=false;hidden=false;dialogue.gameObject.SetActive(true);hud.gameObject.SetActive(true);CloseOverlay(false);RenderSession();
        }
        public void RenderSession()
        {
            title=false;
            if(session.mode=="dialogue")DrawDialogue();else if(session.mode=="choices")ShowChoices();else if(session.mode=="ended")Credits(true);else Explore();
        }
        void OnApplicationQuit(){if(!title&&session!=null)Save("autosave",false);PersistPreferences();}
#if UNITY_EDITOR
        public void TestFinishDialogue()
        {
            if(session.mode!="dialogue")throw new InvalidOperationException("Expected dialogue");
            session.lineIndex=session.lines.Length;FinishSegment();
        }
        public void TestCloseMenu()=>CloseOverlay(false);
        public void TestLoad(string slot)=>Load(slot);
        public bool TestSave(string slot)=>Save(slot,false);
        public void TestSettings()=>Settings();
        public void TestMap()=>Map();
        public void TestJournal()=>Journal();
        public void TestGallery()=>Gallery();
        public void TestTitle()=>ShowTitle();
#endif
    }
}
