<a id='bf6fcb5d-d40e-432a-8ed2-2796f501dca3'></a>

© original report

**Mathematical Approach to Differentiate Spontaneous and Induced Evolution to Drug Resistance During Cancer Treatment**

James M. Greene, PhD¹; Jana L. Gevertz, PhD²; and Eduardo D. Sontag, PhD³,⁴

<a id='899dcef4-4496-44b1-9e97-071ac0be89b4'></a>

abstract

**PURPOSE** Drug resistance is a major impediment to the success of cancer treatment. Resistance is typically thought to arise from random genetic mutations, after which mutated cells expand via Darwinian selection. However, recent experimental evidence suggests that progression to drug resistance need not occur randomly, but instead may be induced by the treatment itself via either genetic changes or epigenetic alterations. This relatively novel notion of resistance complicates the already challenging task of designing effective treatment protocols.

<a id='96018690-1184-4314-97b9-e8537a140a66'></a>

**MATERIALS AND METHODS** To better understand resistance, we have developed a mathematical modeling framework that incorporates both spontaneous and drug-induced resistance.

<a id='e5d205da-ff3e-4ac0-8533-8455a32436f7'></a>

RESULTS Our model demonstrates that the ability of a drug to induce resistance can result in qualitatively different responses to the same drug dose and delivery schedule. We have also proven that the induction parameter in our model is theoretically identifiable and propose an in vitro protocol that could be used to determine a treatment's propensity to induce resistance.

<a id='d0894df3-4594-4de8-b5e9-40717436ebdf'></a>

Clin Cancer Inform. © 2019 by American Society of Clinical Oncology
Licensed under the Creative Commons Attribution 4.0 License cc i

<a id='6e71269c-d674-4d63-8e30-bb99bf46adea'></a>

## INTRODUCTION

Tumor resistance to chemotherapy and targeted drugs is a major cause of treatment failure. Both molecular and microenvironmental factors have been implicated in the development of drug resistance.¹ As an example of molecular resistance, upregulation of drug efflux transporters can prevent sufficiently high intracellular drug accumulation, which limits treatment efficacy.² Other molecular causes of drug resistance include modification of drug targets, enhanced DNA damage repair mechanisms, dysregulation of apoptotic pathways, and the presence of cancer stem cells.¹⁻⁵ Irregular tumor vasculature that results in inconsistent drug distribution and hypoxia is an example of a microenvironmental factor that impacts drug resistance.⁶ Other characteristics of the tumor microenvironment influencing drug resistance include regions of acidity, immune cell infiltration and activation, and the tumor stroma.¹,⁶⁻¹⁰ Experimental and clinical research continues to shed light on the multitude of factors that contribute to cancer drug resistance. Mathematical modeling studies have also been used to explore both broad and detailed aspects of cancer drug resistance, as reviewed previously.¹¹⁻¹³

<a id='f63d9d5a-523d-432a-82cd-c93712220bc5'></a>

Resistance to cancer drugs can be classified as either
pre-existing or acquired.¹ Pre-existing—or intrinsic—

<a id='7490150f-7b13-45ca-80bf-c92b835fd7cc'></a>

drug resistance describes the case in which a tumor contains a subpopulation of drug-resistant cells at the initiation of treatment, which makes therapy even-tually ineffective as a result of resistant cell selection.¹
As examples, pre-existing BCR-ABL kinase domain mutations confer resistance to the tyrosine kinase inhibitor imatinib in patients with chronic myeloid leukemia,¹⁴,¹⁵ and pre-existing MEK1 mutations confer resistance to BRAF inhibitors in patients with melanoma.¹⁶ Many mathematical models have considered how the presence of such pre-existing resistant cells impacts cancer progression and treatment.¹⁷⁻⁴⁰

<a id='0be9db3c-2b2d-4fa4-b728-544bae975d20'></a>

Acquired drug resistance broadly describes the case in which drug resistance develops during the course of therapy from a population of cells that were initially drug sensitive.<sup>1</sup> The term acquired resistance is really an umbrella term for two distinct phenomena, which complicates the study of acquired resistance. On the one hand, there is resistance that is spontaneously—or randomly—acquired during the course of treatment, be it as a result of random genetic mutations or stochastic nongenetic phenotype switching.<sup>41</sup> This spontaneous form of acquired resistance has been considered in many mathematical models.<sup>18-22,27-29,31,32,35,40,42-49</sup> On the other hand, drug resistance can be induced (ie, caused) by the drug itself.<sup>41,50-52</sup>

<a id='13854f3e-95d9-4dd8-b905-93c25835375e'></a>

<::transcription of the content
: ASCO®
: logo::>

<a id='839d24a9-7bfc-421d-8d4e-d531a00967a5'></a>

JCO® Clinical Cancer Informatics

<a id='4136e786-9671-49c8-8e99-2f3d5e007aa2'></a>



<a id='70978828-dc17-4f1a-8a0b-d6721053fe02'></a>

**ASSOCIATED**
**CONTENT**

**Appendix**
**Data Supplement**

Author affiliations
and support
information (if
applicable) appear at
the end of this
article.

<a id='cb5a9aef-adda-4425-a0d0-e308762a379e'></a>

Accepted on February
14, 2018 and
published at
ascopubs.org/journal/
cci on April 10, 2019:
DOI https://doi.org/10.
1200/CCI.18.00087

<!-- PAGE BREAK -->

<a id='dc28717e-7524-4d74-8434-a18fcd42e6a4'></a>

Greene, Gevertz, and Sontag

<a id='7e14ece6-2885-41b9-972b-d27e5a8248b8'></a>

## CONTEXT
### Key Objective
Resistance to chemotherapy may arise from Darwinian selection of resistant subclones that either predate therapy or emerge during treatment. In addition, treatment itself may induce genetic or epigenetic variation that catalyzes drug resistance. This work aims to mathematically tease out these various factors.

<a id='e6cd69a0-2bdd-4fed-aa4c-4a5f5858d65f'></a>

## Knowledge Generated
A mathematical model is introduced to distinguish the effect of drugs that merely select from those that both create variation and select. The ability of a drug to induce resistance can result in qualitatively different responses on the basis of dose and delivery; constant-infusion regimes are less successful in controlling tumor growth than pulsed therapy for drugs that induce resistance, but the situation is reversed for drugs that act only by selection.

<a id='3064e20f-6fc5-4c6e-9a68-2ca2fa97e892'></a>

**Relevance**
Recent experimental evidence suggests that progression to drug resistance need not occur randomly, but instead may be induced by the treatment itself. Understanding the clinical implications of treatment-induced resistance will help formulate appropriate protocols.

<a id='02bc7eec-ff82-4b25-a675-977f0f38c6fe'></a>

The question of whether resistance is an induced phe-nomenon or predates treatment was first famously studied by Luria and Delbrück 53 in the context of bacterial (*Escherichia coli*) resistance to a virus (T1 phage). In particular, Luria and Delbrück hypothesized that if selective pressures imposed by the presence of the virus induce bacterial evolution, then the number of resistant colonies formed in their plated experiments should be Poisson distributed and thus have an approximately equal mean and variance. What Luria and Delbrück found instead was that the number of resistant bacteria on each plate varied drastically, with variance being significantly larger than the mean. As a result, the authors concluded that bacterial mutations predated the viral challenge. 53

<a id='767e5a39-883e-4284-a38d-4caaf9bb8c43'></a>

In the case of cancer, there is strong evidence that at least some drugs have the ability to induce resistance, as genomic mutations can be caused by cytotoxic cancer chemotherapeutics.54,55 For instance, nitrogen mustards can induce base substitutions and chromosomal rearrangements, topoisomerase II inhibitors can induce chromosomal translocations, and antimetabolites can induce double-stranded breaks and chromosomal aberrations.54 Such drug-induced genomic alterations would generally be nonreversible. Drug resistance can also be induced at the epigenetic level.41,50,56 For example, expression of multidrug resistance 1 (MDR1), an ABC-family membrane pump that mediates the active efflux of the drug, can be induced during treatment.1,41 In another recent example, the addition of a chemotherapeutic agent is shown to induce, through a multistage process, epigenetic reprogramming in patient-derived melanoma cells.56 Resistance developed in this way can occur quite rapidly and can often be reversed.41,52,57

<a id='09b4f1c0-bab5-48ff-95ff-adb89be61c72'></a>

Despite these known examples of drug-induced resistance,
differentiating between drug-selected and drug-induced
resistance is nontrivial. For example, what appears to be

<a id='ebfc337f-9d48-4532-9334-5ec4bc4b58e6'></a>

drug-induced acquired resistance may simply be the rapid selection of a small number of pre-existing resistant cells or the selection of cells that spontaneously acquired resistance.41,44 In pioneering work by Pisco and colleagues,41 the relative contribution of resistant cell selection versus drug-induced resistance was assessed in an experimental system that involved HL60 leukemic cells that were treated with the chemotherapeutic agent vincristine. After 1 to 2 days of treatment, expression of MDR1 was demonstrated to be predominantly mediated by cell-individual induction of MDR1 expression and not by the selection of MDR1-expressing cells.41,58 In particular, these cancer cells exploit their heritable, nongenetic phenotypic plasticity-by which one genotype can map onto multiple stable phenotypes-to change their gene expression to a temporarily more resistant state in response to treatment-related stress.41,58

<a id='55ad8935-c845-4b97-a09d-be1167a4628a'></a>

Although there is a wealth of mathematical research that addresses cancer drug resistance, relatively few models have considered drug-induced resistance. Of the models of drug-induced resistance that have been developed, many do not explicitly account for the presence of the drug. Instead, it is assumed that these models apply only under treatment, 41,59-62 with the effects of the drug implicitly captured in model terms. As these models of resistance induction are dose independent, they are unable to capture the effects that the alteration of the drug dose has on resistance formation. To our knowledge, there have been less than a handful of mathematical models developed in which resistance is induced by a drug in a dose-dependent fashion. 33,34,63, In Gevertz et al33 and follow-up work in Shah, Rejniak, and Gevertz38 and Perez-Velazquez et al, 64 duration and intensity of drug exposure determines the resistance level of each cancer cell. This model allows for a continuum of resistant phenotypes, but is computationally complex as it is a hybrid discrete-continuous, stochastic spatial model. While interesting features about

<a id='89a93c50-9984-4553-a2c8-aa240ec8efa6'></a>

2  2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='41f570c3-558b-4819-a63d-cf7aeb6d713e'></a>

Differentiating Spontaneous and Induced Resistance

<a id='69ffd5d1-3dff-41c4-95db-4e67cc9cab95'></a>

the relationship between induced resistance and the mi-
croenvironment have been deduced from this model, its
complexity does not allow for general conclusions to be
drawn about dose-dependent resistance induction.

<a id='11548f5a-6398-40af-9b93-99757b09a304'></a>

Another class of models that addresses drug-induced resistance is that in Chisholm et al. 63 These models are distinct in that they are motivated by in vitro experiments in which a cancer drug transiently induces a reversible resistant phenotypic state. 52 The individual-based and integro-differential equation models developed consider rapidly proliferating drug-sensitive cells, slowly proliferating drug-resistant cells, and rapidly proliferating drug-resistant cells. An advection term—with the speed depending on drug levels—is used to model drug-induced adaptation of the cell proliferation level, and a diffusion term for both the level of cell proliferation and survival potential (response to drug) is used to model nongenetic phenotype instability. 63 Through these models, the contribution of nongenetic phenotype instability (both drug induced and random), stress-induced adaptation, and selection can be quantified. 63

<a id='0508a4d7-e5fe-4986-8f25-d47dc7c3f70e'></a>

Finally, the work in Liu et al34 models the evolutionary dynamics of the tumor population as a multitype non-homogeneous continuous time birth-death stochastic process. This model accounts for the ability of a targeted drug to alter the rate of resistant cell emergence in a dose-dependent manner. The authors specifically considered cases in which the rate of mutation that gives rise to a resistant cell: (1) increases as a function of drug concentration, (2) is independent of drug concentration, and (3) decreases with drug concentration. Interestingly, this model led to the conclusion that the optimal treatment strategy is independent of the relationship between drug concentration and the rate of resistance formation. In particular, the authors found that resistance is optimally delayed using a low-dose continuous treatment strategy coupled with high-dose pulses.

<a id='274a8bf4-a806-486e-a3d3-145d08f85677'></a>

As in vitro experiments have demonstrated that treatment response can be affected by drug-induced resistance,41,52 in the current work we seek to understand this phenomenon further using mathematical modeling. The initial mathematical model that we have developed—and that will be analyzed herein—is a system of two ordinary differential equations with a single control representing the drug. We intentionally chose a minimal model that would be amenable to analysis, as compared with previously developed models of drug-induced resistance which are significantly more complex.33,38,63,64 Despite the simplicity of the model, it incorporates both spontaneous and drug-induced resistance.

<a id='1bac5fa3-2574-4fe2-bdf0-fdce7fc70181'></a>

In addition to drug-induced resistance, the other charac-
teristic of cancer dynamics we explore is that of traditional,
maximally tolerated dose (MTD) treatment protocols
compared with high-frequency, low-dose so-called

<a id='abbe2e1b-dc8a-40f1-a8f8-756bfa74af8d'></a>

metronomic therapies. Indeed, the differential response between these therapies is fundamentally related to intratumoral heterogeneity/competition, and is explicitly considered in our model. Furthermore, results presented in this work support recent evidence that promotes the adoption of metronomic therapy in many circumstances, 65-69 and a main objective of this work is to relate competition and drug-induced resistance to therapy design.

<a id='dc8b2420-1dcc-45cf-97f7-01d76f07f151'></a>

This work is organized as follows. We begin by introducing a mathematical model to describe the evolution of drug resistance during treatment with a theoretical resistance-inducing—and noninducing—drug. We use this mathematical model to explore the role played by the drug's resistance induction rate in treatment dynamics. We demonstrate that the induction rate of a theoretical cancer drug could have a nontrivial impact on the qualitative responses to a given treatment strategy, including tumor composition and the time horizon of tumor control. In our model, for a resistance-preserving drug—that is, a drug that does not induce resistance—better tumor control is achieved using a constant therapeutic protocol versus a pulsed one. Conversely, in the case of a resistance-inducing drug, pulsed therapy prolongs tumor control longer than constant therapy as a result of sensitive/resistant cell competitive inhibition. Once the importance of induced resistance has been established, we demonstrate that all parameters in our mathematical model are identifiable, meaning that it is theoretically possible to determine the rate at which drug resistance is induced for a given treatment protocol. As this theoretical result does not directly lend itself to an experimental approach for quantifying the ability of a drug to induce resistance, we also describe a potential in vitro experiment for approximating this ability utilizing constant therapies. We end with some concluding remarks and a discussion of potential extensions of our analysis, such as a model that differentiates between reversible and nonreversible forms of resistance.

<a id='7154f273-ba16-4084-be63-3c6ad4dbadd4'></a>

## MATERIALS AND METHODS

