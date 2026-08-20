<a id='59f1323c-ae5b-4b60-8730-38eb12804719'></a>

<::logo: Interface Focus
Interface Focus
This logo features the word "Focus" in bold black and gray text, with "Interface" in smaller gray text above the "ocus" part of "Focus".::>

<a id='ae5c9f89-7a07-45aa-92d7-7cc1b0da9113'></a>

Interface Focus (2011) 1, 24-35
doi:10.1098/rsfs.2010.0008
Published online 1 December 2010

<a id='9adc3c05-bce2-4ef0-aeac-1dabcd180dc8'></a>

A skeleton model for the network of
cyclin-dependent kinases driving
the mammalian cell cycle

<a id='4c43d5c4-ed23-457f-bf6e-a593809ed925'></a>

**Claude Gérard and Albert Goldbeter***
*Faculté des Sciences, Université Libre de Bruxelles (ULB), Campus Plaine, CP 231,
1050 Brussels, Belgium*

<a id='0b13e70f-9d14-4b4d-8879-422f38024503'></a>

We previously proposed a detailed, 39-variable model for the network of cyclin-dependent kinases (Cdks) that controls progression along the successive phases of the mammalian cell cycle. Here, we propose a skeleton, 5-variable model for the Cdk network that can be seen as the backbone of the more detailed model for the mammalian cell cycle. In the presence of sufficient amounts of growth factor, the skeleton model also passes from a stable steady state to sustained oscillations of the various cyclin/Cdk complexes. This transition corre- sponds to the switch from quiescence to cell proliferation. Sequential activation of the cyclin/Cdk complexes allows the ordered progression along the G1, S, G2 and M phases of the cell cycle. The 5-variable model can also account for the existence of a restriction point in G1, and for endoreplication. Like the detailed model, it contains multiple oscillatory cir- cuits and can display complex oscillatory behaviour such as quasi-periodic oscillations and chaos. We compare the dynamical properties of the skeleton model with those of the more detailed model for the mammalian cell cycle.

<a id='ac7722cd-d68a-4702-8c4f-f9452ccfdcbd'></a>

Keywords: oscillations; cell cycle; model; systems biology

<a id='24f10fbb-2093-4cd5-92d4-710ca529ad89'></a>

# 1. INTRODUCTION
The mammalian cell cycle is driven by a network of cyclin-dependent kinases (Cdks) [1,2], which control the progression along four successive phases: the gap phase G1, the S phase of DNA replication, the gap phase G2 and the M phase of mitosis. When cells are not in a proliferative state, they remain in a quiescent phase, denoted G0. Several models were proposed to account for parts of the mammalian cell cycle, especially the G1/S transition [3,4], the restriction point in G1 [5], or the G2/M transition [6]. We recently proposed a detailed model describing the dynamics of the global Cdk network driving the mammalian cell cycle [7]. This model consists of four Cdk modules, each centred around one cyclin/Cdk complex. The cyclin D/Cdk4-6 and cyclin E/Cdk2 complexes promote progression in G1 and elicit the G1/S transition, respectively, the cyclin A/Cdk2 complex ensures progression in S and the transition S/G2, while the activity of the cyclin B/Cdk1 complex brings about the G2/M transition. In view of its complexity, it is not surprising that the detailed model for the Cdk network contains 39 variables and as many as 164 parameters. We used this model to show that in the presence of sufficient amounts of growth factor, the Cdk network is capable of temporal

<a id='bfe5b041-9fbc-482d-b5de-0fbbc40deacc'></a>

*Author for correspondence (agoldbet@ulb.ac.be).
One contribution of 16 to a Theme Issue 'Advancing systems medicine
and therapeutics through biosimulation'.

<a id='8c687c46-282c-454c-a3e4-ff7b8262ec38'></a>

self-organization in the form of sustained oscillations
[7]. The latter correspond to the ordered, sequential
activation of the various cyclin/Cdk complexes that
control the successive phases of the cell cycle.

<a id='ec955afb-4d1f-4956-b6e9-6ebc53e200a0'></a>

Is it possible to build a model for the mammalian cell cycle that would contain a much smaller number of variables and fewer parameters, while keeping similar dynamical properties? Such a simpler model would be of interest for at least two reasons. First, it would be more amenable to computer simulations and to searching in parameter space complex oscillatory phenomena. Second, it would help to delineate the minimal regulatory structure needed for obtaining a particular mode of dynamic behaviour such as sustained oscillations. Here, we present a 5-variable model based on the regulatory backbone of the 39-variable model for the Cdk network. To build such a reduced model, we had to abandon many of the biochemical details included in the detailed model. The reduced system can thus be considered as a skeleton version of the full 39-variable representation of the Cdk network.

<a id='60d01392-4c38-4a81-8306-e17931080d9d'></a>

In the detailed model for the Cdk network, the synthesis of the various cyclins is regulated through the balance between the antagonistic effects exerted by the transcription factor E2F, which promotes, and the tumour suppressor pRB, which inhibits cell cycle progression, respectively. The Cdk network in turn regulates through phosphorylation the activity of E2F and pRB [7]. Additional regulations in the detailed model for the Cdk network bear on the control exerted by the proteins Skp2, Cdh1 or Cdc20 on the

<a id='b2fe3ac1-2802-4c3b-9b17-67d01550e436'></a>

Received 9 October 2010 Accepted 8 November 2010

<a id='231219af-2e53-4498-b496-f4a903783a66'></a>

24

<a id='9d986ef8-4d3d-4cf3-8a88-266f2acddae5'></a>

This journal is © 2010 The Royal Society

<!-- PAGE BREAK -->

<a id='be4de812-7582-4c58-b00f-be8801943e2d'></a>

A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='83e97462-d003-4535-bc55-a91f8c2f1b26'></a>

25

<a id='c7f23906-7167-4f0b-99a5-bc15d8fe95d5'></a>

<::flowchart: The diagram illustrates the skeleton model for the Cdk network driving the mammalian cell cycle. On the left, a vertical arrow indicates the progression through cell cycle phases: G1, G1/S, S/G2, and G2/M. On the right, various protein complexes and transcription factors are shown as yellow rectangles or text labels, with blue arrows representing interactions (activation, synthesis, degradation) and black arrows showing cell cycle progression. A horizontal line from the G1 phase points to the synthesis of "cyclin D/Cdk4-6" which is initiated by "GF" (Growth Factor). Cyclin D/Cdk4-6 activates "E2F (a)" (active E2F) from "E2F (i)" (inactive E2F), shown as a reversible conversion. Active E2F promotes the activation of "cyclin E/Cdk2". Cyclin E/Cdk2, in turn, also activates E2F (a), forming a positive feedback loop. Cyclin E/Cdk2 also leads to the activation of "cyclin A/Cdk2". A horizontal line from the G1/S transition points to cyclin E/Cdk2. Cyclin A/Cdk2 promotes the activation of "cyclin B/Cdk1" and also inactivates E2F (a) by promoting its conversion to E2F (i). A horizontal line from the S/G2 transition points to cyclin A/Cdk2. Cyclin B/Cdk1 activates "Cdc20 (a)" (active Cdc20) from "Cdc20 (i)" (inactive Cdc20), which is also a reversible conversion. Active Cdc20 creates a negative feedback loop by promoting the degradation (indicated by blunt-ended arrows) of both cyclin A/Cdk2 and cyclin B/Cdk1. A horizontal line from the G2/M transition points to cyclin B/Cdk1. Figure 1. Scheme of the skeleton model for the Cdk network driving the mammalian cell cycle. The model contains the four main cyclin/Cdk complexes, the transcription factor E2F and the protein Cdc20. At the beginning of the cell cycle, the growth factor GF ensures the synthesis of the cyclin D/Cdk4-6 complex, which promotes progression in the G1 phase. This complex allows the activation of the transcription factor E2F, which will bring about the activation of cyclin E/Cdk2 at the G1/S transition, and cyclin A/Cdk2 during the S phase of DNA replication. Cyclin E/Cdk2 also activates E2F, which reinforces the activation by cyclin D/Cdk4-6 and promotes progression to the G1/S transition. Cyclin A/Cdk2 allows progression in S and elicits the S/G2 transition by promoting the inactivation of E2F. During G2, cyclin A/Cdk2 also triggers the activation of cyclin B/Cdk1, which leads to the G2/M transition. During mitosis, cyclin B/Cdk1 activates by phosphorylation the protein Cdc20. This protein creates a negative feedback loop involving cyclin A/Cdk2 and cyclin B/Cdk1 by promoting the degradation of these complexes. The regulations controlled by Cdc20 allow the cell to complete mitosis, and to start a new cell cycle if sufficient amounts of GF are present. The model represents a skeleton version of the much more detailed model proposed by Gérard & Goldbeter [7] for the mammalian cell cycle.::>

<a id='f2e00611-5a4e-41c5-b38a-b243ec1d8c3f'></a>

degradation of cyclins E, A and B at the G1/S or G2/M
transitions, respectively. Finally, the activity of each
cyclin/Cdk complex can itself be regulated through
phosphorylation-dephosphorylation. The activity of
cyclin D/Cdk4-6 is thus activated by phosphorylation
by the CAK protein (cyclin-activated kinase), while the
Cdk2 and Cdk1 complexes are activated by the phos-
phatase Cdc25 and inhibited by the kinase Wee1.
Multiple positive feedback loops characterize the
activation of the Cdks, because the phosphatases
Cdc25 that activate the various Cdks are themselves
activated through phosphorylation by their correspond-
ing Cdk, while the latter inactivate their inhibitory
kinase Wee1. The activity of the Cdks is further
regulated through association with the protein inhibitor
p21/p27 [7]. The already large number of variables
in the detailed model goes up to 44 when the ATR/
Chk1 checkpoint controlling DNA replication is
incorporated into the model.

