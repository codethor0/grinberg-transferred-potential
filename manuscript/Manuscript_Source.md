---
title: Reassessing the Transferred-Potential Hypothesis
subtitle: Syntergic Theory, Isolated-Brain EEG Evidence, and Reproducible Tests
author: Thor Thor
date: October 25, 2026
lang: en-US
abstract: 'Jacobo Grinberg-Zylberbaum''s Syntergic Theory proposed that organized neural activity interacts
  with an underlying structure of space and that interpersonal interaction can leave measurable correlations
  between separated brains. The experimental claim most amenable to investigation is the *transferred
  potential*: a stimulus-locked electroencephalographic response in an unstimulated participant while
  a separated partner receives visual stimulation. This article reconstructs that claim, distinguishes
  it from later studies of receiver-side power, inter-brain synchrony, neuroimaging changes, and machine-learning
  classification, and assesses the conditions required for independent replication. The review draws on
  original publications, a facsimile of the 1994 report, methodological critiques, later experiments,
  and recent syntheses. It is a source-traced critical review, not a formally exhaustive systematic review.
  The available record does not establish a robustly replicated isolated-recipient evoked waveform or
  a new physical communication channel. Key limitations include incomplete raw-data provenance, unresolved
  event timing, analytical flexibility, and insufficiently constrained instrumental or environmental paths.
  To illustrate one statistical vulnerability, we executed a fully synthetic null benchmark containing
  5,000 independent pairs of 128-sample signals per frequency condition. Naive Pearson tests yielded false-positive
  rates of 43.28% (13–35 Hz) and 62.06% (4–12 Hz); circular-shift calibration yielded 4.54% and 5.08%.
  These values describe simulated signals, not historical recordings or human EEG. We propose a reproducible
  reanalysis workflow and a prospective, preregistered multi-laboratory protocol with explicit controls
  for physical leakage, statistical dependence, and machine-learning data leakage. A surviving receiver-side
  association would justify further investigation but would not, on its own, establish a pre-space structure,
  entanglement, or a nonclassical transmission mechanism.'
keywords: Syntergic Theory; Grinberg-Zylberbaum; transferred potential; EEG; replication; statistical
  dependence; signal leakage; synthetic null simulation; open science
---

**Author affiliation:** Independent Open-Source Researcher  
**ORCID:** 0009-0001-6573-385X  
**Research coverage:** Primary literature and indexed reviews available through October 25, 2026  
**Article type:** Critical methodological review with an original synthetic demonstration and proposed replication protocol  
**Data declaration:** No new human-subject recordings were collected or analyzed for this manuscript.  
**Code declaration:** Synthetic benchmark code, seed, and environment assumptions are provided in Appendix A.  
**Research transparency:** Journal peer review has not occurred. An independent adversarial scientific audit informed the present text. Review sources and computational claims are distinguished from hypotheses and recommendations.  
**Keywords:** Syntergic Theory; Grinberg-Zylberbaum; transferred potential; EEG; replication; statistical dependence; signal leakage; synthetic null simulation; open science

# 1. The Question Behind the Claim

A brain creates measurable electrical activity. That observation is not controversial. Whether a pattern in one brain can generate a detectable, stimulus-locked response in another person's brain when familiar sensory and technical channels are excluded is a much narrower and considerably harder question. Jacobo Grinberg-Zylberbaum's work brought these two propositions into the same experimental program. His theoretical writing addressed how coordinated neuronal activity could give rise to experience; his later work attempted to connect the theory to electrophysiological responses in separate people. The most cited assertion was that an electrical potential evoked by flashes in one participant could be seen in the averaged EEG of an unstimulated partner located in another chamber [1–5].

This distinction determines the scope of the present inquiry. The existence of scalp potentials, neural oscillations, and sensory-linked synchrony does not validate the transferred-potential claim. Conversely, an unsuccessful replication of the transferred potential does not by itself resolve the nature of conscious experience. The claims sit at different levels of explanation, require different observations, and have different falsification conditions. Treating them as one thesis makes the historical record difficult to assess and makes future testing unnecessarily ambiguous.

Three questions guide this paper. First, what did the original researchers measure and report, without importing later reconstructions or a preferred mechanism? Second, do independent findings establish a recipient-side response of the same experimental kind? Third, what would an experiment or computational analysis need to rule out before a residual response could be accepted as a physiological phenomenon requiring explanation? These questions are answered through a source-traced review, an illustrative synthetic statistical benchmark, and a concrete experimental design. The paper does not attempt to establish or disprove every possible philosophical theory of consciousness.

The central conclusion is restrained: the published record contains unusual reported correlations, but not a robustly replicated isolated-recipient evoked response under controls sufficient to identify an unknown inter-brain pathway. The appropriate next step is neither to canonize the original interpretation nor to declare all anomalous measurements impossible. It is to fix the target observation and its error model, then make failure and success equally informative.

# 2. Scope, Evidence Handling, and Review Method

## 2.1. A source-traced critical review, not a PRISMA systematic review

This manuscript draws on the primary publications associated with Grinberg's theory and EEG reports (1981, 1987, 1992, 1994, and 1997), selected replications and conceptual follow-ups, methodological work on EEG, signal dependence, and reproducibility, and contemporary systematic or descriptive reviews. We reconciled supplied research dossiers against publisher pages, PubMed records, and source material when available. In particular, the 1994 *Physics Essays* facsimile and the 1987 article were inspected directly; the later 1997 theoretical paper was available as a scanned journal article. Source-level access is not interchangeable with a secondary account of a paper.

Searches were conducted in PubMed and PubMed Central, Crossref, publisher and journal archives, F1000Research, Figshare, and the *European Journal of Parapsychology* archive during October 24–25, 2026. Search combinations included "transferred potential," "Grinberg-Zylberbaum," "separated subjects," "inter-brain EEG correlation," "evoked alpha," and methodological correlation terms. Reference lists of the primary reports, Ambach (2008), Wackermann (2004), and the 2026 reviews were followed backward and forward. This bounded search statement describes the work performed; it is not a systematic-search protocol.

The search and integration process was not prospectively registered. No complete deduplicated database export, dual-reviewer eligibility decision log, or prespecified risk-of-bias instrument was produced. Accordingly, this article is **not** labeled a PRISMA-compliant systematic review, and no pooled effect estimate is calculated for noncomparable experimental outcomes. These limitations do not prevent a focused methods analysis, but they constrain claims about exhaustive coverage and publication-bias-adjusted prevalence of effects. A complete systematic review would be a separate project with a publicly registered protocol.

A reference was used as evidence for a factual claim only when its bibliographic identity was established and relevant text or a reliable abstract could be inspected. The publisher's 1981 record gives pages 201–210, correcting a page-range error repeated in some secondary summaries [1]. The 1992 study belongs to *Subtle Energies*, volume 3, issue 3, not issue 1 [3]. The recovered 1994 article supplies substantive methods that should not be described as unknown merely because a search engine or citation index failed to retrieve the full text [4]. Such corrections illustrate why agreement among secondary summaries is not source validation.

## 2.2. Epistemic categories

Every major proposition is assigned to one of five categories. **Original assertion** identifies what an author argued. **Instrumental observation** identifies voltages or other measured quantities. **Statistical result** identifies the calculation and claimed significance. **Independent replication** identifies whether another investigation recovered the same endpoint using a comparable design. **Present proposal** identifies mathematical definitions or tests introduced here and not attributable to Grinberg. This separation prevents the common substitution of the word *entanglement* for an unexplained correlation.

Evidence labels have precise meanings. *Documented* means the cited publication contains the report, not that the effect is independently established. *Independently supported* means multiple suitable studies support the relevant ordinary phenomenon. *Not established* means the available observations do not justify the stronger conclusion. *Not presently testable* means an asserted mechanism lacks variables or distinct predictions that define a discriminating observation. *Unresolved* marks a factual gap in the accessible historical record, such as instrument wiring, timestamp provenance, or data availability.

## 2.3. The endpoint problem

The phrase "brain-to-brain correlation" covers non-equivalent estimands. A waveform in an isolated receiver with the sender's evoked-potential morphology is not the same as an increase in receiver EEG power, a covariance of time-window statistics, a small classification advantage, or social synchronization during a shared task. Even within EEG, event-related potentials, spectral coherence, phase-locking, and machine-learned features respond differently to filtering, referencing, artifacts, and selection. This paper therefore organizes historical findings by **endpoint first** and **significance second**.

# 3. Syntergic Theory: Reconstruction and Limits

## 3.1. From neural integration to an alleged structure of space

The 1981 article, *The Transformation of Neuronal Activity into Conscious Experience: The Syntergic Theory*, asks how physiological activity becomes subjective experience [1]. The later account, *Ideas About a New Psychophysiology of Consciousness: The Syntergic Theory* (1997), elaborates a "neuronal field" produced by coordinated neural activity and an underlying structure of space in which information is proposed to be distributed [5]. The 1997 article describes this substrate as a "pre-space structure" whose coherence it calls syntergy [5]. This manuscript uses "lattice" only as a shorthand for that structure, not as Grinberg's term in the texts examined. The proposal is not merely that sensory processing integrates distributed signals; it adds the claim that the field interacts with this pre-space structure, and that the interaction constitutes or shapes perceptual experience.

Two claims can be separated. The modest claim is that distributed neuronal populations integrate information and produce measurable fields through ordinary electrodynamics. That belongs to established neurophysiology, although the relationship between those measurements and phenomenology remains an open problem. The stronger claim posits a distinct, information-bearing physical substrate whose interaction with the neural field is causally necessary for conscious perception. The latter is not an established consequence of EEG, Maxwell's equations, or the observed existence of neural coherence [26–28].

Grinberg's terminology includes *syntergy*, associated with the organization, coherence, and integration of the proposed substrate and neuronal activity; *neurosyntergy*, applied to organized brain activity; and a proposed inter-individual relationship through the neuronal fields. These terms function as qualitative organizing ideas. They are not in the examined texts linked to a jointly calibrated field quantity, SI unit, coupling constant, distance law, spectral response, or Hamiltonian that would make the pre-space structure independently measurable [1,5]. A modern coherence metric may be a useful operational proxy for a restricted part of the idea, but redefining "syntergy" as a current EEG statistic would be a new model, not a recovery of the original theory.

![Conceptual reconstruction of Syntergic Theory. Measured EEG and population dynamics are distinguished from the proposed neuronal-field extension and unmeasured pre-space structure, abbreviated as "lattice" in this manuscript; dashed arrows represent theoretical rather than established physical links.](figures/figure1_syntergic_theory.png){width=90%}

## 3.2. The meaning of a neuronal field

Scalp EEG measures voltage differences arising predominantly from synchronized electrical activity in populations of cortical neurons, with important effects from volume conduction, geometry, reference choice, and non-neural sources [26]. It is reasonable to speak of extracellular electric fields and collectively generated signals in this established sense. It is not reasonable to infer from EEG alone that an additional field extends across arbitrary distances or modifies a universal informational pre-space structure. A field theory capable of that inference would need a defined state variable, a physical interaction, boundary conditions, an independently calibrated sensor response, and predictions that differ from known field models.

A useful formal distinction is between a recorded sensor vector $X(t)\in\mathbb{R}^{C}$, measured in volts or microvolts, and an unobserved physical state $Q(t)$. EEG source inversion estimates some function of intracranial current distributions from $X(t)$, under modeling assumptions; it does not identify an arbitrary hypothesized field. The inverse problem is many-to-one and sensor-level coherence can arise through common sources and referencing. These constraints matter whenever geometric language about neuronal fields is treated as direct evidence for a proposed space-time mechanism.

## 3.3. What could falsify the broader theory?

A general statement that "consciousness depends on information" has many compatible readings and few decisive tests. To be testable as physics, Syntergic Theory would need to predict at least one observable $O$ for which $P(O\mid H_{\mathrm{lattice}})$ differs from predictions under explicit non-lattice alternatives. A measured variation in ordinary neural coherence would not suffice because existing neuroscience predicts it too. A genuinely discriminating result could be a calibrated, repeatable physical effect whose magnitude, sign, and dependence on manipulated conditions are predicted independently of post hoc parameter choice. No such quantitative discriminator was established in the primary materials inspected here [1,5].

This does not render the entire research program useless. The isolated-recipient EEG prediction is concrete enough to test independently of the metaphysical explanation. If that effect fails under a sufficiently sensitive and controlled design, the particular empirical argument for nonlocal brain coupling is weakened even if the philosophical theory remains logically flexible. If an effect succeeds, one must still identify which physical or technical path produced it before claiming to have validated a lattice.


## 3.4. Translation into contemporary systems neuroscience

If Syntergic Theory is translated into modern technical language, the claim stack can be separated into four layers. The first layer is ordinary neural population dynamics: pyramidal cells synchronize over time, local and long-range circuits exchange information, and rhythmic activity can be measured in voltage differences at the scalp. The second layer is an integration layer: large-scale coordination across cortical and thalamocortical systems may help explain why perception appears unified rather than fragmentary. The third layer is a measurement layer: EEG does not image the brain directly, but records a weighted, reference-dependent projection of many sources through tissue and geometry. The fourth layer is the interpretive layer, where a researcher decides whether the measured organization is sufficiently explained by known neurophysiology or whether a new construct is needed [26,35,36].

This translation matters because Grinberg's language sometimes moves rapidly between these layers. A coherent neuronal field can mean at least three different things: the ordinary extracellular fields generated by neural populations; a systems-neuroscience shorthand for temporally coordinated activity across distributed regions; or a proposed field-like entity with causal properties not captured by conventional EEG theory. Those are not interchangeable. The first two are continuous with mainstream electrophysiology. The third is a stronger theoretical extension that requires its own measurement model, parameterization, and discriminating predictions [26,28].

