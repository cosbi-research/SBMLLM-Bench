<a id='cee0b4c8-a48e-450e-bf75-d7d8163171b6'></a>

Journal of Theoretical Biology 335 (2013) 283–294

<a id='ed484b60-d77e-49ea-977b-a27716212f08'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a person and a tree, with text on a banner around the tree and the brand name below.::>

<a id='f36ea0ab-7665-4085-91e2-f52504928a60'></a>

Contents lists available at ScienceDirect

<a id='b251f489-395a-4e44-9db9-34d3d2ecb4f1'></a>

Journal of Theoretical Biology

<a id='42c7baca-2841-4c13-8823-8d4e5f2c547e'></a>

journal homepage: www.elsevier.com/locate/yjtbi

<a id='723b8697-7336-46e6-aeaf-39942d99a625'></a>

<::Cover of the "Journal of Theoretical Biology". The background is a marbled pattern in shades of green and cream. In the upper left corner, there is a small emblem with text that is not clearly legible. The title "Journal of Theoretical Biology" is prominently displayed in red serif font, with "Theoretical Biology" being larger than "Journal of".
: journal cover::>

<a id='0d24d289-794e-4abc-bfea-2055728c0674'></a>

On the effect of circadian oscillations on biochemical cell signaling by *NF* – *κB*

<a id='1194bc45-a199-4f9f-a961-567041a0c99a'></a>

<::logo: CrossMark
CrossMark
A circular blue icon with a red bookmark ribbon in the center.::>

<a id='9a673532-5ecf-4c5d-ac69-37bd571513cc'></a>

J.M. González-Miranda *
Departamento de Física Fundamental, Universidad de Barcelona, Av. Diagonal 647, 08028 Barcelona, Spain

<a id='aed44398-1263-4ada-b8f7-98092f64a2ab'></a>

AUTHOR - HIGHLIGHTS

* A mathematical model of a signaling pathway is modified to include circadian rhythms.
* New oscillatory behaviors appear from the interactions with the circadian clock.
* The dominant oscillatory behavior, although not the only one, is quasiperiodicity.
* Explanation of these new types of oscillations by means of spectral analysis is given.
* The results obtained are shown to be structurally stable.

<a id='5d0da500-545e-477c-a86f-fa0523bb6291'></a>

ARTICLE INFO
---
Article history:
Received 14 January 2013
Received in revised form
16 April 2013
Accepted 21 June 2013
Available online 29 June 2013
---
Keywords:
Signaling pathway
Circadian clock
Computational biology
Quasiperiodic motion
Spectral analysis

<a id='6b48bc9e-c606-42fd-b4c4-3926e12a799c'></a>

ABSTRACT
We report the results of a numerical investigation of a mathematical model for NF-̸B oscillations, described by a set of ordinary nonlinear differential equations, when perturbed by a circadian oscillation. The main result is that a circadian rhythm, even when it represents a weak perturbation, enhances the signaling capabilities of NF-̸B oscillations. This is done by turning rest states into periodic oscillations, and periodic oscillations into quasiperiodic oscillations. Strong perturbations result in complex periodic oscillations and even in chaos. Circadian rhythms would then result in a NF-̸B dynamics that is more complex than the simple oscillations and rest states, initially reported for this model. This renders it more amenable for information coding.

<a id='dfbabf52-34ec-411e-b8ac-2916db752753'></a>

 2013 Elsevier Ltd. All rights reserved.

<a id='b08403a2-d91f-46d0-80cc-dc90a6f148da'></a>

# 1. Introduction

There is experimental evidence (Hoffmann et al., 2002; Nelson et al., 2004; Park et al., 2006; Tay et al., 2010; Lee and Sankar, 2011) that oscillations in the concentration of nuclear factor κB proteins, NF-κB, in the nucleus and cytoplasm of a cell are involved in the control of immune and inflammatory responses, developmental processes, cellular growth, apoptosis, and several disease states. It is well known that the activity of NF-κB is regulated by inhibitory proteins κB, IκB. The experiments show an inverse relation between the frequency of the oscillations and the amount of IκB. Numerical simulations also show this relation (Hoffmann et al., 2002; Krishna et al., 2006). This suggests that oscillations in NF-κB control the expression of genes. The diversity of biological processes involving NF-κB suggest (Hoffmann et al., 2002; Nelson et al., 2004; Park et al., 2006; Tay et al., 2010; Lee and Sankar, 2011;

<a id='76ae40a4-3b3c-40f2-bc5f-2e5f822b4765'></a>

---* Tel.: +34 934021163. *E-mail address: jmgonzalezm@ub.edu*

<a id='9407e513-5e6e-4ad5-835c-2913b3874476'></a>

0022-5193/$-see front matter © 2013 Elsevier Ltd. All rights reserved.
http://dx.doi.org/http://dx.doi.org/10.1016/j.jtbi.2013.06.027

<a id='325b6868-f27b-41bf-9b37-611585abf194'></a>

Stavreva et al., 2012) that the functional consequences of
NF-κB signaling could be determined by the nature and proper-
ties of these oscillations, more that by the mere presence of
NF-κB.

<a id='83beda51-c932-4a7a-bf85-50aefa5e4e4f'></a>

Once we accept that the sensitive response of many biological processes to the presence of NF-κB is determined by the dynamic pattern of NF-κB oscillations we have a code problem (Goldbeter, 2002; Cai et al., 2008; Behar and Hoffmann, 2010). We need to know how the oscillations in NF-κB encode the command that tells the cell which particular response is to be delivered. A first approach would require to characterize the system dynamics. This can be done by means of exploratory studies of the dynamics of NF-κB aimed to obtain response to questions such as: when we have rest states? When we have sustained oscillations? Which particular features presents the oscillatory dynamics? Where we have chaos? An experimental realization of such approach is difficult and expensive. Otherwise, the resort to analytical or computational techniques, which are cheaper and easier to implement, provides a kind of knowledge able to be used later to more efficient design of experiments. Approaches of this kind are being

<!-- PAGE BREAK -->

<a id='db2667c2-64a0-4f76-83ad-9cf28c4d67ea'></a>

284

<a id='c0f68990-4cf1-42d9-9076-4e6cfd10de74'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='19de1800-62c5-4113-8be5-c327b3f94dc6'></a>

used in the problem of the neuronal coding (see, for example,
González-Miranda, 2007; Robinson et al., 2008; Watts et al., 2011;
González-Miranda, 2012 and references therein), which is a
related biological problem that deals with the information
encoded in the trains of action potential running along a neuron
axon.

<a id='f885b686-846a-4ae2-8bf1-853ea555ffdf'></a>

Regarding NF-κB signaling, Krishna et al. (2006) have presented a mathematical model for NF-κB oscillations addressed to contribute to the problem of NF-κB signaling along a theoretical approach. This is a reduced model, described by a system of three nonlinear ordinary differential equations, aimed to capture the essential mechanisms of NF-κB signaling. The Krishna, Jensen and Sneppen model (KJS model) results from the reduction of a high order model, consisting of twenty four differential equations, previously proposed by Hoffmann et al. (2002). Having a sound biochemical background it allows to get insight on the processes being modeled. If, once studied the simple _KJS_ model, one is interested in more detail, the results of such study would be a good starting point to go to more complex and detailed models, such as the full model of Hoffmann et al. (2002). An alternative is to treat other related biochemical process also as minimal oscillators, and deal the more complex case when these different oscillators are to be considered together by coupling these models (Goldbeter, 2002). In this case, concepts and techniques for coupled nonlinear oscillators (González-Miranda, 2004; Osipov et al., 2007) could be used.

<a id='f8e3d077-9ef3-4eef-97b9-44ce01327972'></a>

Depending on system parameters, the KJS model displays periodic sustained oscillations in nuclear NF-κB concentration, which may be spiky or soft, as well as damped oscillations to a rest state (Krishna et al., 2006). A numerical study of this model under pulse and periodic stimulations with frequencies of the same order of magnitude than the system intrinsic oscillations has been reported by Fonslet et al. (2007) adding chaotic oscillations to the periodic ones previously found. A theoretical and numerical study of the effect of inhibitory protein RKIP, modeled by means of the applications of constant and transient stimulations to the model, has been reported by Nikolov et al. (2009), showing a variety of periodic oscillations. Jensen and Krishna (2012) have studied the frequency synchronization of NF-κB oscillations operating in a ultradian regime to an oscillating tumor necrosis factor (TNF) external signal, also oscillating within the ultradian range. The dynamic behaviors reported were periodic phase-locked oscillations and chaos.

<a id='093be65b-9962-4c36-a616-943b4f535492'></a>

The research presented in this paper is aimed to take into account that living organisms are subject to a twenty four hours periodic perturbation, due to the Earths rotation. In most life forms, from microbes to mammals, this has resulted in the development of biochemical internal clocks with a twenty four hours period, know as circadian clocks (Edmunds, 1988; Harmer et al., 2001; Leloup and Goldbeter, 2004; Kulasiri et al., 2011; Liu and Wang, 2012). They are endogenous in the sense that they are insensitive to the particular details of a given day. Circadian clocks act as strong regulators, imposing circadian rhythms to biological activity at its different levels, from physiological to biochemical (Matsuo et al., 2003; Mullenders et al., 2009). Particularly, recent research by Lee and Sankar (2011) has provided experimental evidence of circadian clock regulation of apoptosis by means of NF-κB signaling in mammals.

<a id='756d0d49-1d8a-440b-99f5-88c0324b8f6c'></a>

The question then emerges of the effect of circadian oscillations on the signaling abilities of NF-κB oscillations. In this paper, we present an approach to this question. In particular, we report the result of a numerical investigation of the KJS model, subject to an external periodic perturbation of low frequency, corresponding to a circadian oscillation. Our aim is to provide some clues on the biological signaling capabilities of NF-κB oscillations. The layout of the paper is as follows. In Section 2, we present and discuss the

<a id='d4ed2428-d19c-439e-a411-8a4587f33bf1'></a>

model of NF-κB signaling that we will study. In Section 3, we present the main qualitative effects of a circadian rhythm on the oscillations described by the KJS model, and in Section 4, we provide further assessment and dynamical characterization of these effects. In Section 5, we provide a justification of the dynamic behaviors observed, grounded on a spectral analysis. In Section 6, we give a global view of the dynamical behaviors available to the KJS model subject to a circadian rhythm when their parameters are changed. In Section 7, we present our conclusions and discuss our results against other related studies found in the literature.