<a id='43792fe9-42f3-4482-9645-7bea89f07019'></a>

We show here that many of these biochemical details may be relinquished in building a skeleton, 5-variable model for the mammalian cell cycle, without losing key dynamical properties of the Cdk network. In §2, we describe the skeleton model and explain what characteristics of the detailed model are kept or aban- doned in the reduced version. In §3, we show how sustained oscillations in the various cyclin/Cdk com- plexes occur in the skeleton model in the presence of

<a id='06367096-757c-4015-bb9a-64ba1d9647af'></a>

sufficient amounts of growth factor. We address the existence of a restriction point in G1 beyond which the presence of the growth factor is not needed to complete a cycle. Section 4 is devoted to the multiple oscillatory circuits contained in the skeleton model for the Cdk network. One consequence of such multiplicity of oscillatory mechanisms is that their interplay may give rise to complex modes of oscillatory behaviour, as shown in §5. These results are discussed in §6. All along, we compare the behaviour of the reduced and detailed models for the Cdk network, to assess in what measure the skeleton model is suitable for describing the dynamics of the mammalian cell cycle.

<a id='0c31203b-9955-4721-bded-9e4db13786df'></a>

## 2. A SKELETON 5-VARIABLE MODEL FOR THE NETWORK OF CYCLIN-DEPENDENT KINASES

Based on the detailed model, which counts 39 variables, we construct a skeleton model with a reduced number of variables. This model involves as variables the four cyclin/Cdk complexes that allow the correct progression along the successive phases of the cell cycle. Other variables are the transcription factor E2F, and the protein Cdc20 that controls the degradation of the cyclin A/Cdk2 and cyclin B/Cdk1 complexes (figure 1). Because the level of cyclin D/Cdk4–6 is

<a id='bd27d91a-71f3-45ec-a807-6a98a0d0bdaa'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='c591f2d6-00cc-4307-bf01-f0ab5d1f20bf'></a>

26 A skeleton model for the cell cycle C. Gérard and A. Goldbeter
---


<a id='65a73ec4-4d67-45dd-acc4-4588e58d33a3'></a>

only regulated by the level of growth factor, it rapidly
reaches a steady state. The model therefore contains
only five variables.

<a id='b757bf8c-2a7e-418c-bbf4-33959e27396d'></a>

The skeleton model for the Cdk network is schema-tized in figure 1. At the beginning of the cell cycle, the growth factor GF activates directly the synthesis of the cyclin D/Cdk4-6 complex, which promotes pro-gression in G1. This complex ensures the activation of the transcription factor E2F, which in turn activates the synthesis of the cyclin E/Cdk2 and cyclin A/Cdk2 complexes. During the G1 phase, cyclin E/Cdk2 reinforces the activation of the transcription factor E2F. During the S phase of DNA replication, cyclin A/Cdk2 activates the degradation of cyclin E/Cdk2, which ensures that the latter complex will not be activated at the end of the cell cycle. Cyclin A/Cdk2 also permits exit of the S phase by allowing the inactivation of the transcription factor E2F and by pro-moting the synthesis of cyclin B/Cdk1, whose peak of activity brings about the G2/M transition. During mitosis, cyclin B/Cdk1 activates, by phosphorylation, the protein Cdc20. This protein is at the core of the negative feedback loop since it promotes the degra-dation of cyclin A/Cdk2 and cyclin B/Cdk1, thereby permitting the completion of the cell cycle. A new cell cycle starts if the growth factor is still present in sufficient amounts.

<a id='766e70d0-6ba4-4e09-a053-19f0a8fa4cb9'></a>

As compared with the detailed, 39-variable model, what are the characteristics that had to be abandoned in building the skeleton, 5-variable model? The latter does not incorporate explicitly the reversible binding of each cyclin to its corresponding Cdk; we assume that this complex is rapidly formed. The regulation of the activity of the cyclin/Cdk complexes through phosphorylation-dephosphorylation by the phosphatases Cdc25 and the kinase Wee1 is not considered. Thus, the skeleton model contains only the active forms of the cyclin/Cdk complexes: variations in the activity of the cyclin/Cdk complexes occur solely through cyclin synthesis and degradation. Moreover, the Cdk inhibitor p21/p27 is not present in the skeleton model; this prevents the regulation of the activity of the four cyclin/Cdk complexes through reversible association with this inhibitor.

<a id='61b484ac-67b8-4a11-8280-5b666c206343'></a>

Moreover, in contrast to the detailed model, the 5-variable model does not take into account the tumour suppressor protein pRB in its various phosphorylated or unphosphorylated forms. In the detailed model, E2F was inactivated upon binding the unphosphorylated and monophosphorylated forms of pRB; activation of E2F followed from the progressive inactivation of pRB through phosphorylation by cyclin D/Cdk4-6 and cyclin E/Cdk2. In the skeleton model, because we do not include the role of pRB, and because we wish to couple E2F to cyclin D/ Cdk4-6 and cyclin E/Cdk2, we assume, for simplicity, that the latter kinases directly activate E2F through phosphorylation, even if there is no evidence for such direct control of E2F by the two cyclin/Cdk complexes. In the detailed model, the specific degradation of cyclin E is brought about by the protein Skp2 and the degradation of cyclin B is partly controlled by Cdh1;

<a id='e672acc7-a775-490c-92be-2fcd8064bfe1'></a>

Table 1. Variables of the model.
<table id="2-1">
<tr><td id="2-2">symbol</td><td id="2-3">definition</td></tr>
<tr><td id="2-4">Mdª</td><td id="2-5">cyclin D/Cdk4-6 complex</td></tr>
<tr><td id="2-6">E2F</td><td id="2-7">transcription factor E2F</td></tr>
<tr><td id="2-8">Me</td><td id="2-9">cyclin E/Cdk2 complex</td></tr>
<tr><td id="2-a">Ma</td><td id="2-b">cyclin A/Cdk2 complex</td></tr>
<tr><td id="2-c">Mb</td><td id="2-d">cyclin B/Cdk1 complex</td></tr>
<tr><td id="2-e">Cdc20</td><td id="2-f">protein that belongs to the anaphase-promoting complex (APC)</td></tr>
</table>
ªMd is uncoupled from the other variables and rapidly
reaches a steady state. The model thus contains only five
variables.

<a id='39a95a0d-a4d0-42c8-92c2-f342870bb3e2'></a>

cyclin A/Cdk2 inhibits Cdh1, which itself promotes the degradation of Skp2 [7]. Here, Cdh1 and Skp2 are not included, and since we wish to couple the degradation of cyclin E/Cdk2 to the rise in cyclin A/Cdk2, we assume that this degradation rate is simply proportional to the concentration of the latter complex.

<a id='a6a1f7b5-179d-42b9-add1-2d56b17ad997'></a>

The fact that the phosphatases Cdc25 and the kinase Wee1 are not considered in the 5-variable model prevents the existence of the positive feedback loops that characterize the Cdk2 and Cdk1 modules in the detailed model. Finally, we consider that the total amount of the Cdc20 protein involved in the degradation of cyclin A/Cdk2 and cyclin B/Cdk1 remains constant, whereas the total quantity of this protein could vary in the detailed model. As in the detailed model, however, Cdc20 is present in the skeleton model both under an active, phosphorylated and an inactive, dephosphorylated form.

<a id='b35f9bff-7322-400f-a82e-161103ca8dce'></a>

The kinetic equations of the skeleton model are pre-
sented as equations (2.1)-(2.6). Table 1 defines the
different variables of the model, and table 2 shows the
list of parameters together with their numerical values
used in the simulations.

<a id='224b1e09-31f3-440b-a5dd-2eb07cc03fd8'></a>

dMd/dt = v_sd * (GF / (K_gf + GF)) - V_dd * (Md / (K_dd + Md)), (2.1)
dE2F/dt = V_le2f * ((E2F_tot - E2F) / (K_le2f + (E2F_tot - E2F))) * (Md + Me)

<a id='996d2c18-0c62-4cab-b1bf-bbf769864c64'></a>

$$-V_{2e2f} \cdot \left( \frac{E2F}{K_{2e2f} + E2F} \right) \cdot Ma, \quad (2.2)$$

<a id='04981392-675c-4c4b-9236-f2995920bf10'></a>

$$\frac{\text{d Me}}{\text{dt}} = v_{se} \cdot \text{E2F} - V_{de} \cdot \text{Ma} \cdot \left(\frac{\text{Me}}{K_{de} + \text{Me}}\right), \quad (2.3)$$

$$\frac{\text{d Ma}}{\text{dt}} = v_{sa} \cdot \text{E2F} - V_{da} \cdot \text{Cdc20} \cdot \left(\frac{\text{Ma}}{K_{da} + \text{Ma}}\right), \quad (2.4)$$

$$\frac{\text{d Mb}}{\text{dt}} = v_{sb} \cdot \text{Ma} - V_{db} \cdot \text{Cdc20} \cdot \left(\frac{\text{Mb}}{K_{db} + \text{Mb}}\right), \quad (2.5)$$

<a id='0c9d2bdd-74c4-4cb8-a145-50d02f6d751b'></a>