Here we introduce a general modeling framework to describe the evolution of drug resistance during treatment. Our model captures the fact that resistance can result from random events or can be induced by the treatment itself. Random events that can confer drug resistance include genetic alterations—for example, point mutations or gene amplification—and phenotype switching.⁴¹ These spontaneous events can occur either before or during treatment. Drug-induced resistance is resistance specifically activated by the drug and, as such, depends on the effective dose encountered by a cell. Such a formulation allows us to distinguish the contributions of both drug-dependent and drug-independent mechanisms, as well as any dependence on pre-existing—that is prior to treatment—resistant populations.

<a id='0838063b-659c-4077-abf9-ba60b30e080a'></a>

JCO Clinical Cancer Informatics

<a id='23e7d3d9-7b9c-48b9-876e-96f7f60e0153'></a>

3

<!-- PAGE BREAK -->

<a id='29f1638b-162b-41d6-b145-1f61ad079d68'></a>

Greene, Gevertz, and Sontag

<a id='6ed0f617-0708-4552-b133-0e20facaae2a'></a>

We consider the tumor to be composed of two types of cells, sensitive (_S_) and resistant (_R_). Sensitive (or wild-type) cells are fully susceptible to treatment, whereas treatment affects resistant cells to a lesser degree. To analyze the role of both random and drug-induced resistance, we use a system of two ordinary differential equations to describe the dynamics between the _S_ and _R_ subpopulations:

<a id='799e9908-568e-4602-a521-735cea062d94'></a>

$\frac{dS}{dt} = r\left(1 - \frac{S+R}{K}\right)S - (\epsilon + \alpha u(t))S - du(t)S + \gamma R, (1)$

<a id='a6292225-2793-4901-a98e-6f5495e06026'></a>

$$\frac{dR}{dt} = r_R\left(1 - \frac{S+R}{K}\right)R + (\epsilon + \alpha u(t))S - d_R u(t)R - \gamma R. \quad (2)$$

<a id='9835310d-14f2-4a4b-bddc-b5f641162964'></a>

All parameters are non-negative. In the absence of treat-
ment, we assume that the tumor grows logistically, with
each population contributing equally to competitive in-
hibition. Phenotypes _S_ and _R_ each possess individual
intrinsic growth rates, and we make the assumption in
the remainder of the work that 0 ≤ _r_R < _r_. This simply
states that resistant cells grow slower than nonresistant
cells, an assumption that is supported by experimental
evidence.70-72

<a id='a7aa8230-b8d3-488f-83f2-b71dc789b59c'></a>

The transition to resistance can be described with a net term of the form ɛS + au(t)S. Mathematically, the drug-induced term au(t)S, where u(t) is the effective applied drug dose at time t, describes the effect of treatment on promoting the resistant phenotype. For example, this term could represent the induced overexpression of the P-glycoprotein gene, a well-known mediator of multidrug resistance, by the application of chemotherapy. 1,73

<a id='ca88e9ac-ddc0-4551-a203-5e4913135e10'></a>

Spontaneous evolution of resistance is captured in the the \$\epsilon S\$
term, which permits resistance to develop even in the
absence of treatment. Note that \$\epsilon\$ is generally considered
small, 74 although recent experimental evidence regarding
error-prone DNA polymerases suggests that cancer cells
may have increased mutation rates as a result of the
overexpression of such polymerases. 75-77 For example, in
Krutyakov, 75 mutation rates as a result of such polymerases
are characterized by probabilities as high as \$7.5 \times 10^{-1}\$ per
base substitution, and it is known that many point muta-
tions in cancer arise from these DNA polymerases. 77 For
this work, we adopt the notion that random point mutations
that lead to drug resistance are rare, and that drug-induced
resistance occurs on much quicker time scales 41; there-
fore, we will assume that \$\alpha > \epsilon\$ with \$u = O(1)\$ in our analysis
of Equations 1 and 2.

<a id='0619aa70-a71d-4f70-9800-3d5a03214f09'></a>

We model the effects of treatment by assuming the log-kill hypothesis, 78 which states that a given dose of chemotherapy eliminates the same fraction of tumor cells regardless of tumor size. We allow for each cellular compartment to have a different drug-induced death rate (d, dR); however, to accurately describe resistance it is required that 0 ≤ dR < d. Our analysis presented herein will

<a id='97ff6d06-fe20-4b81-9c1c-a199d36c51f0'></a>

be under the simplest assumption that the drug is com-pletely ineffective against resistant cells, so that $d_R = 0$.

<a id='722b5013-0b44-49fa-a9d0-fff89bc7699d'></a>

The last term in the equations, γR, represents the resensitization of cancer cells to the drug. In the case of non-reversible resistance, γ = 0; otherwise γ > 0. Our subsequent analysis will be done under the assumption of nonreversible resistance. For a discussion of the effect of reversibility on the presented model, see the Appendix.

<a id='3ef3a640-6b5d-4ef3-a740-4cd776a107e1'></a>

Finally, we note that the effective drug concentration _u_(_t_)
can be thought of as a control input. For simplicity, in this
work we assume that it is directly proportional to the applied
drug concentration; however, pharmacodynamic/phar-
macokinetic considerations could be incorporated to more
accurately describe the uptake/evolution of the drug in vivo
or in vitro—for example, as in Bender, Schindler, and
Friberg, 79 Wu et al,80 and Fetterly et al.81

<a id='fd27cee4-9a3a-4b43-bd5f-0fa57704436a'></a>

To understand the above system of drug resistance evo-
lution, we reduce the number of parameters via non-
dimensionalization. Rescaling _S_ and _R_ by their (joint)
carrying capacity _K_, and time _t_ by the sensitive cell growth
rate,

<a id='edae7ca7-ade4-4dcd-b8aa-158a7666ed8a'></a>

Š(τ) = 1/K S(1/r τ),
Ř(τ) = 1/K R(1/r τ),

(3)

<a id='6243b548-dfd1-40e5-a2d8-47eb772ce002'></a>

Equations 1 and 2 (with γ = d_R = 0) can be written in the form,

dS/dt = (1 − (S + R))S − (ε + αu(t))S – du(t)S, (4)

dR/dt = p_r(1 − (S + R))R + (ε + αu(t))S. (5)

<a id='a5c84be8-6d6e-4fcb-b852-dd4f36b531f3'></a>

For convenience, we have relabeled _S_, _R_, and _t_ to coincide with the nondimensionalization so that the parameters _ε_, _α_, and _d_ must be scaled accordingly (by 1/_r_). As _r_R was assumed to satisfy 0 ≤ _r_R < _r_, the relative resistant population growth rate _p_r satisfies 0 ≤ _p_r < 1.

<a id='681eca0b-4bf7-4267-87a7-f6351300a541'></a>

One can show (Appendix) that asymptotically, under any treatment regimen $u(t) \ge 0$, the entire population will become resistant:

$$\begin{pmatrix} S(t) \\ R(t) \end{pmatrix} \xrightarrow{t \to \infty} \begin{pmatrix} 0 \\ 1 \end{pmatrix}.\quad(6)$$

<a id='11b7b30f-a8a6-436f-94b6-f6117de3c4cf'></a>

However, tumor control is still possible where one can combine therapeutic efficacy and clonal competition to influence transient dynamics and possibly prolong patient life. Indeed, the modality of adaptive therapy has shown promise in using real-time patient data to inform therapeutic modulation aimed at increasing quality of life and survival times.⁶⁷ This work will focus on such dynamics and controls.

<a id='73d0cf66-d85d-4f4c-b582-09576d1651dc'></a>

4 © 2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='af05ff89-336b-45bb-96a7-7e57dec93133'></a>

Differentiating Spontaneous and Induced Resistance

<a id='a6dd2ad2-165a-40b6-b53b-874be1fae81f'></a>

<span style="color:#e26b28;">**RESULTS**</span>
**Effect of Induction on Treatment Efficacy**
We investigate the role of the induction capability of a drug (parameter α in Eqs 4 and 5) on treatment dynamics. Specifically, the value of α may have a substantial impact on the relative success of two standard therapy protocols—constant dosage and periodic pulsing.

<a id='a79fa988-1c6d-43a2-a175-c570a7e621d8'></a>

## Treatment Protocol
To quantify the effects of induced resistance, a treatment protocol must be specified. We adopt a clinical perspective over the course of the disease, which is summarized in Figure 1. We assume that the disease is initiated by a small number of wild-type cells:

<a id='3ec9b462-7b64-49bf-8fa1-2feaaef8c039'></a>

S(0) = S0, R(0) = 0,

(7)

<a id='0183f449-3cb5-4435-801f-5017ef81a258'></a>

where 0 < S₀ < 1. Denote the tumor volume at time t by
V(t):

V(t) = S(t) + R(t).

(8)

<a id='010d6e32-2d83-49a7-94fd-7fb0cf73f1d8'></a>

The tumor then progresses untreated until a specific vol-
ume $V_d$ is detected—or, for hematologic tumors, via ap-
propriate blood markers—which using existing nuclear
imaging techniques corresponds to a tumor with diameter
on the order of 10 mm.$^{82}$ Time to reach $V_d$ is denoted by $t_d$,
which in general depends on all parameters that appear in
Equations 4 and 5. Note that, assuming $\epsilon > 0$, a nonzero
resistant population will exist at the onset of treatment.
Therapy, represented through $u(t)$, is then applied until the
tumor reaches a critical size $V_c$, which we equate with
treatment failure. Because the $(S,R) = (0,1)$ state is globally
asymptotically stable in the first quadrant, $V_c < 1$ is
guaranteed to be obtained in finite time. Time until failure,
$t_c$, is then a measure of efficacy of the applied $u(t)$.

<a id='96de7e6e-1231-4808-9180-5898d828b612'></a>

Although a diverse set of inputs *u(t)* may be theoretically applied, presently we consider only strategies as illustrated in Figure 1B. The blue curve in Figure 1B corresponds to a constant effective dosage *u_c(t)* initiated at *t_d*—administered approximately using continuous infusion pumps and/or slow-release capsules—whereas the black curve represents a corresponding pulsed strategy *u_p(t)*, with fixed treatment windows (*Δt_on*) and holidays (*Δt_off*). In general, we may allow for different magnitudes, *U_on,c* and *U_on,p*, for constant and pulsed therapies respectively—for example, to relate the total dosage applied per treatment cycle (area under the drug concentration-time curve [AUC]^(83)). However, for simplicity we assume the same magnitude in the subsequent section (although see the Appendix for a normalized comparison). While these represent idealized therapies, such *u(t)* may form an accurate approximation to in vitro and/or in vivo kinetics. Note that the response *V(t)* illustrated in Figure 1A will not be identical, or even qualitatively similar, for both presented strategies, as will be demonstrated numerically.

<a id='6077af69-fe65-49eb-9c98-1841d02d51a1'></a>

**Constant Versus Pulsed Therapy Comparison**
To qualitatively demonstrate the role that induced resistance plays in the design of therapy schedules, we consider two drugs with the same cytotoxic potential—that is, the same drug-induced death rate *d*—each possessing a distinct level of resistance induction (parameter *α*). A fundamental question, then, is whether there exist qualitative distinctions between treatment responses for each chemotherapy. More specifically, how does survival time compare when scheduling is altered between constant therapy and pulsing? Does the optimal strategy—in this case, optimal across only two schedulings—change depending on the extent to which the drug induces resistance?

<a id='1ae0601c-e1d6-4b83-8449-23c13fec64d3'></a>

ically stable in the first quadrant, Vc < 1 is ed to be obtained in finite time. Time until failure, 1 a measure of efficacy of the applied u(t). We fix two values of the induction parameter α: αs = 0, αi = 10⁻². <::chart: The visual content shows two plots, (A) and (B), depicting tumor dynamics and treatment regimes. (A) Tumor Volume vs. Time: The y-axis is labeled "Tumor Volume" with values V, Vc, Vd, V0. The x-axis is labeled "Time" with values td, tc, t. A gray curve shows tumor volume starting at V0, increasing to Vd, decreasing, and then rapidly increasing to Vc. A dashed red horizontal line marks Vc. A dashed blue horizontal line marks Vd. (B) Treatment vs. Time: The y-axis is labeled "Treatment" with values u, u_on,p, u_on,c. The x-axis is labeled "Time" with values td, tc, t. A legend indicates "Constant" (blue line) and "Pulsed" (gray dashed line). A solid blue horizontal line represents "Constant" treatment at u_on,c, starting at td and ending at tc. A dashed gray line represents "Pulsed" treatment at u_on,p, showing intermittent pulses from td to tc. FIG 1. Schematic of tumor dynamics under two treatment regimes. (A) Tumor volume V in response to treatment initiated at time td. Cancer population arises from a small sensitive population at time t = 0, upon which the tumor grows to detection at volume Vd. Treatment is begun at td and continues until the tumor reaches a critical size Vc (at a corresponding time tc), where treatment is considered to have failed. (B) Illustrative constant and pulsed treatments, both initiated at t = td.::>

<a id='e37e5e38-2957-44ca-8b9c-3787e80b6f6e'></a>

JCO Clinical Cancer Informatics

<a id='d95687de-6d69-4518-9c49-19812cd92249'></a>

5

<!-- PAGE BREAK -->

<a id='61d1de51-c67b-46d3-b533-61bda7ee74c8'></a>

Greene, Gevertz, and Sontag

<a id='eb6a98ef-2a9a-4362-a7ab-1b6b871b947b'></a>

Recall that we are studying the nondimensional model Equations 4 and 5, so no units are specified. Parameter $\alpha=0$ corresponds to no therapy-induced resistance (henceforth denoted as phenotype preserving), and therefore considering this case allows for a comparison between the classic notion of random evolution toward resistance ($\alpha=0$) and drug-induced resistance ($\alpha>0$). For the remainder of the section, parameters are fixed as in Table 1. Critically, all parameters excluding $\alpha$ are identical for each drug, which enables an unbiased comparison. Treatment magnitudes $u_{on,c}$ and $u_{on,p}$ are selected to be equal: $u_{on,c}=u_{on,p}=u_{on}$.

<a id='89f9b2ea-b56e-4839-aedb-ba59125ec405'></a>

Note that selecting parameter V_d = 0.1 implies that the carrying capacity has a diameter of 100 mm, as V_d corresponds to a detectable diameter of 10 mm. Assuming each cancer cell has volume 10^-6 mm^3, tumors in our model can grow to a carrying capacity of approximately 12.4 cm in diameter, which is in qualitative agreement with the parameters estimated in Chignola and Foroni^84 (≈12.42 cm, assuming a tumor spheroid).

<a id='df0ef997-2c87-4953-b1b2-faafd0f52059'></a>

By examining Figures 2A and 2B, we clearly observe an improved response to constant therapy when using a phenotype-preserving drug, with treatment success time tc nearly seven times as long compared with pulsed therapy (tc ≈ 90 for constant, compared with tc ≈ 14 for pulsed). It can be observed that the tumor composition at treatment conclusion is different for each therapy—not shown for this simulation, but see a comparable result in Appendix Figures A2B and A2D—and it seems that pulsed therapy was not sufficiently strong to hamper the rapid growth of the sensitive population. Indeed, treatment failed quickly as a result of insufficient treatment intensity in this case, as the population remains almost entirely sensitive. Thus, for this patient under these specific treatments, assuming drug resistance only arises via random stochastic events, constant therapy would be preferred. One might argue that pulsed, equal-magnitude treatment is worse when α = 0 simply because less total