<a id='748f8023-4602-4943-a4e7-0af49a689c30'></a>

## 2. Model of NF-κB oscillations

The biochemical system studied here is the IκB—NF-κB signaling module working on eukaryotic cells. From a functional point of view, this module works as a signal transduction device whose inputs are signals created by external stimulus of the cell-membrane receptors and whose outputs are signals transmitted to the cell nucleus that regulate gene expression. In the IκB—NF-κB signaling system the nuclear factor κB, NF-κB, is a dimer protein complex that works as a transcription factor regulating the expression of hundreds of genes, and IκB (inhibitor of nuclear factor κB) stands for three isoform proteins whose association with NF-κB inhibit its transcription abilities. Conversely, among the capabilities of NF-κB there is the activation of genes that promote the synthesis of IκB. Under appropriate external stimulation, the IκB kinase complex (IKK) phosphorylates and degrades the IκB proteins, giving rise to a negative feed-back loop that results in oscillations of NF-κB nuclear concentration. These oscillations, which have been measured in experiments, appear to have a functional role regarding the diversity of processes that NF-κB can regulate.

<a id='ba7332b0-947c-41db-8f93-80b270061f92'></a>

We study here the three-variable model of NF-κB oscillations
by Krishna et al. (2006), which is a minimal mathematical model
for the nuclear NF-κB oscillations. The biochemical processes
described by this model are presented schematically in Fig. 1.
They work as follows: (i) NF-κB proteins are inactive in the cell
cytoplasm by association with IκB cytoplasmatic proteins, (ii) an
external stimulus activating the IκB kinase complex (IKK) results in
the degradation of cytoplasmatic IκB proteins and liberation of
NF-κB, (iii) this translocates to the cell nucleus, (iv) where it
regulates gene transcription by binding to one of a set of the so

<a id='d6d49b54-4bf7-4556-ae8e-89a371472856'></a>

<::Diagram: A cellular diagram illustrating the regulation and transport processes of NF-κB. A legend at the top left identifies: NF-κB (red blob), IκB (blue blob), and IKK (green square). The diagram shows a cell with a CELL MEMBRANE enclosing the cytoplasm, and a NUCLEAR ENVELOPE enclosing the nucleus.In the nucleus, DNA is shown. From the DNA, IκB mRNA is produced, leading to the Synthesis of IκB. NF-κB (red blob) is also present in the nucleus. IκB and NF-κB form a complex that is transported out of the nucleus, labeled "Bounded NF-κB transported to the cytoplasm".In the cytoplasm, this complex is referred to as "Cytoplasmatic IκB—NF-κB". IKK (green square) interacts with this complex, leading to the "Degradation of IκB" (represented by fragmented blue blobs). This process releases "Free NF-κB" (red blob), which then moves "back to the nucleus".A "Circadian rhythm" (represented by a 24-hour wave) is shown to influence the degradation process of IκB, acting on IKK.Fig. 1. Diagram showing the regulation and transport processes that determine the nonlinear dynamic of NF-κB in the KJS model (Krishna et al., 2006), with the assumption that the degradation rates of IκB oscillate driven by a circadian clock.::>

<!-- PAGE BREAK -->

<a id='c09c33fe-d367-4941-95be-e4c1000eb60d'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='6a5f8fb3-d9d6-4032-8644-b554634281ff'></a>

285

<a id='e55ae7fe-9b47-4b0c-8e90-dd5f67e59a53'></a>

called κB sites, (v) this process implies the synthesis of new IκB (IκB mRNA), (vi) which enters the nucleus to associate with nuclear NF—κB, (vii) the newly formed complex IκB—NF—κB translocates to the cytoplasm, then closing the cycle. Although the above processes can be described giving more detail of the biochemical reactions implied, then adding new equations, the dynamics just described appears to give a consistent description of the small core network driving the NF—κB oscillations.

<a id='7de96b17-0ce0-4460-95d1-4addc68befce'></a>

The formalization of these ideas results in a dynamical system that can be described by means of an autonomous three-dimensional system of nonlinear first-order differential equations, which reads (Krishna et al., 2006):

$\frac{dx}{dt} = A\frac{1-x}{\varepsilon+z} - B\frac{zx}{\delta+x}$ (1)

$\frac{dy}{dt} = x^2-y$ (2)

$\frac{dz}{dt} = y-C\frac{(1-x)z}{\varepsilon+z}$ (3)

<a id='78db3e1e-2325-4100-b5ec-4be3e02197f7'></a>

These equations are written in dimensionless form, so that the unit of time is equal to 0.980 h. The dynamic variables are the concentrations of three basic constituents: nuclear NF-κB (x), IκB mRNA (y), and cytoplasmatic IκB (z), which are dimensionless quantities. The parameters of the model (A, B, C, δ, ε) are dimensionless quantities given by the reaction constants (Krishna et al., 2006; Hoffmann et al., 2002).

<a id='234c6932-caff-4b3f-9dfa-c84838f7d8c8'></a>

In this paper we aim to study the case when the external stimulation triggering the NF-κB oscillations follows a 24 h circadian rhythm resulting from the organism adaptation to the Earth rotation. These rhythms are robust in the sense that they reproduce autonomously the day cycle, with independence of the environment conditions. The study of circadian rhythm is an open field of research with many facets to be considered (Goldbeter, 2002; Harmer et al., 2001). The biochemical mechanisms behind generation and maintenance of circadian rhythms are circadian clocks, which are biochemical oscillators generated by feed-back loops resulting from the self-regulation of genes by its protein products. There is a variety of such clocks, which have been found to work in many organisms, from cyanobacteria to mammals, with the possibility of being located in different organs and being of different kinds. They also regulate the rhythm of a variety of functions such as photosynthesis, cell division, hormone secretion and sleep cycles, among many others. An additional complexity in the study of the circadian rhythms is the path from the circadian clock to the regulation of intracellular processes, which is a complex downstream succession of biochemical events. A detailed experimental study of one of such networks, linking a cryto-chrome protein based circadian clock and the NF-κB signaling pathway regulating apoptosis in mince, has been presented recently by Lee and Sankar (2011).

<a id='0a4fe861-0505-4058-b7e6-8e1e753d5725'></a>

Having all this in mind, and within the reductionist approach mentioned in the paper introduction, where complex processes are decomposed in simpler minimal ones for their analysis, we make only a minimal modification to the _KJS_ model by assuming that the final output of a hypothetical circadian clock acting on a cell will be an external signal having a periodicity of 24 h (top right corner of Fig. 1). This signal is supplied to the IκB–NF-κB signaling module by the concentration of _IKK_. This enters the equations through the parameter _C_ that is proportional to the rate of degradation of IκB, which occurs after the phosphorylation of IκB by activated _IKK_. Therefore, _C_ is proportional to the intensity of the input signal driving the IκB–NF-κB signaling module. In the original _KJS_ model, this was a given constant. We will introduce the effect of an external periodic perturbation by treating _C_ as a time dependent function chosen to include the essential

<a id='baf85921-5eb8-48ba-9767-72d72a7256f5'></a>

experimental fact that circadian rhythms are robust in the sense
that they reproduce autonomously the day cycle. Our choice is

$C(t) = C_0[1 + \alpha \sin (\beta t)]$ (4)

<a id='6481121d-dcfb-4abe-baa5-e99fe1da008b'></a>

being C₀ the unperturbed value of C, α a dimensionless measure of
the strength of the perturbation, and β the angular frequency of its
oscillation. That means that we consider oscillations around C₀.
This function is a surrogate of the output of a complex network of
biochemical processes starting in the circadian clock.

<a id='a79dbaa2-2f50-435e-a932-960889beea8d'></a>

We note that, with this modification of the _KJS_ model, the system of equations (Eqs. (1)-(3)) stops being autonomous. However, it can be rendered autonomous again (Strogatz, 2001; González-Miranda, 2004) by defining the new variable, φ = βt, whose differential equation is dφ/dt = β. The resulting system of equations becomes four dimensional and autonomous. This has the advantage of allowing us the use concepts and methods of autonomous differential equations, while the new dimension adds only little complication because its differential equation is simple and independent of the others.

<a id='18e4c03a-9f92-48df-82cd-22f34d6a5073'></a>

Although, in Krishna et al. (2006), results for a wide set of parameter values were reported, a particular set deserved more attention as representative examples of the dynamic behavior observed. These are A=0.007, B=954.5, C=0.035 and δ = 0.029. Moreover, for the fifth parameter, two values were considered εS = 2.0 × 10-5 and εW = 5.0 × 10-4, which correspond to two qualitatively different types of oscillations called (Krishna et al., 2006) spiky oscillations and soft oscillations, respectively. We adhere to these parameter values in our investigation, using C0 = 0.035, and will add εR = 1.5 × 10-3, which corresponds to a rest state. Following Krishna et al. (2006), in the remainder of this paper, we will use the parameter E = -ln (ε), instead of ε. This is more convenient because the values of ε span over several orders of magnitude. Doing so, we will work with positive quantities of order 101, being the values of ε easily obtained from ε = exp(-E). The values of E, for the three dynamical states considered will be: ES = 10.82, EW = 7.60, and ER = 6.50.

<a id='576f77d9-7c6d-4fd8-8bb6-ff03ff5848a1'></a>

The question we address in this paper is how these dynamic states respond to a periodic perturbation whose frequency corresponds to a circadian rhythm. For the spiky oscillations observed at the above parameter values, the angular frequency is βs = 3.081 h⁻¹ (i.e., βs = 3.019 in reduced units), which means a period of Ts = 2.039 h. For soft oscillations, the correspondent values are βw = 7.482 h⁻¹ (i.e., βw = 7.332 in reduced units), and Tw = 0.840 h. For the rest state we have damped oscillations to a fixed point whose frequency is given by the imaginary part of the complex conjugate eigenvalues of this point. For the particular case considered the eigenvalues of the fixed point, in reduced units, are Λ = -8.291, and Λ± = -0.162 ± i · 6.696. Therefore, the damped oscillations of the rest state are characterized by a frequency βR = 6.832 h⁻¹ (i.e., βR = 6.696 in reduced units), and TR = 0.920 h. A circadian rhythm, having a frequency βC = 0.262 h⁻¹ (βC = 0.257 in reduced units), provides an example of an oscillation that is one order of magnitude smaller than that those characteristic of the NF-κB oscillations.

<a id='e724463f-5af7-4dd6-bb00-116733035b24'></a>