$$\frac{\text{d Cdc20}}{\text{dt}} = V_{1\text{cdc20}} \cdot \text{Mb} \times \left(\frac{(\text{Cdc20}_{\text{tot}} - \text{Cdc20})}{K_{1\text{cdc20}} + (\text{Cdc20}_{\text{tot}} - \text{Cdc20})}\right) - V_{2\text{cdc20}} \cdot \left(\frac{\text{Cdc20}}{K_{2\text{cdc20}} + \text{Cdc20}}\right) \quad (2.6)$$

<a id='ddc7156c-3bdf-4e24-965c-893cde86ca2e'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='ac6084c2-94e9-41c3-b018-6ee668467fdf'></a>

A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='e4b46170-2a0a-4d18-8f0e-1ccd12744d71'></a>

27

<a id='604336e7-d832-45b3-80bc-851ca5b1d796'></a>

Table 2. Parameters of the model. Concentrations are tentatively expressed in M. Because many are still unknown and probably vary from one cell type to another, the parameter values are selected in a semi-arbitrary manner so as to produce sustained oscillatory behaviour [7]. The main goal of the model is indeed to determine the types of dynamic behaviour associated with the regulatory structure of the Cdk network.

<a id='ec00b0c6-e052-4962-80b2-4370c755a5f3'></a>

<table id="3-1">
<tr><td id="3-2">symbol</td><td id="3-3">definition</td><td id="3-4">numerical values</td></tr>
<tr><td id="3-5">Cdc20tot</td><td id="3-6">total concentration of the protein Cdc20</td><td id="3-7">5 μM</td></tr>
<tr><td id="3-8">E2Ftot</td><td id="3-9">total concentration of the transcription factor E2F</td><td id="3-a">3 μM</td></tr>
<tr><td id="3-b">GF</td><td id="3-c">growth factor</td><td id="3-d">1 μM</td></tr>
<tr><td id="3-e">Kda</td><td id="3-f">Michaelis constant for the degradation, activated by Cdc20, of cyclin A/Cdk2</td><td id="3-g">0.1 μM</td></tr>
<tr><td id="3-h">Kdb</td><td id="3-i">Michaelis constant for the degradation, activated by Cdc20, of cyclin B/Cdk1</td><td id="3-j">0.005 μM</td></tr>
<tr><td id="3-k">Kdd</td><td id="3-l">Michaelis constant for the degradation of cyclin D/Cdk4-6</td><td id="3-m">0.1 μM</td></tr>
<tr><td id="3-n">Kde</td><td id="3-o">Michaelis constant for the degradation of cyclin E/Cdk2</td><td id="3-p">0.1 μM</td></tr>
<tr><td id="3-q">Kgf</td><td id="3-r">Michaelis constant for synthesis of the cyclin D/Cdk4-6 complex induced by growth factor</td><td id="3-s">0.1 μM</td></tr>
<tr><td id="3-t">K1cdc20</td><td id="3-u">Michaelis constant for Cdc20 activation through phosphorylation by cyclin B/Cdk1</td><td id="3-v">1 μM</td></tr>
<tr><td id="3-w">K₂cdc20</td><td id="3-x">Michaelis constant for Cdc20 inactivation through dephosphorylation</td><td id="3-y">1 μM</td></tr>
<tr><td id="3-z">K1e2f</td><td id="3-A">Michaelis constant for E2F activation by cyclin D/Cdk4-6 and cyclin E/Cdk2 complexes</td><td id="3-B">0.01 μM</td></tr>
<tr><td id="3-C">K2e2f</td><td id="3-D">Michaelis constant for E2F inactivation by the cyclin A/Cdk2 complex</td><td id="3-E">0.01 μM</td></tr>
<tr><td id="3-F">Vda</td><td id="3-G">rate constant for the degradation of the cyclin A/Cdk2 complex by the protein Cdc20</td><td id="3-H">0.245 h⁻¹</td></tr>
<tr><td id="3-I">Vdb</td><td id="3-J">rate constant for the degradation of the cyclin B/Cdk1 complex by the protein Cdc20</td><td id="3-K">0.28 h⁻¹</td></tr>
<tr><td id="3-L">V_dd</td><td id="3-M">maximum degradation rate of cyclin D/Cdk4-6 complex</td><td id="3-N">0.245 μM h⁻¹</td></tr>
<tr><td id="3-O">V_de</td><td id="3-P">rate constant for the degradation of cyclin E/Cdk2 by cyclin A/Cdk2</td><td id="3-Q">0.35 h⁻¹</td></tr>
<tr><td id="3-R">V_sa</td><td id="3-S">rate constant for synthesis of cyclin A/Cdk2 induced by the transcription factor E2F</td><td id="3-T">0.175 h⁻¹</td></tr>
<tr><td id="3-U">V_sb</td><td id="3-V">rate constant for synthesis of cyclin B/Cdk1 induced by cyclin A/Cdk2</td><td id="3-W">0.21 h⁻¹</td></tr>
<tr><td id="3-X">V_sd</td><td id="3-Y">rate constant for synthesis of cyclin D/Cdk4-6 induced by growth factor GF</td><td id="3-Z">0.175 h⁻¹</td></tr>
<tr><td id="3-10">vse</td><td id="3-11">rate constant for synthesis of cyclin E/Cdk2 induced by the transcription factor E2F</td><td id="3-12">0.21 h-1</td></tr>
<tr><td id="3-13">V1cdc20</td><td id="3-14">rate constant for activation of Cdc20 through phosphorylation by cyclin B/Cdk1</td><td id="3-15">0.21 h-1</td></tr>
<tr><td id="3-16">V2cdc20</td><td id="3-17">maximum rate constant for inactivation of Cdc20 through dephosphorylation</td><td id="3-18">0.35 μM h-1</td></tr>
<tr><td id="3-19">V1e2f</td><td id="3-1a">rate constant for activation of E2F by cyclin D/Cdk4-6 and cyclin E/Cdk2 complexes</td><td id="3-1b">0.805 h-1</td></tr>
<tr><td id="3-1c">V2e2f</td><td id="3-1d">rate constant for inactivation of E2F by the cyclin A/Cdk2 complex</td><td id="3-1e">0.7 h-1</td></tr>
</table>

<a id='a5ea6c08-ebe4-4d4c-b063-dd2458bdb096'></a>

We observe that equation (2.1) for cyclin D/Cdk4-6
(Md) is not coupled to the other equations. Numerical
integration of equations (2.1)-(2.6) accordingly shows
that even when the other variables oscillate in time,
variable Md rapidly reaches a steady state, which only
depends on the level of the growth factor, GF:

<a id='8821bdb0-fe62-4306-b467-b38f979f9cd8'></a>

Md = \frac{K_{dd}v_{sd}GF/(K_{gf} + GF)}{V_{dd} - (v_{sd}GF/(K_{gf} + GF))}. (2.7)

<a id='648877ec-f0c8-450f-931d-27e178731263'></a>

We shall assume that the level of Md rapidly reaches its steady-state level given by equation (2.7). The dynamics of the skeleton model for the cell cycle controlled by the level of the growth factor is thus governed by the five kinetic equations (2.2)-(2.6), supplemented by the algebraic equation (2.7).

<a id='c9dc31e9-1f3a-4a46-80f3-cd6dee7d0e6d'></a>

### 3. GROWTH FACTOR-INDUCED OSCILLATIONS IN THE NETWORK OF CYCLIN-DEPENDENT KINASES

Mammalian cells progress in the cell cycle and proliferate only in the presence of sufficient amounts of growth factor. In the absence of the growth factor, healthy cells are in a quiescent phase and do not proliferate. Figure 2 shows the dynamic behaviour of the Cdk network in the presence or absence of the growth factor, for the 39-variable model (figure 2a) and for the 5-variable model (figure 2b). In both cases, in the absence of the growth factor, i.e. for $t < 50 \text{ h}$ and $t > 200 \text{ h}$, the Cdk network,

<a id='0ebdc515-61d7-4fef-a43e-64e9dec0f3a3'></a>

characterized by the level of cyclin B/Cdk1, tends to
a stable steady state defined by low levels of the var-
ious cyclin/Cdk complexes. This stable steady state
corresponds to the quiescent phase. In the presence
of the growth factor, i.e. for 50 h<t< 200 h, the
Cdk network undergoes sustained oscillations that cor-
respond to cell proliferation [7]. The effect of the
growth factor on cell cycle progression is qualitatively
the same in the 39-variable model (figure 2a) and in
the 5-variable model (figure 2b). One noticeable differ-
ence, however, is that the limit cycle is reached right
away in the detailed model, and only after a few
cycles of increasing amplitude in the skeleton model.
This difference is due to the fact that the bifurcation
is subcritical in the detailed model, and supercritical
in the reduced model.

<a id='4f522f3a-cc43-4a15-8f57-2698e886a654'></a>

We previously showed in the detailed model that the curve showing the relative magnitude of the peak of cyclin B/Cdk1 as a function of GF exhibits a sharp threshold: above a critical value of GF, the Cdk network begins to oscillate with a high amplitude and cells enter in a proliferative mode (figure 3a, black curve). The response of the Cdk network as a function of the level of GF in the skeleton model is quite similar, but the threshold is somewhat less sharp (figure 3a, red curve). The amplitude of the peak in cyclin B/Cdk1 increases at first progressively, and then more rapidly. The bifurcation diagram for cyclin B/Cdk1 as a function of GF (see §5, figure 8d) indicates that the Cdk network tends to a stable steady state for low levels of GF. For intermediate levels of GF, the Cdk

<a id='56e6ec1a-d2d3-4619-8433-c3653237af6c'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='c360300f-eb7a-4cc9-92a7-851b87fcc914'></a>

