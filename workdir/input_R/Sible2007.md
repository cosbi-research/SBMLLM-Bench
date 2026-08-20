<a id='24583c57-0bff-4af1-b664-4648792bd77a'></a>

NATIONAL INSTITUTES OF HEALTH

NIH Public Access

**Author Manuscript**

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='cbb694b1-2aeb-47dc-842c-82b07e3a15a1'></a>

Published in final edited form as:
*Methods*. 2007 February ; 41(2): 238–247.

<a id='943adb53-b608-443d-8bc8-424b61245f6d'></a>

**Mathematical Modeling as a Tool for Investigating Cell Cycle**
**Control Networks**

**Jill C. Sible*** and **John J. Tyson**
*Department of Biological Sciences, Virginia Polytechnic Institute and State University, Blacksburg,*
*VA USA 24061-0406*

<a id='69dbf6a1-a1c1-4ecc-815a-af49556bf658'></a>

# Abstract
Although not a traditional experimental "method," mathematical modeling can provide a powerful approach for investigating complex cell signaling networks, such as those that regulate the eukaryotic cell division cycle. We describe here one approach to modeling the cell cycle based on expressing the rates of biochemical reactions in terms of nonlinear ordinary differential equations (ODEs). We discuss the steps and challenges in assigning numerical values to model parameters and the importance of experimental testing of a mathematical model. We illustrate this approach throughout with the simple and well-characterized example of mitotic cell cycles in frog egg extracts. To facilitate new modeling efforts, we describe several publicly available modeling environments, each with a collection of integrated programs for mathematical modeling. This review is intended to justify the place of mathematical modeling as a standard method for studying molecular regulatory networks and to guide the non-expert to initiate modeling projects to gain a systems-level perspective for complex control systems such as those governing the eukaryotic cell cycle.

<a id='8f5dfb07-3fac-4b64-bf1f-1a66527dd842'></a>

## Keywords
cell cycle; computational biology; frog egg extracts; mathematical modeling; ordinary differential equations; parameter estimation; systems biology; Xenopus laevis

<a id='96f40bbe-3b18-4ddc-a37e-95ae7b0ce664'></a>

# 1 Introduction

Because a universal mechanism controlling DNA synthesis, mitosis, and cell division underlies the growth, development, and reproduction of all eukaryotes, an understanding of this molecular regulatory system is one of the most important goals of modern cell biology. As the complex network of cell cycle controls is uncovered, it becomes increasingly difficult to make reliable predictions about how modification of one component affects the system as a whole. However, such predictions are needed if we are to identify the host of mutations contributing to cancer or find within the molecular network novel targets for therapeutic intervention. Mathematical models provide powerful tools for managing the complexity of the cell cycle control system and of other signaling networks. Models organize a large body of experimental data, describe the fundamental behaviors of the system as a whole, bridge gaps where experimental data are missing, and drive hypothesis-building for the next round of experimentation. The value of mathematical modeling in describing and predicting the behavior of complex systems has been well established in fields such as chemical engineering

<a id='f3a3b801-c59b-4688-84d3-745e84b09e21'></a>

*to whom correspondence should be addressed, phone: 540 231 1842, FAX: 540 231 9307, e-mail: siblej@vt.edu
**Publisher's Disclaimer:** This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

<a id='5262f029-f841-4b38-bcc3-f916f1eefa83'></a>

NIH-PA Author Manuscript

<a id='12cdad07-a1e1-4c55-8e07-d6fb55f23fba'></a>

NIH-PA Author Manuscript

<a id='317026e0-1c38-49c9-93fb-25866a751a9f'></a>

NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='6066a325-9c27-4e76-bc25-06e0ccb0a910'></a>

Sible and Tyson

<a id='773a5615-9135-4e4f-93e2-77f5349f5f79'></a>

Page 2

<a id='0d7e7ca9-0b67-4b9b-b6a4-48bee56b84f1'></a>

and meteorology, but its power has been underappreciated until recently in molecular cell
bilogy.

<a id='6d932d4f-3ca9-4485-a4e7-7c0658ba0a09'></a>

Although mathematical models can be built to describe any signaling network, application of modeling tools to cell cycle regulation is particularly well suited and timely. First, the data in this field are vast, both providing a large body of information to build comprehensive models and creating the need for a tool to understand how these data fit together. Second, cell cycle signaling networks are modular, allowing models to be constructed in parts and then assembled and reassembled in various ways. Furthermore, many models of the network are comparable between different systems (e.g. budding yeast and mammals) so that it is feasible to make relatively small changes to a model describing one particular system in order to apply it to another. Thus, each new model need not be constructed from scratch. Third, a reasonable amount of quantitative or semi-quantitative information can be extracted from the literature, facilitating the early phases of model building. By modifying established protocols (described in the accompanying articles), additional quantitative data can be generated to improve parameter estimation and experimental validation of models. Finally, despite the wealth of detailed information on cell cycle molecules and their specific interactions, we lack a systems-level perspective of this complex control network. Modeling can provide this perspective by helping to identify underlying regulatory principles. Where a specific experimental detail is missing, modeling can serve as bridge, enabling progress in building a systems-level view, and guiding the design and execution of future experiments.

<a id='5e50a3af-a7d9-4011-9cc7-c03e39b9d5c6'></a>

Although the term "mathematical modeling" encompasses a wide range of computational approaches applicable to cell cycle studies, we focus this review on one branch of modeling: the construction of ordinary differential equations (ODEs) to describe protein interaction networks that regulate the cell cycle. This approach has a strong track record of yielding accurate, predictive and testable models (1-7), and in recent years, has been integrated well with experimental methodologies (8-12). We will illustrate each step of the modeling process with an example: the core signaling network that controls entry into and exit from mitosis in frog egg extracts by regulating the activity of the mitotic cyclin-dependent kinase (Cdk1). We chose this example because the network is relatively simple, many predictions of the model have been validated experimentally, and this module can be adapted to more complex cell cycles both in _Xenopus_ and other eukaryotes.

<a id='e8a99801-67e4-43d8-bf50-96d9aec598da'></a>

## 2 Approach
### 2.1 Construction of a wiring diagram

<a id='5a62bf02-e9bc-4724-a9b7-22d3c534cb1d'></a>

The first step in the modeling process is to organize the known interactions of the relevant molecules into a concept map or wiring diagram. A simple diagram representing the core machinery regulating mitotic transitions in *Xenopus* cell-free egg extracts is depicted in Figure 1. The diagram depicts each biochemical entity with a separate icon. For example, the phosphorylated form of Wee1 is represented by a modified version of the icon for unphosphorylated Wee1. Solid arrows indicate chemical transitions between states, and dotted arrows represent a modulating signal on a biochemical reaction (often the catalytic influence of an enzyme). Because no universal conventions for building these diagrams exist, all symbols must be defined explicitly and used consistently. Hopefully, contributors to this field will adopt a common symbolism in the near future, facilitating the exchange of information between wiring diagrams and their affiliated mathematical models.

<a id='8ccf6708-43d6-4291-a768-adc8efe306e2'></a>

Despite the wealth of information regarding cell cycle signaling networks, gaps in knowledge may exist such that portions of the diagram cannot be wired with certainty. It is neither necessary nor advised to postpone the modeling process indefinitely until all molecular details of the wiring diagram are understood. Rather, the gaps in the wiring diagram can be filled with

