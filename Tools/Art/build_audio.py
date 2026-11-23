"""Original synthesized underscore and foley; no sampled/copyrighted recordings."""
from pathlib import Path
import json, wave
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'Assets/AprilAgain/Audio'
SR=22050
RNG=np.random.default_rng(4217)
CAT=[]

def write(name, sound, loop=False, provenance='Original procedural sound design'):
    sound=np.asarray(sound,dtype=float)
    if sound.ndim==1: sound=np.stack((sound,sound),axis=1)
    peak=float(np.max(np.abs(sound)))
    if peak>0.88: sound*=0.88/peak
    OUT.mkdir(parents=True,exist_ok=True)
    with wave.open(str(OUT/(name+'.wav')),'wb') as w:
        w.setparams((2,2,SR,len(sound),'NONE','not compressed'))
        w.writeframes((np.clip(sound,-1,1)*32767).astype('<i2').tobytes())
    CAT.append(dict(id=name,file=name+'.wav',seconds=round(len(sound)/SR,3),sampleRate=SR,
                    channels=2,loop=loop,peak=round(float(np.max(np.abs(sound))),5),
                    rms=round(float(np.sqrt(np.mean(sound*sound))),5),provenance=provenance))

def tone(freq, seconds, amp=.14):
    t=np.arange(int(seconds*SR))/SR
    env=(1-np.exp(-t*95))*np.exp(-t*2.6)
    end=np.minimum(1,(seconds-t)/.04)
    return amp*env*end*(np.sin(2*np.pi*freq*t)+.22*np.sin(4*np.pi*freq*t)+.07*np.sin(6*np.pi*freq*t))

def midi(n): return 440*2**((n-69)/12)

def music(name,bpm,chords,melody):
    beat=60/bpm
    n=round(32*beat*SR)
    x=np.zeros((n,2))
    def add(note,start,amp=.11,pan=0):
        v=tone(midi(note),3.1,amp)
        at=round(start*beat*SR)
        indices=(np.arange(len(v))+at)%n
        # Wrapped tails form an actual seamless musical loop.
        np.add.at(x[:,0],indices,v*(.72-pan*.15))
        np.add.at(x[:,1],indices,v*(.72+pan*.15))
    for bar in range(8):
        chord=chords[bar%len(chords)]
        add(chord[0]-12,bar*4,.11,-.15)
        for i,pitch in enumerate(chord):
            add(pitch,bar*4+i*.5,.068,-.4+i*.27)
        add(chord[1],bar*4+2.5,.055,.25)
        for pos,note in melody[bar%len(melody)]:
            add(note,bar*4+pos,.115,.1)
    # Restrained short stereo room reflection, circular for continuous looping.
    x+=np.roll(x,int(.083*SR),axis=0)*.10
    x+=np.roll(x[:,::-1],int(.173*SR),axis=0)*.06
    write(name,x,True,'Original eight-bar composition; synthesized soft piano-like instrument, no samples')

def noise(seconds,amp=.08,smooth=10):
    x=RNG.normal(0,1,int(seconds*SR))
    return np.convolve(x,np.ones(smooth)/smooth,mode='same')*amp

def fade(x,edge=.02):
    n=min(round(edge*SR),len(x)//2)
    if n:
        x[:n]*=np.linspace(0,1,n)
        x[-n:]*=np.linspace(1,0,n)
    return x

def sfx():
    write('ui_confirm',tone(659,.17,.1)+tone(988,.17,.06))
    write('ui_hover',tone(880,.06,.035))
    write('ui_cancel',tone(392,.18,.085))
    write('page_turn',fade(noise(.48,.16,3)*np.sin(np.linspace(0,np.pi,int(.48*SR)))**2))
    write('paper',fade(noise(.27,.12,2)*np.sin(np.linspace(0,np.pi,int(.27*SR)))**2))
    write('zip',fade(noise(.38,.13,2)*(.6+.4*np.sin(np.arange(int(.38*SR))*.09))))
    write('cup',tone(1780,.28,.075)+tone(2710,.28,.035))
    write('footstep',fade(noise(.19,.14,22)*np.exp(-np.arange(int(.19*SR))/SR*21)))
    t=np.arange(int(.65*SR))/SR
    bounce=np.sin(2*np.pi*(125*t-55*t*t))*np.exp(-t*16)*.28
    bounce+=noise(.65,.05,5)*np.exp(-t*30)
    write('basketball_bounce',fade(bounce,.004))
    write('basketball_rim',tone(540,.7,.12)+tone(1120,.7,.08))
    write('door',fade(noise(.65,.09,25))+tone(110,.65,.06))
    write('bag_set_down',fade(noise(.28,.17,18)*np.exp(-np.arange(int(.28*SR))/SR*13)))
    bell=np.zeros(int(5*SR))
    for at,n in [(0,76),(.7,72),(1.4,74),(2.1,67)]:
        v=tone(midi(n),2.8,.16)
        pos=round(at*SR); end=min(pos+len(v),len(bell));bell[pos:end]+=v[:end-pos]
    write('school_bell',fade(bell,.04))
    alarm=np.zeros(int(3*SR))
    for at in [0,.22,.44,1.25,1.47,1.69]:
        v=tone(880,.13,.1);p=round(at*SR);alarm[p:p+len(v)]+=v
    write('alarm',fade(alarm))
    write('pa_chime',tone(523,1.6,.09)+tone(659,1.6,.07))
    # Noise loops use matching endpoint crossfades rather than hard cuts.
    for name,amp,smooth in [('light_rain',.12,4),('amb_school',.035,60)]:
        x=noise(16,amp,smooth)
        edge=SR
        bridge=np.linspace(0,1,edge)
        x[:edge]=x[:edge]*bridge+x[-edge:]*(1-bridge)
        x=x[:-edge]
        write(name,x,True)

if __name__=='__main__':
    C=[60,64,67,71]; Am=[57,60,64,67]; F=[53,57,60,64]; G=[55,59,62,67]
    motif=[[(.5,76),(2,74),(3,72)],[(1,71),(2.5,72)],[(.5,69),(2,72),(3,74)],[(1,71),(3,67)]]
    music('bgm_daily',88,[C,Am,F,G],motif)
    music('bgm_reflection',68,[Am,F,C,G],[[(1,72),(3,71)],[(.5,69),(2.5,67)],[(1,64),(3,67)],[(2,71)]])
    music('bgm_ending_good',80,[F,G,Am,C],[[(.5,72),(1.5,74),(3,76)],[(1,74),(2.5,71)],[(.5,72),(2,76)],[(1,74),(3,72)]])
    music('bgm_ending_neutral',76,[C,F,Am,G],motif)
    music('bgm_ending_bad',66,[Am,F,[55,59,62,65],Am],[[(1,72),(3,71)],[(1,69),(3,67)],[(.5,65),(2.5,64)],[(2,69)]])
    sfx()
    (OUT/'audio-manifest.json').write_text(json.dumps(dict(license='Original project-authored compositions and sound design; no third-party samples.',assets=CAT),indent=2),encoding='utf-8')
    print(f'Wrote {len(CAT)} original audio assets; all peaks below 0 dBFS.')