28 A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='d7c6adb8-2c3b-4f31-8334-7c1b6152e1b7'></a>

<::Figure: Two line graphs showing temporal series of cyclin B/Cdk1 and growth factor (GF) over time. Both graphs share a common x-axis labeled "time (h)" ranging from 0 to 250. Each graph has a left y-axis labeled "cyclin B/Cdk1" and a right y-axis labeled "growth factor". The black line represents the growth factor (GF), which is 0 for t < 50 h and t > 200 h, and 1.0 for 50 h <= t <= 200 h. The red line represents cyclin B/Cdk1.

(a) The 39-variable model. The left y-axis for cyclin B/Cdk1 ranges from 0 to 0.5. The right y-axis for growth factor ranges from 0 to 1.2. The cyclin B/Cdk1 level remains near 0 when GF is 0, and shows sustained oscillations with peaks around 0.4 when GF is 1.0.

(b) The skeleton 5-variable model. The left y-axis for cyclin B/Cdk1 ranges from 0 to 3.5. The right y-axis for growth factor ranges from 0 to 1.2. The cyclin B/Cdk1 level remains near 0 when GF is 0, and shows sustained oscillations with peaks around 3.0 when GF is 1.0.

Figure 2. Growth factor-induced oscillations in the Cdk network. Temporal series of cyclin B/Cdk1 for (a) the 39-variable model and (b) the skeleton 5-variable model in the presence (50 h < t < 200 h) or absence (t < 50 h and t > 200 h) of the growth factor (GF). In both cases, the Cdk network, represented by the level of the cyclin B/Cdk1 complex, tends to a stable steady state corresponding to cell cycle arrest in the absence of the growth factor (GF = 0), and tends to a sustained oscillatory regime corresponding to cell proliferation in the presence of sufficient amounts of the growth factor (GF = 1). The values of parameters used for the 39-variable model are given elsewhere (table S2 in Gérard & Goldbeter [7]). The values of the parameters used in (b) are given in table 2.::>

<a id='edb39d4c-0e5e-4d72-800f-600ff4f97e1a'></a>

network tends to a regime of sustained oscillations characterized by small-amplitude oscillations in cyclin B/Cdk1. For high values of GF, the Cdk network tends to a regime of large-amplitude oscillations. These large amplitudes in the oscillations could corre- spond to active cell proliferation. At intermediate levels of GF, over a narrow range of GF values, two stable oscillatory regimes coexist; this phenomenon is known as birhythmicity (§5).

<a id='3dbce4ad-6f4b-496f-b85f-f94232ece583'></a>

We also studied the dynamical properties of the Cdk network as a function of the time of GF removal in the G1 phase. For the detailed model, we previously showed the existence of a sharp threshold in the rela- tive magnitude of cyclin B/Cdk1 as a function of the time at which GF is removed during the G1 phase (figure 3b, black curve). As previously discussed [7], this sharp threshold defines the existence of a restric- tion point in G1 beyond which cells do not need the presence of the growth factor anymore to complete

<a id='9820831e-a913-4d94-a957-c1de38c93d89'></a>

the cell cycle [8,9]. Even if the threshold is less sharp in the 5-variable model for the Cdk network, we observe that the amplitude of the peak in Cdk1 rapidly rises as a function of the time of GF removal in G1 (figure 3b, red curve), which also defines the existence of a restriction point in G1. The fact that the threshold is less sharp in this version of the model is due to the absence of positive feedback loops in the Cdk1 module. In contrast, in the 39-variable model, two such positive feedback loops are present in the Cdk1 module: the first one is due to the mutual activation between cyclin B/Cdk1 and its phosphatase Cdc25, and the second one rests on the mutual inhibition of cyclin B/Cdk1 and the kinase Weel. These two positive feedback loops give rise to bistability in the activation of cyclin B/Cdk1 [10,11], which leads to the abrupt activation of the kinase Cdk1 once GF passes a threshold.

<a id='629f6a50-0be3-4e43-be49-9b1f589341ae'></a>

In the presence of sufficient amounts of growth factor, the Cdk network self-organizes in time in the form of sustained oscillations (figure 2). The repetitive, ordered activations of the various cyclin/Cdk complexes in the detailed model and in the skeleton model are shown in figure 4a,b, respectively. The cyclin D/ Cdk4-6 complex, which promotes progression in G1, changes only slightly during cell cycle progression [12]. In agreement with these experimental observations, this complex fluctuates with a small amplitude in the 39-variable model as a result of its binding to p21/ p27; the latter inhibitor of Cdk2 and Cdk1 also binds to Cdk4-6 but does not affect its activity [13]. In the skeleton model, the level of cyclin D/Cdk4-6, given by equation (2.7), remains constant. In both the detailed and skeleton models for the Cdk network, the oscillations occur successively in cyclin E/Cdk2, which triggers the G1/S transition, cyclin A/Cdk2, which ensures progression in S and elicits the S/G2 transition, and cyclin B/Cdk1, which brings about the G2/M transition.

<a id='f7553b82-c82c-45cc-97f0-99c49f68f559'></a>

Sustained oscillations of the various cyclin/Cdk complexes correspond to the evolution to a limit cycle. Figure 5 shows the projection of the limit cycle onto the plane formed by the concentrations of cyclin A/Cdk2 and cyclin B/Cdk1, for the detailed, 39-variable model (figure 5a) and for the skeleton, 5-variable model (figure 5b). The transitions between the different phases of the cell cycle are less abrupt in the skeleton than in the detailed model. This is again due to the absence of any positive feedback loop in the 5-variable model, in contrast to the detailed model in which various positive feedback loops give rise to bistable behaviour and, thereby, to all-or-none transitions in several Cdk modules [7]. Positive feedback loops thus contribute to the abrupt activation of cyclin/Cdk complexes, leading to more abrupt transitions between the successive phases of the cell cycle, as shown in figure 5a. We note, however, that if the positive feedback loops, which are present in the detailed model, contribute to abrupt, large-amplitude changes in Cdk activation, they are not crucial to generate sustained oscillations in the Cdk network, as shown by the skeleton model, in agreement with experimental observations which show, nevertheless,

<a id='5c2b5684-5712-4e24-8e62-ebb167ca10a9'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='2a134e4a-c011-432a-8f79-e8d3c197b46a'></a>

A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='066f9cc4-0c0a-4b21-8365-1b58560e1254'></a>

29

<a id='c2735f37-6ee0-4e78-ae3d-e1f1e83f6397'></a>

<::chart: The image displays two line graphs, (a) and (b), comparing 39-variable (black curve) and 5-variable (red curve) models.

Graph (a) is titled "relative magnitude of peak in cyclin B/Cdk1" on the y-axis (ranging from 0 to 1.2) versus "growth factor (GF)" on the x-axis (log scale from 0.001 to 10). The curves show a sharp transition from a "quiescence" state (low relative magnitude) to a "proliferation" state (high relative magnitude, near 1.0). The 5-variable model shows this transition at a lower GF concentration than the 39-variable model.

Graph (b) is titled "relative magnitude of peak in cyclin B/Cdk1" on the y-axis (ranging from 0 to 1.2) versus "time of GF removal after preceding peak of cyclin B/Cdk1 (h)" on the x-axis (ranging from 0 to 8). Both curves start at a low relative magnitude and rise sharply to a high relative magnitude (near 1.0) as the time of GF removal increases. The 39-variable model shows this sharp increase at an earlier time (around 2-3 hours) compared to the 5-variable model (around 3-4 hours).

Figure 3. Effect of growth factor on the dynamics of the Cdk network and the presence of a restriction point in G1. (a) A sharp threshold in the concentration of GF separates a non-proliferative, quiescent state (below threshold) and a proliferative state (above threshold) where the oscillations of the cyclin/Cdk complexes in the Cdk network reach a maximum level. The dynamic behaviour of the Cdk network is represented for the 39-variable (black curve) and for the skeleton, 5-variable (red curve) models by the steady state or by the maximum level of cyclin B/Cdk1 in the course of oscillations, divided by the maximum amplitude of the peak in cyclin B/Cdk1 observed in the course of oscillations at large values of GF. (b) The existence of a restriction point in G1 is reflected by the threshold in the curve showing the magnitude of the peak of cyclin B/Cdk1 relative to the magnitude of the preceding peak in cyclin B/Cdk1 as a function of the time at which GF is removed in G1. The curves pertain to the 39-variable (black curve) and to the skeleton, 5-variable (red curve) models. Parameter values used for the 5-variable model are listed in table 2 (see [7] for the parameter values used for the 39-variable model).::>

<a id='f635d45a-555a-4417-aefb-fc21b8f720f8'></a>

