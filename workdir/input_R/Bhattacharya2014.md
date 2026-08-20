<a id='7690be11-d117-42d4-9244-5083d48648e4'></a>

Journal of Theoretical Biology 349 (2014) 150–162

<a id='e14ea02a-8245-4807-b067-fa6929b48d57'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a person and a tree, with text on a banner around the tree and the brand name below.::>

<a id='ba774f8d-887b-43ad-85ae-14cb17d55168'></a>

Contents lists available at ScienceDirect

Journal of Theoretical Biology

journal homepage: www.elsevier.com/locate/yjtbi

<a id='c9d18b99-6c99-4b6f-ba45-d52ccc8125c2'></a>

<::Cover of "Journal of Theoretical Biology". The background is a marbled green and white pattern. In the upper left corner, there is a small logo with the text "ELSEVIER". The title "Journal of Theoretical Biology" is written in a large, red, serif font, centered on the cover.: figure::>

<a id='610b736d-a586-439f-b7a3-bdcea1c0eafe'></a>

A mathematical model of the sterol regulatory element binding protein
2 cholesterol biosynthesis pathway

<a id='438a9726-243d-40df-9e97-6409ad9c07b5'></a>

<::CrossMark logo with a red bookmark icon inside a blue circle.
: figure::>

<a id='242db775-8f61-43af-b3d2-07ef5de58904'></a>

Bonhi S. Bhattacharya⁰, Peter K. Sweby⁰, Anne-Marie Minihane ⁱ,
Kim G. Jackson ⁲,⁴, Marcus J. Tindall ⁰,⁳,⁴,*

<a id='88317acf-3d7c-4e3f-b409-eaf8d944ecfa'></a>

a Department of Mathematics and Statistics, University of Reading, Whiteknights, Reading RG6 6AX, UK
b Department of Nutrition, Norwich Medical School, University of East Anglia, Norwich NR4 7TJ, UK
c Department of Food and Nutritional Sciences, University of Reading, Whiteknights, Reading RG6 6AP, UK
d School of Biological Sciences, University of Reading, Whiteknights, Reading RG6 6AJ, UK
e Institute of Cardiovascular and Metabolic Research, University of Reading, Whiteknights, Reading RG6 6AA, UK

<a id='91e9491a-221a-40b4-84d3-72b4142d3e7c'></a>

H I G H L I G H T S

<a id='5a69cfda-1951-4b9a-90f8-60d5b5907fdb'></a>

• We formulate and analyse a nonlinear ODE model of the SREBP2 pathway.
• The mathematical model exhibits stable limit cycles under certain parameter conditions.
• Negative feedbacks in the SREBP2 pathway may help regulate cholesterol homeostasis.
• Our model provides a more accurate formulation of genetic regulation using nonlinear ODEs.

<a id='9f2c20f5-3998-444c-aa8e-62d6df7b39c3'></a>

ARTICLE INFO

Article history:
Received 18 June 2013
Received in revised form
26 December 2013
Accepted 8 January 2014
Available online 18 January 2014

Keywords:
Genetic regulation
Transcription factor
Nonlinear ordinary differential equation
SREBP-2

<a id='bb4639f6-60dc-4a2c-897d-f3fdb308d1ba'></a>

ABSTRACT
Cholesterol is one of the key constituents for maintaining the cellular membrane and thus the integrity of the cell itself. In contrast high levels of cholesterol in the blood are known to be a major risk factor in the development of cardiovascular disease. We formulate a deterministic nonlinear ordinary differential equation model of the sterol regulatory element binding protein 2 (SREBP-2) cholesterol genetic regulatory pathway in a hepatocyte. The mathematical model includes a description of genetic transcription by SREBP-2 which is subsequently translated to mRNA leading to the formation of 3-hydroxy-3-methylglutaryl coenzyme A reductase (HMGCR), a main regulator of cholesterol synthesis. Cholesterol synthesis subsequently leads to the regulation of SREBP-2 via a negative feedback formulation. Parameterised with data from the literature, the model is used to understand how SREBP-2 transcription and regulation affects cellular cholesterol concentration. Model stability analysis shows that the only positive steady-state of the system exhibits purely oscillatory, damped oscillatory or monotic behaviour under certain parameter conditions. In light of our findings we postulate how cholesterol homeostasis is maintained within the cell and the advantages of our model formulation are discussed with respect to other models of genetic regulation within the literature.
© 2014 Elsevier Ltd. All rights reserved.

<a id='fc797ca6-73ab-4785-8d23-f89214bc37ba'></a>

## 1. Introduction and motivation

As an essential constituent of the plasma membrane of mammalian cells, cholesterol is used for the maintenance of both membrane structural integrity and selective permeability (Simons and Iknonen, 2000). However, superfluous cholesterol levels result in cellular toxicity (Yeagle, 1991; Tabas, 1997; Tangirala et al., 1994). Insufficient cholesterol causes cytotoxicity via compromised membrane structure.

<a id='3122f8c7-605b-41ed-a1cc-b953cddb8a82'></a>

--- 
* Corresponding author. Permanent address: Department of Mathematics and Statistics, University of Reading, Whiteknights, Reading RG6 6AX, UK.
Tel.: +44 118 378 8992; fax: +44 118 378 6537.
E-mail address: m.tindall@reading.ac.uk (M.J. Tindall).

<a id='37e033d5-c84a-4f2f-b765-3aa933084a62'></a>

0022-5193/$- see front matter © 2014 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.jtbi.2014.01.013

<a id='b86ef5a5-9236-4b8b-92e6-22e34dd17f0a'></a>

Furthermore cellular cholesterol metabolism is a key modulator of plasma cholesterol, with the management of plasma hypercholesterolaemia at the cornerstone of population cardiovascular disease management (Grundy et al., 2004). It is therefore crucial that intracellular cholesterol levels are strictly regulated. Cellular cholesterol homeostasis, the property to maintain cholesterol concentration to within narrow ranges, results from a balance of three mechanisms: efflux, influx and biosynthesis.

<a id='bfa60e97-0003-4ee0-948e-c869b7275a9c'></a>

Understanding the mechanisms which regulate cellular cholesterol content is vital to understanding pathology associated with sub- and supra-optimal cell and blood cholesterol concentrations. These levels are dependent on both the balance between dietary cholesterol intake and *de novo* synthesis of cholesterol within cells.

<!-- PAGE BREAK -->

<a id='912a7eb9-97a2-4c94-a92f-221d468b74ee'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='8a0d7896-442e-410a-a8a8-69df66fcf23e'></a>

151

<a id='af3610a7-a8d0-4c3f-9d0f-1de0339b12b9'></a>

The low density lipoprotein receptor (LDLR) protein forms part of the lipoprotein metabolic pathway responsible for the clearance of cholesterol from the circulation (Brown and Goldstein, 1979; Goldstein et al., 1985). Biosynthesis of cholesterol is a multistep reaction in which the rate-limiting step is the reduction of 3-hydroxy-3-methylglutaryl coenzyme A (HMG-CoA) in the reaction catalysed by the enzyme HMG-CoA reductase (HMGCR).

<a id='9089b59f-13c0-4d94-9321-ddc429842a10'></a>

Over accumulation or excessive depletion of free cholesterol within the cell is prevented by a negative feedback loop that responds to elevations or depressions in intracellular cholesterol. This feedback loop exerts the majority of its control by regulating the synthesis of the two key proteins: HMGCR and LDLR. In brief, when the intracellular cholesterol level is low, both LDLR and HMGCR synthesis are activated, thereby increasing the influx of cholesterol via the LDLR pathway, and the biosynthesis of cholesterol in the cell. If conversely there are high cholesterol levels in the cell, synthesis of LDLR and HMGCR declines.

<a id='aa06014e-d4e5-4ebe-ad89-7d430acd0730'></a>

There has been much research conducted into the response of
cell cholesterol to dietary intake, with the dietary fatty acid
composition rather than cholesterol intake reported to have a
greater impact on circulating cholesterol concentrations. In parti-
cular, partial replacement of saturated fat with either monounsa-
turated (found in olive oil) or n-6 polyunsaturated (found in
vegetable oils such as sunflower oil) fatty acids have been
associated with significant reductions in both total and LDL-
cholesterol concentrations (Mensink et al., 2003; Micha and
Mozaffarian, 2010). Dietary fat composition is considered to
influence circulating cholesterol concentrations via effects on
hepatic cholesterol synthesis and the expression of genes involved
in circulating LDL-cholesterol metabolism (Xu et al., 1999).

<a id='9bb786da-5b97-4af7-9974-c0e9cc88654b'></a>

Previous mathematical modelling has included compartmental models of the lipoprotein metabolic pathway (Knoblauch et al., 2000; Packard et al., 2000; Adiels et al., 2005) and dynamic models of lipoprotein metabolism in conjunction with the LDLR pathway (August et al., 2007; Wattis et al., 2008). Of particular note in these dynamic models is the lack of explicit representation of the cholesterol biosynthesis reaction and as a consequence, the interplay between cholesterol biosynthesis, the LDLR uptake of

<a id='47952ebd-ba33-4fd7-9c2f-e3b7c3d4731a'></a>

lipoprotein cholesterol and cholesterol mediated negative feed-
back is not fully appreciated.

<a id='5b9fd569-4c50-40e6-b8a0-af3787d79303'></a>

The cholesterol biosynthetic pathway is already the basis of the most common form of pharmaceutical treatment for high plasma cholesterol levels. HMGCR inhibitors, more commonly known as statins, act as competitive inhibitors of the HMGCR enzyme. By inhibiting the biosynthesis of cholesterol, statins deplete intracellular cholesterol concentration and promote the synthesis of both HMGCR and the LDLR, thereby increasing the uptake of lipoproteins (and plasma cholesterol) via the LDLR. It is recognised that individual response to statin treatment varies widely. Genetic variation in *HMGCR* has been associated with a diminished lipid lowering response (Chasman et al., 2004; Krauss et al., 2008), suggesting that the cholesterol biosynthetic pathway plays an important role in the control of plasma cholesterol levels.

<a id='497ed5eb-109d-4c4f-ac5e-3c3425b928d0'></a>

However, relatively little modelling has been conducted to investigate the qualitative behaviour of the processes which govern _de novo_ cholesterol synthesis at a genetic level, which may provide a better understanding of such phenomena. The mathematical model presented in this paper will examine the underlying genetic mechanisms governing cholesterol biosynth-esis as a first step towards elucidating the dynamics of this pathway.

<a id='f19bafed-f025-4441-a99e-e5ce5b426134'></a>

The paper is organised as follows. In Section 2 the biological
processes which describe the genetic regulation of cholesterol
biosynthesis are reviewed. Following this, the mathematical model
is derived in Section 3 and details of model parameter values
obtained from the literature are summarised in Section 4. Model
analysis is undertaken in Sections 5–7 and the results are sum-
marised and discussed in Section 8.

<a id='e42d1a19-a753-426a-9eee-81ad66e4550e'></a>

## 2. Regulated expression of cholesterol biosynthetic genes
A major point of control of the cholesterol biosynthetic pathway occurs at the level of gene expression in response to cellular cholesterol levels, as shown in Fig. 1. The insolubility of cholesterol dictates that it cannot directly influence a genetic response.

<a id='11859ef6-ab01-4184-8d5d-ac6eebcdcdab'></a>

<::flowchart: The diagram illustrates the genetic regulation of cholesterol biosynthesis by SREBP-2 within a hepatocyte. The hepatocyte is shown as a large outer circle, containing the 'CELL CYTOPLASM'. Inside the cytoplasm, a dashed inner circle represents the 'ENDOPLASMIC RETICULUM', and within that, another dashed circle represents the 'NUCLEAR REGION'. Within the NUCLEAR REGION, the 'HMGCR GENE' is present, associated with a 'SRE' (sterol regulatory element). An arrow labeled 'HMGCR mRNA transcription' points from the HMGCR GENE to 'MH HMGCR mRNA' in the cytoplasm. From 'MH HMGCR mRNA', an arrow labeled 'HMGCR translation' points to 'HMGCR' (represented by blue hexagonal shapes). There is also an arrow labeled 'HMGCR mRNA degradation' pointing from 'MH HMGCR mRNA' to a 'Ø' symbol. The 'HMGCR' enzyme then leads to 'cholesterol synthesis' (represented by small 'C' circles). An arrow labeled 'HMGCR degradation' points from 'HMGCR' to a 'Ø' symbol. The 'cholesterol synthesis' process results in 'cholesterol' (C circles). An arrow labeled 'cholesterol degradation' points from the cholesterol out of the cell cytoplasm. The regulation by SREBP is depicted with two states: 'HIGH CHOLESTEROL' and 'LOW CHOLESTEROL FEEDBACK'. In the 'HIGH CHOLESTEROL' state, 'INACTIVE SREBP' (represented by a protein with a black head and a light blue body, associated with multiple C circles) is present. An arrow from cholesterol synthesis points to INACTIVE SREBP. In the 'LOW CHOLESTEROL FEEDBACK' state, 'ACTIVE SREBP' (represented by the protein without associated C circles) is present. An arrow points from ACTIVE SREBP to the 'SRE' element on the HMGCR GENE, indicating its role in promoting transcription. An arrow also points from INACTIVE SREBP towards ACTIVE SREBP. Fig. 1. Genetic regulation of cholesterol biosynthesis by SREBP-2. Hepatocytes synthesise HMGCR mRNA which in turn is translated into the enzyme HMGCR. HMGCR catalyses the synthesis of cholesterol which in turn influences its own transcription rate by interacting with the transcription factor SREBP; the transcription rate increases when cholesterol is low in the cell and declines when cholesterol is high. (SRE – sterol regulatory element; Mₕ – HMGCR mRNA; C – cholesterol).::>

