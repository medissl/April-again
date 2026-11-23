using System;
using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEngine;

namespace AprilAgain
{
    [Serializable] public class Line { public string speaker, text, kind; }
    [Serializable] public class Alias { public string id, value; }
    [Serializable] public class CharacterData { public string id, name, voice, busy, used; public string[] idle; public Alias[] aliases; }
    [Serializable] public class Temperature { public string id; public Line[] lines; }
    [Serializable] public class ChoiceData { public string id, kind, text; public Line[] response; }
    [Serializable] public class PropData { public string id, asset, label; }
    [Serializable] public class SceneData
    {
        public string id, girl, title, location, expression, wardrobe, requiredBlock, background, room, portrait;
        public int number; public bool club; public Line[] setup, closing;
        public Temperature[] temperature; public ChoiceData[] choices; public PropData[] props;
    }
    [Serializable] public class SequenceData { public string id, location, background, portrait, girl; public Line[] lines; public PropData[] props; }
    [Serializable] public class EndingData { public string id, girl, kind, title, cg; public Line[] lines; }
    [Serializable] public class ExitData { public string destination,label,kind; public float[] rect; }
    [Serializable] public class LocationData { public string id, name, description; public string[] neighbors; public float[] rect; public ExitData[] exits; }
    [Serializable] public class AssetData { public string id, path; public float[] rect,border; }
    [Serializable] public class ContentData
    {
        public CharacterData[] characters; public SceneData[] scenes; public SequenceData[] sequences;
        public EndingData[] endings; public LocationData[] locations; public AssetData[] assets;
    }
    [Serializable] public class SpriteEntry { public string id; public Sprite sprite; }
    [Serializable] public class AudioEntry { public string id; public AudioClip clip; }
    [Serializable] public class RouteState
    {
        public string id; public int next = 1, good, bad, neutral;
    }
    [Serializable] public class Session
    {
        public int version = 1, day = 1, block, lineIndex;
        public string location = "bedroom", mode = "dialogue", segment = "opening.bedroom", after = "intro.gate";
        public string girl = "", scene = "", background = "bg_bedroom_day", portrait = "", lastChoice = "", pendingEnding = "";
        public bool opening = true, endingUnlocked;
        public RouteState[] routes;
        public List<string> observed = new List<string>(), used = new List<string>(), choices = new List<string>(), history = new List<string>();
        public Line[] lines;
        public static Session New(ContentData c) => new Session { routes = c.characters.Select(x => new RouteState { id = x.id }).ToArray() };
        public RouteState Route(string id) => routes.First(x => x.id == id);
        public Session Clone() => JsonUtility.FromJson<Session>(JsonUtility.ToJson(this));
    }
    [Serializable] public class Preferences
    {
        public float master = .8f, music = .45f, sound = .65f, ambience = .28f, textSpeed = 45f, autoDelay = 2.5f;
        public bool reducedMotion, fullscreen, muteUnfocused;
        public List<string> read = new List<string>(), gallery = new List<string>();
    }
    public static class GameRules
    {
        public static int Weekday(int day) => (day - 1) % 7;
        public static bool Saturday(Session s) => Weekday(s.day) == 5;
        public static bool Sunday(Session s) => Weekday(s.day) == 6;
        public static int Blocks(Session s) => Sunday(s) ? 0 : Saturday(s) ? 3 : 2;
        public static string Block(Session s) => s.block >= Blocks(s) ? "evening" : Saturday(s) && s.block == 0 ? "morning" : s.block == Blocks(s) - 1 ? "late" : "midday";
        public static SceneData Next(ContentData c, Session s, string girl) => c.scenes.FirstOrDefault(x => x.girl == girl && x.number == s.Route(girl).next);
        public static bool Eligible(ContentData c, Session s, string girl)
        {
            var n = Next(c, s, girl);
            if (s.opening || Sunday(s) || s.block >= Blocks(s) || n == null || s.used.Contains(girl) || n.club && !Saturday(s)) return false;
            var block = Block(s);
            if (!string.IsNullOrEmpty(n.requiredBlock)) return block == n.requiredBlock;
            int i = Array.FindIndex(c.characters, x => x.id == girl);
            return block == ((s.day + i) % 5 < 3 ? "midday" : "late") || Saturday(s) && block == "morning";
        }
        public static string Place(ContentData c, Session s, string girl)
        {
            if (s.opening) return c.sequences.First(x => x.id == "observe." + girl).location;
            if (s.block >= Blocks(s) || Sunday(s)) return "";
            var ch = c.characters.First(x => x.id == girl);
            if (Eligible(c, s, girl)) return Next(c, s, girl).location;
            return ch.idle[(s.day + s.block) % ch.idle.Length];
        }
        public static string Temperature(RouteState r) => r.good - r.bad >= 3 ? "warm" : r.good - r.bad <= -3 ? "cool" : "mixed";
        public static string Ending(RouteState r) => r.good == r.bad ? "neutral" : r.good > r.bad ? "good" : "bad";
        public static void Commit(ContentData c, Session s, SceneData scene, ChoiceData choice)
        {
            if (!scene.choices.Any(x => x.id == choice.id) || s.scene != scene.id || s.Route(scene.girl).next != scene.number || !Eligible(c, s, scene.girl) || s.location != scene.location || s.choices.Contains(choice.id))
                throw new InvalidOperationException("This choice has already been recorded or the appointment has changed.");
            var r = s.Route(scene.girl);
            if (choice.kind == "good") r.good++; else if (choice.kind == "bad") r.bad++; else r.neutral++;
            r.next++; s.used.Add(scene.girl); s.choices.Add(choice.id); s.lastChoice = choice.kind; s.block++;
            if (scene.number == 15) s.pendingEnding = scene.girl + ".ending." + Ending(r);
        }
        public static void AdvanceDay(Session s) { s.day++; s.block = 0; s.used.Clear(); s.location = "bedroom"; }
        public static bool Valid(ContentData c, Session s)
        {
            if (s == null || s.version != 1 || s.day < 1 || s.day > 100000 || s.block < 0 || s.block > 3 || s.routes == null || s.routes.Length != 5 || s.choices == null || s.used == null || s.observed == null || s.history == null || s.lines == null) return false;
            if (s.routes.Select(x=>x.id).Distinct().Count()!=5 || c.characters.Any(x=>!s.routes.Any(r=>r.id==x.id))) return false;
            if (!c.locations.Any(x=>x.id==s.location) || s.lineIndex<0 || s.lineIndex>s.lines.Length || s.choices.Distinct().Count()!=s.choices.Count) return false;
            if(!new[]{"explore","dialogue","choices","ended"}.Contains(s.mode) || s.lines.Length>1000 || s.history.Count>400) return false;
            if(s.lines.Any(l=>l==null||l.text==null||l.speaker==null))return false;
            if(s.observed.Any(id=>!c.characters.Any(x=>x.id==id)) || s.used.Any(id=>!c.characters.Any(x=>x.id==id))) return false;
            if(s.observed.Distinct().Count()!=s.observed.Count || s.used.Distinct().Count()!=s.used.Count) return false;
            if(!string.IsNullOrEmpty(s.pendingEnding)&&!c.endings.Any(e=>e.id==s.pendingEnding)) return false;
            if(s.mode=="choices"&&!c.scenes.Any(x=>x.id==s.scene)) return false;
            if(s.mode=="ended"&&string.IsNullOrEmpty(s.pendingEnding)) return false;
            if(s.choices.Any(id=>!c.scenes.Any(x=>x.choices.Any(ch=>ch.id==id)))) return false;
            return s.routes.All(r=> r.next>=1 && r.next<=16 && r.good>=0 && r.bad>=0 && r.neutral>=0 && r.good+r.bad+r.neutral==r.next-1);
        }
    }
}