### 3. Circadian oscillations

We start our study by computing one-dimensional bifurcation diagrams and Lyapunov spectra for β = βc, and α∈[0, 1.0]. The one-dimensional bifurcation diagrams are obtained (Strogatz, 2001; González-Miranda, 2004) by plotting the values of the maxima of x(t), X, against α. In such diagrams, periodic orbits appear as discrete sets of points, while chaotic and quasiperiodic dynamics appear as approximately continuous lines. The spectrum of Lyapunov exponents, λ1≥λ2≥...≥λn, with n the dimension of the

<!-- PAGE BREAK -->

<a id='b9192bde-d33c-451d-8864-d2f76cb2b239'></a>

286

<a id='2f1975c2-0668-4992-ae2c-18896ef0c717'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='b40323e3-a7e5-462f-bcc5-229c091b3484'></a>

system, is computed using standard techniques for systems of differential equations (Wolf et al., 1985). This allows us to distinguish the different dynamic attractors available from the signs of the Lyapunov spectrum. For n=3 we have the following possible dynamics: chaotic (+,0,-), quasiperiodic (0,0,-), periodic (0,-,-), fixed point (-,-,-). For n=4 we have: hyperchaotic (+,+,0,-), chaotic (+, 0, -, -), quasiperiodic (0,0,-, -), periodic (0, -, -, -), fixed point (-, -, -, -). In our case, the fourth equation, dφ/dt = β, imposes a zero Lyapunov exponent, which the numerical technique renders exactly equal to zero (Wolf et al., 1985). We call this the compulsory-zero Lyapunov exponent and fix our attention in the other three, which will determine the kind of oscillatory dynamics that is to be observed. Our results for the perturbation of the three dynamic states said above are presented in Fig. 2.

<a id='3f6d7ba7-4352-42c2-81de-7a785d9623ed'></a>

<::chart: This figure, labeled "Fig. 2.", displays the dynamic behavior for the KJS model subject to a circadian rhythm under different perturbed states, characterized by the maxima of NF-kB oscillations (upper panels) and the three largest Lyapunov exponents (lower panels) as a function of α. The fourth Lyapunov exponent is negative with a large absolute value and is not shown, and the zero line observed in the lower panels is due to the compulsory-zero Lyapunov exponent calculation. The x-axis for all subplots is α, ranging from 0.0 to 1.0. The y-axis for the upper panels is X, and for the lower panels is λ. 

(a) Perturbed state is a rest state, E=6.50. 
- The upper panel shows green lines representing the maxima of NF-kB oscillations (X). X starts around 0.12, slightly increases, and then shows a bifurcation around α=0.8, fanning out into multiple branches as α approaches 1.0, reaching up to X=0.24. 
- The lower panel shows Lyapunov exponents (λ). A green line is near λ=0. A purple line (overlapping with red) starts near λ=-0.1, decreases to about λ=-0.6, and then shows red dotted points and a blue dashed line as α approaches 1.0, indicating more complex dynamics. A horizontal brown line is at λ=0.

(b) Perturbed state is a soft oscillation, E=7.60. 
- The upper panel shows green lines for X, starting around 0.25. The oscillations fan out into multiple branches, showing complex behavior and decreasing values as α approaches 1.0, ranging from X=0.0 to X=0.4. 
- The lower panel shows Lyapunov exponents (λ). A horizontal brown line is at λ=0. A blue line starts around λ=-0.9, increases to about λ=-0.4, then decreases again and becomes dotted blue as α approaches 1.0. Red dotted points appear as α approaches 1.0, indicating other exponents.

(c) Perturbed state is a spiky oscillation, E=10.82. 
- The upper panel shows green lines for X, starting around 0.6. The oscillations fan out into many branches, showing highly complex and chaotic behavior, with values ranging from X=0.0 to X=0.6. 
- The lower panel shows Lyapunov exponents (λ). A horizontal brown line is at λ=0. A blue line starts around λ=-0.9, increases to about λ=-0.4, then decreases and becomes dotted blue as α approaches 1.0. Red dotted points appear as α approaches 1.0, showing some positive values for λ, indicating chaotic dynamics.::>

<a id='58ff66df-7e49-4d09-97c3-9367b6b7173b'></a>

A circadian rhythm imposed on the rest state ($E_R = 6.50$) results in a oscillatory state. The bifurcation diagram, shown in the upper panel of Fig. 2(a), shows a simple periodic oscillation for almost all values of the strength of the perturbation, $\alpha$, except for large values ($\alpha\geq0.83$) where the signature observed is that of a complex oscillation, with multiple maxima. The Lyapunov spectrum, presented in the lower panel of Fig. 2(a), is in good agreement with the bifurcation diagram, showing that all exponents, except the compulsory-zero, are negative. This is again a signal of periodic oscillations.

<a id='e9548a16-2cf1-4058-9006-440d6b520595'></a>

The perturbation of a soft oscillation (Ew = 7.60), may result in two types of oscillatory dynamics as shown in Fig. 2(b). For small and medium values of the perturbation (a≤0.87), the bifurcation diagram shows an approximately continuous homogeneous band, which increases in wide with increasing a; while the Lyapunov spectrum is made of two null exponents and two negative exponents. These are signatures of quasiperiodic motion. For large values of a, we see signatures of complex periodic oscillations characterized again by multiple maxima.

<a id='210ecdaf-b7dc-4528-b1fa-d0a9e5330ecb'></a>

The effects of the perturbation on spiky oscillations (Es = 10.82) are illustrated in Fig. 2(c). For small and medium values of the perturbation strength (a≤0.85) we observe again the signatures of quasiperiodic motion in both, bifurcation diagram and Lyapunov spectrum. For large values of a, the dynamics becomes chaotic with periodic windows interspersed.

<a id='ca8013fd-74ee-4492-b100-198338b7d366'></a>

For a better understanding of these bifurcation diagrams, in
Figs. 3 and 4, we present examples of NF-κB oscillations at
selected values of α. The response of the rest state to the circadian
rhythm is illustrated in Fig. 3(a). There, we see two simple wavy
oscillations for small and medium values of α, and a complex
multipeaked oscillation for a large value of α. Fig. 3(b) illustrates

<a id='c8863e9a-442b-41d0-85a9-ed7e581f7ffd'></a>

<::chart: The image displays a figure labeled 'Fig. 3. NF-κB oscillations for a circadian perturbation of: (a) a rest state, E=6.50, (b) a soft oscillation, E=7.60. In (a) we see a dashed line for the value of the coordinate of the fixed point and oscillations of increasing amplitude and complexity as the intensity of the perturbation increases. In (b) we see the non-perturbed soft oscillation (α=0.00), a quasiperiodic oscillation (α=0.50), and a periodic oscillation (α = 0.88).'

The figure contains two main panels, (a) and (b).

Panel (a) shows a plot with 'x' on the y-axis (ranging from 0.00 to 0.20) and time 't' on the x-axis (ranging from 0.0 to 90.0). It displays three colored lines representing oscillations for different α values, along with a dashed black line indicating a fixed point. The red line is labeled "α=0.1", the green line "α=0.5", and the blue line "α=0.9". The oscillations increase in amplitude and complexity as α increases.

Panel (b) consists of three stacked subplots, each showing 'x' on the y-axis (ranging from 0.0 to 0.3) and time 't' on the x-axis (ranging from 0.0 to 60.0). Each subplot represents a different α value:
- The top subplot, labeled "α=0.00", shows a black line with consistent, rapid oscillations.
- The middle subplot, labeled "α=0.50", shows a blue line with quasiperiodic oscillations, where the amplitude varies over time.
- The bottom subplot, labeled "α=0.88", shows a green line with periodic oscillations that exhibit larger, distinct peaks and troughs.:>


<!-- PAGE BREAK -->

<a id='6f02202b-fbeb-454c-8318-368a8990b84d'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283-294

<a id='795755db-3964-4aa9-98e4-4ce4f93fa088'></a>

287

<a id='2a277652-30bf-4652-bddd-d64f481eafe1'></a>

<::chart: A multi-panel line chart showing NF-κB oscillations for different perturbation intensities. All panels share a common x-axis labeled 't' ranging from 0.0 to 90.0, and a common y-axis labeled 'x' ranging from 0.0 to 0.6. The panels are: (a) Black line showing non-perturbed spiky oscillations with consistent amplitude and frequency (α=0.00). (b) Cyan line showing quasiperiodic motion in a thin torus, with spiky oscillations exhibiting slight, regular amplitude modulation (α=0.20). (c) Blue line showing quasiperiodic motion in a thick torus, with spiky oscillations exhibiting more pronounced, regular amplitude modulation over longer periods (α=0.60). (d) Green line showing modulated periodic oscillations, with spiky oscillations exhibiting strong, regular amplitude modulation, forming distinct periodic envelopes (α=0.85). (e) Red line showing modulated chaotic oscillations, with spiky oscillations exhibiting irregular and complex amplitude modulation (α=0.96). Fig. 4. NF-κB oscillations for a circadian perturbation of a spiky oscillation for values of the intensity of the periodic perturbation giving rise to: (a) non-perturbed spiky oscillations, α=0.00, (b) quasiperiodic motion in a thin torus, α=0.20, (c) quasiperiodic motion in thick torus, α=0.60, (d) modulated periodic oscillations, α=0.85 and (e) modulated chaotic oscillations, α=0.96.::>

<a id='36a2e722-4ee3-41fc-a703-2971811a419d'></a>

the response of the soft oscillation. The upper panel shows the soft
oscillation itself (non-perturbed state), the medium panel shows
an oscillation in the quasiperiodic regime, which is characterized
by a high frequency periodic oscillation, whose amplitude is
modulated by other low frequency periodic oscillation. The peri-
odic oscillation in the lower panel is similar to the complex
periodic oscillation in the rest state, where a simple nearly
sinusoidal oscillation has superimposed a large frequency oscilla-
tion (with a greater amplitude, in this case).

<a id='c879bf3e-c94f-4055-938c-00da4ee4c796'></a>

Regarding the effect of the circadian rhythm on the spiky oscillation, the time series for the non-perturbed case appears in Fig. 4(a). Quasiperiodic oscillations appear in Fig. 4(b)-(c), and again show up as low frequency modulation of the high frequency spiky oscillation. The periodic oscillation in Fig. 4(d) can be described as a burst containing 22 spikes that repeats itself with a period T≈24.7. The chaotic oscillation in Fig. 4(d) is quite similar to the periodic oscillation, except that it is aperiodic as clearly seen by paying attention to details such as the two smaller spikes in each burst.