<a id='7ee014ee-18fe-45de-a2a0-a6030883f6af'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='f373e1aa-aa67-4c27-867f-a1ddc36d9722'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='f9813b53-1318-4858-8377-38d82acae261'></a>

Sible and Tyson

<a id='ab866c7d-8364-4e83-a73f-3cd8f9b9b38f'></a>

Page 3

<a id='ed818d16-d31a-45f2-9e67-bfd004ae1138'></a>

placeholders. These placeholders can be generic ones for which parameters will be selected empirically to model the behavior of the system without representing the molecular mechanism in detail. This approach allows the modeling effort to continue in order to discover properties of the system as a whole as well as specific features of better-characterized portions of the diagram. Alternatively, a more specific placeholder can be created that makes some untested assumptions about the molecular mechanism. These assumptions in the wiring diagram will be tested in simulations of the model to determine whether they are consistent with known behaviors of the system. Eventually, the assumptions that work in silico must be tested experimentally when appropriate methodologies and reagents become available. Ideally, portions of the wiring diagram that are hypothetical should be clearly delineated from those that are grounded in experimentation.

<a id='87b36559-6766-4088-a739-225cb986561a'></a>

Our example, a model of the cell cycle machinery regulating mitosis in frog egg extracts, demonstrates the usefulness of placeholders. When the wiring diagram depicted in Figure 1 was first constructed (2), little information was known about the mechanisms regulating exit from mitosis. Experimental data suggested that MPF triggered the degradation of cyclin (13) and a previous mathematical model indicated that a time delay in this negative feedback loop could create sustained oscillations (3). Based on this information, the wiring diagram was constructed with an intermediate component (called IE) that was phosphorylated by MPF, and then activated the APC, triggering the polyubiquitination and subsequent degradation of cyclin (2). Several years later as the details of the ubiquitin-proteasome pathway governing cyclin degradation were discovered, IE was replaced by Fizzy/Cdc20 and components of the APC (14-16) but the fundamental features of the model remained the same.

<a id='44daed31-bd90-4314-a409-02a956d2ac1a'></a>

## 2.2 Writing the ordinary differential equations

Once the model is represented diagrammatically, the biochemical relationships need to be converted to the language of mathematics in the form of nonlinear ODEs. A rate equation is written for each biochemical entity whose concentration changes over time. The right side of the equation includes a positive term for every arrow that directs toward that entity and a negative term for every arrow that directs away from the entity. The kinetics selected should be appropriate for the type of biochemical transition represented. In general, mass-action kinetics are appropriate for most biochemical reactions except when [substrate]>>[enzyme], in which case Michaelis-Menten kinetics should be applied.

<a id='242bcae9-a7c8-4455-8cb1-02850573c671'></a>

In our example of the core mitotic machinery, the rate equation for the concentration of cyclin monomers is based on mass-action kinetics:

<a id='9e777dc3-1b45-442f-8868-6c14dd0807d1'></a>

d/dt [Cyclin] = k₁ - k₂[Cyclin] - k₃[Cyclin][Cdk]

<a id='65563abe-2919-43ff-9b64-38edc4b6081f'></a>

where k₁ is the rate constant for cyclin synthesis, k2 is a function that describes the activity of the APC in promoting cyclin degradation, and k3 is the rate constant for association of cyclin monomers and Cdk monomers to form MPF dimers. These dimers are phosphorylated on threonine 161 to make active MPF. Because this reaction is fast and essentially irreversible, we are justified in neglecting the T161-unphosphorylated forms of MPF.

<a id='c01cfea1-3451-466c-8abc-badfc77d2e5d'></a>

The rate equation for [MPF] is likewise based on mass-action kinetics:

<a id='334cfb81-7de2-4b23-b297-55e51f9c9402'></a>

d/dt[MPF] = k₃[Cyclin][Cdk] – k₂[MPF] – k_wee[MPF] + k₂₅[preMPF]

<a id='ca6c9257-5e16-43aa-83e1-43f8f21e1f3d'></a>

A similar equation pertains to [preMPF]. [Cdk], the concentration of Cdk monomers, is governed not by an ODE but rather by a conservation condition:

<a id='ea6314ef-04a9-4f1c-96ff-e0072e0fd5fc'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='34a119b1-8906-442c-869e-e637f1314869'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='b6dc44fa-290b-4ce2-93df-3071f87616f6'></a>

Sible and Tyson

<a id='e673552d-121b-45cc-9b86-76fbc3b52ed5'></a>

Page 4

<a id='26410510-05ba-4b74-beaa-81bc7eed8705'></a>

[Total Cdk] = [Cdk] + [MPF] + [preMPF] = constant.

<a id='af508c5b-f531-4010-9f59-e94494b77ff6'></a>

We assume that [Total Cdk] = 100 nM in a typical frog egg extract.

<a id='7da87c4d-35af-4567-a2cb-76a9f1b20b46'></a>

The full set of differential equations for the model of M-phase control is shown in Figure 2. This early version of the model uses Michaelis-Menten kinetics to describe the rate changes of the regulatory enzymes, Cdc25 and Wee1 (2). Because of the positive feedback between Cdc25 and MPF and between Wee1 and MPF, the assumption that [enzyme]<<[substrate] may be invalid. In more recent iterations of the model, these equations have been rewritten with mass-action kinetics, and parameter sets that reproduce the fundamental behaviors of the system have been identified (Dravid and Tyson, unpublished data).

<a id='165a537f-c560-40f0-9954-8b933cf29215'></a>

## 2.3 Parameterizing the model
The next step in the modeling process is the most challenging. A preliminary set of parameters (rate constants for each reaction) must be selected. The challenges arise because for many models, few if any of these parameters have been measured directly. Therefore, the initial set of parameters must be selected based on semi-quantitative data, indirect measurements and typically, a fair amount of guesswork. In an iterative process, each set of parameters must be "run" through the model (described below) and modified to bring the output of the model into better and better agreement with observed behaviors of the system.

<a id='0de4658c-197f-4af2-8ea4-8cd6f951dec9'></a>

Even though few direct measurements of rate constants or concentrations of cell-cycle regulatory proteins have been published, valuable information for parameter estimation can be mined from the literature, and a thorough effort to do so is recommended before one undertakes the task of measuring parameters de novo. A reasonable body of experimental literature has informed the model depicted in Figures 1 and 2, although the initial parameter set was almost purely guesswork, based on rough qualitative features of mitotic control in frog eggs and extracts (2).

<a id='5a8c159c-dabd-4af8-b554-b7e3b8a1080c'></a>