<!-- PAGE BREAK -->

<a id='e6d43690-06d9-4998-9336-e2511a48c0ca'></a>

152

<a id='a5056458-0080-4d9a-a1ea-882f840e5757'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='b7abd72f-8248-48c9-a271-a194c3103d3a'></a>

The critical role in controlling the expression of a range of genes involved in the regulation of cellular lipid homeostasis falls to the three isoforms of the SREBP family of transcription factors, SREBP- 1a, SREBP-1c and SREBP-2. In particular, the SREBP-2 isoform is relatively specific to regulating the expression of many enzymes involved in cholesterol biosynthesis (Brown and Goldstein, 1997).

<a id='69b5852a-4b21-455f-b56e-badbf0c8c088'></a>

SREBPs exist normally in a tight complex with the SREBP cleavage activating protein (SCAP) within the endoplasmic reticu- lum of cells. SCAP consists of two domains, one of which is responsible for the association with SREBP. The other domain contains a region known as the sterol sensing domain (SSD). When the cellular cholesterol concentration becomes depleted, SCAP escorts SREBP to the Golgi apparatus of the cell, where it under- goes sequential cleavage by proteases. The net effect of this is to liberate the transcription factor, nuclear SREBP which can then enter the cell nucleus (Eberlé et al., 2004). Here it binds to a regulatory binding site (a short sequence of DNA) on the promoter region of the target gene known as the sterol regulatory element (SRE) and activates its transcription (Soutar and Knight, 1990).

<a id='04f966e1-4111-4223-bb62-620fa62cdf00'></a>

In the presence of replete cellular sterol concentrations, cholesterol binds directly to the SSD of SCAP. This causes a conformational change in SCAP which results eventually in the anchoring of the SCAP–SREBP complex to the endoplasmic reticulum (ER) membrane (Yang et al., 2002). This process is responsible for the retention of the SCAP–SREBP complex within the ER. Transcription of the target genes declines.

<a id='5311e407-5a4d-4553-b6db-7fa84bad9f96'></a>

In the context of the HMGCR gene, when a cell's cholesterol levels are low, the SCAP-SREBP complex is active and free to move. In such a state SREBP is formed and is able to reach the nucleus and activate HMGCR mRNA transcription and thus HMGCR synthesis, increasing the cholesterol concentration in the cell by upregulating its synthesis. If, conversely, there are high cellular cholesterol levels, then SCAP-SREBP is unable to move and effectively inactive. Consequently both HMGCR mRNA transcription and HMGCR translation decrease, and cholesterol synthesis is reduced.

<a id='f86d34ea-38e1-4fad-95af-f3cce5277289'></a>

In a simplified model of the gene expression response to cellular cholesterol concentration, the system can be seen as an end product negative feedback loop system, in the manner of the mathematical models of expression developed by, for example, Goodwin (1963, 1965) and Griffith (1968). In such models, the response of the gene is directly dependent upon the concentration of cholesterol. A very low level of cholesterol will provoke a large response in the synthesis of HMGCR enzyme, and vice-a-versa. Theoretically, this results in a considerable range over which the model allows cholesterol concentration to vary. This is, however, uncharacteristic of the homeostatic property which the physiological system possesses, and which ensures that cellular cholesterol can only fluctuate within a narrow range of values, to avoid the cytotoxicity associated with extreme values.

<a id='505ee9b4-f88c-40ce-b757-ddb5be095fa2'></a>

The addition of the SREBP transcription factor function models the underlying biological mechanism, and also introduces complexity to the negative feedback loop in the form of an activator function which is suppressed by accumulation of an end product. In the following section a model of this interaction between SREBP and cholesterol, and the effect on gene expression are presented.

<a id='6f08b4d1-97e1-4908-a6f2-d5efe689ef4e'></a>

## 3. The model
The interactions characterising cellular cholesterol homeostasis and its regulation by transcription factors are many, and a full model of all variables and reactions is not necessarily pragmatic. Furthermore, the number of parameter values required will increase with complexity. Previous models have shown that

<a id='1aa093b9-480f-4862-8030-a7ac523a83bb'></a>

excessive simplification can fail to reproduce dynamics which have been observed in experimental settings.

<a id='44a91bae-7290-459d-908b-574e927cf953'></a>

As an example, the work by Wattis et al. (2008) models non-lipoprotein cholesterol influx to the cell as proportional to the difference between cell cholesterol concentration and a predetermined ideal equilibrium value; this produces the correct dynamics for cell cholesterol response. An interesting consequence of this formalism, though, is that intracellular cholesterol concentration in the model reaches equilibrium rapidly (on a timescale of the order of minutes) after an influx of lipoprotein cholesterol to the cell. However, experimental results suggest that this may not be the case, with changes in intracellular cholesterol concentration occurring on timescales of 12-24 h (Liscum and Faust, 1987; Liscum et al., 1989). This suggests that not enough complexity is included here to capture the longer term dynamics of cholesterol synthesis at the level of the HMGCR gene.

<a id='2fe7260b-2a84-4c1f-9a6a-e0d923c44755'></a>

A further requirement is that the system must respond natu-
rally in the absence or presence of cholesterol as opposed to only
acting reasonably under certain circumstances. For example, in the
work of August et al. (2007), all cholesterol in the cell is assumed
to be derived from lipoprotein sources. Whilst this reproduces the
required qualitative behaviour under the conditions whereby
extracellular lipoprotein is present, in the case where this is zero,
the intracellular cholesterol level falls to zero, which is physiolo-
gically fatal for the cell.

<a id='1f81444c-5191-461d-9fdf-2396e365f6b8'></a>

The work presented in this paper is focused on formulating and analysing a nonlinear ordinary differential equation (ODE) model of the SREBP-2 cholesterol biosynthesis pathway. The goal of the work is to understand cholesterol regulation via the negative feedback between SREBP-2 transcription and cholesterol and to what extent this affects the steady-state cholesterol levels of the cell. In doing so we hope to more accurately capture cellular regulation of cholesterol and be able to understand it in the wider context of dietary cholesterol intake.

<a id='ab29f7f1-44de-42a7-b956-8c86a737ba5e'></a>

### 3.1. Mathematical model formulation

In this section we derive a system of nonlinear ODEs to describe the genetic regulation of cholesterol biosynthesis by SREBP-2 as summarised in Fig. 2.

<a id='8b2db71f-8c4c-42b3-9bd6-ae59c3ec3232'></a>

The binding of SREBP-2 to the gene, subsequent transcription and translation to HMG-CoA mRNA and production of HMGCR and <::A biochemical pathway diagram illustrates the genetic regulation of cholesterol production. A light blue rectangle labeled 'G' represents the HMGCR gene. An arrow from 'G' leads to a wavy line labeled 'M' (HMGCR mRNA), with the arrow labeled 'μm' (transcription rate). From 'M', an arrow points to a dark teal circle labeled 'H' (HMGCR enzyme), with the arrow labeled 'μh' (translation rate). From 'H', an arrow points to a light blue circle labeled 'C' (cholesterol), with the arrow labeled 'μc' (catalysis rate). Degradation pathways are shown: an arrow from 'M' points to a circle with a diagonal line (representing degradation) labeled 'Ø', with the arrow labeled 'δm'; an arrow from 'H' points to 'Ø', labeled 'δh'; and an arrow from 'C' points to 'Ø', labeled 'δc'. Regulatory feedback is depicted by a red circle labeled 'S' (SREBP) marked 'active', with an arrow pointing to 'G'. A dashed arrow originates from 'C' and points to a complex formed by a red 'S' and a light blue 'C', labeled 'inactive complex'. Another dashed arrow connects this 'inactive complex' back to the 'active S'. Fig. 2. The genetic regulation of cholesterol production by SREBP-2. The HMGCR gene $\bar{G}$ is transcribed at a rate $\bar{\mu}_m$ to produce HMGCR mRNA $\bar{M}$. This is translated at a rate $\bar{\mu}_h$ into the HMGCR enzyme $\bar{H}$. HMGCR then goes on to catalyse the reaction creating the metabolite cholesterol $\bar{C}$ at a rate $\bar{\mu}_c$. This process is under the control of the transcription factor SREBP $\bar{S}$ which acts as a transcriptional activator for the pathway. Under conditions where cholesterol $\bar{C}$ is in excess $\bar{S}$ forms an inactive complex with $\bar{C}$ and transcription of the target gene declines. HMGCR mRNA, HMGCR and cholesterol are degraded at rates $\bar{\delta}_m$, $\bar{\delta}_h$ and $\bar{\delta}_c$, respectively.: diagram::>

<!-- PAGE BREAK -->

<a id='aa031dc9-7a2b-43df-9751-da64572f1b18'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150–162

<a id='9761b447-4fdc-47a1-b59b-5840837556df'></a>

153

<a id='ecdb2e57-388f-47e5-a20b-9c69556dd0e9'></a>

cholesterol can be described by the reaction equation<::Ḡ + xS̄ <=> Ḡ : xS̄ (reaction with k̄_1 above the forward arrow and k̄_-1 below the reverse arrow)Ḡ : xS̄ → M̄ (reaction with μ̄_d above the arrow)M̄ → H̄ (reaction with μ̄_h above the arrow)H̄ → C̄ (reaction with μ̄_c above the arrow)M̄ ↓ ∅ (degradation with δ̄_m below the arrow)H̄ ↓ ∅ (degradation with δ̄_h below the arrow)C̄ ↓ ∅ (degradation with δ̄_c below the arrow): reaction equation::>(1)

<a id='ed204286-bd6d-4789-8d5b-fcce545fae43'></a>

Here x is the number of molecules of S̄ required to bind to Ḡ to produce a functional effect. This binding reaction has an association rate k̄_1 and a dissociation rate k̄_-1. M̄ is transcribed at a rate μ̄_d and H̄ is translated at a rate μ̄_h. The creation of C̄ occurs at a rate μ̄_c. δ̄_m, δ̄_h and δ̄_c are respectively the degradation rates of M̄, H̄ and C̄.

<a id='fc1ea4a0-dfb7-4b97-8bd8-2c3904b0d2ae'></a>

Similarly the binding of cholesterol to active SREBP-2 to form an inactive complex which down-regulates the transcription of cholesterol (negative feedback) is given by

<a id='5cb2ffbb-2922-4a53-883d-84ae33958be1'></a>

S + yC <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='20'%3E%3Ctext x='0' y='10' font-family='serif' font-size='10'%3Ek%E2%82%82%3C/text%3E%3Ctext x='0' y='20' font-family='serif' font-size='10'%3Ek%E2%82%8B%E2%82%82%3C/text%3E%3Cpath d='M0 10 L30 10 M30 10 L25 5 M30 10 L25 15 M30 10 L0 10 M0 10 L5 5 M0 10 L5 15' fill='none' stroke='black' stroke-width='1'%3E%3C/path%3E%3C/svg%3E" alt="k2 over k-2 equilibrium arrow"> S : yC (2)

<a id='295bf5c5-b0e1-47de-915e-610761fedfa1'></a>

where y is the number of molecules of c̅ required to bind to s̅ to cause inactivation. This binding reaction has an association rate K̅₂ and a dissociation rate K̅₋₂.

<a id='9f5c6267-91e3-4206-b03a-19bd8070afdc'></a>

We note two important biological concepts arising from the
physiological mechanism of gene expression or protein synthesis,
which will affect the form of the ODEs (Alberts et al., 2008)
describing Eqs. (1) and (2).

<a id='f734723a-b9ff-4485-9787-d6f905232b9b'></a>

(i) [G: xS] represents the concentration of DNA in an active state, which is able to undergo transcription. During transcription, activated DNA is copied by the action of an enzyme to produce mRNA. This process does not deplete [G: xS].
(ii) Protein is synthesised from mRNA via the action of ribosomes. Following protein synthesis, mRNA detaches from the ribosome and the mRNA is free to participate in further synthesis reactions until it is degraded according to its half-life. Therefore, the synthesis of the enzyme, H, does not affect the concentration of M. That is, synthesis of H will not deplete M.

<a id='1758cc39-7a34-49f0-ac27-90489852a97e'></a>

The governing ODEs equations are derived by application of the law of mass action to the biochemical reactions (1) and (2) which gives

$\frac{d\bar{g}}{dt} = \bar{k}_{-1}\bar{s}_b - \bar{k}_1\bar{s}^x\bar{g}$ (3)

$\frac{d\bar{s}}{dt} = x\bar{k}_{-1}\bar{s}_b - x\bar{k}_1\bar{s}^x\bar{g} - \bar{k}_2\bar{c}\bar{s} + \bar{k}_{-2}\bar{c}_b$ (4)

$\frac{d\bar{s}_b}{dt} = -\bar{k}_{-1}\bar{s}_b + \bar{k}_1\bar{s}^x\bar{g}$ (5)

$\frac{d\bar{m}}{dt} = \mu_d \bar{s}_b - \delta_m \bar{m}$ (6)

$\frac{d\bar{h}}{dt} = \mu_h \bar{m} - \delta_h \bar{h}$ (7)

$\frac{d\bar{c}}{dt} = \mu_c \bar{h} + y\bar{k}_{-2}\bar{c}_b - \delta_c \bar{c} - y\bar{k}_2\bar{c}\bar{s}$ (8)