A modern systems-neuroscience framing would therefore ask what, exactly, is being integrated and at what scale. Neural oscillations can couple local processing to long-range communication. Phase relationships can modulate effective connectivity. Task engagement can increase or decrease synchrony depending on the network and the behavioral demand. None of those observations imply a physically nonlocal interpersonal channel, but they do provide a precise vocabulary for restating the empirical ambition of the work: if two isolated nervous systems exhibit more coordination than expected, what statistics capture that coordination, under what manipulations, and against what null model [17,19,20,35,36]?

The measurement chain is equally important. Every quantity reported in the transferred-potential literature is downstream of choices about electrode montage, reference, filtering, epoch definition, artifact handling, averaging, and significance testing. A headline phrase such as *correlated brains* hides the fact that different studies summarized different mathematical objects. An event-related potential is a time-locked average. A power change is a spectral summary. A synchrony metric is a dependence measure. A classifier score is a prediction statistic. Treating them as one category encourages historical confusion and weakens inference [18,19,21,22,36].

For that reason, the strongest contemporary restatement of the scientific program is narrower than the original metaphysical framing. One can ask whether isolated participants show repeatable sender-linked receiver-side EEG structure that survives instrument controls and calibrated nulls, without assuming that any positive result would validate a lattice-like theory of reality. This narrower program is difficult enough to test rigorously. It also has the advantage of being falsifiable, because the measurement target, the confound model, and the decision rules can all be written down in advance [22,31,32,37].

![Neural generators, EEG forward measurement, and derived observables. The conceptual drawing is not a source-localization result: scalp potentials are indirect, reference-dependent measurements of neural activity.](figures/figure2_brain_measurement_chain.png){width=92%}

# 4. The Original Experimental Record

## 4.1. The 1987 communication study

Grinberg-Zylberbaum and Ramos analyzed interhemispheric EEG correlation patterns during conditions designed to encourage interpersonal communication [2]. In that study, 13 pairs sat about 50 cm apart in the same sound-proof Faraday cage. Interhemispheric correlations were computed over 64-sample, 256 ms windows, and judges compared the resulting patterns. The publication is relevant because it shows the laboratory's interest in patterns formed from multiple correlations rather than only from evoked waveforms. Its conclusions were framed as support for the theoretical account, but the reported association is not a controlled demonstration of communication across physically isolated rooms, still less a test of quantum entanglement.

The distinction between a subject's *interhemispheric pattern* and a correlation *between two independent brains* must not be lost. Two subjects can each show ordinary fluctuations in network organization and produce visually similar summary plots without a directed interaction. If time windows overlap or electrodes are reused across pairwise correlations, the resulting coefficients are not independent observations. Modern statistical analysis would evaluate effects at the participant or dyad level, use suitable null surrogates, and quantify whether condition differences generalize to new pairs.

## 4.2. Earlier and later reports from the same laboratory

The 1994 article identifies its immediate antecedent as a study in which an evoked potential was reported as transferred between participants in two Faraday chambers about 3 m apart, and describes the 14.5 m study as a replication of that experiment [4]. Its reference list identifies that study as Grinberg-Zylberbaum, Delaflor, and Sánchez (1989) in the *Revista Intercontinental de Psicología y Educación* [39]. The 1992 *Subtle Energies* paper [3] also reports an evoked-like response in a separated, nonstimulated participant after interaction; its archive abstract mentions electromagnetically isolated chambers but not their separation.

The 1997 article cites further reports in the same series: a 1982 study described as the first experiment of the series, a 1995 study of transferred-potential topography in the *Revista Mexicana de Psicología*, and a 1996 UNAM thesis by Attie on EEG topography and the transferred potential [5,40–42]. None of these Spanish-language reports was inspected for this manuscript. Their bibliographic details come from the reference lists of [4], [5], and May et al. (2010), which differ in some details [38]. They are not independent replications because investigators, assumptions, and apparatus overlap, but they may contain methods, counts, or topographic data bearing directly on the 1994 claim. The 1995 report may be the full-scalp mapping that the 1994 article announced as planned. These reports are priority targets for archival retrieval. An increase in separation from about 3 m to 14.5 m within one program is not equivalent to an independently randomized between-laboratory replication.

## 4.3. The 1994 report: what is actually specified

The 1994 article reports **seven pairs** of participants, ages **20–44**, tested in two Faraday chambers separated by **14.5 m** [4]. EEG was recorded at O1 and O2 with a reference on the tip of the nose. The sender chamber used a **Beckman polygraph** and the receiver chamber a **Grass polygraph**. The article describes digitization in each chamber and **two AT computers of different makes**. These details are inconsistent with descriptions of the historical setup as a single shared analog-to-digital converter or a common EEG computer. Common electrical paths remain possible in principle, but the text does not demonstrate their existence.

The sender received **100 flashes** at intervals reported as **2–5 seconds**, while the receiver was not deliberately stimulated. Two main conditions were distinguished: recordings before the participants had met and recordings after a 20-minute period of interpersonal interaction and meditative silence. The conditions differed in more than prior interaction. In Condition 1 the participants had not met and did not know that a partner was in the other chamber; in Condition 2 they had just meditated together and the receiver was instructed to maintain direct communication. Condition 2 also followed Condition 1 in time. Expectancy, instruction, arousal, vigilance, fatigue, and time on task therefore covary with the interaction manipulation and cannot be separated from it in this design.

In the post-interaction condition, the flashes were delivered by a Grass photostimulator "on maximum power" [4]. A photic stimulator of this kind discharges stored energy through a flash tube at each flash. Whether the resulting electrical and acoustic transients were attenuated below detectability at the receiver amplifier is not documented. This is a concrete, stimulus-locked candidate path, not a demonstrated one. The methods describe a blind Control B consisting of 100 EEG samples "under stimulus but without a subject in the stimulation chamber", the arrangement most directly relevant to stimulator leakage. The results and figures present outcomes only for the no-interaction condition, the absence of a distinct sender response, and no stimulation. No trace, coefficient, or numerical outcome is shown for Control B; its result is conveyed only by the general statement that control subjects showed no transferred potentials.

The article also describes no-flash sampling. It states that saturated epochs were automatically rejected and also claims that no arbitrary epochs were removed. A reader should not silently turn this into "no artifacts were rejected"; the apparent tension is resolved only by inspecting the exact rejection code and trial logs, neither of which accompanies the publication.

The paper gives analog filtering around **5.3–35 Hz** and also describes digital removal of components below **12.7 Hz**. It reports moving-window Pearson correlations between the averaged sender and receiver signals, and mentions spectral analysis and $t$ tests. Each average contained 64 points, as indicated by "Puntos: 64" in the figure panels. Pearson correlations were computed over windows of 16 consecutive points, shifted one point at a time; the authors report 48 correlations per pair of averages, although a one-point shift over 64 points permits 49 [4]. Each coefficient therefore rests on 16 serially dependent, band-limited values, and adjacent windows share 15 of their 16 points. The printed probabilities are numerically consistent with a conventional test treating the 16 points as independent: for $n=16$, $r=0.70$ gives a two-sided nominal $p$ of about 0.0025 and $r=0.62$ about 0.010 by our calculation. The article does not state which test was used.

The printed sampling interval of 8 units, window length of 128 units, and epoch of 512 units are mutually consistent with 64 points per epoch under either unit. The figure captions show waveforms on a **0–512 ms** axis, but nearby method text uses microsecond-like symbols for epoch durations, sampling intervals, and correlation shifts. Those statements are internally incompatible if read literally. The laboratory's 1987 article reports sampling "every four ms" [2], so millisecond usage was established in the group's earlier work. This makes a millisecond reading more plausible, but it does not justify silently replacing the printed symbols, inferring a sample rate, or claiming to reconstruct the original temporal resolution. The uncertainty requires original acquisition records or direct author-level clarification [4].

| Feature | Explicit in the 1994 paper | Status for present audit |
|:--|:--|:--|
| Sample | Seven pairs; adults aged 20–44 | Documented; about 25% judged successful, count not given; underpowered and conditionally selected |
| Physical separation | Two Faraday chambers; 14.5 m | Documented distance; measured attenuation curves unavailable |
| Recording | O1/O2, nose reference; different polygraphs; two AT computers | Documented; cable/ground topology not established |
| Stimulation | 100 flashes from a Grass photostimulator at maximum power; reported 2–5 s spacing | Documented; device transients and full event log unavailable |
| Experimental comparison | Before and after interpersonal interaction | Documented; fixed order and psychological differences confound the contrast |
| Controls | No-stimulation control; flashes with empty sender chamber (Control B) | Documented in methods; Control B outcome not shown; calibration traces unavailable |
| Signal processing | Analog filtering and digital exclusion of low frequencies | Documented, but exact implementation and effective passband unresolved |
| Inference | Sixteen-point correlations; 48 reported overlapping windows per average pair | Documented analytical strategy; one-point shifts permit 49 windows; full multiplicity not recoverable |
| Data provenance | No public raw epoch files or complete hardware logs located | Unresolved, not proof that records no longer exist |

**Table 1.** The principal source-level facts and limits of the original apparatus. Missing technical details are not replaced with assumptions about historical hardware.

## 4.4. Reported waveforms and the reported success proportion

The reported transferred potentials were conditional on a sequence of judgments. First, the interaction had to be "deemed successful". The methods state that about 25% of subject pairs attained the intended "direct communication", and the results describe success in "about one in four cases" [4]. The article does not state who made this judgment, by what criterion, or whether it was recorded before the EEG averages were inspected. The later theoretical paper describes the criterion as participants' verbal reports and a self-rating of empathic communication from 0 to 10, and states that transferred potentials occur "if and only if" interaction succeeded, the stimulated participant showed evident evoked potentials, and outside interference was absent [5]. Second, the stimulated participant's average had to show a "distinct evoked potential", a visual judgment for which no amplitude or morphology criterion is given. Third, the published examples are O2 traces, and the authors note that O2 seemed to give the clearer transferred potential.

If "about 25%" refers to the seven pairs, it corresponds to roughly two pairs. Because 25% of seven is not an integer, the denominator itself is uncertain, and no count is given. The estimand actually reported is therefore not the average receiver response across seven pairs but the receiver response within a subset defined by success, sender-response, and derivation judgments. If any of these judgments was made with knowledge of the receiver averages, the reported association between successful interaction and transferred potentials would be partly circular. The source does not allow that possibility to be confirmed or excluded.

The printed figures add a further caution. Each panel has its own ordinate scale, as the captions note. The sender averages labeled as distinct evoked potentials in Figures 1 and 2 stay within about 0.6 microvolts in magnitude, whereas the sender average labeled as an absent evoked potential in Figure 4 spans about -0.5 to +1.0 microvolts and the receiver average without stimulation in Figure 5 spans about -0.8 to +1.25 microvolts. On the printed scales, amplitude does not separate distinct from absent responses; the distinction rests on visual judgments of morphology in averages whose residual background activity is of comparable size [4]. The investigators reported correlation coefficients between about **0.62 and 0.92**, with nominal probabilities below 0.009 or 0.005 for the early windows highlighted in the figures [4]. The proportion of successful interactions is not a population prevalence, a prespecified detection probability, or a replication rate; it describes a small, conditionally interpreted series.

The authors interpreted the effect as a macroscopic Einstein–Podolsky–Rosen (EPR) correlation and argued that ordinary transmission and chance correspondence were excluded. The instrument, however, measured scalp voltages. The statistical procedure tested resemblance between curves, not a Bell inequality, a quantum state, or a causal channel with known bandwidth. Even if the quoted correlations were numerically correct, the inference from waveform similarity to quantum nonlocality would remain unsupported.

A further issue is the unit of replication. A 512 ms waveform sampled at many adjacent instants does not give an independent subject for every point. Filtered observations are serially correlated, and overlapping moving windows reuse the same values. A nominal $t$ test calculated as if all points were independent can be badly miscalibrated. The paper's available information is not sufficient to calculate a corrected original $p$ value, because the underlying covariance structure and full analysis path are unknown. It is consequently incorrect to publish an exact revised $p$ value as though one had reanalyzed the original EEG [4,23,24].

This concern has already been examined empirically. May, Spottiswoode, and Faith (2010) followed the printed 1994 procedure with uncorrelated EEG from unrelated recordings: they filtered two records to 12.7–35 Hz, averaged 64-point segments at 100 random entry points, and computed 16-point Pearson correlations between the two averages. Under their empirical null, $r=0.70$ had a one-tailed empirical probability of about **0.0418**, whereas the conventional calculation gave about **0.0009** [38]. Their analysis does not reconstruct the original recordings and depends on their own EEG and their reading of the printed time units, but it shows that coefficients of the size printed in the 1994 figures are not rare between independent filtered averages of this length. Their nonsignificant comparison of the two conditions, $Z=1.22$, assumed zero correlation for Condition 1 because the 1994 article reports no Condition 1 coefficients. It is illustrative, not a corrected reanalysis of Grinberg's raw EEG.

## 4.5. What the source does not establish

The original record does not provide independently audited receiver-room light, sound, vibration and electromagnetic measurements, the galvanic-isolation diagram, complete timestamps, raw recordings, executable analysis code, or a preregistered definition of the primary receiver endpoint. Nor does it show the numerical result of the empty-sender-chamber control. These omissions leave alternative explanations incompletely tested. They do **not** prove that a TTL pulse entered a receiver amplifier or that the two acquisition systems used shared grounds. Those are competing hypotheses, not reconstructed historical events. The correct language is that such paths must be measured and ruled out in a new experiment.


## 4.6. Historical drift in what counted as evidence

The historical record is easier to understand when read as a sequence of changing endpoint claims rather than as a single uninterrupted finding. The 1981 paper focused on consciousness theory. The 1987 and 1992 papers leaned toward communication-related correlation patterns. The 1994 article made the most concrete experimental assertion, namely a transferred potential in an isolated recipient. The 1997 paper, completed in December 1994 according to its editorial note, folded the empirical material back into the broader theory. Later studies often retained the language of interpersonal coupling while shifting toward different outcome variables. That progression helps explain why the literature can appear more cumulative than it actually is.