Although enzyme rate constants are rarely measured or reported directly, reasonable estimates can be derived from time course studies, which abound in the cell cycle literature. For example, the experimental data of Kumagai and Dunphy (17), reproduced in Figure 3, gives us hints about the rates of phosphorylation of cyclin-Cdk1 by Wee1 in its more active form (Vwee") and its less active form (Vwee'). Lanes d-h and i-m show that Cdk1 is rapidly phosphorylated by Wee1 in an interphase extract, when Wee1 is expected to be in its active form. That rapid activation is observed even in the presence of aphidicolin ("+APC;" not to be confused with the Anaphase Promoting Complex), an inhibitor of DNA replication. Because Cdk1 appears to be completely converted to the tyrosine phosphorylated form within 2 minutes, Vwee" must be 1 min⁻¹ or larger. On the other hand, in an M-phase arrested extract (lanes a-c), tyrosine phosphorylation of Cdk1 by less active Wee1 is much slower, say Vwee' ≈ 0.01 min⁻¹. Kumagai and Dunphy (1995) also show that the rate of tyrosine phosphorylation is 2.5 times slower when cycloheximide-treated extracts were supplemented with cyclin B monomers rather than with preformed cyclin B-Cdk1 dimers (their Figure 3, A and C), allowing Marlovits et al. (1998) (43) to estimate that k₃ ≈ 0.005 nM⁻¹ min⁻¹. Although only rough estimates, these values for Vwee', Vwee", and k₃ provide good starting points for more sophisticated parameter optimization procedures. Table 1 provides the ODE files with the Marlovits' estimates of the rate constants for the ODEs in Figure 2.

<a id='5a2a5098-c75b-4668-9663-314f8ac1a457'></a>

At present, mining the literature to inform parameter estimation remains a laborious task. The body of literature is enormous and even the most carefully constructed database search algorithms will not identify all of the articles that might contain experiments relevant for parameter estimation. As modeling efforts become more widely utilized and organized, links between specific components of the model (parameters or details of the wiring diagram) and

<a id='a857dacd-24dc-47f4-b16b-4046dd258fcd'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='decb2fa1-dab7-4842-ae84-2f52086e4296'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='1f7a0759-d792-4012-9cd3-8b6cc60747f0'></a>

Sible and Tyson

<a id='67d660d1-7a4d-42f5-b796-25546101866f'></a>

Page 5

<a id='d0767c57-2179-4822-ad50-8c46f292783b'></a>

the data upon which they are based (a specific figure or page in a research article) need to be built. Meanwhile, even a limited amount of quantitative information can be useful in constructing the initial set of parameters, constraining portions of the model and allowing the governing ODEs to be numerically simulated to see how close or far the model lies from describing observed behaviors.

<a id='0448db33-eb64-4cb6-b223-4f1814c54043'></a>

Once the process of mining the literature has been exhausted, then the remaining parameters must be estimated by other means. Even in cases where the majority of the parameter values are unknown or where it would be feasible to measure parameter values directly, we recommend that the initial parameter set be derived with a minimal investment in new experimentation. Through computer simulations (described below), parameters can be twiddled with efficiency so that the modeler can develop a sense of which variables under which conditions are sensitive to which parameters. Such simulation will help design experiments that will yield the most quantitative "bang" for one's funding "buck." If during this twiddling phase, no reasonable parameter set can be developed to approximate the behavior of the system, then the wiring diagram may need to be reconsidered, and experiments carried out to test fundamental qualitative assumptions of the model rather than generating specific quantitative data.

<a id='21788b26-3e6f-46b9-896f-566cd513ca8d'></a>

## 2.4 Running simulations of the model

With an initial parameter set in hand, the next step is to "run" the model, that is, to use software that solves ODEs numerically in order to simulate the behavior of the system over time. WinPP (for Windows) and XPP (for Unix) are two simulation programs freely available from Dr. G. Bard Ermentrout, University of Pittsburgh. Go to http://www.math.pitt.edu/~phase for links to software downloads and tutorials. The basic output of a simulation is a graph of the concentration of each component over time.

<a id='903d0b1e-b02b-4f5c-b6d5-32e49a3d3222'></a>

To run a simulation one needs, in addition to differential equations (Figure 2) and rate constants (Table 1), "initial conditions" for all the variables (i.e. concentrations of each variable at t = 0). Initial conditions can usually be estimated readily from the experimental protocol of a particular experiment. For example, a "cycling" extract is prepared by activating the APC, which degrades most of the cyclin in the extract, so it is reasonable to set [IEP] = [APC] =1 and [cyclin] = [MPF] = [preMPF]=0 at t=0. Furthermore, we assume that [Cdc25P] = [Wee1P] = 0 at t = 0, because MPF is inactive. These common sense considerations fix reasonable initial conditions for a simulation of the temporal evolution of a cycling extract.

<a id='78b2b187-287d-4780-8dbd-a555731dd546'></a>

The ODEs, parameter values, and initial conditions are communicated to WinPP in a text file called an '-.ode' file (see Table 1). By opening this .ode file in WinPP.exe and clicking 'Run' 'Go,' one will generate Figure 4A, which simulates the temporal evolution of cyclin B, preMPF and active MPF in a cycling frog-egg extract. A comparison of the simulation to experimental observations shows that the model successfully reproduces the basic features of the egg extract: cyclin accumulates during interphase then is rapidly degraded at mitosis, and a time lag exists in which tyrosine-phosphorylated cyclin:Cdk dimers form, then these dimers are converted to the active form of MPF.

<a id='30b87ef2-260c-40e0-8363-1fcf8f161c11'></a>

The simulation represents the behavior of the cell cycle engine in an unperturbed extract. One could also vary parameters to represent experiments in which one or more components of the system is altered. For example, in a classic set of experiments by Solomon et al. (18), synthesis of endogenous cyclin was blocked by addition of cycloheximide, and extracts were supplemented with fixed amounts of recombinant, non-degradable cyclin B (Δcyclin B). As done originally by Novak and Tyson (1993), we can simulate this experiment by setting k₁ = V₂' = V₂" = 0 and setting the initial concentration of cyclin to a fixed value. By varying the initial concentration of cyclin (Figure 4B), we can draw two conclusions from the model. First

<a id='619ab44c-42ed-4f51-8414-18e4d76a1b07'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='b5354590-9d64-4109-bbeb-14c6f172396e'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='db431559-fc66-4960-9868-e3d34ab299ce'></a>

Sible and Tyson

<a id='6d9851a4-68b7-416c-b7f9-2aca19b6ac6a'></a>

Page 6

<a id='2d65924a-85b7-4a90-bc4c-e586816e6cc2'></a>

of all, the graph of active MPF over time indicates that the initial cyclin concentration must exceed a threshold (between 15 and 20 nM in Figure 4B) in order to activate MPF. This prediction agrees well with the experimental data (18). The simulation also suggests that as cyclin concentration approaches this activation threshold from larger values, the lag time to activate MPF becomes longer and longer. This prediction was first made by Novak and Tyson in 1993. Although no published studies showed evidence of this "critical slowing down," subsequent experiments confirmed this prediction (8). This example illustrates that mathematical models of the cell cycle can both be informed by and can inform experimental studies.

<a id='cf1e3706-288c-4c94-bcf9-0c85348dde1e'></a>

## 2.5 Parameter optimization
Initial simulations of the model, based on the original estimates of parameter values, may or may not approximate the behavior of the system to the modeler's satisfaction. The more qualitative data available to build the wiring diagram and quantitative data available to constrain the parameter values, the closer the simulations are likely to be to the biological system. However, rarely have all rate constants been measured, and estimates of initial conditions typically rely on semi-quantitative and relative data (such as that obtained by Western blotting). Therefore, most parameter sets will need to be optimized to bring the model and the biological system into better quantitative agreement. For relatively simple models, such as our example here, consisting of 7 ODEs and 24 kinetic constants, it may be possible to derive a satisfying parameter set "by hand," varying one parameter at a time and determining how well simulations match known behaviors of the system. However, this approach is inefficient and tedious, requires considerable advance knowledge of the system in order to make a good "starting guess" of the parameters, and is virtually impossible for more complex models consisting of many variables and many more parameters.

<a id='312012c4-f692-4daf-a630-0a4b3a9e040a'></a>

A collection of global parameter optimization tools is publicly available in the Gepasi modeling
platform (discussed below) (19). The choice of which tool to apply remains somewhat
empirical (19,20) and largely the realm of the theoretician.

<a id='4aea5eea-16df-4426-b23f-6ae3bba2b1cd'></a>

In our example of the cell cycle engine in frog egg extracts, a deterministic global optimizer (called VTDIRECT) followed by local optimization (using ODRPACK, an implementation of the Levenberg-Marquardt method) was applied to derive an optimized set of rate constants (21). Overall, simulations using the optimized parameter set give a better fit to the experimental data than simulations using the Marlovits parameter values (Table 1).

<a id='722d7867-ac73-4380-b903-d983878a8844'></a>

## 2.6 Experimental testing of the model

Once parameter optimization is used to bring a mathematical model into reasonable quantitative and qualitative agreement with existing experimental data, the next step is to test predictions made by the model experimentally. The rationale for doing so is twofold: the predictive ability of a model is a rigorous test of its accuracy, and more importantly, a major reason for building a model in the first place is to make novel predictions that inform subsequent rounds of experimentation. Virtually any experiment can be simulated in silico by varying parameter values in logical ways: (e.g. decreasing an enzyme's rate constant to represent the effect of a specific inhibitor, setting the rates of synthesis of all proteins to zero in the presence of cycloheximide, setting the rate of synthesis of a specific protein to zero for a gene deletion mutant, or setting the initial concentration of protein to zero for an immunodepletion).

Conditions that produce the most interesting and measurable cell behaviors are good candidates to test experimentally. Other considerations are whether or not the experiment is feasible (e.g. depleting a Cdk without removing associated cyclins could be problematic) and whether a particular experiment will help define ambiguous parts of the model (e.g. resolve uncertainties in the wiring diagram or constrain a parameter value).

<a id='6592ab9f-9f06-40de-a943-3b68b6a60413'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='e766dbb7-47af-476e-893c-485698175a4e'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='b18485e8-ff9b-4989-af08-498510fea0d1'></a>

Sible and Tyson

<a id='9e7e2d40-4500-4d5e-aa4f-4603b0eb320b'></a>

Page 7

<a id='aff70835-3d4c-4ebf-bcfc-fb209fa4479d'></a>

The interplay between modeling and experimentation is at its most valuable when a model can lead to novel, non-intuitive predictions about the behavior of the system. For example, Novak and Tyson's prediction that a hysteresis loop governs entry into and exit from mitosis in frog egg extracts (Figure 5A), was tested and validated experimentally (8,9). Using a modified protocol of Solomon et al. (18), in which cyclin levels were controlled in cycloheximide-treated extracts by the addition of exogenous nondegradable cyclin B, a variety of experiments indicated that higher levels of cyclin are required to enter mitosis than to stay in mitosis.
Another key prediction of the Novak-Tyson model is that, if the control of MPF activity by Wee1-dependent phosphorylation of Cdk1 is eliminated, then MPF activity continues to oscillate but at a higher frequency and smaller amplitude (compare Figures 4A and 5B). This prediction was validated experimentally in a series of clever experiments in which Wee1- and Cdc25-control loops were eliminated by adding a nonphosphorylatable Cdk1 (called the Cdc2AF mutant) and inhibiting endogenous Cdk1 (11). These elegant yet straightforward experiments were inspired by systems-level predictions derived from mathematical models rather than the published experimental studies that preceded them.

<a id='54c83b1c-81f4-468f-afa1-a5967fdba35f'></a>

Because the frog egg extract is biochemically tractable, experimental testing of the model was performed by biochemical manipulations, such as altering the concentration of cyclin in the system. Genetic approaches can be used to test both quantitative and qualitative predictions of the models that describe cell cycle networks in genetically tractable organisms. For example, a comprehensive mathematical model of the cell cycle control network in *Saccharomyces cerevisiae* describes the behavior of more than 100 genetic mutants (4,22). Rigorous tests of the model have been performed by creating new mutants predicted by the model to give the most informative phenotypes (23) and by challenging the model to predict phenotypes of yet unpublished mutants (24). Complete details of the model are available at an easily navigable web site: http://mpf.biol.vt.edu/research/budding_yeast_model/pp/.

<a id='4ce58138-6340-4e4b-b882-588ad5bf6c2d'></a>

## 3 Modeling tools and environments

The development of modeling "environments" that contain suites of tools necessary for model building, simulations, data fitting, and data management is an advancement that will benefit both experts and novices building models of molecular regulatory networks. The modeling environments described here are publicly available, relatively user friendly, and operate on personal computers running Windows, Macintosh, and/or Linux operating systems. Furthermore, each environment contains tools to translate models into the Systems Biology Markup Language (SBML), a grammar that is becoming widely adopted by the biochemical network modeling community to exchange models (25).

<a id='7a7bc38f-e3e1-4095-ba30-f90ec3c0dc87'></a>

## 3.1 Gepasi (http://www.gepasi.org)

Gepasi, the first package for modeling biochemical networks, was originally released in 1993 (26) and has been enhanced by regular additions and revisions (27). The current version (3.3) runs on Windows and Linux operating systems. Gepasi supports modeling of time course data in an environment that includes a graphical user interface (GUI) for model building, tools for simulations, and a collection of parameter estimation algorithms. Gepasi allows the definition of spatial compartments and includes a tool called MEG that allows modeling of spatially heterogeneous systems such as cell cultures or tissues (28). The environment also includes a number of tutorials to guide novice users through key aspects of the modeling environment. Although the Gepasi 3.3 is reported to be the last iteration, COPASI (complex pathway simulator), a new modeling environment based on Gepasi, is being developed. Test versions of COPASI are available at http://www.copasi.org. COPASI is designed to be more user-friendly, compatible with the latest versions of SMBL, and functional in Windows, Macintosh and Linux operating systems.

<a id='f5acbeac-18fd-4fb8-940a-1676c2ef1f16'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='37162e99-93fa-49a4-a657-6e751d4d6e81'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='a1e13741-5797-4b2a-97ea-b736f832266d'></a>

Sible and Tyson

<a id='2f7e229f-354b-452d-b7a3-28383642ba20'></a>

Page 8

<a id='e6ba4d47-792f-4998-9bb6-da78f0951fec'></a>

## 3.2 Virtual Cell (http://www.vcell.org)

Virtual Cell, a modeling environment created by the National Resource for Cell Analysis and Modeling, may be the most user-friendly for the non-expert (29). The current version, 4.0, can be run as a Java application or applet link on Windows, Macintosh OSX 10.1 and higher, and Linux operating systems. User support is available by e-mail. Programs for building models, running simulations, and managing documents are included, with plans for parameter estimation tools in Version 4.2. Virtual Cell places particular emphasis on modeling spatially distributed systems, providing tools to formulate and simulate partial differential equations (PDEs), which are better suited to represent spatiotemporal dynamics in cell signaling networks (30). Virtual Cell 4.1, available as a beta version, allows representation of 2- and 3-dimensional membrane diffusion and visualization of 3-dimensional surfaces. Virtual Cell utilizes its own language, VCML, which can be translated to SBML. A host of known incompatibilities between the two languages is documented on the Virtual Cell website.

<a id='cf46b446-22b9-42ac-8557-396391c59b79'></a>

### 3.3 Systems Biology Workbench (http://sbw.kgi.edu)
The Systems Biology Workbench (SBW) provides a suite of tools generically suited for modeling biochemical networks (31). The current version 2.5.0 operates in Windows, Linux and Macintosh OSX. SBW provides a GUI for model building (JDesigner) and a simulation tool (Jarnac) (32). Most importantly, SBW enables modeling applications written in diverse languages to communicate and operate together. The SBW group has worked for interoperability with the BioSPICE modeling projects, described below. SBW requires some background in dynamical systems and computer science to utilize the full suite of programs, but the basic operation of JDesigner/Jarnac is designed to be user-friendly.

<a id='b4cbc960-8946-42bb-9cd7-bc4220be0169'></a>

## 3.4 JigCell ( http://jigcell.biol.vt.edu )

JigCell is a modeling environment for Windows being developed as part of the larger DARPA BioSPICE effort (33,34). Although still a work-in-progress, JigCell includes a convenient spreadsheet-style Model Builder, a Run Manager for organizing related parameter sets and running multiple simulations (35), a Comparator for comparing simulations to experimental data (36), and a Parameter Estimator (21,37). Although JigCell is suited for modeling any biochemical network, it was developed with a particular emphasis on modeling the cell cycle. A model of the cell cycles of frog egg extracts (described above) and a model of the more complex budding yeast cell cycle have been used as test cases for developing the various components of JigCell, and these models are available on the website. JigCell is designed for interoperability with other modeling environments under the BioSPICE umbrella, and thus, is compatible with SBW as well.

<a id='9e02362a-6a51-437a-a77e-886c05fb3cb3'></a>

# 4 Conclusions

Because of the enormous body of data, the ability to test quantitative theoretical predictions in powerful biochemical and genetic systems, and the obvious value in deciphering this regulatory network, rigorous mathematical models of the eukaryotic cell cycle have been under development for over a decade, long before systems biology became fashionable. Early models were largely theoretical, and parameter values were based on scanty experimental measurements, back-of-envelope calculations, and a good deal of guesswork. However, in more recent years, serious collaborations between experimentalists and modelers have begun, and efforts to make modeling tools accessible to the non-expert have emerged. At present, we cannot provide a "recipe" or "kit" for building and using a mathematical model of your favorite molecular regulatory network. Serious work will probably require collaboration with professional modelers for the near future. However, we are confident that as computer tools get better and theoretical concepts seem more familiar, mathematical modeling will take its place in the molecular cell biologist's toolkit alongside SDS-PAGE and PCR!

<a id='c7fb7253-1faa-4873-b17f-0bfd17ac6fe4'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='2b70fef9-f4ba-4c88-a13c-64fc96bf55da'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='2f2a0b4e-0dab-4f17-8454-0fa1de85e524'></a>

Sible and Tyson

<a id='b75f1875-fb1e-4eb2-8246-8c84fc688bb3'></a>

Page 9

<a id='d29d60b9-514d-41ee-bae6-f91e478564e6'></a>

## 5 For further study

This review was written for the non-expert. We recommend as a first foray into modeling, that newcomers familiarize themselves with the example provided here and/or tutorial models found on the websites described in Section 3. For those interested in delving deeper into the theory and practice of modeling complex biochemical networks, we suggest the following literature:

(38) Fall, C. P., Marland, E. S., Wagner, J. M., and Tyson, J. J. (Eds.) (2000) Computational Cell Biology, Springer, Springer, New York.

(39) Tyson, J. J., Chen, K. C., and Novak, B. (2003) _Curr. Opin. Cell Biol._ **15**, 221-31.

(40) Lauffenburger, D. A., and Linderman, J. J. (1993) Receptors: models for binding, trafficking, and signaling, Oxford University Press, New York.

(41) Segel, L. A. (1989) Modeling dynamic phenomena in molecular and cellular biology, Cambridge University Press, New York.

(42) Goldbeter, A. (1996) Biochemical Oscillations and Cellular Rhythms: The molecular bases of periodic and chaotic behaviour, Cambridge University Press, New York.

<a id='aec4e5bb-3bc0-4eba-babf-0f5e88bdd1d3'></a>

## Acknowledgements
We thank the NIH (GM59688 to JCS) and DARPA/ARFL (F30602-01-2-0572 to JJT) for funding. Thanks for Dr. Brian Wroble for critical reading of this manuscript.

<a id='bcaf2ba1-1c83-411f-9ce4-f46376994e08'></a>

## References

<a id='ee846f5f-63e0-4740-971f-519310535c46'></a>

1. Aguda B. Proc Natl Acad Sci USA 1999;96:11352-57. [PubMed: 10500180]
2. Novak B, Tyson JJ. J Cell Sci 1993;106:1153-68. [PubMed: 8126097]
3. Goldbeter A. Proc Natl Acad Sci USA 1991;88:9107–11. [PubMed: 1833773]
4. Chen KC, Csikasz-Nagy A, Gyorffy B, Val J, Novak B, Tyson JJ. Mol Biol Cell 2000;11:369-91. [PubMed: 10637314]
5. Qu Z, Weiss JN, MacLellan WR. J Cell Sci 2004;117:4199-207. [PubMed: 15280433]
6. Qu Z, Weiss JN, MacLellan WR. Am J Physiol Cell Physiol 2003;284:C349-C64. [PubMed: 12388094]
7. Thron CD. Biophys Chem 1996;57:239-51. [PubMed: 8573678]
8. Sha W, Moore J, Chen K, Lassaletta A, Yi CS, Tyson J, Sible J. Proc Natl Acad Sci USA 2003;100:975-80. [PubMed: 12509509]
9. Pomerening JR, Sontag ED, Ferrell JEJ. Nat Cell Biol 2003;5:346-51. [PubMed: 12629549]
10. Xiong W, Ferrell JEJ. Nature 2003;426:460-65. [PubMed: 14647386]
11. Pomerening JR, Kim SY, Ferrell JEJ. Cell 2005;122:565-78. [PubMed: 16122424]
12. Bai S, Goodrich D, Thron CD, Tecarro E, Obeyesekere M. Cell Cycle 2003;2:46-52. [PubMed: 12695688]
13. Felix MA, Labbe JC, Doree M, Hunt T, Karsenti E. Nature 1990;346:379–82. [PubMed: 2142754]
14. Kramer ER, Gieffers C, Holzl G, Hengstschlager M, Peters JM. Curr Biol 1998;8:1207-10. [PubMed: 9811605]
15. Hershko A. Philos Trans R Soc Lond B Biol Sci 1999;354:1571–75. [PubMed: 10582242]
16. Lorca T, Castro A, Martinez AM, Vigneron S, Morin N, Sigrist S, Lehner C, Doree M, Labbe JC. EMBO J 1998;17:3565-75. [PubMed: 9649427]
17. Kumagai A, Dunphy WG. Mol Biol Cell 1995;6:199-213. [PubMed: 7787246]
18. Solomon MJ, Glotzer M, Lee TH, Phillippe M, Kirschner MW. Cell 1990;63:1013–24. [PubMed: 2147872]
19. Mendes P, Kell DB. Bioinformatics 1998;14:869-83. [PubMed: 9927716]

<a id='0a072f67-2bf4-4089-9fd3-e529510f6eea'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='d0d3d808-d118-4eb5-b2b3-69aee40170f1'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='df01a993-2e7a-4bc2-b79a-9f598279362a'></a>

Sible and Tyson

<a id='24a28bee-c638-464a-95f4-42655c650242'></a>

Page 10

<a id='4c028a3f-a2c5-4ce6-8281-c43da46860ce'></a>

20. Moles CG, Mendes P, Banga JR. Genome Res 2003;13:2467–74. [PubMed: 14559783]
21. Zwolak JW, Tyson JJ, Watson LT. J Comput Biol 2005;12:48–63. [PubMed: 15725733]
22. Chen KC, Calzone L, Csikasz-Nagy A, Cross FR, Novak B, Tyson JJ. Mol Biol Cell 2004;15:3841–
62. [PubMed: 15169868]
23. Cross FR, Archambault V, Miller M, Klovstad M. Mol Biol Cell 2002;13:52–70. [PubMed:
11809822]
24. Cross FR, Schroeder L, Kruse M, Chen KC. Mol Biol Cell 2005;16:2129–38. [PubMed: 15716353]
25. Hucka M, Finney A, Sauro HM, Bolouri H, Doyle JC, Kitano H, Arkin AP, Bornstein BJ, Bray D,
Cornish-Bowden A, Guellar AA, Dronov S, Gilles ED, Ginkey M, Gor V, Goryanin II, Hedley WJ,
Hodgman TC, Hofmeyr JH, Hunter PJ, Juty NS, Kasberger JL, Kremling A, Kummer U, Novere NL,
Loew LM, Lucio D, Mendes P, Minch E, Mjolsness EJ, Nakayama Y, Nelson MR, Nielsoen PF,
Sakurada T, Schaff JC, Shapiro BE, Shimizu TS, Spence HD, Stelling J, Takahashi K, Tomita M,
Wagner J, Wang J. Bioinformatics 2003;19:524–31. [PubMed: 12611808]
26. Mendes P. Comput Appl Biosci 1993;9:563–71. [PubMed: 8293329]
27. Mendes P. Trends Biochem Sci 1997;22:361–63. [PubMed: 9301339]
28. Mendes P, Kell DB. Bioinformatics 2001;17:288–89. [PubMed: 11294797]
29. Moraru II, Schaff JC, Slepchenko BM, Loew LM. Ann, NY Acad Sci 2002;971:595–96. [PubMed:
12438191]
30. Eungdamrong NJ, Iyengar R. Biol Cell 2004;96:355–62. [PubMed: 15207904]
31. Sauro HM, Hucka M, Finney A, Wellock C, Bolouri H, Doyle J, Kitano H. OMICS 2003;7:355–72.
[PubMed: 14683609]
32. Sauro, HM.; Hofmeyr, J-HS.; Rohwer, JM.; Snoep, JL. Animating the Cellular Map; Proceedings of
the 9th International Meeting on BioThermoKinetics; Stellenbosch University Press. 2000. p. 221–28.
33. Allen NA, Calzone L, Chen KC, Ciliberto A, Ramakrishnan N, Shaffer CA, Sible JC, Tyson JJ, Vass
MT, Watson LT, Zwolak JW. OMICS 2003;7:285–99. [PubMed: 14583117]
34. Allen NA, Shaffer CA, Ramakrishnan N, Vass MT, Watson LT. Simulation 2003;79:674–88.
35. Vass MT, Allen NA, Shaffer CA, Ramakrishnan N, Watson LT, Tyson JJ. Bioinformatics
2004;20:3680–81. [PubMed: 15273159]
36. Allen NA, Shaffer CA, Ramakrishnan N, Vass MT, Watson LT. Simulation 2005;79:674–88.
37. Zwolak JW, Tyson JJ, Watson LT. IEE Proc-Syst Biol 2005;152:81–92. [PubMed: 17044236]
38. Fall, CP.; Marland, ES.; Wagner, JM.; Tyson, JJ., editors. Computational Cell Biology. Springer,
Springer; New York: 2000.
39. Tyson JJ, Chen KC, Novak B. Curr Opin Cell Biol 2003;15:221–31. [PubMed: 12648679]
40. Lauffenburger, DA.; Linderman, JJ. Receptors: models for binding, trafficking, and signaling. Oxford
University Press; New York: 1993.
41. Segel, LA. Modeling dynamic phenomena in molecular and cellular biology. Cambridge University
Press; New York: 1989.
42. Goldbeter, A. Biochemical Oscillations and Cellular Rhythms: The molecular bases of periodic and
chaotic behaviour. Cambridge University Press; New York: 1996.
43. Marlovits G, Tyson CT, Novak B, Tyson JJ. Modeling M-phase control in Xenopus oocyte extracts:
the surveillance mechanism for unreplicated DNA. Biophys Chem 1998;72:169–184. [PubMed:
9652093]

<a id='a9b89fa5-d30d-4713-9e0e-8eed607eb4f7'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='b20246fa-43db-408e-9946-1de0d697aa1f'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='ad0284fb-8bd8-45ae-9774-1f908bbe0a2e'></a>

Sible and Tyson

<a id='aef3ea0d-d510-434c-b401-159c31dd77e4'></a>

Page 11

<a id='75944fa7-a8cb-46cb-bd31-06d7d6af1d13'></a>

<::A biological pathway diagram illustrates the regulation of Cdk1-Cyclin activity. The pathway begins with `amino acids` leading to the synthesis of `Cyclin`. `Cyclin` then binds with `Cdk1` to form a complex. This complex can exist in two main phosphorylation states: an inactive `P-Cdk1-P-Cyclin` form and an active `Cdk1-P-Cyclin` form. The interconversion between these states is regulated by `Cdc25` and `Wee1`. `Cdc25` dephosphorylates `P-Cdk1-P-Cyclin` to activate `Cdk1-P-Cyclin`. Conversely, `Wee1` phosphorylates `Cdk1-P-Cyclin` to inactivate it as `P-Cdk1-P-Cyclin`. Both `Cdc25` and `Wee1` can also be phosphorylated: `Cdc25` interconverts with `P-Cdc25`, and `Wee1` interconverts with `Wee1-P`. The active `Cdk1-P-Cyclin` complex provides positive feedback by activating `Cdc25` (dashed arrow) and negative feedback by inhibiting `Wee1` (dashed arrow). The active `Cdk1-P-Cyclin` complex also activates an intermediate `IE` (shown in two states, one phosphorylated with a green P), which in turn activates `APC` (Anaphase-Promoting Complex). `APC` exists in `OFF` and `ON` states, interconverting. The `APC ON` state leads to the degradation of `Cyclin` into `degraded cyclin`, releasing `Cdk1`. The `APC ON` state is depicted with an open mouth, while `APC OFF` is closed. A green circle labeled `P` represents a phosphate group.: pathway diagram::>

<a id='b8afdd3d-dad9-4878-8a74-3bddfc67e611'></a>

Figure 1.
Wiring diagram of the core mitotic cell cycle engine in *Xenopus* cell-free egg extracts. Central to the diagram is the active cyclin-Cdk1 complex (also referred to as MPF), with activating phosphorylation on Thr 161 indicated by the green 'P'. Cyclin enters the system by de novo synthesis and then combines with Cdk1. The phosphorylation on Thr 161 is rapid and therefore not represented in the diagram or the mathematical equations. Active Cdk1 can be phosphorylated on Thr 14 and Tyr 15 to form inactive preMPF. The double arrows indicate the reversibility of this process. The inhibitory phosphates are represented by the red 'P'; and the influences of the relevant kinase (Wee1) and phosphatase (Cdc25C) are indicated by the dotted arrows. MPF itself phosphorylates Cdc25 and Wee1, positively and negatively affecting their activities, respectively. These feedback loops are easily appreciated from the wiring diagram. MPF also participates in a negative feedback loop whereby it phosphorylates a component of the APC, which subsequently directs the polyubiquitination of cyclin, tagging it for degradation by the proteasome. Like cyclin synthesis, cyclin degradation is represented by a single unidirectional arrow because the process is irreversible. Although not indicated in the diagram, cyclin degradation by the APC applies equally to free cyclin monomers and to preMPF. IE indicates an Intermediate Component (see text).

<a id='a0d416ed-1ee6-4afe-9587-d9dac934b508'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='724a0d49-9684-4dbb-be05-d3b147157f7a'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='dcdfefff-d6c4-47f4-a0e7-3caff5af584e'></a>

Sible and Tyson

<a id='6cb41983-a2ed-42f7-b1d0-672761c0235a'></a>

Page 12

<a id='0a8d7965-d2ab-4c94-8242-26c55ab619c2'></a>

1. d/dt [Cyclin] = k1 - k2 [Cyclin] - k3 [Cyclin] [Cdk]
2. d/dt [MPF] = k3 [Cyclin] [Cdk] - k2 [MPF] - kwee [MPF] + k25 [preMPF]
3. d/dt [preMPF] = - k2 [preMPF] + kwee [MPF] - k25 [preMPF]
4. d/dt [Cdc25P] = (ka [MPF] ([total Cdc25] - [Cdc25P])) / (Ka + [total Cdc25] - [Cdc25P]) - (kb [PPase] [Cdc25P]) / (Kb + [Cdc25P])
5. d/dt [Wee1P] = (ke [MPF] ([total Wee1] - [Wee1P])) / (Ke + [total Wee1] - [Wee1P]) - (kf [PPase] [Wee1P]) / (Kf + [Wee1P])
6. d/dt [IEP] = (kg [MPF] ([total IE] - [IEP])) / (Kg + [total IE] - [IEP]) - (kh [PPase] [IEP]) / (Kh + [IEP])
7. d/dt [APC] = (kc [MPF] ([total APC] - [APC])) / (Kc + [total APC] - [APC]) - (kd [PPase] [APC]) / (Kd + [APC])
8. [Cdk] = [Total Cdk] - [MPF] - [preMPF]
9. k25 = V25' ([Total Cdc25] - [Cdc25P]) + V25'' [Cdc25P]
10. kwee = Vwee' [Wee1P] + Vwee'' ([Total Wee1] - [Wee1P])
11. k2 = V2' ([Total APC] - [APC*]) + V2'' [APC*]

<a id='74b86718-80c8-466d-b578-c303c70d9f48'></a>

Figure 2.
Mathematical model of the cell cycle control network in frog egg extracts (2). ODEs describe
the rate of change in concentration of every non-constant species in the wiring diagram in
Figure 1.

<a id='a038fb8c-5000-41b2-9c35-eda43f7e27c0'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='90233c4c-b0b1-4ff0-a4ff-9e2c9d7ccd7b'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='783dcf0f-4a88-483a-945f-87893ce2f3ea'></a>

Sible and Tyson

<a id='5e17d4dc-66d8-40af-bb4e-0179693c14e4'></a>

Page 13

<a id='0dd327f0-a414-4909-baec-fac0571cacc1'></a>

C a b c d e f g h i j k l m n o p q r s

<a id='be7829f8-6fac-4c82-9192-e5741c49dadf'></a>

<::Gel electrophoresis image (likely a Western blot) showing bands for 'cdc2-' protein. The image displays the protein's presence or modification under various conditions and time points.

**Labels:**
- **Y-axis label:** cdc2-
- **X-axis conditions and time points (in minutes):**
  - **M-phase:** 0, 4, 16
  - **- APC:** 0, 2, 4, 8, 16
  - **+ APC:** 0, 2, 4, 8, 16
  - **+ CAFF:** 0, 2, 4, 8, 16
- The very last label on the x-axis indicates "0 min".

The bands vary in intensity and possibly migration, suggesting changes in cdc2 protein levels or post-translational modifications across the different experimental conditions and time points.
: gel electrophoresis::>

<a id='e8150d30-d17d-4b35-9228-7405da2f1f4b'></a>

Figure 3.
Experimental data used to estimate the value of Vwee" in the Novak-Tyson model of the cell
cycle in frog egg extracts. Data are from Figure 3C of Kumagai and Dunphy, 1995 (17). "Cdc2"
refers to Cdk1 (lower band is unphosphorylated on Wee1 sites and upper band is
phosphorylated on Wee1 sites). APC = aphidicolin, an inhibitor of DNA replication and CAFF
= caffeine, an inhibitor of cell cycle checkpoint kinases.

<a id='c99a3706-2e31-4dd4-8d25-93732ba8bce1'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='62c17dbb-4adb-4331-800c-6727275c88dc'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='1e9b1a0d-8cbe-466e-a7a3-e9bb072d359f'></a>

Sible and Tyson

<a id='71744708-a376-49e4-90ac-da4fcb4d11a9'></a>

Page 14

<a id='efe661d5-1f38-421e-a027-d18cd3c62a12'></a>

<::Line graph showing concentration (nM) versus time (min). The x-axis ranges from 0 to 200 min, and the y-axis ranges from 0 to 25 nM. Three curves are plotted: 'total cyclin', 'MPF', and 'pre-MPF'. The 'total cyclin' curve peaks highest, followed by 'MPF', and then 'pre-MPF' peaks lowest. All three curves show oscillatory behavior, with 'total cyclin' reaching concentrations above 20 nM, 'MPF' peaking around 18 nM, and 'pre-MPF' peaking around 5 nM. The graph indicates a period of 55 min for these oscillations.: chart::>

<a id='2c499201-10da-4564-a60c-a686200fb4bf'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='eadd1b59-5972-45f0-a760-5c6508229d5c'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='12bfdc4a-a263-4c26-97c6-b01507797c26'></a>

Sible and Tyson

<a id='2f2f2965-55b4-4185-aecc-23f544733935'></a>

Page 15

<a id='1aec4151-1fea-479e-bce7-ec74b9aa8cc6'></a>

<::line chart::> Figure 4. The chart displays the concentration of MPF ([MPF] in nM) on the y-axis against time (min) on the x-axis. The y-axis ranges from 0 to 80 nM, and the x-axis ranges from 0 to 40 minutes. Multiple curves are plotted, each representing a different total cyclin concentration. The curves are labeled on the right side with their respective total cyclin concentrations: 15, 20, 30, 40, 50, 60, 70, and 80 nM. The curve labeled "total cyclin = 80 nM" shows the highest MPF concentration, reaching approximately 75 nM at 40 minutes. Lower total cyclin concentrations result in lower peak MPF concentrations and longer delays in MPF accumulation. For instance, the curve for 15 nM total cyclin shows MPF levels remaining very low, barely rising above 5 nM, while the 20 nM curve shows MPF reaching about 15 nM at 40 minutes. Simulations of the mathematical model of the cell cycle in frog egg extracts describe known and previously unobserved behaviors of the control system. A) Simulation of the changes in cyclin, preMPF and MPF levels over time in a cycling frog egg extract (2). Computed from the 'ode' file in Table 1. The simulations are consistent with a body of experimental data. B) Simulations of the lag time into mitosis after addition of various fixed concentrations of nondegradable cyclin B. Computed from the 'ode' file in Table 1, with k₁ = V2' = V2" = 0. The lengthening lag times at progressively lower concentrations of cyclin B was not validated experimentally until 2003, when sufficiently small increments in cyclin B were used for the experiments (8). <::/line chart::>