<a id='ecb93ff5-73b5-4e8d-881a-c848907ed05f'></a>

## 4. Quasiperiodic dynamics

We have performed some additional tests to assess the above picture. First we have computed Poincaré maps (González-Miranda, 2004; Strogatz, 2001) for several values of ε and α. Illustrative results are presented in Fig. 5. The calculation of Poincaré maps is a classic test for the dynamic behavior of a dynamical system (Glazier and Libchaber, 1988). To compute Poincaré maps we have worked in the three dimensional space described by the variables of the KJS model, (x,y,z). In this space we consider a surface of section, which is a surface that is crossed by the trajectory, [x(t), y(t), z(t)], that describes the full dynamics of the KJS model. The Poincaré map is made by the set of points where the trajectory intersects the surface of section. Different kinds of dynamics have different signatures in terms of Poincaré maps. In the present case we have a dynamical system characterized by two frequencies: the frequency of the circadian rhythm, βc, and the natural frequency of the NF-κB oscillations, which can be damped, βR, or sustained, βW or βS. Consequently, besides simple periodic oscillations we can expect a variety of trajectories in the (x,y,z) space and then a variety of Poincaré maps (González-Miranda, 2004; Strogatz, 2001; Glazier and Libchaber, 1988).

<a id='aa3a6483-2498-4b86-95d7-aebbfa8cb514'></a>

A simple periodic trajectory, characterized by a single fre-quency of oscillation, cuts the surface of section always at the same point; then, the Poincaré map is a single point. When the trajectory is characterized by two frequencies the kind of dynamic obtained is called motion in a torus because the trajectory occurs on a doughnut shaped surface. Depending on whether the quo-tient between these frequencies is an irrational or a rational number, we have quasiperiodic oscillations or combination oscil-lations, respectively. For quasiperiodic oscillations the trajectory is said to be ergodic, meaning that the motion is aperiodic, occurring on a curve that never closes, and such that all points of the torus are visited by the trajectory at some time. In this case, the intersection of the trajectory with the surface of section is the same than the intersection of the torus with the surface of section; therefore the Poincaré map is a closed curve. In the case of combination oscillations the two frequencies are entrained, this resulting in complex closed periodics orbits lying on the surface of the torus. This trajectory is not ergodic and cuts the surface of section in a well defined discrete set of points, located on the closed curve that results from the intersection between the torus and the surface of section. Chaotic dynamics occurs on strange attractors, which are fractal sets of points, whose intersection with the surface of section and, consequently, its Poincaré map is a two-dimensional fractal set of points. Because of the well know route to chaos through quasiperiodicity (González-Miranda, 2004; Strogatz, 2001; Glazier and Libchaber, 1988), we expect to observe chaos in our system. In this case, the strange attractor associated to chaos would take the form of a broken torus, and the Poincaré map would look like a broken closed curve.

<a id='432462fa-21c6-425b-b0e2-9c9b0fadd8d3'></a>

For the results displayed in Fig. 5 the surface considered was a plane, orthogonal to the x-axis, and containing the stable rest state. Poincaré maps for the perturbation of the rest state, presented in Fig. 5(a) are in good agreement with the results in the above section. For a very weak perturbation, the trajectory cuts the plane in a single point very close to the equilibrium point, which is indication a cycle tightly surrounding the rest state. For a perturbation of medium strength, we obtain a single point located further from the equilibrium point suggesting an ample cycle around the rest state. For a strong perturbation we have several points, being an indication of a periodic cycle with a complex structure and then of combination oscillations resulting from frequency entrainment.

<a id='41ca95ac-7330-4c0d-b468-789bcbd591da'></a>

The results of perturbing a soft oscillation are shown in Fig. 5(b).
The unperturbed case shows up as a single point, which corresponds

<!-- PAGE BREAK -->

<a id='7a0b8c25-3900-4642-b9ae-11b9adfd24df'></a>

288

<a id='ec5892dc-37ef-4c2d-9749-104c404e655c'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='a47ae609-51a1-4545-b2b1-02b9f3d09c97'></a>

<::Poincaré maps: chart::>Fig. 5. Poincaré maps for NF-κB oscillations under a circadian perturbation of: (a) a rest state, E=6.50, (b) a soft oscillation, E=7.60 and (c) a spiky oscillation, E=10.82. The strength of the perturbation, given by α, is indicated in the labels of each set of points. The surface of section is the plane orthogonal to the x-direction that contains the equilibrium point, indicated by a cross in each graph. (a) A scatter plot with y-axis 'z' ranging from 0.0021 to 0.0022 and x-axis 'y' ranging from 0.01 to 0.02. The plot shows points for α=0.10 (red dots), α=0.50 (green dots), and α=0.90 (blue dots). A black cross marks the equilibrium point near (0.015, 0.00215). (b) A scatter plot with y-axis 'z' ranging from 0.0025 to 0.0035 and x-axis 'y' ranging from 0.02 to 0.04. The plot shows points for α=0.00 (black dots), α=0.50 (blue dots forming a closed loop), and α=0.88 (green dots). A black cross marks the equilibrium point near (0.025, 0.0025). (c) A scatter plot with y-axis 'z' ranging from 0.002 to 0.008 and x-axis 'y' ranging from 0.00 to 0.08. The plot shows points for α=0.00 (black dots), α=0.20 (light blue dots forming a loop), α=0.60 (blue dots forming a loop), α=0.85 (green dots), and α=0.96 (red dots forming a loop). A black cross marks the equilibrium point near (0.025, 0.0028).

<a id='c5fdff2d-3c4c-4f59-9afc-9523d098a2c8'></a>

to a simple cycle. A medium perturbation results in a continuous closed curve around that point, indicating quasiperiodic motion. A strong perturbation results again in a discrete set of points laying on a closed curve that surrounds the non-perturbed cycle. This is the characteristic sign of frequency entrainment, and then of a periodic combination oscillation.

<a id='5e37aabf-3131-4e14-9a60-dd83f169bfd4'></a>

The perturbation of a spiky oscillation results in a more complex response as shown in Fig. 5(c). For the unperturbed case we see the single point characteristic of the simple cycle, weak and medium perturbations results in closed curves, surrounding this point, which are characteristic of quasiperiodic motion. For large perturbations we see again a discrete set of points on a closed curve, signal of periodic combination oscillation, or a complex set of points that is the signature of chaos. In this last case the Poincaré map looks like a broken closed curve, as expected.

<a id='76259b4e-21ac-49f1-b2c3-d1111f681b84'></a>

For better understanding and assessment of these results on Poincaré maps, in Figs. 6 and 7 we present plots of trajectories in the (x, y, z) space, together with details of the calculation of Lyapunov exponents. Trajectories appear as projections on the plane y–z. The trajectory points are colored black when above the surface of section considered in Fig. 5, and gray when bellow. The Poincaré maps in Fig. 5 have also been included in this plot. This technique of visualization is useful to get a three-dimensional idea of the trajectory (González-Miranda, 2010). Regarding Lyapu- nov exponents, because they are computed numerically by aver- aging over a sample (Wolf et al., 1985), it is interesting to watch out how the value obtained changes with the size of the sample. This is useful to unambiguously distinguish no-null Lyapunov exponents with a very small absolute value from legitimate zero Lyapunov exponents. The difference is given by the dependence of the Lyapunov exponent value with the size of the sample. This is a decreasing potential law for the zero exponent, while the no-null exponent tends to become constant. Double logarithmic plots make easy this distinction. This test tells us that the quasiperiodic motion reported is really quasiperiodic, and not some sort of complicated or atypical periodic motion. The results for negative and positive exponents, also asses the periodic or chaotic nature of the correspondent oscillations.

<a id='76dedb80-0be6-4e18-8772-60bdbca499cf'></a>

Results for a medium strength perturbation of a rest state show the resulting simple cycle [Fig. 6(a)], ever crossing in a single point.
For a strong perturbation, we again see periodic combination

<a id='cefc5fdc-abaf-4abc-a486-c8efb37306f7'></a>

oscillations [Fig. 6(b)], crossing several times the surface of section.
In the two cases, the evolution of the Lyapunov exponent is typical
of no null negative exponents [Fig. 6(f,g)].

<a id='d8c6f576-514e-45f5-9e54-5249f99b4772'></a>

A non-perturbed soft oscillation, shown in Fig. 6(c), is a simple cycle, whose exponents are computed in a three-dimensional space. Then the first one has to be null, as seen by the exponential decay, while the second is no null and negative, [Fig. 6(h)]. For a medium perturbation [Fig. 6(d)] we see motion in a torus, with the trajectory ergodically covering its surface. We observe how the torus surrounds the unperturbed cycle, being the Poincaré map a intersection of the surface of section with the surface of the torus. For a strong perturbation, Fig. 6(e) shows again a periodic entrained non-ergodic motion on a torus surface. Again, in the two cases we see the expected behavior for the relevant Lyapunov exponents in Fig. 6(i,j).

<a id='d32f5d44-e44f-45dc-a2e6-058511244912'></a>

Fig. 7 presents an analogous study for the perturbation of the spiky oscillation. Again we start in Fig. 7(a,f) with the unperturbed case, which is analogous to the case shown in Fig. 6(c,h). The torus that develops around this cycle for a weak perturbation is illustrated in Fig. 7(b,g), and a thicker one for a medium perturba- tion in Fig. 7(c,h). The periodic combination oscillations for a strong perturbation in Fig. 7(d,i) are quite similar to those for the soft oscillation. Finally, we see in Fig. 7(e,j) an example of the chaotic motion in a broken torus that also develops for strong perturbations.

<a id='614e9e2a-a9fa-4d67-8064-d93cd3779c75'></a>

## 5. Spectral analysis

A justification of the periodic, quasiperiodic and chaotic behavior observed can be provided by a spectral analysis of the dynamics (González-Miranda, 2002a,b). This is performed by means of the study of the one-sided power spectral density (Press et al., 1996) of x(t),

<a id='9ddd530e-eab5-4e4c-844b-2592dbaa676f'></a>

P(ω) = 2|∫₀^∞ x(t)e^(iωt) dt|²

<a id='ea77c8cb-1c48-43b6-9206-250444bacb82'></a>