Figure 4. <::chart: Chart (a) displays cyclin/Cdk complex activation over time (h). The left y-axis is 'cyclin E/Cdk2, cyclin A/Cdk2 and cyclin B/Cdk1' ranging from 0 to 0.5. The right y-axis is 'cyclin D/Cdk4-6' ranging from 1.26 to 1.36. The black line, labeled 'D/Cdk4-6', shows slight variations around 1.32-1.34. The red line, labeled 'B/Cdk1', oscillates with peaks around 0.4. The blue line, labeled 'A/Cdk2', oscillates with peaks around 0.3, phase-shifted from B/Cdk1. The green line, labeled 'E/Cdk2', oscillates with peaks around 0.2, phase-shifted from A/Cdk2. Chart (b) displays cyclin/Cdk complex activation over time (h). The y-axis is 'cyclin E/Cdk2, cyclin A/Cdk2 and cyclin B/Cdk1' ranging from 0 to 3.5. The red line, labeled 'B/Cdk1', oscillates with peaks around 3.0. The blue line, labeled 'A/Cdk2', oscillates with peaks around 2.5, phase-shifted from B/Cdk1. The green line, labeled 'E/Cdk2', oscillates with peaks around 3.0, phase-shifted from A/Cdk2 and B/Cdk1. Both charts show self-sustained oscillations in the presence of sufficient amounts of growth factor. The curves show the periodic activation of the four cyclin/Cdk complexes for the 39-variable model (a) and for the skeleton, 5-variable model (b). In both cases, the sequential, repetitive activation of the various cyclin/Cdk complexes ensures the correct progression along the successive phases of the cell cycle. In agreement with the observation that the level of cyclin D/Cdk4–6 remains more or less constant during the cell cycle, this complex varies only slightly in the detailed model and remains constant in the skeleton model. Parameters used in (a) for the 39-variable model are given in table S2 in Gérard & Goldbeter [7]. (b) Parameter values are listed in table 2.::>


<a id='f1d5b9d3-39da-4489-bafd-6301e87f0ace'></a>

<::visual content: chart: (a) A phase plane plot showing limit cycle oscillations for the 39-variable model. The x-axis is labeled "cyclin A/Cdk2" and ranges from 0 to 0.30 in increments of 0.05. The y-axis is labeled "cyclin B/Cdk1" and ranges from 0 to 0.5 in increments of 0.1. A red closed loop curve represents the limit cycle. Arrows on the curve indicate the direction of movement: an arrow pointing down on the left side is labeled "M/G1", an arrow pointing right on the bottom side is labeled "S/G2", and an arrow pointing up-left on the top-right side is labeled "G2/M". (b) A phase plane plot showing limit cycle oscillations for the 5-variable model. The x-axis is labeled "cyclin A/Cdk2" and ranges from 0 to 3.5 in increments of 0.5. The y-axis is labeled "cyclin B/Cdk1" and ranges from 0 to 3.5 in increments of 0.5. A red closed loop curve, shaped like an elongated oval, represents the limit cycle. Arrows on the curve indicate the direction of movement: an arrow pointing down-left on the left side is labeled "M/G1", an arrow pointing up-right on the bottom-right side is labeled "S/G2", and an arrow pointing up-left on the top-right side is labeled "G2/M". Figure 5. Limit cycle oscillations in the Cdk network. The oscillations of figure 4a,b correspond to the evolution to a limit cycle shown as a projection onto the cyclin A/Cdk2 versus cyclin B/Cdk1 phase plane for the 39-variable model (a) and for the 5-variable model (b). Arrows show the direction of movement on the limit cycle. Parameter values are as in figure 4.::>

<a id='6c12bba1-be91-4ccd-bf10-f356b84f4b7f'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='075bba05-ad1d-42b1-849e-ae6c31b21753'></a>

30 A skeleton model for the cell cycle C. Gerard and A. Goldbeter

<a id='dc2001ed-d905-4703-ac58-732165377be9'></a>

<::Figure: Flowchart::> (a) Oscillator A: A flowchart showing GF (Growth Factor) activating cyclin D/Cdk4–6. Cyclin D/Cdk4–6 activates E2F (i) and E2F (a). E2F (i) and E2F (a) form a positive feedback loop with each other. E2F (a) activates cyclin E/Cdk2 and cyclin A/Cdk2. Cyclin A/Cdk2 provides a negative feedback loop to E2F (a). Arrows indicate forward progression from cyclin D/Cdk4–6, cyclin E/Cdk2, and cyclin A/Cdk2. (b) Oscillator B: A flowchart showing GF activating cyclin D/Cdk4–6. Cyclin D/Cdk4–6 activates E2F (i) and E2F (a). E2F (i) and E2F (a) form a positive feedback loop with each other. E2F (a) activates cyclin E/Cdk2 and cyclin A/Cdk2. Cyclin A/Cdk2 provides a negative feedback loop to E2F (a). Cyclin E/Cdk2 also provides a negative feedback loop to itself. Arrows indicate forward progression from cyclin D/Cdk4–6, cyclin E/Cdk2, and cyclin A/Cdk2. (c) Oscillator C: A flowchart showing cyclin A/Cdk2 activating cyclin B/Cdk1. Cyclin B/Cdk1 activates Cdc20 (i) and Cdc20 (a). Cdc20 (i) and Cdc20 (a) form a positive feedback loop with each other. Cdc20 (a) provides a negative feedback loop to cyclin B/Cdk1. Arrows indicate forward progression from cyclin A/Cdk2 and cyclin B/Cdk1.Figure 6. Multiple oscillatory circuits are present in the skeleton, 5-variable model for the Cdk network. All these circuits are based on a negative feedback loop and can generate sustained oscillations of the cyclin/Cdk complexes involved in the circuit. Oscillators A (a) and B (b) involve the transcription factor E2F, cyclin D/Cdk4–6, cyclin E/Cdk2 and cyclin A/Cdk2, but not the cyclin B/Cdk1 complex and the protein Cdc20. Thus, they can produce sustained oscillations of Cdk2, which is responsible for DNA replication, without oscillation of Cdk1, which is responsible for the G2/M transition. In these conditions, cells go through multiple rounds of DNA replication without passing through mitosis. This phenomenon corresponds to endoreplication. Oscillator C (c) involves cyclin A/Cdk2 and cyclin B/Cdk1, and can therefore be viewed as a mitotic oscillator.::>

<a id='bc744837-bc82-4a44-9aa5-72904c7bf229'></a>

that oscillations are more robust in the presence of positive feedback [14].

<a id='de6c9762-f275-4793-9ed5-45ebb93f4fc7'></a>

4. MULTIPLE OSCILLATORY CIRCUITS
IN THE SKELETON MODEL FOR THE
NETWORK OF CYCLIN-DEPENDENT
KINASES

The Cdk network contains several negative feedback
loops that can give rise to oscillatory behaviour. In
the 39-variable model for the Cdk network, we
showed that there are at least four negative feedback
circuits that can generate sustained oscillations in the
Cdk network. Two oscillators involve Cdk1, responsible
for the entry of the cell in mitosis, and are therefore con-
sidered as mitotic oscillators. The two others involve
only Cdk2, which is responsible for DNA replication,
without oscillation of Cdk1. The two latter oscillators
will thus promote multiple rounds of DNA replication
without occurrence of mitosis. This phenomenon is
known as endoreplication [15,16]. The possibility of
endoreplication in theoretical models for the yeast cell
cycle [17] and for the eukaryotic cell cycle [18] was pre-
viously reported.

<a id='d9fc5afa-792a-4d64-b10e-62d481ae6006'></a>

The 5-variable skeleton model contains all the negative feedback loops present in the more detailed, 39-variable model [7]. However, instead of the four oscillatory circuits observed in the detailed model, the skeleton model contains only three such circuits

<a id='2d420866-817b-491f-a862-827764e0a268'></a>

(figure 6). Oscillators A and B involve Cdk2 but not Cdk1; this situation can lead to endoreplication. Oscillator C involves both Cdk2 and Cdk1, and can thus be considered as a mitotic oscillator. In the scheme of figure 1, there is the possibility of a fourth oscillator based on the Cdk1 induction of its own inactivation. Indeed, cyclin B/Cdk1 can activate the protein Cdc20, which enhances the degradation of cyclin B/Cdk1. This negative feedback loop will, however, not lead to sustained oscillations in the 5-variable model because in this model the regulatory loop is too short and does not allow for sufficient delay between the activation of Cdc20 by cyclin B/Cdk1 and the degradation of cyclin B/Cdk1 by Cdc20. In contrast, in the 39-variable model, this negative feedback loop can create sustained oscillations because the delay is longer, as we took explicitly into account in this model the reversible formation of a complex between the Cdk and its corresponding cyclin as well as the existence of an active, dephosphorylated form and an inactive, phosphorylated form of Cdk1 [7]. This fourth oscillatory circuit in the detailed model is similar to the mitotic oscillator driving embryonic cell cycles [19].

<a id='097b8335-41c1-4f33-bb79-27c8c037e840'></a>

The oscillations generated by the three oscillatory cir-cuits A, B and C of figure 6 are shown in figure 7a-c, respectively. While oscillators A and B correspond to endoreplication, for oscillator C the existence, in each cycle, of one peak of cyclin A/Cdk2 followed by one

<a id='f4ebfc04-aea7-49d1-ac35-df39ab10b44d'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='4111d11e-044d-4a0b-b1fd-bbca2ed6a0d6'></a>

_A skeleton model for the cell cycle_ C. Gérard and A. Goldbeter

<a id='5c8c6829-1d2d-45af-b98b-03b25b0853cc'></a>

31

<a id='9400eda7-7416-4218-a826-a86e7cd2f8f5'></a>