<a id='88d9e338-655d-478f-84ff-5698988c395d'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='83a49ed8-3ae5-4364-b47e-e8944fd6f099'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='9b66b547-ee99-4e70-a705-2835f9f5264a'></a>

Sible and Tyson

<a id='e61f1809-b593-48f6-92f4-db5ac55d07df'></a>

Page 16

<a id='1014f391-ffe9-4ac4-b70a-a792283a37ac'></a>

<::Graph showing MPF activity as a function of cyclin level.: chart::>The x-axis is labeled "cyclin level" with two specific points marked as T_i and T_a. The y-axis is labeled "MPF activity." The graph displays a sigmoidal-like curve with hysteresis. At low cyclin levels, MPF activity is low, represented by a solid line with black circular data points. As the cyclin level increases, MPF activity remains low until T_a, where it sharply transitions to a high activity state, indicated by an upward arrow. In the high activity state, MPF activity increases with cyclin level, shown by a solid line with gray and black circular data points. If the cyclin level then decreases, MPF activity remains high until T_i, where it sharply transitions back to the low activity state, indicated by a downward arrow. A dashed line connects the low and high activity states, representing an unstable or intermediate region between T_i and T_a.

<a id='acf637ec-b3e4-4187-9243-9ecf9aafcc46'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='e3753867-0b0d-46db-8866-363964018b27'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='d9544e6c-9475-43f4-8c5f-504de0557fea'></a>

