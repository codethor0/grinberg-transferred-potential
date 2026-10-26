import os, math, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Rectangle, PathPatch, Polygon
from matplotlib.path import Path
from scipy.stats import t

from pathlib import Path
OUT=Path(__file__).resolve().parent / 'generated' / 'base'
OUT.mkdir(parents=True, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({
    'font.family':'DejaVu Sans',
    'font.size':9,
    'axes.spines.top':False,
    'axes.spines.right':False,
    'pdf.fonttype':42,
    'savefig.facecolor':'white'
})

def save(fig, name):
    fig.tight_layout()
    fig.savefig(f'{OUT}/{name}.png', dpi=240, bbox_inches='tight')
    fig.savefig(f'{OUT}/{name}.pdf', bbox_inches='tight')
    plt.close(fig)

def box(ax, xy, w, h, txt, fs=9, fc='#f7f7f7', ec='black', lw=1.2, weight='normal', rounding=0.02):
    p = FancyBboxPatch(xy, w, h, boxstyle=f'round,pad=0.008,rounding_size={rounding}', linewidth=lw, edgecolor=ec, facecolor=fc)
    ax.add_patch(p)
    ax.text(xy[0]+w/2, xy[1]+h/2, txt, ha='center', va='center', fontsize=fs, fontweight=weight, linespacing=1.25)
    return p

def arrow(ax, x1,y1,x2,y2, style='->', dash=False, lw=1.2, ms=13):
    a=FancyArrowPatch((x1,y1),(x2,y2), arrowstyle=style, mutation_scale=ms, color='black', lw=lw, linestyle='--' if dash else '-')
    ax.add_patch(a)
    return a

def add_brain(ax, center=(0.25,0.5), width=0.24, height=0.18, face='#efefef'):
    cx, cy = center
    left = Ellipse((cx - width*0.18, cy), width*0.52, height, facecolor=face, edgecolor='black', lw=1.2)
    right = Ellipse((cx + width*0.18, cy), width*0.52, height, facecolor=face, edgecolor='black', lw=1.2)
    ax.add_patch(left); ax.add_patch(right)
    # midline
    ax.plot([cx, cx], [cy-height*0.45, cy+height*0.45], color='black', lw=1.0)
    # gyri-like arcs
    for side in [-1,1]:
        for frac in [-0.25, 0.0, 0.25]:
            theta = np.linspace(-1.0, 1.0, 80)
            x = cx + side*width*0.18 + side*0.15*width*np.cos(theta)*0.55
            y = cy + frac*height + 0.13*height*np.sin(theta)
            ax.plot(x, y, color='#6b6b6b', lw=0.8)
    return (left,right)

# Figure 1: conceptual layers improved
fig, ax = plt.subplots(figsize=(9.0,4.6))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
add_brain(ax, center=(0.14,0.70), width=0.18, height=0.18, face='#f1f1f1')
ax.text(0.14,0.49,'Observed neural dynamics\n(measured EEG, ERP, spectra)', ha='center', va='center', fontsize=9)
box(ax,(0.25,0.59),0.20,0.22,'Neuronal integration\nand coordinated activity', fs=9, fc='#fbfbfb')
box(ax,(0.51,0.59),0.18,0.22,'Proposed\n"neuronal field"', fs=9, fc='#efefef')
box(ax,(0.75,0.59),0.18,0.22,'Proposed space-time\n"lattice"', fs=9, fc='#efefef')
box(ax,(0.38,0.15),0.24,0.17,'Conscious experience\n(explanandum)', fs=10, fc='#fbfbfb', weight='bold')
arrow(ax,0.21,0.70,0.25,0.70)
arrow(ax,0.45,0.70,0.51,0.70,dash=True)
arrow(ax,0.69,0.70,0.75,0.70,dash=True)
arrow(ax,0.60,0.59,0.56,0.32,dash=True)
arrow(ax,0.35,0.59,0.44,0.32,dash=True)
ax.text(0.03,0.08,'Solid links: operationally tied to measurement. Dashed links: theoretical extensions not independently established by the EEG record.', fontsize=8)
ax.text(0.03,0.94,'Syntergic Theory separates an empirical signal layer from a stronger interpretive layer.', fontsize=10, fontweight='bold')
save(fig,'figure1_syntergic_theory')

# Figure 2: brain-to-EEG measurement chain
fig, ax = plt.subplots(figsize=(9.0,4.8))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
# Head outline
head = Ellipse((0.24,0.55),0.22,0.36,facecolor='#fafafa',edgecolor='black',lw=1.3)
ax.add_patch(head)
# neck
ax.add_patch(Rectangle((0.205,0.28),0.07,0.07,facecolor='#fafafa',edgecolor='black',lw=1.0))
# brain inside
add_brain(ax, center=(0.24,0.58), width=0.15, height=0.14, face='#e8e8e8')
# electrodes
for dx, dy in [(-0.07,0.08),(-0.03,0.12),(0.02,0.13),(0.06,0.09),(-0.06,0.02),(-0.01,0.05),(0.04,0.05),(0.07,0.01),(-0.03,-0.03),(0.02,-0.03)]:
    ax.add_patch(Circle((0.24+dx,0.58+dy),0.006,fc='white',ec='black',lw=0.9))
# arrows and boxes
box(ax,(0.39,0.70),0.21,0.16,'Large-scale cortical\nsynchronization', fs=10)
box(ax,(0.39,0.47),0.21,0.16,'Extracellular fields and\nvolume conduction', fs=10)
box(ax,(0.39,0.24),0.21,0.16,'Scalp potential differences\n(reference dependent)', fs=10)
box(ax,(0.70,0.47),0.24,0.22,'Recorded observables\nERP latency\nBand-limited power\nPhase metrics\nConnectivity estimates', fs=9, fc='#f7f7f7', weight='bold')
arrow(ax,0.32,0.72,0.39,0.78)
arrow(ax,0.32,0.58,0.39,0.55)
arrow(ax,0.32,0.44,0.39,0.32)
arrow(ax,0.60,0.78,0.70,0.58)
arrow(ax,0.60,0.55,0.70,0.58)
arrow(ax,0.60,0.32,0.70,0.58)
ax.text(0.05,0.90,'A modern translation of the theory starts from how distributed neural activity becomes a scalp measurement.', fontsize=10, fontweight='bold')
ax.text(0.05,0.08,'Key caution: EEG is a measurement model, not a direct readout of an arbitrary new field.', fontsize=8)
save(fig,'figure2_brain_measurement_chain')

# Figure 3: historical timeline
fig, ax = plt.subplots(figsize=(10.0,2.7))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
ax.plot([0.05,0.95],[0.50,0.50], color='black', lw=1.4)
pts=[(0.10,'1981','Syntergic theory\nconsciousness paper'),(0.24,'1987','Interhemispheric\ncommunication patterns'),(0.40,'1992','Human communication\nand brain activity'),(0.56,'1994','Transferred potential\nclaim in Physics Essays'),(0.70,'1997','Theory synthesis\nand terminology'),(0.82,'2008','Ambach replication\nand critique'),(0.93,'2026','Critical reviews\nand reappraisals')]
for i,(x,yr,txt) in enumerate(pts):
    ax.add_patch(Circle((x,0.50),0.015,fc='black'))
    y=0.77 if i%2==0 else 0.22
    arrow(ax,x,0.50,x,y-0.06 if y>0.5 else y+0.06,style='-')
    box(ax,(x-0.07,y-0.10),0.14,0.16,f'{yr}\n{txt}', fs=8.5, fc='#f8f8f8')
ax.text(0.05,0.93,'The claim shifted from theory-building to several non-equivalent empirical endpoints over time.', fontsize=10, fontweight='bold')
ax.text(0.05,0.04,'A positive result in a later endpoint class does not automatically reproduce the 1994 isolated-recipient waveform claim.', fontsize=8)
save(fig,'figure3_historical_timeline')

# Figure 4: endpoint taxonomy
fig, ax = plt.subplots(figsize=(9.0,4.5))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
box(ax,(0.05,0.69),0.18,0.16,'Randomized\nsender stimulus', fs=10, weight='bold')
box(ax,(0.31,0.69),0.18,0.16,'Sender\nevoked response', fs=10)
box(ax,(0.56,0.75),0.22,0.14,'Hypothesized receiver ERP\n1994-style waveform target', fs=8.2)
box(ax,(0.58,0.58),0.18,0.12,'Receiver power /\nphase statistic', fs=9)
box(ax,(0.58,0.40),0.18,0.12,'Inter-brain synchrony\n/coherence', fs=9)
box(ax,(0.58,0.22),0.18,0.12,'Classifier accuracy /\nmultivariate score', fs=9)
box(ax,(0.82,0.42),0.14,0.18,'Non-equivalent\noutcomes', fs=10, fc='#f0f0f0', weight='bold')
arrow(ax,0.23,0.77,0.31,0.77)
for y in [0.82,0.64,0.46,0.28]:
    arrow(ax,0.49,0.77,0.56 if y==0.82 else 0.58,y,dash=True)
arrow(ax,0.76,0.48,0.82,0.51)
ax.text(0.05,0.92,'Endpoint taxonomy: later studies often tested related but different receiver-side quantities.', fontsize=10, fontweight='bold')
ax.text(0.05,0.06,'Replication requires matching the estimand, not just reporting any statistically unusual sender–receiver relation.', fontsize=8)
save(fig,'figure4_endpoint_taxonomy')

# Figure 5: apparatus audit
fig, ax = plt.subplots(figsize=(9.3,5.0))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
# rooms
roomA = Rectangle((0.05,0.18),0.32,0.60,fill=False,ec='black',lw=1.4)
roomB = Rectangle((0.63,0.18),0.32,0.60,fill=False,ec='black',lw=1.4)
ax.add_patch(roomA); ax.add_patch(roomB)
ax.text(0.21,0.81,'ROOM A',ha='center',fontsize=10,fontweight='bold')
ax.text(0.79,0.81,'ROOM B',ha='center',fontsize=10,fontweight='bold')
# person / brain icons
add_brain(ax, center=(0.17,0.57), width=0.11, height=0.09)
add_brain(ax, center=(0.75,0.57), width=0.11, height=0.09)
box(ax,(0.10,0.31),0.14,0.10,'Stimulus screen\n+ photodiode', fs=8.5)
box(ax,(0.24,0.31),0.10,0.10,'EEG amp A', fs=8.5)
box(ax,(0.68,0.31),0.10,0.10,'No deliberate\nstimulus', fs=8.5)
box(ax,(0.80,0.31),0.10,0.10,'EEG amp B', fs=8.5)
box(ax,(0.42,0.56),0.16,0.12,'Randomization /\nevent service', fs=9, fc='#f7f7f7')
box(ax,(0.42,0.34),0.16,0.10,'Clock sync /\nlogging', fs=8.5, fc='#f7f7f7')
arrow(ax,0.24,0.36,0.42,0.61)
arrow(ax,0.58,0.61,0.80,0.36)
arrow(ax,0.21,0.53,0.24,0.41)
arrow(ax,0.75,0.53,0.80,0.41)
# leakage channels dashed
for (x1,y1,x2,y2,lbl,tx,ty) in [
    (0.37,0.67,0.63,0.67,'acoustic / vibration',0.50,0.71),
    (0.34,0.50,0.66,0.50,'electromagnetic / ground',0.50,0.54),
    (0.34,0.25,0.66,0.25,'experimenter / timing leakage',0.50,0.29)
]:
    arrow(ax,x1,y1,x2,y2,dash=True,lw=1.0)
    ax.text(tx,ty,lbl,ha='center',fontsize=8)
ax.text(0.05,0.92,'Isolation is not established by room labels alone; each potential path must be measured or bounded.', fontsize=10, fontweight='bold')
ax.text(0.05,0.06,'This is a proposed audit schematic, not a claim that the historical setup necessarily contained these specific paths.', fontsize=8)
save(fig,'figure5_apparatus_audit')

# Figure 6: causal, measurement, and analysis relationships
fig, ax = plt.subplots(figsize=(10.0,5.2))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
node_pos = {
    'S':(0.11,0.72),'X':(0.32,0.72),'Y':(0.72,0.72),
    'L':(0.50,0.44),'Z':(0.50,0.16),'A':(0.83,0.44),'T':(0.83,0.16)
}
labels = {
    'S':'Stimulus\nschedule S','X':'Sender EEG X','Y':'Receiver EEG Y',
    'L':'Leakage / latent\ncommon causes L',
    'Z':'Measured proxy Z\nEM, sound, timing, motion',
    'A':'Analysis choices A\npreprocessing and windows',
    'T':'Derived statistic T\ncomputed from X, Y, S, Z'
}
for k,(x,y) in node_pos.items():
    fc = '#f0f0f0' if k in ('L','A','Z','T') else '#fafafa'
    box(ax,(x-0.10,y-0.06),0.20,0.12,labels[k],fs=8.4,fc=fc)
arrow(ax,0.21,0.72,0.22,0.72)
arrow(ax,0.42,0.72,0.62,0.72,dash=True)
arrow(ax,0.16,0.66,0.44,0.47,dash=True)
arrow(ax,0.44,0.50,0.36,0.66,dash=True)
arrow(ax,0.56,0.50,0.66,0.66,dash=True)
arrow(ax,0.50,0.38,0.50,0.22)
arrow(ax,0.83,0.38,0.83,0.22)
arrow(ax,0.60,0.16,0.73,0.16)
ax.text(0.52,0.79,'hypothesized target association',fontsize=8)
ax.text(0.25,0.54,'stimulus-locked leakage',fontsize=8,ha='center')
ax.text(0.34,0.61,'competing paths',fontsize=8,ha='center')
ax.text(0.51,0.30,'measurement',fontsize=8,ha='left')
ax.text(0.04,0.93,'Causal hypotheses, measurement proxies, and analysis choices must not be conflated.', fontsize=10, fontweight='bold')
ax.text(0.04,0.05,'Dashed edges mark hypothesized or competing paths. Controls constrain alternatives only when measured and linked to the analysis.', fontsize=8)
save(fig,'figure6_identifiability')

# Figure 7: synthetic FPR (reuse)
rng=np.random.default_rng(20261025);FS=256;T=128;RUNS=5000
records=[]
for low,high in ((13,35),(4,12)):
    freq=np.fft.rfftfreq(T,1/FS); mask=(freq>=low)&(freq<=high)
    a=rng.normal(size=(RUNS,T));b=rng.normal(size=(RUNS,T))
    af=np.fft.rfft(a,axis=-1)*mask;bf=np.fft.rfft(b,axis=-1)*mask
    axsig=np.fft.irfft(af,n=T,axis=-1); by=np.fft.irfft(bf,n=T,axis=-1)
    axsig-=axsig.mean(axis=1,keepdims=True);by-=by.mean(axis=1,keepdims=True)
    axsig/=np.linalg.norm(axsig,axis=1,keepdims=True);by/=np.linalg.norm(by,axis=1,keepdims=True)
    r=np.sum(axsig*by,axis=1)
    pnaive=2*t.sf(np.abs(r)*np.sqrt((T-2)/(1-r*r)),T-2)
    cc=np.fft.irfft(np.conjugate(np.fft.rfft(axsig,axis=1))*np.fft.rfft(by,axis=1),n=T,axis=1)
    pc=np.mean(np.abs(cc)>=np.abs(cc[:,0:1])-1e-12,axis=1)
    records.append((f'{low}-{high} Hz',100*np.mean(pnaive<.05),100*np.mean(pc<=.05)))
fig,ax=plt.subplots(figsize=(8.5,4.2))
xx=np.arange(2);w=.32
bars1=ax.bar(xx-w/2,[r[1] for r in records],w,facecolor='#5a5a5a',label='Naive t-test (128 assumed independent samples)')
bars2=ax.bar(xx+w/2,[r[2] for r in records],w,facecolor='white',edgecolor='black',hatch='////',label='Circular-shift calibration')
ax.axhline(4.6875,color='black',lw=1,ls='--',label='Exact shift-test size: 4.69%')
ax.set_xticks(xx,[r[0] for r in records]);ax.set_ylim(0,75);ax.set_ylabel('False-positive rate (%)')
ax.spines['left'].set_visible(True);ax.spines['bottom'].set_visible(True)
ax.legend(loc='upper center',bbox_to_anchor=(0.5,1.25),fontsize=8,frameon=False,ncol=1)
for bars in (bars1,bars2):
    for b in bars:
        ax.text(b.get_x()+b.get_width()/2,b.get_height()+1.7,f'{b.get_height():.2f}%',ha='center',fontsize=8)
ax.set_title('Synthetic null benchmark: miscalibration after band-limiting independent signals', fontsize=10, pad=72)
save(fig,'figure7_synthetic_fpr')
with open(f'{OUT}/figure7_results.json','w') as f: json.dump(records,f)

# Figure 8: reanalysis pipeline
fig, ax = plt.subplots(figsize=(9.2,4.8))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
steps=[
    (0.03,0.64,0.19,0.16,'1  Provenance'),
    (0.27,0.64,0.19,0.16,'2  Preregistration\n+ endpoint lock'),
    (0.51,0.64,0.19,0.16,'3  Locked\npreprocessing'),
    (0.75,0.64,0.19,0.16,'4  QC + event\nvalidation'),
    (0.75,0.32,0.19,0.16,'5  Calibrated\ninference'),
    (0.51,0.32,0.19,0.16,'6  Sensitivity\n+ failure gates'),
    (0.27,0.32,0.19,0.16,'7  Report\n+ archive')
]
for x,y,w,h,txt in steps:
    box(ax,(x,y),w,h,txt,fs=9)
for a,b in [
    ((0.22,0.72),(0.27,0.72)),
    ((0.46,0.72),(0.51,0.72)),
    ((0.70,0.72),(0.75,0.72)),
    ((0.845,0.64),(0.845,0.48)),
    ((0.75,0.40),(0.70,0.40)),
    ((0.51,0.40),(0.46,0.40))
]:
    arrow(ax,*a,*b)
box(ax,(0.04,0.07),0.91,0.12,'Adversarial checks throughout: timing drift, leakage proxies, artifact imbalance,\nmultiple-comparison inflation, and label leakage.',fs=8.8,fc='#f0f0f0')
ax.text(0.04,0.93,'Retrospective reanalysis should move from provenance to inference through a locked, auditable pipeline.', fontsize=10, fontweight='bold')
save(fig,'figure8_reanalysis_pipeline')

# Figure 9: multilab protocol
fig, ax = plt.subplots(figsize=(9.5,4.8))
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
for i,x in enumerate([0.05,0.36,0.67], start=1):
    box(ax,(x,0.52),0.24,0.28,f'Lab {i}\nSender–receiver chambers\nMatched hardware\nShielding and monitoring',fs=9.5)
    add_brain(ax, center=(x+0.08,0.60), width=0.07, height=0.05)
    add_brain(ax, center=(x+0.17,0.60), width=0.07, height=0.05)
box(ax,(0.36,0.18),0.28,0.14,'Central preregistration\n+ blinded randomization service',fs=9.5,fc='#f7f7f7',weight='bold')
box(ax,(0.36,0.01),0.28,0.12,'Independent analysis container\nlocked before unblinding',fs=9.2,fc='#f7f7f7')
for x in [0.17,0.48,0.79]:
    arrow(ax,x,0.52,0.50,0.32)
arrow(ax,0.50,0.18,0.50,0.13)
ax.text(0.05,0.93,'Prospective replication is strongest when multiple labs share hardware standards, blind labels, and an identical decision rule.', fontsize=10, fontweight='bold')
ax.text(0.05,0.41,'Cross-site agreement matters more than a single striking dataset.', fontsize=8)
save(fig,'figure9_multilab_protocol')

print('Figures written to', OUT)