$\frac{d\bar{c}_b}{dt} = \bar{k}_2\bar{c}\bar{s} - \bar{k}_{-2}\bar{c}_b$ (9)

<a id='d6ed985f-cb70-4e7a-99f4-c4731e16694b'></a>

with initial conditions
$\bar{g}(0)=\bar{g}_0$, $\bar{s}(0)=\bar{s}_0$, $\bar{s}_b(0)=0$, $\bar{m}(0)=\bar{m}_0$,
$\bar{h}(0)=\bar{h}_0$, $\bar{c}(0)=\bar{c}_0$, $\bar{c}_b(0)=0$, (10)

<a id='56eff6dc-53e2-45ec-b786-1e919fbf692c'></a>

where in the above system of equations, we use the following notation in which square brackets denote concentration: ḡ = [G], s̄ = [S], s̄_b = [G : xS], m̄ = [M], h̄ = [H], c̄ = [C] and c̄_b = [S : yC].

<a id='3e336861-3a3e-44b7-aa55-b9aad29a7edb'></a>

The coefficient _x_ in the first term of Eq. (4) reflects that the dissociation of one active DNA complex releases _x_ molecules of unbound transcription factor. The coefficient _x_ in the second term of Eq. (4) states that the creation of one active DNA complex requires up to _x_ DNA binding sites.
The number of genes within a cell is constant so adding Eqs. (3) and (5) leads to

dg/dt + ds_b/dt = 0 => g(t) + s_b(t) = g_0, (11)

<a id='22f9b200-7f87-40c6-bc35-96b290a6cecd'></a>

on using the initial conditions (10). We now assume that Eq. (5)
reaches equilibrium rapidly (quasi-steady-state approximation)
such that

$\frac{ds_b}{dt} \approx 0$, (12)

<a id='da76c4e7-c42d-4c4c-9f5c-629d389f293a'></a>

and using Eq. (11) we have

K_1 s^x (g_0 - s_b) + K_{-1} s_b \approx 0 (13)

which upon rearranging gives

s_b \approx \frac{g_0 s^x}{K_m^x + s^x} (14)

<a id='4edbef6c-d872-454e-910c-13cb7783a388'></a>

where

$\bar{K}_m = (\bar{K}_d)^{1/x} = (\bar{K}_{-1} / \bar{K}_1)^{1/x}$. (15)

Here $\bar{K}_d$ is the dissociation constant for the reaction between $\bar{S}$ and
$\bar{C}$

<a id='daa0f6e3-16ff-45dd-a28d-97e56ca2af3a'></a>

We further observe that adding Eqs. (4), (5) and (9) gives

$\frac{d}{dt}(\bar{s}+\bar{s}_b+\bar{c}_b) = (1-x)(-\bar{\kappa}_1\bar{s}_b+\bar{\kappa}_1\bar{s}^xg)$, (16)

<a id='db2175ed-7f6b-472a-afdf-b5d66a051e2a'></a>

= (1-x) d(s̅_b)/dt (17)

<a id='3b98442b-49eb-4af7-be41-e52b6d88bd0e'></a>

Under the quasi-steady state assumption of Eq. (12) together with the initial conditions (10) we find that

d/dt (s̄ + s̄₁ + c̄₁) ≈ 0, (18)

<a id='2940ffff-7195-41f4-b624-b746992d90ad'></a>

→ Œ + œ₁ + ā₁ = œ₀ (19)

<a id='d754fb97-85dc-4070-8b21-ce21cfcd80c0'></a>

Also under the approximation (12) we see that s̅_b ≈ s̅_b(0) ≈ 0. This is a valid assumption if we consider that the concentration of binding sites for a particular transcription factor on one particular gene is extremely small compared to the concentration of free transcription factor available in the cell, i.e. s̅_b < <s̅. We then obtain the following equation from (19):

s̅ + c̅_b ≈ s̅_0. (20)

<a id='e4d7150a-1fdd-4b0f-90b1-16e67b48fb5a'></a>

Finally we assume that the binding reaction between s̄ and c̄ reaches equilibrium rapidly such that

k̄₂c̄ˢ - k̄₋₂(s̄₀ - s̄) ≈ 0. (21)

<a id='69cd7c30-0a34-4451-9e88-42f07bf1277b'></a>

Rearranging this result gives

$\bar{s} = \frac{\bar{s}_0}{1+(C/K_c)^y}$ (22)

<a id='e0ee97a4-b3ec-47a0-a425-1a262f59c394'></a>

in which we define the constant _K_c such that
_K_c = (_K_s) ^(1/y) = (_K_-2/_K_2)^(1/_y),
(23)
where _K_s is the dissociation constant for the reaction between _S_
and _C_.

<a id='45fdef49-22f7-453b-b7c6-5d00e7acc034'></a>

Using Eqs. (14), (20) and (22) to eliminate Eqs. (3)-(5) and (9)
from the system equations (3)-(9) we obtain the reduced system

$$\frac{dm}{dt} = \frac{\mu_m}{1 + \left(\frac{\kappa_m(1 + (\bar{C}/\kappa_c)^y)}{\bar{s}_0}\right)^x} - \bar{\delta}_m\bar{m} = \bar{f}(\bar{m}, \bar{h}, \bar{c}), \quad (24)$$


<!-- PAGE BREAK -->

<a id='a5c84664-2168-47d3-bc58-ed04013f1115'></a>

154

<a id='8557a4b3-84cc-4a13-89c1-5eec5cffa057'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='1288ee9a-3864-4653-b8bf-48ee5a1ddae5'></a>

$\frac{dh}{dt} = \bar{\mu}_h \bar{m} - \bar{\delta}_h \bar{h} = g(\bar{m}, \bar{h}, \bar{c})$, (25)

$\frac{d\bar{c}}{dt} = \bar{\mu}_c \bar{h} - \bar{\delta}_c \bar{c} = j(\bar{m}, \bar{h}, \bar{c})$, (26)

with the initial conditions

$\bar{m}(0) = \bar{m}_0$, $\bar{h}(0) = \bar{h}_0$ and $\bar{c}(0) = \bar{c}_0$. (27)

Here $\bar{\mu}_m = \bar{\mu}_d g_0$ where $\bar{\mu}_m$ is the maximal rate of transcription.
Non-dimensionalisation: Before proceeding to a complete analysis of the model, Eqs. (24)-(26) are non-dimensionalised. Time is scaled with respect to the synthesis rate of $\bar{m}$ such that

$\tau = \bar{\mu}_h t$, (28)

where $\tau$ represents the non-dimensional time. The remaining variables are rescaled with respect to the concentration of total transcription factor, $\bar{s}_0$, such that

$m = \frac{\bar{m}}{\bar{s}_0}$, $h = \frac{\bar{h}}{\bar{s}_0}$, and $c = \frac{\bar{c}}{\bar{s}_0}$. (29)

<a id='8cd90a21-35ff-42e9-abed-f850c3bd1875'></a>

This non-dimensionalisation leads to

$\frac{dm}{d\tau} = \frac{\mu_m}{1 + (\kappa_m(1 + (c/\kappa_c))^y)^x} - \delta_m m = f(m, h, c), \quad (30)$

$\frac{dh}{d\tau} = m - \delta_h h = g(m, h, c), \quad (31)$

$\frac{dc}{d\tau} = \mu_c h - \delta_c c = j(m, h, c), \quad (32)$

with the initial conditions

<a id='7f4324de-1457-4b73-b8d5-07bc50b2105e'></a>

m_0 = \frac{\bar{m}_0}{\bar{s}_0}, h_0 = \frac{\bar{h}_0}{\bar{s}_0}, c_0 = \frac{\bar{c}_0}{\bar{s}_0} (33)
where the non-dimensional parameters are given by
\mu_m = \frac{\bar{\mu}_m}{\mu_h \bar{s}_0}, \mu_c = \frac{\bar{\mu}_c}{\mu_h}, \kappa_m = \frac{\bar{\kappa}_m}{\bar{s}_0}
\kappa_c = \frac{\bar{\kappa}_c}{\bar{s}_0}, \delta_c = \frac{\bar{\delta}_c}{\mu_h}, \delta_h = \frac{\bar{\delta}_h}{\mu_h}, \delta_m = \frac{\bar{\delta}_m}{\mu_h} (34)
The non-dimensional parameter values are summarised in Table 2.

<a id='7136c277-67ff-4e45-9f58-a8ffba42aed4'></a>

## 4. Parameter estimation

A summary of the model parameter values is provided in Table 1 with details on how each was derived from the experimental literature given in Appendix A. Wherever possible data elicited from human liver cells (Hep G2) have been used. However, it has not been possible to determine all required parameters in this manner. In some cases the model parameters do not have a direct physiological counterpart since the biological processes occurring have been simplified in the mathematical modelling to

<a id='48fb78ec-44aa-40fb-818b-0cc43b0a5d80'></a>

25) reduce complexity; in others, the parameter value is not customarily measured in the required units, not least because of the difficulty in isolating the biosynthesis pathway. In these instances
26) underlying biological principles have been used to estimate a realistic value, and to ensure that the model operates within a plausible physiologic domain.

<a id='c8bcc791-61f3-4ab3-9b7e-0e198e8eaae8'></a>

5. Model analysis

In this section and continuing in Sections 6 and 7 we discuss the existence of steady-states of Eqs (30)–(32) and their stability.

5.1. Fixed point analysis

The steady states of equations (30)–(32) are given by the solution of

$0 = \frac{\mu_m}{1+(\kappa_m(1+(c_{ss}/\kappa_c))^y)^x} - \delta_m m_{ss},$ (35)

$0 = m_{ss} - \delta_h h_{ss},$ (36)

$0 = \mu_c h_{ss} - \delta_c c_{ss},$ (37)

where $m_{ss}$, $h_{ss}$ and $c_{ss}$ are the steady state values of $m$, $h$ and $c$ respectively. Using Eqs. (36) and (37), Eq. (35) can be written as

$\alpha c_{ss} \left(1+\left(\kappa_m \left(1+\left(\frac{c_{ss}}{\kappa_c}\right)^y\right)\right)^x\right) - \mu_m = 0,$ (38)

where

$\alpha = \frac{\delta_m \delta_h \delta_c}{\mu_c}.$ (39)

<a id='30c0f56f-ce44-4928-b5f9-688f85197d76'></a>

Expanding, we find that the steady states are given by the solution of the polynomial equation of degree (xy+1),

$\frac{\beta}{\gamma^x c_{ss}^{yx+1}} + \frac{x\beta}{\gamma^{x-1} c_{ss}^{y(x-1)+1}} + \dots + \frac{x\beta}{\gamma c_{ss}^{y+1}} + (\alpha + \beta)c_{ss} - \mu_m = 0, \quad (40)$

<a id='d9ef436b-c941-4f7e-a5af-ecdbc18cae02'></a>

Table 2
Non-dimensional parameter values.
<table id="4-1">
<tr><td id="4-2" colspan="2">Parameter Description</td><td id="4-3">Nondimensional value</td></tr>
<tr><td id="4-4">με</td><td id="4-5">Cholesterol synthesis rate</td><td id="4-6">1.30</td></tr>
<tr><td id="4-7">μm</td><td id="4-8">HMGCR transcription rate</td><td id="4-9">1.90 x 10-10</td></tr>
<tr><td id="4-a">δη</td><td id="4-b">HMGCR mRNA degradation rate</td><td id="4-c">1.35 x 10-3</td></tr>
<tr><td id="4-d">δη</td><td id="4-e">HMGCR degradation rate</td><td id="4-f">1.93 x 10</td></tr>
<tr><td id="4-g">δc</td><td id="4-h">Cholesterol utilisation rate</td><td id="4-i">3.60 x 10-3</td></tr>
<tr><td id="4-j">Km</td><td id="4-k">SREBP-2-HMGCR gene dissociation constant</td><td id="4-l">1.00 x 10-4</td></tr>
<tr><td id="4-m">Kc</td><td id="4-n">SREBP-2-cholesterol dissociation constant</td><td id="4-o">1.00 x 10-3</td></tr>
</table>

<a id='3755a8ff-1dee-48e6-bbe4-86c4e66db827'></a>

Table 1
Summary of model parameter values. Details of parameter derivations are given in Appendix A.
<table id="4-p">
<tr><td id="4-q">Parameter</td><td id="4-r">Description</td><td id="4-s">Dimensional value</td></tr>
<tr><td id="4-t">m</td><td id="4-u">HMGCR transcription rate</td><td id="4-v">5.17 x 105 molecules ml s¹</td></tr>
<tr><td id="4-w">h</td><td id="4-x">HMGCR translation rate</td><td id="4-y">3.33x102</td></tr>
<tr><td id="4-z">c</td><td id="4-A">Cholesterol synthesis rate</td><td id="4-B">4.33x10s</td></tr>
<tr><td id="4-C">Om</td><td id="4-D">HMGCR mRNA degradation rate</td><td id="4-E">4.48x10</td></tr>
<tr><td id="4-F">δh (symbol)</td><td id="4-G">HMGCR degradation rate</td><td id="4-H">6.42 x 10⁻⁵ s⁻¹</td></tr>
<tr><td id="4-I">δc (symbol)</td><td id="4-J">Cholesterol utilisation rate</td><td id="4-K">1.20 x 10⁻⁴ s⁻¹</td></tr>
<tr><td id="4-L">κm (symbol)</td><td id="4-M">SREBP-2-HMGCR gene dissociation constant</td><td id="4-N">O(10¹³) molecules ml⁻¹</td></tr>
<tr><td id="4-O">κc (symbol)</td><td id="4-P">SREBP-2-Cholesterol dissociation constant</td><td id="4-Q">O(10¹⁴) molecules ml⁻¹</td></tr>
<tr><td id="4-R">X</td><td id="4-S">Molecules of SREBP-2 binding to gene</td><td id="4-T">3</td></tr>
<tr><td id="4-U">y</td><td id="4-V">Molecules of cholesterol binding to SREBP-2</td><td id="4-W">4</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='d49c6ea2-e046-48ee-901c-86c04718b567'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='a34d00bf-188c-420e-8a32-b775fdc4875f'></a>