Sible and Tyson

<a id='832e5ebd-d187-4411-b8be-e4c18ec89f7c'></a>

Page 17

<a id='e52a1e4a-29eb-4da3-b0b8-468b9bc18bac'></a>

<::A line graph titled "concentration (nM)" on the y-axis and "time (min)" on the x-axis. The y-axis ranges from 0 to 25, and the x-axis ranges from 0 to 200. Two lines are plotted, both showing oscillating behavior. The upper line is labeled "total cyclin" and the lower line is labeled "MPF". Both lines start at approximately 0 concentration at time 0, rise to a peak around 12-13 nM for total cyclin and 10-11 nM for MPF at approximately 35 minutes, then decrease, and repeat this oscillating pattern with a period of about 47 minutes. The text "(V'wee = V''wee = 0)" and "period = 47 min" is displayed in the upper right corner of the plot area.: chart::>

<a id='42dc5079-c799-4e92-bd4b-24891677556f'></a>

Figure 5.
Theoretical predictions from Novak and Tyson (2). A) Hysteresis drives mitotic transitions in frog egg extracts. The simulation indicates that the concentration of cyclin required to drive high MPF activity (and thereby enter mitosis) is higher than the concentration required to maintain high MPF activity (and thereby stay in mitosis). For the Marlovits parameter set, Table 1, T₁ = 8 nM and Tₐ = 17 nM. The theoretical prediction of two distinct thresholds was confirmed experimentally (8,9). B) MPF oscillations are faster and smaller if Cdk1 is not phosphorylatable by Wee1. Computed from the 'ode' file in Table 1, with Vwee' = Vwee" = 0. This prediction was confirmed experimentally by Pomerening et al. (11).