<a id='6169098f-14e3-44ab-ab60-d453a315d532'></a>

TABLE 1. Parameters Used For Comparison of Treatment Efficacy for Phenotype-
Preserving Drugs and Resistance-Inducing Drugs
<table id="5-1">
<tr><td id="5-2">Parameter</td><td id="5-3">Biologic Interpretation</td><td id="5-4">Value (dimensionless)</td></tr>
<tr><td id="5-5">S₀</td><td id="5-6">Initial sensitive population</td><td id="5-7">0.01</td></tr>
<tr><td id="5-8">R₀</td><td id="5-9">Initial resistant population</td><td id="5-a">0</td></tr>
<tr><td id="5-b">Vd</td><td id="5-c">Detectable tumor volume</td><td id="5-d">0.1</td></tr>
<tr><td id="5-e">Vc</td><td id="5-f">Tumor volume defining treatment failure</td><td id="5-g">0.9</td></tr>
<tr><td id="5-h">ε</td><td id="5-i">Background mutation rate</td><td id="5-j">10-6</td></tr>
<tr><td id="5-k">d</td><td id="5-l">Cytotoxicity of sensitive cells</td><td id="5-m">1</td></tr>
<tr><td id="5-n">Pr</td><td id="5-o">Resistant growth fraction</td><td id="5-p">0.2</td></tr>
<tr><td id="5-q">Uon</td><td id="5-r">Treatment magnitude, constant dose</td><td id="5-s">1.5</td></tr>
<tr><td id="5-t">Aton</td><td id="5-u">Pulsed treatment window</td><td id="5-v">1</td></tr>
<tr><td id="5-w">Δtoff</td><td id="5-x">Pulsed holiday length</td><td id="5-y">3</td></tr>
</table>
NOTE. Parameters used in Figure 2.

<a id='e11c2876-49ad-4dec-b420-1334cbcd6fc9'></a>

drug—that is, AUC—is applied. However, we see that even in this case, intermediate doses may be optimal (Figs 3A and 4A). Thus, it is not the larger total drug, per se, that is responsible for the superiority of the constant protocol in this case, a point that is reinforced by the fact that the results remain qualitatively unchanged even if the total drug is controlled for (Appendix).

<a id='972062a3-e92e-491a-be24-88c3293dfe28'></a>

Compare this with Figures 2C and 2D, which consider the same patient and cytotoxicity, but for a highly inductive drug. Results are strikingly different and suggest that pulsed therapy is now not worse but in fact substantially improves patient response (t ≈ 61 for pulsed, compared with t ≈ 45 for constant). In this case, both tumors are now primarily resistant (Figs A3B and A3D), but the pulsed therapy allows for prolonged tumor control via sensitive/resistant competitive inhibition. Furthermore, treatment holidays reduce the overall flux into resistance as the application of the drug itself promotes this evolution. The total amount of drug (AUC) is also less for pulsed therapy (22.5 compared with ≈ 64), so that pulsed therapy is both more efficient in terms of treatment efficacy and less toxic to the patient as adverse effects are typically correlated with the total administered dose, which is proportional to the AUC. This is further consistent with recent experimental and clinical evidence that supports metronomic therapy as a superior alternative to classic chemotherapy regimens. The results presented in Figure 2 suggest that it may be advantageous to apply a smaller amount of drug more frequently; however, we also note that the results depend on patient-specific parameters, so that therapy would ideally be personalized to individual patients. Of note, we do not claim that these results hold for all parameter values—both patient and treatment specific—but instead emphasize that the rate of induction may play a large role in the design of therapies for specific patients.

<a id='27bdd12c-bd73-4505-be7a-1150a92cfabd'></a>

For these specific parameter values, differences between constant and pulsed therapy for the inductive drug are not as extensive as in the phenotype-preserving case; however, recall that time has been nondimensionalized and, hence, the scale may indeed be clinically relevant. Such differences can be further amplified, and, as exact parameters are difficult or even (currently) impossible to measure, qualitative distinctions are paramount. Thus, at this stage, ranking of therapies, rather than their precise quantitative efficacy, should act as the more important clinical criterion.

<a id='84e54db2-abe7-4057-90d8-ba3b6d6c279d'></a>

From these results, we observe a qualitative difference in the treatment strategy to apply based entirely on the value of α, the degree to which the drug itself induces resistance. Thus, in administering chemotherapy, the resistance-promotion rate α of the treatment is a clinically significant parameter. In the next section, we use our model and its output to propose in vitro methods for experimentally measuring a drug's α parameter.

<a id='8639f181-9ce2-420b-8f39-960136174335'></a>

6  2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='32ddb2b7-515b-44f2-9f1a-e10eb1ca02b9'></a>

Differentiating Spontaneous and Induced Resistance

<a id='89422092-6c0a-416c-afd8-37bbbfa6c4fc'></a>

<::A composite figure consisting of four line graphs (A, B, C, D) arranged in a 2x2 grid. The x-axis for all graphs is 'Time'.

**Graph A: Treatment Strategies, α = 0**
- Y-axis: 'u', ranging from 0 to 1.6.
- X-axis: 'Time', ranging from 0 to 80.
- Two lines are plotted: 'Constant' (blue) and 'Pulsed' (gray).
- The 'Constant' blue line is flat at approximately u = 1.5.
- The 'Pulsed' gray line shows periodic pulses from u = 0 to u = 1.5, occurring for short durations at regular intervals up to around Time = 15, after which it remains at u = 0.

**Graph B: Tumor Dynamics, α = 0**
- Y-axis: 'Tumor Volume S + R', ranging from 0 to 1.
- X-axis: 'Time', ranging from 0 to 80.
- A dashed red line is present at 'Tumor Volume S + R' = 0.9.
- Two lines are plotted: 'Constant' (blue) and 'Pulsed' (gray).
- The 'Constant' blue line starts near 0, stays low for a prolonged period, then increases sharply, crossing the 0.9 dashed line around Time = 85.
- The 'Pulsed' gray line exhibits oscillatory behavior, initially rising and falling sharply, then settling near 0, followed by another period of oscillation and a sharp increase, crossing the 0.9 dashed line around Time = 15, and then falling again, showing complex dynamics.

**Graph C: Treatment Strategies, α = 10⁻²**
- Y-axis: 'u', ranging from 0 to 1.6.
- X-axis: 'Time', ranging from 0 to 60.
- Two lines are plotted: 'Constant' (blue) and 'Pulsed' (gray).
- The 'Constant' blue line is flat at approximately u = 1.5.
- The 'Pulsed' gray line shows periodic pulses from u = 0 to u = 1.5, occurring for short durations at regular intervals throughout the entire time range up to Time = 60.

**Graph D: Tumor Dynamics, α = 10⁻²**
- Y-axis: 'Tumor Volume S + R', ranging from 0 to 1.
- X-axis: 'Time', ranging from 0 to 60.
- A dashed red line is present at 'Tumor Volume S + R' = 0.9.
- Two lines are plotted: 'Constant' (blue) and 'Pulsed' (gray).
- The 'Constant' blue line starts near 0, stays low for a period, then gradually increases, crossing the 0.9 dashed line around Time = 45.
- The 'Pulsed' gray line exhibits oscillatory behavior, repeatedly rising and falling, generally staying below the 0.9 dashed line, but with its baseline gradually increasing towards 0.9 by Time = 60.::>

<a id='d47709c3-cf7d-48ef-8e7d-3de3be5b6927'></a>

FIG 2. Comparison of treatment efficacy for phenotype-preserving drugs (a = 0) and resistance-inducing drugs (a = 10-2). The left column indicates treatment strategy, whereas the right column indicates corresponding tumor volume response. Note that the dashed red line in the right column indicates the tumor volume representing treatment failure, Vc. (A) Constant and pulsed therapies after tumor detection for a = 0. (B) Responses corresponding to treatment regimens in panel A. (C) Constant and pulsed therapies after tumor detection for a = 10-2. (D) Responses corresponding to treatment regimens in panel C.

<a id='97ff6d3d-c0de-40e4-8325-482676a26a34'></a>

### Identifying the Rate of Induced Drug Resistance
The effect of treatment on the evolution of phenotypic resistance may have a significant impact on the efficacy of conventional therapies. Thus, it is essential to understand the value of the induction parameter \alpha before administering therapy. In this section, we briefly discuss both the theoretical possibility and practical feasibility of determining \alpha from different input strategies _u_(_t_). For more details, see the Appendix.

<a id='620a1611-55b8-456c-a9d7-6c238af17c16'></a>

## Theoretical Identifiability
We first study the structural identifiability of Equations 4 and 5, a prerequisite for analyzing practical methods for determining parameter values. Structural identifiability is the process of determining model parameters—for example, α—from a set of control experiments. Here, we assume that the only measurable quantity is the tumor volume V= S + R, along with its derivatives, in time. Using four different controls, we show that all model parameters, including the induction rate α,

<a id='758a3613-508d-4feb-a3f0-f4b59ded6dd0'></a>

JCO Clinical Cancer Informatics

<a id='2ec77fc5-8465-4735-a465-1c3c8dfacd95'></a>

7

<!-- PAGE BREAK -->

<a id='03f7a965-2d7d-40f3-ae85-1643a8087118'></a>

Greene, Gevertz, and Sontag

<a id='25bb133e-a972-4eea-be14-0f59e8b58430'></a>

may be determined by precisely measuring the corre- sponding volume-response curves. For more details, see the Appendix.

<a id='bc36a585-8aef-4b62-a957-ca471f8de215'></a>

**An In Vitro Experimental Protocol to Distinguish Spontaneous and Drug-Induced Resistance**As structural identifiability was established in the previous section, we focus on practical qualitative differences exhibited by Equations 4 and 5 as a function of the resistance-induction rate α. Utilizing only constant dosages, we investigate the dependence of t_c on dose u, cytotoxicity d, and α. Defining the supremum over doses of the response time (Eq 8),

<a id='162cce61-0d2b-4a54-89c3-60dd8a2ea2aa'></a>

T_\alpha(d) := \sup_u\{t_c(u, d, \alpha)\}, (9)

<a id='ba12121a-6af8-4e56-bc10-4a320013336d'></a>

we plot the results for different α values in Figures 3 and 4. Comparing Figures 3B and 4B, we observe a clear qualitative difference in maximum response times. In the case of a phenotype-preserving drug, the proposed in vitro experiment would produce a flat curve, whereas a resistance-inducing drug (α > 0) would yield an increasing function Tα (d). Additional comparisons are presented in Figure 5, where the α dependence is more closely analyzed. For more details and analysis, see the Appendix.

<a id='bd401575-68c7-4415-ba51-259befd4e788'></a>

## DISCUSSION
In the current work, we analyzed two distinct mechanisms that can result in drug resistance. Specifically, a mathematical model is proposed which describes both the spontaneous generation of resistance and drug-induced resistance. Using this model, we contrasted the effect of

<a id='3741f712-6789-40ff-93cb-4450ab5ad873'></a>

standard therapy protocols and demonstrate that contrary to the work in Liu et al, 34 the rate of resistance induction may have a significant effect on treatment outcome. Thus, understanding the dynamics of resistance evolution with regard to the applied therapy is crucial.

<a id='10a4dd06-3318-42f1-9da3-d891349d079a'></a>

To demonstrate that one can theoretically determine the induction rate, we performed an identifiability analysis on the parameter α and demonstrated that it can be obtained via a set of appropriate perturbation experiments on u(t).
Furthermore, we presented an alternative method, using only constant therapies, for understanding the qualitative differences between purely spontaneous and induced cases. Such properties could possibly be used to design in vitro experiments on different pharmaceuticals, which allows one to determine the induction rate of drug resistance without an a priori understanding of the precise mechanism. We do note, however, that such experiments may still be difficult to perform in a laboratory environment, as engineering cells with various drug sensitivities d may be challenging. Indeed, this work can be considered as a thought experiment to identify qualitative properties that the induction rate α yields in our modeling framework.

<a id='bc39903c-e4d1-4210-ad99-f8a349571d2f'></a>

Our simple model allows significant insight into the role of random versus induced resistance. Of course, more elaborate models can be studied by incorporating more biologic detail. For example, while our two-equation model classifies cells as either sensitive or resistant, not all resistance is treated equally. Some resistant cancer cells are permanently resistant, whereas others could transition back to a sensitive state.41 This distinction may prove to be vitally important in treatment design. A possible extension

<a id='f803e984-5907-4d5f-a865-e548cb73d2a9'></a>

<::transcription of the content: chart::>FIG 3. Variation in response time t_c for a treatment that induces resistance. Constant therapy u(t) = u is applied for t_d <= t <= t_c. Induction rate α = 10⁻², with all other parameters as in Table 1. (A) Time until tumor reaches critical size V_c for various drug sensitivities d. This panel shows a line graph titled "Constant Therapy Dose Response, α = 10⁻²". The y-axis is labeled "t_c" and ranges from 0 to 160. The x-axis is labeled "u" and ranges from 0 to 5. There are five lines plotted, representing different values of d: - d = 0.1 (gray solid line) - d = 0.2 (blue dashed line) - d = 0.95 (teal dash-dot line) - d = 1.45 (red dotted line) - d = 2.95 (purple solid line). (B) Maximum response time Tα(d) for a treatment that induces resistance. Note that time Tα(d) increases with drug sensitivity; compare with Figure 4B for purely random resistance evolution. This panel shows a line graph titled "Maximum Critical Time as a Function of Sensitivity, α = 10⁻²". The y-axis is labeled "Tα(d)" and ranges from 0 to 160. The x-axis is labeled "d" and ranges from 0 to 4. A single blue dashed line is plotted, showing an increasing trend of Tα(d) with respect to d.::>

<a id='43a73cd7-4c83-46a8-a341-f5526eb17306'></a>

8 © 2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='fed4c2c8-08de-47e4-a980-3adeb40eac28'></a>

Differentiating Spontaneous and Induced Resistance

<a id='e19d80a4-711e-4e0b-b92b-fa4282c13ea2'></a>

<::figure: FIG 4. Change in critical time $t_c$ for differing drug sensitivities in the case of a phenotype-preserving treatment. (A) Time until tumor reaches critical size $V_c$ for various drug sensitivities $d$; comparable to Figure 3A, with $\alpha = 0$. This plot shows multiple line graphs with the title "Constant Therapy Dose Response, $\alpha = 0$". The y-axis is labeled "$t_c$" and ranges from 0 to 450. The x-axis is labeled "$u$" and ranges from 0 to 5. There are five distinct lines, each representing a different drug sensitivity 'd': a solid gray line for d = 0.1, a dashed blue line for d = 0.2, a dotted teal line for d = 0.95, a dotted red line for d = 1.45, and a solid purple line for d = 2.95. Each line shows a different response curve for $t_c$ as a function of $u$. (B) Maximum critical time $T_0(d)$. Note that the curve is essentially constant. This plot shows a single line graph with the title "Maximum Critical Time as a Function of Sensitivity, $\alpha = 0$". The y-axis is labeled "$T_0$" and ranges from 0 to 450. The x-axis is labeled "$d$" and ranges from 0 to 3. A single, mostly flat gray line is plotted, indicating that $T_0$ remains relatively constant across the range of $d$.::>