which provides a quantitative information of the relative impor-
tance of the different oscillatory motions that compose the system
dynamics. Research on chaos suppression by periodic driving
(González-Miranda, 2002a), and on chaos synchronization by

<!-- PAGE BREAK -->

<a id='3e50c78b-afde-4037-b382-7d28171fb6cb'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283-294

<a id='b2119c46-551d-4f19-834e-be1e8e33d6ab'></a>

289

<a id='c729a935-9386-43fa-ab8c-c1bf299d66ae'></a>

<::figure: A multi-panel figure showing the characterization of the dynamic behavior of a perturbed NF-κB oscillator. The figure consists of two rows of plots, labeled (a) through (j). The first row (a-e) shows phase space plots (z vs y), and the second row (f-j) shows Lyapunov exponents (log |λ| vs log t). A Poincaré map is plotted together with the trajectories in the phase space plots. The figure explores different oscillation states based on the α parameter.  (a) Phase space plot for simple periodic oscillations (α=0.50), showing a small black loop with a green point, and a gray trajectory leading to it. E=6.50.  (b) Phase space plot for complex periodic oscillations (α=0.90), showing a more intricate black loop with green points, and a gray trajectory.  (c) Phase space plot for periodic oscillations of the unperturbed soft oscillation (α=0.00), showing a black loop with a green point and a black cross, and a gray trajectory. E=7.60.  (d) Phase space plot for quasiperiodic oscillations (α=0.50), showing a dense black region forming a wider loop, with green points along the outer edge, and a gray trajectory.  (e) Phase space plot for periodic oscillations (α=0.88), showing a black trajectory forming a loop with green points, and a gray trajectory.  (f) Lyapunov exponent plot for simple periodic oscillations, showing two lines (red and blue) converging to λ₃=-0.165 and λ₂=-0.165.  (g) Lyapunov exponent plot for complex periodic oscillations, showing two lines converging to λ₃=-0.508 and λ₂=-0.508.  (h) Lyapunov exponent plot for periodic oscillations of the unperturbed soft oscillation, showing two lines converging to λ₃=-0.949 and λ₁=0.  (i) Lyapunov exponent plot for quasiperiodic oscillations, showing two lines converging to λ₃=-0.582 and λ₂=0.  (j) Lyapunov exponent plot for periodic oscillations, showing two lines converging to λ₃=-0.282 and λ₂=+0.026.  The x-axis for plots (a-e) is 'y' and for plots (f-j) is 't'. The y-axis for plots (a-e) is 'z' and for plots (f-j) is '|λ|'.::>Figure 6. Characterization of the dynamic behavior of a perturbed NF-κB oscillator in a rest state and in a state of soft oscillations as given by means of phase space plots (first row) and Lyapunov exponents (second row). (a,f) Simple periodic oscillations and (b,g) complex periodic oscillations for a rest state. (c,h) Periodic oscillations for the unperturbed soft oscillation. (d,i) Quasiperiodic oscillations and (e,j) periodic oscillations for a perturbed soft oscillation. A Poincaré map is plotted together with the trajectories. (a) α=0.50, (b) α=0.90, (c) α=0.00, (d) α=0.50, (e) α=0.88.

<a id='234b3ee1-b4f3-482e-87cb-532c75fa029b'></a>

<::figure: A multi-panel figure titled "Fig. 7. Characterization of the dynamic behavior of a perturbed NF-κB spiky oscillations by means of phase space plots (first row), and Lyapunov exponents (second row). The strength of the perturbation increases from left to right giving rise to: (a) periodic oscillations, α=0.00, (b) quasiperiodic oscillations in a thin torus, α=0.20, (c) quasiperiodic oscillations in a thick torus, α=0.60, (d) periodic combination oscillations, α=0.85 and (e) chaotic oscillations in a broken torus, α=0.96. A Poincaré map is plotted together with the trajectories." The figure is composed of two rows of five plots each, labeled (a) through (j). The first row, (a) through (e), displays phase space plots of 'z' versus 'y'. The second row, (f) through (j), displays Lyapunov exponents '|λ|' versus 't'.

First row, phase space plots (y-axis: z, x-axis: y):
- (a) Periodic oscillations (α=0.00): A plot showing a single closed black trajectory and a gray trajectory, with a '+' marker at approximately y=0.025, z=0.003. The y-axis ranges from 0 to 0.06 and the z-axis from 0 to 0.020.
- (b) Quasiperiodic oscillations in a thin torus (α=0.20): A plot showing a black trajectory, a wider gray region indicating a torus, and green points representing the Poincaré map. A '+' marker is visible at approximately y=0.025, z=0.003.
- (c) Quasiperiodic oscillations in a thick torus (α=0.60): A plot showing a black trajectory, a broader gray region indicating a thick torus, and green points for the Poincaré map.
- (d) Periodic combination oscillations (α=0.85): A plot showing multiple black and gray trajectories forming a more complex pattern, with green points for the Poincaré map.
- (e) Chaotic oscillations in a broken torus (α=0.96): A plot showing numerous black and gray trajectories spread across a region, suggesting a broken torus, with green points for the Poincaré map.

Second row, Lyapunov exponents plots (y-axis: |λ| (log scale from 10^-8 to 10^2), x-axis: t (log scale from 10^1 to 10^4)):
- (f) A plot with a blue curve and a red curve. Labels indicate λ3 = -0.136 and λ1 = 0.
- (g) A plot with a blue curve and a red curve. Labels indicate λ3 = -0.128 and λ2 = 0.
- (h) A plot with a blue curve and a red curve. Labels indicate λ3 = -0.183 and λ2 = 0.
- (i) A plot with a blue curve and a red curve. Labels indicate λ3 = -0.410 and λ2 = -0.057.
- (j) A plot with a blue curve and a red curve. Labels indicate λ3 = -0.745 and λ2 = +0.052.::>

<a id='a94c8e60-25fc-4f2f-a5eb-24f78702a812'></a>

periodic driving or mutual coupling (González-Miranda, 2002b) has show that a variety of dynamic behaviors can be understood when analyzed in Fourier space by means of the power spectral density. Two basic mechanisms have been identified: the excitation of new motions with frequencies around that of the excitation (and its harmonics), and the rearrangement of power spectra structures around the dominant frequencies (González-Miranda, 2002a,b). With this aim, for each of the three perturbed states considered, we have computed the power spectral densities as functions of a displayed in Figs. 8–10. We present them as 2–D color plots in the

<a id='81574cc6-a9af-4822-aef2-d02d862aac34'></a>

plane ω-α. Moreover, 1-D plots, for selected values of α are also
given to ease interpretation.

<a id='e710056a-b84b-4b06-be00-523ef88cbe09'></a>

The perturbation of the fixed point [Fig. 8] results in the rise of an oscillation with a frequency equal to that of the perturbation, which is the frequency of the circadian rhythm, βc = 0.257. This oscillation becomes enhanced as new harmonics of βc, with frequencies ωn=nβc, being n = 2,3,4,..., are excited with the increase of the strength of the perturbation. For small and medium strength of the perturbation, the harmonics are excited consecutively from n=2 up, and the height of the correspondent peaks

<!-- PAGE BREAK -->

<a id='551e78a2-ad1c-4a49-abcd-43a41045cf8e'></a>

290

<a id='8d196e34-c2cc-4aa0-bac2-3d7a0669d558'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='01d7542b-12df-4e79-8522-1839542e76e3'></a>

a<::2D color plot labeled 'a'. The x-axis is labeled 'ω' and ranges from 0.0 to 10.0. The y-axis is labeled 'α' and ranges from 0.0 to 1.0. A color bar at the top indicates 'P' values, ranging from 10^-14 (dark blue) to 10^-4 (red), with intermediate values 10^-12, 10^-10, 10^-8, 10^-6. The plot shows a gradient of colors from blue to green to yellow and red.::>b<::xy-plot labeled 'b'. The x-axis is labeled 'ω' and ranges from 0.0 to 10.0. The y-axis is labeled 'P' on a logarithmic scale, ranging from 10^-20 to 10^-5. Three lines are plotted: a red line representing 'α = 0.10', a green line representing 'α = 0.50', and a blue line representing 'α = 0.90'. The curves are shifted vertically to avoid overlapping.::>Fig. 8. Power spectral density of a NF−κB oscillator in a rest state under a circadian perturbation: (a) 2D color plot showing the dependence on α (vertical axis), and (b) xy-plots of selected P(ω) functions, with the several curves shifted down as α increases to avoid overlapping. In both panels a logarithmic scale is used for P(ω). (For interpretation of the references to color in this figure caption, the reader is referred to the web version of this paper.)

<a id='03c0125c-b87c-47f5-adf0-7889fed2c014'></a>

decreases with _n_, indicating its lower presence in the oscillation
generated. This gives rise to the simple oscillations seen in Fig. 3(a)
and the cycle in Fig. 6(a).

<a id='7425a8a8-8313-4f34-8a43-402111543be8'></a>

When the perturbation becomes strong (α≥0.83) the new frequencies excited happen to be around the frequency characteristic of the damped oscillation that occurs for the unperturbed state, βR = 6.696. A resonance phenomenon occurs in this range of frequencies giving rise to higher peaks in P(ω) around βR. This results in the complex oscillation in Fig. 3(a), and the complex cycle in Fig. 6(b), which describe an oscillatory motion composed of two oscillations, a main one with the frequency of the perturbing circadian rhythm, and a second close to the natural oscillation of the system being perturbed. Because all peaks observed correspond to frequencies that are harmonics of βC, this complex oscillation is a case of entrainment of the frequency of the NF-κB oscillations to the circadian rhythm.

<a id='b2fdefe9-248a-4d7b-b5b8-1cf57930b76d'></a>

The spectral analysis of the perturbation of the oscillatory states presents a different scenario, shown in Figs. 9 and 10, for soft and spiky oscillations respectively. For very weak perturba-tions, in the two cases, P(ω) presents two peaks, one at βc and other at the frequency of the unperturbed oscillation, βw = 7.332 or βs = 3.019, for soft and spiky oscillations respectively. Increase of the perturbation, within the weak and medium strength range, results in the excitation of harmonics of βc, and harmonics and subharmonics of βw or βs, whose importance decreases from the correspondent frequency. The harmonics associated to each of the main frequencies are well separated by a gap where P(ω)≈0. The scenario is one in which we have two nearly independent oscillations, with two dominant frequencies: the frequency of the circadian rhythm, and other frequency close to natural fre-quency of the NF-κB oscillation. This results in the quasiperiodic

