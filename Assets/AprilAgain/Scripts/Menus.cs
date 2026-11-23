using System;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using static AprilAgain.NovelUI;

namespace AprilAgain
{
    public partial class AprilAgainGame
    {
        RectTransform OpenPanel(string heading,float w=1420,float h=900)
        {
            Clear(overlay);modal=true;overlayReturn=null;audioPlayer.Sfx("open");
            hud.gameObject.SetActive(false);dialogue.gameObject.SetActive(false);
            foreach(var target in world.GetComponentsInChildren<Button>(true))target.gameObject.SetActive(false);
            var shade=Image(overlay,"Modal shade",0,0,1920,1080,new Color(.12f,.08f,.15f,.62f));shade.raycastTarget=true;
            var p=Rect(heading,overlay,(1920-w)/2,(1080-h)/2,w,h);
            var plate=Image(p,"Paper",0,0,w,h,Color.white,catalog.Sprite("spring_menu"));plate.raycastTarget=true;
            // The illustrated frame includes a bow, a fold and transparent outer space.
            // Keep the header inside the paper, clear of that decorative perimeter.
            var panelHeading=Text(p,heading,220,104,w-560,60,catalog.titleFont,36,Rose);
            panelHeading.name="Panel heading";panelHeading.enableAutoSizing=true;panelHeading.fontSizeMin=30;panelHeading.fontSizeMax=36;
            Icon(p,"Close","close",w-220,100,64,DismissOverlay);
            return p;
        }
        void CloseOverlay(bool sound=true)
        {
            Clear(overlay);modal=false;overlayReturn=null;if(sound&&audioPlayer!=null)audioPlayer.Sfx("back");
            hud.gameObject.SetActive(!hidden);dialogue.gameObject.SetActive(!hidden);
            foreach(var target in world.GetComponentsInChildren<Button>(true))target.gameObject.SetActive(true);
            if(sound&&!title&&session!=null&&session.mode=="ended")ShowTitle();
        }
        void DismissOverlay()
        {
            var back=overlayReturn;overlayReturn=null;
            if(back!=null)back();else CloseOverlay();
        }
        void Confirm(string text,Action yes,Action cancelled=null)
        {
            var p=OpenPanel("April, again",1080,570);
            overlayReturn=cancelled;Text(p,text,160,220,760,150,Font,29);
            Btn(p,"Cancel",174,432,330,66,DismissOverlay);
            Btn(p,"Continue",552,432,354,66,()=>{CloseOverlay(false);yes();},true,true);
        }
        void Message(string text,Action returned=null)
        {
            var measure=Text(overlay,text,0,0,780,1,Font,29);
            float textHeight=Mathf.Ceil(measure.GetPreferredValues(text,780,10000).y);
            float height=Mathf.Max(580,220+textHeight+180);
            var p=OpenPanel("April, again",1100,height);overlayReturn=returned;Text(p,text,160,220,780,textHeight+2,Font,29);
            Btn(p,"Return",390,height-136,320,66,DismissOverlay);
        }
        void Toast(string text)
        {
            var panel=Image(overlay,"Notice",560,180,800,78,Color.white,catalog.Sprite("final_tooltip"));panel.raycastTarget=false;
            Text(panel.transform,text,24,12,752,54,Font,25,Ink,TextAlignmentOptions.Center);
            Destroy(panel.gameObject,5);
        }
        void Pause()
        {
            auto=skip=resumeSkipAfterChoice=false;RefreshReadingControls();
            var p=OpenPanel("Menu",1050,850);
            Btn(p,"Resume",180,224,690,66,()=>CloseOverlay(),true,true);
            Btn(p,"Save",180,314,330,64,()=>Saves(true));Btn(p,"Load",540,314,330,64,()=>Saves(false));
            Btn(p,"Settings",180,394,330,64,Settings);Btn(p,"History",540,394,330,64,History);
            Btn(p,"Journal",180,474,330,64,Journal);Btn(p,"Gallery",540,474,330,64,Gallery);
            Btn(p,"Quick save",180,554,330,64,()=>{if(Save("quick"))CloseOverlay();});
            Btn(p,"Quick load",540,554,330,64,()=>Confirm("Load the quick save?",()=>Load("quick")),SaveStore.Load("quick",Content)!=null);
            Btn(p,"Title screen",180,634,330,64,()=>Confirm("Return to the title? The current story will be autosaved.",()=>{Autosave();ShowTitle();}));
            Btn(p,"Quit",540,634,330,64,()=>Confirm("Save and close the game?",()=>{if(Save("autosave",false))Application.Quit();}));
            if(session.mode=="dialogue")Quiet(p,"Hide interface · H",340,738,370,48,HideInterface);
        }
        void Saves(bool saving,int page=0)
        {
            var p=OpenPanel(saving?"Save":"Load",1650,948);
            string[] special={"autosave","quick","pre-finale"};
            for(int i=0;i<6;i++)
            {
                string slot=page==2?special[i%3]:"slot"+(page*6+i+1);
                if(page==2&&i>=3)break;
                var saved=SaveStore.Load(slot,Content);
                float x=160+(i%3)*450,y=226+(i/3)*290;
                var tile=Btn(p,"",x,y,430,270,()=>{
                    if(saving){Action write=()=>{if(Save(slot)){Saves(true,page);Toast("Saved.");}};if(saved!=null)Confirm("Overwrite this save?",write,()=>Saves(true,page));else write();}
                    else Confirm("Load this save?",()=>Load(slot),()=>Saves(false,page));
                },saving?session!=null&&!title&&page<2:saved!=null);
                string label=page==2?(slot=="autosave"?"Auto":slot=="quick"?"Quick":"Before finale"):"Slot "+(page*6+i+1);
                if(saved!=null)Image(tile.transform,"Scene preview",75,14,280,158,Color.white,catalog.Sprite(saved.background),true);
                else Text(tile.transform,"Empty",24,62,382,70,Font,27,Muted,TextAlignmentOptions.Center);
                Text(tile.transform,label,24,182,382,36,catalog.titleFont,23,Rose);
                string place=saved==null?"":saved.location=="field"?"Sports field":saved.location=="corridor"?"Corridor":Content.locations.First(l=>l.id==saved.location).name;
                string info=saved==null?"":new DateTime(2026,4,6).AddDays(saved.day-1).ToString("ddd d MMM",System.Globalization.CultureInfo.InvariantCulture)+" · "+place;
                Text(tile.transform,info,24,220,382,38,Font,22,Muted);
            }
            for(int i=0;i<3;i++){int index=i;Btn(p,i==2?"Auto":""+(i+1),580+i*170,824,150,58,()=>Saves(saving,index),true,page==i);}
        }
        void History()
        {
            var p=OpenPanel("History",1580,948);
            var items=session?.history??new System.Collections.Generic.List<string>();
            if(items.Count==0){Text(p,"Your story hasn't begun yet.",160,224,1260,80,Font,32);return;}
            var content=Scroll(p,160,224,1260,600,items.Count*100);float y=0;
            foreach(var item in items)
            {
                var line=Text(content,item,16,y,1212,100,Font,29);
                float height=Mathf.Max(76,line.GetPreferredValues(item,1212,10000).y)+36;
                line.rectTransform.sizeDelta=new Vector2(1212,height-24);y+=height;
            }
            content.sizeDelta=new Vector2(content.sizeDelta.x,Mathf.Max(600,y));
            p.GetComponentInChildren<ScrollRect>().verticalNormalizedPosition=0;
        }
        void Journal()
        {
            var p=OpenPanel("Journal",1650,948);
            if(session==null){Text(p,"Start a new story to fill these pages.",160,224,1330,100,Font,32);return;}
            var content=Rect("Classmates",p,160,224,1330,570);
            for(int i=0;i<Content.characters.Length;i++)
            {
                var c=Content.characters[i];var r=session.Route(c.id);float y=i*112;
                CenterArtwork(Image(content,c.name,12,y+4,96,96,Color.white,catalog.Sprite("expr_"+c.id+"_neutral"),true));
                Text(content,Familiar(c.name),150,y+3,860,42,catalog.titleFont,29,Rose);
                Text(content,session.opening?(session.observed.Contains(c.id)?"Seen at orientation":"Someone to notice"):Appointment(c.id),150,y+55,1040,44,Font,25,Muted);
                Text(content,(r.next-1)+" / 15",1150,y+8,160,40,Font,25,Ink,TextAlignmentOptions.Right);
                Image(content,"Page rule",150,y+110,1160,1,new Color(.8f,.5f,.6f,.22f));
            }
            Quiet(p,"How days work",180,828,260,56,()=>Message("Travel and looking around are free. Each encounter takes one 3-hour block, with one encounter per classmate per day.\n\nThe fifteenth encounter ends that route and the playthrough. Saturday has an extra activity block.",Journal));
            bool allClub=session.mode=="explore"&&!session.opening&&Content.characters.All(c=>GameRules.Next(Content,session,c.id)?.club??false);
            if(allClub)Btn(p,"Skip to Saturday",1160,824,400,64,()=>Confirm("Finish the intervening school days and wait for Saturday? No relationship scores will change.",()=>{do{GameRules.AdvanceDay(session);}while(!GameRules.Saturday(session));session.location="gate";CloseOverlay(false);Explore();}));
        }
        void Gallery()
        {
            var p=OpenPanel("Memories",1740,948);
            var content=Scroll(p,160,224,1420,596,1360);
            for(int i=0;i<Content.endings.Length;i++)
            {
                var ending=Content.endings[i];bool unlocked=prefs.gallery.Contains(ending.id);float x=(i%3)*468,y=(i/3)*266;
                var b=Btn(content,"",x,y,438,242,()=>ViewCG(ending),unlocked);
                if(unlocked)Image(b.transform,"Memory",77,12,284,160,Color.white,catalog.Sprite(ending.cg),true);
                else Image(b.transform,"Unseen memory",178,65,80,80,Muted,catalog.Sprite("spring_icon_lock"),true);
                Text(b.transform,unlocked?ending.title:"Unseen",18,172,402,64,Font,22,Rose,TextAlignmentOptions.Center);
            }
        }
        void ViewCG(EndingData ending)
        {
            Clear(overlay);modal=true;overlayReturn=Gallery;
            Image(overlay,"Memory",0,0,1920,1080,Color.white,catalog.Sprite(ending.cg),true).raycastTarget=true;
            Icon(overlay,"Back to gallery","back",40,32,76,Gallery,Paper);
            Icon(overlay,"Close","close",1800,32,76,DismissOverlay,Paper);
        }
        int settingsTab;
        void Settings()=>SettingsPage(settingsTab);
        void SettingsPage(int page)
        {
            settingsTab=page;
            var p=OpenPanel("Settings",1640,954);
            for(int i=0;i<3;i++){int index=i;Btn(p,new[]{"Reading","Sound","Display"}[i],160+i*430,224,400,58,()=>SettingsPage(index),true,page==i);}
            void SliderRow(string label,float x,float y,float value,float min,float max,Action<float> changed,string format)
            {
                Text(p,label,x,y,400,40,Font,25);
                var number=Text(p,value.ToString(format),x+400,y,120,40,Font,25,Rose,TextAlignmentOptions.Right);
                var r=Rect(label+" slider",p,x,y+44,520,40);var hit=r.gameObject.AddComponent<Image>();hit.color=new Color(1,1,1,0);hit.raycastTarget=true;var slider=r.gameObject.AddComponent<Slider>();
                var bg=Image(r,"Track",0,17,520,6,Hex("EBD5DD"));
                var fillArea=Rect("Fill area",r,14,17,492,6);var fill=Image(fillArea,"Fill",0,0,492,6,Rose);
                fill.rectTransform.anchorMin=Vector2.zero;fill.rectTransform.anchorMax=Vector2.one;fill.rectTransform.offsetMin=new Vector2(-14,0);fill.rectTransform.offsetMax=Vector2.zero;
                var handleArea=Rect("Handle area",r,14,0,492,40);var handle=Image(handleArea,"Handle",0,0,28,28,Rose,catalog.Sprite("spring_slider_knob"),true);handle.raycastTarget=true;
                handle.rectTransform.pivot=new Vector2(.5f,.5f);handle.rectTransform.sizeDelta=new Vector2(28,-12);handle.rectTransform.anchoredPosition=Vector2.zero;
                slider.fillRect=fill.rectTransform;slider.handleRect=handle.rectTransform;slider.targetGraphic=handle;slider.minValue=min;slider.maxValue=max;slider.value=value;
                slider.onValueChanged.AddListener(v=>{number.text=v.ToString(format);changed(v);audioPlayer.Apply();});
            }
            void Toggle(string label,bool value,float x,float y,Action change)=>Btn(p,label+"  "+(value?"On":"Off"),x,y,580,66,()=>{change();PersistPreferences();Settings();});
            if(page==0)
            {
                SliderRow("Text speed",160,354,prefs.textSpeed,15,100,v=>prefs.textSpeed=v,"0");
                SliderRow("Auto pause",160,504,prefs.autoDelay,1,6,v=>prefs.autoDelay=v,"0.0 's'");
                Toggle("Instant text",prefs.instantText,160,654,()=>prefs.instantText=!prefs.instantText);
                Toggle("Skip unread text",prefs.skipUnread,900,354,()=>prefs.skipUnread=!prefs.skipUnread);
                Toggle("Resume skip after choices",prefs.skipAfterChoices,900,454,()=>prefs.skipAfterChoices=!prefs.skipAfterChoices);
                Toggle("Keep auto after a click",prefs.autoAfterClick,900,554,()=>prefs.autoAfterClick=!prefs.autoAfterClick);
                Text(p,"Skip always waits for your choice.",916,660,540,80,Font,25,Muted);
            }
            else if(page==1)
            {
                SliderRow("Master",160,354,prefs.master,0,1,v=>prefs.master=v,"P0");
                SliderRow("Music",160,504,prefs.music,0,1,v=>prefs.music=v,"P0");
                SliderRow("Sound effects",900,354,prefs.sound,0,1,v=>prefs.sound=v,"P0");
                SliderRow("Ambience",900,504,prefs.ambience,0,1,v=>prefs.ambience=v,"P0");
                Toggle("Mute outside game",prefs.muteUnfocused,160,654,()=>prefs.muteUnfocused=!prefs.muteUnfocused);
            }
            else
            {
                Btn(p,prefs.fullscreen?"Borderless fullscreen":"Windowed",160,354,580,66,()=>{prefs.fullscreen=!prefs.fullscreen;ApplyDisplay();PersistPreferences();Settings();});
                Text(p,prefs.fullscreen?"Uses your display's native resolution.":"Choose the window size below.",176,438,540,78,Font,25,Muted);
                Btn(p,"Window size  "+new[]{"1280 × 720","1600 × 900","1920 × 1080"}[Mathf.Clamp(prefs.windowSize,0,2)],160,544,580,66,()=>{prefs.windowSize=(prefs.windowSize+1)%3;ApplyDisplay();PersistPreferences();Settings();},!prefs.fullscreen);
                Toggle("Reduced motion",prefs.reducedMotion,900,354,()=>prefs.reducedMotion=!prefs.reducedMotion);
                Toggle("VSync",prefs.vsync,900,454,()=>{prefs.vsync=!prefs.vsync;ApplyDisplay();});
            }
            Quiet(p,"Controls",170,830,230,60,()=>Message("Click anywhere in the scene or press Space to reveal and advance dialogue. Escape opens the menu. H hides the interface.\n\nAuto reads at your pace. Skip follows your Reading settings and always waits at choices.\n\nF5: quick save. F9: quick load.",Settings));
            Btn(p,"Done",1110,830,310,64,()=>{PersistPreferences();CloseOverlay();},true,true);
        }
        void Credits(bool ending)
        {
            var p=OpenPanel(ending?Content.endings.First(x=>x.id==session.pendingEnding).title:"April, again",1420,920);
            Text(p,"Thank you for spending these days at Seiran.",150,224,1120,90,catalog.titleFont,32,Rose,TextAlignmentOptions.Center);
            Text(p,"Door and interface sounds: Kenney (CC0)\nRain recording: alxl (CC0)\nOriginal music made for April, again\n\nNunito — SIL Open Font License",190,340,1040,364,Font,27,Ink,TextAlignmentOptions.Center);
            Btn(p,ending?"Return to title":"Return",470,784,480,72,()=>{if(ending){Autosave();ShowTitle();}else CloseOverlay();},true,true);
        }
    }
}