<a id='c29bd685-3c38-4a75-96ab-a26b7d790fa5'></a>

of our model is one in which we distinguish between
sensitive cells S, nonreversible resistant cells R_n, and re-
versible resistant cells R_r (Eqs 9-12):

<a id='8b2ecbd0-514a-4f09-bfde-ca97cf1e22fa'></a>

$$\frac{dS}{dt} = r\left(1 - \frac{V}{K}\right)S - (\epsilon_n + \epsilon_r)S - (\alpha_n + \alpha_r)u(t)S - du(t)S + \gamma R_r, \quad (10)$$

<a id='be6d3f86-5b76-47a1-a52e-38ca6f6c4ac4'></a>

$$\frac{dR_n}{dt} = r_n\left(1 - \frac{V}{K}\right)R_n + \epsilon_n S + \alpha_n u(t) S - d_n u(t) R_n, \quad (11)$$

<a id='598e325c-6ac6-4bfe-9c69-50c994694b13'></a>

dRr / dt = rr (1 - V/K) Rr + εr S + αr u(t) S - γ Rr - dr u(t) Rr.

(12)

<a id='e2390e14-8554-423d-bcde-1fa5379e5523'></a>

Here, _V_ denotes the entire tumor population—that is,

_V_ := _S_ + _R_n + _R_r. (13)

<a id='fc07dab2-9ec5-405f-bb8a-87747e12c4b7'></a>

In this version of the model, nonreversible resistant cells R_n
can be thought of as resistant cells that form via genetic
mutations. Under this assumption, ε_n represents the rate at
which spontaneous genetic mutations give rise to re-
sistance, and α_n is the drug-induced resistance rate. This
situation can be classified as nonreversible as it is in-
credibly unlikely that genomic changes that occur in re-
sponse to treatment would be reversed by an "undoing"
mutation. Therefore, once cells confer a resistant pheno-
type via an underlying genetic change, we assume that they
maintain that phenotype. This term could also be thought of
as describing resistance that forms via stable epigenetic

<a id='6bb5cfa7-0ef1-4647-97ac-36da15eafd84'></a>

alterations or resistance that forms by some combination of genetic and stable epigenetic changes.

<a id='266404f1-4b0c-43d7-8ffa-c2b0f2820ccb'></a>

Conversely, reversible resistant cells R_r denote resistant cells that form via phenotype switching, as described in Pisco et al.⁴¹ Random phenotype switching in the absence of treatment is captured in the ε_rS term. This is consistent—and indeed necessary—to understand the experimental results in Pisco et al,⁴¹ where a stable distribution of MDR1 expressions is observed even in the absence of treatment. The α_r u(t)S term represents the induction of a drug-resistant phenotype. Phenotype switching is often reversible, and therefore we allow a back transition from the R_r compartment to the sensitive compartment at a nonnegligible rate γ⁷⁰ (see Appendix). Formulated in this way, the model can be calibrated to experimental data and we can further consider the effects of the dosing strategy on treatment response. We plan to further study this model in future work.

<a id='6c4e03cf-92cb-4052-9cbe-4dc202b90f8d'></a>

Other extensions which include different clinical scenarios
are also being investigated. In practice, chemotherapies are
rarely applied in isolation. Multiple therapies are often
administered simultaneously to improve efficacy. The in-
clusion of multiple drugs, including targeted therapies that
act primarily on resistant subpopulations, yields natural
control questions that are clinically relevant. Similarly,
immune cells, together with immunotherapies, may also be
incorporated to more accurately mimic the cancer
microenvironment.

<a id='8cd0cfdc-1994-4ce1-972b-8fd75371a1fd'></a>

Overcoming drug resistance is crucial for the success of both chemotherapy and targeted therapy. Furthermore, the added complexity of induced drug resistance complicates

<a id='99b300db-5be8-426e-8c26-9e36a972a16f'></a>

JCO Clinical Cancer Informatics

<a id='e564054f-17d7-4157-a269-745de1c33a5b'></a>

9

<!-- PAGE BREAK -->

<a id='1df8f8f1-9dde-444f-a6ca-637c262c5c41'></a>

Greene, Gevertz, and Sontag

<a id='927adfb0-c153-4cf1-af7f-4f423925de88'></a>

<::Figure: The image displays two line graphs, labeled A and B, both showing 'Maximum Critical Time for Different Induced Mutation Rates'. Both graphs plot T_α on the y-axis against d on the x-axis, with d ranging from 0 to 2.5. Graph A's y-axis ranges from 20 to 180, while Graph B's y-axis ranges from 0 to 450. Both graphs contain multiple lines, each representing a different value of α (alpha).

Graph A legend:
- α = 5.00e-03 (dashed line)
- α = 6.00e-03 (dotted line)
- α = 7.00e-03 (dash-dot line)
- α = 8.00e-03 (solid line)
- α = 9.00e-03 (dashed line)
- α = 1.00e-02 (dotted line)
- α = 1.10e-02 (dash-dot line)
- α = 1.20e-02 (solid line)
- α = 1.30e-02 (dashed line)
- α = 1.40e-02 (dotted line)
- α = 1.50e-02 (dash-dot line)

Graph B legend:
- α = 0 (dashed line)
- α = 10^-6 (dotted line)
- α = 10^-5 (dash-dot line)
- α = 10^-4 (solid line)
- α = 10^-3 (dashed line)
- α = 10^-2 (dotted line)
- α = 10^-1 (dash-dot line)

In both graphs, T_α generally increases with d. In Graph A, the lines are relatively close, showing an increasing trend with varying slopes. In Graph B, the lines show a wider spread, with higher α values generally leading to higher T_α values and some curves flattening out at higher d values.::>

<a id='cca0f01f-3938-42a0-ae1b-9861f7eb3b65'></a>

FIG 5. Variation in maximum response time for different induction rates α. For details on computation of Tα(d), see Appendix Figure A4. All other parameters are given as in Table 1. (A) Plot of Tα(d) for α near 10-2. (B) Analogous to panel A, where α is now varied over several orders of magnitude. Nonmutagenic case (α = 0) is included for reference.

<a id='947934c5-e579-40c4-a611-1ae6b5cdad77'></a>

therapy design, as the simultaneous effects of tumor re-
duction and resistance propagation confound one another.
Mathematically, we have presented a clear framework for

<a id='5fd71367-8149-47a5-a530-68829137208b'></a>

## AFFILIATIONS
¹Rutgers University, New Brunswick, NJ
²The College of New Jersey, Ewing Township, NJ
³Northeastern University, Boston, MA
⁴Harvard Medical School, Cambridge, MA

<a id='6b9c20b0-efbc-408f-9bab-15b9c9bbae36'></a>

Preprint version available on https://www.biorxiv.org/content/10.1101/235150v2.

<a id='f683fbe0-8850-4803-a10e-f78b02748c0b'></a>

**CORRESPONDING AUTHOR**
Eduardo D. Sontag, PhD, Northeastern University, 360 Huntington
Avenue, Boston, MA 02115; e-mail: sontag@sontaglab.org.

<a id='2fb909be-dc42-4bb8-b00c-2ba0d80e444f'></a>

AUTHORS' DISCLOSURES OF POTENTIAL CONFLICTS OF INTEREST AND DATA AVAILABILITY STATEMENT
Disclosures provided by the authors and data availability statement (if applicable) are available with this article at DOI https://doi.org/10.1200/CCI.18.00087.

<a id='91e713fb-aed1-47db-b3f9-337f47a2f74c'></a>

differentiating random and drug-induced resistance, which
will allow for clinically actionable analysis on a biologically
subtle, yet important, issue.

<a id='76c1ca04-c347-4dfb-93b1-642f90224b9d'></a>

## AUTHOR CONTRIBUTIONS
Conception and design: All authors
Collection and assembly of data: All authors
Data analysis and interpretation: All authors
Manuscript writing: All authors
Final approval of manuscript: All authors
Accountable for all aspects of the work: All authors

<a id='4cf5e3e6-d4bf-4e10-8a88-19f9da7be827'></a>

AUTHORS' DISCLOSURES OF POTENTIAL CONFLICTS OF INTEREST AND DATA AVAILABILITY STATEMENT
The following represents disclosure information provided by authors of this manuscript. All relationships are considered compensated. Relationships are self-held unless noted. I = Immediate Family Member, Inst = My Institution. Relationships may not relate to the subject matter of this manuscript. For more information about ASCO's conflict of interest policy, please refer to www.asco.org/rwc or ascopubs.org/jco/site/ifc.

<a id='5282c1c8-ffa5-43b0-a82f-f1ab161b3616'></a>

No potential conflicts of interest were reported

<a id='d07c9f1f-b3cd-46ea-bafc-3af1f04a6353'></a>

REFERENCES
1. Holohan C, Van Schaeybroeck S, Longley DB, et al: Cancer drug resistance: An evolving paradigm. Nat Rev Cancer 13:714-726, 2013
2. Gottesman MM: Mechanisms of cancer drug resistance. Annu Rev Med 53:615-627, 2002
3. Dean M, Fojo T, Bates S: Tumour stem cells and drug resistance. Nat Rev Cancer 5:275-284, 2005
4. Woods D, Turchi JJ: Chemotherapy induced DNA damage response: Convergence of drugs and pathways. Cancer Biol Ther 14:379-389, 2013

<a id='84d906e4-586a-4352-a3fe-3429e3d1ddfc'></a>

10 © 2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='e80892cb-43d2-4ecc-afb7-0a843fb8de4f'></a>

Differentiating Spontaneous and Induced Resistance

<a id='b15c4106-0544-4838-8241-3b45e17291a2'></a>

5. Zahreddine H, Borden KL: Mechanisms and insights into drug resistance in cancer. Front Pharmacol 4:28, 2013
6. Trédan O, Galmarini CM, Patel K, et al: Drug resistance and the solid tumor microenvironment. J Natl Cancer Inst 99:1441-1454, 2007
7. Gajewski TF, Meng Y, Blank C, et al: Immune resistance orchestrated by the tumor microenvironment. Immunol Rev 213:131-145, 2006
8. Meads MB, Gatenby RA, Dalton WS: Environment-mediated drug resistance: A major contributor to minimal residual disease. Nat Rev Cancer 9:665-674, 2009
9. Correia AL, Bissell MJ: The tumor microenvironment is a dominant force in multidrug resistance. Drug Resist Updat 15:39-49, 2012
10. McMillin DW, Negri JM, Mitsiades CS: The role of tumour-stromal interactions in modifying drug response: Challenges and opportunities. Nat Rev Drug Discov 12:217-228, 2013
11. Lavi O, Gottesman MM, Levy D: The dynamics of drug resistance: A mathematical perspective. Drug Resist Updat 15:90-97, 2012
12. Brocato T, Dogra P, Koay EJ, et al: Understanding drug resistance in breast cancer with mathematical oncology. Curr Breast Cancer Rep 6:110-120, 2014
13. Foo J, Michor F: Evolution of acquired resistance to anti-cancer therapy. J Theor Biol 355:10-20, 2014
14. Roche-Lestienne C, Preudhomme C: Mutations in the ABL kinase domain pre-exist the onset of imatinib treatment. Semin Hematol 40:80-82, 2003 (suppl 2)
15. Iqbal Z, Aleem A, Iqbal M, et al: Sensitive detection of pre-existing BCR-ABL kinase domain mutations in CD34+ cells of newly diagnosed chronic-phase chronic myeloid leukemia patients is associated with imatinib resistance: Implications in the post-imatinib era. PLoS One 8:e55717, 2013
16. Carlino MS, Fung C, Shahheydari H, et al: Preexisting MEK1P124 mutations diminish response to BRAF inhibitors in metastatic melanoma patients. Clin Cancer Res 21:98-105, 2015
17. Jackson TL, Byrne HM: A mathematical model to study the effects of drug resistance and vasculature on the response of solid tumors to chemotherapy. Math Biosci 164:17-38, 2000
18. Komarova NL, Wodarz D: Drug resistance in cancer: Principles of emergence and prevention. Proc Natl Acad Sci USA 102:9714-9719, 2005
19. Michor F, Nowak MA, Iwasa Y: Evolution of resistance to cancer therapy. Curr Pharm Des 12:261-271, 2006
20. Komarova NL, Wodarz D: Stochastic modeling of cellular colonies with quiescence: An application to drug resistance in cancer. Theor Popul Biol 72:523-538, 2007
21. Foo J, Michor F: Evolution of resistance to targeted anti-cancer therapies during continuous and pulsed administration strategies. PLOS Comput Biol 5:e1000557, 2009 [Erratum: PLoS Comput Biol doi:10.1371/annotation/d5844bf3-a6ed-4221-a7ba-02503405cd5e]
22. Foo J, Michor F: Evolution of resistance to anti-cancer therapy during general dosing schedules. J Theor Biol 263:179-188, 2010
23. Silva AS, Gatenby RA: A theoretical quantitative model for evolution of cancer chemotherapy resistance. Biol Direct 5:25, 2010
24. Cunningham JJ, Gatenby RA, Brown JS: Evolutionary dynamics in cancer therapy. Mol Pharm 8:2094-2100, 2011
25. Mumenthaler SM, Foo J, Leder K, et al: Evolutionary modeling of combination treatment strategies to overcome resistance to tyrosine kinase inhibitors in non-small cell lung cancer. Mol Pharm 8:2069-2079, 2011
26. Orlando PA, Gatenby RA, Brown JS: Cancer treatment as a game: Integrating evolutionary game theory into the optimal control of chemotherapy. Phys Biol 9:065007, 2012
27. Bozic I, Reiter JG, Allen B, et al: Evolutionary dynamics of cancer in response to targeted combination therapy. eLife 2:e00747, 2013
28. Foo J, Leder K, Mumenthaler SM: Cancer as a moving target: understanding the composition and rebound growth kinetics of recurrent tumors. Evol Appl 6:54-69, 2013
29. Lavi O, Greene JM, Levy D, et al: The role of cell density and intratumoral heterogeneity in multidrug resistance. Cancer Res 73:7168-7175, 2013
30. Bozic I, Nowak MA: Timing and heterogeneity of mutations associated with drug resistance in metastatic cancers. Proc Natl Acad Sci USA 111:15964-15968, 2014
31. Greene J, Lavi O, Gottesman MM, et al: The impact of cell density and mutations in a model of multidrug resistance in solid tumors. Bull Math Biol 76:627-653, 2014
32. Yamamoto KN, Hirota K, Takeda S, et al: Evolution of pre-existing versus acquired resistance to platinum drugs and PARP inhibitors in BRCA-associated cancers. PLoS One 9:e105724, 2014
33. Gevertz J, Aminzare Z, Norton K-A, et al: Emergence of anti-cancer drug resistance: exploring the importance of the microenvironmental niche via a spatial model, in Jackson T and Radunskaya A (eds): Applications of Dynamical Systems in Biology and Medicine, Volume 158, Berlin, Germany, Springer-Verlag, 2015, pp 1-34
34. Liu LL, Li F, Pao W, et al: Dose-dependent mutation rates determine optimum erlotinib dosing strategies for EGRF mutant non-small lung cancer patients. PLoS One 10:e0141665, 2015
35. Menchón SA: The effect of intrinsic and acquired resistances on chemotherapy effectiveness. Acta Biotheor 63:113-127, 2015
36. Mumenthaler SM, Foo J, Choi NC, et al: The impact of microenvironmental heterogeneity on the evolution of drug resistance in cancer cells. Cancer Inform 14:19-31, 2015 (suppl 4)
37. Waclaw B, Bozic I, Pittman ME, et al: A spatial model predicts that dispersal and cell turnover limit intratumour heterogeneity. Nature 525:261-264, 2015
38. Shah AB, Rejniak KA, Gevertz JL: Limiting the development of anti-cancer drug resistance in a spatial model of micrometastases. Math Biosci Eng 13:1185-1206, 2016
39. Carrère C: Optimization of an in vitro chemotherapy to avoid resistant tumours. J Theor Biol 413:24-33, 2017
40. Chakrabarti S, Michor F: Pharmacokinetics and drug-interactions determine optimum combination strategies in computational models of cancer evolution. Cancer Res 77:3908-3921, 2017
41. Pisco AO, Brock A, Zhou J, et al: Non-Darwinian dynamics in therapy-induced cancer drug resistance. Nat Commun 4:2467, 2013
42. Coldman AJ, Goldie JH: A stochastic model for the origin and treatment of tumors containing drug-resistant cells. Bull Math Biol 48:279-292, 1986
43. Ledzewicz U, Schättler H: Drug resistance in cancer chemotherapy as an optimal control problem. Discrete Continuous Dyn Syst Ser B 5:129-150, 2006
44. Leder K, Foo J, Skaggs B, et al: Fitness conferred by BCR-ABL kinase domain mutations determines the risk of pre-existing resistance in chronic myeloid leukemia. PLoS One 6:e27682, 2011
45. Hadjiandreou MM, Mitsis GD: Mathematical modeling of tumor growth, drug-resistance, toxicity, and optimal therapy design. IEEE Trans Biomed Eng 61:415-425, 2014
46. Lorz A, Lorenzi T, Hochberg M, et al: Populational adaptive evolution, chemotherapeutic resistance and multiple anti-cancer therapies. ESAIM: Math Model Num Anal 47:377-399, 2013
47. Fu F, Nowak MA, Bonhoeffer S: Spatial heterogeneity in drug concentrations can facilitate the emergence of resistance to cancer therapy. PLOS Comput Biol 11:e1004142, 2015
48. Ledzewicz U, Bratton K, Schättler H: A 3-compartment model for chemotherapy of heterogeneous tumor populations. Acta Appl Math 135:191-207, 2015