<a id='a17e8d3e-76b6-4abf-b414-15d7facaed08'></a>

<::Figure: The image contains two plots, (a) and (b), illustrating the power spectral density of an NF-κB soft oscillation under a circadian perturbation. (a) is a 2D color plot with 'ω' on the x-axis ranging from 0.0 to 10.0, and 'α' on the y-axis ranging from 0.0 to 1.0. A color bar at the top indicates 'P' values on a logarithmic scale from 10^-11 (dark blue) to 10^-2 (red). The plot shows intricate patterns of varying power spectral density across the ω and α ranges. (b) consists of three xy-plots of selected P(ω) functions. The x-axis is 'ω' from 0.0 to 10.0, and the y-axis is 'P' on a logarithmic scale from 10^-20 to 10^-5. There are three distinct curves, each corresponding to a different 'α' value: α = 0.00 (black line, highest), α = 0.50 (blue line, middle), and α = 0.88 (green line, lowest). Each curve displays multiple peaks and troughs, with the curves progressively shifted downwards as α increases to prevent overlapping. Both panels use a logarithmic scale for P(ω).::>Fig. 9. Power spectral density of a NF-κB soft oscillation under a circadian perturbation: (a) 2D color plot showing the dependence on α (vertical axis), and (b) xy-plots of selected P(ω) functions with the several curves shifted down as α increases to avoid overlapping. In both panels a logarithmic scale is used for P(ω). (For interpretation of the references to color in this figure caption, the reader is referred to the web version of this paper.)

<a id='788509b3-e92b-41d8-8d11-846d7c851a8a'></a>

dynamics described by the composition of two cycles: a main cycle close to the unperturbed one [Figs. 6(c) and 7(a)], and a second cycle close to the closed curve in the surface of section [Fig. 5(b,c)]. This shows up as the motion in a torus seen in Figs. 6(d) and 7(b,c), and the modulated NF-kB oscillations seen in Figs. 3(b) and 4(b,c).

<a id='dda6a3e5-5e31-4461-b330-f1268ba7bd6f'></a>

For strong coupling these two oscillations collide and become entrained. This means that the applied external rhythm becomes dominant in the sense that all frequencies observed are harmonics of βc. Once the system has entrained to the perturbation, we have a nonlinear oscillator characterized by a certain dominant frequency, as many of those studied in the literature on nonlinear dynamics and chaos (Strogatz, 2001; González-Miranda, 2004).
Depending on parameter values, it can display periodic or chaotic dynamics as occurs in many nonlinear systems of this kind. However, the resulting dynamics, periodic or chaotic, is one of a especial type. This is because the harmonics occurring in the neighborhood of the frequency of the unperturbed system, βW or βS, have a relatively high importance, then giving rise to modulated periodic or chaotic NF-κB oscillations as those shown in Figs. 3(b) and 4(d,e). The correspondent attractors occur on a torus, as those in Figs. 6(e) and 7(d) or on a broken torus as that in Fig. 7(e).

<a id='b416b89a-5376-417f-bdc2-8ee8063da859'></a>

## 6. Structural stability
Along this paper we have focused on a particular value of the driving frequency, which corresponds to a circadian rhythm, and on three particular values of the parameter E, corresponding to

<!-- PAGE BREAK -->

<a id='7fe0c470-ce80-43ad-b881-313e9e20ae76'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='d4e293c9-537c-43f2-ab75-ba8a785f0184'></a>

291

<a id='f4991ea0-248d-41e8-8cf0-ce0fe31d8a9c'></a>

<::figure: Fig. 10. Power spectral density of a NF-κB spiky oscillation under a circadian perturbation: (a) 2D color plot showing the dependence on α (vertical axis), with ω on the x-axis from 0.0 to 5.0 and α on the y-axis from 0.0 to 1.0. A color bar at the top indicates P (Power spectral density) values ranging from 10^-11 to 10^-2. (b) xy-plots of selected P(ω) functions with the several curves shifted down as α increases to avoid overlapping. The x-axis represents ω from 0.0 to 5.0, and the y-axis represents P (Power spectral density) on a logarithmic scale from 10^0 to 10^-25. A legend indicates the α values for each curve: α = 0.00 (black), α = 0.20 (cyan), α = 0.60 (blue), α = 0.85 (green), α = 0.96 (red). In both panels a logarithmic scale is used for P(ω). (For interpretation of the references to color in this figure caption, the reader is referred to the web version of this paper.)::>

<a id='7932c550-19af-4105-bf67-82b9d100fcae'></a>

representative dynamical states of the unperturbed NF-$\kappa$B oscil-lator. To have an idea of the degree of generality of the results reported, we studied the system Lyapunov exponents in two parameter planes, the plane $\beta$-$\alpha$, with $E$ fixed, and the plane $E$-$\alpha$ with $\beta$ fixed. This also provides an idea of the stability of the results reported with respect to changes in the system variables, i.e. its structural stability. Moreover, the results serve as 2-$D$ bifurcation diagrams that give information on the dynamic beha-vior to be expected as a function the system parameters.

<a id='7c97d243-c7ac-4306-b549-5fba54f3c268'></a>

For each of the values of E considered along the paper, we have
studied the Lyapunov spectrum in a rectangle in the plane β-α to
determine the structural stability regarding changes in the value of
the forcing frequency. For each type of unperturbed dynamic
behavior, we have considered a grid of 133 × 240 parameter values
evenly spaced in the rectangle defined by the conditions β∈[0, 0.5]
and α∈[0, 1.0]. The results appear in Fig. 11 where the two largest
non-compulsory-null Lyapunov exponents are plotted. The results
obtained, in the three cases are straightforward generalizations of
the Lyapunov spectra seen in Fig. 2. This tells us that, in a wide
strip of frequencies around the circadian rhythm, we have
dynamic scenarios qualitatively similar to those presented in the
above sections. For the rest state, we have periodic oscillations.
For the soft oscillation, we have quasi-periodic oscillations for
a perturbation of small and medium strength, and periodic

<a id='272ba360-8132-469b-9492-22505264967a'></a>

<::Bifurcation diagrams: chart::>Fig. 11. Bifurcation diagrams of the KJS model of NF-κB signalling perturbed by a circadian oscillation in the plane β−α as described by the two largest non-compulsory-null Lyapunov exponents. The figure consists of a color bar and six subplots (a-f). The color bar at the top ranges from -1.1 (dark blue) to 0.1 (red), with intermediate labels 0-, 0, 0+, and is labeled 'λ'. Each subplot shows a 2D map with 'α' on the y-axis (0.0 to 1.0) and 'β' on the x-axis (0.0 to 0.4). The color in the plots corresponds to the 'λ' values from the color bar. For (a,d) the plots represent a rest state, for (b,e) soft oscillations, and for (c,f) spiky oscillations. Specific E values are given for the top row: (a) E=6.50, (b) E=7.60, (c) E=10.82. Subplots (a), (b), (d), (e), (f) are predominantly blue or green, while subplot (c) shows a more complex pattern with areas of red, orange, and yellow in the top right.

<a id='6afedd76-7004-4f0b-8fee-b3def3815bc8'></a>

oscillations for a strong perturbation. For the spiky oscillation,
we have again quasi-periodic oscillations for weak and medium
perturbation, and a mix of chaotic and periodic oscillations for a
strong perturbation. In all cases, the interval of a, where we have
simple periodic oscillations or quasiperiodic dynamics diminishes
with increasing β.

<a id='e97b14c8-cda8-4d02-922c-a274d0e4f918'></a>

We have also studied the Lyapunov spectrum in the plane E−α
for β fixed at βc. For this aim we have considered a grid of
240 × 240 parameter values, in the rectangle defined by the
conditions E∈[6.0, 12.0] and α∈[0, 1.0]. A global picture of
the system dynamics dependence on E and α, as given by the
Lyapunov spectra, is shown in Fig. 12. Again, the overall picture
presented along the manuscript is confirmed: we have a region of
periodic oscillations along a vertical strip at the left of the diagram,
which corresponds to small values of E. We have a horizontal strip

<!-- PAGE BREAK -->

<a id='bca4ba4c-e3c8-4c6b-b61b-52df7dbdaf83'></a>

292

<a id='184aa605-b8c2-470b-b110-bccde336f1ba'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='a1adf492-fa20-4f18-a808-a0b8a4cce250'></a>

<::bifurcation diagram: The image displays two bifurcation diagrams, labeled (a) and (b), showing the KJS model of NF-κB signaling perturbed by a circadian oscillation in the E-α plane. Both plots share a common x-axis labeled 'E' ranging from 6.0 to 12.0, and a common y-axis labeled 'α' ranging from 0.0 to 1.0. A color bar at the top indicates the value of 'λ', ranging from -1.1 (dark blue) to 0.1 (red), with intermediate values like 0- (light blue), 0 (green), and 0+ (yellow). (a) The top plot shows the largest non-compulsory null Lyapunov exponents. It features a large green region (λ=0) covering most of the plot for E > 7.0 and α < 1.0. To the left of E ≈ 7.0, there is a blue region (λ < 0). Near the top right, there are complex patterns with yellow and red colors (λ > 0), indicating positive Lyapunov exponents. (b) The bottom plot shows the second largest non-compulsory-null Lyapunov exponent. This plot is predominantly dark blue (λ < 0), with a thin, bright green line (λ=0) curving from approximately (E=6.8, α=0.0) up to (E=7.2, α=1.0). The color variations suggest a negative Lyapunov exponent across most of the E-α plane, with a narrow region where the exponent is zero. Fig. 12. Bifurcation diagrams of the KJS model of NF−κB signalling perturbed by a circadian oscillation in the plane E−α as described by: (a) the largest non-compulsory null Lyapunov exponents, and (b) the second largest non-compulsory-null Lyapunov exponent.::>

<a id='4c2966b5-ce7a-4d20-9fbf-7a28a1f59e9f'></a>

where periodic and chaotic dynamics appear interwoven, which corresponds to large values of α. The rest of the plane E−α studied is dominated by quasiperiodic dynamics, which appears to be the dominant effect of a circadian perturbation. Being E a system parameter, its change can be interpreted as peaking a different cell; therefore, the robustness of behavior against small changes in E, provides an indication of robustness against cell-to-cell variability.

<a id='6a87a178-ad4f-4442-a589-5d798410c03b'></a>

