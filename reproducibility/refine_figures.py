from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

OUT=Path(__file__).resolve().parent / 'generated' / 'refined'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'pdf.fonttype':42,'savefig.facecolor':'white'})
BLACK='#111111'; GREY='#777777'; PALE='#f6f6f6'; LIGHT='#e8e8e8'

def save(fig,name):
    fig.savefig(OUT/(name+'.png'), dpi=250, bbox_inches='tight', facecolor='white')
    fig.savefig(OUT/(name+'.pdf'), bbox_inches='tight', facecolor='white')
    plt.close(fig)

def textbox(ax,x,y,w,h,label,fs=9,fc=PALE,edge=BLACK,weight='normal'):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.007,rounding_size=0.018',facecolor=fc,edgecolor=edge,linewidth=1.2)
    ax.add_patch(p)
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=fs,fontweight=weight,linespacing=1.27)

def arrow(ax, x1,y1,x2,y2,dashed=False,width=1.2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=12,linewidth=width,linestyle='--' if dashed else '-',color=BLACK))

def brain(ax,center=(0.5,0.6),w=0.36,h=0.32):
    cx,cy=center
    ax.add_patch(Ellipse((cx-w*.20,cy),w*.56,h,facecolor=LIGHT,edgecolor=BLACK,linewidth=1.3))
    ax.add_patch(Ellipse((cx+w*.20,cy),w*.56,h,facecolor=LIGHT,edgecolor=BLACK,linewidth=1.3))
    ax.plot([cx,cx],[cy-h*.42,cy+h*.42],color=BLACK,lw=1.0)
    # gyri curve segments
    for side in (-1,1):
        for hh in (0.15, 0, -0.15):
            xx=np.linspace(0,1,50)
            ax.plot(cx+side*(w*.09 + w*.10*xx),cy+hh*h + h*.065*np.sin(2*np.pi*xx),color=GREY,lw=.8)

# Fig 2: anatomy --> physics --> signals, no overlapping text
fig=plt.figure(figsize=(10.0,4.5))
gs=fig.add_gridspec(1,3,left=0.05,right=0.96,top=0.84,bottom=0.18,wspace=0.19,width_ratios=[1.05,1.25,1.10])
A,B,C=[fig.add_subplot(gs[0,i]) for i in range(3)]
for ax in (A,B,C):ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.text(.05,.94,'From neural activity to EEG evidence',fontsize=12,fontweight='bold')
fig.text(.05,.895,'Measurements constrain the hypothesis; they do not directly reveal a new physical field.',fontsize=8.5)
A.text(.5,.97,'A  |  Neural generators',ha='center',va='top',fontweight='bold',fontsize=9.5)
# neutral head profile with electrodes, simplified schematic
A.add_patch(Ellipse((.49,.56),.61,.64,fc='#fbfbfb',ec=BLACK,lw=1.25))
brain(A,(.49,.60),.43,.27)
for x,y in [(0.25,.58),(.30,.75),(.44,.85),(.59,.83),(.72,.69),(.76,.52),(.56,.35)]:
    A.add_patch(Circle((x,y),.014,fc='white',ec=BLACK,lw=1.1))
A.text(.49,.11,'Scalp electrodes record\npotential differences',ha='center',va='center',fontsize=8.8)
B.text(.5,.97,'B  |  Forward measurement',ha='center',va='top',fontweight='bold',fontsize=9.5)
textbox(B,.08,.64,.84,.18,'Neural current distributions\n+ tissue conductivity',fs=9)
arrow(B,.50,.62,.50,.50)
textbox(B,.08,.30,.84,.18,'Reference-dependent EEG channels\n+ noise + measurement artifacts',fs=9)
B.text(.5,.13,'Inverse reconstruction is non-unique',ha='center',fontsize=8.6)
C.text(.5,.97,'C  |  Reported observables',ha='center',va='top',fontweight='bold',fontsize=9.5)
for j,t in enumerate(['Evoked potential\namplitude and latency','Oscillatory power\nand phase structure','Coupling statistics\nand model scores']):
    textbox(C,.08,.69-j*.235,.84,.17,t,fs=9)
fig.text(.05,.08,'Conceptual schematic. Neural sources, extracranial fields, and derived EEG statistics must not be treated as equivalent entities.',fontsize=8)
save(fig,'figure2_brain_measurement_chain')

# Fig 3 precise two-sided timeline
fig,ax=plt.subplots(figsize=(10.2,3.5))
fig.subplots_adjust(left=.055,right=.97,bottom=.13,top=.82)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.text(.055,.94,'A selected chronology of changing scientific claims',fontsize=12,fontweight='bold')
fig.text(.055,.885,'From a theory of experience to distinct classes of inter-brain EEG outcomes.',fontsize=8.7)
ax.plot([.045,.955],[.51,.51],color=BLACK,lw=1.5)
years=[('1981','Syntergic\ntheory'),('1987','Interhemispheric\ncorrelations'),('1992','Human\ncommunication'),('1994','Transferred\npotential'),('1997','Theory\nsynthesis'),('2008','Replication\ncritique'),('2026','Research\nreviews')]
xs=np.linspace(.105,.895,len(years))
for i,((year,desc),x) in enumerate(zip(years,xs)):
    top=i%2==0
    ax.add_patch(Circle((x,.51),.012,color=BLACK))
    ax.plot([x,x],[.53,.61] if top else [.49,.40],color=BLACK,lw=1.05)
    # place label x in own column; keep borders inside frame
    if top:
        ax.text(x,.77,year,ha='center',va='center',fontsize=11,fontweight='bold')
        ax.text(x,.675,desc,ha='center',va='center',fontsize=8.2,linespacing=1.15)
    else:
        ax.text(x,.29,year,ha='center',va='center',fontsize=11,fontweight='bold')
        ax.text(x,.17,desc,ha='center',va='center',fontsize=8.2,linespacing=1.15)