<a id='2ef4f351-24c4-4e61-8742-1247e0feb8f6'></a>

JCO Clinical Cancer Informatics

<a id='37a13041-2035-4d76-a4f7-66a4a7a8688b'></a>

11

<!-- PAGE BREAK -->

<a id='d894d513-d570-471b-9e93-26e28b0b48ab'></a>

Greene, Gevertz, and Sontag

<a id='64e8e7b0-32ea-4eea-aca5-273ae536bb0c'></a>

49. Lorz A, Lorenzi T, Clairambault J, et al: Modeling the effects of space structure and combination therapies on phenotypic heterogeneity and drug resistance in solid tumors. Bull Math Biol 77:1-22, 2015
50. Nyce J, Leonard S, Canupp D, et al: Epigenetic mechanisms of drug resistance: Drug-induced DNA hypermethylation and drug resistance. Proc Natl Acad Sci USA 90:2960-2964, 1993
51. Nyce JW: Drug-induced DNA hypermethylation: A potential mediator of acquired drug resistance during cancer chemotherapy. Mutat Res 386:153-161, 1997
52. Sharma SV, Lee DY, Li B, et al: A chromatin-mediated reversible drug-tolerant state in cancer cell subpopulations. Cell 141:69-80, 2010
53. Luria SE, Delbrück M: Mutations of bacteria from virus sensitivity to virus resistance. Genetics 28:491-511, 1943
54. Szikriszt B, Póti Á, Pipek O, et al: A comprehensive survey of the mutagenic impact of common cancer cytotoxics. Genome Biol 17:99, 2016
55. Swift LH, Golsteyn RM: Genotoxic anti-cancer agents and their relationship to DNA damage, mitosis, and checkpoint adaptation in proliferating cancer cells. Int J Mol Sci 15:3403-3431, 2014
56. Shaffer SM, Dunagin MC, Torborg SR, et al: Rare cell variability and drug-induced reprogramming as a mode of cancer drug resistance. Nature 546:431-435, 2017
57. Housman G, Byler S, Heerboth S, et al: Drug resistance in cancer: An overview. Cancers (Basel) 6:1769-1792, 2014
58. Pisco AO, Huang S: Non-genetic cancer cell plasticity and therapy-induced stemness in tumour relapse: 'What does not kill me strengthens me'. Br J Cancer 112:1725-1732, 2015
59. Goldman A, Majumder B, Dhawan A, et al: Temporally sequenced anticancer drugs overcome adaptive resistance by targeting a vulnerable chemotherapy-induced phenotypic transition. Nat Commun 6:6139, 2015
60. Chapman M, Risom T, Aswani A, et al: A model of phenotypic state dynamics initiates a promising approach to control heterogeneous malignant cell populations. IEEE 55th Conference on Decision and Control, Las Vegas, NV, December 12-14, 2016 (abstr)
61. Axelrod DE, Vedula S, Obaniyi J: Effective chemotherapy of heterogeneous and drug-resistant early colon cancers by intermittent dose schedules: A computer simulation study. Cancer Chemother Pharmacol 79:889-898, 2017
62. Feizabadi MS: Modeling multi-mutation and drug resistance: Analysis of some case studies. Theor Biol Med Model 14:6, 2017
63. Chisholm RH, Lorenzi T, Lorz A, et al: Emergence of drug tolerance in cancer cell populations: An evolutionary outcome of selection, nongenetic instability, and stress-induced adaptation. Cancer Res 75:930-939, 2015
64. Perez-Velazquez J, Gevertz J, Karolak A, et al: Microenvironmental niches and sanctuaries: A route to acquired resistance, in Rejniak K (ed): Systems Biology of Tumor Microenvironment, Volume 936, New York, NY, Springer, 2016, 149-164
65. Kerbel RS, Kamen BA: The anti-angiogenic basis of metronomic chemotherapy. Nat Rev Cancer 4:423-436, 2004
66. Pasquier E, Kavallaris M, André N: Metronomic chemotherapy: New rationale for new directions. Nat Rev Clin Oncol 7:455-465, 2010
67. Gatenby RA, Silva AS, Gillies RJ, et al: Adaptive therapy. Cancer Res 69:4894-4903, 2009
68. Ghiringhelli F, Menard C, Puig PE, et al: Metronomic cyclophosphamide regimen selectively depletes CD4+CD25+ regulatory T cells and restores T and NK effector functions in end stage cancer patients. Cancer Immunol Immunother 56:641-648, 2007
69. Kareva I, Waxman DJ, Lakka Klement G: Metronomic chemotherapy: An attractive alternative to maximum tolerated dose therapy that can activate anti-tumor immunity and minimize therapeutic resistance. Cancer Lett 358:100-106, 2015
70. Lee W-P: The role of reduced growth rate in the development of drug resistance of HOB1 lymphoma cells to vincristine. Cancer Lett 73:105-111, 1993
71. Shackney SE, McCormack GW, Cuchural GJ Jr: Growth rate patterns of solid tumors and their relation to responsiveness to therapy: An analytical review. Ann Intern Med 89:107-121, 1978
72. Brimacombe KR, Hall MD, Auld DS, et al: A dual-fluorescence high-throughput cell line system for probing multidrug resistance. Assay Drug Dev Technol 7:233-249, 2009
73. Thomas H, Coley HM: Overcoming multidrug resistance in cancer: An update on the clinical strategy of inhibiting p-glycoprotein. Cancer Contr 10:159-165, 2003
74. Loeb LA, Springgate CF, Battula N: Errors in DNA replication as a basis of malignant changes. Cancer Res 34:2311-2321, 1974
75. Krutyakov V: Eukaryotic error-prone DNA polymerases: The presumed roles in replication, repair, and mutagenesis. Mol Biol 40:1-8, 2006
76. Makridakis NM, Reichardt JK: Translesion DNA polymerases and cancer. Front Genet 3:174, 2012
77. Lange SS, Takata K, Wood RD: DNA polymerases and cancer. Nat Rev Cancer 11:96-110, 2011
78. Traina TA, Norton L: Log-kill hypothesis, in Schwab M (ed): Encyclopedia of Cancer. Springer, Berlin, Germany, 2011, pp 1713-1714
79. Bender BC, Schindler E, Friberg LE: Population pharmacokinetic-pharmacodynamic modelling in oncology: A tool for predicting clinical response. Br J Clin Pharmacol 79:56-71, 2015
80. Wu Q, Li MY, Li HQ, et al: Pharmacokinetic-pharmacodynamic modeling of the anticancer effect of erlotinib in a human non-small cell lung cancer xenograft mouse model. Acta Pharmacol Sin 34:1427-1436, 2013
81. Fetterly GJ, Aras U, Lal D, et al: Development of a preclinical PK/PD model to assess antitumor response of a sequential aflibercept and doxorubicin-dosing strategy in acute myeloid leukemia. AAPS J 15:662-673, 2013
82. Erdi YE: Limits of tumor detectability in nuclear medicine and pet. Mol Imaging Radionucl Ther 21:23-28, 2012
83. Jodrell DI, Egorin MJ, Canetta RM, et al: Relationships between carboplatin exposure and tumor response and toxicity in patients with ovarian cancer. J Clin Oncol 10:520-528, 1992
84. Chignola R, Foroni RI: Estimating the growth kinetics of experimental tumors from as few as two determinations of tumor size: Implications for clinical oncology. IEEE Trans Biomed Eng 52:808-815, 2005

<a id='aac0bfbc-ba8e-477d-b2a1-38197fc5a0ba'></a>

12 © 2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='9d26a7ff-db32-483b-acbc-a3d6af84b7fd'></a>

Differentiating Spontaneous and Induced Resistance

<a id='ee565eb1-8d70-4805-99f2-f667af0ce917'></a>

## APPENDIX
The supplement contains additional results and extensions related to the model Equations 1 and 2 presented in the main text. Sections include details on the mathematical characteristics of solutions of Equations 4 and 5, an extension describing the reversibility of drug resistance, treatment regimens with normalized dosages, details on structural identifiability, and an expanded discussion on the maximum critical time Tα(d).

<a id='d51eadbc-b8c6-435d-b5a2-2186ca41aee7'></a>

**Fundamental Solution Properties of Resistance Model**
For convenience, Equations 4 and 5 are reproduced below:

dS/dt = (1 - (S + R))S - (ε + αu(t))S - du(t)S, (A1)

<a id='e1a86d96-65e4-442f-82a3-ac7ce9a8817e'></a>

dR/dt = p_r(1-(S+R))R + (ε + αu(t))S (A2)

<a id='0137cd6d-a903-401c-9846-29842194c11d'></a>

We begin with a standard existence/uniqueness result, as well as the dynamical invariance of the triangular region:

<a id='1b223218-73d9-46f9-ac49-15b0a3caef85'></a>

T := {(S, R)|S ≥ 0, R ≥ 0, S + R ≤ 1}. (A3)

<a id='86903dbd-f308-4ca1-905f-f93feaeb43c8'></a>

Note that T represents the region of non-negative tumor sizes less than
1. Biologically, this implies that all solutions remain physical (non-
negative) and bounded above by the carry capacity (non-
dimensionalized to 1 here, generally K in Eqs 1 and 2).

<a id='952cc813-e5c5-4d22-884a-fbe8e186d889'></a>

Theorem 1. For any bounded measurable control u: [0,∞) → [0, u_max], with u_max < ∞, and (S_0, R_0) ∈ T, the initial value problem Equations Al and A2,

<a id='0de8aa2c-6e32-43d7-ab5d-cb6e1e0366c1'></a>

S(0) = S₀, R(0) = R₀,

<a id='6bd1f1c6-a16c-4c93-9869-52b2c2fa257a'></a>

has a unique solution [S(t), R(t)] defined for all times t ∈ R. Furthermore, under the prescribed dynamics, region T is invariant.

<a id='8452f627-a815-4cea-a232-c7e51f085d09'></a>

_Proof._ Existence and uniqueness of local solutions follow from standard results in the theory of differential equations—for example (Sontag ED: Mathematical Control Theory: Deterministic Finite Dimensional Systems. Springer, 1998). As the vector field

<a id='4b149af4-986d-4739-8721-add6a406af11'></a>

F(S, R, t) := \begin{pmatrix} (1 - (S + R))S - (\epsilon + \alpha u(t))S - du(t)S \\ p_r(1 - (S + R))R + (\epsilon + \alpha u(t))S \end{pmatrix}.

<a id='f1b4608b-dbcc-4e51-b9dd-750ce01578bc'></a>

is analytic for (S, R) ∈ R², the existence of maximal solutions defined for all t ∈ R will follow from boundedness (Sontag ED: Mathematical Control Theory: Deterministic Finite Dimensional Systems. Springer, 1998), which we demonstrate below.

<a id='f8132d80-b6e6-4920-a704-c579e63a60fd'></a>

Uniqueness implies that solutions remain in the first quadrant for all t≥0. Indeed, we first note that (0, 0) and (0,1) are steady states for any control u(t). As S = 0 implies that S = 0, we see that the R-axis in invariant, with R(t)→1 as t→∞. Similarly, R = 0 implies R ≥ 0, and hence all trajectories with (S₀, R₀) ∈ T remain non-negative for all t. As V= S + R satisfies the differential equation

<a id='c8a4e8ce-ea42-444d-8bff-027ec8fd03ca'></a>

V̇ = α(t) (1 − V) − β(t),

<a id='98dcbb0e-fc0a-4916-8669-4a6e875828c0'></a>

where \alpha(t) := S(t) + p_r R(t), \beta(t) := d_u S(t) are both non-negative,
V_0 < 1 \Rightarrow V(t) < 1. Thus, if the initial conditions (S_0, R_0) reside in T, we
are guaranteed that (S(t), R(t)) \in T for all time t, as desired.

<a id='1af9e8f7-0f75-4fd8-8f2b-e4da2d27098b'></a>

We now prove that, asymptotically, cells will evolve to become entirely resistant. For simplicity, we assume that the tumor is initially below carrying capacity, although a similar result holds for V0 > 1.

<a id='273ff5b0-bd9d-44d0-be47-c7367357a73a'></a>

Theorem 2. For any bounded measurable control u: [0,∞) → [0,u_max], with u_max < ∞, and initial conditions (S₀, R₀) ∈ T, solutions of Equations A1 and A2 will approach the steady state (S, R) = (0,1):

<a id='868390ea-96e8-4515-a35b-7043c694d495'></a>

(S(t), R(t)) \xrightarrow{t\to\infty} (0, 1).

Proof. From Theorem 1, we have that 0 \leq S(t) + R(t) \leq 1, so that
Equation A2 implies