It deserves to be noted the complex structure that appears in the upper frontier between quasiperiodic and chaotic dynamics in Fig. 12(a) [and also in Fig. 11(b)]. The most relevant trait is the set of areas of periodic dynamics having the shape of small curvilinear triangles. These are Arnold tongues, which are complex bifurcation structures commonly displayed by dynamical systems where periodicity, quasiperiodicity and chaos are interwoven (Glazier and Libchaber, 1988; Strogatz, 2001). In particular, they correspond to the periodic combination oscillation resulting from frequency entrainment. Therefore, this observation provides additional back-up to the observations and statements made in Sections 3 and 4.

<a id='4db3678c-f53c-4fd4-a55d-ac0e98fed855'></a>

7. Conclusions and discussion

We have shown that the effect of a circadian rhythm acting on the _KJS_ model of _NF-κB_ signaling is as follows. If the circadian rhythm is a perturbation of small and medium strength we can have simple periodic oscillations or quasiperiodic oscillations. Strong perturbations result in entrainment to the circadian rhythm (with the resulting oscillation having the form of a combination oscillation), or in chaotic dynamics. In all cases, the _NF-κB_ oscillations have an structure that can be described as a fast oscillation whose amplitude is modulated by a slower one. More specifically, the perturbation of a rest state result in periodic oscillations that can be simple or complex, depending on the strength of the perturbation. Weak and medium perturbations of oscillating states, no matter if soft or spiky, result in a quasiperiodic oscillation, which develops as a motion in a torus. Strong perturbations of an oscillatory state result in a special form of periodic oscillations, called combination oscillations because they represent again a form of motion in a torus, although periodic. Strong perturbations can also result in a chaotic attractor, which has a special structure as it occurs in a broken torus. Is deserves to be noted the unifying trait shared by these quasiperiodic, periodic combination, and chaotic oscillations: all of them are diverse forms of motions on a torus.

<a id='3b03a032-58fb-47ac-a64a-dbc6fbeb9244'></a>

Spectral analysis justifies the above picture. A perturbing circadian oscillation excites oscillations with the frequency of the perturbation. This is far of the natural frequency of the unperturbed system; therefore, the two oscillations are independent and the result is to turn periodic the rest states and quasiperiodic the oscillating states. Although increase of the perturbation strength creates harmonics around the frequencies of these two oscillations, they remain independent for weak and medium perturbation, so that the system dynamics does not changes qualitatively. Only for strong coupling, these two oscillations collide and become entrained to the applied external rhythm. This renders our system a regular nonlinear oscillator dominated by a single frequency able to display periodic oscillations and chaos. However, these dynamic behaviors bear a qualitative resemblance with the quasiperiodic oscillations because the harmonics around the frequency of the unperturbed system have a relatively high importance. This gives rise to modulated periodic or chaotic NF-κB oscillations.

<a id='97207329-f0e3-46cc-9d63-b74660201cb8'></a>

By means of the study of the variation of dynamic behaviors against parameters of the system and perturbation, we have provided pictures of the bifurcation diagram for the NF-κB dynamics in the interaction with a circadian clock. They provide information, not only on which dynamic behaviors exist but also on under which conditions they occur. Each point in the two-dimensional diagrams shown in Figs. 11 and 12 summarizes single-cell data that can be useful in further studies addressed to modeling complex situations such as those when heterogeneous populations of cells are involved, or when deterministic or stochastic interactions with the environment are considered. Moreover, this study shows small changes in behavior against small changes in system parameters, which means that the results presented in this paper display structural stability.

<a id='fdf4cb3f-1727-4f37-94f9-c1f914c97733'></a>

Other authors have studied perturbations of the _KJS_ model.
A first numerical approximation of the dynamics available to this
model, when perturbed by pulses and periodic oscillations, due to
Fonslet et al. (2007) showed periodic oscillations and chaos. These
authors studied a perturbation of a fixed large frequency _β_ = 2_π_,
while our study refers to a frequency one order of magnitude
smaller; therefore, the two studies can be seen as complementary
of each other. In fact, comparison of the chaotic attractors and 1-_D_
bifurcation diagrams in the present paper with those reported
by Fonslet et al. (2007) present differences large enough as to

<!-- PAGE BREAK -->

<a id='3bb9919d-882d-4395-b30d-8c9f3bc8b086'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='7d60cd34-880c-4ddd-89e4-24c15be71e79'></a>

293

<a id='0c11c9da-ec2c-4547-ab64-f95c687b0c1b'></a>

conclude that the response of the *KJS* model to a periodic perturbation presents not only quantitative, but significant qualitatively differences depending on whether we talk of low frequency or high frequency perturbations. In the study by Nikolov et al. (2009), they modified the constant *C* to include the combined effect of *IKK* activation and *RKIP*. They considered constant and transient stimulation (modeled as an exponential decay). The main results given were the ranges of existence of periodic oscillatory solutions, and the amplitude and frequency of these oscillations as functions of the strength of *IKK* activation and *RKIP* stimulation. No quasiperiodicity, nor chaos was reported, which is a result to be expected if we have in mind that no oscillation was included in the perturbation.

<a id='0a3158de-06fe-4bc4-b57e-e6145a1bcc11'></a>

Jensen and Krishna (2012) have performed research concerning
to the case of spiky NF-κB oscillation (βS=3.49 h⁻¹) driven by TNF
periodic oscillation with frequencies of the same order of magni-
tude as those of the NF-κB oscillation (β≥1.0 h⁻¹≫βc). For this aim
they, studied two schemes off driving, one coupling the KJS model
to an additional oscillator modeling the fluctuations in IKK caused
by TNF oscillations, and other based on a direct periodic driving. In
all cases, the main result reported, for weak perturbations, was a
entrainment of the frequency of the NF-κB oscillation to that of
the driving signal, so that the ratio of the frequencies is a rational
number. For large perturbations, chaotic dynamics was reported.
The 2D bifurcation diagrams showed a structure of Arnold tongues
developing and gaining width from a zero intensity of the
perturbation, until chaos develops for larger values of the intensity
of the perturbation. It is to be noted that the range of perturbing
frequencies considered in the preset paper is an order of magni-
tude smaller than the one studied by Jensen and Krishna (2012).
The means that the cases studied in the two papers are quite
different, then presenting different dynamics. While for small
frequencies, we obtain that the dominant dynamics is quasiper-
iodic, with frequency entrainment and chaos occurring only in a
narrow band of large amplitude forcing, Jensen and Krishna (2012)
obtain frequency locking and chaos to be dominant. In our 2D
bifurcation diagram, shown in Fig. 11(c), we see that the size of the
forcing amplitude band where quasi-periodicity occurs decreases
with increasing frequency, while the region where Arnold tongues
and chaos develop becomes wider. This suggests a gradual change
from quasiperiodicity dominance to frequency entrainment dom-
inance with increasing perturbation frequency. Consequently, we
can reasonably conjecture a smooth change from the dynamical
scenario presented in this paper to the one reported by Jensen and
Krishna (2012) as the frequency of the perturbation increases.

<a id='1db5f5cd-5150-4bc9-93db-4afbed87bf4c'></a>

The results reported in this paper add new information on dynamic behaviors for the KJS model, such as periodicity and chaos, previously observed (Krishna et al., 2006; Fonslet et al., 2007; Nikolov et al., 2009; Jensen and Krishna, 2012), although under other conditions of occurrence. Moreover, for the case of a circadian perturbation, we found that the dominant dynamic behavior observed is quasi-periodicity, which has not been studied before for this model. Each of these different dynamic behaviors entails a distinctive wave form for the oscillations of the concen-tration of nuclear NF-κB in a eukaryotic cell (as illustrate by Figs. 3 and 4). For the case of periodicity the oscillations are can be simple, fully predictable, and characterized by two parameters: amplitude and frequency. We have also observed complex periodic oscillations when there is entrainment. These are characterized by two frequencies whose ratio is a rational number, and whose amplitude changes presenting a pattern of peaks and troughs. Quasiperiodic oscillations are characterized by two different frequen-cies, whose ratio is an irrational number, the oscillations are not periodic presenting certain degree of unpredictability, and the amplitude changes presenting peaks and troughs. Chaotic oscillations are characterized by a broad range of frequencies, they are not

<a id='02be5dbb-8d87-41fe-9d43-6162697aad22'></a>

periodic and strongly unpredictable. All this dynamic behaviors are cases of biological oscillations, which are mostly complex, then providing examples of a phenomenology that has raised considerable interest in the life sciences. In many cases, such complex oscillations are interesting because they perform functions in intracellular and extracellular communication, in a variety of biological systems ranging from neurons to biochemical reactions (Stavreva et al., 2012; Goldbeter, 2002; Cai et al., 2008; Behar and Hoffmann, 2010).

<a id='00a80b50-5c3d-474f-88ba-9e7be6b15687'></a>

The particular importance of these results, regarding biochem-
ical cell signaling, is that they provide some background informa-
tion relevant for the understanding of the mechanism by which
NF-κB conveys information. As noted above, NF-κB regulates a
large number of genes and a variety of cellular outcomes. If the
transcription response to be obtained is to be determined by the
oscillatory dynamics of NF-κB, to unambiguously perform such
amount of different task, it is reasonable to expect an ample
repertory of NF-κB oscillations. In the literature on biological cell
signaling (see for example, refs. Stavreva et al., 2012; Goldbeter,
2002; Cai et al., 2008; Behar and Hoffmann, 2010 and references
therein) we can read about two basic regulatory mechanisms, one
based in signal amplitude, where different concentrations would
produce different outputs, and other on signal frequency, where
different frequencies would produce different outputs. Nowadays,
the mechanism based on frequency appears to be the quite
popular regarding NF-κB signaling. However, things could be
more complex, and the proper question to ask would be, which
mechanism will work in a particular regulatory process? An
answer is only to be determined by experiments on that particular
process. For example, the response to the question "Does the
circadian coupling repress or promote the inflammatory response?
" will require to deal, at least, with two issues: (i) which is the
particular dynamical behavior associated to inflammation? and (ii)
how do the NF-κB oscillations encode the information they
convey? The first is to be determined by experiments and the
second is a open problem.

<a id='5a5b37f3-b85a-4f0a-a2d9-495369dc4639'></a>

