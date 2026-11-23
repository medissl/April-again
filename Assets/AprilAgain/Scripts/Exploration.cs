using System;
using System.Linq;
using TMPro;
using UnityEngine;
using static AprilAgain.NovelUI;

namespace AprilAgain
{
    public partial class AprilAgainGame
    {
#if UNITY_EDITOR
        string reviewBackground,reviewGirl;
        public void TestWorldArtwork(string asset,string location,string girl)
        {
            session=Session.New(Content);session.opening=false;session.day=3;session.location=location;
            reviewBackground=asset;reviewGirl=girl;Explore();reviewBackground=reviewGirl=null;
        }
#endif
        public void Explore()
        {
            session.mode="explore";session.lines=session.lines??Array.Empty<Line>();title=false;auto=skip=false;body=null;
            Clear(hud);Clear(dialogue);CloseOverlay(false);
            var loc=Content.locations.First(x=>x.id==session.location);
            var present=Content.characters.Where(c=>session.location!="bedroom"&&GameRules.Place(Content,session,c.id)==session.location).ToArray();
#if UNITY_EDITOR
            if(reviewBackground!=null)present=Content.characters.Where(c=>c.id==reviewGirl).ToArray();
#endif
            string background="bg_"+session.location+"_day";
            SceneData scene=null;string primary="";
            if(present.Length>0)
            {
                var person=present.OrderByDescending(c=>GameRules.Eligible(Content,session,c.id)).ThenBy(c=>session.observed.Contains(c.id)).First();primary=person.id;
                scene=GameRules.Next(Content,session,primary);
                if(session.opening)background=Seq("observe."+primary).background;
                else if(GameRules.Eligible(Content,session,primary))background=scene.room;
                else if(catalog.Sprite("room_"+primary+"_"+session.location+"_school_uniform")!=null)background="room_"+primary+"_"+session.location+"_school_uniform";
                else primary="";
            }
            if(session.location=="bedroom"&&(session.day==1||GameRules.Block(session)=="evening"||GameRules.Sunday(session)))background="bg_bedroom_evening";
#if UNITY_EDITOR
            if(reviewBackground!=null){background=reviewBackground;primary=reviewGirl??"";}
#endif
            Background(background);session.background=background;
            audioPlayer.Music(session.location=="bedroom"?"bgm_reflection":"bgm_daily");audioPlayer.Ambience(background.Contains("rain")?"rain_window":"");
            var personAreas=new System.Collections.Generic.List<Rect>();
            var secondaryRects=new System.Collections.Generic.Dictionary<string,Rect>();
            var primaryBounds=primary!=""?Content.assets.First(a=>a.id==background).rect:null;
            float primaryCenter=primaryBounds==null?960:(primaryBounds[0]+primaryBounds[2]/2)*1920;
            int secondaryIndex=0;
            for(int i=0;i<present.Length;i++)
            {
                if(present[i].id==primary){var q=Content.assets.First(a=>a.id==background).rect;personAreas.Add(new Rect(q[0]*1920,q[1]*1080,q[2]*1920,q[3]*1080));}
                else
                {
                    // Stand in the opposite foreground aisle, with feet on the floor.
                    // The prior index-based placement stacked people over the baked-in girl.
                    float px=primaryCenter>=960?80+secondaryIndex*600:1170-secondaryIndex*600;
                    var placement=new Rect(px,240,600,800);secondaryRects[present[i].id]=placement;
                    personAreas.Add(new Rect(px+90,260,420,770));secondaryIndex++;
                }
            }
            foreach(var exit in loc.exits??Array.Empty<ExitData>())
            {
                var r=exit.rect;var center=new Vector2((r[0]+r[2]/2)*1920,(r[1]+r[3]/2)*1080);
                DoorTarget(world,PlaceName(exit.destination),r[0]*1920,r[1]*1080,r[2]*1920,r[3]*1080,Font,()=>Travel(exit.destination,true),()=>audioPlayer.Sfx("hover"),!personAreas.Any(a=>a.Contains(center)));
            }
            for(int i=0;i<present.Length;i++)
            {
                var c=present[i];string label=Familiar(c.name)+(session.opening?(session.observed.Contains(c.id)?" • Seen":" • Observe"):GameRules.Eligible(Content,session,c.id)?" • Talk · 3h":" • Busy");
                if(c.id==primary)
                {
                    var asset=Content.assets.FirstOrDefault(x=>x.id==background);var r=asset?.rect??new[]{.14f,.2f,.22f,.7f};
                    Hotspot(world,label,r[0]*1920,r[1]*1080,r[2]*1920,r[3]*1080,Font,()=>Talk(c.id),()=>audioPlayer.Sfx("hover"));
                }
                else
                {
                    var placement=secondaryRects[c.id];
                    string pose=Content.assets.First(a=>a.id.StartsWith("pose_"+c.id+"_standing")).id;
                    Image(world,c.name,placement.x,placement.y,placement.width,placement.height,Color.white,catalog.Sprite(pose),true);
                    Hotspot(world,label,placement.x+90,260,420,770,Font,()=>Talk(c.id),()=>audioPlayer.Sfx("hover"));
                }
            }
            DrawSchoolHud();
            if(session.location=="bedroom")
            {
                Btn(hud,"Sleep • next day",1430,942,390,70,Sleep,!session.opening,true);
                Hotspot(world,"Desk",1344,562,538,389,Font,()=>Message("My admission letter sits under the folded campus map. Getting in felt impossible last month. Tomorrow, I only have to show up."),()=>audioPlayer.Sfx("hover"));
            }
            else
            {
                if(!session.opening&&session.block<GameRules.Blocks(session))Icon(hud,"Wait • 3 hours","wait",1780,944,72,Wait,Paper);
                if((session.opening&&session.observed.Count==5)||!session.opening&&session.block>=GameRules.Blocks(session))Icon(hud,"Home","home",1780,944,72,GoHome,Paper);
            }
            if(primary!="")
            {
                var nearby=session.opening?Seq("observe."+primary).props:GameRules.Eligible(Content,session,primary)?scene.props:Array.Empty<PropData>();
                if(nearby!=null&&nearby.Length>0)Icon(hud,"Look closer","inspect",1780,824,64,()=>RoomObjects(nearby),Paper);
            }
            Autosave();
        }
        string PlaceName(string id)=>id=="field"?"Sports field":id=="bedroom"?"My room":id=="gate"?"School gate":Content.locations.First(l=>l.id==id).name;
        void DrawSchoolHud(bool reading=false)
        {
            Image(hud,"Calendar ticket",24,24,440,194,Color.white,catalog.Sprite("spring_calendar"));
            var date=new DateTime(2026,4,6).AddDays(session.day-1);
            var culture=System.Globalization.CultureInfo.InvariantCulture;
            Text(hud,date.ToString("dd MMMM",culture),44,34,310,44,catalog.titleFont,32,Ink);
            string time=GameRules.Block(session)=="evening"?"Evening":GameRules.Block(session)=="morning"?"9–12":GameRules.Block(session)=="midday"?"12–15":"15–18";
            Text(hud,date.ToString("dddd",culture),44,82,310,36,catalog.titleFont,26,Ink);
            Text(hud,PlaceName(session.location),44,134,310,38,Font,24,Ink);
            var calendar=Image(hud,"Day details",24,24,440,194,new Color(1,1,1,0));calendar.raycastTarget=true;
            var button=calendar.gameObject.AddComponent<UnityEngine.UI.Button>();button.transition=UnityEngine.UI.Selectable.Transition.None;button.onClick.AddListener(Journal);
            var tip=Image(calendar.transform,"Time",20,202,400,54,Color.white,catalog.Sprite("final_tooltip"));tip.gameObject.SetActive(false);
            Text(tip.transform,session.opening?"Orientation · "+session.observed.Count+" / 5":time+" · encounters take 3h",20,12,360,36,Font,22,Ink,TextAlignmentOptions.Center);
            calendar.gameObject.AddComponent<SoftHighlight>().change=on=>tip.gameObject.SetActive(on);
            Icon(hud,"Map","map",1650,16,72,Map,Paper);Icon(hud,"Journal","journal",1744,16,72,Journal,Paper);Icon(hud,"Menu","menu",1836,16,72,Pause,Paper);
        }
        public void Travel(string location,bool throughDoor=false)
        {
            if(session.mode!="explore")return;
            if(location=="bedroom"){GoHome();return;}
            if(session.location=="bedroom"&&!session.opening&&(GameRules.Block(session)=="evening"||GameRules.Sunday(session))){Message("School has finished for today. Sleep when you're ready for tomorrow.");return;}
            if(!Content.locations.Any(x=>x.id==location))return;
            bool interior=location.StartsWith("class_")||session.location.StartsWith("class_")||location=="library"||location=="infirmary"||session.location=="library"||session.location=="infirmary";
            if(throughDoor&&interior)audioPlayer.Sfx("room_door",.25f);
            session.location=location;Explore();
        }
        void GoHome()
        {
            if(session.opening&&session.observed.Count<5){Message("There are still a few classmates to notice before I leave.");return;}
            if(session.location=="bedroom")return;
            if(session.opening){StartSequence("firstNight","firstNight");return;}
            Action finish=()=>{
                bool full=session.block>=GameRules.Blocks(session);session.location="bedroom";session.block=GameRules.Blocks(session);
                StartSequence("home."+(full?"full":"early"),"explore");
            };
            if(session.block>=GameRules.Blocks(session))finish();
            else Confirm("Head home early? Any unused activity blocks will be left behind today.",finish);
        }
        void Wait()
        {
            session.block++;Explore();
        }
        void Sleep()
        {
            GameRules.AdvanceDay(session);
            if(GameRules.Sunday(session)){session.block=0;StartSequence("home.sunday","explore");}
            else StartSequence("morning."+(session.day%4),"morningDone");
        }
        string Appointment(string girl)
        {
            var copy=session.Clone();
            for(int d=0;d<15;d++)
            {
                for(int b=copy.block;b<GameRules.Blocks(copy);b++)
                {
                    copy.block=b;if(GameRules.Eligible(Content,copy,girl))
                    {
                        var next=GameRules.Next(Content,copy,girl);var place=Content.locations.First(x=>x.id==next.location).name;
                        string day=d==0?"Today":d==1?"Tomorrow":new DateTime(2026,4,6).AddDays(copy.day-1).ToString("ddd d MMM",System.Globalization.CultureInfo.InvariantCulture);
                        return day+" • "+GameRules.Block(copy)+" • "+place;
                    }
                }
                GameRules.AdvanceDay(copy);
            }
            return "Route complete";
        }
        void RoomObjects(PropData[] props)
        {
            var p=OpenPanel("Nearby",1240,880);
            var content=Scroll(p,150,180,960,540,Mathf.Ceil(props.Length/3f)*250);
            for(int i=0;i<props.Length;i++)
            {
                var prop=props[i];float x=(i%3)*312,y=(i/3)*250;
                var b=Quiet(content,prop.label,x,y,290,232,()=>Inspect(prop,()=>RoomObjects(props)));
                b.GetComponentInChildren<TextMeshProUGUI>().gameObject.SetActive(false);
                Image(b.transform,prop.label,30,0,230,180,Color.white,catalog.Sprite(prop.asset),true);
                Text(b.transform,prop.label,12,190,266,42,Font,23,Ink,TextAlignmentOptions.Center);
            }
            Btn(p,"Return",450,758,340,64,()=>CloseOverlay());
        }
        void Inspect(PropData prop,Action returned=null)
        {
            var p=OpenPanel(prop.label,980,810);
            overlayReturn=returned;
            Image(p,"Item",230,130,520,430,Color.white,catalog.Sprite(prop.asset),true);
            string text=prop.id.Contains("journal")?"Her notebook. I'll leave it closed unless she wants to share something.":prop.id.Contains("camera")?"A well-kept camera. I'd rather ask her about it than touch it.":prop.id=="bento"?"A tidy lunchbox. There's a spare pair of chopsticks beside it.":prop.id=="thermos"?"The tea flask is still warm.":prop.id=="folder"?"The corners are already a little bent. It's been a busy first week.":"";
            if(text!="")Text(p,text,130,590,720,100,Font,27);
            Btn(p,"Return",330,718,320,60,DismissOverlay);
        }
        void Map()
        {
            var p=OpenPanel("Campus",1792,996);
            const float mapX=192,mapY=154,mapW=1408,mapH=792;
            Image(p,"Campus",mapX,mapY,mapW,mapH,Color.white,catalog.Sprite("map_campus"),true);
            foreach(var loc in Content.locations.Where(x=>x.id!="bedroom"))
            {
                var r=loc.rect;float x=mapX+r[0]*mapW,y=mapY+r[1]*mapH,w=r[2]*mapW,h=r[3]*mapH;
                var occupants=Content.characters.Where(c=>GameRules.Place(Content,session,c.id)==loc.id).ToArray();
                string name=loc.id=="field"?"Sports field":loc.id=="corridor"?"Corridor":loc.id=="gate"?"Gate":loc.name;
                float labelWidth=loc.id=="corridor"?170:Mathf.Clamp(w-20,142,218);
                float labelX=x+(w-labelWidth)/2,labelY=y+Mathf.Min(h*.1f,24);
                var regions=new System.Collections.Generic.List<Rect>{new Rect(x,y,w,h)};
                if(loc.id=="corridor")regions.Add(new Rect(mapX+.465f*mapW,mapY+.38f*mapH,.07f*mapW,.173f*mapH));
                for(int i=0;i<occupants.Length;i++)regions.Add(new Rect(labelX+labelWidth/2-27+(i-(occupants.Length-1)/2f)*58,labelY+52,54,54));
                var destination=MapTarget(p,"Map room "+loc.id,regions.ToArray(),()=>{if(session.mode=="explore"){audioPlayer.Sfx("select");CloseOverlay(false);Travel(loc.id);}});
                destination.interactable=session.mode=="explore";
                var roomLabel=Image(p,"Map label",labelX,labelY,labelWidth,48,Color.white,catalog.Sprite(session.location==loc.id?"final_map_current":"final_map_label"));
                var focus=roomLabel.gameObject.AddComponent<UnityEngine.UI.Outline>();focus.effectColor=Rose;focus.effectDistance=new Vector2(2,-2);focus.enabled=false;
                destination.gameObject.AddComponent<SoftHighlight>().change=on=>{focus.enabled=on&&destination.interactable;if(on&&destination.interactable)audioPlayer.Sfx("hover");};
                Text(p,name,labelX+8,labelY+6,labelWidth-16,38,Font,22,Ink,TextAlignmentOptions.Center);
                for(int i=0;i<occupants.Length;i++)
                {
                    var person=occupants[i];float px=labelX+labelWidth/2-27+(i-(occupants.Length-1)/2f)*58;
                    Image(p,"Portrait",px,labelY+52,54,54,Color.white,catalog.Sprite("expr_"+person.id+"_neutral"),true);
                    if(GameRules.Eligible(Content,session,person.id))Image(p,"Free now",px+13,labelY+105,28,3,Rose);
                }
            }
            Icon(p,"Map help","info",1550,42,64,()=>Message("Select a room to visit it. Travel is free.\n\nPortraits show where classmates are now. A rose mark means a story encounter is available. Check the journal for their next appointment.",Map));
            if(session.mode=="explore"&&(!session.opening||session.observed.Count==5))Icon(p,"Home","home",1640,840,72,()=>{CloseOverlay(false);GoHome();});
        }
    }
}