<a id='d9208f17-d461-45fe-a204-12c70ef3b77d'></a>

dR/dt ≥ 0.

<a id='a719bacf-026a-45e2-9292-6733ecc8f6b8'></a>

As 0 \le R(t) \le S(t) + R(t) \le 1, R(t) must converge, so that there exists
0 \le R_* \le 1 such that

R(t) \xrightarrow{t\to\infty} R_*

<a id='1c55e7bc-b714-4eb8-8696-45c0e463ae2a'></a>

Define

ρ := lim inf S(t).
     t→∞

<a id='01a56407-59a0-409b-ac4f-34b9ea8ac1ea'></a>

Since S(t) ∈ [0,1], we know that 0 ≤ ρ ≤ 1. Assume that the inequality is strict on the left: ρ > 0. By definition, there then exists t* > 0 such that

<a id='b0b40a8b-4e8a-42c4-8b0f-b0bbd583be03'></a>

s(t) \ge \frac{\rho}{2},

<a id='3f36786e-9a32-454c-9497-f020b9a7598b'></a>

for all $t \ge t_{*}$. As $S(t) + R(t) \le 1$ for all $t$, Equation A2 implies that for all $t \ge t_{*}$,

<a id='e9125120-a687-443a-be33-c7b985014468'></a>

Ṙ(t) ≥ εS(t) ≥ ερ/2,

<a id='39909891-0f6d-426a-b04e-5e61c505998f'></a>

which implies that

$R(t) - R(t_*) \ge \frac{\epsilon\rho}{2} \int_{t_*}^t ds \to_{t\to\infty} \infty,$

<a id='37e18dfb-fa9c-43e9-bcea-f1925d526eaf'></a>

a contradiction. Thus, ρ = 0.
Define

<a id='9177803d-7797-467d-bf05-56a902d5bdae'></a>

σ := lim inf(S(t) + R(t)).
08-1

<a id='068e296c-1e70-422e-a45f-496af4542acf'></a>

As above, it is clear that σ ∈ [0,1]. Assume that σ < 1. Thus, there exists t*, ε̄ > 0 such that S(t) + R(t) ≤ 1 - ε̄ < 1 for all t ≥ t*. Equation A2 then implies that for all t ≥ t*,

<a id='f946b733-7d77-4816-a673-790c79902faf'></a>

R(t) >= pr(1-(S(t) + R(t)))R > preR,

<a id='fadcd1f4-effd-4ae6-bbc7-9bc4b2f9eaef'></a>

As in the previous argument, this differential inequality contradicts the
boundedness of _R_. Thus, _σ_ = 1.

<a id='786c722c-913e-4ecb-b7ca-4565d86a9af0'></a>

Since R converges to R*, lim inf distributes over the sum of S + R, and we have that

<a id='d852806a-3beb-4316-9234-799bc335eb6c'></a>

1 = \lim_{t \to \infty} \inf(S(t) + R(t)) = \rho + R_*

<a id='690866da-a67c-40ce-b52a-d1e4c65b581d'></a>

Thus $R_* = 1$.
As $R(t) \xrightarrow{t\to\infty} 1$, there exists $t_* > 0$ such that

<a id='3df56683-56ae-4df0-99fe-ec1fc093ebd9'></a>

R(t) ≥ 1 - ε/2

<a id='312ca8a8-a345-4933-81de-d14986cfecfb'></a>

for all $t \geq t'$. For such $t$, Equation A1 implies that $\dot{S}(t) < 0$. Thus, $S$ is eventually decreasing and hence must converge to its $\lim \inf \rho = 0$. Thus, we have that $(S(t), R(t)) \to^{t \to \infty} (0, 1)$, as desired.

<a id='b7c8d7dc-c4f7-4356-8f67-ec5f7d95c87e'></a>

**Reversible Phenotype Switching**
In the model analyzed in this work (Eqs 4 and 5), we assumed that resistance is nonreversible; however, experiments suggestX that phenotypic alterations are generally unstable and hence a non--negligible back transition exists. In this Appendix, we demonstrate that an extension of our model to include this phenomenon does not

<a id='1ef03621-992a-4b14-baa6-93b42970a8f3'></a>

JCO Clinical Cancer Informatics

<a id='38122a68-39cd-4bf3-83e8-26e8f39ef51a'></a>



<!-- PAGE BREAK -->

<a id='c119a6bc-5b52-48a6-b8e2-863327b2396b'></a>

Greene, Gevertz, and Sontag

<a id='dd723cd8-7272-4228-ac2a-1eab50227ac1'></a>

change the qualitative results presented previously, at least for pa- parameter values that are consistent with experimental data.

<a id='59ed0c5e-f9dd-40b4-b193-4525ccf8e0b2'></a>

To model reversible drug resistance, we include a constant per-capita transition rate from the resistant compartment R back to the wild cell-type S. Denoting this rate by γ, we obtain the system

<a id='a8539ed9-72b9-4796-a547-c5aad40a0999'></a>

dS/dt = (1 - (S + R))S + γR - (ε + αu(t))S - du(t)S, (A4)

<a id='6dbc2019-e6cd-41d8-b6f7-24e4e9e2020f'></a>

$$\frac{dR}{dt} = p_r (1-(S+R))R + (\epsilon + \alpha u(t))S - \gamma R. \quad (A5)$$

<a id='d9c8b1b3-19a1-4e02-8696-452df80ba09c'></a>

We first consider an appropriate value of the rate γ. Note that in the
absence of treatment (u(t) = 0), the system becomes

<a id='9431154b-766d-41d6-add8-e3a5adbdb6e7'></a>

dS/dt = (1 - (S + R))S + γR - εS (A6)

<a id='8a7bb5c5-95aa-4b63-85fb-415f0e8e4c82'></a>

$$\frac{dR}{dt} = p_r(1-(S+R))R + \epsilon S - \gamma R. \quad (A7)$$

<a id='36a99bb5-2527-4487-973c-2fd95a01fd8d'></a>

Note that the tumor volume V(t) = S(t) + R(t) satisfies the equation

<a id='8f5342ba-d0c9-4e66-af3b-121eef0e08be'></a>

V̇ = (S + p_r R)(1 - V),

(A8)

<a id='cc04049e-a7c3-4f32-ada0-c4f161f82490'></a>

which is nondecreasing (recall Theorem 1). This implies that the
system approaches a steady state (S*, R*), which can be easily
computed as

<a id='0becc8ce-a848-4de1-925c-54c04d8f8bbb'></a>

(S*, R*) = (γ / (γ + ε), ε / (γ + ε)). (A9)

<a id='fc0f9612-89e3-492d-9c93-f57afbaeadfc'></a>

Note that Equation A9 lies on the line V = 1.
Pisco and colleagues⁵³ measure a 1% to 2% subpopulation of clonally derived HL60 cells that consistently express high levels of MDR1, which we equate with the resistant population R. Using the 2% upper bound, this implies that

<a id='8aa2c0ca-a7a0-4990-a5aa-811bdc36c25d'></a>

S* = 0.98, R* = 0.02. (A10)

<a id='08afa9e5-4960-4c4a-adbd-7ed8ba4966ac'></a>

Solving Equation A9 with the above values then determines the ratio:

γ
— = 49. (A11)
ε

<a id='bb62ecda-80b2-493b-bd20-70fb55651730'></a>

We now repeat the constant versus pulsed experiments discussed in the main text, but for the reversible Equations A4 and A5. Parameter values are taken again as in Table 1, and γ is de- termined via Equation A11. Results are presented in Figure A1 and should be compared with that presented in Figure 2. Note that the same qualitative—and indeed quantitative—conclusions hold: constant therapy improves response time compared with pulsing when α = 0, whereas the reverse is true for α = 10⁻². Thus, the inclusion of instability of the resistant cell subpopulation still suggests that knowledge of the resistance-induction rate α for a chemotherapy is critical when designing therapies. We note that precise agreement of Figures A1 and A2 is a result of the small values taken for ε and hence γ.

<a id='00eda1a2-8bef-4362-8826-57b76bfb6b9d'></a>

**Treatment Comparison for Equal Area Under the Drug Concentration-Time Curve**Here, we provide an analogous comparison of treatment outcomes between constant and pulsed therapy as in the main text; however, treatment magnitudes Uon,c and Uon,p are chosen such that

<a id='9252f6f5-bbbd-4ee7-922f-012905238669'></a>

$$\int_{t_d}^{t_d+\Delta t_{on}+\Delta t_{off}} u_c(t)dt = \int_{t_d}^{t_d+\Delta t_{on}+\Delta t_{off}} u_p(t)dt,$$ (A12)

<a id='b656bf82-8144-4610-adfe-930b0b561a63'></a>

which is equivalent to the conservation of total administered dose between
both strategies over a single pulsing cycle. In Equation A12, u_c(t) and u_p(t)
denote constant and pulsed therapy schedules, respectively. The constant

<a id='b8a77398-59d7-4b49-a26c-eafa4db49472'></a>

therapy magnitude Uon,c is fixed (arbitrarily) at 0.5, which by Equation A12 implies that Uon,p = 5. We also adjust Aton = 0.5, Atoff = 4.5, and all other parameter values remain as in Table 1.

<a id='61477882-0b55-42b3-8914-329096efef48'></a>

Results of the simulations are presented in Figures A2 and A3. Note that here Figure A2 displays the results for the phenotype-preserving drug (α = 0), whereas Figure A3 represents the resistance-inducing drug (α = 10⁻²). Each drug is simulated for the two distinct strategies; each strategy is represented in the left column of the respective figures. The right column illustrates the population response for both the individual populations—sensitive _S_ and resistant _R_ cells—as well as for the total tumor volume _V_ = _S_ + _R_. As previously discussed, treatment is continued until a critical tumor size _V_c is obtained, and the corresponding time _t_c is used as a measure of treatment efficacy, with a larger _t_c indicating a better response.
Our results are qualitatively in agreement with those presented in the main text (Fig 2), where no preservation of total administered drug (area under the drug concentration-time curve) was considered. Specifically, we observe a superior response with constant therapy for the phenotype-preserving drug (α = 0), whereas the situation is reversed for the resistance-inducing drug (α = 10⁻²).

<a id='1f840218-de4f-4ffa-8845-79e96099ea06'></a>

# Identifiability
We provide details of both the structural and practical identifiability of control system Equations A1 and A2. Technical details are provided that do not appear in the main text.

<a id='11ef2d25-d72f-4d9c-ac34-194291e0a88e'></a>

**Theoretical identifiability.** We first show that all parameters in Equations A1 and A2 are identifiable using a relatively small set of controls *u(t)* via classic methods from control theory. We provide a self-contained discussion. For a thorough review of theory and methods, see a recent article (Sontag ED: PLOS Comput Biol 13:e1005447, 2017) and the references therein.

<a id='0999c48a-3f17-4626-a167-94d249ac01ae'></a>

Assuming that time and tumor volume are the only clinically observable outputs—that is, that one cannot readily determine sensitive and resistant proportions in a given population—we measure V(t) and its derivatives at time t = t_d for different controls u(t). For simplicity, we assume that t_d = 0, so that treatment is initiated with a purely wild-type (sensitive) population. Note that this is equivalent to assuming an entirely sensitive tumor at treatment initiation. Although the results remain valid if t_d > 0 as the system of equations gain only a constant, this assumption will simplify the subsequent computations. For a discussion of the practical feasibility of such methods, see the next section.

<a id='4efc81a8-a350-448a-81a4-16ec98e7dada'></a>

Specifically, consider the Equations A1 and A2 with initial conditions (Eqn 7). Measuring V(t) = S(t) + R(t) at time t = 0 implies that we can identify S₀:

<a id='9a5e042b-29ed-447f-a25e-c276d354415c'></a>

V(0) = S(0) + R(0) = S₀ =: Y₀,

<a id='253b5a38-929c-4dc6-951c-a15d42ab94e9'></a>

where we adopt the notation $Y_{i,i} \ge 0$ for measurable quantities.
Similarly, define the following for the given input controls:

$Y_1 := V'(0), u(t) \equiv 0,$
$Y_2 := V(0), u(t) \equiv 1,$
$Y_3 := V(0), u(t) \equiv 0,$
$Y_4 := V'(0), u(t) \equiv 1,$
$Y_5 := V(0), u(t) \equiv 2,$
$Y_6 := V'(0), u(t) \equiv 0,$
$Y_7 := V'(0), u(t) \equiv t.$ (A13)

<a id='609f9a7d-b95b-4ee0-a725-3702a489a83e'></a>

All quantities $Y_i, i = 0, 1,..., 7$ are measurable, as each requires only knowledge of $V(t)$ in a small positive neighborhood of $t = 0$. Note that the set of controls $u(t)$ is relatively simple, with $Y_7$ exclusively determined via a nonconstant input.

<a id='bae8d2d5-9e43-4df5-8556-b9118f9e1841'></a>

Each measurable Y_i may also be written in terms of a subset of the parameters d, \epsilon, p_r, and \alpha, as all derivatives can be calculated in terms of the right sides of Equations A1 and A2. For more details, see the below section. Equating the expressions yields a system of

<a id='bcd6145f-2201-45bd-9be8-f417bc9fa07a'></a>

14  2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='453fbbbf-54c4-4be1-92be-428718e71e2e'></a>

Differentiating Spontaneous and Induced Resistance

<a id='24c35664-bfd5-404a-81aa-f6aafe8b0179'></a>

<::Figure: Two plots side-by-side, labeled A and B, showing treatment strategies and tumor dynamics with α=0. Both plots share a legend indicating 'Constant' (blue line) and 'Pulsed' (gray line) strategies. Both plots have 'Time' on the x-axis, ranging from 0 to 80. A. Treatment Strategies, α=0: The y-axis is labeled 'u', ranging from 0 to 1.6. The 'Constant' line (blue) shows u = 1.5 for the entire duration from Time 0 to 80. The 'Pulsed' line (gray) shows a series of pulses: u is 0, then jumps to 1.5 for a short duration (approximately from Time 1.5-2.5, 3.5-4.5, 5.5-6.5, 7.5-8.5, 9.5-10.5), and is 0 otherwise, remaining at 0 after Time 10. B. Tumor Dynamics, α=0: The y-axis is labeled 'Tumor Volume S + R', ranging from 0 to 1. A dashed red horizontal line is present at Y = 0.9. The 'Constant' line (blue) starts near 0, stays very close to 0 until around Time 60, then increases sharply, reaching 0.9 around Time 87. The 'Pulsed' line (gray) shows an oscillating pattern, starting near 0, increasing rapidly to a peak around 0.85 at Time 5, then fluctuating with multiple peaks and troughs, frequently reaching or exceeding 0.9 after Time 10.::>

<a id='66e43881-52bd-41c8-a2ff-aab886d6a8b7'></a>

C<::A line graph titled "Treatment Strategies, α = 10⁻²". The y-axis is labeled 'u' and ranges from 0 to 1.6. The x-axis is labeled 'Time' and ranges from 0 to 60. The graph displays two data series: "Constant" and "Pulsed". The "Constant" series is represented by a teal horizontal line at u=1.5, starting from Time 0 and extending to approximately Time 45. The "Pulsed" series is represented by gray vertical bars that go from u=0 to u=1.5, appearing intermittently across the x-axis, starting around Time 2 and continuing to Time 60. These pulses have a width of approximately 2 units and a period of about 5 units.: chart::>