<::Figure 7: Two line graphs showing oscillations of cyclin/Cdk complexes over time.
(a) The top graph shows the concentration of cyclin E/Cdk2 and cyclin A/Cdk2.
The Y-axis is labeled "cyclin E/Cdk2 and cyclin A/Cdk2" and ranges from 0 to 2.0.
A green line represents A/Cdk2, showing oscillations peaking at approximately 1.9.
A blue line represents E/Cdk2, showing oscillations peaking at approximately 1.3, with its peaks slightly preceding those of A/Cdk2.
(c) The bottom graph shows the concentration of cyclin A/Cdk2 and cyclin B/Cdk1.
The Y-axis is labeled "cyclin A/Cdk2 and cyclin B/Cdk1" and ranges from 0 to 3.5.
The X-axis is labeled "time (h)" and ranges from 0 to 120.
A red line represents B/Cdk1, showing oscillations peaking at approximately 3.2.
A green line represents A/Cdk2, showing oscillations peaking at approximately 2.6, with its peaks slightly preceding those of B/Cdk1.
Both graphs illustrate sustained oscillatory behavior of the cyclin/Cdk complexes.
Caption: 7 Oscillations produced by the multiple oscillatory circui::>

<a id='dfc75e2a-a26a-4e85-a80a-8b37b074c6c3'></a>

<::Figure (b) shows a line graph with an unlabelled y-axis ranging from 0 to 4.0, and an unlabelled x-axis. Two oscillating lines are plotted: a green line labelled 'A/Cdk2' and a blue line labelled 'E/Cdk2'. The A/Cdk2 line peaks at approximately 3.75, while the E/Cdk2 line peaks at approximately 1.5. Both lines show periodic fluctuations. Figure (d) shows a line graph with the y-axis labelled 'cyclin E,A/Cdk2 and cyclin B/Cdk1' ranging from 0 to 1.2, and the x-axis labelled 'time (h)' ranging from 0 to 120. Three oscillating lines are plotted: a green line labelled 'A/Cdk2' peaking at approximately 1.15, a blue line labelled 'E/Cdk2' peaking at approximately 0.6, and a red line labelled 'B/Cdk1' which remains very low, peaking slightly above 0.0 at regular intervals. All lines exhibit periodic fluctuations, similar to those in figure (b) but with different magnitudes and the addition of the B/Cdk1 line.: figure::>

<a id='059e8d6e-80e9-49f0-b301-2cbbdec5d208'></a>

Figure 7. Oscillations produced by the multiple oscillatory circuits present in the skeleton model for the Cdk network. (a) Oscillations of cyclin E/Cdk2 and cyclin A/Cdk2 produced by oscillator A (figure 6a). In these conditions, vsd = 0.5 µM h⁻¹, Vdd = 1 µM h⁻¹, E2Ftot = 2 µM, V1e2f = 2.8 h⁻¹, V2e2f = 2.2 h⁻¹, K1e2f = K2e2f = 0.005 µM, vse = 0.6 h⁻¹, Vde = 1 h⁻¹, vsa = 0.5 h⁻¹, Vda = 0.7 h⁻¹. (b) Oscillations of cyclin E/Cdk2 and cyclin A/Cdk2 produced by oscillator B (figure 6b). In these conditions, vsd = 0.8 µM h⁻¹, Vdd = 1 µM h⁻¹, V1e2f = 4 h⁻¹, V2e2f = 2 h⁻¹, E2Ftot = 2 µM, vse = 0.2 h⁻¹, Vde = 0.2 h⁻¹, Kde = 0.01 µM, vsa = 0.5 h⁻¹, Vda = 0.7 h⁻¹, K1e2f = K2e2f = 0.1 µM. (c) Oscillations of cyclin A/Cdk2 and cyclin B/Cdk1 produced by oscillator C (figure 6c). Here, vsa = 0.5 h⁻¹, vsb = 0.6 h⁻¹, Vda = 0.7 h⁻¹, Vdb = 0.8 h⁻¹, V1cdc20 = 0.6 h⁻¹, V2cdc20 = 1 µM h⁻¹. (d) Oscillations of cyclin E/Cdk2, cyclin A/Cdk2 and cyclin B/Cdk1 for the full 5-variable model in conditions allowing for endoreplication. Some parameter values have to be modified in table 2 to obtain endoreplication behaviour: Vda = 52.5 h⁻¹ instead of 0.245 h⁻¹, vsb = 0.0035 h⁻¹ instead of 0.21 h⁻¹ and Vdb = 1.75 h⁻¹ instead of 0.28 h⁻¹. In all cases, other parameter values are as in table 2.

<a id='2f387f1d-f6c4-44e6-b2ac-2979ab25f1f0'></a>

peak of cyclin B/Cdk1 defines the repetitive passage
through DNA replication and mitosis, which corresponds
to the 'classical' mitotic cell cycle.

<a id='2c78eeeb-7f4d-4ca0-b36d-82518b50bbd7'></a>

To reveal the existence of the three oscillators of figure 6 and to obtain their corresponding time series shown in figure 7a-c, we decomposed the Cdk network of figure 1 so as to isolate each negative feedback circuit capable of generating sustained oscillations. In physiological conditions, however, all these oscillatory circuits are tightly coupled in the Cdk network. It is therefore important to determine whether endoreplication may occur when all the oscillators are present, as is the case in the full model of figure 1. As shown in figure 7d, sustained oscillations of cyclin E/Cdk2 and cyclin A/Cdk2 may indeed occur, for appropriate

<a id='64cc7cf3-e7e2-4eaa-9a61-5837f0680429'></a>

parameter values, in the full skeleton model without
significant oscillation of cyclin B/Cdk1.

<a id='2b8bf876-55d4-4a01-a9fa-9813aa601098'></a>

## 5. COMPLEX OSCILLATIONS:
BIRHYTHMICITY, QUASI-PERIODIC
BEHAVIOUR AND CHAOS
The presence of multiple sources of oscillations can generate complex oscillatory behaviour in regulatory networks [20,21]. We recently observed such complex patterns of oscillatory dynamics in the detailed model for the Cdk network [22]. We show here that the interplay between multiple oscillatory mechanisms in the skeleton model can also be the source of complex

<a id='a74e6cc8-a860-43f0-a8e0-9b99281ef4cb'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='bb8b5f33-be88-4e3e-bcb6-9b4aa20f215b'></a>

32 A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='af0e0be7-8759-4612-90e3-43a11e442863'></a>

<::A multi-panel figure (a, b, c, d) titled "Figure 8. Birhythmicity in the skeleton model for the Cdk network driving the mammalian cell cycle." The stable oscillations can be observed in the model when GF = 0.1 µM (see the bifurcation diagram in (d)). The level of cyclin B/Cdk1 is equal to 1.1 µM in (a) and for the black curve in (c), or 1.2 µM in (b) and in (c). The bifurcation diagram in (d) shows the level of cyclin B/Cdk1 as a function of GF. Black curve represents stable steady state, red dashed line represents unstable steady state or the envelope of unstable oscillations, and blue curve represents envelope of stable oscillations. The Cdk network tends to a stable steady state for a low level of GF, and to a unique oscillatory regime at high levels. At intermediate levels of GF (close to 0.1 µM), the Cdk network can evolve to either one of two stable oscillations. In (a)-(c), the initial conditions for the other variables of the model are equal to 0.01 µM. Other parameter values are given in table 2.

Panel (a): A line graph showing cyclin B/Cdk1 on the y-axis (from 0 to 3.2) versus time (h) on the x-axis (from 0 to 500). The black line shows oscillations that start with a higher amplitude and then settle into a stable limit cycle around 0.6-1.6 on the y-axis.

Panel (b): A line graph showing cyclin B/Cdk1 on the y-axis (from 0 to 3.2) versus time (h) on the x-axis (from 0 to 400). The black line shows oscillations that start with a lower amplitude and then grow to a stable limit cycle around 0.4-2.8 on the y-axis.

Panel (c): A phase portrait showing cyclin B/Cdk1 on the y-axis (from 0 to 3.0) versus cyclin A/Cdk2 on the x-axis (from 0 to 3.0). It displays two stable limit cycles. The inner loop is black, showing a counter-clockwise trajectory, representing the 1.1 µM oscillation. The outer loop is red, also showing a counter-clockwise trajectory, representing the 1.2 µM oscillation.

Panel (d): A bifurcation diagram showing cyclin B/Cdk1 on the y-axis (from 0 to 3.5) versus growth factor (GF) on a logarithmic x-axis (from 0.001 to 0.1). A black line indicates a stable steady state at low GF values. A blue line indicates the envelope of stable oscillations, appearing at higher GF values. A red dashed line indicates an unstable steady state or the envelope of unstable oscillations, connecting the stable steady state and the oscillatory regimes.::>

<a id='80c3e4df-3707-4840-87d6-75fffe26155c'></a>

oscillatory behaviour in the form of birhythmicity,
quasi-periodic oscillations or chaos.

<a id='95016012-6023-4206-b3d5-5d76b39f8378'></a>

In the bifurcation diagram of figure 8d where the amplitude of cyclin B/Cdk1 is plotted as a function of GF, we observe that for intermediate values of GF, there is a range in which two stable oscillatory regimes of distinct amplitudes coexist. These stable oscillations are separated by an unstable periodic solution. The two stable oscillations (figure 8a,b) can be reached from closely related initial conditions corresponding to a point in the vicinity of the unstable oscillatory regime. The two limit cycle trajectories corresponding to the stable oscillations are shown in figure 8c as projections onto the phase plane formed by cyclin B/Cdk1 and cyclin A/Cdk2. The period of the small stable limit cycle is close to 24.1 h, while that of the large-amplitude limit cycle is close to 25.1 h.

<a id='3933d847-8c3b-4060-aff6-93070e424aa4'></a>

The skeleton model for the Cdk network can also exhibit quasi-periodic oscillations, as shown in figure 9 where cyclin B/Cdk1 is plotted as a function of time in figure 9a. Part of this time series is enlarged in figure 9b, while the phase plane projection of the corresponding trajectory is shown in figure 9c. To establish the quasi-periodic nature of these complex oscillations, we obtained a Poincaré section, which takes the characteristic form of a closed curve (figure 9d).