A useful discipline is to ask, for each paper, not whether it sounds adjacent to the transferred-potential hypothesis, but whether it reproduces the same estimand. In most cases the answer is no. Some later studies reported receiver-side power changes, others inter-brain synchrony measures, and others classification outcomes. Those may all be legitimate experimental questions, but they are not interchangeable forms of confirmation. Figure 3 summarizes this historical drift so that later sections can evaluate replications at the correct level of detail.

![Selected chronology of the theoretical and experimental literature. The labels identify shifts in investigated outcomes; this selected chronology does not imply exhaustive coverage or cumulative replication of the 1994 waveform claim. Same-laboratory reports from 1982, 1989, 1995, and 1996 cited in [4] and [5] were not inspected and are not shown.](figures/figure3_historical_timeline.png){width=95%}

# 5. Replication and Non-Equivalent Outcomes



Before study-by-study review, it is helpful to make the endpoint taxonomy explicit. The sender always receives some form of stimulation or task structure, but the receiver-side quantity has varied substantially across the literature. Figure 4 organizes the main classes that appear in the record. The figure is not intended as a ranking of quality. Its purpose is narrower: to show that the empirical target has often changed while the rhetoric of confirmation stayed broad.

![Taxonomy of related but non-equivalent endpoints. A receiver-side waveform, power change, synchrony statistic, or classifier score requires its own estimand and null model.](figures/figure4_endpoint_taxonomy.png){width=92%}

| Endpoint class | Typical measurement target | Example studies | Does it directly reproduce the 1994 claim? | Main vulnerabilities |
|---|---|---|---|---|
| Receiver ERP / waveform | Time-locked averaged response in the unstimulated receiver | Grinberg 1994 [4] | Yes, if the waveform, timing, and design are comparable | Event-marker uncertainty, averaging flexibility, residual stimulus leakage |
| Receiver power or band statistic | Post-stimulus power change or band-limited statistic | Wackermann 2003 [7], Ambach 2008 [12] | No | Dependence inflation, filter choice, non-independence |
| Inter-brain synchrony / coherence | Dyad-level coupling, coherence, or phase relation | Giroldini 2016 [13], hyperscanning literature [17–21] | No | Common task structure, shared artifacts, volume conduction analogues |
| Classifier or multivariate score | Decoding sender condition from receiver-derived features | Bilucaglia 2019 [14] | No | Overfitting, leakage, unbalanced folds, opaque feature pipelines |

This distinction is not semantic bookkeeping. It changes the scientific meaning of a positive result. If a study reports better-than-chance classification from receiver EEG, the result may motivate further work, but it does not by itself show a transferred potential. Likewise, a dyadic synchrony measure observed during a shared interaction does not establish a stimulus-locked response in an isolated receiver. A rigorous paper must preserve those boundaries throughout the evidence review.

## 5.1. A positive result in one endpoint does not replicate another

The strongest original claim is a *stimulus-locked recipient potential similar in time course to the sender's visual evoked potential*. Later investigators studied related, but different, responses: effective voltage at selected latencies, receiver EEG power during sender stimulation, correlations between aggregate trial statistics, departures in runs tests, intermittent fMRI activation, and weak classifier separation of stimulus and no-stimulus periods. These may be legitimate scientific questions individually. They cannot be pooled as demonstrations of a single mechanism or substituted for an independently replicated recipient waveform.

This point matters because the phrase "replication failure" can also be imprecise. A study that fails to find a waveform but reports a power deviation is negative for the waveform endpoint and exploratory or positive for its own power endpoint. A subsequent failure to reproduce that power endpoint is a different result. Scientific inference requires keeping those contrasts separate rather than counting studies into competing camps.

## 5.2. Wackermann and colleagues: power statistics without a copied waveform

Wackermann, Seiter, Keibel, and Walach (2003) recorded six-channel EEG simultaneously from physically separated participants in acoustically and electromagnetically shielded rooms [7]. One participant received visual pattern-reversal stimulation. Rather than identify a visual evoked waveform in the other participant, the investigators analyzed an effective-voltage ratio ($Q$) between stimulus-related and baseline EEG averages. Their abstract reports significant departures from reference distributions in most nonstimulated participants and cautiously suggests that brain-activity correlations may occur [7]. Later accounts note that across the Freiburg studies the direction and electrode location of the effect varied and that deviations appeared partly in the control condition as well [8,12]. These findings should be quoted accurately. The study was not simply a null experiment.

Nevertheless, the reported $Q$ deviations did not reproduce the original Grinberg-style copied visual response. A receiver amplitude statistic can depart from a baseline for reasons unrelated to sensory-specific evoked morphology. The analysis also raises questions about how the null distribution incorporates within-record autocorrelation, dependence across channels, and the selection of receiver latency based on the sender's response. Those questions are empirical and statistical, not semantic disputes about terminology.

## 5.3. Ambach's independent replication and its statistical finding

Ambach (2008) conducted a replication of the separated-subject EEG power design using **17 related pairs** of friends, relatives, or partners and a revised analysis [12]. The published paper explains that the earlier segment-sampling approach could systematically overestimate apparent effects; the author modified the nonparametric procedure and applied a Monte Carlo correction to address dependence across the 19 EEG channels. After correction, none of six chi-square tests reached significance. The closest, the between-condition difference for the 1000 ms window, gave $p=.067$, which Ambach noted might remain open to discussion. He described the outcome as negative for this paradigm, not as proof that the phenomenon is absent [12]. This is substantial adverse evidence against the stability of that **power-statistic** result. It is not an independent reanalysis of the unavailable raw records of Grinberg's 1994 waveform study.

Ambach also ran a null-condition simulation of the previous evaluation procedure. With a nominal $\alpha=0.05$, that procedure produced **20.1%** significant results for one 136 ms analysis window and **26.2%** for a 1000 ms window under the simulated null [12]. These are Ambach's published numerical results for the method and conditions studied. They should not be rewritten as a universal false-positive rate for every Wackermann experiment, nor passed off as findings from a new simulation in this manuscript. They do establish a concrete reason to demand calibrated resampling whenever several EEG channels and time windows are analyzed together.

## 5.4. Radin, Standish, Richards, and other conceptual follow-ups

Radin (2004) reported small EEG associations in separated pairs with a different stimulation and analysis design [9]. His reported aggregate correlation, approximately $r=0.20$, belongs to a statistical measure of ensemble activity, not a recipient waveform that duplicates a sender visual potential. The study is relevant as an independent conceptual test of an unusual correlation; it does not settle the original waveform claim. Standish and colleagues (2004) tested event-related EEG signals in physically and sensory isolated individuals and reported a subset of significant outcomes with limited successful retesting [10]. The dependence of inference on subgroup findings and the physical synchronization arrangement requires careful scrutiny.

Richards and colleagues (2005) reported selected fMRI results in separated individuals [11]. A blood-oxygen-level-dependent response has temporal characteristics, preprocessing choices, spatial inference, and multiple-comparison risks quite different from an EEG evoked potential. A selected small set of participants, even with striking images, does not turn a BOLD result into an independent reproduction of an occipital ERP. The correct relation is conceptual, not instrumental equivalence.

The 2001 conference report by Sabell, Clarke, and Fenwick [6] has not been inspected in full here. Two secondary accounts by researchers in the field describe it as a failed replication: Wackermann (2004) states that participants were placed in separate rooms and no transferred potentials were found, and Ambach (2008) lists it among replication studies that failed to confirm the effect [8,12]. Wackermann (2004) also describes an earlier unpublished study by Fenwick and colleagues (1998) that used auditory clicks with both participants in the same room and reported "some perturbation" in the nonstimulated EEG of six empathically relating pairs [8]. These secondary descriptions do not substitute for the primary texts, which remain priority retrieval targets. Unverified optical-fiber engineering details are not treated as established here.

Kittenis, Caryl, and Stevens (2004) reported a related-pair evoked-alpha global-field-power effect ($p<.023$, $N=13$) and a combined related/unrelated-pair effect ($p<.007$, $N=18$), with no such effect in single-participant controls [45]. Kittenis's 2008 thesis abstract reports effects in nonstimulated members of related pairs in two studies but not in a third, and describes the overall findings as inconclusive [43]. These are evoked-alpha endpoints, not replications of a sender-like waveform. The reported related-versus-unrelated difference is a moderator claim that a prospective design should register in advance rather than apply as a post hoc inclusion rule.

Tressoldi and colleagues (2014) reported a confirmatory study with seven selected participants in two laboratories about 190 km apart [44]. Version 3 describes 20 retained sessions and 78.4% initial coincidences, but only four pairs under the revised procedure, and characterizes the evidence as "mild support". Its event-coincidence endpoint differs from both the 1994 waveform and Wackermann-style power. The replication by Wackermann, Naranjo Muradas, and Putz (2004), whose paradigm Ambach adopted, is also part of this conceptual record [8,12]. Additional bibliographic leads not inspected here include Standish et al. (2001) and Charman's 2006 review; no numerical claim is drawn from them [12]. Taken together, these reports contain positive, null, and internally inconsistent results across non-equivalent endpoints; they do not form a cumulative waveform-replication series.

## 5.5. Open-data EEG studies and machine-learning outcomes

Giroldini and colleagues' later work offered a valuable methodological shift: EEG data and some processing materials were deposited for reanalysis [13]. In the 25-pairing study, the investigators observed conventional evoked responses in stimulated participants and reported a weak receiver-side response using a more elaborate across-electrode correlation algorithm. The paper's ordinary averaged receiver ERP, however, did not display the same clear visual response as the directly stimulated sender. The exploratory method and its null distribution therefore remain central to interpretation.

Bilucaglia and colleagues subsequently reanalyzed two separated-pair datasets with linear discriminant classifiers [14]. The receiver-side classification accuracies they reported were **50.74%** for one dataset and **51.17%, 50.45%, and 51.91%** for stimulation frequencies of 10, 12, and 14 Hz in the other. They evaluated classifiers with stratified 10-fold cross-validation repeated 10 times; the article does not state that folds respected participant or pair boundaries [14]. The same pipeline classified the stimulated partners' own data at **82.84%** in the first dataset and **70.11%, 72.38%, and 72.09%** in the second, so it could detect a genuine evoked response. For nonstimulated partners, the 12 Hz comparison was not significant ($p=.202$), while the others were nominally significant. In the second dataset stimulation frequencies were presented in blocks, which a reviewer flagged as a possible source of time-related confounding; the authors replied that block order varied across participants [14].

These numbers are small differences around the balanced chance baseline, not robust communication accuracy. A nominally significant population-level deviation can coexist with poor prediction for a new person. Whether an effect survives participant-held-out validation, time-block protection, artifact controls, and independently randomized labels is the unanswered computational question. Pair-held-out validation is a useful sensitivity analysis, but it does not replace participant-held-out validation for new-person claims.

The first dataset contains **25 ordered pairings formed from six adults**; the second contains **20 ordered pairings formed from five adults** [14]. Pair counts therefore exceed the numbers of unique participants, and inference must account for participant, pairing, session, and temporal dependence. In particular, holding out a nominated pair does not necessarily hold out every recording from the people in that pair.

The authors provide public Figshare identifiers for the two datasets in their data-availability statement [14]. This makes the work a practical candidate for **retrospective methods research**. An analyst can rerun preprocessing, examine participant and group leakage, and test alternate dependency-preserving nulls. No amount of retrospective code can recover environmental monitors that were never recorded, so a reanalysis must not claim to conclusively exclude technical or sensory pathways.

## 5.6. The 2026 reviews: useful context, no direct confirmation

Acunzo, Denton, Weiler, and Kelly (2026) performed a critical review of neuroimaging research on alleged extrasensory perception, assessing **143 reports** and **129 individual studies** [15]. They identified recurrent challenges including small samples, heterogeneous protocols, analytical flexibility, and weak replication. Batouli and colleagues (2026) provided a distinct **92-study/report descriptive synthesis**, explicitly declining to claim one reliable neural signature across incompatible paradigms [16]. These reviews are useful as a check against selective historical storytelling, but neither performs a new direct reproduction of Grinberg's transferred potential.