<a id='8b764feb-dca6-4f27-8bcf-e55b9458964d'></a>

D
<::chart: Tumor Dynamics, α = 10⁻²

Y-axis: Tumor Volume S + R, ranging from 0.1 to 1.
X-axis: Time, ranging from 0 to 60.

Two lines are plotted:
- Blue line: "Constant" - starts low, increases steadily, crosses the red dashed line around Time = 45.
- Gray line: "Pulsed" - starts low, shows a saw-tooth pattern of rapid increase followed by a drop, generally trending upwards. It reaches the red dashed line multiple times.

A red dashed horizontal line is present at Y = 0.9.::>

<a id='f5e52ef0-5b3a-499f-befc-1b35bef1c9ba'></a>

FIG A1. Comparison of treatment efficacy for phenotype-preserving drugs (\alpha=0) and resistance-inducing drugs (\alpha=10^{-2}), where resistance is reversible. The left column indicates treatment strategy, whereas right indicates corresponding tumor volume response. Note that the dashed red line in the right column indicates the tumor volume representing treatment failure, V_{c}. (A) Constant and pulsed therapies after tumor detection for \alpha=0. (B) Responses corresponding to treatment regimens in panel A. (C) Constant and pulsed therapies after tumor detection for \alpha=10^{-2}. (D) Responses corresponding to treatment regimens in panel C.

<a id='6c19d4d5-525e-4fec-a9aa-11a86a0fe85e'></a>

equations for the model parameter, which we are able to solve.
Carrying out these computations yields the following solution:

<a id='12b9e51e-af8d-457e-9b91-bab4be8be690'></a>

d = Y₂ - Y₁ / Y₀ , (A14)ε = Y₇ - Y₆ + ½Y₅ - 2Y₄ - ¾Y₃ + dY₀(1 - Y₀) / dY₀ , (A15)ρᵣ = Y₃ - (1 - ε)Y₀ + (3 - ε)Y₀² - 2Y₀³ / εY₀(1 - Y₀) (A16)

<a id='4f45a3b9-fceb-469d-89be-e4cc8245568b'></a>

<::transcription of the content
: $\alpha = \frac{\frac{1}{2}Y_5 - Y_4 + \frac{1}{2}Y_3 - d^2 Y_0}{dY_0}$ (A17)
::>

<a id='17d71484-0733-4f75-ab34-4466e5da4bb4'></a>

Note that in Equations A14 and A17 each quantity is determined by the Yi and the parameter values previously listed. We do not write the solution in explicit form for the sake of clarity as the resulting equations are unwieldy. Furthermore, the solution of this system relies on the assumption of strictly positive initial conditions (S⁰ = Y⁰ > 0), wild-type drug induction death rate (d), and background mutation rate (ε), all of which are made in this work.

<a id='01b28f28-1c03-4934-9a08-60fe76b2c4da'></a>

JCO Clinical Cancer Informatics

<a id='5a752d79-1a03-45d9-a065-134d252e06f5'></a>

15

<!-- PAGE BREAK -->

<a id='685bb200-2606-491c-84f6-b3ce5f1b6694'></a>

Greene, Gevertz, and Sontag

<a id='3b436c31-e4f3-41fc-b84b-e0d86fc89208'></a>

<::figure::>
FIG A2. Treatment dynamics for phenotype-preserving drugs (α = 0). The left column indicates treatment strategy, whereas the right indicates corresponding population response.

**A) Constant treatment after tumor detection.** This plot shows the treatment strategy over time. The x-axis is "Time" from 0 to 140. The y-axis is "U" from 0 to 0.5. A horizontal line is shown at U = 0.45, starting from Time 0 and extending to Time 140, indicating a constant treatment.

**B) Response to constant treatment.** Note that at the time of treatment failure, the tumor is essentially entirely resistant. This plot shows population dynamics over time. The x-axis is "Time" from 0 to 140. The y-axis is "Population" from 0 to 1. The legend indicates: "S" (solid blue line), "R" (dashed red line), and "V" (dotted grey line). The "S" population rises from 0 to about 0.5 by Time 20, remains constant until about Time 100, then decreases to 0 by Time 130. The "R" population remains at 0 until about Time 80, then increases sharply, reaching about 0.9 by Time 140. The "V" population (total population) rises from 0 to about 0.5 by Time 20, remains constant until about Time 80, then increases sharply, reaching about 0.9 by Time 140.

**C) Pulsed therapy after tumor detection.** This plot shows the treatment strategy over time. The x-axis is "Time" from 0 to 18. The y-axis is "U" from 0 to 5. Three rectangular pulses are shown, each reaching U = 5 for a short duration, centered around Time 2, Time 8, and Time 12, with U returning to 0 between pulses.

**D) Response to pulsed therapy.** Note that the treatment fails much earlier versus the constant dose and that the tumor is primarily drug sensitive. This plot shows population dynamics over time. The x-axis is "Time" from 0 to 18. The y-axis is "Population" from 0 to 0.9. The legend indicates: "S" (solid blue line), "R" (dashed red line), and "V" (dotted grey line). The "S" population rises, drops during treatment pulses, then rises again, reaching about 0.9 by Time 18. The "R" population remains very low, close to 0, throughout the entire period. The "V" population (total population) generally follows the "S" population, rising and dropping, reaching about 0.9 by Time 18.
::>

<a id='1a9fe6ca-b5b5-4077-8acc-9ed990f366fd'></a>

Equation A17 is the desired result of our analysis. It demonstrates that the drug-induced phenotype switching rate α may be determined by a relatively small set of input controls u(t). As discussed in the previous section, the value of α may have a large impact on treatment efficacy and, therefore, determining its value is clinically significant. Our results now prove that it is possible to compute the induction rate and, hence, use this information in the design of treatment protocols. In the next section, we investigate other qualitative properties that could also be applied to understand the rate of drug-induced resistance.

<a id='6492a325-855a-4dc3-aa0d-e4cfe3ef37c2'></a>

An In Vitro Experimental Protocol to Distinguish
Spontaneous and Drug-Induced Resistance
We have demonstrated that all parameters in Equations 4 and 5 are
identifiable so that it is theoretically possible to determine the

<a id='894ea5d0-6c05-4328-9b36-664b82fb2dc6'></a>

phenotype-switching rate α from a class of input controls u(t);
however, we see that the calculation involved measuring de-
rivatives at the initial detection time t=td. Furthermore, the applied
controls (Eq A13) are nonconstant and thus require fractional
doses to be administered. Clinically, such strategies and mea-
surements may be difficult and/or impractical. In this section, we
describe an in vitro method for estimating α using constant ther-
apies only. Specifically, our primary goal is to distinguish drugs with
α = 0 (phenotype preserving) and α > 0 (resistance inducing). Such
experiments, described below, may be implemented for a specific
drug, even if its precise mechanism of promoting resistance remains
uncertain.

<a id='54922f4b-8b0a-4722-bdea-b3f707dd3bae'></a>

Before describing the in vitro experiment, we note that we are in-
terested in qualitative properties for determining α. Indeed, in most

<a id='ec4279ee-be02-4fe8-8ebc-5c733da01af4'></a>

16 © 2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='602765ba-7ffa-4e8f-a474-66ca3ae2572d'></a>

Differentiating Spontaneous and Induced Resistance

<a id='a50c0493-a726-45fe-8da6-82223f6fea02'></a>

<::Figure: The image contains two plots, labeled A and C, showing different treatment strategies over time. Both plots have 'Time' on the x-axis, ranging from 0 to 60, and 'u' on the y-axis, representing the treatment strategy.

Plot A: A line graph titled "Treatment Strategy, α = 10^-2". The y-axis 'u' ranges from 0.05 to 0.5. The graph shows a vertical line at Time = 0, extending from 0 to u = 0.5, followed by a horizontal line at u = 0.5, extending from Time = 0 to Time = 60.

Plot C: A bar chart titled "Treatment Strategy, α = 10^-2". The y-axis 'u' ranges from 0.5 to 5. The chart displays a series of vertical bars (pulses) reaching u = 5, occurring periodically at approximately Time = 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, and 50. There are also partial labels for B and D on the right side of the image, showing the word "Population" vertically, but no corresponding plots or data are visible.: chart::>

<a id='f7064fb6-13a0-4fd0-a2e5-f0d0f42ce7ca'></a>

B
<::Graph B: Line chart showing Population Dynamics, α = 10⁻².
X-axis: Time, from 0 to 60.
Y-axis: Population, from 0 to 0.9.
Legend:
- S: solid blue line
- R: dashed red line
- V: dash-dot grey line

Plot description:
- The S line (solid blue) starts low, rises to a peak of approximately 0.45 around Time = 10, then steadily declines to near zero by Time = 50.
- The R line (dashed red) starts near zero, slowly increases until Time = 20, then accelerates its increase, reaching approximately 0.8 by Time = 50.
- The V line (dash-dot grey) follows the S line initially, peaking around 0.45 at Time = 10, then continues to increase, forming a smooth curve that reaches approximately 0.85 by Time = 50.
: chart::>
D
<::Graph D: Line chart showing Population Dynamics, α = 10⁻².
X-axis: Time, from 0 to 60.
Y-axis: Population, from 0 to 1.
Legend:
- S: solid blue line
- R: dashed red line
- V: dash-dot grey line

Plot description:
- The S line (solid blue) exhibits oscillations, rising sharply and falling multiple times, with peaks reaching approximately 0.8 to 0.9. The oscillations occur frequently until Time = 35-40, after which the amplitude decreases and the line approaches zero by Time = 50.
- The R line (dashed red) starts near zero, shows a gradual increase with minor fluctuations, and then rises sharply from Time = 20 to Time = 50, reaching approximately 0.8.
- The V line (dash-dot grey) also exhibits oscillatory behavior, generally following the peaks and troughs of the S line but with an overall increasing trend, reaching approximately 0.85 by Time = 50. The oscillations become less distinct towards the end.
: chart::>

<a id='6c95864c-64ff-45d6-b7a1-151f68f7801d'></a>

FIG A3. Treatment dynamics for resistance-inducing drugs (a = 10⁻²). The left column indicates treatment strategy, whereas the right indicates corresponding population response. (A) Constant treatment after tumor detection. (B) Response to constant treatment. Note that at the time of treatment failure, the tumor is essentially entirely resistant. Dynamics are similar to Figure 2B, although with a shorter survival time. (C) Pulsed therapy after tumor detection. (D) Response to pulsed therapy. Note that here, in contrast to the case of a phenotype-preserving drug as shown in Figure A2, pulsed therapy exhibits a longer survival time.

<a id='437f328e-d9d4-402b-8c54-d05101695228'></a>

modeling scenarios, we have little or no knowledge of precise pa-
rameter values and instead must rely on characteristics that distinguish
the switching rate a independently of quantitative measurements.
Furthermore, as a general framework for drug resistance, the only
guaranteed clinically observable output variables are the critical tumor
volume Vc and the corresponding time tc. For a description of the
treatment protocol, see above. We cannot expect temporal clonal
subpopulation measurements. Assuming that Vc is fixed for a given
cancer, tc is thus the only observable that we consider.

<a id='9b08df96-8872-4824-848f-329d682f3e1a'></a>

By examining Equations 4 and 5, we see that the key parameters that dictate progression to the steady state (S, R) = (0,1) are d and α, as these determine the effectiveness and resistance induction of the treatment, respectively. Recall that ε is the fixed background

<a id='1dca64bf-10ef-4bde-ab5a-e83d519711c5'></a>

mutation rate and _p_, the relative fitness of resistant cells. We thus
perform a standard dose-response experiment for each value of
drug sensitivity _d_ and measure the time _t_c to reach critical size _V_c as
a function of _d_. The response _t_c will then depend on the applied
dose _u_—recall that we are only administering constant therapies—
and the sensitivity of wild-type cells _d_, as well as the induction
rate _α_:

<a id='3f19dfa8-4fac-4f7f-b31e-4e54bd82f209'></a>

tc = tc(u, d, \alpha). (A18)

<a id='983fec16-e7b3-416b-899d-b9388aef2134'></a>

We further imagine that it is possible to adjust the wild-type
drug sensitivity d. For example, in the case of multidrug resistance

<a id='49a3d4c1-52e9-41eb-8f14-8e73d9fec405'></a>

JCO Clinical Cancer Informatics

<a id='20bc56d9-452d-48c1-b58c-fdaa40e9d7ec'></a>

17

<!-- PAGE BREAK -->

<a id='68aa0691-c68a-4fb7-9553-4be7126a1e48'></a>

Greene, Gevertz, and Sontag

<a id='cabe24a5-10ab-4633-9f7c-d9c26c47ff6c'></a>

in which the overabundance of P-glycoprotein affects drug phar-
macokinetics, altering the expression of MDR1 via ABCBC1 or even
CDX2 (Koh I, Hinoi T, Sentani K, et al: Cancer Med 5:1546-1555,
2016) may yield a quantifiable relationship between wild-type cell
and d, thus producing a range of drug-sensitive cell types. Figure 3A
exhibits a set of dose-response curves for representative drug
sensitivities d for the case of a resistance-inducing drug (a = 10-2).

<a id='658e42c3-1282-4161-b76c-c98f3894adfc'></a>

For each of these cell types, we then define the supremum response time over administered doses:

<a id='9b027159-5254-4905-91ff-aa79f21ef483'></a>

T_a (d) := sup_u {t_c (u, d, \alpha)}. (A19)

<a id='e8ac5a56-8dd0-459b-814c-8ab45573e1ca'></a>

Note that in a laboratory setting, only a finite number of doses will be administered so that the above supremum is actually a maximum, but for mathematical precision we retain supremum. Thus, we obtain a curve $T_\alpha = T_\alpha(d)$ for each value of the induced resistance rate $\alpha$. We then explore the properties of these curves for different $\alpha$ values.

<a id='05b31903-8b88-478c-899c-28a904a4116a'></a>

Consider first the case of a phenotype-preserving drug, so that α = 0.
As u(t) ≡ u, we see that the system Equations 4 and 5 depends only
on the product of u and d. Hence, the dependence in Equation A18
becomes the form t_c(u·d, 0), and thus the supremum in Equation
A19 is instead across the joint parameter D := u·d:

<a id='6552a987-39f6-4fa5-8a40-191575eecede'></a>

T_0 := \sup_{D}\{t_c(D,0)\}. (A20)

<a id='668af36f-8a00-425f-b303-cdb85c0e0656'></a>

Clearly, this is independent of d so that T₀ is simply a horizontal line for
α = 0. Qualitatively, the resulting curve will have no variation among the
engineered sensitive phenotypes, save for experimental and mea-
surement noise. Figure 4 shows both representative curves (Fig 4A
compared with Fig 3A) and a plot of T₀(d) (Fig 4B), which verifies its
independence of d. We make two minor technical notes. First, it is
important that we assume d > 0 here, as otherwise D = 0, independent
of dose u and the supremum is over a one element set. See below for
more details and the implications for α identifiability. Second, the slight
variation for large values of d is a result of numerical error, as the
maximum of t_c occurs at decreasing doses (see the below section and
Figure A4 for more details).

