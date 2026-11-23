using System;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

namespace AprilAgain
{
    public class MapHitRegion : MonoBehaviour, ICanvasRaycastFilter
    {
        public RectTransform space;public Rect[] regions;
        public bool IsRaycastLocationValid(Vector2 point,Camera camera)
        {
            if(!RectTransformUtility.ScreenPointToLocalPointInRectangle(space,point,camera,out var local))return false;
            return regions.Any(r=>r.Contains(new Vector2(local.x,-local.y)));
        }
    }
    public class SoftHighlight : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, ISelectHandler, IDeselectHandler
    {
        public Action<bool> change;
        bool hovered,selected,active;
        void Apply(){bool next=hovered||selected;if(next==active)return;active=next;change?.Invoke(next);}
        public void OnPointerEnter(PointerEventData e){hovered=true;Apply();}
        public void OnPointerExit(PointerEventData e){hovered=false;Apply();}
        public void OnSelect(BaseEventData e){selected=true;Apply();}
        public void OnDeselect(BaseEventData e){selected=false;Apply();}
        void OnDisable(){hovered=selected=false;Apply();}
    }
    public static class NovelUI
    {
        public static NovelCatalog Skin;
        public static RectTransform Stage;
        public static readonly Color Ink=Hex("6E3C50"), Rose=Hex("CB4D7A"), Paper=Hex("FFF7F2"), Muted=Hex("7E6270");
        public static Color Hex(string value) { ColorUtility.TryParseHtmlString("#"+value,out var c);return c; }
        public static RectTransform Rect(string name, Transform parent, float x,float y,float w,float h)
        {
            var o=new GameObject(name,typeof(RectTransform));o.transform.SetParent(parent,false);
            var r=o.GetComponent<RectTransform>();r.anchorMin=r.anchorMax=new Vector2(0,1);r.pivot=new Vector2(0,1);
            r.anchoredPosition=new Vector2(x,-y);r.sizeDelta=new Vector2(w,h);return r;
        }
        public static Image Image(Transform p,string name,float x,float y,float w,float h,Color color,Sprite sprite=null,bool aspect=false)
        {
            var r=Rect(name,p,x,y,w,h);var i=r.gameObject.AddComponent<Image>();i.color=color;i.sprite=sprite;i.preserveAspect=aspect;i.raycastTarget=false;
            if(sprite!=null&&!aspect&&sprite.border.sqrMagnitude>0)i.type=UnityEngine.UI.Image.Type.Sliced;
            return i;
        }
        public static TextMeshProUGUI Text(Transform p,string value,float x,float y,float w,float h,TMP_FontAsset font,int size=30,Color? color=null,TextAlignmentOptions align=TextAlignmentOptions.TopLeft)
        {
            var r=Rect("Text",p,x,y,w,h);var t=r.gameObject.AddComponent<TextMeshProUGUI>();
            t.font=font;t.text=value;t.fontSize=size;t.color=color??Ink;t.alignment=align;t.raycastTarget=false;
            t.textWrappingMode=TextWrappingModes.Normal;t.overflowMode=TextOverflowModes.Overflow;t.richText=false;return t;
        }
        public static void CenterArtwork(Image image)
        {
            var rect=image.rectTransform;var center=new Vector2(.5f,.5f);
            rect.anchoredPosition+=Vector2.Scale(center-rect.pivot,rect.rect.size);rect.pivot=center;
        }
        public static Button Button(Transform p,string value,float x,float y,float w,float h,TMP_FontAsset font,Action click,bool enabled=true,bool accent=false,Action hover=null)
        {
            var sprite=Skin?.Sprite(accent?"final_button_primary":"final_button");
            var image=Image(p,value,x,y,w,h,sprite!=null?Color.white:Paper,sprite);image.raycastTarget=true;
            var b=image.gameObject.AddComponent<Button>();b.targetGraphic=image;b.interactable=enabled;
            var colors=b.colors;colors.normalColor=Color.white;colors.highlightedColor=Hex("F3D3E2");colors.pressedColor=Hex("DB9CB7");colors.selectedColor=Hex("F1CCDD");colors.disabledColor=new Color(.92f,.85f,.88f,.7f);b.colors=colors;
            var t=Text(image.transform,value,20,8,w-40,h-16,font,26,accent?Paper:Ink,TextAlignmentOptions.Center);t.fontStyle=FontStyles.Normal;
            var focus=image.gameObject.AddComponent<Outline>();focus.effectColor=Rose;focus.effectDistance=new Vector2(2,-2);focus.enabled=false;
            image.gameObject.AddComponent<SoftHighlight>().change=on=>{focus.enabled=on&&enabled;if(on&&enabled)hover?.Invoke();};
            b.onClick.AddListener(()=>{if(enabled)click();});return b;
        }
        public static Button QuietButton(Transform p,string value,float x,float y,float w,float h,TMP_FontAsset font,Action click,Action hover=null)
        {
            var i=Image(p,value,x,y,w,h,new Color(1,1,1,0));i.raycastTarget=true;
            var b=i.gameObject.AddComponent<Button>();b.transition=Selectable.Transition.None;b.targetGraphic=i;
            var t=Text(i.transform,value,0,4,w,h-8,font,24,Ink,TextAlignmentOptions.Center);
            var line=Image(i.transform,"Focus",14,h-5,w-28,2,Rose);line.gameObject.SetActive(false);
            i.gameObject.AddComponent<SoftHighlight>().change=on=>{t.color=on?Rose:Ink;line.gameObject.SetActive(on);if(on)hover?.Invoke();};
            b.onClick.AddListener(()=>click());return b;
        }
        public static Button IconButton(Transform p,string name,string icon,float x,float y,float size,TMP_FontAsset font,Action click,Action hover=null,Color? tint=null)
        {
            var i=Image(p,name,x,y,size,size,new Color(1,1,1,0));i.raycastTarget=true;
            var b=i.gameObject.AddComponent<Button>();b.transition=Selectable.Transition.None;b.targetGraphic=i;
            var glyph=Image(i.transform,"Icon",size*.08f,size*.08f,size*.84f,size*.84f,tint??Ink,Skin?.Sprite("spring_icon_"+icon),true);
            var shade=glyph.gameObject.AddComponent<Shadow>();shade.effectColor=new Color(.2f,.1f,.15f,.3f);shade.effectDistance=new Vector2(0,-1);
            if(tint.HasValue)
            {
                var outline=glyph.gameObject.AddComponent<Outline>();outline.effectColor=new Color(.25f,.12f,.2f,.72f);outline.effectDistance=new Vector2(1.5f,-1.5f);
            }
            var tip=Image(i.transform,"Hint",-(180-size)/2,y>850?-48:size+4,180,42,Color.white,Skin?.Sprite("final_tooltip"));tip.gameObject.SetActive(false);
            Text(tip.transform,name,10,5,160,32,font,20,Ink,TextAlignmentOptions.Center);
            KeepInsideStage(tip.rectTransform);
            i.gameObject.AddComponent<SoftHighlight>().change=on=>{tip.gameObject.SetActive(on);glyph.color=on?Rose:tint??Ink;if(on)hover?.Invoke();};
            b.onClick.AddListener(()=>click());return b;
        }
        public static Button Hotspot(Transform p,string label,float x,float y,float w,float h,TMP_FontAsset font,Action click,Action hover)
        {
            var b=HitArea(p,"Inspect "+label,x,y,w,h,click);
            var frame=Rect("Focus corners",b.transform,0,0,w,h);frame.gameObject.SetActive(false);
            foreach(float xx in new[]{0f,w-16})foreach(float yy in new[]{0f,h-16})
            {
                Image(frame,"Corner",xx,yy+(yy>0?14:0),16,2,Paper);
                Image(frame,"Corner",xx+(xx>0?14:0),yy,2,16,Paper);
            }
            float cw=320,cx=Mathf.Clamp((w-cw)/2,32-x,1888-x-cw);
            var caption=Image(b.transform,"Hover label",cx,Mathf.Max(0,h-56),cw,56,Color.white,Skin?.Sprite("final_tooltip"));caption.gameObject.SetActive(false);
            Text(caption.transform,label,12,8,cw-24,40,font,23,Ink,TextAlignmentOptions.Center);
            b.gameObject.AddComponent<SoftHighlight>().change=on=>{frame.gameObject.SetActive(on);caption.gameObject.SetActive(on);if(on)hover?.Invoke();};
            return b;
        }
        public static Button HitArea(Transform p,string name,float x,float y,float w,float h,Action click)
        {
            var i=Image(p,name,x,y,w,h,new Color(1,1,1,0));i.raycastTarget=true;
            var b=i.gameObject.AddComponent<Button>();b.targetGraphic=i;b.transition=Selectable.Transition.None;
            b.onClick.AddListener(()=>click());return b;
        }
        public static Button DoorTarget(Transform p,string label,float x,float y,float w,float h,TMP_FontAsset font,Action click,Action hover,bool showMarker=true)
        {
            float hitWidth=Mathf.Max(56,w);x-=(hitWidth-w)/2;w=hitWidth;
            var b=HitArea(p,"Door "+label,x,y,w,h,click);
            var arrow=Image(b.transform,"Door marker",w/2-18,h/2-18,36,36,Paper,Skin?.Sprite("spring_icon_next"),true);
            arrow.gameObject.SetActive(showMarker);
            var outline=arrow.gameObject.AddComponent<Outline>();outline.effectColor=new Color(.2f,.1f,.15f,.7f);outline.effectDistance=new Vector2(1,-1);
            float cw=230,cx=Mathf.Clamp((w-cw)/2,32-x,1888-x-cw);
            var caption=Image(b.transform,"Destination",cx,h/2-28,cw,56,Color.white,Skin?.Sprite("final_tooltip"));caption.gameObject.SetActive(false);
            Text(caption.transform,label,12,8,cw-24,40,font,23,Ink,TextAlignmentOptions.Center);
            b.gameObject.AddComponent<SoftHighlight>().change=on=>{arrow.gameObject.SetActive(showMarker&&!on);caption.gameObject.SetActive(on);if(on)hover?.Invoke();};
            return b;
        }
        public static Button MapTarget(RectTransform parent,string name,Rect[] regions,Action click)
        {
            float x=regions.Min(r=>r.xMin),y=regions.Min(r=>r.yMin);
            var button=HitArea(parent,name,x,y,regions.Max(r=>r.xMax)-x,regions.Max(r=>r.yMax)-y,click);
            var filter=button.gameObject.AddComponent<MapHitRegion>();filter.space=parent;filter.regions=regions;
            return button;
        }
        public static void KeepInsideStage(RectTransform target)
        {
            if(Stage==null)return;
            var corners=new Vector3[4];target.GetWorldCorners(corners);
            var points=corners.Select(p=>Stage.InverseTransformPoint(p)).ToArray();var safe=Stage.rect;
            float dx=Mathf.Max(0,safe.xMin+32-points.Min(p=>p.x))+Mathf.Min(0,safe.xMax-32-points.Max(p=>p.x));
            float dy=Mathf.Max(0,safe.yMin+32-points.Min(p=>p.y))+Mathf.Min(0,safe.yMax-32-points.Max(p=>p.y));
            target.anchoredPosition+=new Vector2(dx,dy);
        }
        public static RectTransform Scroll(Transform parent,float x,float y,float w,float h,float contentHeight)
        {
            var r=Rect("Scroll",parent,x,y,w,h);var scroll=r.gameObject.AddComponent<ScrollRect>();
            var view=Rect("Viewport",r,0,0,w,h);view.gameObject.AddComponent<RectMask2D>();
            var hit=view.gameObject.AddComponent<Image>();hit.color=new Color(1,1,1,.001f);
            var content=Rect("Content",view,0,0,w-24,Mathf.Max(h,contentHeight));
            scroll.viewport=view;scroll.content=content;scroll.horizontal=false;scroll.movementType=ScrollRect.MovementType.Clamped;scroll.scrollSensitivity=48;
            return content;
        }
        public static void Clear(Transform parent)
        {
            for(int i=parent.childCount-1;i>=0;i--){var o=parent.GetChild(i).gameObject;o.SetActive(false);UnityEngine.Object.Destroy(o);}
        }
    }
}