A descriptive theoretical approach, of the kind presented here, provides background information potentially useful to guide the choice and design of experiments aimed to understand the role of NF-κB oscillations in gene expression. In particular, provides conditions for occurrence of the different types of oscillations and specific details regarding these oscillations that can be useful to guess coding mechanisms to be tested by experiments. Understanding the temporal codes of biological signals is a problem with many different possibilities, as discussed by Behar and Hoffmann (2010). These can be simple, as those based on frequency coding, of the kind described, for example, by Goldbeter (2002) and by Cai et al. (2008) for calcium oscillations, and by Ashall et al. (2009) for NF-κB oscillations. However, given the amount of responses associated to NF-κB, one should not discard cases where a simple amplitude coding (described by Cai et al., 2008 and by Behar and Hoffmann, 2010) will work. Moreover, having signals whose waveform changes, presenting peaks and troughs, one might think of a combination of both mechanisms, amplitude and frequency. For example, one could consider pulsatile signaling, of the kind described by Goldbeter (2002) for the slime mould Dictiostelium diciodeum, and by Stavreva et al. (2012) for glucorticoid-receptor mediated transcription. Anyway, no matter the coding mechanism of choice, the way it works would depend on the features of the underlying deterministic NF-κB oscillations. This is why we say that this paper provides background information to be considered in the controversy on the mechanism by which NF-κB conveys information.

<a id='26c10130-50c9-49bb-9425-d654f4a911f0'></a>

Finally, we would like to remark the observation of chaos among the dynamic behaviors observed that, although occurring only for strong perturbations, introduces an scenario of intrinsic stochasticity. This is interesting because some experimental

<!-- PAGE BREAK -->

<a id='88bdacfa-4e6e-4d13-b99b-055b12d1670e'></a>

294

<a id='304165e9-b4e5-46cc-b3c7-d901a3362a62'></a>

J.M. González-Miranda / Journal of Theoretical Biology 335 (2013) 283–294

<a id='b2cfbd55-2e33-48ae-ae2c-66635845ad12'></a>

studies (Tay et al., 2010; Turner et al., 2010; Bartfeld et al., 2010) have reported stochasticity in NF-κB oscillations, which have been theoretically dealt off by means of stochastic differential equations. Moreover, it happens that the role of stochasticity in biological systems, in more general terms, is an issue of interest (Skinner, 1994; Wilkinson, 2009). Theoretical results on deterministic chaos reported here, provide a potential source of stochasticity in NF-κB signaling, restricted to certain cases, but worthy of being taken into consideration.

<a id='547b5514-5ecb-420c-a7a4-ba7f654ebd92'></a>

## Acknowledgments

I like to thank Pedro Gonzalez for drawing my attention to the kind of biological oscillators studied in this paper, and for useful discussion. Partial financial support by DGI is also acknowledged.

<a id='6de1fef9-dd2c-4aa3-b569-50ae4df4e47e'></a>

# References
Ashall, L., Horton, C.A., Nelson, D.E., Paszek, P., Harper, C.V., Sillitoe, K., Ryan, S., Spiller, D.G., Unitt, J.F., Broomhead, D.S., Kell, D.B., Rand, D.A., Sée, V., White, M.R.H., 2009. Pulsatile stimulation determines timing and specificity of NF-kB-dependent transcription. Science 324, 242-246.
Bartfeld, S., Hess, S., Bauer, B., Machuy, N., Ogilvie, L.A., Schuchhardt, J., Meyer, T.F., 2010. High-throughput and single-cell imaging of NF-kB oscillations using monoclonal cell lines. BMC Cell Biol. 2010, 11-21.
Behar, M., Hoffmann, A., 2010. Understanding the temporal codes of intra-cellular signals. Curr. Opin. Genet. Dev. 20, 684-693.
Cai, L., Dalal, Ch.K., Elowitz, M.B., 2008. Frequency-modulated nuclear localization bursts coordinate gene regulation. Nature 455, 485-490.
Edmunds, L.N., 1988. Cellular and Molecular Bases of Biological Clocks: Models and Mechanisms for Circadian Timekeeping. Springer, New York, NY, USA.
Fonslet, J., Rud-Petersen, K., Krishna, S., Jensen, M.H., 2007. Pulses and chaos: dynamical response in a simple genetic oscillator. Int. J. Mod. Phys. B 21, 4083-4090.
Glazier, J.A., Libchaber, A., 1988. Quasi-periodicity and dynamical systems: an experimentalist's view. IEEE Trans. CAS 35, 790-809.
Goldbeter, A., 2002. Computational approaches to cellular rhythms. Nature 420, 238-245.
González-Miranda, J.M., 2002a. Phase synchronization and chaos suppression in a set of two coupled nonlinear oscillators. Int. J. Bifurcation Chaos 20, 2105-2122.
González-Miranda, J.M., 2002b. Amplitude envelope synchronization in coupled chaotic oscillators. Phys. Rev. E 65 036232-[10 pages].
González-Miranda, J.M., 2004. Synchronization and Control of Chaos. Imperial College Press, London, UK.
González-Miranda, J.M., 2007. Complex bifurcation structures in the Hindmarsh-Rose neuron model. Int. J. Bifurcation Chaos 17, 3071-3083.
González-Miranda, J.M., 2010. Linear stability analysis of a boundary crisis in a minimal chaotic flow. Phys. D 239, 322-326.
González-Miranda, J.M., 2012. Nonlinear dynamics of the membrane potential of a bursting pacemaker cell. Chaos 22 023123-[12 pages].
Harmer, S.L., Panda, S., Kay, S.A., 2001. Molecular bases of circadian rhythms. Annu. Rev. Cell Dev. Biol. 17, 215-253.
Hoffmann, A., Levchenko, A., Scott, M.L., Baltimore, D., 2002. The IKB-NF-KB signaling module: temporal control and selective gene activation. Science 298, 1241-1245.

<a id='f1eec779-4c3d-4892-884b-c33a8ee00e44'></a>

Jensen, M.H., Krishna, S., 2012. Inducing phase-locking and chaos in cellular
oscillators by modulating the driving stimuli. FEBS Lett. 586, 1664-1668.
Krishna, S., Jensen, M.H., Sneppen, K., 2006. Minimal model of spiky oscillations in
NF-KB signaling. Proc. Natl. Acad. Sci. 103, 10840-10845.
Kulasiri, D., He, Y., Samarasinghe, S., 2011. Robustness of circadian rhythms in the
presence of molecular fluctuations: an investigation based on a mechanistic,
statistical theory and a simulation algorithm. BioSystems 106, 57-66.
Lee, J.H., Sankar, A., 2011. Regulation of apoptosis by the circadian clock through
NF-KB signaling. Proc. Natl. Acad. Sci. 108, 12036-12041.
Leloup, J.-C., Goldbeter, A., 2004. Modeling the mammalian circadian clock:
sensitivity analysis and multiplicity of oscillatory mechanisms. J. Theor. Biol.
230, 541-562.
Liu, K., Wang, R., 2012. MicroRNA-mediated regulation in the mammalian circadian
rhythm. J. Theor. Biol. 304, 103-110.
Matsuo, T., Yamaguchi, S., Mitsui, S., Emi, A., Shimoda, F., Okamura, H., 2003. Control
mechanism of the circadian clock for timing of cell division in vivo. Science 302,
255-259.
Mullenders, J., Fabius, A.W.M., Madiredjo, M., Bernards, R., Beijersbergen, R.L., 2009.
A large scale shRNA barcode screen identifies the circadian clock component
ARNTL as putative regulator of the p53 tumor suppressor pathway. PLoS ONE 4,
e4798-[10 pages].
Nelson, D.E., Ihekwaba, A.E.C., Elliott, M., Johnson, J.R., Gibney, C.A., Foreman, B.E.,
Nelson, G., See, V., Horton, C.A., Spiller, D.G., Edwards, S.W., McDowell, H.P.,
Unitt, J.F., Sullivan, E., Grimley, R., Benson, N., Broomhead, D., Kell, D.B., White,
M.R.H., 2004. Oscillations in NF-kB signaling control the dynamics of gene
expression. Science 306, 704-708.
Nikolov, S., Vera, J., Rath, O., Kolch, W., Wolkenhauer, O., 2009. Role of inhibitory
proteins as modulators of oscillations in NF-kB signaling. IET Syst. Biol. 3,
59-76.
Osipov, G.V., Kurths, J., Zhou, C., 2007. Synchronization in Oscillatory Networks.
Springer-Verlag, Germany, Berlin.
Park, S.G., Lee, T., Kang, H.Y., Park, K., Cho, K.-H., Jung, G., 2006. The influence of the
signal dynamics of activated form of IKK on NF-kB and anti-apoptotic gene
expressions: a systems biology approach. FEBS Lett. 580, 822-830.
Press, W.H., Teukolsky, S.A., Vetterling, W.T., Flannery, B.P., 1996. Numerical Recipes
in Fortran 90. Cambridge University Press, Cambridge.
Robinson, P.A., Wu, H., Kim, J.W., 2008. Neural rate equations for bursting dynamics
derived from conductance-based equations. J. Theor. Biol. 250, 663-672.
Skinner, J.E., 1994. Low-dimensional chaos in biological systems. Nat. Biotechnol.
12, 596-600.
Stavreva, D.A., Varticovski, L., Hager, G.L., 2012. Complex dynamics of transcription
regulation. Biochim. Biophys. Acta 1819, 657-666.
Strogatz, S.H., 2001. Nonlinear Dynamics and Chaos. Westview Press, Boulder, CO,
USA.
Tay, S., Hughey, J.J., Lee, T.K., Tay, S., Lipniacki, T., Quake, S.R., Covert, M.W., 2010.
Single-cell NF-KB dynamics reveals digital activation and analog information
processing. Nature 466, 267-271.
Turner, D.A., Paszek, P., Woodcock, D.J., Nelson, D.E., Horton, C.A., Wang, Y., Spiller,
D.G., Rand, D.A., White, M.R.H., Harper, C.V., 2010. Physiological levels of TNFa
stimulation induce stochastic dynamics of NF-KB responses in single living
cells. J. Cell Sci. 123, 2834-2843.
Watts, M., Tabak, J., Zimliki, C., Sherman, A., Bertram, R., 2011. Slow variable
dominance and phase resetting in phantom bursting. J. Theor. Biol. 276,
218-228.
Wilkinson, D.J., 2009. Stochastic modeling for quantitative description of hetero-
geneous biological systems. Nat. Rev. Genet. 10, 122-133.
Wolf, A., Swift, J.B., Swinney, H.L., Vastano, J.A., 1985. Determining Lyapunov
exponents from a time series. Phys. D 16, 285-317.