fig.text(.055,.055,'A finding in a new endpoint class does not, without further work, replicate the 1994 waveform claim.',fontsize=8)
save(fig,'figure3_historical_timeline')

# Fig 5 experimental audit; clean three-column layout and separated risk channels
fig,ax=plt.subplots(figsize=(10.1,5.5))
fig.subplots_adjust(left=.04,right=.97,bottom=.09,top=.84)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.text(.045,.945,'Experimental isolation: a measurable property, not a room label',fontsize=12,fontweight='bold')
fig.text(.045,.893,'Proposed prospective apparatus audit; the diagram does not reconstruct undocumented 1994 wiring.',fontsize=8.6)
# three distinct bounded zones
for x,w,title in [(.04,.30,'SENDER ROOM'),(.37,.26,'CONTROL / TIMING'),(.66,.30,'RECEIVER ROOM')]:
    ax.add_patch(Rectangle((x,.35),w,.54,fill=False,edgecolor=BLACK,lw=1.35))
    ax.text(x+w/2,.825,title,ha='center',fontsize=10,fontweight='bold')
brain(ax,(.14,.685),.145,.112);brain(ax,(.77,.685),.145,.112)
ax.text(.23,.69,'A',fontsize=10,fontweight='bold');ax.text(.86,.69,'B',fontsize=10,fontweight='bold')
textbox(ax,.075,.50,.23,.12,'Stimulus with\nverified onset',fs=9)
textbox(ax,.075,.37,.23,.09,'Isolated EEG unit A',fs=8.6)
textbox(ax,.695,.50,.23,.12,'No assigned\nvisual stimulus',fs=9)
textbox(ax,.695,.37,.23,.09,'Isolated EEG unit B',fs=8.6)
textbox(ax,.395,.64,.21,.13,'Randomized\nevent schedule',fs=9)
textbox(ax,.395,.46,.21,.13,'Clock and\nlogging audit',fs=9)
# noncrossing arrows x1->x2
arrow(ax,.395,.70,.315,.56)
arrow(ax,.305,.42,.395,.51)
arrow(ax,.695,.42,.605,.51)
ax.text(.5,.315,'No shared sensor ground assumed',ha='center',fontsize=8)
# risk channel checklist below
ax.text(.05,.27,'Instrument and environment audit checklist',fontsize=9.8,fontweight='bold')
labels=['Acoustic / optical','Vibration / EM','Ground / clock','Event-label leakage']
for j,lab in enumerate(labels):
    x=.05+j*.235
    textbox(ax,x,.125,.21,.09,lab,fs=8.6)
fig.text(.045,.035,'All paths must be measured or bounded; evidence of a residual response would not by itself establish its mechanism.',fontsize=8)
save(fig,'figure5_apparatus_audit')

# Fig 9 labs and analytic safeguards separate elements
fig,ax=plt.subplots(figsize=(10.0,4.7))
fig.subplots_adjust(left=.04,right=.97,bottom=.12,top=.82)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.text(.045,.94,'Prospective replication across independent laboratories',fontsize=12,fontweight='bold')
fig.text(.045,.888,'Shared protocol. Independent acquisition. Locked analysis. Explicit failure states.',fontsize=8.7)
labxs=[.045,.355,.665]
for lab,x in zip(('LAB A','LAB B','LAB C'),labxs):
    ax.add_patch(FancyBboxPatch((x,.50),.285,.39,boxstyle='round,pad=0.006,rounding_size=.025',ec=BLACK,fc=PALE,lw=1.3))
    ax.text(x+.1425,.833,lab,ha='center',fontsize=10,fontweight='bold')
    # pair icons on their own row
    brain(ax,(x+.095,.705),.075,.065)
    brain(ax,(x+.195,.705),.075,.065)
    ax.text(x+.1425,.606,'Independent EEG systems',ha='center',fontsize=8.5)
    ax.text(x+.1425,.554,'Measured shielding and clocks',ha='center',fontsize=8.4)
    arrow(ax,x+.1425,.49,x+.1425,.40)
# separate three paths join at a horizontal bus
ax.plot([.188,.808],[.38,.38],color=BLACK,lw=1.3)
arrow(ax,.50,.38,.50,.30)
textbox(ax,.33,.15,.34,.13,'Blinded event and metadata escrow\n+ independent analysis container',fs=8.8,weight='bold')
fig.text(.045,.055,'Declare one confirmatory endpoint in advance; publish null, positive, and inconclusive outcomes with full provenance.',fontsize=8)
save(fig,'figure9_multilab_protocol')

print('Regenerated 4 figures')