155

<a id='77dea98d-d796-407b-8e33-1f93ac1fb199'></a>

where β = ακᵐ and γ = κᶜ. As all parameters are positive, we may apply the results of Descartes' Rule of Signs which states that the number of positive real roots of the system is either equal to the number of variations of signs in the coefficients of Eq. (40) or less than this by an even integer (Murray, 2002). As there is only one sign change in the sequence of coefficients Eq. (40), the system has only one positive real root, and therefore only one physiologically valid fixed point.

<a id='fefd7df4-e158-41a2-b236-c3cca1d7e22b'></a>

5.2. Fixed point stability

We now consider the stability of this fixed point by investiga-
tion of the eigenvalues of the linearised Jacobian matrix **J** of the
system equations (30)-(32). The Jacobian is given by

<a id='c2f4faaa-51bb-464f-97d0-185ef74f6682'></a>

J = 

[
f_m f_h f_c
g_m g_h g_c
j_m j_h j_c
] = [
-δ_m 0 -ψ
1 -δ_h 0
0 μ_c -δ_c
]
,
(41)

with

<a id='6758ff9b-377e-4507-a4f8-304abdd2fecf'></a>

\(\Psi = \frac{xy\mu_m \kappa_m^x c_{ss}^{y-1} \left(1 + \left(\frac{c_{ss}}{\kappa_c}\right)^y\right)^{x-1}}{\kappa_c^y \left(1 + \kappa_m^x \left(1 + \left(\frac{c_{ss}}{\kappa_c}\right)^y\right)\right)^2}\) (42)

<a id='3b459df8-56e1-4397-8a48-401df624620a'></a>

We note that ψ≥ 0 as all parameter values are positive and that
css ≥ 0 for physiologically valid parameter ranges.
Calculation of the eigenvalues of **J** requires the solution of the
equation
det(**J**-λ**I**) = 0, (43)

<a id='dace8bae-e0f0-442c-a369-cbf6534585d3'></a>

where $\lambda$ are the eigenvalues to be found and **I** is the identity
matrix. Evaluation of Eq. (43) leads to the characteristic equation,

<a id='efbd0ef7-6786-4700-898f-aa072c2e94ec'></a>

$\lambda^3 + (\delta_m + \delta_h + \delta_c)\lambda^2$
$+ (\delta_m\delta_h + \delta_m\delta_c + \delta_h\delta_c)\lambda$
$+ (\delta_m\delta_h\delta_c + \mu_c\Psi) = 0,$\n$(44)

<a id='8fa1d256-6e1a-405d-b5bf-3516bd91088e'></a>

which has three roots, the eigenvalues $\lambda_1$, $\lambda_2$ and $\lambda_3$. Firstly we
note that $\psi \ge 0$ ensures all coefficients of Eq. (44) are positive and
thus by Descartes' Rule of Signs there can be no purely positive
real eigenvalues. There are then two cases for the roots of (44),
either three negative real eigenvalues or one negative real eigen-
value and a pair of complex conjugate eigenvalues.

<a id='66605105-4a50-4e7b-bf0b-10f9f206eee2'></a>

The fixed point is stable if and only if the real parts of λ₁, λ₂ and
λ₃ are negative. To determine for which conditions this occurs, we
apply the Routh-Hurwitz Stability criteria to Eq. (44) (Murray,
2002). Routh-Hurwitz's criteria applied to a cubic equation of the

<a id='5208fb30-6f55-4006-a127-169725f0404b'></a>

form

$\lambda^3 + a_2\lambda^2 + a_1\lambda + a_0 = 0$

<a id='3af226c5-0fc8-4fb1-ab1b-93b5adef96fb'></a>

are satisfied if and only if $a_0 > 0$, $a_1 > 0$, $a_2 > 0$ and $a_1a_2 - a_0 > 0$.
That is, the necessary and sufficient condition for the roots of
Eq. (44) to have negative real part requires

$\delta_m + \delta_h + \delta_c > 0,$ (45)

$\delta_m\delta_h + \delta_m\delta_c + \delta_h\delta_c > 0,$ (46)

$\delta_m\delta_h\delta_c + \mu_c\psi > 0,$ (47)

$(\delta_m+\delta_h+\delta_c)(\delta_m\delta_h + \delta_m\delta_c + \delta_h\delta_c)$

$- (\delta_m\delta_h\delta_c+\mu_c\psi) = \rho(\delta_m, \delta_h, \delta_c) > 0.$ (48)

<a id='1eb18d0c-e908-47df-a7b9-1ee4aa71d38b'></a>

Since all parameters are positive and real, conditions (45)-(47)
hold. Thus the stability of the roots is dependent on condition (48).
The possible dynamic behaviour of the system can be summarised
as follows.

<a id='6969551f-8166-4327-81d3-7f02b5d2b958'></a>

Case 1: ρ(δm, δh, δc) > 0. Here all real parts of all eigenvalues are negative. In this case the steady state is stable. This stable steady state may arise in one of two ways: (i) Case Ia: where all eigenvalues are real and negative. This will result in a stable node, where the concentrations of mRNA, protein and cholesterol will tend monotonically to a steady state; and (ii) Case Ib: where one eigenvalue is real and negative and two eigenvalues are complex conjugates with negative real part. In this case the fixed point is a stable spiral and the concentrations of mRNA, protein and cholesterol will demonstrate oscillatory convergence to a steady state.

<a id='8556bfb2-6448-4ace-aec0-ac76345c6da3'></a>

Case II: ρ(δm, δh, δc) = 0. By substituting this value of (δmδhδc + μcψ) into Eq. (44), we now have the characteristic equation given by

<a id='f1451f59-59e9-4e12-aa90-b994316f4cce'></a>

λ³ + γ₁λ² + γ₂λ + γ₁γ₂ = 0,
(λ + γ₁)(λ² + γ₂) = 0,

<a id='1db61f32-becc-4880-93c9-3789392202da'></a>

where we have γ₂ = (δmδh + δmδc + δhδc) and γ₁ = (δm + δh + δc).
Therefore the characteristic equation has two conjugate roots λ₁,₂
on the imaginary axis and one negative real eigenvalue λ₃ given by

λ₁,₂ = ± i√(δmδh + δmδc + δhδc),
(49)

<a id='ece0b549-5900-4abc-9713-6206d049643e'></a>

λ₃ = −(δm + δh + δc)                                                                                                              (50)

<a id='7d756818-3401-4b8c-a25e-977a6d8665a2'></a>

one negative real eigenvalue and two pure imaginary eigenvalues.
The existence of two conjugate eigenvalues on the imaginary axis
means that the stability of the equilibrium cannot be directly
determined; this case is discussed in detail in Section 6.1.

<a id='7b36a009-a3da-4b21-a639-42f12bcb29fb'></a>

Case III: ρ(δm, δη, δc) <0. Here one eigenvalue is real and positive and two eigenvalues are complex conjugates with positive real part. In this case the steady state is unstable, implying that end product concentration would grow unboundedly. This case is biologically infeasible and hence we ignore it for the remainder of this paper.

<a id='825e9d84-46f3-4630-a4a9-36edd80e50a7'></a>

## 6. Fixed point stability – variation of μc

The eigenvalues of Eq. (44) can move between each case under the variation of system parameters. As an example we consider the effect of varying μc on the system dynamics. This parameter may be varied so that a pair of complex conjugate eigenvalues can either move into the negative real half plane (a stable focus equilibrium) or into the positive real half plane (an unstable focus equilibrium). The point where the eigenvalues cross the imaginary axis (Case II) occurs at a critical value of μc denoted by μ*c. At this point a unique, closed periodic orbit may bifurcate locally from the equilibrium as it changes stability. The isolated, closed trajectory is known as a limit cycle and causes oscillatory behaviour. This phenomenon is called a Hopf bifurcation (Guckenheimer and Holmes, 1983) and its existence dictates that the concentrations of m, h and c will oscillate.

<a id='f03e4835-ea17-4fbb-94a3-d9d0ff0e9ad7'></a>

## 6.1. Hopf bifurcation existence

According to the Hopf bifurcation theorem (Guckenheimer and Holmes, 1983), a bifurcation occurs for a critical value μc = μ*c, for which the following two conditions are fulfilled, at the equilibrium point (mss, hss, Css):

<a id='768f01c7-783b-41e5-9af8-a17440c4783a'></a>

1. The matrix **J** has two complex eigenvalues

$\lambda_{2,3} = \theta(\mu_c) \pm i\omega(\mu_c),$ 

<!-- PAGE BREAK -->

<a id='efebbfe9-df58-4c6d-8617-2fb0112c154b'></a>

156

<a id='5544200b-cd68-43e6-bc07-0dc14be6e30f'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150–162

<a id='8a16809d-c44d-4cde-927b-4d4d7b78c6b1'></a>

in some neighbourhood of μ_c^* and for μ_c = μ_c^* these eigenvalues
are purely imaginary, that is,
θ(μ_c^*) = 0 and ω(μ_c^*) ≠ 0.

<a id='ec5858cf-0329-4a5f-8a3a-cdc53872d97f'></a>

This non-hyperbolicity condition is a necessary condition for
the Hopf bifurcation.

2. The relation described by

$\frac{d\theta(\mu_c)}{d\mu_c} \Big|_{\mu_c = \mu_c^*} \neq 0,$

<a id='b4cc719f-9651-486e-970f-37f70a4bb0f5'></a>

holds in some neighbourhood of µ*c. This is a sufficient condi-
tion for the Hopf bifurcation and is also known as the
transversality or Hopf crossing condition. It ensures that the
eigenvalues cross the imaginary axis with non-zero speed and
thus ensures that the crossing of the complex conjugate pair at
the imaginary axis is not tangent to the imaginary axis. If this is
not the case we may observe, for example, the occurrence in
which the eigenvalues move up to the imaginary axis and then
reverse direction without crossing.

<a id='6a45f086-3fa0-4dc8-a9f2-21b002b32013'></a>

We notice that the first condition has already been shown to hold at the critical value c*, given by the solution of

<a id='4ce8ff2e-bc38-4371-b7dc-d1afd700fbb2'></a>

$$\mu_c^* = \frac{((\delta_m + \delta_h + \delta_c)(\delta_m\delta_h + \delta_m\delta_c + \delta_h\delta_c) - \delta_m\delta_h\delta_c)}{\Psi},$$

<a id='1ceff606-cd5c-40eb-950d-fe5ce8cda58a'></a>

where \(\psi\) is given by Eq. (42), together with the equation determin-
ing the equilibrium value of \(c_{ss}\) for \(\mu_c^*\):

$$\frac{(c_{ss})^{yx+1}}{(\kappa_c)^x} + x^\frac{(c_{ss})^{y(x-1)+1}}{(\kappa_c)^{x-1}} + \cdots + x^\frac{(c_{ss})^{y+1}}{(\kappa_c)^y}$$ 

$$+ \left(\frac{1}{\kappa_m^x}+1\right)c_{ss} - \left(\frac{\mu_m}{\kappa_m^x\delta_m\delta_h\delta_c}\right)\mu_c^* = 0.$$

<a id='7cacd462-ef06-4865-bfd3-8bc6ece257dd'></a>

From the results of Case II we know that at this value of μ* the characteristic polynomial Eq. (44) has two purely imaginary roots ± iω(μ*), given in Eqs. (49) and (50), where

<a id='6d8693da-876b-4e07-8379-6b79bb6ad37e'></a>

$\omega(\mu_c^*) = \sqrt{(\delta_m \delta_h + \delta_m \delta_c + \delta_h \delta_c)} \neq 0.$ (51)

<a id='36177a26-2ac0-4090-9491-92a9d8386a9c'></a>

To show that the second condition holds we use the Implicit
Function Theorem. For each \u00b5c \u2208 \u211d and the corresponding system,
Eqs. (30)-(32), define

<a id='0241ebcb-915c-4320-85e9-82a986aee510'></a>

k(μc, λ) = p(λ),

<a id='6d7fdc32-c327-446b-af76-4d108614b127'></a>

as a function of two variables μ_c and λ, where p(λ) is the characteristic polynomial of the system equations (30)–(32) defined by Eq. (44).

<a id='5c59e65d-c82a-49b4-84f1-672908f7c1eb'></a>

Let the complex eigenvalues \lambda(\mu_c) = \theta(\mu_c) \pm i\omega(\mu_c) be the roots of the characteristic polynomial. Hence, for these eigenvalues we have

<a id='dae69d14-d1bf-46d6-962e-9a53fe6fed17'></a>

k(μ_c, λ(μ_c)) = 0,                                                                  (52)

<a id='11562a84-8ed5-4c39-8feb-2fe5d09b3c44'></a>

