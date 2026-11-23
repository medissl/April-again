using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEngine;

namespace AprilAgain
{
    public class NovelCatalog : ScriptableObject
    {
        public TextAsset content; public TMP_FontAsset bodyFont, titleFont;
        public SpriteEntry[] sprites; public AudioEntry[] audio;
        Dictionary<string, Sprite> spriteMap;
        Dictionary<string, AudioClip> audioMap;
        ContentData data;
        void OnValidate(){spriteMap=null;audioMap=null;data=null;}
        public ContentData Data => data ?? (data = JsonUtility.FromJson<ContentData>(content.text));
        public Sprite Sprite(string id)
        {
            if (string.IsNullOrEmpty(id)) return null;
            if (spriteMap == null) spriteMap = sprites.ToDictionary(x => x.id, x => x.sprite);
            return spriteMap.TryGetValue(id, out var value) ? value : null;
        }
        public AudioClip Clip(string id)
        {
            if (audioMap == null) audioMap = audio.ToDictionary(x => x.id, x => x.clip);
            return audioMap.TryGetValue(id, out var value) ? value : null;
        }
    }
}