<a id='efe6862c-240d-4a5b-83c6-d7e8d38e82cb'></a>

Deterministic chaos can also be observed in the
skeleton model for the Cdk network (figure 10). The
time series for cyclin B/Cdk1 starting from two
slightly different initial conditions in figure 10a show
that the trajectories eventually diverge in time; such
a sensitivity to initial conditions is characteristic of
chaotic behaviour. An enlargement of the oscillatory
time course of cyclin B/Cdk1 is shown in figure 10b.

<a id='856e4dad-b1bb-4303-a00a-c7f3e8b49259'></a>

Interface Focus (2011)

<a id='6038ebb7-15c6-45cd-a1c8-8e95daba4fc2'></a>

<::Figure: The image displays three separate plots. The top plot shows a black oscillating waveform, with the x-axis ranging from 00 to 500. The middle plot is a short, solid blue horizontal line segment. The bottom plot features two horizontal line segments: a dashed red line positioned above a solid blue line, with the x-axis labeled '1'. The accompanying text describes the coexistence of two states. Initial conditions: and for the red curve stable steady state; ble oscillations. The levels of GF. At inter-; (birhythmicity). In values are the same as::>

<!-- PAGE BREAK -->

<a id='389487a2-98b5-4f36-8766-6bc2de7e0e16'></a>

_A skeleton model for the cell cycle_ C. Gérard and A. Goldbeter

<a id='743ecc00-3715-4c0a-8df9-20321be064cd'></a>

33

<a id='9de7a8cb-809d-499d-8c85-b897e58b0de6'></a>

<::
Figure 9. Quasi-periodic oscillations in the skeleton model for the Cdk network.
(a) Time series of cyclin B/Cdk1. This plot shows cyclin B/Cdk1 concentration on the y-axis (ranging from 0 to 2.0) against time (h) on the x-axis (ranging from 0 to 500). The graph displays a quasi-periodic oscillatory pattern.
(b) Time series of a portion of the time series shown in (a). This plot shows cyclin B/Cdk1 concentration on the y-axis (ranging from approximately 0.2 to 1.8) against time (h) on the x-axis (ranging from 0 to 50). It magnifies a section of the oscillations seen in (a).
(c) Phase plane trajectory of cyclin B/Cdk1 and cyclin E/Cdk2. This plot shows cyclin B/Cdk1 concentration on the y-axis (ranging from 0 to 2.0) against cyclin E/Cdk2 concentration on the x-axis (logarithmic scale, ranging from 0.0001 to 1.0). The trajectory forms a complex, multi-layered spiral.
(d) Potassium current (IK) versus cyclin B/Cdk1 and cyclin A/Cdk2 corresponding to the successive passages of cyclin E. This plot shows a quantity on the y-axis (ranging from 0.2 to 1.2, likely IK) against another quantity on the x-axis (ranging from 0 to 0.2, likely related to cyclin B/Cdk1 or cyclin A/Cdk2). The plot shows a looped trajectory.
SE = 0.01 M, µ = 0.01 M⁻¹, K₁ = 0.7 M⁻¹, V = 0.1 M⁻¹.
: chart::>

<a id='6259687b-e5a4-4b22-a801-7bc0094eb8b5'></a>

(b)

<::A line graph with an unlabeled y-axis and an x-axis labeled "time (h)" ranging from 0 to 200. The graph displays a complex, fluctuating black curve with multiple peaks and troughs.::>

<a id='c43d22b8-9b43-4fab-a13a-bab3ab6a7286'></a>

periodic oscillations in the skeleton model for the Cdk network. (a) Time evolution of cyclin B/Cdk1. (b) Enlarge-1 of the time series shown in (a).
<::chart: (c) Phase plane trajectory. Plot showing cyclin B/Cdk1 (y-axis, 0.0 to 2.0) versus cyclin E/Cdk2 (x-axis, 0.0001 to 1.0, log scale). The plot displays a complex, multi-loop trajectory, indicating oscillatory behavior.
(d) Poincaré section showing the levels of cyclin A/Cdk2 corresponding to the successive passages of cyclin E/Cdk2 through a maximum. Plot showing unlabeled y-axis (0.2 to 1.2) versus cyclin A/Cdk2 (x-axis, 0 to 0.8). The plot displays a closed loop trajectory composed of dashed and dotted lines.
Parameters: = 0.01 µM, Vsd = 0.01 µM h⁻¹, Vdd = 0.7 µM h⁻¹, V1e2f = 3.1 h⁻¹, V2e2f = 2 h⁻¹, Vse = 0.6 h⁻¹, Vde = 1 h⁻¹ a = 0.7 h⁻¹, Kda = 0.25 µM, Vsb = 1.06 h⁻¹, Vdb = 0.8 h⁻¹, Kdb = 0.25 µM, V1cdc20 = 1.185 h⁻¹, V2cdc20 = K2cdc20 = 0.01 µM, Cdc20tot = 2 µM. Other parameter values are listed in table 2.::>


<a id='7df2c851-b64f-4938-81f1-157af4c07a49'></a>

In phase space, the system evolves towards a strange
attractor (figure 10c). The associated Poincaré section
is represented in figure 10d.

<a id='cab8a51a-36ef-489d-b765-18443d2f9694'></a>

Finally, the skeleton model for the mammalian cell
cycle can also display complex periodic oscillations
(results not shown). In such a case, the phase space tra-
jectory takes the form of a folded limit cycle, and the
Poincaré section reduces to a limited set of distinct
points corresponding to the number of peaks per period.

<a id='4c907615-5024-4259-8e31-9102bb56e231'></a>

## 6. DISCUSSION
In this study, we proposed a skeleton 5-variable model for the dynamics of the Cdk network that controls the mammalian cell cycle. This model incorporates the core regulations considered in a much more detailed model for the Cdk network, which counts 39 variables [7]. Much as this detailed model, the skeleton model is built around the four cyclin/Cdk complexes that control progression along the successive phases of the mammalian cell cycle (figure 1). The main goal of this study was to compare the dynamic behaviour of the skeleton model with that of the 39-variable model for the Cdk network.

<a id='14d20df9-8ad4-4884-a618-dc3865256510'></a>

In both models, the Cdk network responds in the same way as a function of the presence of the growth factor: in the absence of the growth factor, the network tends to a stable steady state corresponding to a quies- cent phase, while in the presence of sufficient amounts of the growth factor, it displays sustained oscillations that correspond to the sequential activation of the var- ious cyclin/Cdk complexes, thereby allowing the correct progression along successive cell cycle phases. These sustained oscillations correspond to the evolution to a limit cycle. One noticeable difference is that oscillations in the skeleton model are less abrupt than in the detailed model, because the former lacks bistable tran- sitions associated with the positive feedback loops that are present in the more detailed system.

<a id='3cec03bc-eeff-43cc-b50b-45d5debc1919'></a>

Both models for the Cdk network contain several negative feedback circuits that can generate on their own sustained oscillations (figures 6 and 7). Two of these oscillators involve the kinase Cdk2, which is responsible for DNA replication, without the intervention of the kinase Cdk1, which is responsible for entry into mitosis, and therefore correspond to endoreplication. The interaction between these multiple oscillators can produce complex periodic behaviour, quasi-periodic oscillations (figure 9) and deterministic chaos (figure 10)

<a id='063a9bd7-0cbd-44bd-85f5-119d910cd4e5'></a>

Interface Focus (2011)

<a id='d8029221-90ee-49c9-803b-7458c1728ecb'></a>

Figure 9. Quasi-pe
ment of a portion
B/Cdk1 and cyc
values are: GF =
vsa = 0.5 h⁻¹, Vd
1 µMh⁻¹, K1cdc20

<!-- PAGE BREAK -->

<a id='bcec149a-bbf2-4ed6-bea5-ebd96bc986c4'></a>

34 A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='4f576382-3a54-4d7e-a3a7-14abc1b36327'></a>

<::chart: Figure 10. Chaos in the skeleton model for the Cdk network. The figure contains four sub-plots (a), (b), (c), and (d). (a) Time evolution of cyclin B/Cdk1 for two closely related initial values of cyclin A/Cdk2: 0.0099 μM (black curve) and 0.01 μM (red curve). The initial values of the other variables are equal to 0.01 μM. The sensitivity to initial conditions is indicative of chaotic behaviour. The x-axis is 'time (h)' ranging from 1000 to 1500, and the y-axis is 'cyclin B/Cdk1' ranging from 0 to 5. (b) Enlargement of a portion of the time series shown in (a). The x-axis is 'time (h)' ranging from 1000 to 1300, and the y-axis is 'cyclin B/Cdk1' ranging from 0 to 4. (c) Phase plane trajectory showing the evolution to a strange attractor. The x-axis is 'cyclin E/Cdk2' on a logarithmic scale from 10⁻⁷ to 10, and the y-axis is 'cyclin B/Cdk1' ranging from 0 to 6.4. (d) Poincaré section established as in figure 9d. The x-axis is 'cyclin A/Cdk2' ranging from 0 to 2.0, and the y-axis is 'cyclin B/Cdk1' ranging from 0 to 3.0. The rate constant for activation of E2F, V1e2f, is equal to 2.6 h⁻¹. Other parameter values are as in figure 9.::>

<a id='fd766d11-2bb0-47f4-a67e-3945b74fdd58'></a>