where this represents an implicit function of two variables μc and λ. The Implicit Function Theorem tells us that we may define μc as a function of λ near the point (μc*, λ(μc*)), and the derivative of this function is given by

<a id='022bef39-8f12-40db-b8ae-38967fe1daad'></a>

$$\frac{d\lambda}{d\mu_c}\Big|_{\mu_c = \mu_c^*} = - \left( \frac{\partial \mathbf{k}}{\partial \mu_c} \middle/ \frac{\partial \mathbf{k}}{\partial \lambda} \right)\Big|_{\mu_c = \mu_c^*}, \quad (53)$$

<a id='7dd921e5-7e66-4bb0-80b8-cc2970fca7e8'></a>

providing
∂k
--- ≠ 0.
∂λ

<a id='12d41289-ead8-4f9e-98bd-7243bab56e7d'></a>

We begin by computing the derivative of the function k($\mu_c$, $\lambda(\mu_c)$) with respect to $\lambda$, and evaluating this at the critical

<a id='e9bc5727-a9df-49aa-92eb-ed2bb9dc1649'></a>

point $\mu_c^*$. Thus we have,

<a id='8612ca97-7f41-408c-ab19-1e29efc195bc'></a>

<::
∂k/∂λ (μc, λ) |(μc,λ) = (μc*, ± iω(μc*))
= 3λ² + 2(δm + δh + δc)λ
+ (δmδh + δmδc + δhδc) |(μc,λ) = (μc*, ± iω(μc*))
= 3(± iω(μc*))² + 2(δm + δh + δc)(± iω(μc*))
+ (δmδh + δmδc + δhδc).
: figure::>

<a id='7695deaf-068d-4955-89d4-ff845f0d8724'></a>

Simplifying in conjunction with the fact that ω²(μ*c) = (δmδh + δmδc + δhδc) from Eq. (51), we obtain

∂k/∂λ = -2ω²(μ*c) ± 2i(δm + δh + δc)ω(μ*c) ≠ 0. (54)

<a id='d944a290-fc27-4c27-a7f3-5ba7bb18b8a0'></a>

Furthermore, from the characteristic polynomial Eq. (44), we
have

<a id='3d41f956-1cc8-4c58-9210-e521063e2a60'></a>

$$\frac{\partial \mathbf{k}}{\partial \mu_c} (\mu_c, \lambda) \Bigg|_{(\mu_c, \lambda) = (\mu_c^*, \pm i\omega(\mu_c^*))} = \Psi, \quad (55)$$

<a id='236d619d-c252-427f-a6bd-077d3b571fed'></a>

where, we have previously noted that \\( \\psi \\ge 0 \\). However, in the case \\( \\psi=0 \\), the Jacobian matrix becomes

\\( J=\begin{bmatrix} -\delta_m & 0 & 0 \\ 1 & -\delta_h & 0 \\ 0 & \\mu_c & -\delta_c \end{bmatrix} \\)

<a id='90eb409f-ab49-4ebc-93b0-8ba171c950c5'></a>

which is lower triangular and hence has three negative real
eigenvalues given by the entries of the leading diagonal, specifi-
cally −δm, −δh and −δc. This violates the requirement of condi-
tion 1 that the matrix **J** has two complex eigenvalues. Therefore we
can conclude that in the case of a Hopf bifurcation, ψ ≠ 0 and we
need only be concerned with the strict inequality ψ > 0.
Eqs. (54) and (55) together with Eq. (53) yield

<a id='ec6af7cf-fc6e-4e94-bd6a-bfae32b2107c'></a>

$$\frac{d\lambda}{d\mu}(\mu_c^*) = \frac{1}{2\omega(\mu_c^*)} \left( \frac{\psi}{-\omega(\mu_c^*) \pm i(1+\delta_h+\delta_c)} \right). $$

<a id='d5f84e3e-1855-4bd2-8b00-40f3f210e28e'></a>

Upon the rationalisation of the denominator of this complex fraction we obtain

$$\frac{d\lambda}{d\mu_c^*} = \frac{1}{2\omega(\mu_c^*)} \left( \frac{-\omega(\mu_c^*)\psi}{\omega^2(\mu_c^*) + (\delta_m + \delta_h + \delta_c)^2} \right)
+ \frac{i}{2\omega(\mu_c^*)} \left( \frac{\mp \psi(\delta_m + \delta_h + \delta_c)}{\omega^2(\mu_c^*) + (\delta_m + \delta_h + \delta_c)^2} \right)$$

<a id='a8e3c9d6-bee9-4b0c-bb4e-9b9a18c17341'></a>

and since ψ > 0,

$\frac{d\theta(\mu_c)}{d\mu_c}\Big|_{\mu_c = \mu_c^*} = \text{Re}\left(\frac{d\lambda}{d\mu_c}(\mu_c^*)\right)$

$= \frac{1}{2}\left(\frac{-\psi}{\omega^2(\mu_c^*) + (\delta_m + \delta_h + \delta_c)^2}\right) < 0$

<a id='1ab19aa5-0e02-4824-99cd-c1709f4652de'></a>

and the second condition of the Hopf theorem is fulfilled. Thus we
have proved the existence of a Hopf bifurcation at the critical value
μc = μc*.

<a id='07e88139-f049-4478-a7f4-422658f1ba47'></a>

6.2. Hopf bifurcation stability

Just as the steady states of a system may be stable or unstable, the limit cycle which branches from the fixed point in a Hopf bifurcation may also be stable or unstable. A stable limit cycle occurs if the Hopf bifurcation is supercritical whereas an unstable limit cycle is the product of a subcritical bifurcation.

<a id='cab903f5-233a-4984-b760-82239de4317a'></a>

At a subcritical bifurcation a unique and unstable limit cycle,
which exists for μc < μc*, is absorbed by a stable spiral equilibrium.
The equilibrium becomes unstable for μc > μc*; in this case diver-
ging oscillations and therefore unbounded growth in the evolution

<!-- PAGE BREAK -->

<a id='53ad2709-6771-41ba-85e9-f1b12c01e2b0'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150–162

<a id='566e6587-eea3-4ade-bc08-9cf0fd1fbb6f'></a>

157

<a id='9dce17be-1d13-40b7-9361-ea0cf8fc6d80'></a>

of variables is seen. In a supercritical bifurcation the equilibrium point prior to the Hopf bifurcation is a stable spiral, and concen-trations of mRNA, protein and cholesterol display oscillatory decay before reaching a steady state value. At the bifurcation point $\mu_c = \mu_c^\times$, a limit cycle is born. At this point the equilibrium changes stability and becomes unstable. For $\mu_c > \mu_c^\times$, this becomes a unique and stable small amplitude limit cycle; here the concentrations of mRNA, protein and cholesterol exhibit stable oscillations.

<a id='ba77ac90-f408-436a-82dd-a6d223d6007d'></a>

As the limit cycle is stable, any small perturbation from the closed trajectory causes the system to return to the limit cycle resulting in self sustained oscillations in concentrations of mRNA, protein and cholesterol within the region of some equilibrium value. Thus, as the occurrence of a supercritical Hopf bifurcation will result in behaviour which is analogous to the physiological process of homeostasis, it is necessary to determine the stability of the Hopf bifurcation. This analysis was undertaken as follows.

<a id='41d36ba1-f5a5-4e11-8e5e-aa5f66514664'></a>

Numerical solutions to Eqs. (30)-(32) were obtained using
MATLAB (MATLAB, 8.0.0.783, The MathWorks Inc., Natick, MA,
2012) and the characteristics of system bifurcations and limit
cycles were explored using the MATLAB numerical continuation
toolbox Matcont (Dhooge et al., 2003). The basic principle of this
toolbox is to consider a system of ODEs

<a id='972bec7e-488e-4404-a98b-5cf323c4f09f'></a>

$$\frac{d\mathbf{x}}{dt} = f(\mathbf{x}, \mu) \quad \mathbf{x} \in \mathbb{R}^n, \mu \in \mathbb{R}^1 \qquad (56)$$

<a id='8000a266-ee56-4ef9-90a0-3002f0c48497'></a>

with an equilibrium point at ($x_0$, $\mu_0$). The principle of numerical continuation requires finding a solution curve $\sigma$ of $f(x_0, \mu_0) = 0$ with $\sigma(0) = (x_0, \mu_0)$ which describes how the equilibrium point varies. The curve $\sigma$ is traced by means of a predictor-corrector algorithm and bifurcations along $\sigma$ are detected using a suitable test function which changes sign at the bifurcation point.

<a id='3484b77c-4e02-44fa-a5a9-24c5e0c087a7'></a>

Once the Hopf bifurcation has been detected, Matcont calculates the stability of the subsequent limit cycle by calculating the first Lyapunov coefficient or Lyapunov characteristic exponent, l_1(0), of the dynamical system near the bifurcation point. This coefficient describes the average rate at which neighbouring trajectories in the phase space converge or diverge. Specifically,

* l_1(0) < 0 implies that the system is attracted to a stable periodic orbit and
* l_1(0) > 0 implies that the system is attracted to an unstable periodic orbit.

<a id='bf96e32e-4fe7-4b8c-a964-2ccc25f25f20'></a>

In the case of Eqs. (30)-(32) with μ₊ as the bifurcation parameter,
we find that a Hopf bifurcation is predicted to occur at the point
(μ₊, c*)=(1.809, 0.011), whose values are the solution of the
simultaneous equations (40) and (48). This bifurcation has a
negative first Lyapunov coefficient which indicates that a stable
limit cycle is produced and the bifurcation is supercritical.

<a id='a7d2303d-3ae1-4afa-8331-641933551041'></a>

The results of the Hopf bifurcation existence and stability analysis of the governing system of Eqs. (30)–(32) can now be discussed in the context of cellular cholesterol homeostasis. Homeostasis is the tendency of a system to regulate its internal environment by maintaining a stable condition. All homeostatic mechanisms use feedback inhibition to facilitate a constant level. Essentially this involves controlling the concentration of a particular variable within a narrow range in the region of an optimal value. If this concentration alters, the feedback inhibition pathway automatically initiates a corrective mechanism which reverses this change and brings it back towards an equilibrium. In a system controlled by feedback inhibition, the equilibrium is never perfectly maintained, but constantly oscillates about an optimal level. Thus the existence of the Hopf bifurcation and the consequent appearance of small amplitude oscillations in the concentrations

<a id='5d1bdd0a-dbd9-42d2-a3d8-45f1b16f68c5'></a>

of mRNA, protein and cholesterol, are significant in its similarity to the behaviour of a homeostatic system.

<a id='ca8cf2b1-57d3-4e08-882c-431969b18b7f'></a>

## 6.3. Illustration of system behaviour

In this section we present numerical solutions to Eqs. (30)-(32) using the MATLAB stiff differential equation solver ODE15s (MATLAB, 8.0.0.783, The MathWorks Inc., Natick, MA, 2012) for various values of μc to illustrate the system behaviour elucidated in the previous sections. All remaining parameters were held constant as detailed in Table 1. The parameter μc was varied between 1.53 x 10-2 s-1 and 6.46 x 10-2 s-1 (physiologically valid limits) to demonstrate the variation of system behaviour through Cases I to II.

<a id='d5886fa2-7940-4d3a-96ac-b0bac688fa18'></a>

Simulation of Eqs. (30)–(32) starting with the initial value of 1.53 x 10^-2 s^-1 shows monotonic non-oscillatory convergence to a steady state, equivalent to Case Ia as illustrated in Fig. 3. Continually increasing μc shows the system shifting to Case Ib. Thus we see oscillatory convergence to a steady-state as shown in Fig. 4. Still further increases in μc see the system reaching Case II, where we have pure oscillations in mRNA, HMGCR and choles- terol; this is illustrated in Fig. 5. The Hopf bifurcation occurs at the transition from Case Ib to Case II.

<a id='92b6d0ff-532d-4186-9b2a-65036c8b61fb'></a>

<::chart: The chart shows the nondimensional concentration of HMGCR, Cholesterol, and mRNA over nondimensional time. The x-axis is "Nondimensional Time" ranging from 0 to 10000. There are two y-axes. The left y-axis is "Nondimensional Concentration (HMGCR and Chol)" ranging from 0 to 0.08. The right y-axis is "Nondimensional Concentration (mRNA)" ranging from 0 to 2 x 10^-7. The legend indicates three lines: HMGCR (light blue line with square markers), Cholesterol (dark blue line with star markers), and mRNA (orange line with circle markers). The HMGCR concentration starts around 0.01, increases to about 0.07, and then stabilizes. The Cholesterol concentration starts around 0.015, decreases to near 0, and then slowly increases to about 0.005. The mRNA concentration starts around 1.5 x 10^-7, decreases to about 0.5 x 10^-7, then increases to about 1.2 x 10^-7, and stabilizes. Fig. 3. Stable node equilibrium (corresponding to Case Ia) where there are three negative real eigenvalues; variable concentrations exhibit monotonic convergence towards a steady state value. All parameters are as in Table 2 except nondimensional μc=0.462. Nondimensional initial conditions: m(0)=3.65 x 10⁻⁸, h(0)= 1.10 x 10⁻⁵ and c(0)=2.30 x 10⁻². Note that the evolution of HMGCR has been rescaled to allow for easier comparison.::>

<a id='24c59eb9-3fce-4eec-9f27-505c2b7b234e'></a>

