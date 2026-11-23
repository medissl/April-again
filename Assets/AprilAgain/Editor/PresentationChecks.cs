using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using TMPro;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.UI;

namespace AprilAgain.Editor
{
    public static class PresentationChecks
    {
        static AprilAgainGame Game=>UnityEngine.Object.FindAnyObjectByType<AprilAgainGame>();
        const string Output="Documentation/Testing/Production";
        static readonly BindingFlags Private=BindingFlags.Instance|BindingFlags.NonPublic;
        static void Invoke(string method,params object[] args)=>typeof(AprilAgainGame).GetMethod(method,Private).Invoke(Game,args);
        static int checks;
        static readonly List<string> Issues=new List<string>();
        static void Check(bool value,string message){checks++;if(!value)Issues.Add(message);}

        public static string Capture(string name,int width=1920,int height=1080)
        {
            Directory.CreateDirectory(Output);
            var camera=Camera.main;var previous=camera.targetTexture;var active=RenderTexture.active;
            var target=RenderTexture.GetTemporary(width,height,24,RenderTextureFormat.ARGB32,RenderTextureReadWrite.sRGB);
            Texture2D image=null;
            try
            {
                foreach(var text in UnityEngine.Object.FindObjectsByType<TextMeshProUGUI>(FindObjectsSortMode.None))text.maxVisibleCharacters=int.MaxValue;
                camera.targetTexture=target;Canvas.ForceUpdateCanvases();
                if(GraphicsSettings.currentRenderPipeline!=null)
                    RenderPipeline.SubmitRenderRequest(camera,new UniversalRenderPipeline.SingleCameraRequest{destination=target});
                else camera.Render();
                RenderTexture.active=target;image=new Texture2D(width,height,TextureFormat.RGB24,false);
                image.ReadPixels(new Rect(0,0,width,height),0,0);image.Apply();
                string path=Output+"/"+name+"-"+height+".jpg";File.WriteAllBytes(path,image.EncodeToJPG(88));return path;
            }
            finally
            {
                camera.targetTexture=previous;RenderTexture.active=active;
                if(image!=null)UnityEngine.Object.DestroyImmediate(image);RenderTexture.ReleaseTemporary(target);
            }
        }
        static void CheckText(string screen)
        {
            Canvas.ForceUpdateCanvases();
            foreach(var t in UnityEngine.Object.FindObjectsByType<TextMeshProUGUI>(FindObjectsSortMode.None).Where(t=>t.gameObject.activeInHierarchy&&!string.IsNullOrWhiteSpace(t.text)))
            {
                t.ForceMeshUpdate();var box=t.rectTransform.rect;
                var preferred=t.GetPreferredValues(t.text,box.width,10000);
                Check(t.font==Game.catalog.bodyFont,screen+": mixed font: "+t.text);
                Check(preferred.y<=box.height+2,screen+": text height "+preferred.y+" > "+box.height+": "+t.text);
            }
        }
        static void SaveScreen(string name)
        {
            CheckText(name);Capture(name);Capture(name,1280,720);
        }
        static void Hover(GameObject target,bool enter)
        {
            var pointer=new PointerEventData(EventSystem.current);
            foreach(var h in target.GetComponents<SoftHighlight>())
            {if(enter)h.OnPointerEnter(pointer);else h.OnPointerExit(pointer);}
        }
        static void CheckDoors(string screen)
        {
            foreach(var b in UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).Where(b=>b.gameObject.activeInHierarchy&&b.name.StartsWith("Door ")))
            {
                Check(b.GetComponentsInChildren<Button>(true).Length==1,screen+": nested door buttons");
                Check(b.GetComponent<Image>().color.a==0,screen+": opaque door hit region");
                Hover(b.gameObject,true);
                Check(b.transform.Find("Destination").gameObject.activeSelf,screen+": missing destination label");
                Check(!b.transform.Find("Door marker").gameObject.activeSelf,screen+": arrow duplicates destination label");
                CheckText(screen+" hover "+b.name);
                Capture(screen+"-hover-"+b.name.Replace(' ','_'),1280,720);Hover(b.gameObject,false);
            }
        }
        public static string StartVisualReview()
        {
            checks=0;Issues.Clear();Directory.CreateDirectory(Output);
            Game.StartCoroutine(VisualReview());return "Visual review started";
        }
        static IEnumerator VisualReview()
        {
            var g=Game;g.TestTitle();yield return null;SaveScreen("title");
            foreach(var screen in new[]{"Settings","Gallery"})
            {
                Invoke(screen);yield return null;SaveScreen(screen.ToLower());
                Check(!GameObject.Find("HUD")?.activeSelf??true,screen+": background HUD remains visible");
                if(screen=="Settings")
                foreach(var slider in UnityEngine.Object.FindObjectsByType<Slider>(FindObjectsSortMode.None))
                {
                    var corners=new Vector3[4];slider.fillRect.GetWorldCorners(corners);float left=corners[0].x;
                    var track=slider.transform.Find("Track").GetComponent<RectTransform>();track.GetWorldCorners(corners);
                    Check(Mathf.Abs(left-corners[0].x)<.6f,"Slider fill starts after track: "+slider.name);
                }
                g.TestCloseMenu();yield return null;
            }
            var art=g.Content.assets.Where(a=>a.id.StartsWith("bg_")||a.id.StartsWith("room_")||a.id.StartsWith("observation_")).ToArray();
            foreach(var a in art)
            {
                string girl="",location="";
                var sequence=g.Content.sequences.FirstOrDefault(s=>s.background==a.id);
                if(a.id.StartsWith("observation_")){girl=sequence.girl;location=sequence.location;}
                else if(a.id.StartsWith("room_"))
                {
                    girl=g.Content.characters.First(c=>a.id.StartsWith("room_"+c.id+"_")).id;
                    string suffix=a.id.Substring(("room_"+girl+"_").Length);
                    location=g.Content.locations.OrderByDescending(l=>l.id.Length).First(l=>suffix.StartsWith(l.id+"_")).id;
                }
                else location=g.Content.locations.OrderByDescending(l=>l.id.Length).First(l=>a.id.StartsWith("bg_"+l.id+"_")).id;
                g.TestWorldArtwork(a.id,location,girl);yield return null;
                SaveScreen(a.id);CheckDoors(a.id);yield return null;
            }
            g.TestWorldArtwork("bg_corridor_day","corridor","");g.TestMap();yield return null;SaveScreen("map");
            var targets=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).Where(b=>b.gameObject.activeInHierarchy&&b.name.StartsWith("Map room ")).ToArray();
            Check(targets.Length==g.Content.locations.Length-1,"Map has duplicate/missing room controls");
            foreach(var b in targets)
            {
                Check(b.GetComponent<MapHitRegion>()!=null,"Map room missing shaped hit region");
                Hover(b.gameObject,true);Check(b.GetComponentsInChildren<TextMeshProUGUI>(true).Length==0,"Map creates duplicate room captions");
                Capture("map-hover-"+b.name.Replace(' ','_'),1280,720);Hover(b.gameObject,false);
            }
            g.TestCloseMenu();g.TestJournal();yield return null;SaveScreen("journal");
            g.TestCloseMenu();Invoke("Saves",true,0);yield return null;SaveScreen("save");
            Invoke("Saves",false,2);yield return null;SaveScreen("load-auto");
            g.TestCloseMenu();Invoke("Pause");yield return null;SaveScreen("pause");
            Invoke("Confirm","Return to the title screen?",(Action)(()=>g.TestTitle()),null);yield return null;SaveScreen("confirmation");
            g.TestCloseMenu();Invoke("History");yield return null;SaveScreen("history");
            g.TestCloseMenu();var prop=g.Content.scenes.SelectMany(s=>s.props).First();Invoke("Inspect",prop,null);yield return null;SaveScreen("inspection");
            g.TestCloseMenu();Invoke("RoomObjects",new object[]{g.Content.scenes.OrderByDescending(s=>s.props.Length).First().props});yield return null;SaveScreen("nearby");
            g.TestCloseMenu();
            File.WriteAllLines(Output+"/visual-issues.txt",Issues);
            File.WriteAllText(Output+"/visual-status.txt","Completed "+checks+" checks; "+Issues.Count+" layout issues.");
            g.TestTitle();
        }
        public static string StartPlaythroughs()
        {
            Directory.CreateDirectory(Output);Game.StartCoroutine(Playthroughs());return "Full controller playthroughs started";
        }
        public static string PopulatedHistory()
        {
            Game.State.history=Game.Content.scenes.SelectMany(s=>s.setup).Take(100).Select(l=>l.speaker+": "+l.text).ToList();
            Invoke("History");SaveScreen("history-populated-bottom");
            UnityEngine.Object.FindAnyObjectByType<ScrollRect>().verticalNormalizedPosition=1;
            SaveScreen("history-populated-top");Game.TestCloseMenu();
            File.WriteAllLines(Output+"/history-issues.txt",Issues);
            return "Checked populated scroll history, "+Issues.Count+" layout issues";
        }
        public static string StartCrowdReview(){Game.StartCoroutine(CrowdReview());return "Crowded room review started";}
        static IEnumerator CrowdReview()
        {
            var g=Game;g.NewGame();var state=g.State;state.opening=false;var captured=new HashSet<string>();
            for(int day=2;day<29;day++)
            {
                state.day=day;
                for(int block=0;block<GameRules.Blocks(state);block++)
                {
                    state.block=block;
                    var groups=g.Content.characters.GroupBy(c=>GameRules.Place(g.Content,state,c.id)).Where(group=>group.Count()>1).ToArray();
                    foreach(var group in groups)
                    {
                        state.location=group.Key;g.Explore();yield return null;
                        string key=state.background+"-"+string.Join("-",group.Select(c=>c.id));if(!captured.Add(key))continue;
                        var people=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).Where(b=>b.gameObject.activeInHierarchy&&b.name.StartsWith("Inspect ")&&b.name.Contains(" • ")).ToArray();
                        Check(people.Length==group.Count(),key+": missing classmate target");
                        for(int i=0;i<people.Length;i++)for(int j=i+1;j<people.Length;j++)
                        {
                            var a=(RectTransform)people[i].transform;var b=(RectTransform)people[j].transform;
                            var ar=new Rect(a.anchoredPosition.x,-a.anchoredPosition.y,a.rect.width,a.rect.height);
                            var br=new Rect(b.anchoredPosition.x,-b.anchoredPosition.y,b.rect.width,b.rect.height);
                            Check(!ar.Overlaps(br),key+": overlapping classmate targets");
                        }
                        SaveScreen("crowd-"+key);
                    }
                }
            }
            File.WriteAllLines(Output+"/crowd-issues.txt",Issues);File.WriteAllText(Output+"/crowd-status.txt",captured.Count+" crowded room arrangements checked; "+Issues.Count+" issues.");g.TestTitle();
        }
        static IEnumerator Playthroughs()
        {
            var g=Game;int encounters=0,completed=0;
            foreach(var character in g.Content.characters)
            foreach(string outcome in new[]{"good","neutral","bad"})
            {
                g.NewGame();g.TestFinishDialogue();g.TestFinishDialogue();g.TestFinishDialogue();
                var state=g.State;state.opening=false;state.day=2;state.mode="explore";
                for(int number=1;number<=15;number++)
                {
                    int guard=0;while(!GameRules.Eligible(g.Content,state,character.id))
                    {if(state.block<GameRules.Blocks(state))state.block++;else GameRules.AdvanceDay(state);if(++guard>300)throw new Exception("Unreachable encounter");}
                    var scene=GameRules.Next(g.Content,state,character.id);state.location=scene.location;g.Explore();g.BeginEncounter(character.id);
                    yield return null;
                    if(outcome=="good")SaveScreen(scene.id+"-dialogue");
                    g.TestFinishDialogue();
                    if(outcome=="good")SaveScreen(scene.id+"-choices");
                    var choice=scene.choices.First(c=>c.kind==outcome);
                    var button=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).First(b=>b.gameObject.activeInHierarchy&&b.GetComponentsInChildren<TextMeshProUGUI>().Any(t=>t.text==choice.text));
                    button.onClick.Invoke();if(state.choices.Count!=number)throw new Exception("Choice count mismatch");
                    g.TestFinishDialogue();encounters++;yield return null;
                    if(number==15)
                    {
                        string ending=character.id+".ending."+outcome;
                        if(state.pendingEnding!=ending||state.background!="cg_"+character.id+"_"+outcome)throw new Exception("Ending mismatch");
                        SaveScreen(ending);g.TestFinishDialogue();yield return null;SaveScreen(ending+"-credits");
                        if(state.mode!="ended")throw new Exception("Missing ending credits");
                        var returnButton=UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).First(b=>b.gameObject.activeInHierarchy&&b.name=="Return to title");
                        returnButton.onClick.Invoke();yield return null;
                        if(!GameObject.Find("HUD").activeSelf||!UnityEngine.Object.FindObjectsByType<Button>(FindObjectsSortMode.None).Any(b=>b.gameObject.activeInHierarchy&&b.name=="New game"))throw new Exception("Ending returns to an invisible title");
                        completed++;
                    }
                }
                yield return null;
            }
            File.WriteAllLines(Output+"/playthrough-layout-issues.txt",Issues);
            File.WriteAllText(Output+"/playthrough-status.txt",completed+" full controller playthroughs, "+encounters+" committed encounters, all 15 ending/CG/credits branches verified. Layout issues: "+Issues.Count);
            g.TestTitle();
        }
    }
}