Jiang, Zou, and Yu (2026) reviewed **54** EEG hyperscanning studies of social interaction [17]. In a core meta-analysis of 14 studies, inter-brain synchrony was stronger under social-interaction-related conditions (Hedges' $g=0.887$, 95% CI 0.533–1.241), with a smaller effect in an expanded model of 36 studies. The authors note heterogeneity in task design and frequency band and list shared stimulation and behavioral synchrony among relevant factors. These experiments concern participants exposed to common stimuli and reciprocal behavior. Ordinary coupling through auditory, visual, movement, attentional, or shared task pathways remains possible and frequently expected. They should not be used as external validation of anomalous transfer in shielded isolated pairs. Burgess's cautionary analysis and later methods reviews show why even ordinary hyperscanning metrics require well-designed controls [18–20].

| Work | Design and endpoint | Reported result | Relation to original transferred potential |
|:--|:--|:--|:--|
| Grinberg et al. (1994) [4] | Seven pairs; stimulus-aligned receiver EEG waveform | Selected waveform similarities and reported correlations | Original claim; no public raw EEG identified |
| Fenwick et al. (1998) [8, secondary] | Same-room auditory clicks; receiver EEG perturbation | Reported perturbation in six empathic pairs | Unpublished secondary account; not physically isolated |
| Sabell et al. (2001) [6; 8, secondary] | Separate-room design | No transferred potentials in secondary accounts | Primary methods and outcome not inspected |
| Wackermann et al. (2003) [7] | Receiver effective-voltage $Q$ statistic | Deviations in most nonstimulated participants | Related endpoint; no validated copied receiver VEP |
| Kittenis et al. (2004) [45] | Related/unrelated pairs; evoked-alpha global field power | Related-pair $p<.023$; no single-participant-control effect | Different endpoint; not waveform replication |
| Wackermann, Naranjo Muradas, and Putz (2004) [8,12] | Separated-pair power paradigm | Conceptual replication in the Freiburg series | Related endpoint; later corrected replication was null |
| Radin (2004) [9] | EEG aggregate covariance | Reported weak positive association | Conceptual study; not waveform replication |
| Standish et al. (2004) [10] | Event-related/runs and retesting | Positive subset with limited retest consistency | Conceptual study; uncertain generalization |
| Richards et al. (2005) [11] | fMRI response in isolated subjects | Variable positive sessions | Different modality and estimand |
| Ambach (2008) [12] | Independent receiver-power replication, 17 related pairs | All six corrected tests nonsignificant; closest $p=.067$ | Adverse result for Wackermann-style endpoint |
| Kittenis (2008) [43] | Three studies; evoked-alpha global field power | Related-pair effects in two studies, none in the third | Different endpoint; thesis abstract reports inconclusive overall findings |
| May et al. (2010) [38] | Empirical null for the printed 1994 correlation method | $r=0.70$: empirical one-tailed $p\approx.0418$ | Methodological critique, not raw-data reanalysis or replication |
| Tressoldi et al. (2014) [44] | Distant pairs; event-coincidence measure | Authors report mild support; four pairs under revised procedure | Different endpoint; version 3 inspected |
| Giroldini et al. (2016) [13] | Twenty-five ordered pairings from six adults; EEG ERP and across-channel algorithm | Direct receiver ERP unclear; algorithmic association reported | Open-data conceptual follow-up; pairing count is not unique-participant count |
| Bilucaglia et al. (2019) [14] | ML reanalysis of 25 ordered pairings from six adults and 20 from five adults | 50.45%–51.91% on specified receiver comparisons | Weak prediction; participant-held-out validation required |
| Acunzo et al. (2026) [15] | Critical systematic review of broader ESP neuroimaging | Mixed, heterogeneous, limited replication | Contextual synthesis, not direct test |
| Batouli et al. (2026) [16] | PRISMA-informed descriptive synthesis | No unified neural signature established | Contextual synthesis, not direct test |
| Jiang et al. (2026) [17] | Social-interaction EEG meta-analysis | Core $g=0.887$, 95% CI 0.533–1.241 | Different phenomenon; not a replication |

**Table 2.** Endpoint-aware evidence inventory. Reported significance does not determine whether a study measures the same phenomenon. Secondary accounts and abstract-level evidence are labeled rather than treated as full primary-source inspection.

# 6. Causal and Statistical Identifiability

## 6.1. The observation is not the mechanism

The experimental target can be written with two continuous EEG time series recorded on separate systems, sender $X(t)$ and receiver $Y(t)$, a randomized stimulation sequence $S(t)$, and the recorded environmental state $Z(t)$. A sender evoked response is expected under normal sensory physiology. An unexpected receiver association can arise from several classes of pathways: a true physiological response of unknown origin, a common physical signal, a direct instrumentation channel, synchronized behavioral expectation, selection, or a statistical artifact. Unless the design controls those alternatives, the association is not sufficient to identify the source.

Consider a general measurement model:

$$
Y_{\mathrm{obs}}(t)=Y_{\mathrm{phys}}(t)+\lambda L(t)+\eta(t), \tag{1}
$$

where $Y_{\mathrm{phys}}$ is the receiver's genuine physiological signal, $L$ is a measurable or latent leakage process, $\lambda$ its coupling to the recording system, and $\eta$ other measurement noise. All $Y$ terms and $\eta$ are expressed in the recorded voltage units, and $\lambda$ maps the units of $L$ into those voltage units; if $L$ is nondimensional, $\lambda$ has voltage units. The additive form is a modeling assumption, not a general law. Equation (1) is a **new explanatory model**, not an equation from Syntergic Theory. If the experimental onset $S(t)$ influences both a hypothetical physiological response and $L(t)$, a time-locked average can contain both. Without an independent constraint on $L$ and $\lambda$, an observed receiver average cannot uniquely estimate the hypothetical physiological term.

## 6.2. The null models that actually matter

A single statement such as "there is no telepathy" is a poor operational null because it leaves many ways for the experiment to fail. We propose three distinguishable model families. Under $M_0$ there is no time-locked receiver dependence after the specified receiver baseline structure and measured covariates are accounted for. Under $M_1$ an association is produced by an observed or latent common physical/measurement path. Under $M_2$ a reproducible residual receiver association remains after the stated controls. **$M_2$ is a statistical category, not a discovery of quantum physics.**

The primary question is whether the receiver response distribution changes between real-stimulation and matched sham events. A useful study-level contrast is

$$
\Delta=\mathbb{E}\!\left[T(Y)\mid S=1\right]-\mathbb{E}\!\left[T(Y)\mid S=0\right], \tag{2}
$$

where $T$ is a prespecified receiver EEG feature or summary, $S=1$ denotes real sender stimulation, and $S=0$ denotes a sham event. Written at the dyad level, the corresponding equal-dyad-weight contrast is

$$
\Delta_{\mathrm{dyad}}=\frac{1}{I}\sum_{i=1}^{I}\left[\mu_i(1)-\mu_i(0)\right],
$$

where $\mu_i(s)$ is the mean of $T$ over accepted events of condition $s$ in dyad $i$, and $I$ is the number of eligible dyads. The population estimand is the expectation of $\mu_i(1)-\mu_i(0)$ over dyads. Each dyad is weighted equally after within-dyad application of the locked accepted-event rule; event-level analyses must not silently give larger weight to dyads with more usable flashes. The expectations require a valid randomized experiment, comparable recording conditions, and participant- or dyad-level uncertainty. An effect on $\Delta$ may warrant attention; it does not identify whether the pathway was neural, technical, environmental, or unknown.

A stricter conditional hypothesis may be expressed as

$$
H_0: P(Y_{t+\tau}\mid Y_{<t},H_t,S_t)=P(Y_{t+\tau}\mid Y_{<t},H_t), \tag{3}
$$

with a prespecified set of latencies $\tau$ and a recorded covariate history $H_t$ containing the relevant environmental, instrumental, clock, and stimulus-history measurements. $H_t$ may include stimulus-locked leakage proxies recorded within the latency window when the aim is to block a known physical path. Conditioning on a proxy removes only the part of a path that the proxy measures, so residual dependence after conditioning on an imperfect proxy can still be physical. Variables that a genuine receiver response could itself change, such as receiver muscle activity, must not be conditioned on without justification. The latency family and its multiplicity control must be registered, and correlated time samples must be handled at the appropriate independent-unit level. Failure to reject (3) is not the same as proving the absence of every conceivable effect. Conversely, rejecting (3) only rejects the particular conditional independence model under its assumptions. Neither outcome licenses a statement about macroscopic entanglement.

## 6.3. Filters, dependence, and multiplicity

A filtered EEG trace is not a sequence of independent coin flips. If the correlation of adjacent samples is substantial, the sample size $n$ in a conventional Pearson $t$ statistic cannot be interpreted as the effective number of independent observations. Filters also change temporal phase, edge behavior, baseline variance, and waveform shape. A response created by a genuine stimulus and a response created by a stimulus-synchronous cable transient may look similar after the same filter. Adequate controls therefore operate at both the recording and statistical levels.

The original paper describes 16-point rolling comparisons, with 48 reported windows and adjacent windows sharing 15 values [4]. Selecting a significant window after looking at the plotted average introduces another layer of multiplicity. The literature on event-related potentials explains how such researcher degrees of freedom can create convincing but false component differences [23]. Surveys of ERP studies also document incomplete methods reporting and low statistical power [34]. A proper analysis must either prespecify a primary electrode/time-window contrast or use a calibrated multiple-comparison procedure with an exchangeability structure matching the actual experiment [22–24].


## 6.4. A confound stack for anomalous receiver effects

A useful way to organize the problem is as a confound stack. At the outer layer are ordinary sensory and environmental channels: sound, vibration, light leakage, inadvertent experimenter cues, and room-level electromagnetic contamination. At the next layer are timing and instrumentation channels: clocks that drift, event markers that are reconstructed after the fact, trial labels that are copied between systems, or software that shares triggers in ways not fully documented. A third layer contains analysis-induced dependencies: common filtering, flexible baselines, multiple overlapping time windows, selective rejection of trials, and statistics that assume independence where none exists. Only after those layers are measured or bounded does a residual biological question become interpretable.

This stack is not a rhetorical device. It dictates what metadata must be archived. If the hypothesis concerns a receiver-side waveform, the study must preserve raw data, event logs, amplifier specifications, shielding descriptions, synchronization methods, and preplanned analysis code. If the hypothesis concerns synchrony or spectral dependence, it must additionally justify why the chosen statistic is appropriate and how its null distribution was calibrated. A surprising effect with poor provenance is weaker evidence than a null result with complete provenance, because the former cannot separate phenomenon from pipeline.

The apparatus and identifiability schematics below summarize this logic. They emphasize that a correlation is not yet a mechanism, and that the unknown-pathway interpretation is always downstream of measurement discipline. The question is not whether one can imagine a novel pathway, but whether known paths and analysis artifacts were constrained tightly enough that a remaining dependence demands further explanation.

![Proposed prospective apparatus and isolation audit. Rooms and acquisition systems are shown schematically; the diagram does not reconstruct undocumented wiring in the historical experiment.](figures/figure5_apparatus_audit.png){width=96%}

![Causal and measurement alternatives. The randomized stimulus schedule $S$ can influence the receiver record $Y$ through the hypothesized sender-mediated path ($X$ to $Y$), through stimulus-locked leakage $L$, such as generator transients, sound, or timing signals, that bypasses the sender's brain, and through analysis choices $A$. A sender-linked receiver signal is not mechanism-identifying until these paths have been measured or bounded.](figures/figure6_identifiability.png){width=92%}

# 7. Original Synthetic Null Benchmark

## 7.1. Purpose and boundaries

Temporal dependence is a recognized threat to inference in this literature [12,38]. To test that general statistical warning without falsely claiming possession of Grinberg's raw recordings, we ran an independent simulation in which the null hypothesis was known to be true by construction. This is **a methodological illustration**, not a recreation of the 1994 data acquisition, the authors' rolling-window statistic, or Ambach's bootstrap experiment. It estimates the false-positive rate of one clearly defined naive correlation test under a narrow synthetic data-generating process.

The benchmark is not the first demonstration of this problem in the transferred-potential literature. May et al. (2010) used real EEG and the printed 1994 windowing to show the same inflation [38], and Ambach (2008) reported related inflation for a power-statistic procedure [12]. The present benchmark adds a fully synthetic, openly executable version with a known zero association and an exact randomization comparison. Its contribution is transparency and reproducibility, not discovery of the problem.

## 7.2. Data generation

For each frequency band, we generated **5,000 independent pairs** of Gaussian white-noise sequences using NumPy's PCG64 random-number generator with seed **20261025**. Each sequence had **128 samples** at **256 Hz**, representing a nominal half-second observation window. Each member of a pair was transformed by a discrete Fourier filter retaining frequencies from **13–35 Hz** or **4–12 Hz** and zeroing other Fourier coefficients; the inverse transform returned a real, periodically stationary synthetic series. The first band is a transparent approximation to the high-frequency portion discussed in the 1994 report; the second explores a narrower oscillatory band. Neither is a physiologically complete EEG simulator.

With 128 samples at 256 Hz, the Fourier resolution is 2 Hz. The 13–35 Hz filter retains the 11 bins from 14 to 34 Hz, and the 4–12 Hz filter retains the 5 bins from 4 to 12 Hz. Each filtered series therefore lies in a 22- or 10-dimensional real subspace. For independent isotropic Gaussian vectors in $d$ dimensions, $r\sqrt{(d-1)/(1-r^2)}$ follows a $t$ distribution with $d-1$ degrees of freedom. Evaluated at the naive critical correlation for $n=128$, $r=0.1736$, this gives expected naive false-positive rates of **42.82%** for $d=22$ and **60.97%** for $d=10$, close to the simulated finite-sample rates below.

For each pair, the sequences were mean-centered and normalized. The observed zero-lag Pearson coefficient was computed as

$$
r_0=\frac{\sum_{t=1}^{128}(x_t-\bar{x})(y_t-\bar{y})}{\sqrt{\sum_t(x_t-\bar{x})^2\sum_t(y_t-\bar{y})^2}}. \tag{4}
$$

The naive two-sided $p$ value used the standard statistic $t=|r_0|\sqrt{(n-2)/(1-r_0^2)}$ with $n-2=126$ degrees of freedom. This is only properly calibrated when its assumptions hold. As a dependence-aware comparison under the constructed periodic stationary null, we calculated correlation at **all 128 circular shifts** of $y$, using the absolute-correlation rank of lag zero. Ties were retained conservatively. This shift calibration is justified for the specific null model; it is not automatically valid for nonstationary EEG, blocked experiments, or real sequences containing stimulus timing artifacts.

## 7.3. Results

| Synthetic frequency band | Naive Pearson $p<0.05$ | Circular-shift $p\leq0.05$ | Number of independent pairs |
|:--|--:|--:|--:|
| 13–35 Hz | 43.28% | 4.54% | 5,000 |
| 4–12 Hz | 62.06% | 5.08% | 5,000 |

**Table 3.** Executed synthetic null results. All true generating-pair associations were zero. Values are empirical rejection proportions across simulated independent pairs, not historical EEG effect estimates.

\clearpage

![Synthetic null benchmark (5,000 independent pairs per band; 128 samples each). Naive Pearson tests are miscalibrated for the simulated frequency-limited signals; circular-shift calibration is close to its exact attainable size of 4.69% (6/128) in this particular stationary null.](figures/figure7_synthetic_fpr.png){width=93%}

Under the 13–35 Hz synthetic null, **2,164** of 5,000 naive tests rejected at the 5% threshold, compared with **227** calibrated shift tests. Under the 4–12 Hz null, the corresponding counts were **3,103** and **254**. The Wilson 95% Monte Carlo intervals, in the same order as Table 3, are **41.91%–44.66%**, **4.00%–5.15%**, **60.71%–63.40%**, and **4.51%–5.72%**. These intervals quantify simulation sampling uncertainty only; they are not confidence intervals for historical EEG effects or real-data calibration. With 128 shifts, the smallest attainable shift $p$ value is **1/128 = 0.0078125** before tie handling. Because rejection requires lag zero to rank among the six largest of 128 absolute correlations, the exact size under the constructed null is **6/128 = 4.6875%**, slightly below the nominal 5%. Both observed rates are compatible with that value (exact binomial $p=0.66$ and $p=0.19$). These outcomes follow directly from the executable script in Appendix A; no human participants, observed brain correlations, or reconstructed 1994 epochs are involved. The naive-rate inflation arises because band limitation imposes temporal dependence while the naive test continues to use 126 degrees of freedom.

## 7.4. Interpretation and sensitivity

The simulation demonstrates an elementary but consequential point: a nominal significance threshold can become disconnected from the actual false-positive rate when its independence assumptions are false. It does **not** prove that the original investigators used this exact incorrect test, that their receiver signals shared particular oscillations, or that a reported historical coefficient has a corrected probability equal to one of the simulated rates. The 1994 analysis used averaged signals and its own moving-window procedure; our benchmark instead analyzes two independent filtered series and a single zero-lag coefficient. The methods differ deliberately so that the simulation's interpretation remains narrow and reproducible.

The shift test relies on periodic stationarity induced by the spectral construction. Real EEG includes nonstationarity, line noise, event-related artifacts, reference changes, changing vigilance, and edge effects; in such data, arbitrary circular shifts can themselves be misleading. Under strong autocorrelation, small circular shifts leave the shifted series partly aligned with the original. In this periodic construction the test remains exact because every shift is equally likely under the null, but in short or nonstationary recordings nearby shifts are not interchangeable surrogates, and the number of effectively distinct shifts can be far smaller than the number of samples. Practical replication should randomize experimental event assignments at the design stage and use null resampling at the independent unit of randomization. The false-positive rates reported here should motivate a calibration audit, not be presented as proof that all positive studies are artifacts.

# 8. An Operational Framework for Reproducible Testing

## 8.1. Define the scientific estimand before choosing an algorithm

A modern program should begin with a decision about what it intends to detect. The original hypothesis is not "any difference between two signals"; it is a response in a participant who does not receive a stimulus, aligned to the timing of another participant's visual stimulation. The most faithful confirmatory target is therefore a receiver event-related response linked to independently randomized real stimulus onsets, compared with sham onsets under otherwise comparable conditions. A separate spectral or classification hypothesis can be legitimate, but it is secondary unless registered as its own experiment. Analysis after looking at selected waveforms is exploratory and must be presented as such.

Let $Y_{i,c}(t)$ be the receiver EEG voltage for dyad $i$, channel $c$, and time $t$. Let $t_{ij}$ denote externally audited onset time for event $j$ in pair $i$, and $s_{ij}\in\{0,1\}$ indicate sham or real stimulation. Define the receiver's stimulus-locked average by

$$
\widehat{m}_{i,c,s}(\tau)=\frac{1}{N_{is}}\sum_{j:s_{ij}=s}Y_{i,c}(t_{ij}+\tau),\qquad -200\leq\tau\leq500\ \mathrm{ms}. \tag{5}
$$

Here $N_{is}$ is the number of events in condition $s$ that survive the locked quality and missing-data rules, not the number originally assigned. Sampling rate, electrode reference, filters, artifact handling, and accepted-event criteria must be fixed before outcome inspection. The voltage entering the average is baseline-corrected using the prespecified $-200$ to $0$ ms interval, and no epoch with missing baseline or primary-interval samples is silently imputed.

An analysis can compare averaged traces, but its primary contrast should be declared before the first held-out response is examined. For the primary template-projection statistic, let $W$ be the registered latency window, $C$ the registered electrodes, and $u_{i,c}(\tau)$ the unit-norm sender template for dyad $i$, computed from sender real-event data alone and frozen before receiver unblinding. Define

$$
P_i=\sum_{c\in C}\sum_{\tau\in W}u_{i,c}(\tau)\left[\widehat{m}_{i,c,1}(\tau)-\widehat{m}_{i,c,0}(\tau)\right],
$$

and the secondary mean-amplitude statistic

$$
A_i=\frac{1}{|C||W|}\sum_{c\in C}\sum_{\tau\in W}\left[\widehat{m}_{i,c,1}(\tau)-\widehat{m}_{i,c,0}(\tau)\right],
$$

where $|W|$ is the number of latency samples in the window. Set $T_i=P_i$ for the primary dyad-level analysis and report $A_i$ as secondary. Section 10.4 explains why template projection is primary and mean amplitude can cancel a multiphasic response. The final inferential unit is the **independent pair**, not the number of flash epochs. Consecutive flashes are repeated observations within one pair and must be modeled as such. Report both pair-level effects and the hierarchical uncertainty, including between-laboratory variation where applicable.

## 8.2. Statistical hypotheses and inference

A confirmatory frequentist test can use a paired, dyad-level randomization statistic with the actual sham/real schedule as the assignment mechanism. It must preserve block structure, numbers of events, and any stratification in stimulus randomization. The analysis should estimate a population mean or median contrast with a confidence interval rather than simply report whether $p<0.05$. In parallel, define a **smallest effect size of interest** ($\delta_{\min}$) through external physiological calibration and pilot feasibility, with the decision fixed before confirmatory data inspection.

Three possible conclusions follow. *Support for the declared receiver endpoint* requires a consistent real-versus-sham difference in the preselected direction, adequate uncertainty control, successful negative controls, and confirmation in an independent cohort or laboratory. *Evidence against effects at or above $\delta_{\min}$* requires a sufficiently narrow interval or valid equivalence test within a declared equivalence region. *Inconclusive* applies when the interval is too wide to determine either. A conventional nonsignificant result is not automatically proof of a zero effect; likewise, a small statistically significant result in a large, methodologically flexible analysis does not establish the claimed physiology [22–24].

## 8.3. Phase synchrony, information theory, and complexity

The neural field can be represented operationally as a vector of measured or source-estimated states, but such a representation is an analytical construct rather than the physical pre-space structure described in Syntergic Theory. One conventional measure of within-brain synchronization is the phase-locking value,

$$
\operatorname{PLV}_{jk}=\left|\frac{1}{N_t}\sum_{t=1}^{N_t}e^{\mathrm{i}(\phi_j(t)-\phi_k(t))}\right|,\qquad 0\leq\operatorname{PLV}_{jk}\leq1, \tag{6}
$$

where $N_t$ is the number of time samples, distinct from the receiver statistic $T_i$. PLV is useful only under a design that can separate genuine relationships from common referencing, spectral concentration, trial count, and volume conduction. Burgess showed that common synchronization measures can report apparent between-brain coupling from independent recordings [18]. Similar cautions apply to coherence, weighted phase-lag measures, and directed estimators: the estimator's name does not supply causal identification. We therefore treat coherence and related indices as secondary descriptive measures unless a validated physical and causal model has been specified [18–21].

Conditional mutual information and transfer entropy may help measure residual dependence after accounting for measured confounds, but they are sample-hungry for noisy continuous EEG and are highly vulnerable to estimator choice, embedding dimension, lag selection, and hidden common causes. A positive transfer-entropy estimate does not entail directed information transfer through an unknown physical channel. In particular, any conditional model must distinguish a stimulus-associated measurement artifact from a physiological response with identical timing.

The idea of a single "neurosyntergy score" is tempting, but multiplication of coherence and complexity does not automatically yield a valid new theoretical observable. One can define a descriptive index $I(t)=C(t)K(t)$ from normalized connectivity $C$ and normalized complexity $K$ and test its repeatability. That is not the original author's field equation, and its construct validity depends on whether it predicts outcomes that simpler measures do not. We decline to present an unvalidated index as a discovered law. Its use remains optional, exploratory, and subordinate to direct stimulus-locked evidence.

## 8.4. Model comparison and a detection ladder

The proposed inference ladder is deliberately conservative. First demonstrate acquisition integrity: independent receivers, accurate event timing, controlled stimulation and sham distribution, and stable recording quality. Second show a prespecified effect relative to design-valid nulls. Third establish site-independent generalization. Fourth eliminate measured technical and environmental candidate paths using interventions such as hardware swapping, shielding changes, phantom receivers, and no-human controls. Fifth, test whether any remaining effect carries randomized sender content beyond the real/sham event itself, for example frequency-tagged or multi-valued content, rather than only marking event times. Only thereafter should novel physical mechanisms enter a model comparison.

An anomalous correlation that cannot be reproduced in a new laboratory is not a validated physical effect. A classifier that discriminates real events only when the training and test segments share temporal context is not an independent prediction. A result that is abolished by breaking a ground path, suppressing a stimulus-generator transient, or swapping amplifiers is evidence about instrumentation. These decision rules are more informative than retrospectively selecting a favorite explanation after a significant output.


## 8.5. A concrete pipeline from raw signals to an auditable claim

One weakness of the historical literature is that it often presents the statistical result without exposing the full path from raw voltages to inference. A modern workflow should do the opposite. The unit of scientific inspection is not the final p-value alone but the entire transformation chain: data intake, file integrity, event validation, preprocessing, feature extraction, null calibration, sensitivity analysis, and report generation. Every transformation should be scripted, versioned, and tied to a frozen configuration.

In practice that means starting from raw or minimally processed recordings, mapping them into a standard structure such as EEG-BIDS when possible, and generating a machine-readable audit trail for each subject and session [25,31]. Filters, re-referencing choices, bad-channel handling, and epoch boundaries should be locked before the final labels are examined. Artifact rejection should be quantified, not left as an informal visual judgment. A primary endpoint should be declared in advance, and all secondary or exploratory analyses should remain explicitly labeled as such.

The inferential core should then use null procedures that respect autocorrelation, trial structure, and multiplicity. For waveform questions, cluster-based or permutation approaches can be appropriate if their assumptions and family-wise error targets are stated clearly [22]. A cluster-based permutation test controls familywise error for the omnibus null; it does not establish that any particular time point or electrode within a significant cluster carries an effect, and it does not estimate onset or offset latency. Claims about timing or topography require separate, prespecified procedures [46]. For synchrony or dependence statistics, circular shifts, permutation of condition labels, or hierarchical resampling may be more defensible than naive per-sample tests. The point is not that one method solves everything, but that the null model must match the data-generating structure well enough that a $p$ value retains its meaning.

Finally, a publication-grade workflow needs a failure path. If provenance is incomplete, if event logs cannot be validated, if sensitivity analyses show strong instability, or if artifact imbalance dominates the result, the pipeline should terminate in a formal *inconclusive* outcome rather than force a positive or negative headline. That discipline is especially important in controversial domains where weak evidence is easily over-interpreted.

![Proposed retrospective EEG reanalysis workflow. Data integrity, event timing, locked preprocessing, calibrated nulls, sensitivity analyses, and explicit failure criteria precede interpretation.](figures/figure8_reanalysis_pipeline.png){width=96%}

# 9. Retrospective Open-Data Reanalysis Plan

## 9.1. Rationale and data boundaries

The most efficient next empirical step does not require recruiting new participants. The two EEG datasets cited in Bilucaglia et al. (2019) have public Figshare records associated with the underlying Giroldini/Tressoldi studies [13,14]. The identifiers given in the data-availability statement are **10.6084/m9.figshare.1466876** and **10.6084/m9.figshare.5132647.v7**. Both records have later versions, so the analysis must cite and hash the exact version downloaded. The statement of [14] lists the data under CC-BY 4.0; consent terms for reanalysis must still be confirmed from the deposits or original articles. The precise version, file hashes, consent and redistribution terms, montage information, timing-channel semantics, and event balance must be recorded before analysis. Public availability does not establish that every device log or environmental variable needed for a definitive interpretation is included.

No retrospective human EEG results are reported in this manuscript. The following is a specified **analysis plan**, not a claim of completed reanalysis. This distinction avoids a common defect in methods reporting: a detailed method section describing code that was never run. Prospective registration of retrospective analyses can prevent additional tuning against a known dataset only if the frozen plan specifies the remaining degrees of freedom before the analysts inspect new condition-specific outcomes.

The validation unit must match the intended generalization. **Pair-held-out** evaluation excludes recordings assigned to a nominated ordered pairing, but the same people may remain in training through other pairings. **Participant-held-out** evaluation excludes every recording involving the held-out people and therefore addresses generalization to new individuals more directly. With only six adults in one dataset and five in the other, neither scheme supplies many independent human units; folds, confidence intervals, and conclusions must preserve that limitation rather than treating 25 or 20 ordered pairings as independent samples.

## 9.2. Data intake and validation

The intake stage will store the immutable source version and SHA-256 digest for every downloaded file. Each dataset will be mapped into EEG-BIDS where the metadata permit, preserving original channels, reference settings, acquisition sampling frequency, event definitions, event times, recording run, subject, pair, and site. Where the acquisition reference or hardware synchronization information is absent, the manifest will explicitly mark it unknown. Conversion will not invent stimulus timestamps, calibration measurements, or participant attributes [31].

Quality assessment will compare recorded sampling rates with event indices, detect missing or duplicated markers, inspect line-noise structure, assess event counts and class balance, and document recording boundaries. Filtering and artifact rejection must use frozen parameters and be applied identically to real and yoked conditions. Channels should never be selected after identifying those that maximize receiver classification. Any automated artifact-removal model that learns parameters must be trained within the appropriate cross-validation fold to prevent information from held-out data leaking into fitted transformations.

## 9.3. Leakage-resistant evaluation

The primary retrospective endpoint will be **sender-stimulus label prediction from receiver data under participant-held-out validation**, but only where the archive includes suitable independent labels and enough distinct participants to support the split. Pair-held-out and session-held-out analyses will be reported separately as sensitivity analyses, not treated as equivalent to participant-held-out validation. Every recording involving a held-out participant must be excluded from training, tuning, feature selection, and fitted artifact-removal transformations. Random splits of windows from a continuous recording are prohibited because adjacent windows may share noise, time drift, and task structure. The entire preprocessing transformation that estimates parameters, feature selection, dimensionality reduction, and model selection must be nested inside training folds [14,18,23,33].

The simplest baseline should be an interpretable, regularized linear classifier using a prespecified feature set. A deep neural network should only be considered if sample size and nested validation support it. AUC and balanced accuracy must be accompanied by confidence intervals that respect the participant-level resampling unit and the corresponding randomization distributions, not just a single percentage. Trial and pairing counts cannot substitute for the number of independent participants when the claim is expected to generalize to new people; pair-level intervals may accompany, but cannot replace, participant-level uncertainty for that claim.

The negative-control suite will include independent pseudo-pairing, time-block-preserving label randomization, event schedules from different recordings, no-event surrogate segments, and any instrument-only records present in the public datasets. Each control answers a different question. Time-shifts ask whether a signal depends on exact alignment. Yoked schedules ask whether general session structure can predict labels. Pseudo-pairing probes whether results are tied to the nominated dyad. A phantom or no-human control, when available, directly tests whether an EEG amplifier records stimulus-linked artifacts in the absence of a brain.

## 9.4. Audit outputs and acceptance gates

The reanalysis must produce a machine-readable manifest; code/environment lockfiles; a frozen analysis plan; a table of available and absent physical controls; exact train/test memberships; full prediction vectors; confidence intervals; permutation nulls; and a failure-case report. If the dataset cannot support a participant-held-out analysis, the project should say so rather than manufacture independence by splitting time windows or pairings. If the public data show classification near 50%, that alone does not determine absence of an effect, but the interval must quantify how much predictive information is excluded. If a significant residual is found, it remains a retrospective candidate awaiting a new prospective dataset with audited physical isolation.

# 10. Prospective Multi-Laboratory Replication Protocol

## 10.1. Scope and ethics

A prospective study should be registered, reviewed by an appropriate ethics body, and conducted with volunteers who understand that the phenomenon is unestablished. Consent materials should state plainly that no health benefit, diagnostic information, or spiritual outcome is expected, that the phenomenon is unestablished, and that a null result reflects nothing about the participants or their relationship. The protocol must avoid implying that successful "connection" has clinical, spiritual, or diagnostic significance. The scientific aim is narrow: test whether a prespecified receiver EEG response to externally randomized sender stimulation can be detected above matched sham conditions when ordinary channels have been measured and actively challenged.

The strongest design uses at least two independently managed acquisition sites, a common protocol, and a held-out replication cohort. Geographic separation may reduce some shared environmental paths, but distance alone does not substitute for equipment audits, time synchronization, or counterbalanced control states. In particular, two distant systems can still share software artifacts, remote commands, labels, or network-derived timing patterns. Every connection that carries stimulus information must be logged and shown not to reach receiver EEG hardware through an unmodeled pathway.

## 10.2. Stimulus design and blinding

Each dyad completes randomized real and sham trials. The generator records every decision; participants, receiver-side operators, and primary analysts are blinded to the event type during acquisition. Real events create a brief sender visual stimulation; sham events run an indistinguishable acquisition schedule without delivering a real visual flash. Hardware behavior during sham should be matched or characterized to avoid trivially classifying real versus sham from generator current draw or mechanical sound. Trial timing will include jitter sufficient to prevent predictable periodic entrainment, and the exact schedule will be committed before the EEG outcome is analyzed.

The sender's response should provide a manipulation check that visual stimulation actually evoked a response, but sender ERP amplitude is not allowed to become a post hoc gate for excluding pairs from the primary test. The original theory's emphasis on perceived connection may be tested as a secondary predeclared moderator, not used to discard unsuccessful pairs after observing the receiver result. Relationship type, for example long-term partners, friends, or strangers, should be recorded and, if recruitment permits, used as a registered stratification variable so that the proponent hypothesis that effects require an established relationship can be tested without becoming a post hoc inclusion rule. Such subgroup selection would otherwise change the estimand and expand false-positive opportunities.

## 10.3. Instrumentation and physical isolation

Separate, independently powered EEG systems should be used for sender and receiver. The hardware should have documented grounding and shielding, with no unexamined conductive path that could carry event-locked transients. Receiver-side physical monitors should record light, sound, vibration, and electromagnetic activity at a temporal resolution sufficient to evaluate plausible artifacts. Receiver EOG, EMG, and respiration should be recorded so that blinks, movement, or breathing that could synchronize with sender events can be detected, and sender behavior should be logged for the same reason. A calibrated photodiode at the sender confirms actual light onset. External timing logs must be capable of post hoc alignment without requiring a conductor that places the sender's stimulus pulse into the receiver amplifier. Timing uncertainty should be measured with an independent calibration event whose leakage behavior is understood.

Hardware-only negative controls, with electrodes placed on suitable phantoms rather than human skin, are mandatory. The exact flash and sham sequence is run with no receiver present. Room and amplifier assignments are then swapped, and the procedure repeated. If a reproducible receiver-linked electrical transient exists in the phantom condition, the human EEG finding requires reconsideration even if its time course resembles an ERP. These controls test an instrumental mechanism directly rather than treating the phrase "Faraday chamber" as a universal guarantee.

## 10.4. Preregistered primary endpoint

The first proposal is a receiver posterior real-minus-sham event-related response, summarized by two prespecified statistics whose roles are fixed before data collection. The **primary statistic is template projection**. For each dyad, the sender's real-event average over the registered window, computed from sender data alone and frozen before any receiver data are unblinded, is scaled to unit norm. The primary outcome $P_i$ defined in Section 8.1 is the inner product of the receiver's real-minus-sham average with that template over the same window and electrodes. Because the template comes from the sender and is independent of receiver noise under the null, the statistic has expectation zero under the null, is signed, and tests the original claim that the receiver average resembles the sender's evoked response.

A mean-amplitude contrast $A_i$ over the same window is simpler but can cancel when a multiphasic visual response changes polarity within the window; it is therefore secondary. For illustration, an occipital region and an 80–250 ms window are plausible, but these values are not confirmed parameters until equipment and pilot evidence establish their suitability. Any latency tolerance for the template, such as a small registered family of lags, must be declared with its multiplicity correction. Both statistics are analyzed at the pair level, and neither may be tuned on the receiver recordings used to claim success.

Secondary endpoints include spectral changes, non-zero-lag phase coupling, multivariate sender-label decoding, and independent distance/shielding manipulations. Their familywise error control and inferential priority must be specified in advance. Multiple channels and windows may be explored for hypothesis generation, but they do not count as confirmation without adjustment and replication. No-result conclusions should report precise confidence bounds and an equivalence analysis against the prespecified minimum scientifically relevant effect.

## 10.5. Sample size and precision

A numerical sample size cannot be responsibly fixed from the original seven-pair correlations because those are not unbiased estimates of the standardized real-minus-sham recipient effect. For a simple paired contrast with standardized within-pair effect $d_z$, a normal-approximation planning relation is

$$
n\approx\frac{\left(z_{1-\alpha/2}+z_{1-\beta}\right)^2}{d_z^2}. \tag{7}
$$

For an illustrative $d_z=0.20$, two-sided $\alpha=0.05$, and power $1-\beta=0.80$, Equation (7) gives $n\approx196.22$, or **197 independent pairs** after rounding up; the exact paired-$t$ calculation gives **199**. Either figure applies before allowing for unusable recordings or between-site heterogeneity. The true design must update this with independent pilot variance, expected missingness, cluster effects, multiple endpoints if any, and site-level replication requirements. A small convenience sample cannot acquire high evidential value by multiplying the number of electrodes or trials.

This planning value addresses detection. If the study must also be able to conclude that effects at or above the declared threshold are absent, using two one-sided tests against bounds of $\pm0.20$ in $d_z$ units at $\alpha=0.05$, the probability of reaching that conclusion when the true effect is zero is about **75% at 197 pairs** and reaches 80% at about **215 pairs** by normal approximation. The registered sample size must satisfy whichever conclusions the study is designed to support.

## 10.6. Outcome criteria and mechanism discrimination

The result will be called *supported for the preregistered endpoint* only if the receiver contrast is statistically and practically distinguishable from the matched sham distribution, survives the physical negative controls, and reproduces in an independently held-out site. It will be called *not supported above the declared meaningful effect* if the uncertainty bound excludes effects at or above the registered threshold. Otherwise it will remain inconclusive. A single significant omnibus $p$ value does not meet any broader claim about causal information transfer or quantum biology.

If a robust residual survives, the next experiment should vary physical distance, shielding, grounded versus isolated apparatus, stimulation intensity, and sender-content encoding under prespecified predictions. Two cases must be distinguished. If flash times are predictable, a time-locked receiver response can arise from expectancy or periodic entrainment without any dependence on the sender, which is why jittered and yoked schedules are required. If real and sham events are randomized and concealed, a reliable real-minus-sham difference in receiver data is already, in information-theoretic terms, a channel from the randomization to the receiver with nonzero capacity, however small. Decoding sender-chosen randomized content adds a demonstration of practical capacity and content specificity; it is not the first point at which communication becomes the relevant description.


## 10.7. Multi-laboratory governance, not just multi-laboratory data

A convincing prospective program needs more than several sites running nominally similar experiments. The governance structure has to be shared as well. The same preregistration, randomization logic, shielding checks, stopping rule, and analysis container should be applied across labs before the first confirmatory recording is evaluated. Otherwise, cross-site variation becomes uninterpretable because hardware differences, silent analytic drift, and post hoc parameter tuning are mixed together.

This is why the protocol uses a central blinded randomization service that supplies each site's schedule, and why Figure 9 shows a blinded event and metadata escrow with an independent analysis container locked before unblinding. A multi-lab study should also appoint an adversarial confound team whose role is to search for timing leakage, electromagnetic coupling, motion contamination, and experimenter effects. If a signal survives both the confirmatory pipeline and the confound audit, it becomes substantially more interesting. If it fails either, the field still gains a clear answer rather than another ambiguous anecdote.

Multi-lab agreement is also the best safeguard against charismatic over-interpretation. A single dramatic dataset can always be questioned. A repeated effect across matched sites, with archived controls and a predeclared decision rule, is much harder to dismiss and much easier to interpret scientifically.

![Proposed prospective multi-laboratory replication architecture. Independent acquisition sites use a common preregistered endpoint, documented isolation checks, blinded schedules, a blinded event and metadata escrow, and an independent analysis container locked before unblinding.](figures/figure9_multilab_protocol.png){width=95%}

# 11. Physics and the Boundary of Interpretation

Grinberg and colleagues linked the transferred potential to the Einstein–Podolsky–Rosen problem [4]. That connection was an interpretation of classical voltages; the published experimental results did not specify a joint quantum state or measure an entanglement witness. Quantum entanglement is defined within the mathematical structure of quantum states and measurements; a positive EEG cross-correlation in conventional recordings does not satisfy those criteria. Bell-type tests additionally require carefully designed measurement choices and control of relevant causal loopholes. The EEG studies reviewed here did not implement such a test.

The quantum no-signaling principle rules out using entanglement alone to send controllable information without an ordinary channel [30]. This bears directly on the transferred potential as it was reported. The claim was not only that sender and receiver EEG covaried; it was that the receiver's own average, aligned to the sender's randomly timed flashes, showed a deflection that was absent when no flash was delivered. If real, that is a dependence of the receiver's local data on a variable controlled at the sender's location, which is the defining feature of a signal. In principle it has positive channel capacity because a sender could encode bits by delivering or withholding flashes at prearranged times. Ordinary quantum entanglement cannot produce such a dependence. The 1994 authors stated that no violation of causality was involved and that the correlation becomes meaningful only after comparison, by analogy with Bell experiments, yet they also suggested that frequency-tagged flashes might in principle carry messages in Morse code, possibly through nonlinear Schrödinger dynamics [4]. Wackermann (2004) noted the same tension between causal transfer and the entanglement metaphor [8]. This does not show that the reported effect is impossible. It shows that a confirmed real-versus-sham receiver difference would be inconsistent with an explanation based on ordinary entanglement and collapse, and would require either a classical pathway or new physics with its own testable dynamics.

Tegmark's decoherence calculations place strong physical constraints on particular proposals for coherent macroscopic neural quantum states [29]. Their exact estimates are model-dependent and should not be misrepresented as a theorem excluding all quantum behavior in living matter. They also do not bear directly on correlations between scalp voltages.

Classical neuroscience already provides substantial accounts of the generation and propagation of EEG signals, neural oscillations, hierarchical inference, and the neural correlates of perceptual access [26–28,35]. Those accounts are neither identical nor a settled solution to subjective experience. Their existence makes it necessary, however, to show what unique explanatory or predictive work the proposed pre-space structure does beyond existing models. Until a distinctive prediction survives experimental testing, that structure should be described as a speculative interpretive proposal.

The relevant scientific question is not whether the word "quantum" can be attached to consciousness. It is whether a model has well-defined state variables, physical couplings, quantitatively different predictions, and a feasible falsification criterion. A theory that can explain every possible outcome after the experiment is not adding empirical constraint. A narrow, reproducible EEG phenomenon would be an important result even if its ultimate explanation were conventional; the physics must follow the measurement rather than precede it.

# 12. Discussion: What Remains Worth Studying

The historical record supports a restricted but legitimate research agenda. A theory of consciousness need not be treated as established to inspire a clean empirical question. Likewise, a failed reproduction need not be treated as a personal or intellectual indictment of the investigator. The contribution of this review is to specify a path from an evocative hypothesis to observations that an independent laboratory can inspect, criticize, and reproduce.

There are three principal lessons. **First**, the experimental target must be stable. A receiver waveform, a receiver variance statistic, a classifier score, and social-interaction synchrony are different quantities. Once a strong claim fails under its original endpoint, changing the metric may yield an interesting new hypothesis, but it does not rescue the old one without an explicit new prediction. **Second**, data provenance is part of the scientific result. A published curve does not preserve event labels, excluded epochs, hardware transients, or an acquisition circuit. Those missing components determine how strongly a causal interpretation can be defended. **Third**, computational adversarial testing is useful here: it can expose subtle classification leakage, construct realistic nulls, compare preprocessing choices, audit metadata, and help organize archival sources. It cannot infer physical channels from pattern scores in the absence of measurements.

The review also shows why negative findings and methodological critiques deserve more attention. Ambach's corrected power analysis addressed a real statistical vulnerability and found no support for the tested endpoint [12]. May et al. showed that correlations of the magnitude highlighted in 1994 can arise between independent filtered EEG averages under an empirical null [38]. The 2026 broader reviews acknowledge heterogeneous positive reports but do not find a settled neural signature of anomalous information transfer [15,16]. The difference between a convincing null against a declared meaningful effect and an underpowered failure to obtain $p<0.05$ must still be respected. A definitive negative result can narrow the space of plausible effects and prevent further investment in unconstrained claims.

At the same time, archival access remains a practical research opportunity. Recovery of the 1994 raw EEG, timing records, and wiring diagram would be more informative than another summary of the same printed figures. In their absence, the public later datasets support an independent software audit with measurable error rates, but not a reconstruction of the historical room environment. A public repository should preserve all scripts, source identifiers, model versions, simulated datasets, analysis logs, and registration history. This is the standard needed if the work is to become cumulative rather than another isolated report.



## 12.1. Specific limitations of this manuscript

This is not a complete systematic review. We have not independently retrieved or inspected every proceedings report, same-laboratory article, or unpublished thesis, and we have not calculated a publication-bias-adjusted pooled estimate of a common transferred-potential effect. Different versions of later open-review papers may have amended methods and conclusions; publication version and date must be fixed whenever a numerical result is cited. Some historical technical statements are ambiguous in the printed record, including the 1994 units and the full signal-processing path. We did not reprocess original human EEG or conduct a new experiment; the only executed computation here is the deliberately constrained synthetic null benchmark. These statements restrict what the paper can conclude.

The simulation uses independent stationary Gaussian signals with ideal frequency-domain filtering. Its circular-shift calibration is not an automatic recipe for real nonstationary EEG, and it cannot identify the source of a historical waveform. The proposed sample size is a planning illustration, not an approved protocol. The model equations are modern test definitions and do not establish Grinberg's physical ontology. Finally, an unexpectedly reproducible effect would require its own mechanism-discrimination experiments; a positive receiver difference alone cannot support claims of telepathy, superluminal signaling, or quantum entanglement.

## 12.2. A prioritized research program

The first priority is **independent source recovery**: obtain the 1989, 1992, 1995, and 1996 same-laboratory reports, authoritative proceedings, raw event logs, and unambiguous versions of the 1992 and 1994 articles. The second is **retrospective data integrity**: freeze a participant-held-out primary reanalysis of public 2016/2019 datasets, with pair-held-out sensitivity analyses, and publish both the failures and successes of every negative-control test. The third is **prospective measurement**: conduct a blinded, physically audited pilot that measures the environmental signal paths and fixes the event-related endpoint. The fourth is a **multi-site confirmatory study** designed for precision rather than sample-size optics. The fifth, conditional on an independent residual, is **mechanism discrimination**. The last step is deliberately contingent; it should not be funded or advertised as a demonstrated effect before the earlier steps succeed.

## 12.3. Why the topic remains scientifically interesting despite weak support

The literature remains worth studying for three reasons. First, the underlying measurement problem is real and general: how should one detect weak dependence between two high-dimensional, autocorrelated biological time series without fooling oneself? That problem matters well beyond parapsychology. It appears in hyperscanning, closed-loop neurotechnology, brain-computer interfaces, and any setting in which small apparent couplings can be manufactured by preprocessing choices or shared task structure.

Second, the historical case is a useful stress test for open science. It concentrates many failure modes that now concern the broader neuroscientific community: unclear provenance, underpowered samples, flexible analyses, endpoint drift, and the temptation to infer mechanism from statistically unusual correlation. A rigorous reassessment therefore has pedagogical value. It shows how a dramatic claim can be taken seriously enough to audit without treating seriousness as belief.

Third, there is a legitimate scientific asymmetry between impossibility claims and failed evidence. The present paper does not argue that unusual interpersonal EEG dependence is metaphysically impossible. It argues that the published record does not yet isolate such a phenomenon convincingly. That leaves open a disciplined path for further testing while refusing to upgrade suggestive findings into established physics.

## 12.4. What would count as genuinely strong evidence

Strong evidence would have several simultaneous properties. The effect would appear in a predeclared primary endpoint, under physical and instrumental isolation that has itself been measured rather than assumed. The effect size and timing would be stable across sessions and laboratories. The analysis would survive sensitivity checks over reasonable preprocessing variants. Alternative channels and leakage proxies would fail to account for the result. Most importantly, the full raw data, metadata, and code would be public or at least escrowed for independent inspection.

Even then, interpretation would proceed in stages. A robust receiver-side signal would first justify the claim that an anomalous dependence exists under the tested conditions. Only after that stage would a mechanism debate become scientifically productive. The leap from *anomalous dependence* to *pre-space structure* or *quantum nonlocality* would still require an additional layer of evidence. This sequence is not overly conservative; it is what keeps electrophysiology from collapsing into metaphysics whenever an unusual graph or $p$ value appears.

# 13. Conclusion

The historical strength of Syntergic Theory lies in the question it raises about neural integration and experience, not in the demonstrated existence of an informational pre-space structure. Grinberg-Zylberbaum's transferred-potential experiment supplied a testable electrophysiological prediction, but the published evidence does not establish a robustly reproduced sender-like evoked waveform in a sensory-isolated receiver. Later reports measure heterogeneous endpoints, some positive and some null, and the corrected statistical evidence weakens straightforward claims of replication.

The present paper contributes a source-corrected account of the original experiment, an endpoint-based map of later work, an explicit causal and statistical model, an openly executable synthetic demonstration of false-positive inflation under temporal dependence consistent with earlier empirical demonstrations by May et al. (2010) and Ambach (2008), and a protocol for retrospective and prospective verification. None of these contributions demonstrates anomalous brain-to-brain communication. They specify what evidence would be required before that conclusion could be entertained. The next defensible claim must be a reproducible measurement with a declared null, audited physical channels, independently held-out data, and a result that survives researchers who are actively trying to disprove it.

# Acknowledgments and Research Disclosures

AI-based assistants were used for literature discovery, synthesis of research notes, drafting and revision of text, writing and checking the benchmark and figure code, generating figures, converting the PDF and DOCX files, and running verification checks. AI outputs were not treated as sources: citations, quotations, equations, and numerical results were checked against primary sources or by executing the included code. AI tools are not authors. The author retains responsibility for all content and release decisions. Source material from prior investigators is credited in the references. No new human-subject study, retrospective human EEG computation, or randomized laboratory trial was conducted for this paper. No new human-subject ethics approval was required for the synthetic simulation. Independent checking of primary-source interpretations, statistical code, and unresolved historical details remains welcome.

# References

[1] Grinberg-Zylberbaum, J. (1981). The transformation of neuronal activity into conscious experience: The syntergic theory. *Journal of Social and Biological Structures*, 4(3), 201–210 (registered by Crossref under the title *Journal of Social and Biological Systems*). https://doi.org/10.1016/S0140-1750(81)80036-X

[2] Grinberg-Zylberbaum, J., & Ramos, J. (1987). Patterns of interhemispheric correlation during human communication. *International Journal of Neuroscience*, 36(1–2), 41–53. https://doi.org/10.3109/00207458709002138

[3] Grinberg-Zylberbaum, J., Delaflor, M., Sánchez Arellano, M. E., Guevara, M., & Pérez, M. (1992). Human communication and the electrophysiological activity of the brain. *Subtle Energies*, 3(3), 25–43. https://journals.holosuniversity.org/index.php/seemj/article/view/154

[4] Grinberg-Zylberbaum, J., Delaflor, M., Attie, L., & Goswami, A. (1994). The Einstein-Podolsky-Rosen paradox in the brain: The transferred potential. *Physics Essays*, 7(4), 422–428. https://doi.org/10.4006/1.3029159

[5] Grinberg-Zylberbaum, J. (1997). Ideas about a new psychophysiology of consciousness: The syntergic theory. *Journal of Mind and Behavior*, 18(4), 443–458. https://www.jstor.org/stable/43853834

[6] Sabell, A., Clarke, C., & Fenwick, P. (2001). Inter-subject EEG correlations at a distance: The transferred potential. *Proceedings of the 44th Annual Convention of the Parapsychological Association*, 419–422. **Citation metadata located; underlying proceedings methods not independently inspected in this manuscript.**

[7] Wackermann, J., Seiter, C., Keibel, H., & Walach, H. (2003). Correlations between brain electrical activities of two spatially separated human subjects. *Neuroscience Letters*, 336(1), 60–64. https://doi.org/10.1016/S0304-3940(02)01248-X

[8] Wackermann, J. (2004). Dyadic correlations between brain functional states: Present facts and future perspectives. *Mind and Matter*, 2(1), 105–122. https://www.mindmatter.de/resources/pdf/wackermann.pdf

[9] Radin, D. I. (2004). Event-related electroencephalographic correlations between isolated human subjects. *Journal of Alternative and Complementary Medicine*, 10(2), 315–323. https://doi.org/10.1089/107555304323062301

[10] Standish, L. J., Kozak, L., Johnson, L. C., & Richards, T. (2004). Electroencephalographic evidence of correlated event-related signals between the brains of spatially and sensory isolated human subjects. *Journal of Alternative and Complementary Medicine*, 10(2), 307–314. https://doi.org/10.1089/107555304323062293

[11] Richards, T. L., Kozak, L., Johnson, L. C., & Standish, L. J. (2005). Replicable functional magnetic resonance imaging evidence of correlated brain signals between physically and sensory isolated subjects. *Journal of Alternative and Complementary Medicine*, 11(6), 955–963. https://doi.org/10.1089/acm.2005.11.955

[12] Ambach, W. (2008). Correlations between the EEGs of two spatially separated subjects: A replication study. *European Journal of Parapsychology*, 23(2), 131–146. https://ejp.wyrdwise.com/EJP%20v23-2.pdf

[13] Giroldini, W., Pederzoli, L., Bilucaglia, M., Caini, P., Ferrini, A., Melloni, S., Prati, E., & Tressoldi, P. (2016). EEG correlates of social interaction at distance. *F1000Research*, 4, 457, version 5. https://doi.org/10.12688/f1000research.6755.5

[14] Bilucaglia, M., Pederzoli, L., Giroldini, W., Prati, E., & Tressoldi, P. (2019). EEG correlation at a distance: A re-analysis of two studies using a machine learning approach. *F1000Research*, 8, 43, version 2. https://doi.org/10.12688/f1000research.17613.2

[15] Acunzo, D. J., Denton, A. H., Weiler, M., & Kelly, E. F. (2026). Neuroimaging studies of extra-sensory perception: A systematic and critical review. *NeuroImage*, 333, 121937. https://doi.org/10.1016/j.neuroimage.2026.121937

[16] Batouli, S. A. H., Parsa, M., Safdari, S., & Radin, D. I. (2026). Neuroimaging findings in extrasensory perception research: A PRISMA-informed descriptive synthesis. *Explore*, 22(5), 103478. https://doi.org/10.1016/j.explore.2026.103478

[17] Jiang, L., Zou, Q., & Yu, S. (2026). EEG inter-brain synchrony in social interaction: A systematic review and meta-analysis of condition effects and outcome associations. *Biological Psychology*, 210, 109367. https://doi.org/10.1016/j.biopsycho.2026.109367

[18] Burgess, A. P. (2013). On the interpretation of synchronization in EEG hyperscanning studies: A cautionary note. *Frontiers in Human Neuroscience*, 7, 881. https://doi.org/10.3389/fnhum.2013.00881

[19] Hakim, U., De Felice, S., Pinti, P., Zhang, X., Noah, J. A., Ono, Y., et al. (2023). Quantification of inter-brain coupling: A review of current methods used in haemodynamic and electrophysiological hyperscanning studies. *NeuroImage*, 280, 120354. https://doi.org/10.1016/j.neuroimage.2023.120354

[20] Dumas, G., Nadel, J., Soussignan, R., Martinerie, J., & Garnero, L. (2010). Inter-brain synchronization during social interaction. *PLoS ONE*, 5(8), e12166. https://doi.org/10.1371/journal.pone.0012166

[21] Xu, X., Kong, Q., Zhang, D., & Zhang, Y. (2024). An evaluation of inter-brain EEG coupling methods in hyperscanning studies. *Cognitive Neurodynamics*, 18, 67–83 (online 2022). https://doi.org/10.1007/s11571-022-09911-1

[22] Maris, E., & Oostenveld, R. (2007). Nonparametric statistical testing of EEG- and MEG-data. *Journal of Neuroscience Methods*, 164, 177–190. https://doi.org/10.1016/j.jneumeth.2007.03.024

[23] Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology*, 54(1), 146–157. https://doi.org/10.1111/psyp.12639

[24] Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A., Flint, J., Robinson, E. S. J., & Munafò, M. R. (2013). Power failure: Why small sample size undermines the reliability of neuroscience. *Nature Reviews Neuroscience*, 14, 365–376. https://doi.org/10.1038/nrn3475

[25] Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., et al. (2013). MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience*, 7, 267. https://doi.org/10.3389/fnins.2013.00267

[26] Nunez, P. L., & Srinivasan, R. (2006). *Electric Fields of the Brain: The Neurophysics of EEG* (2nd ed.). Oxford University Press.

[27] Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138. https://doi.org/10.1038/nrn2787

[28] Koch, C., Massimini, M., Boly, M., & Tononi, G. (2016). Neural correlates of consciousness: Progress and problems. *Nature Reviews Neuroscience*, 17, 307–321. https://doi.org/10.1038/nrn.2016.22

[29] Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E*, 61, 4194–4206. https://doi.org/10.1103/PhysRevE.61.4194

[30] Eberhard, P. H., & Ross, R. R. (1989). Quantum field theory cannot provide faster-than-light communication. *Foundations of Physics Letters*, 2, 127–149. https://doi.org/10.1007/BF00696109

[31] Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., Flandin, G., Phillips, C., Delorme, A., & Oostenveld, R. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*, 6, 103. https://doi.org/10.1038/s41597-019-0104-8

[32] Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

[33] Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359–1366. https://doi.org/10.1177/0956797611417632

[34] Clayson, P. E., Carbine, K. A., Baldwin, S. A., & Larson, M. J. (2019). Methodological reporting behavior, sample sizes, and statistical power in studies of event-related potentials: Barriers to reproducibility and replicability. *Psychophysiology*, 56, e13437. https://doi.org/10.1111/psyp.13437

[35] Buzsáki, G., & Draguhn, A. (2004). Neuronal oscillations in cortical networks. *Science*, 304(5679), 1926–1929. https://doi.org/10.1126/science.1099745

[36] Cohen, M. X. (2014). *Analyzing Neural Time Series Data: Theory and Practice*. MIT Press.

[37] Poldrack, R. A., Baker, C. I., Durnez, J., et al. (2017). Scanning the horizon: Towards transparent and reproducible neuroimaging research. *Nature Reviews Neuroscience*, 18, 115–126. https://doi.org/10.1038/nrn.2016.167

[38] May, E. C., Spottiswoode, S. J. P., & Faith, L. V. (2010). A methodological issue in the study of correlation between psychophysiological variables. *European Journal of Parapsychology*, 25, 5–24. An earlier version appeared in the *Proceedings of the 44th Annual Convention of the Parapsychological Association* (2001), 166–178; that version was not inspected.

[39] Grinberg-Zylberbaum, J., Delaflor, M., & Sánchez, M. E. (1989). El potencial transferido en el cerebro humano. *Revista Intercontinental de Psicología y Educación*, 2(1–2), 309–323. **Metadata from the reference lists of [4] and [5]; not inspected.**

[40] Grinberg-Zylberbaum, J., Attie, L., Cerezo, R., Schettino, L., Pérez, M., & Meraz, P. (1995). Electrofisiología de la interacción entre cerebros: Topografía del potencial transferido y la teoría sinérgica. *Revista Mexicana de Psicología*, 2(1), 33–53. **Volume as printed in [5]; metadata not independently verified; not inspected.**

[41] Attie, L. B. (1996). *Actividad electroencefalográfica y topografía cerebral en relación a la interacción humana: El potencial transferido* [Thesis]. Universidad Nacional Autónoma de México. **Metadata from the reference list of [5]; not inspected.**

[42] Grinberg-Zylberbaum, J. (1982). Psychophysiological correlates of communication, gravitation and unity. *Psychoenergetics*, 4, 227–256. **Metadata from [5]; [38] instead gives *Journal of Psychophysical Systems*; bibliographic conflict unresolved; not inspected.**

[43] Kittenis, M. D. (2008). *Event-related EEG correlations between physically isolated participants* [Doctoral thesis]. University of Edinburgh. https://era.ed.ac.uk/items/20d869e5-7690-4366-a04e-f573c1c6b2dc **Abstract reviewed only.**

[44] Tressoldi, P., Pederzoli, L., Bilucaglia, M., Caini, P., Fedele, P., Ferrini, A., Melloni, S., Richeldi, D., Richeldi, F., & Accardo, A. (2014). Brain-to-brain (mind-to-mind) interaction at distance: A confirmatory study. *F1000Research*, 3, 182, version 3. https://doi.org/10.12688/f1000research.4336.3

[45] Kittenis, M., Caryl, P. G., & Stevens, P. (2004). Distant psychophysiological interaction effects between related and unrelated participants. In S. Schmidt (Ed.), *Proceedings of the 47th Annual Convention of the Parapsychological Association*. Vienna.

[46] Sassenhagen, J., & Draschkow, D. (2019). Cluster-based permutation tests of MEG/EEG data do not establish significance of effect latency or location. *Psychophysiology*, 56(6), e13335. https://doi.org/10.1111/psyp.13335

# Appendix A. Synthetic Null Benchmark: Reproduction Instructions

This appendix contains the implementation used to generate the quantitative results in Section 7. It uses NumPy and SciPy; it neither downloads nor processes human EEG. The executed environment was **Python 3.12.15, NumPy 2.4.4, and SciPy 1.18.1**, pinned in `reproducibility/requirements_executed.txt`. Reproduction uses the fixed pseudo-random seed 20261025, and executed output should be compared with Table 3. The two bands are simulated sequentially from the same random generator; changing order or random-library version may change the finite-sample percentages.

```python
import numpy as np
from scipy.stats import t

rng = np.random.default_rng(20261025)
fs, n_samples, n_pairs = 256, 128, 5000

for low, high in ((13, 35), (4, 12)):
    freq = np.fft.rfftfreq(n_samples, d=1 / fs)
    keep = (freq >= low) & (freq <= high)
    a = rng.normal(size=(n_pairs, n_samples))
    b = rng.normal(size=(n_pairs, n_samples))
    xa = np.fft.irfft(np.fft.rfft(a, axis=-1) * keep,
                      n=n_samples, axis=-1)
    yb = np.fft.irfft(np.fft.rfft(b, axis=-1) * keep,
                      n=n_samples, axis=-1)
    xa -= xa.mean(axis=1, keepdims=True)
    yb -= yb.mean(axis=1, keepdims=True)
    xa /= np.linalg.norm(xa, axis=1, keepdims=True)
    yb /= np.linalg.norm(yb, axis=1, keepdims=True)
    r = np.sum(xa * yb, axis=1)
    stat = np.abs(r) * np.sqrt((n_samples - 2) / (1 - r * r))
    naive_p = 2 * t.sf(stat, n_samples - 2)
    corr_by_shift = np.fft.irfft(
        np.conjugate(np.fft.rfft(xa, axis=1)) *
        np.fft.rfft(yb, axis=1), n=n_samples, axis=1)
    shift_p = np.mean(
        np.abs(corr_by_shift) >=
        np.abs(corr_by_shift[:, :1]) - 1e-12,
        axis=1)
    print(low, high,
          np.mean(naive_p < 0.05),
          np.mean(shift_p <= 0.05))
```

**Expected output, rounded:** `13 35 0.4328 0.0454` and `4 12 0.6206 0.0508`. The purpose is to reproduce an error-calibration illustration, not to fit a theory to historical participants.

# Appendix B. Source and Claim Audit

| Claim or number | Traceable source | Permissible inference | Unresolved caution |
|:--|:--|:--|:--|
| 1981 paper title/pages | Elsevier/Crossref metadata [1] | Original conceptual theory exists; pages 201–210 | Container-title variant registered; no pre-space state equation recovered |
| 1987 communication study | Original journal PDF [2] | Correlation-pattern report exists | Same cage, about 50 cm apart; not sensory-isolated causality |
| 1992 journal issue | Journal archive [3] | Vol. 3, no. 3 confirmed | Full methods merit independent archival audit |
| Seven pairs and 14.5 m | Original 1994 facsimile [4] | Historical experimental specifications | Small, conditionally selected series; success count not given |
| Beckman and Grass / two computers | Original 1994 facsimile [4] | Not a documented single-ADC apparatus | Full ground and cable map absent |
| 1994 microsecond/millisecond conflict | Printed prose versus figure axes [4] | Timing notation is internally ambiguous | Raw timing or corrected original needed |
| 1994 nominal correlations | Original figures and results [4] | Sixteen-point coefficients; 48 reported overlapping windows | Adjacent windows share 15 values; 49 windows arithmetically possible |
| 1994 empirical-null critique | May et al. [38] | $r=0.70$ not rare under their independent-EEG null | Not a reanalysis of Grinberg's raw EEG; $Z=1.22$ is illustrative |
| 2003 Q-ratio deviation | Wackermann et al. [7] | A distinct receiver-side statistic was reported | Not copied receiver VEP morphology |
| 2008 null corrected power analysis | Ambach [12] | Negative for the sampled Q/power-type endpoint | Closest corrected test $p=.067$; not proof of absence |
| 20.1% and 26.2% false-positive rates | Ambach [12] | Monte Carlo result for earlier specified evaluation | Do not generalize to all EEG designs |
| Near-50% receiver classifiers | Bilucaglia et al. [14] | Small classification departures were reported | Participant-held-out generalization unestablished; pair-held-out results are sensitivity analyses only |
| 143 reports / 129 studies | Acunzo et al. [15] | Broader critical review scope | Not a direct Grinberg replication |
| 92 studies/reports | Batouli et al. [16] | Descriptive synthesis scope | No unified signature or pooled effect |
| 54 EEG social-interaction studies | Jiang et al. [17] | Ordinary task-linked IBS evidence | Different estimand from isolated receiver |
| 43.28%, 62.06%, 4.54%, 5.08% | This work, Appendix A | Synthetic null calibration result | Not historical or human empirical data |

# Appendix C. Preregistration Skeleton and Data Dictionary

A prospective registry entry should fix: (C1) primary hypothesis and contrast; (C2) target population and exclusion rules; (C3) independently randomized sender real/sham schedule and allocation concealment; (C4) receiver electrode region, reference, baseline, ERP latency, sender-derived template construction and freezing before receiver unblinding, primary $P_i$, and secondary $A_i$; (C5) acquisition calibration and timing-uncertainty bounds; (C6) acoustic, electromagnetic, vibration, optical, and ground-path controls; (C7) phantom and no-human negative controls; (C8) primary independent statistical unit and randomization test; (C9) planned effect-size precision and smallest effect of interest; (C10) multiplicity and secondary endpoints; (C11) analysis and code hashes; (C12) independent validation laboratory and lock-box rules; (C13) prospective publication of null, positive, and inconclusive results.

Each EEG recording should preserve `pair_id`, `participant_role`, `relationship_type`, `site_id`, `session_id`, `device_id`, `montage`, `reference`, `sampling_rate_hz`, `acquisition_start_utc`, `clock_offset_estimate_ms`, `clock_uncertainty_ms`, `event_id`, `condition_real_sham`, `stimulus_schedule_version`, `photodiode_onset`, `stimulator_current_monitor`, `receiver_light_monitor`, `receiver_audio_monitor`, `receiver_vibration_monitor`, `receiver_em_monitor`, `receiver_eog`, `receiver_emg`, `receiver_respiration`, `sender_behavior_log`, `raw_file_sha256`, `analysis_commit`, and `preregistration_id`. Protected human metadata should be separated from analysis identifiers. Any unavailable field must be marked missing rather than filled with a guessed default.

For the public archive, deposit the manuscript PDF, editable source, environment lockfile, synthetic benchmark script, reproduction output, figure assets, and a clear data-availability statement. Cite the archival DOI **only after** the actual Zenodo deposit creates one; do not preassign a fabricated identifier.


# Appendix D. Endpoint Taxonomy and Confound Audit Matrix

The table below condenses the operational logic of the manuscript into a review aid for external auditors.

| Question | Minimum evidence requirement | Common failure mode | Consequence if unresolved |
|---|---|---|---|
| Was the estimand stated clearly? | Explicit definition of receiver-side target (ERP, power, synchrony, classifier score) | Mixing endpoint classes under one narrative label | The study cannot be matched to prior claims |
| Was timing validated? | Hardware event markers, documented delays, and synchronized clocks | Post hoc timestamp reconstruction | Apparent effects may be alignment artifacts |
| Was isolation measured? | Documented shielding, room separation details, and logged environmental proxies | Assuming isolation from room labels alone | Alternative pathways remain live |
| Was the null calibrated to the signal structure? | Permutation, circular-shift, or hierarchical resampling justified for the endpoint | Using independent-sample formulas on autocorrelated data | Inflated significance and false positives |
| Were analysis choices locked? | Preregistered primary pipeline with versioned code | Researcher degrees of freedom across filters or windows | Results become difficult to interpret |
| Does validation match the generalization unit? | Participant-held-out primary folds for new-person claims; separately labeled pair- and session-held-out sensitivity analyses | Treating ordered pairings as independent people or leaving a held-out person's other recordings in training | Leakage and optimistic estimates of generalization |
| Were negative and inconclusive outcomes allowed? | Decision rule includes failure states and audit outputs | Selective reporting | Published evidence becomes biased toward dramatic claims |

A brief endpoint glossary is also useful.

- **Transferred potential:** a stimulus-locked averaged receiver waveform claimed to mirror the sender condition.
- **Receiver power effect:** a change in receiver spectral energy or band statistic after sender stimulation.
- **Inter-brain synchrony:** a dependence metric between two simultaneously recorded brains, often in social or shared-task settings.
- **Classifier outcome:** a predictive score obtained by training a model to distinguish sender conditions from receiver-derived features.
- **Leakage proxy:** any measured channel, such as sound level, electromagnetic field, or timing discrepancy, that could explain an observed association without invoking a novel biological pathway.