<::line chart: The chart displays Nondimensional Concentration over Nondimensional Time. The x-axis is "Nondimensional Time" ranging from 0 to 2.5 x 10^4. There are two y-axes. The left y-axis is "Nondimensional Concentration (HMGCR and Chol)" ranging from 0 to 0.05. The right y-axis is "Nondimensional Concentration (mRNA)" ranging from 2 x 10^-8 to 12 x 10^-8. Three lines are plotted: 1. HMGCR (light blue line with squares), which starts low, peaks around 0.05, oscillates, and then converges to a steady state around 0.038 on the left y-axis. 2. Cholesterol (dark blue line with asterisks), which starts low, peaks around 0.01, oscillates, and then converges to a steady state around 0.01 on the left y-axis. 3. mRNA (red line with circles), which starts low, peaks around 0.05 (on the left y-axis scale), oscillates, and then converges to a steady state around 0.032 (on the left y-axis scale) or 8 x 10^-8 (on the right y-axis scale). The legend indicates the lines represent HMGCR, Cholesterol, and mRNA. Fig. 4. Stable spiral equilibrium (corresponding to Case Ib) where there is one negative real eigenvalue and a pair of complex conjugate eigenvalues with negative real part; variable concentrations exhibit oscillatory convergence towards a steady state value. Initial conditions are as in Fig. 3. All parameters are as in Table 2 except for μc which has been increased 2 fold to μc=0.923.::>

<!-- PAGE BREAK -->

<a id='69108f1c-04f1-47fb-882d-b9256a3a632b'></a>

158

<a id='0b453433-701b-4905-b96b-50a801792864'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='097a6bc7-f691-4cc3-ac8c-5c812aba9c19'></a>

<::chart: line chart showing the time evolution of HMGCR, Cholesterol, and mRNA concentrations. The x-axis is labeled "Nondimensional Time" and ranges from 0 to 3.5 x 10^4. The left y-axis is labeled "Nondimensional Concentration (HMGCR and Chol)" and ranges from 0 to 0.04. The right y-axis is labeled "Nondimensional Concentration (mRNA)" and ranges from 0 to 1 x 10^-7. Three lines are plotted: HMGCR (cyan squares), Cholesterol (dark blue stars), and mRNA (red circles). All three concentrations exhibit stable oscillatory behavior over time.Fig. 5. Following the occurrence of a Hopf bifurcation the (now unstable) equilibrium is attracted to a stable limit cycle. Variable concentrations exhibit purely oscillatory behaviour; the oscillations are stable. Initial conditions are as in Fig. 3. All parameters are as in Table 2 except for µc which has been increased approximately 4 fold to µc = 1.946.::>

<a id='18096750-1f2f-4787-83fd-1d50479a2363'></a>

Following the bifurcation, the evolution of the concentrations of mRNA, HMGCR and cholesterol are purely periodic, with small amplitude stable oscillations. The period of the oscillations in Fig. 5 is approximately 16.9 h; further numerical investigations have revealed that on manipulation of system parameters, the oscillatory period can vary between approximately 12 and 24 h.

<a id='272a17c1-da5e-4608-b4b4-9285156c4bc5'></a>

We also find that after μc has passed through its critical Hopf bifurcation value, no further changes in dynamical behaviour occur. That is, once the system becomes oscillatory, it remains in this manner for all μc > μc*.

<a id='0c900fd3-1efc-465a-9ded-b82748ed7b91'></a>

7. Remaining parameter analysis and system behaviour

Further numerical investigation of the governing system of equations has shown that each of the system parameters, if varied whilst all other parameters are kept constant, are capable of inducing a Hopf bifurcation. In the case of synthesis rates, µm and µc, only one Hopf bifurcation occurs and is supercritical. Any oscillatory behaviour the system demonstrates is always stable and these oscillations persist for any parameter value greater than its critical bifurcation value.

<a id='8682378c-cf29-429a-885c-39637505e3f0'></a>

We note, however, that if either the degradation rates,
($\\delta_m$, $\\delta_h$, $\\delta_c$), or binding affinities ($k_m$, $k_c$), are taken to be bifurcation
parameters, qualitatively different behaviour from the case dis-
cussed above is seen. Calculation of the critical values for these
parameters indicates that there are two physiologically valid
points where a Hopf bifurcation may occur.

<a id='e1ccfbd8-0e87-449d-9dd3-69b3f676267a'></a>

Examining the case of δc we see that the critical value δc* for which a Hopf bifurcation may occur is given by the solution of the equation

<a id='64c3dd41-5431-4fbb-983c-ca9e18a50793'></a>

(δm + δh)(δc*) + (δm + δh) δc*
+ (δm δh + δm δh - μc ψ) = 0,
(57)

<a id='2e66f98f-13dc-4889-8982-66247508c6a7'></a>

which is quadratic in ̑̂\* and hence, for the case of two positive real
roots, gives rise to the possibility that there are two Hopf
bifurcation points associated with this parameter. This result in
turn affects the steady-states of Cₙₙ which are determined from

<a id='4f4e5163-3fd3-45e9-b5c2-7145a9de3d8c'></a>

\delta^*_c \frac{(c_{ss})^{yx+1}}{(\kappa^y_c)^x} + x\delta^*_c \frac{(c_{ss})^{y(x-1)+1}}{(\kappa^y_c)^{x-1}} + \dots + x\delta^*_c \frac{(c_{ss})^{y+1}}{(\kappa^y_c)} \\ + \left(\frac{\delta^*_c}{\kappa^x_m} + \delta^*_c\right) c_{ss} - \left(\frac{\mu_m\mu_c}{\kappa^x_m\delta_m\delta_h}\right) \mu^*_c = 0.

<a id='b0fc2d54-017f-46a6-9277-2b000cdf3ac0'></a>

<::chart: line::>Nondimensional Concentration (x 10⁻⁷) vs Nondimensional Time (x 10⁴) line chart.The x-axis, labeled "Nondimensional Time", ranges from 0 to 7 (x 10⁴).The y-axis, labeled "Nondimensional Concentration", ranges from 0 to 1 (x 10⁻⁷).There are three lines plotted:
- Red line with circles: Starts around 0.9, quickly drops and oscillates, then stabilizes around 0.55. This corresponds to δc = 3.5 x 10⁻³.
- Blue line: Starts around 0.5, oscillates with decreasing amplitude, then settles into a stable oscillation between approximately 0.25 and 0.5. This corresponds to δc = 2.5 x 10⁻³.
- Cyan line with squares: Starts around 0.2, quickly drops and oscillates with decreasing amplitude, then stabilizes around 0.08. This corresponds to δc = 3.5 x 10⁻⁴.

Fig. 6. The response of mRNA concentration to variation of δc. A clearly demarcated region of purely stable oscillatory behaviour is visible between stable steady state solutions. All parameters are as in Table 2 except for δc which is successively varied with nondimensional values as indicated. Initial conditions are as in Fig. 3.<::>

<a id='e09bdf48-a18b-4fcc-a6a7-84970247f20c'></a>

The eigenvalues at this critical point are given by

$\lambda_{1,2} = \pm i\sqrt{(\delta_h + \delta_c + \delta_h\delta_c^*)}$ (58)

$\lambda_3 = -(1 + \delta_h + \delta_c^*)$ (59)

and so the first Hopf bifurcation condition holds. Proceeding in the manner of the calculation for $\mu_c^*$, we find

$\frac{d\theta(\delta_c)}{d\delta_c}\bigg|_{\delta_c = \delta_c^*} = \text{Re}\frac{d\lambda}{d\delta_c}(\delta_c^*)$

$= \frac{\omega^2(\delta_c^*) + (1 + \delta_h)(1 + \delta_h + \delta_c^*) - \delta_h}{2(\omega^2(\delta_c^*) + (1 + \delta_h + \delta_c^*)^2)} > 0$ (60)

and therefore the second condition of the Hopf theorem also holds.

<a id='8dc98cfa-4588-419f-ab5d-1350e648df6e'></a>

Here, the unique equilibrium value undergoes two Hopf bifur-
cation points. Before the first of these points, the equilibrium is a
stable spiral. At the first bifurcation point a supercritical Hopf
bifurcation leads to the appearance of a stable periodic orbit (as
the eigenvalues of the system cross the imaginary axis from left to
right). The amplitude of this limit cycle increases initially as δc
increases whilst later decreasing until the second bifurcation point
where the limit cycle disappears (as the eigenvalues of the system
cross the imaginary axis from right to left) and the equilibrium
point becomes stable again. Numerical analysis demonstrates a
negative first Lyapunov coefficient for Hopf bifurcations confirm-
ing their supercriticality. For any value of δc falling between the
two bifurcation values purely oscillatory behaviour is generated,
whilst outside this region only stable non-oscillatory solutions
exist as illustrated in Fig. 6.

<a id='0bcd341d-db31-4377-88c5-147f42b68511'></a>

## 8. Discussion

We have formulated and solved a deterministic ODE model of cholesterol biosynthetic regulation by SREBP-2 in a hepatocyte. The model predicts the existence of oscillatory behaviour within the system which we believe is important in understanding cholesterol homeostasis. In the HMGCR system, such a mechanism means that perturbations may be made to certain system variables without losing the required concentration within which cholesterol is allowed to vary to guard against cytotoxicity. Other advantages to this dynamic mechanism include limiting the time during which cholesterol concentration is necessarily elevated

<!-- PAGE BREAK -->

<a id='a02f404b-6bdc-4236-94ff-254b13011e0e'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150–162

<a id='a72d0d72-23ed-45ab-8b79-805312aa2385'></a>

159

<a id='de0fd52c-85a5-41ef-a5cd-fe7aeeb4969a'></a>

within the cell in response to increased demand. Furthermore,
controlling cellular cholesterol levels in this manner may incur less
demand on cellular energy supplies than sustained elevation.
Dynamic oscillatory steady-state behaviour allows the system to
vary between upper and lower bounds consistent with an oscilla-
tory homeostatic mechanism (Ghosh and Chance, 1964; Waxman
et al., 1966).

<a id='e7833d2c-5abe-47f0-8bf8-29125d8529f5'></a>

Following the work of Goodwin (1965) and Griffith (1968)
negative feedback regulation of mRNA levels, which are modu-
lated by end product concentration, are often modelled using a
Hill type function such that the

<a id='5d937c73-5b70-486d-a43b-3ac3cac91c67'></a>

dm/dt = μ / (K^n + b^n) - αm,

<a id='19650565-c496-4a1e-b3b5-20b2ea3ec037'></a>

where m = m(t) is the mRNA concentration, b = b(t) is the con-
centration of the end product, μ is the rate of mRNA transcription,
K is the Hill constant, n is the Hill coefficient and α is the rate of
mRNA degradation. Goodwin (1965) and Griffith (1968) showed
that such a system will exhibit oscillations should n ≥ 8. Values of
n greater than approximately 4 are, however, deemed biologically
implausible. In comparison, our mathematical model formulation
has explicitly accounted for the interaction between not only the
transcriber (in this case SREBP-2), but the negative regulation of
the transcriber by the end product (cholesterol). The form of Eq.
(24) accurately accounts for these interactions and allows biologi-
cally realistic values for them to be included in the model
formulation whilst accurately accounting for the system dynamics.

<a id='29d283c5-64ea-4ebc-9148-9b04b2a4b681'></a>

Whilst our mathematical model has been formulated in the context of cholesterol biosynthesis this specific process of transcription factor regulated gene expression could be applicable to other pathways regulated by SREBP-2, in addition to the modulation of other lipid regulating proteins by the SREBP-1a and SREBP-1c isoforms. Further experimental research is necessary to evaluate these mathematical results and to clarify the system behaviour. However, this model and its analysis may serve as a basis for the investigation of transcription factor mediated gene expression dynamics, and furthermore constitute an important component of the synthetic engineering of biological circuits (Zhang and Jiang, 2010).

<a id='d539a4db-1237-4fae-b8ef-4deb94f7df29'></a>

## Acknowledgments

BSB acknowledges the support of a Biotechnology and Biological Sciences Research Council (BBSRC) UK CASE studentship in collaboration with Unilever Research. MJT is grateful for the support of a Research Council UK Fellowship during the period in which this work was undertaken.

<a id='f2f0d47e-c44c-4eb5-90dc-2b55f9af5cb3'></a>

# Appendix A. Parameter derivation and estimation

## *A.1. Determination of synthesis parameters*

Information on the rates of transcription and translation are rarely quantified in terms of mass per unit time, instead these rates are often measured relative to a control process. Therefore in order to estimate practical values for these parameters, we consider the relevant biological mechanisms.

<a id='e9df90be-85dc-4031-83ab-ced01d3ef2f5'></a>

A.1.1. *Rate of HMGCR mRNA transcription – \overline{\mu}_{m}*

In order to produce an estimate for the transcription rate the assumption that any time delays involved in the initiation of transcription and promoter clearance are negligible, is made. It is also assumed that no abortive transcripts are produced. Liver cells are somatic and therefore the majority are diploid, meaning they

<a id='ef19be03-e89e-4470-9253-be14fee2ffb9'></a>

contain two chromosomes and thus normal amounts of DNA.
Ignoring the existence of both tetraploidy and double nuclei that
can be present within some liver cells, we assume all liver cells to
be diploid.

<a id='d9c65f7f-a303-4935-940e-2b905f3f076d'></a>

We estimate the rate of transcription in terms of nucleotides per unit time in a typical mammalian gene. It is possible for a cell to transcribe 14,000 base pairs in 20 min giving a rate of 12 bases per second (Darzacq et al., 2007). This value is used to provide a rough estimate of the rate of transcription, equivalent to the number of mRNA molecules produced per cell per unit time.