<a id='2b0aa9b9-84b6-4665-8fef-7a1831f6e545'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='e62d3388-f0e9-478a-b66e-05044234bc7a'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='d6afddee-3b23-4533-a21b-53b2a563f7d9'></a>

Sible and Tyson

<a id='622d3ded-0684-45f2-abb5-720c115b9316'></a>

Page 18

<a id='6d55c217-638b-4d02-8ef4-e28438bc9903'></a>

Table 1
Input file for WinPP to reproduce Figure 4.

# A model of MPF regulation in frog egg extracts
# after (Novak & Tyson, J. Cell Sci., 1993)
# Warning: WinPP and XPP are case insensitive.
# Differential Equations (Figure 2)
dCyclin/dt = k1 - k2*Cyclin - k3*Cyclin*Cdk
dMPF/dt = k3*cyclin*Cdk - k2*MPF - kwee*MPF + k25*preMPF
dpreMPF/dt = kwee*MPF - k25*preMPF - k2*preMPF
dCdc25P/dt = F(TotCdc25-Cdc25P,MPF,ka,KKa) - F(Cdc25P,PPase,kb,KKb)
dWee1P/dt = F(TotWee1-Wee1P,MPF,ke,KKe) - F(Wee1P,PPase,kf,KKf)
dIEP/dt = F(TotIE-IEP,MPF,kg,KKg) - F(IEP,PPase,kh,KKh)
dAPC/dt = F(TotAPC-APC,IEP,kc,KKc) - F(APC,PPase,kd,KKd)
# Conservation of Cdk subunits
Cdk = TotCdk - MPF - preMPF
# Rate functions embodying the regulatory signals
k25 = V25'*(TotCdc25-Cdc25P) + V25"*Cdc25P
kwee = Vwee'*Wee1P + Vwee"*(TotWee1-Wee1P)
k2 = V2'*(TotAPC-APC) + V2"*APC
# Michaelis-Menten Rate Law
F(S,E,k,Km) = k*E*S/(Km+S)
# Parameter values (from Marlovits et al., (43))
par k1=1, V2'=.005, V2"=.25, k3=.005
par V25'=.017, V25"=.17, Vwee'=.01, Vwee"=1
par ka=.02, KKa=.1, kb=.1, KKb=1
par kc=.13, KKc=.01, kd=.13, KKd=1
par ke=.02, KKe=.1, kf=.1, KKf=1
par kg=.02, KKg=.01, kh=.15, KKh=.01
par TotCdk=100
# These parameters are arbitrarily set to 1.
par TotCdc25=1, TotWee1=1, TotIE=1, TotAPC=1, PPase=1
# Initial conditions
init Cyclin=0, MPF=0, preMPF=0, Cdc25P=0, Wee1P=0, IEP=1, APC=1
# Define "auxiliary" variables for plotting purposes
aux TotCyclin=cyclin+MPF+preMPF
aux Wee1=10*(TotWee1-Wee1P)
# Simulator settings
@ meth=stiff, Total=200, Bounds=1000
# Plotter settings
@ xhi=200, ylo=0, yhi=25
@ nplot=2, yp2=MPF
done

<a id='cd2ee916-8ac5-4c16-a6c1-4ea517c042aa'></a>

Methods. Author manuscript; available in PMC 2007 September 24.

<a id='2c575093-c6b3-4a9c-b85f-a83c6800079c'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript