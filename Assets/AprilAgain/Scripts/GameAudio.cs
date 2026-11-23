using UnityEngine;

namespace AprilAgain
{
    public class GameAudio : MonoBehaviour
    {
        AudioSource music, effects, ambience;
        NovelCatalog catalog; Preferences prefs;
        string currentMusic, currentAmbience;
        public void Init(NovelCatalog c, Preferences p)
        {
            catalog=c; prefs=p;
            music=gameObject.AddComponent<AudioSource>(); music.loop=true;
            effects=gameObject.AddComponent<AudioSource>();
            ambience=gameObject.AddComponent<AudioSource>(); ambience.loop=true;
            Apply();
        }
        public void Apply()
        {
            if(music==null)return;
            music.volume=prefs.master*prefs.music;
            effects.volume=prefs.master*prefs.sound;
            ambience.volume=prefs.master*prefs.ambience*.35f;
        }
        public void Music(string id)
        {
            if(currentMusic==id)return;currentMusic=id;
            music.Stop(); music.clip=catalog.Clip(id); if(music.clip!=null)music.Play();
        }
        public void Ambience(string id)
        {
            if(currentAmbience==id)return; currentAmbience=id;
            ambience.Stop(); ambience.clip=catalog.Clip(id);if(ambience.clip!=null)ambience.Play();
        }
        public void Sfx(string id,float gain=1) { var c=catalog.Clip(id);if(c!=null)effects.PlayOneShot(c,Mathf.Clamp01(gain)); }
        void OnApplicationFocus(bool focus) { if(prefs!=null)AudioListener.pause=prefs.muteUnfocused&&!focus; }
    }
}