both in the skeleton version and in the detailed model
[22]. The coexistence between two stable modes of
oscillations (birhythmicity) occurs in the skeleton
model (figure 8), but has not been observed so far in
the detailed model for the mammalian cell cycle.

<a id='96ff044f-f992-4667-bd7c-3eb6c41a7d7f'></a>

From the above results, we conclude that the skel-eton, 5-variable model proposed in this study provides a good qualitative approximation of the 39-variable model previously proposed for the mammalian cell cycle [7]. To obtain the reduced version, as explained in §2, we had to pay a price by making a number of simplifying assumptions and by relinquishing a variety of biochemical details such as the control of the Cdks through phosphorylation-dephosphorylation and the associated positive feedback loops leading to bistability, the role of pRB as a brake on cell cycle progression, the role of Cdh1 and Skp2 in cyclin degradation and the effect of the protein p21/p27 as Cdk inhibitor. The skeleton model thus represents a stripped-down version of the Cdk network, but it nevertheless retains its regulatory backbone. Most features of the network dynamic behaviour observed in the detailed version are still displayed by the skeleton model. Both model-ling approaches are useful and complementary. Indeed, the detailed model for the Cdk network pro-vides a more comprehensive picture of the dynamics of the mammalian cell cycle. Being much more refined,

<a id='2b58bbd1-38a2-4012-8a25-7a74a0a5a6c3'></a>

it allows us to address more precise questions about the roles of the various molecular actors in the network. On the other hand, because the skeleton model contains five instead of 39 variables, and 24 instead of 164 parameters, it might be used more readily, e.g. for the study of synchronization or desynchronization in cell populations. The reduced version has also the merit of bringing to light the minimum regulatory structure capable of displaying the rich repertoire of dynamic behaviour seen in the detailed model for the Cdk network driving the mammalian cell cycle. As in the detailed model, the oscillations are based on the sequential activation of cyclin D/Cdk4-6, cyclin E/Cdk2, cyclin A/Cdk2 and cyclin B/Cdk1 and on the property that, once activated, each of these complexes inactivates the preceding cyclin/Cdk complex in the network.

<a id='3e35a6c1-7793-4dc7-b4bb-4a8614191b6f'></a>

The skeleton model is particularly well suited to
study complex modes of oscillatory behaviour and the
conditions in which they occur, since they generally
arise in small domains in parameter space. It is much
easier to explore the possibilities of complex oscillatory
dynamics in the skeleton model which has much fewer
parameters. Birhythmicity has accordingly been found
in the skeleton model but not yet in the detailed
model. The occurrence of chaos and birhythmicity
was previously reported in a relatively simple model
for the cell cycle [23], which was, however, not related

<a id='feb900f6-4f6c-45ba-871c-113408672931'></a>

Interface Focus (2011)

<!-- PAGE BREAK -->

<a id='a642f563-7f73-4b3a-a97c-e0cbde11aab9'></a>

A skeleton model for the cell cycle C. Gérard and A. Goldbeter

<a id='1912d996-2a45-488e-8c87-0251e6b72c8c'></a>

35

<a id='7376d19b-9d18-4fa7-8c33-016b61b0672e'></a>

as closely as the skeleton model to the dynamics of the
Cdk network driving the mammalian cell cycle.

<a id='794c0351-1994-4b07-af23-c1b31ff84db1'></a>

This work was supported by grant no 3.4607.99 from the Fonds de la Recherche Scientifique Médicale (F.R.S.M., Belgium), by the Belgian Federal Science Policy Office (IAP P6/25 'BioMaGNet': 'Bioinformatics and Modelling—From Genomes to Networks') and by the European Union through the Network of Excellence BioSim, Contract no. LSHB-CT-2004-005137.

<a id='5dfc55f4-0e4c-4a29-82ef-dea9a66b0a80'></a>

## REFERENCES

1.  Morgan, D. O. 1995 Principles of Cdk regulation. *Nature* **374**, 131–134. (doi:10.1038/374131a0)
2.  Morgan, D. O. 2006 *The cell cycle: principles of control*. Oxford, UK: Oxford University Press.
3.  Qu, Z., Weiss, J. N. & MacLellan, W. R. 2003 Regulation of the mammalian cell cycle: a model of the G1-to-S transition. *Am. J. Physiol. Cell Physiol.* **284**, 349–364.
4.  Swat, M., Kel, A. & Herzel, H. 2004 Bifurcation analysis of the regulatory modules of the mammalian G1/S transition. *Bioinformatics* **20**, 1506–1511. (doi:10.1093/bioinformatics/bth110)
5.  Novak, B. & Tyson, J. J. 2004 A model for restriction point control of the mammalian cell cycle. *J. Theor. Biol.* **230**, 563–579. (doi:10.1016/j.jtbi.2004.04.039)
6.  Aguda, B. D. 1999 A quantitative analysis of the kinetics of the G2 DNA damage checkpoint system. *Proc. Natl Acad. Sci. USA* **96**, 11 352–11 357. (doi:10.1073/pnas.96.20.11352)
7.  Gérard, C. & Goldbeter, A. 2009 Temporal self-organization of the cyclin/Cdk network driving the mammalian cell cycle. *Proc. Natl Acad. Sci. USA* **106**, 21 643–21 648. (doi:10.1073/pnas.0903827106)
8.  Pardee, A. B. 1974 A restriction point for control of normal animal cell proliferation. *Proc. Natl Acad. Sci. USA* **71**, 1286–1290. (doi:10.1073/pnas.71.4.1286)
9.  Zetterberg, A., Larsson, O. & Wiman, K. G. 1995 What is the restriction point? *Curr. Opin. Cell Biol.* **7**, 835–842. (doi:10.1016/0955-0674(95)80067-0)
10. Pomerening, J. R., Sontag, E. D. & Ferrel Jr, J. E. 2003 Building a cell cycle oscillator: hysteresis and bistability in the activation of Cdc2. *Nat. Cell Biol.* **5**, 346–351. (doi:10.1038/ncb954)
11. Sha, W., Moore, J., Chen, K., Lassaletta, A. D., Yi, C. S., Tyson, J. J. & Sible, J. C. 2003 Hysteresis drives cell-cycle

<a id='3bf8fd13-0307-4bcb-bad9-fcb2f11b9c94'></a>

transitions in *Xenopus laevis* egg extracts. *Proc. Natl Acad. Sci. USA* **100**, 975–980. (doi:10.1073/pnas.0235349100)
12 Matsushime, H., Quelle, D. E., Shurtleff, S. A., Shibuya, M., Sherr, C. J. & Kato, J. Y. 1994 D-type cyclin- dependent kinase activity in mammalian cells. *Mol. Cell. Biol.* **14**, 2066–2076.
13 Sherr, C. J. & Roberts, J. M. 1999 CDK inhibitors: posi- tive and negative regulators of G1-phase progression. *Genes Dev.* **13**, 1501–1512. (doi:10.1101/gad.13.12.1501)
14 Pomerening, J. R., Kim, S. Y. & Ferrel Jr, J. E. 2005 Sys- tems-level dissection of the cell-cycle oscillator: bypassing positive feedback produces damped oscillations. *Cell* **122**, 565–578. (doi:10.1016/j.cell.2005.06.016)
15 Edgar, B. A. & Orr-Weaver, T. L. 2001 Endoreplication cell cycles: more for less. *Cell* **105**, 297–306. (doi:10. 1016/S0092-8674(01)00334-8)
16 Parisi, T., Beck, A. R., Rougier, N., McNeil, T., Lucian, L., Werb, Z. & Amati, B. 2003 Cyclins E1 and E2 are required for endoreplication in placental trophoblast giant cells. *EMBO J.* **22**, 4794–4803. (doi:10.1093/emboj/cdg482)
17 Novak, B. & Tyson, J. J. 1997 Modeling the control of DNA replication in fission yeast. *Proc. Natl Acad. Sci. USA* **94**, 9147–9152. (doi:10.1073/pnas.94.17.9147)
18 Csikasz-Nagy, A., Battogtokh, D., Chen, K. C., Novak, B. & Tyson, J. J. 2006 Analysis of a generic model of eukaryotic cell-cycle regulation. *Biophys. J.* **90**, 4361–4379. (doi:10. 1529/biophysj.106.081240)
19 Goldbeter, A. 1991 A minimal cascade model for the mitotic oscillator involving cyclin and cdc2 kinase. *Proc. Natl Acad. Sci. USA* **88**, 9107–9111. (doi:10.1073/pnas. 88.20.9107)
20 Goldbeter, A. 1996 *Biochemical oscillations and cellular rhythms. The molecular bases of periodic and chaotic be- haviour.* Cambridge, UK: Cambridge University Press.
21 Leloup, J. C. & Goldbeter, A. 1999 Chaos and birhythmi- city in a model for circadian oscillations of the PER and TIM proteins in *Drosophila*. *J. Theor. Biol.* **198**, 445– 459. (doi:10.1006/jtbi.1999.0924)
22 Gérard, C. & Goldbeter, A. In press. From simple to complex patterns of oscillatory behavior for the mam- malian cell cycle containing multiple oscillatory circuits. *Chaos*.
23 Romond, P.-C., Rustici, M., Gonze, D. & Goldbeter, A. 1999 Alternating oscillations and chaos in a model of two coupled biochemical oscillators driving successive phases of the cell cycle. *Ann. N. Y. Acad. Sci.* **879**, 180–193. (doi:10.1111/j.1749-6632.1999.tb10419.x)

<a id='6d3b7bbd-1925-4c50-af13-9347ea6cb7ff'></a>

Interface Focus (2011)