<a id='94501d00-d63d-4bf2-bf4e-cce75ae953ae'></a>

The human HMG-CoA reductase gene is 24,826 bases long (Goldstein and Brown, 1984). To transcribe one molecule of primary HMG-CoA reductase mRNA, from one gene, assuming a rate of 12 bases per second, takes 2068.83 s. We then take into account that the post transcriptional processing steps of mRNA cleavage, 5' capping and polyadenylation are rate limiting. A delay of approximately 30 min has been added to account for this. Therefore an approximation of the time it takes to transcribe one molecule of primary HMG-CoA reductase mRNA from one gene is 3868.83 s. Per gene, this equates to

<a id='51838d81-f924-4127-9dec-cf9811dc7975'></a>

2.59 × 10⁻⁴ molecules HMGCR mRNA s⁻¹. (A.1)

<a id='7b9e1d6f-e816-4ea5-bbf1-8274b34bd224'></a>

Therefore one gene can synthesise 2.59 × 10⁻⁴ molecules of HMG-CoA reductase mRNA per second. Taking diploidy into account there are 5.17 × 10⁻⁴ molecules HMG-CoA reductase mRNA being synthesised per cell per second.
Given an average cell volume of 1pl (1 × 10⁻¹² l = 1 × 10⁻⁹ ml),
the required approximate rate of HMGCR transcription is given by

<a id='5d44fbdf-9d2c-40ad-9770-db1e45374d74'></a>

μm = 5.17 × 10^-4 molecules s^-1 / 1 × 10^-9 ml
= 5.17 × 10^5 molecules ml^-1 s^-1.
(A.2)

<a id='aff602ee-5219-4b05-ab44-a1858f7b963e'></a>

A.1.2. Rate of HMGCR protein translation – µh
To calculate an estimate of the rate of translation the following assumptions are made. Firstly, any effects caused by the transport of mRNA from the nucleus to its localisation in the cytoplasm are ignored. Also ignored are the effects of protein folding on transcriptional regulation as well as biochemical interactions amongst proteins. Finally any time delays in the elongation phase of protein synthesis are considered to be negligible.

<a id='c3a410ee-434c-4c26-9e15-b7b36a912313'></a>

The _in vivo_ estimate from Slobin (1991) suggests that the translation rate for eukaryotic cells is 6 amino acids per second, where one amino acid is encoded by 3 nucleotides or bases. Many ribosomes can translate the same mRNA molecule simultaneously (Granner and Weil, 2006). Because of their large size, ribosomes cannot attach to mRNA any closer than 35 nucleotides apart. This detail allows estimation of the rate of transcription, equivalent to proteins synthesised per unit time from mRNA.

<a id='fb913321-37a0-46fa-8ef1-ee4d63bab3f5'></a>

A human HMG-CoA reductase mRNA transcript contains 4475
bases (Goldstein and Brown, 1984). For one ribosome to transcribe
one molecule of HMG-CoA reductase protein, from one HMG-CoA
reductase mRNA, assuming a translation rate of 6 amino acids
per second, where three bases code for one amino acid, takes

<a id='bd8a5b4d-77bd-4d9d-89e6-3fe27753e636'></a>

4475 amino acids
-----------------
18 amino acids/s = 248.61 s.

(A.3)

<a id='83a036eb-2acd-4c8a-8de0-7abd160fe468'></a>

Taking into account that the rate limiting step in translation is the initiation of the process itself, a delay of approximately 60 min is added. This gives the approximation that each ribosome takes 3848.61 s to translate one molecule of HMG-CoA reductase from HMG-CoA reductase mRNA. Then per ribosome, this equates to

<a id='2aab0c50-f7a9-407e-89e6-b1d1126d3443'></a>

1 molecule / 3848.61 s = 2.598 × 10⁻⁴ molecules s⁻¹. (A.4)

<!-- PAGE BREAK -->

<a id='1191b84c-5449-4197-b968-4d918c5c0681'></a>

160

<a id='53c1ee7e-c243-4ce1-9aaa-95b6a7ec47c7'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='8be94d1d-3601-4257-bf09-347d3ab3e50c'></a>

Thus, 2.598 x 10-4 molecules of HMG-CoA reductase protein may be synthesised per second per ribosome.
  Given that the coding region of the HMG-CoA reductase mRNA is 4475 nucleotides long and a ribosome can attach every 35 nucleotides, 127.85 ribosomes can attach per mRNA molecule.
  Therefore, per HMG-CoA reductase mRNA molecule,

<a id='0d1a3e77-46c8-4eb3-bec3-611388adf17a'></a>

2.598 × 10⁻⁴ molecules s⁻¹ ribosome⁻¹
× 127.85 ribosomes
= 3.32 × 10⁻² molecules s⁻¹,
(A.5)

<a id='723d8141-0ff2-4f82-be43-ba2ddd12cd07'></a>

that is, there are 3.32 x 10-2 molecules of HMG-CoA reductase protein being synthesised per second. We thus take

<a id='f8cf2e93-bec6-4e7c-9b61-62fc9565d855'></a>

\overline{\mu}_h = 3.32 \times 10^{-2} \text{ s}^{-1}

<a id='7de5fffa-b277-48f5-b8e9-f11747487500'></a>

as an approximation of the rate of HMGR translation.

<a id='28cbdc68-f88d-4121-a358-2f48f0c3d0ed'></a>

A.1.3. HMGCR activity – µ̄c
The value of 52 pmol mevalonate formed per minute per mg protein for HMGCR activity in human liver microsomes is taken directly from Tanaka et al. (1982). This must now be converted into a turnover number for HMGCR which is the maximum number of substrate molecules that an enzyme can convert to product per mole of catalytic site of the enzyme per unit time. The activity of an enzyme is the moles of substrate converted per unit time and is a measure of the quantity of active enzyme present. The specific activity is the activity of an enzyme per mg of total protein, i.e. a measure of enzyme efficiency.

<a id='66aad870-3e45-4794-a914-72892fac946e'></a>

HMG-CoA reductase is a tetrameric protein, composed of monomers arranged in two dimers. Each dimer has two active sites (Istvan et al., 2000) and has a molecular mass = 99,906 Da. (The Dalton, (Da), (alternatively atomic mass unit) is a unit of mass used to express atomic and molecular masses. It is defined so that one mole of a substance with atomic or molecular mass 1 Da will have a mass of precisely 1 g.)

<a id='aa3826dc-1c4e-46fb-bfa6-ecd514e022a3'></a>

Therefore the full HMG-CoA reductase molecule is an enzyme
containing 4 active sites with a molecular mass M_r=2 \u00d7 99,906=
199,812 Da, i.e. 1 mole HMG-CoA reductase has a mass of 199,812 g.
The reaction catalysed by HMG-CoA reductase is given by

<a id='e23085b8-dccb-4d8c-8b24-5be5879f4638'></a>

HMG - CoA + 2NADPH + 2H+
→mevalonate + 2NADP+ + CoASH,

(A.6)

<a id='459f1d73-ec48-4b80-9348-e369bd23e166'></a>

which indicates a stoichiometry of one mole mevalonate being produced from one mole HMG-CoA. (Note all other substrates of this reaction are assumed to be present in excess).

<a id='fa86c6c7-5e24-48a7-922e-0b8b24eebf9c'></a>

Segel (1993) suggests that there are approximately 1000 different enzymes in a cell. Thus the moles of enzyme in 1 mg of protein are equivalent to

<a id='82a95b98-fce3-420f-9347-4f5b67ee337e'></a>

( (1 × 10⁻³ g) / (199,812 g mol⁻¹) × 1000 ) = 5.00 × 10⁻¹² mol, (A.7)

<a id='67e3e0ee-9c11-4d61-9ae3-6e6472aba661'></a>

and given 4 active sites per HMG-CoA reductase enzyme, there are
2.00 x 10⁻¹¹ moles of enzyme active sites in 1 mg of protein. Given
the specific activity of an enzyme, 52 x 10⁻¹² mol min⁻¹ mg⁻¹,
we have

<a id='c2e7349b-fa52-4140-bb80-76b4f32f7df0'></a>

$$\frac{52 \times 10^{-12} \text{ mol min}^{-1} \text{ mg}^{-1}}{2.00 \times 10^{-11} \text{ mol mg}^{-1}} = 2.60 \text{ min}^{-1}. \quad \text{(A.8)}$$

<a id='f01a2c06-ae2e-4173-823f-0c61e4a3cb76'></a>

And so, an approximation to the turnover number for HMG-
CoA reductase is given by

$\bar{\mu}_c = 4.33 \times 10^{-2} \text{ s}^{-1}$. (A.9)

<a id='bbac9813-622d-4497-ae8e-5017080e2610'></a>

A.2. Determination of degradation rates – δm, δh and δc

<a id='7eef0b79-995c-47a2-be05-10bed08928cf'></a>

The parameters δm and δh determine the degradation rate of
the HMGCR mRNA, and HMGCR enzyme molecule respectively.
The calculation of these values is based on the half-lives, t1/2, of
the molecules as derived from an exponential decay model. For a
decay constant δ, the rate of degradation of the variable is given by

δ = In 2
    ---
    t1/2

(A.10)

<a id='ecdb8898-2ec5-4986-802d-ccc713f5434f'></a>

Data from Wilson and Deeley (1995) give a half-life of t₁/₂ = 4.3 h for HMG-CoA reductase mRNA, measured in Hep G2 cells and so

δ̅m = ln 2 / 15,480 s = 4.48 × 10⁻⁵ s⁻¹.
(A.11)

<a id='2dc7ee1f-4959-477e-acdf-58feeabb6fd1'></a>

Data from Brown et al. (1974) give a half-life of $t_{1/2} = 3 \text{ h}$ for the HMG-CoA reductase protein, measured in human fibroblast cells and so

$\bar{\delta}_h = \frac{\ln 2}{10,800 \text{ s}} = 6.42 \times 10^{-5} \text{ s}^{-1}$. (A.12)

<a id='44fb9713-bd33-40fa-9432-cd16baee4e93'></a>

The parameter \overline{\delta}_{c} determines the effective loss of cholesterol from the system as cholesterol does not degrade in a similar manner to the other species in the system. The value of this parameter may exhibit significant variation dependent on cellular conditions. For an initial value to be used in simulation, this parameter is assumed to be slightly faster than the degradation rates of protein and mRNA and \delta_{c}=1.20\times10^{-4}s^{-1} is used.

<a id='c72c8aae-f1fb-489b-bb60-63831c5645b6'></a>

A.3. Determination of binding affinity parameters – K̅m and K̅c

The parameter defining the binding reaction between SREBP and the HMGCR gene is K̅m. As no specific experimental data is available for the binding affinity between SREBP and the SRE of the HMGCR gene, we use the results of Yang and Swartz (2011) who quantify the DNA binding affinity for other regulatory transcription factors. Their results provide an estimate of DNA transcription factor binding affinity in the region of 54.2 nmol; these estimates are in keeping with the hypothesis that the interaction between SREBPs and SREs is characterised by relatively high affinity and low saturation kinetics (Amemiya-Kudo et al., 2002). To convert these affinities into units of molecules per ml the following calculation is used.

<a id='db8689c5-739d-43ff-a809-586a5255a200'></a>

A binding affinity of 54.2 nmol is equivalent to

$\frac{54.2 \times 10^{-9}}{1000}$ moles/ml $\times N_A$ (A.13)

<a id='f6e8eb18-1e90-4a64-897e-8feaee9fee5b'></a>

= 3.26 × 1023 molecules/ml,

(A.14)

<a id='218b69f3-13ba-497c-b558-ed19d90bc2d6'></a>

and so $\kappa_m$ is taken to be $\mathcal{O}(10^{13})$.

<a id='6f14f8ed-b4a6-4d1b-8211-40bebcd92fea'></a>

The parameter which describes the binding of cholesterol to SREBP is *k*c. Experimental investigations with cholesterol on the SSD contained in SCAP have revealed difficulty in calculating kinetic constants for this interaction owing to the insolubility of both cholesterol and SCAP, and the necessity of performing kinetic experiments in micelles (Radhakrishnan et al., 2004). Data from Radhakrishnan et al. (2004) indicates that the binding reaction between cholesterol and SCAP is saturable and half-maximal binding occurs at approximately 100 nmol. This value is converted into units of molecules per ml using the following calculation.

<!-- PAGE BREAK -->

<a id='d3788a1f-1ca7-44c0-a54a-c74aec49ea3f'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150–162

<a id='1df6791a-8ea9-4be3-a89d-b6634c95cd6b'></a>

161

<a id='1c498e24-897c-4055-bebf-a2c4d77fed2a'></a>

100 nmol is equivalent to

100 x 10^-9
--- moles/ml x N~A~ (A.15)
1000

= 6.02 x 10^13 molecules/ml. (A.16)

44

<a id='8f54d50c-2752-468a-83b2-ee1adb6aaa54'></a>

A.4. Binding coefficients – x and y

TheThe work of Vallett et al. (1996) suggests that three binding locations on the HMGCR gene are available to SREBP and hence x=3. Experimental investigations on the SSD contained in SCAP have revealed its tetrameric nature (Radhakrishnan et al., 2004, 2008). That is, four molecules of cholesterol may bind to a SCAP–SREBP complex in order to promote inactivation and y=4.

