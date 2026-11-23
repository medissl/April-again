using System;
using System.IO;
using UnityEngine;

namespace AprilAgain
{
    public static class SaveStore
    {
        public static string Root => Application.isEditor
            ? Path.GetFullPath(Path.Combine(Application.dataPath,"../Library/AprilAgainPlaytest"))
            : Path.Combine(Application.persistentDataPath, "AprilAgain");
        static string PathFor(string slot) => Path.Combine(Root, slot + ".json");
        public static void Write(string slot, object value)
        {
            Directory.CreateDirectory(Root);
            var path = PathFor(slot); var temporary = path + ".tmp";
            File.WriteAllText(temporary, JsonUtility.ToJson(value, true));
            if (File.Exists(path)) File.Replace(temporary, path, path + ".bak");
            else File.Move(temporary, path);
        }
        public static T Read<T>(string slot) where T : class
        {
            foreach (var path in new[] { PathFor(slot), PathFor(slot) + ".bak" })
            {
                try { if (File.Exists(path)) { var v = JsonUtility.FromJson<T>(File.ReadAllText(path)); if (v != null) return v; } }
                catch (Exception ex) when (ex is IOException || ex is ArgumentException || ex is UnauthorizedAccessException) { }
            }
            return null;
        }
        public static Session Load(string slot, ContentData c)
        {
            foreach(var suffix in new[]{"", ".bak"})
            {
                try
                {
                    var path=PathFor(slot)+suffix;
                    if(File.Exists(path)) { var s=JsonUtility.FromJson<Session>(File.ReadAllText(path)); if(GameRules.Valid(c,s)) return s; }
                }
                catch(Exception ex) when(ex is IOException || ex is ArgumentException || ex is UnauthorizedAccessException) { }
            }
            return null;
        }
        public static string Modified(string slot) => File.Exists(PathFor(slot)) ? File.GetLastWriteTime(PathFor(slot)).ToString("dd MMM • HH:mm") : "Empty";
    }
}