<a id='3bab12fc-35be-4a8e-9603-0cdb237f519d'></a>

<::chart: line chart titled "Maximum Dosage Yield Tα(d)". The y-axis is labeled "u" and ranges from 0 to 3.5. The x-axis is labeled "d" and ranges from 0 to 4. Two lines are plotted: a solid red line representing "Numerical" and a dashed blue line representing "Theory". Both lines start high on the y-axis (around 3.25 for Numerical and 1.6 for Theory at d=0) and rapidly decrease as d increases, eventually flattening out near u=0 for larger d values. The "Numerical" line is slightly above the "Theory" line, especially at lower d values.::>FIG A4. Dose yielding maximal response time $T_{\alpha}(d)$ computed numerically, as well as the approximation given by Equation A24. All parameters appear as in Table 1, and $\alpha=10^{-2}$. The numerical maximum is computed over a discretization of constant dosage procedures $u(t)\equiv u$, for $u\in[0,5]$, with a mesh size $\Delta u=0.005$.

<a id='e8924f38-65e8-4b63-896a-1fe82acee4c5'></a>

Comparing Figures 3A and 4A, we observe similar properties: small *t<sub>c</sub>*
for small doses, a sharp increase about a critical *u<sub>c</sub>*, followed by
smooth decrease and eventual horizontal asymptote (for mathe-
matical justification, see the below section). However, note that for
a resistance-inducing drug (Fig 3A), maximum critical time *T<sub>α</sub>(d)*
increases as a function of *d*. This is in stark contrast to the constant
behavior obtained for *α* = 0, argued above and demonstrated in
Figure 4B. To further understand this phenomenon, we plot *T<sub>α</sub>(d)* for
a fixed induction rate *α* = 10<sup>-2</sup> in Figure 3B. The behavior of this curve
is a result of the fact that the critical dosage *u<sub>c</sub>* at which *T<sub>α</sub>(d)* is
obtained is a decreasing function of *d* (see Equation A24 and Fig A4
in the below section). But as *u<sub>c</sub>* also controls the amount of resistant
cells generated—via the *αu(t)S* term—resistance growth is impeded
by a decreasing *u<sub>c</sub>*. Thus, as a non-negligible amount of resistant
cells are necessary to yield *T<sub>α</sub>(d)*, more time is required for resistant
cells to accumulate as *d* increases. Hence, *T<sub>α</sub>(d)* increases a function
of *d*.

<a id='1a3111e1-ff2d-41d0-8bb4-c2f49a629458'></a>

The behavior observed in Figures 3B and 4B is precisely the qualitative distinction that could assist in determining the induced resistance rate α. In the case of a phenotype-preserving drug, the proposed in vitro experiment would produce a flat curve, whereas a resistance-inducing drug (α > 0) would yield an increasing function Tα(d). Furthermore, we could use this phenomenon, in principle, to measure the induction rate from the experimental Tα(d) curve. For example, Figure 5A displays a range of Tα(d) for α near 10⁻².

<a id='3cbdfc9a-a078-40b9-9699-abfde99a5625'></a>

Figure 5A shows a clear dependence of Tα(d) on the value of α. Quantitatively characterizing such curves would allow us to reverse engineer the induction rate α; however, we note that, in general, the precise characteristics will depend on the other fixed parameter values, such as pr, Vc, and ε. Indeed, only order of magnitude estimates may be feasible. Illustrative sample curves are provided in Figure 5B. Two such characteristics are apparent from this figure, both related to the slope of Tα(d). First, as d → 0+, we observe an increase in the slope of Tα(d) as α decreases (note that in Fig 5B, only d ≥ 0.05 are plotted). This follows from the continuity of solutions on parameters and the fact that T₀(d) possesses a jump discontinuity at d = 0—that is, its distributional derivative is given by

<a id='9b315984-6da8-4359-897f-4891b849e094'></a>

∂/∂d |d=0 T₀(d) = kδ(d),

(A21)

<a id='b4457224-563e-4b41-b9fc-b7ac11989a54'></a>

where δ is the Dirac function and k is a positive constant. As discussed previously (Equation A20 and the subsequent paragraph), T₀(d) is flat, except at d=0 where the vector field contains no u dependence. Therefore, the set over which the maximum is taken is irrelevant and T₀(d) is thus proportional to the Heaviside function, which possesses the distributional derivative Equation A21. The constant k is determined by the size of the discontinuity of T₀(d). Continuous dependence on parameters then implies that as α increases, the resulting derivative decreases away from positive infinity as the corresponding derivative for Tα(d) with α>0 is defined in the classic sense for α>0:

<a id='20c2e897-e160-4c45-91fe-77aee46f4c2a'></a>

∂/∂α ∂/∂d |_{d=0} T_α(d) ≤ 0.

<a id='f242af74-b26a-4d89-97ad-16635e5dfbe3'></a>

The above argument implies that measuring the slope of Tα(d) at d = O will give a characterization of the phenotypic alteration rate α of the treatment; however, such experiments may be impractical, as fine-tuning the sensitivity of a cell near complete resistance may be difficult. Alternatively, one could analyze the degree of flatness for a relatively large d—so to be sufficiently far from d = 0—and correlate this measure with α. For example, examining d = 2 in Figure 5B, we see that the relative slope of Tα(d) with respect to d should correlate with decreasing α. An argument similar to the above makes this rigorous, for d sufficiently large. Practical issues still arise, but this second method provides a more global method for possibly computing α. Indeed, slopes at a given d can be approximated by a wider range of secant approximations as the result holds for a range of d compared with the previously discussed case when d is near zero. Furthermore, our focus

<a id='fc704590-fb41-49f9-8c30-680b25b70f48'></a>

18  2019 by American Society of Clinical Oncology

<!-- PAGE BREAK -->

<a id='c66abc8d-cafb-4ba6-9369-1b5d7fb16026'></a>

Differentiating Spontaneous and Induced Resistance

<a id='8a701f87-ffae-4886-ad78-5098801d6443'></a>

is largely on the qualitative aspects of \u03b1 determination, such as the
differences in Figures 3A and 4A, and determining whether the
treatment itself induces resistance to emerge.

<a id='0b905e44-816f-4e41-956c-fef596204645'></a>

## Introduction to Identifiability Analysis
In this section, we provide additional details on the theoretical identifiability of model parameters. As mentioned in the main text, all higher-order derivatives at initial time _t_ = 0 may be calculated in terms of the initial conditions (_S_(0), _R_(0)) and the control function _u_(_t_). For example, for an arbitrary system

<a id='fb89368c-f00a-4440-bc7f-95091332850c'></a>

x(t) = f(x(t), u(t)),

<a id='758f7434-630b-40a4-a134-9f2e7f9178df'></a>

with external control _u_(_t_), the second derivative _ẍ_ may be calculated using the chain rule:

<a id='2c9eb5b5-6e62-42de-b2f1-18cc1a6926c8'></a>

ẍ = J_f (x, u) f + ∇_u f (x, u) u̇,

<a id='38bd72d8-d041-47c6-b459-cb6040b47f8f'></a>

where J(x) is the Jacobian matrix of f, evaluated at state x and control u. If x(0) = x₀ is known, the above expression is a relation among parameters, together with u and ủ evaluated at time t = 0. An analogous statement holds for a measurable output y = h(x), but will also involve the Jacobian of h. Concretely, for the model of induced drug resistance Equations 4 and 5, first derivatives of the tumor volume may be calculated as

<a id='b990c016-aa74-4bda-8f6a-7d7386576569'></a>

V'(0) = S'(0) + R'(0),
= ((1 - (S + R))S - (ϵ + αu(t))S - du(t)S)
+ (p_r (1 - (S + R))R + (ϵ + αu(t))S)|t=0,
= (1 - S_0)S_0 - du(0)S_0,

<a id='73309e1a-99a4-4d24-86a5-b534e1076850'></a>

for any control u(t) [recall that R(0) = 0]. Similarly, for the second derivative, we compute:

<a id='26857bfd-39da-46f2-8b62-d227d5d07de7'></a>

V''(0) = S0 (1 - S0 - (ε + d)u(0)) (1 - 2S0 - du(0))
+ S0 (αu(0) + ε) (pr - S0 (1 + pr)) - dS0 u̇(0).

<a id='5752ef36-ac2f-4694-954a-ef77943ce65f'></a>

Using such expressions—or, more precisely, the Lie derivatives of the vector field [see Sontag (PLOS Comput Biol 13:e1005447, 2017)] —for the controls in Equation A13, one is able to obtain a set of equations between the set of Yᵢ, i = 0, 1,..., 7 and the parameters d, ε, pᵣ, and α. Solving these equations allows us to determine the parameters with respect to the measurable quantities. The algebraic solution is Equations A14-A17.

<a id='2a5ec51a-2402-439e-b995-36fb22cb24bb'></a>

**Analysis of Critical Time T<sub>α</sub>(d)**

We provide a qualitative understanding of the properties of T<sub>α</sub>(d),
the maximum time, across all constant doses for the tumor to
reach size V<sub>c</sub>. This Appendix is designed to explain the basic
properties discussed in An In Vitro Experimental Protocol to
Distinguish Spontaneous and Drug-Induced Resistance in the
main text.

<a id='85e481a3-64f8-4244-835c-be9084ac4322'></a>

We first note that T⍺(d) is achieved at a medium dose u_c. More precisely, we describe the qualitative properties of Figures 3A and 4A. Fix a drug sensitivity d. For small u, the sensitive subpopulation is not sufficiently inhibited and thus expands rapidly to cross the threshold V_c, with an essentially homogenous population of sensitive

<a id='c8fbdece-eb3f-4f6a-bb78-13796a48e393'></a>

cells. Indeed, as u → 0, the dynamics of Equations A1 and A2
approach those of

<a id='5b465544-5104-41ac-a907-f2ac155c9f17'></a>

$\frac{d\tilde{S}}{dt} = (1-(\tilde{S}+\tilde{R}))\tilde{S}, \quad (A22)$

<a id='992a2c30-da8a-4c5e-8334-ffa3cc4484e2'></a>

<::d~R/dt = p_r(1-(~S + ~R))~R, (A23): figure::>

<a id='6e129e9b-9458-4c3e-bafb-66e30c474272'></a>

for small finite times, as ε <<1. Trajectories of Equations A22 and A23 remain on the curve

<a id='d5197eda-e585-47cb-a7c6-a115b2945643'></a>

R(S) = R_0 / S_0^Pr S^Pr

<a id='1725bd42-c37f-4ed8-aa96-9b5e224d89cd'></a>

as the solution approaches the line S+ R = 1. The critical time tc is then
determined by the intersection of this curve with S + R = Vc and, thus,
has sensitive population Sc at tc given by the unique solution in the first
quadrant of

<a id='27ebb004-db96-4c83-b027-8d82ea0133a5'></a>

$$S_c + \frac{R_0}{S_0^{Pr}} S_c^{Pr} = V_c$$

<a id='cb4fd23f-5b9a-4caa-8c41-ddf357d13331'></a>

As R₀ << 1 (as ε << 1), S_c ≈ V_c, as claimed. Time t_c is thus small for small u.

<a id='370b077a-dcca-478b-b4ef-9b353cf32797'></a>

Increasing values of *u* imply that *t*<sub>c</sub> also increases as the overall growth rate of sensitive cells is decreased; however, there exists a critical dose *u*<sub>c</sub> such that sensitive cells alone are not able to multiply sufficiently to attain *V*<sub>c</sub>, so that the critical volume must have non-negligible contributions from the resistant fraction. This leads to the bifurcation apparent in Figures 3A and 4A. We can even approximate the critical dose maximizing *t*<sub>c</sub>, as *V*<sub>c</sub> must be an approximation for the carrying capacity of the sensitive cells:

<a id='396f34cd-c482-4cba-80e0-7a99e34b9c47'></a>

S_K ≈ V_c.

<a id='1985db77-8ed6-4ee0-925d-2490770e6fe6'></a>

Examining the right side of Equation Al and assuming that the dy-
namics of the resistant population are negligible, which is accurate in
the early stages of treatment (Figs 2B and 3B), we see that the dose
that yields the maximum temporal response should be

<a id='309af451-54e0-46ec-8acc-24e545b41559'></a>

uc ≈ 1 - ε - Vc / α + d (A24)

<a id='d96a40a8-fbcc-4ad6-8e7d-cd24ad4d1093'></a>

That is, the dose at which T_a(d) is obtained is given approximately by the expression in Equation A24. For a sample numerical comparison of the predicted formula Equation A24 and a numerical optimization over a range of drug sensitivities d (Figure A4). Note that in actuality, S_K < V_C, as the resistant dynamics cannot be ignored entirely. Thus, the precise value of u_C will be smaller than that provided in the previous formula as we numerically observe. Lastly, u_C decreases with increasing values of parameter d and, thus, requires an increasingly fine discretization to numerically locate the maximum value. Hence, some numerical error is observed in Figure 4B.

<a id='82601c57-2fdf-479f-a7d4-6456b6f8af52'></a>

Lastly, as u is increased further, the dose becomes sufficiently large so that the inhibition of S via therapy implies that S cannot approach the critical volume V_c and, hence, V_c is again reached by an essentially homogeneous population, but now of resistant cells. As resistant cells divide at a slower rate (p_r < 1), the corresponding time t_c is smaller. For a schematic of the three regimes described above (Figure A5).

<a id='5ea3be8a-e7c1-4fd7-b149-6abff4dbe88c'></a>



<a id='0c3b8579-e375-4ce8-899b-7454f3443e2c'></a>

19

<!-- PAGE BREAK -->

<a id='bd0428d9-c034-4e30-a58c-5b0f13724c89'></a>

Greene, Gevertz, and Sontag

<a id='88eb3b5f-1182-4eb4-a78d-d362818ef01e'></a>

<::chart
: A line graph titled "FIG A5." with "Volume" on the y-axis (labeled S at the top) and "Time" on the x-axis (labeled t at the right, with an additional mark t_d). A dashed red horizontal line indicates V_c on the y-axis. Three curves are plotted, representing the sensitive cell population as a function of time for different dosages (u):
1. A grey curve labeled "u < u_c" shows the volume rapidly increasing, then gradually leveling off towards V_c.
2. A red curve labeled "u ≈ u_c" shows the volume increasing, reaching V_c, maintaining near V_c for a period, and then decreasing.
3. A blue curve labeled "u > u_c" shows the volume steadily decreasing from the start.

FIG A5. Schematic demonstrating dynamics of variation in t_c on dosage u. Sensitive cell population plotted as a function of time for three representative doses. For u < u_c, sensitive cells grow and reach V_c in a short amount of time. As u→u_c, the sensitive population approaches its approximate carrying capacity of V_c, but subsequently decreases as a result of the dynamics of resistance. Here, t_c is maximized as the sensitive population spends a large amount of time near V_c. For u > u_c, the sensitive population is eliminated quickly, and V_c is obtained by a primarily resistant population.
::>


<a id='7180518d-0fbc-4abd-8532-e5ee4d152220'></a>

20 © 2019 by American Society of Clinical Oncology