<a id='7de45e77-dea9-4352-a11a-4dc858220cfd'></a>

A.5. Concentration of total transcription factor - s̄0

In general, transcription factors have low gene expression, and are therefore present in relatively low concentrations within the cell (Sanguinetti et al., 2006). Since the SREBP signalling pathway has been simplified it is necessary to make some assumptions to obtain an estimate for this value. The majority of cellular cholesterol is located within the plasma membrane of the cell. Its concentration is governed by multiple regulatory proteins regulated in the ER which are themselves under the control of a small regulatory pool of ER cholesterol (Lange et al., 1999). The concentration of transcription factor, s̄0, is assumed to be of the order of this concentration, which allows small changes in the cellular cholesterol pool to be magnified in the transcription factor pathway. Lange et al. (1999) give an average of 0.45 nmol ER cholesterol per mg cell protein.

<a id='579f8baa-7203-4197-8fcd-0a04584e98cd'></a>

Avogadro's number (N_A = 6.022 × 10^23) and the assumption
that one cell has approximately 300 pg of cell protein and a
volume of 1 pl (1 mg of cell protein is thus equivalent to
3.3 × 10^-3 ml) produces

<a id='58ddc918-b9ed-42fa-8cfb-bc0d803b2dae'></a>

s̄₀ = (0.45 x 10⁻⁹ mol x 6.022 x 10²³ molecules mol⁻¹) / (3.3 x 10⁻³ ml)
= 8.21 x 10¹⁶ molecules ml⁻¹.
(A.17)

<a id='d0a65cf5-17c3-441e-8aa6-bf6d039fce53'></a>

# References
Adiels, M., Packard, C., Caslake, M.J., Stewart, P., Soro, A., et al., 2005. A new combined multicompartmental model for apolipoprotein B-100 and triglyceride metabolism in VLDL subfractions. J. Lipid Res. 46, 58-67.
Alberts, B., Bray, D., Lewis, J., Raff, M., Roberts, K., Watson, J.D., 2008. Molecular Biology of the Cell. Garland Science, New York
Amemiya-Kudo, M., Shimano, H., Hasty, A.H., Yahagi, N., Yoshikawa, T., Matsuzaka, T., Okazaki, H., Tamura, Y., Iizuka, Y., Ohashi, K., Osuga, J.i., Harada, K., Gotoda, T., Sato, R., Kimura, S., Ishibashi, S., 2002. Transcriptional activities of nuclear srebp-1a, -1c, and -2 to different target promoters of lipogenic and cholestero-genic genes. J. Lipid Res. 43, 1220-1235.
August, E., Parker, K.H., Barahona, M., 2007. A dynamical model of lipoprotein metabolism. Bull. Math. Biol. 69, 535-542.
Brown, M.S., Goldstein, J.L., 1979. Receptor mediated endocytosis: insights from the lipoprotein receptor system. Proc. Natl. Acad. Sci. USA 76, 3330-3337.
Brown, M.S., Goldstein, J.L., 1997. The SREBP pathway: regulation of cholesterol metabolism by proteolysis of a membrane bound transcription factor. Cell 89, 331-340.
Brown, M.S., Dana, S.E., Goldstein, J.L., 1974. Regulation of 3-hydroxy-3-methylglutaryl coenzyme A reductase activity in cultured human fibroblasts. Comparison of cells from a normal subject and from a patient with homozygous familial hypercholesterolemia. J. Biol. Chem. 249, 789-796.
Chasman, D., Posada, D., Subrahmanyan, L., Cook, N., Stanton, J.V., Ridker, P., 2004. Pharmacogenetic study of statin therapy and cholesterol reduction. J. Am. Med. Assoc. 291, 2821-2827.
Darzacq, X., Shav-Tal, Y., de Turris, V., Brody, Y., Shenoy, S.M., et al., 2007. In vivo dynamics of RNA polymerase II transcription. Nat. Struct. Mol. Biol. 14, 796-806.

<a id='7897d03c-248c-4ba3-b4ff-ed6275ce41cf'></a>

Dhooge, A., Govaerts, W., Kusnetsov, Y., 2003. Matcont: a matlab package for numerical bifurcation analysis of odes. ACM Trans. Math. Softw. 29, 141-164.
Eberlé, D., Hegarty, B., Bossard, P., Ferré, P., Foufelle, F., 2004. SREBP transcription factors: master regulators of lipid homeostasis. Biochemie 86, 839-848.
Ghosh, A., Chance, B., 1964. Oscillations of glycolytic intermediates in yeast cells. Biochem. Biophys. Res. Commun. 16, 174-181.
Goldstein, J.L., Brown, M.S., 1984. Progress in understanding the LDL receptor and HMG-CoA reductase, two membrane proteins that regulate the plasma choles-terol. J. Lipid Res. 25, 1450-1461.
Goldstein, J.L., Brown, M.S., Anderson, R.G.W., Russell, D.W., Schneider, W.J., 1985. Receptor-mediated endocytosis: concepts emerging from the LDL receptor system. Ann. Rev. Cell. Biol. 1, 1-39.
Goodwin, B.C., 1963. Temporal Organization in Cells—A Dynamic Theory of Cellular Control Processes. Academic Press, London
Goodwin, B.C., 1965. Oscillatory behaviour of enzymatic control processes. Adv. Enzy. Reg. 3, 425-438.
Granner, D.K., Weil, P.A., 2006. Protein synthesis and the genetic code, in: Murray, R. K., Granner, D.K., Rodwell, V.W. (Eds.), Harper's Illustrated Biochemistry, 27th edition. McGraw Hill Medical, USA, pp. 365-379 (Chapter 37).
Griffith, J.S., 1968. Mathematics of cellular control processes I. Negative feedback to one gene. J. Theor. Biol. 20, 202-208.
Grundy, S.M., Cleeman, J.I., Noel-Bairey-Merz, C., Bryan-Brewer, H.J., Clark, L.T., Hunninghake, D.B., Pasternak, R.C., Smith, S.C.J., Stone, N.J., 2004. Implications of recent clinical trials for the national cholesterol education program adult treatment panel III guidelines. Circulation 110, 227-239.
Guckenheimer, J., Holmes, P., 1983. Nonlinear Oscillations, Dynamical Systems and Bifurcations of Vector Fields. Springer-Verlag, New York
Istvan, E.S., Palnitkar, M., Buchanan, S.K., Deisenhofer, J., 2000. Crystal structure of the catalytic portion of human HMG-CoA reductase: insights into regulation of activity and catalysis. EMBO J. 19, 819-830.
Knoblauch, H., Schuster, H., Lust, F.C., Reich, J., 2000. A pathway model of lipid metabolism to predict the effect of genetic variability on lipid levels. J. Mol. Med. 78, 507-515.
Krauss, R.M., Mangravite, L.M., Smith, J.D., Medina, M.W., Wang, D., Guo, X., Rieder, M.J., Simon, J.A., Hulley, S.B., Waters, D., Saad, M., Williams, P.T., Taylor, K.D., Yang, H., Nickerson, D.A., Rotter, J.I., 2008. Variation in the 3-hydroxyl-3-methylglutaryl coenzyme a reductase gene is associated with racial differences in low-density lipoprotein cholesterol response to simvastatin treatment. Circulation 117, 1537-1544.
Lange, Y., Ye, J., Rigney, M., Steck, T.L., 1999. Regulation of endoplasmic reticulum cholesterol by plasma membrane cholesterol. J. Lipid Res. 40, 2264-2270.
Liscum, L., Faust, J.R., 1987. Low density lipoprotein (LDL)-mediated suppression of cholesterol synthesis and LDL uptake is defective in Niemann-Pick type C fibroblasts. J. Biol. Chem. 262, 17002-17008.
Liscum, L., Ruggiero, R.M., Faust, J.R., 1989. The intracellular transport of low density lipoprotein-derived cholesterol is defective in Niemann-Pick type C fibroblasts. J. Cell Biol. 108, 1625-1636.
Mensink, R., Zock, P., Kester, A., Katan, M., 2003. Effects of dietary fatty acids and carbohydrates on the ratio of serum total to HDL cholesterol and on serum lipids and apolipoproteins: a meta-analysis of 60 controlled trials. Am. J. Clin. Nutr. 77, 1146-1155.
Micha, R., Mozaffarian, D., 2010. Saturated fat and cardiometabolic risk factors, coronary heart disease, stroke, and diabetes: a fresh look at the evidence. Lipids 45, 893-905.
Murray, J.D., 2002. Mathematical Biology I: An Introduction. Springer Verlag, New York
Packard, C.J., Demant, T., Stewart, J.P., Bedford, D., Caslake, M.J., et al., 2000. Apolipoprotein B metabolism and the distribution of VLDL and LDL subfrac-tions. J. Lipid Res. 41, 305-318.
Radhakrishnan, A., Sung, L.P., Kwon, H.J., Brown, M.S., Goldstein, J.L., 2004. Direct binding of cholesterol to the purified membrane region of SCAP: mechanism for a sterol-sensing domain. Mol. Cell 15, 259-268.
Radhakrishnan, A., Goldstein, J.L., McDonald, J.G., Brown, M.S., 2008. Switch-like control of SREBP-2 transport triggered by small changes in ER cholesterol: a delicate balance. Cell Metab. 8, 512-521.
Sanguinetti, G., Lawrence, N.D., Rattray, M., 2006. Probabilistic inference of transcription factor concentrations and gene-specific regulatory activities. Bioinformatics 22, 2775-2781.
Segel, I.H., 1993. Enzyme Kinetics. Behavior and Analysis of Rapid Equilibrium and Steady State Enzyme Systems. Wiley-Interscience, USA.
Simons, K., Iknonen, E., 2000. How cells handle cholesterol. Science 290, 1721-1726.
Slobin, L.I., 1991. Polypeptide chain elongation. In: Trachsel, H. (Ed.), Translation in Eukaryotes, 1st edition. CRC Press, Boca Raton, Florida, pp. 149-176 (Chapter 6).
Soutar, A.K., Knight, B.L., 1990. Structure and regulation of the LDL-receptor and its gene. Brit. Med. Bull. 46, 891-916.
Tabas, I., 1997. Free cholesterol-induced cytotoxicity. A possible contributing factor to macrophage foam cell necrosis in advanced atherosclerosis lesions. Trends Cardiovasc. Med. 7, 256-263.
Tanaka, R.D., Edwards, P.A., Lan, S.F., Knoppel, E.M., Fogelman, A.M., 1982. Purifica-tion of 3-hydroxy-3-methylglutaryl coenzyme A reductase from human liver. J. Lipid Res. 23, 523-530.
Tangirala, R.K., Jerome, W.G., Jones, N.L., Small, D.M., Johnson, W.J., et al., 1994. Formation of cholesterol monohydrate crystals in macrophage-derived foam cells. J. Lipid Res. 35, 93-104.
Vallett, S.M., Sanchez, H.B., Rosenfeld, J.M., Osborne, T.F., 1996. A direct role for sterol regulatory element binding protein in activation of 3-hydroxy-3-methylglutaryl coenzyme A reductase gene. J. Biol. Chem. 271, 12247-12253.

<a id='1850434d-d74e-44eb-ae9b-6c3b4179d05e'></a>

and so κc is taken to be $\mathcal{O}(10^{14})$.

<!-- PAGE BREAK -->

<a id='fce2f783-baae-4bd0-9aca-9552c4f6b4b1'></a>

162

<a id='26d11f5b-65f6-4455-b090-d19ef7fa5e50'></a>

B.S. Bhattacharya et al. / Journal of Theoretical Biology 349 (2014) 150-162

<a id='07efaf18-eebb-42a7-8a3f-7ae57b902a49'></a>

Wattis, J.A.D., O'Malley, B., Blackburn, H., Pickersgill, L., Panovska, J., Byrne, H.M.,
Jackson, K.G., 2008. Mathematical model for low density lipoprotein (LDL)
endocytosis by hepatocytes. Bull. Math. Biol. 70, 2303-2333.
Waxman, A., Collins, A., Tschudy, D., 1966. Oscillations of hepatic delta-
aminolevulinic acid synthetase produced by heme. Biochem. Biophys. Res.
Commun. 24, 675-683.
Wilson, G.M., Deeley, R.G., 1995. An episomal expression vector system for
monitoring sequence specific effects on mRNA stability in human cell lines.
Plasmid 33, 198-207.
Xu, J., Nakamura, M., Cho, H., Clarke, S., 1999. Sterol regulatory element binding
protein-1 expression is suppressed by dietary polyunsaturated fatty acids a

<a id='13f02c23-549f-4b5a-91b4-ea0150c7d8b9'></a>

mechanism for the coordinate suppression of lipogenic genes by polyunsatu-rated fatty acids. J. Biol. Chem. 274, 23577-23583.
Yang, W.C., Swartz, J.R., 2011. A filter microplate assay for quantitative analysis of DNA binding proteins using fluorescent DNA. Anal. Biochem. 415, 168-174.
Yang, T., Espenshade, P.J., Wright, M.E., Daisuke, Y., Gong, Y., et al., 2002. Crucial step in cholesterol homeostasis: sterols promote binding of SCAP to INSIG-1, a membrane protein that facilitates retention of SREBPs in ER. Cell 110, 489-500.
Yeagle, P.L., 1991. Modulation of membrane function by cholesterol. Biochemie 73, 1303-1310.
Zhang, H., Jiang, T., 2010. Synthetic circuits, devices and modules. Protein Cell 1, 974-978.