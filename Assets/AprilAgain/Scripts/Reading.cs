using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using static AprilAgain.NovelUI;

namespace AprilAgain
{
    public partial class AprilAgainGame
    {
        string PlayerFirst=>string.IsNullOrWhiteSpace(session?.firstName)?"Ren":session.firstName;
        string PlayerLast=>string.IsNullOrWhiteSpace(session?.lastName)?"Takahashi":session.lastName;
        string PlayerText(string text)=>Regex.Replace(text,@"\b(Ren Takahashi|Takahashi|Ren)\b",m=>m.Value=="Ren"?PlayerFirst:m.Value=="Takahashi"?PlayerLast:PlayerFirst+" "+PlayerLast);

        Line[] PersonalizedLines(IEnumerable<Line> lines)
        {
            // Names can be longer than the authored default. Measure with the actual
            // game font and retain every word when a reading beat needs another page.
            var measure=Text(stage,"",-6000,0,1560,112,Font,40);
            var result=new List<Line>();
            foreach(var line in lines)
            {
                string text=PlayerText(line.text);var words=Regex.Matches(text,@"\S+\s*");string page="";
                foreach(Match word in words)
                {
                    string trial=page+word.Value;
                    if(page.Length>0&&measure.GetPreferredValues(trial.Trim(),1560,10000).y>112)
                    {result.Add(new Line{speaker=line.speaker,text=page.Trim(),kind=line.kind});page="";}
                    page+=word.Value;
                }
                if(page.Length>0)result.Add(new Line{speaker=line.speaker,text=page.Trim(),kind=line.kind});
            }
            measure.gameObject.SetActive(false);Destroy(measure.gameObject);return result.ToArray();
        }
        void AdvanceInput()
        {
            if(!prefs.autoAfterClick)auto=false;
            skip=false;RefreshReadingControls();NextLine();
        }
        void ApplyDisplay()
        {
            QualitySettings.vSyncCount=prefs.vsync?1:0;
            if(Application.isEditor)return;
            var desktop=Screen.currentResolution;
            if(prefs.fullscreen)Screen.SetResolution(desktop.width,desktop.height,FullScreenMode.FullScreenWindow);
            else
            {
                int[] widths={1280,1600,1920};int width=Mathf.Min(widths[Mathf.Clamp(prefs.windowSize,0,2)],desktop.width-80);
                int height=Mathf.Min(Mathf.RoundToInt(width*9f/16),desktop.height-100);width=Mathf.RoundToInt(height*16f/9);
                Screen.SetResolution(width,height,FullScreenMode.Windowed);
            }
        }
        TMP_InputField NameField(Transform parent,string label,string value,float x)
        {
            Text(parent,label,x,292,440,42,Font,27,Rose);
            var plate=Image(parent,label+" input",x,350,440,82,Color.white,catalog.Sprite("final_button"));plate.raycastTarget=true;
            var viewport=Rect("Text area",plate.transform,20,12,400,58);viewport.gameObject.AddComponent<RectMask2D>();
            var text=Text(viewport,"",0,0,400,58,Font,30,Ink,TextAlignmentOptions.MidlineLeft);
            var field=plate.gameObject.AddComponent<TMP_InputField>();field.targetGraphic=plate;field.textViewport=viewport;field.textComponent=text;
            field.lineType=TMP_InputField.LineType.SingleLine;field.characterLimit=16;field.text=value;field.caretColor=Rose;field.selectionColor=new Color(.8f,.3f,.45f,.25f);
            return field;
        }
        void NameEntry()
        {
            var p=OpenPanel("Your name",1280,850);
            Text(p,"What should your classmates call you?",180,218,920,60,Font,30);
            var first=NameField(p,"First name","Ren",180);var last=NameField(p,"Last name","Takahashi",660);
            var preview=Text(p,"",180,468,920,54,Font,29,Rose,TextAlignmentOptions.Center);
            var error=Text(p,"",180,536,920,96,Font,25,Ink,TextAlignmentOptions.Center);
            string Clean(string value)=>Regex.Replace(value.Trim(),@"\s+"," ");
            bool Valid(string value)=>value.Length>=1&&value.Length<=16&&Regex.IsMatch(value,@"^\p{L}+(?:[ '\-’]\p{L}+)*$")&&Font.HasCharacters(value,out uint[] missing,true,true);
            void Preview(){preview.text=Clean(first.text)+" "+Clean(last.text);error.text="";}
            void Begin()
            {
                string f=Clean(first.text),l=Clean(last.text);
                if(!Valid(f)||!Valid(l)){error.text="Use 1–16 letters for each name. Spaces, apostrophes and hyphens are welcome. Please use letters supported by this font.";return;}
                CloseOverlay(false);NewGame(f,l);
            }
            first.onValueChanged.AddListener(_=>Preview());last.onValueChanged.AddListener(_=>Preview());
            first.onSubmit.AddListener(_=>last.ActivateInputField());last.onSubmit.AddListener(_=>Begin());
            Btn(p,"Cancel",300,704,300,68,DismissOverlay);Btn(p,"Start story",680,704,300,68,Begin,true,true);
            Preview();first.ActivateInputField();
        }
    }
}
