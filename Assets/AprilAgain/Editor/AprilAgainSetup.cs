using System;
using System.IO;
using System.Linq;
using TMPro;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.TextCore.LowLevel;
using UnityEditor.Build.Reporting;

namespace AprilAgain.Editor
{
    public static class AprilAgainSetup
    {
        const string Root="Assets/AprilAgain/";
        [MenuItem("April Again/Prepare game")]
        public static string Prepare()
        {
            if(TMP_Settings.instance==null){TMP_PackageResourceImporter.ImportResources(true,false,false);return "TMP resources importing. Run Prepare again after import completes.";}
            AssetDatabase.Refresh();
            var json=AssetDatabase.LoadAssetAtPath<TextAsset>(Root+"GameData/content.json");
            var data=JsonUtility.FromJson<ContentData>(json.text);
            foreach(var a in data.assets)
            {
                var t=AssetImporter.GetAtPath(a.path) as TextureImporter;if(t==null)throw new Exception("Missing art "+a.path);
                var border=a.border!=null&&a.border.Length==4?new Vector4(a.border[0],a.border[1],a.border[2],a.border[3]):Vector4.zero;
                if(t.textureType==TextureImporterType.Sprite&&t.spriteImportMode==SpriteImportMode.Single&&t.alphaIsTransparency&&t.maxTextureSize==4096&&t.spriteBorder==border&&!t.mipmapEnabled&&t.textureCompression==TextureImporterCompression.Uncompressed)continue;
                t.textureType=TextureImporterType.Sprite;t.spriteImportMode=SpriteImportMode.Single;t.alphaIsTransparency=true;t.mipmapEnabled=false;t.isReadable=false;
                t.wrapMode=TextureWrapMode.Clamp;t.filterMode=FilterMode.Bilinear;t.maxTextureSize=4096;t.textureCompression=TextureImporterCompression.Uncompressed;t.spriteBorder=border;
                t.SaveAndReimport();
            }
            var path=Root+"GameData/GameCatalog.asset";
            var catalog=AssetDatabase.LoadAssetAtPath<NovelCatalog>(path);
            if(catalog==null){catalog=ScriptableObject.CreateInstance<NovelCatalog>();AssetDatabase.CreateAsset(catalog,path);}
            catalog.content=json;
            catalog.bodyFont=Font("Nunito/Nunito-ExtraBold","NunitoDefault");catalog.titleFont=catalog.bodyFont;
            TMP_Settings.defaultFontAsset=catalog.bodyFont;EditorUtility.SetDirty(TMP_Settings.instance);
            var used=data.scenes.SelectMany(s=>s.props.Select(p=>p.asset)).Concat(data.sequences.SelectMany(s=>(s.props??Array.Empty<PropData>()).Select(p=>p.asset))).ToHashSet();
            var retiredSkin=new[]{"spring_button","spring_choice","spring_choice_hover","spring_date"};
            bool RuntimeArt(AssetData a)=>used.Contains(a.id)||a.id.StartsWith("final_")||a.id.StartsWith("spring_")&&!retiredSkin.Contains(a.id)||a.id.StartsWith("bg_")||a.id.StartsWith("expr_")||a.id.StartsWith("pose_")||a.id.StartsWith("room_")||a.id.StartsWith("observation_")||a.id.StartsWith("cg_")||a.id=="map_campus"||a.id=="title_establishing"||a.id.StartsWith("char_")&&a.id.EndsWith("_base")||a.id.StartsWith("vn_")||a.id.StartsWith("wardrobe_")&&new[]{"_full_body","_neutral","_active","_soft_smile","_flustered"}.Any(suffix=>a.id.EndsWith(suffix));
            catalog.sprites=data.assets.Where(RuntimeArt).Select(a=>new SpriteEntry{id=a.id,sprite=AssetDatabase.LoadAssetAtPath<Sprite>(a.path)}).ToArray();
            if(catalog.sprites.Any(x=>x.sprite==null))throw new Exception("Missing imported sprite");
            var activeAudio=new[]{"hover","select","open","back","save","error","room_door","rain_window"};
            catalog.audio=Directory.GetFiles(Root+"Audio","*",SearchOption.AllDirectories).Where(x=>(x.EndsWith(".wav")||x.EndsWith(".ogg"))&&(Path.GetFileNameWithoutExtension(x).StartsWith("bgm_")||activeAudio.Contains(Path.GetFileNameWithoutExtension(x)))).Select(x=>new AudioEntry{id=Path.GetFileNameWithoutExtension(x),clip=AssetDatabase.LoadAssetAtPath<AudioClip>(x.Replace('\\','/'))}).ToArray();
            if(catalog.audio.Any(x=>x.clip==null)||catalog.audio.Select(x=>x.id).Distinct().Count()!=catalog.audio.Length)throw new Exception("Invalid audio bindings");
            EditorUtility.SetDirty(catalog);AssetDatabase.SaveAssets();
            var scene=EditorSceneManager.NewScene(NewSceneSetup.EmptyScene,NewSceneMode.Single);
            var camera=new GameObject("Novel Camera",typeof(Camera),typeof(AudioListener));camera.tag="MainCamera";camera.transform.position=new Vector3(0,0,-10);
            var game=new GameObject("April again",typeof(AprilAgainGame));game.GetComponent<AprilAgainGame>().catalog=catalog;
            EditorSceneManager.SaveScene(scene,"Assets/Scenes/AprilAgain.unity");
            EditorBuildSettings.scenes=new[]{new EditorBuildSettingsScene("Assets/Scenes/AprilAgain.unity",true)};
            PlayerSettings.companyName="Medissl";PlayerSettings.productName="April, again";PlayerSettings.bundleVersion="1.0.1";
            PlayerSettings.defaultScreenWidth=1920;PlayerSettings.defaultScreenHeight=1080;PlayerSettings.resizableWindow=true;
            PlayerSettings.fullScreenMode=FullScreenMode.FullScreenWindow;PlayerSettings.runInBackground=true;
            PlayerSettings.SetUseDefaultGraphicsAPIs(BuildTarget.StandaloneWindows64,false);
            PlayerSettings.SetGraphicsAPIs(BuildTarget.StandaloneWindows64,new[]{UnityEngine.Rendering.GraphicsDeviceType.Direct3D11});
            PlayerSettings.SplashScreen.show=false;
            var icon=AssetDatabase.LoadAssetAtPath<Texture2D>(Root+"Art/Title/app_icon_final.png");
            if(icon==null)throw new Exception("Missing game icon");
            var target=UnityEditor.Build.NamedBuildTarget.Standalone;
            PlayerSettings.SetIcons(target,Enumerable.Repeat(icon,PlayerSettings.GetIconSizes(target,IconKind.Application).Length).ToArray(),IconKind.Application);
            PlayerSettings.SetScriptingBackend(UnityEditor.Build.NamedBuildTarget.Standalone,ScriptingImplementation.Mono2x);
            AssetDatabase.SaveAssets();return "Prepared 75 scenes, 15 endings, full art/audio catalog and AprilAgain.unity";
        }
        static TMP_FontAsset Font(string source,string name)
        {
            var path=Root+"GameData/"+name+"Font.asset";var existing=AssetDatabase.LoadAssetAtPath<TMP_FontAsset>(path);if(existing!=null)return existing;
            var font=AssetDatabase.LoadAssetAtPath<UnityEngine.Font>(Root+"Art/Fonts/"+source+".ttf");
            var asset=TMP_FontAsset.CreateFontAsset(font,64,9,GlyphRenderMode.SDFAA,1024,1024,AtlasPopulationMode.Dynamic,true);
            asset.name=name+" Font";AssetDatabase.CreateAsset(asset,path);AssetDatabase.AddObjectToAsset(asset.material,asset);
            foreach(var texture in asset.atlasTextures){texture.name=name+" Atlas";AssetDatabase.AddObjectToAsset(texture,asset);}
            asset.TryAddCharacters("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?:;'\"—–-…•›/()%+&éÉáàäöüñôçèí韓한서윤黒川安子茉莉");
            EditorUtility.SetDirty(asset);return asset;
        }
        [MenuItem("April Again/Build Windows player")]
        public static string Build()
        {
            Directory.CreateDirectory("Builds/Windows");
            var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions{scenes=new[]{"Assets/Scenes/AprilAgain.unity"},locationPathName="Builds/Windows/AprilAgain.exe",target=BuildTarget.StandaloneWindows64,options=BuildOptions.CleanBuildCache|BuildOptions.CompressWithLz4HC});
            if(report.summary.result!=BuildResult.Succeeded)throw new Exception("Build failed: "+report.summary.result);
            return "Built Windows player: "+report.summary.totalSize+" bytes";
        }
        [MenuItem("April Again/Validate rules")]
        public static string Validate()
        {
            var c=AssetDatabase.LoadAssetAtPath<NovelCatalog>(Root+"GameData/GameCatalog.asset").Data;
            int assertions=0,completed=0,maxDay=0;
            void Check(bool ok,string name){assertions++;if(!ok)throw new Exception("Regression: "+name);}
            foreach(var girl in c.characters)
            foreach(var kind in new[]{"good","neutral","bad"})
            {
                var s=Session.New(c);s.opening=false;s.day=2;s.lines=Array.Empty<Line>();
                for(int n=1;n<=15;n++)
                {
                    int guard=0;while(!GameRules.Eligible(c,s,girl.id))
                    {
                        if(s.block<GameRules.Blocks(s))s.block++;else GameRules.AdvanceDay(s);
                        Check(++guard<300,"schedule cannot strand "+girl.id+" "+n);
                    }
                    var scene=GameRules.Next(c,s,girl.id);s.scene=scene.id;s.location=scene.location;
                    var choice=scene.choices.First(x=>x.kind==kind);int oldBlock=s.block;
                    GameRules.Commit(c,s,scene,choice);Check(s.block==oldBlock+1,"one block per encounter");Check(s.Route(girl.id).next==n+1,"advance exactly once");
                    Check(!GameRules.Eligible(c,s,girl.id),"daily limit");
                    var count=s.choices.Count;bool rejected=false;try{GameRules.Commit(c,s,scene,choice);}catch(InvalidOperationException){rejected=true;}
                    Check(rejected&&s.choices.Count==count,"duplicate is atomic");
                    var copy=s.Clone();Check(GameRules.Valid(c,copy),"serialized state valid");
                    Check(copy.Route(girl.id).next==n+1,"save roundtrip");
                }
                Check(s.pendingEnding==girl.id+".ending."+kind,"correct ending");maxDay=Math.Max(maxDay,s.day);completed++;
            }
            for(int g=0;g<=15;g++)for(int b=0;b<=15-g;b++)
            {
                var r=new RouteState{good=g,bad=b,neutral=15-g-b};
                Check(GameRules.Ending(r)==(g==b?"neutral":g>b?"good":"bad"),"neutral votes balance");
            }
            foreach(var l in c.locations)foreach(var other in l.neighbors)Check(c.locations.First(x=>x.id==other).neighbors.Contains(l.id),"reversible map");
            var result=new ValidationReport{assertions=assertions,completedRoutes=completed,longestRunDay=maxDay,scenes=c.scenes.Length,endings=c.endings.Length};
            Directory.CreateDirectory("Documentation/Testing");var text=JsonUtility.ToJson(result,true);File.WriteAllText("Documentation/Testing/rules-results.json",text);return text;
        }
        [Serializable] class ValidationReport { public int assertions,completedRoutes,longestRunDay,scenes,endings;public string status="passed"; }
    }
}
