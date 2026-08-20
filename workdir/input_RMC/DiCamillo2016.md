<a id='d49ec9f8-fe96-47c5-9bbf-02c80e37a5e3'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38
DOI 10.1186/s12918-016-0281-4

<a id='286a2b9b-fe47-4abc-9086-261ea5e2751d'></a>

BMC Systems Biology

<a id='fb1ebc0e-d438-4293-b22c-aa29f82bbac7'></a>

RESEARCH ARTICLE                                                     Open Access

<a id='0c066f38-7134-4812-94b6-ba7177703325'></a>

A rule-based model of insulin signalling pathway

<a id='681bdca2-082a-49d3-b97a-e15ab7ee4b3c'></a>

<::logo: CrossMark
CrossMark
The logo features a red bookmark icon within a blue and grey circle.::>

<a id='8006bf33-a872-4158-ab39-3fec91e61580'></a>

Barbara Di Camillo¹, Azzurra Carlon ¹,², Federica Eduati¹,³ and Gianna Maria Toffolo¹*

<a id='1a124440-390d-4f00-a3d2-96b12aa47fe6'></a>

## Abstract

**Background:** The insulin signalling pathway (ISP) is an important biochemical pathway, which regulates some fundamental biological functions such as glucose and lipid metabolism, protein synthesis, cell proliferation, cell differentiation and apoptosis. In the last years, different mathematical models based on ordinary differential equations have been proposed in the literature to describe specific features of the ISP, thus providing a description of the behaviour of the system and its emerging properties. However, protein-protein interactions potentially generate a multiplicity of distinct chemical species, an issue referred to as "combinatorial complexity", which results in defining a high number of state variables equal to the number of possible protein modifications. This often leads to complex, error prone and difficult to handle model definitions.

<a id='6b5f47cb-c91c-4a19-8819-6eb095bce90b'></a>

**Results:** In this work, we present a comprehensive model of the ISP, which integrates three models previously available in the literature by using the rule-based modelling (RBM) approach. RBM allows for a simple description of a number of signalling pathway characteristics, such as the phosphorylation of signalling proteins at multiple sites with different effects, the simultaneous interaction of many molecules of the signalling pathways with several binding partners, and the information about subcellular localization where reactions take place. Thanks to its modularity, it also allows an easy integration of different pathways. After RBM specification, we simulated the dynamic behaviour of the ISP model and validated it using experimental data. We the examined the predicted profiles of all the active species and clustered them in four clusters according to their dynamic behaviour. Finally, we used parametric sensitivity analysis to show the role of negative feedback loops in controlling the robustness of the system.

<a id='3ea8d24c-618a-45fa-a8c9-0963894779f5'></a>

Conclusions: The presented ISP model is a powerful tool for data simulation and can be used in combination with experimental approaches to guide the experimental design. The model is available at http://sysbiobig.dei.unipd.it/ was submitted to Biomodels Database (https://www.ebi.ac.uk/biomodels-main/# MODEL 1604100005).

<a id='a520264d-ade0-4480-b977-eadfcfeb0ca2'></a>

Keywords: Insulin signalling pathway, Rule-based modelling, Parametric sensitivity analysis, System robustness

<a id='fc14488a-5ade-4d0b-8ac2-f3f2b782ebea'></a>

**Background**
Biological systems, such as cell signalling pathways, act sensing input stimuli (e.g. extracellular ligands), and transmitting, processing and integrating this information to provide output signals able to regulate many essential cellular activities. Alterations in such information processing capability play a crucial role in the development of a disease state in many cell types [1,2].

<a id='5717af76-5980-454d-a881-b491bd6f5645'></a>

Mathematical models are often used to understand the
functioning of biological systems, thus providing a

<a id='81795ed5-ff75-47ce-8638-76884331613e'></a>

* Correspondence: toffolo@dei.unipd.it
^1Department of Information Engineering, University of Padova, Via Gradenigo
6A, Padova 35131, Italy
Full list of author information is available at the end of the article

<a id='fbc76341-1c90-4272-9812-1e7b4a83663a'></a>

description of the behaviour of the system and allowing useful analysis of its emerging properties [3]. Moreover, mathematical models are powerful tools for data simulation and can be used in combinations with experimental approaches to guide the experimental design, whereas data collected from experiments may help validating and refining the computational models [4].

<a id='024a7d28-0141-44b3-ae9e-167a83979b19'></a>

Signalling pathways are usually modelled using ordin-
ary differential equations (ODEs), able to quantitatively
describe the dynamics of the chemical species, in terms
of mass action law and kinetic rate constants related to
the speed of the chemical reactions occurring among the
interacting species [5]. As a simpler alternative, logic-
based models [6] have been also used. A detailed

<a id='6374707a-f6d6-478a-b110-363f5c2e383f'></a>

<::logo: BioMed Central
BioMed Central
The logo features a circular icon with a blue and green segmented ring next to the company name in blue and dark gray text.::>

<a id='767b237a-144e-4338-bfad-848c089934e9'></a>

&#169; 2016 Di Camillo et al. Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.

<!-- PAGE BREAK -->

<a id='289d8ace-b34f-4de0-8581-73b0725a34bc'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='d33ed885-bb2a-49df-84b1-882400605f9c'></a>

Page 2 of 13

<a id='f2f4f55b-6e98-4106-963e-ea38df33207b'></a>

description of a signalling pathway requires including site-specific details of protein-protein interactions, since signalling proteins contain multiple functional domains and several sites of post-translational modifications. However, protein-protein interactions potentially gener-ate a multiplicity of distinct chemical species, an issue referred to as "combinatorial complexity" [7]. Adopting ODEs to represent such complexity would require using a number of state variables equal to the number of pos-sible protein modifications, thus making model specifi-cation tedious and error-prone.

<a id='5dacbde6-10c8-4523-a6b2-0a1321a65a6f'></a>

In order to deal with the combinatorial complexity of signalling pathways, a novel approach for model specifi-cation known as Rule-based Modelling (RBM), has been introduced in the past years, able to deal with the de-scription of all molecular interactions in a more efficient and compact way [8–10]. RBM is based on the key as-sumption of ‘modularity’, i.e. the assumption that mo-lecular interactions only depend on local properties of the proteins [11,12]. According to this assumption, clas-ses of reactions involving the same components are de-fined by means of a ‘rule’ and are associated with the same rate law. Models specified using RBM can then be used for simulation using a number of different population-based or particle-based methods [13]. In particular, the rules specified can be used to automatic-ally generate a system of ODEs, which can then be simu-lated [10].

<a id='e031a3e0-960e-4426-949f-4b66bf991ab2'></a>

An impressive example of the power of RBM is represented by the specification of the epidermal growth factor (EGF) receptor signalling, in which the interaction among 10^23 distinct chemical species was codified by the use of only 70 rules [14]. As a more recent example, the specification of the complex ERBB receptor signalling network required 544 rules accounting for 18 proteins, over 30 protein domains, several linear motifs, and 56 sites of lipid and protein phosphorylation [12].

<a id='e2996ecd-47a3-40e3-a617-f48989dff641'></a>

An important advantage of RBM resides in its modu-
larity, which facilitates the integration of different path-
ways, as well as the model extension, when new
knowledge becomes available.

<a id='257bad6e-572a-4fc6-a9ed-1683bbd478ce'></a>

In this work, we present a model of the insulin signal-ling pathway (ISP), based on RBM. ISP is one of the most important signalling network, which regulates some fundamental biological functions such as glucose and lipid metabolism, protein synthesis, cell prolifera-tion, cell differentiation and apoptosis. These different biological responses are achieved by the insulin binding to its receptor and by the subsequent combined activa-tion of three major pathways:

<a id='13e666b3-26bf-4a03-a6f5-868a935a5549'></a>

(i). The PI3K-AKT pathway, mostly responsible for the metabolic insulin action via the translocation of the glucose transporter type 4 (GLUT4) vesicles to the

<a id='42aced34-0d4c-47c6-8711-f2656c86d29c'></a>

plasma membrane, which, in turn, allow the glucose uptake in muscle cells and adipocytes [15];

(ii). The TSC1/2-mTOR pathway, playing a critical role in protein synthesis since mammalian target of rapamycin (mTOR) is a central controller for several anabolic and catabolic processes including RNA translation, ribosome biogenesis and autophagy, in response not only to growth factors and hormones like insulin, but also to nutrients, energy and stress signals [16];

(iii). The RAS-MAPK pathway, promoting cell survival, division and motility via extracellular signal-regulated kinase 1/2 (ERK1/2) complex that, once phosphorylated, translocates into the nucleus activating many transcription factors, thus constituting an important connection between the cytoplasmic and nuclear events [17].

<a id='0669fa9e-d40d-4693-985d-6f0a15082f2d'></a>

Several mathematical models of ISP have been published in the last 10 years, focused on different aspects of insulin regulation, including: insulin binding to its receptor [18]; insulin receptor autophosphorylation and subsequent phosphorylation of its substrate together with receptor cycling and endocytosis [19,20]; insulin signalling in insulin resistance state in human adipocytes [21]; translocation of GLUT4 glucose transporter [22]; regulation of mTOR [23,24]; joint regulation of insulin and amino acids [25]; crosstalk with epidermal growth factor (EGF) signalling and the mitogen-activated protein kinase (MAPK) pathway [26].

<a id='53a1f115-8f1b-4bf7-ac6c-a15997e6303d'></a>

In this work, we adapted and integrated the informa-
tion provided by three published models [22,24,26] to
implement, up-to our knowledge, the most comprehen-
sive model of the ISP. The three above listed models de-
scribe, using ODEs, the PI3K-AKT, the mTOR and the
RAS-MAPK pathway, respectively, thus covering most
of the essential regulatory mechanisms characterizing
the ISP. The RBM approach was used to implement our
ISP model. This was then partially validated by compar-
ing the model predictions with measurements of some
phosphorylated proteins involved in ISP, such as pAKT-
S473, ppERK1/2-T202-Y204 and pmTOR-S2448. The
model was then used as an in silico tool to predict the
profiles of all the chemical species during insulin per-
turbation and to analyse, by means of parametric sensi-
tivity analysis [27,28], the role of negative feedback loops
in controlling the robustness of the system.

<a id='65996580-0eff-4cbf-a8fc-9defc38a062a'></a>

## Results and discussion
The model of insulin signalling pathway
Starting from three published models [22,24,26], we im-
plemented the model of ISP as depicted in Fig. 1 using
the Systems Biology Graphical Notation [29].

<!-- PAGE BREAK -->

<a id='be746400-562d-4eeb-a8c4-261d56ed1646'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='0693b201-8c83-49f8-92e9-5022fd71a67d'></a>

Page 3 of 13

<a id='a83208ac-5e4b-4bd8-a5f6-f9345af69530'></a>

<::flowchart: The model of insulin signalling pathway, depicted using the Systems Biology Graphical Notation (SBGN). The diagram illustrates the integration of the PI3K-AKT pathway, the mTOR pathway, and the RAS-MAPK pathway. Various proteins and their interactions are shown within the context of the cell membrane and cytoplasm. The legend defines symbols for Catalysis (circle with cross), Modulation (circle), Complex formation (filled circle), and Complex dissociation (circle with dot). Specific components and their states are color-coded, resembling clustering results, and important feedback mechanisms are highlighted with colored lines. Top Section: - Insulin binds to the Insulin Receptor (IR) at the cell membrane, leading to its phosphorylation (pY). - IR is regulated by PTP/AKT. - RASGAP interacts with IR. - SHP2 interacts with IRS1. Left/RAS-MAPK Pathway: - SRC exists in inactive and active (blue) states. - GRB2/SOS (active (green) and inactive) interacts with IRS1. - RAS (GDP and GTP forms) is activated. - C-RAF exists in inactive, active (purple), and double active (purple) states. - MEK (purple) is activated by C-RAF. - ERK1/2 (purple, pT1, pT2) is activated by MEK. - A blue line represents the ERK1/2-GRB2/SOS negative feedback loop. Middle/PI3K-AKT and mTOR Pathways: - IRS1 (pY, pS) interacts with PI3K (green). - PI3K converts PI(4,5)P2 (green) to PI(3,4,5)P3 (green). - PTEN and SHIP regulate PI(3,4,5)P3, which can be converted to PI(3,4)P2 (green). - AKT (blue, pT, pS) is activated. - PKC-ζ (green) is shown. - AMPK (blue, pT) activates TSC1/2 (yellow, pS). - mTORC1 (yellow, pS) is inhibited by TSC1/2 and activated by Aminoacids. - p70S6K (yellow, pT) is activated by mTORC1. - A red line represents the P70S6K-IRS1 negative feedback loop, where p70S6K inhibits IRS1. Right Section: - PI3Kvariant (blue) and mTORC2 (yellow, pS) are involved. - GLUT4 (yellow) translocates to the cell membrane. Fig. 1 The model of insulin signalling pathway. The model of Insulin Signaling Pathway obtained by integrating the PI3K-AKT pathway, the mTOR pathway and the RAS-MAPK pathway, depicted using the Systems Biology Graphical Notation. Coloured nodes resemble the clustering results obtained on simulated profiles (see Fig. 3). Coloured lines represent important feedback mechanisms; namely: the red line represents the P70S6K-IRS1 negative feedback loop, the blue line the ERK1/2-GRB2/SOS negative feedback loop::>

<a id='0afb6e5c-030f-4fcd-bffd-6f61f61134db'></a>

The model comprises many of the essential elements
responsible for the insulin action since the three major
sub-pathways of the ISP, briefly described in the follow-
ing, are included.

<a id='53c9d621-a586-4b36-8ddc-be52c0684def'></a>

### The PI3K-AKT pathway
For the PI3K-Akt pathway, we mostly refer to the model in Sedaghat et al. [22]. The model has been used by several research groups and includes many of the most known signalling components mediating the translocation of glucose transporter GLUT4. These include the insulin receptor binding and recycle subsystems; the post-receptor signalling subsystem including both Ser- and Tyr- phosphorylation at the insulin receptor substrate1 (IRS1); the formation of a complex (IRS1_PI3K complex) between phosphorylated IRS1 and phosphatidylinositide 3-kinase (PI3K); the phosphatidylinositol 3,4,5-trisphosphates PI(3,4,5)P3, synthesis; the phosphorylation of protein

<a id='69247b49-1df8-4889-896b-03f801bbd328'></a>

kinase B (AKT) and protein kinase C (PKC)-ζ; the translocation of GLUT4 to the plasma membrane. Protein tyrosine phosphatase (PTP1B) and lipid phosphatases (SHIP2 and PTEN) effects are also considered in the model.

<a id='c362628e-fd04-4b60-bb70-c7dda10db205'></a>

_The TSC1/2-mTOR pathway_
For the TSC1/2-mTOR pathway we mostly refer to the
model recently published in Sonntag et al. [24], describ-
ing the mTOR effect in response to insulin and amino
acids. The model considers both mTOR complexes:
mTORC1 and mTORC2. mTORC1 activation is
dependent on the presence of amino acids and is inhib-
ited by the Tuberous sclerosis proteins 1 and 2 (TSC1/2)
activation (i.e. Ser phosphorylation), which, in turn, de-
pends on the 5' AMP-activated protein kinase (AMPK)
activation. AMPK activation depends on IRS1 Tyr phos-
phorylation, whereas TSC1/2 inhibition (i.e. Tyr

<!-- PAGE BREAK -->

<a id='80421148-ddf4-4aa2-b802-146e96633d27'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='371774aa-807a-409d-a3f8-7996694ea07c'></a>

Page 4 of 13

<a id='d16b7076-eb32-4e77-b6f3-702f0708135b'></a>

phosphorylation) depends on AKT phosphorylation at Thr309. mTORC2, which was recently identified as the unknown phosphoinositide-dependent protein kinase 2 (PDK2), i.e. the kinase responsible for Ser474 phosphorylation of AKT [30-32], contributes to the double phosphorylation of AKT together with Thr309 phosphorylation, operated by the phosphoinositide-dependent protein kinase 1 (PDK1). Sonntag et al. [24] formulate the hypothesis of the presence of a PI3K variant, which is directly regulated by the activated insulin receptor and, in turn, activates mTORC2. We included this hypothesis in our model.

<a id='cce01f76-9d3c-487f-9e94-3954c0414fde'></a>

The RAS-MAPK pathway
For the RAS-MAPK pathway, we mostly refer to the model in Borisov et al. [26], describing both EGF and insulin stimulations. The model includes all the main chemical mechanisms involved in the RAS-MAPK pathway: the interaction of Tyr phosphorylated IRS1 with SHP2 (the SH2 domain-containing tyrosine protein kinase 2) and GRB2-SOS complex (the growth factor receptor-bound 2 and the son of sevenless complex), thus forming the SHP2-IRS1 and GRB2/SOS-IRS1 complexes, respectively; the GTP- binding of RAS; the phosphorylation of RAF proto-oncogene serine/threonine-protein kinase (c-RAF); the interaction of insulin receptor with Ras GTPase activating protein (RASGAP), which in turn catalyses the reverse process of Ras deactivation; the activation of the proto-oncogene tyrosine-protein kinase SRC which fully activates c-RAF; the dual specificity mitogen-activated kinase 1/2 (MEK1/2); the extracellular-signal-regulated kinases (ERK1/2).

<a id='f39be93e-9945-4f36-8c8b-80b15dcca22c'></a>

Integration of the PI3K-AKT, the TSC1/2-mTOR and the RAS-MAPK pathways
The PI3K-AKT, TSC1/2-mTOR and RAS-MAPK pathways contain several overlapping parts, which, in the original papers, were often modelled in different ways being based on slightly different assumptions. We compared the overlapping reactions across different models and implemented the most up-to-date version of them based on the current knowledge of cellular biochemistry. Moreover, the integration of the three models required dealing with the different measurement units adopted to describe the state variables. Whereas immunoblot experiments permit to obtain important information concerning the timescale of signalling events, quantitative information about protein expression are often problematic to retrieve so that the predicted concentration profiles are sometimes reported in micromolar concentration, as in Borisov et al. [26], or in arbitrary units (AU), as in Sonntag et al. [24]. In contrast, in Sedaghat et al. [22], concentration were expressed either in molar units or in percentage of total concentration (e.g. GLUT4 cytosol concentration was

<a id='133d8736-7a3a-48e1-a037-bb3e8caf1ef0'></a>

considered to be 96 % of the total GLUT4 concentra-
tion in the cell at baseline condition).

<a id='993f74c8-73fb-46d1-95ff-3e72ba9d1fae'></a>

Potentially, RBM allows performing both deterministic and stochastic simulations, provided that variables quantities are expressed in copies of molecules per cell. Even if in the present work we did not use stochastic simulation, we aligned all the variables to the same unit, i.e. number of molecules per cells, by multiplying the molar units by NA*V (NA indicates Avogadro number and V the cell volume, considered equal to 3e-12 1). All details about unit conversion from AU and percentage concentrations are given in Material and Methods.

<a id='02486746-dcf0-47ac-8bdd-39244e579d46'></a>

The resulting model consists of 42 reaction rules and 101 parameters encoding the interactions among 61 distinct chemical species. Reactions, parameter values and initial conditions are all reported in the Additional file 1.

<a id='b944e664-0882-4753-bb21-78125c3df960'></a>

**Novelties of the RBM-ISP model**
The RBM implementation, facilitated accounting for a number of the ISP features, such as the phosphorylation of signalling proteins at multiple sites and with multiple effects, the simultaneous interaction of molecules with different binding partners and the subcellular localization of some reactions. The above listed characteristics are discussed in details in the following.

<a id='3876cdb4-ba7f-408d-823f-2d33331c95b6'></a>

**Phosphorylation of signalling proteins on multiple sites**
Signalling molecules may have different levels of activity, depending on which residues are phosphorylated. Consider for example IRS1 and AKT. IRS1 has many residues potentially involved in post-translational modifications and can be activated or inhibited in its kinase action, depending on the phosphorylated residue being Tyr or Ser [33,34]. For instance, Tyr-896 phosphorylation is required for PI3K, SHP2 and GRB2 binding, whereas Ser-636 phosphorylation by p70S6K is a mechanism related to insulin resistance [35]. AKT, in contrast, can be activated by phosphorylation at Thr309 or Ser474 by PDK1 and mTORC2, respectively [36].

<a id='5ac5733b-44a0-4c1f-9130-f00eedaea404'></a>

IRS1 phosphorylation dependent activation/inhibition was already included in Sedeghat model although con- sidering Ser phosphorylation regulated by PKC and not by p70S6K, as in Sonntag model. Here we modelled both PKC and p70S6K actions and described pIRS1-Tyr896 complex formation/dissociation with PI3K [22], SHP2 and GRB2 [26].

<a id='e917478b-7e15-420d-9e24-a59eb254793d'></a>

The two phosphorylation sites of AKT were not expli-
citly modelled in Sedaghat et al. [22]. We modelled the
AKT phosphorylation at Thr mediated by PI(3,4,5)P3 as
in Sedaghat et al. model and the AKT phosphorylation
at Ser mediated by mTORC2 as in Sonntag et al. model
and assumed:

<!-- PAGE BREAK -->

<a id='5d7dbd17-b000-40b5-9fea-417651e26760'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='83c20d49-df3b-40ec-b131-992ce493a74f'></a>

Page 5 of 13

<a id='5d1751ca-bc2b-43b6-a03d-c665c2d14be8'></a>

i) AKT phosphorylated either at Thr or both sites to act on TSC1/2 complex by mediating its phosphorylation at Tyr and dephosphorylation at Ser [24];
ii) AKT phosphorylation at Ser or both sites to inactivate C-RAF [26];
iii) AKT phosphorylation at either Thr or Ser to activate GLUT4 translocation [22].

<a id='95230380-f1f4-4193-8198-5ae4d8b0fb96'></a>

***Interaction with multiple binding partners***
The interaction of the molecules in the signalling path-
ways with numerous different binding partners results in
the potential formation of different complexes. In ISP,
IRS1 phosphorylated at Tyr-896 can bind PI3K as mod-
elled in Sedaghat et al. [22] or GRB2/SOS and SHP2, as
modelled in Borisov et al. [26]. In order to match the
RBM-ISP model specification with the current know-
ledge, we allowed the formation of different complexes.
Thus, IRS1 can bind in a mutually exclusive way GRB2/
SOS and SHP2, but can bind simultaneously GRB2/SOS
and the p85 regulatory subunit of PI3K [37,38].

<a id='b6950fe3-03b6-4c30-9b0e-c66fba35fa28'></a>

*Information about subcellular localization in reaction rules*
The possibility that proteins have to interact is often re-
lated to their physical localization, i.e. their presence in
the extra-cellular space, cytoplasm, nucleus, plasma
membrane, etc. For instance, lipids PI(3,4,5)P3 function
as plasma membrane docking sites that recruit different
proteins containing pleckstrin homology (PH) domains

<a id='ecf556a1-a560-4a87-a8d4-64256512bc0b'></a>

(e.g. AKT and PDK1) and their co-localization can accel-
erate specific signalling events [39]. Another example is
the interaction of mTORC1 with the Ras homologue
enriched in brain (RHEB) and Rag family on lysosome
membrane, reported by Zoncu et al. [16]. In our model,
we included the information about subcellular
localization for the insulin receptor and GLUT4 trans-
porter, distinguishing between their plasmatic and cyto-
plasmic localization according to the mathematical
description given by Sedaghat et al. [22].

<a id='b3edad3a-6935-444c-a571-847daec49168'></a>

Model predictions
The concentration profiles of all the chemical species
populating the model were simulated upon 60 min, 100
nM insulin stimulation. The 100 nM concentration rep-
resents a well-accepted level of insulin stimulation in cell
cultures commonly found in the literature [40] and used
also by our group [41]. According to Sonntag et al. [24],
we also assumed a constant amino acids stimulation, ne-
cessary to obtain the mTORC1 activation and the feed-
back of p70S6K on IRS1. To assess the model reliability,
model predictions were compared with experimental
data available in our dataset for some phosphoproteins
at time 2, 5, 10, 30 and 60 min following insulin plus
amino acids, i.e. leucine, stimulation [41]. As shown in
Fig. 2, the experimental and predicted profiles of PAKT-
S473 and pmTORC1-S2448 are in good agreement,
since they both show an increasing phosphorylation pat-
tern reaching a steady state in the first 2-5 min and 20-

<a id='cc90e338-adcb-4338-a78b-8dbc555e6d30'></a>

<::chart: The image displays a multi-panel line chart titled "Fig. 2 Comparison between simulated and experimental data." The chart is arranged in a 2x2 grid, comparing experimental concentration (represented by circular data points) and normalized model predictions (represented by lines) for four different proteins over time. The x-axis for all four subplots is labeled "time (min)" and ranges from 0 to 60 minutes. The y-axis for all subplots represents arbitrary units (AU) and is scaled between 0.0 and 1.0, except for the top-right plot which extends to 1.2. The caption provides further details:

"Fig. 2 Comparison between simulated and experimental data. Comparison between experimental concentration (points) and normalized model predictions (lines) for pAkt-S473, ppERK1/2, pmTOR-S2448 and pP70S6K-T389. The profile of ppERK1/2-Y202,Y204 obtained by increasing the strength of the feedback between ERK and GRB2/SOS is shown in dotted lines. Values are reported for experimental data of human skeletal muscle cells (SkMCs) exposed to EBSS + 100 nM insulin at time 0', 2', 5', 10', 30', and 60'. All measurements were taken in three biological replicated, and for each biological replicates, three technical replicated measurements were taken. All data are expressed in arbitrary units (AU) and rescaled between 0 and 1 for sake of comparison."

**Top-left plot: pAKT-S473**
-   Y-axis: pAKT-S473 (0.0 to 1.0)
-   Shows experimental data points scattered around a model prediction line that rises initially and then flattens.

**Bottom-left plot: pmTOR-S2448**
-   Y-axis: pmTOR-S2448 (0.0 to 1.0)
-   Shows experimental data points with a model prediction line that increases sharply and then plateaus.

**Top-right plot: ppERK1/2-Y202,Y204**
-   Y-axis: ppERK1/2-Y202,Y204 (0.0 to 1.2)
-   Includes a legend:
    -   Solid line: Kcat39=0.0466/(1/60)
    -   Dashed line: Kcat39=0.466/(1/60)
-   The plot shows experimental data points and two model prediction lines. The solid line peaks around 10 minutes and then decreases, while the dashed line peaks earlier and decreases more rapidly, suggesting different feedback strengths.

**Bottom-right plot: pP70S6K-T389**
-   Y-axis: pP70S6K-T389 (0.0 to 1.0)
-   Shows a model prediction line that rises steeply and then plateaus. No experimental data points are visible in this specific subplot.::>

<!-- PAGE BREAK -->

<a id='a57d86ee-792c-4957-941b-c51751f0f823'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='158c099a-2b15-4dee-9d24-f19bbc06a54e'></a>

Page 6 of 13

<a id='688276b0-51d1-43b4-ab5c-e50d925f3e38'></a>

30 min, respectively. The predicted profile for ppERK1/2-Y202,Y204 is confirmed by experimental data in the first 10 min, whereas in the last time points it decreases rapidly in experimental data with respect to model predictions. The profile observed in experimental data for PPERK1/2-Y202,Y204, might be more closely matched by augmenting the strength of the feedback between PPERK1/2-Y202,Y204 and GRB2/SOS. In Fig. 2 (upper right panel, dotted line), the simulated profile of ppERK1/2-Y202,Y204 obtained by multiplying the parameter kcat39 (see Additional file 1) by a factor of 10 is shown. Note that in the RBM ISP model available online, we decided to leave the parameter of the model unchanged, i.e. we use the value from the literature [26], postponing parameter optimization for future studies, when further data will be available. Unfortunately, the experimental data of pP70S6K-T389 were not reliable (only one replicate available), so we cannot compare the experimental and simulated profiles for this protein, which is an endpoint of the pathway with an important feedback action on IRS1. Nevertheless, the simulated profile shown in Fig. 2 (lower, right panel) resembles experimental data shown in other papers [21].

<a id='768f342b-abee-4a4c-921a-7cccae1f4998'></a>

We the examined the predicted profiles of all the active species and clustered them in four clusters according to their dynamic behaviour, as shown in Fig. 3:

<a id='7fa4a5fa-0979-48ad-a52f-963514201ee1'></a>

1. Fast response, reaching the steady state within 2-5 min (blue)
2. Fast overshooting response, reaching the peak within 2-5 min and then the steady state after 10-20 min (green)
3. Slow response, reaching the steady state in 10-20 min (orange)
4. Slow overshooting responses, reaching the peak in 5-10 min and the steady state in 30-60 min (purple).

<a id='caafa2ca-07ba-4c01-b148-4bd31e640285'></a>

Following insulin stimulation, the insulin receptor responds rapidly by phosphorylating and triggering a cascade of events along distinct pathways. Along the PI3K-AKT pathway, all mechanisms tightly related to IRS1 Tyr- phosphorylation are characterized by a fast response. The same is true for other direct targets of IRS1 phosphorylated at Tyr along the TSC1/2-mTOR cascade, i.e. AMPK phosphorylation at T172, SHP2-IRS1 and GRB2/SOS-IRS1 complexes formation. The fast response is characterized by either a rapid rise to the steady state or by a transient overshoot followed by the steady state condition, depending on the absence/presence of feedback mechanisms acting on the target molecule (case 1 and 2, in blue and green, respectively, in Fig. 3). Mechanisms mostly constituting the TSC1/2-

<a id='2e2f4690-85eb-434c-8699-3dca208c69de'></a>

<::chart: A grid of 25 line charts, arranged in 5 rows and 5 columns, displays simulated profiles for various active species. Each chart plots '# molecules/cell' on the y-axis against 'time (min)' on the x-axis, ranging from 0 to 60 min. Each curve is colored (blue, green, orange, or purple) and includes an oval label indicating its cluster (C1, C2, C3, or C4). The legend below the figure describes the four clusters:
1) Fast response reaching the steady state within 2–5 min (blue)
2) Fast overshooting responses reaching a peak within 2–5 min and descending to a steady state after 10–20 min (green)
3) Slow response reaching the steady state in 10–20 min (orange)
4) Slow overshooting responses reaching a peak in 5–10 min and descending to a steady state in 30–60 min (purple)

Detailed breakdown of the charts:

Row 1:
- **IR_phos_memb**: Blue curve, C1. Y-axis: 0 to 150000. Shows a fast response reaching steady state.
- **IRS1_pY**: Green curve, C2. Y-axis: 0 to 200000. Shows a fast overshooting response.
- **IRS1_pS636**: Orange curve, C3. Y-axis: 0 to 150000. Shows a slow response reaching steady state.
- **IRS1_PI3K_complex**: Green curve, C2. Y-axis: 0 to 30000. Shows a fast overshooting response.
- **PI3K_variant_p**: Blue curve, C1. Y-axis: 0 to 4000. Shows a fast response reaching steady state.

Row 2:
- **PI345**: Green curve, C2. Y-axis: 2000 to 10000. Shows a fast overshooting response.
- **Akt_pT**: Green curve, C2. Y-axis: 0 to 14000. Shows a fast overshooting response.
- **PKC_pT410**: Green curve, C2. Y-axis: 0 to 14000. Shows a fast overshooting response.
- **mTORC2_pS2481**: Orange curve, C3. Y-axis: 0e+00 to 3e+05. Shows a slow response reaching steady state.
- **Akt_pS**: Blue curve, C1. Y-axis: 0 to 100000. Shows a fast response reaching steady state.

Row 3:
- **GLUT4_memb**: Orange curve, C3. Y-axis: 2e+06 to 6e+06. Shows a slow response reaching steady state.
- **AMPK_pT172**: Blue curve, C1. Y-axis: 0e+00 to 4e+05. Shows a fast response reaching steady state.
- **TSC1_TSC2_pS1387**: Orange curve, C3. Y-axis: 0 to 3e+05. Shows a slow response reaching steady state.
- **mTORC1_pS2448**: Orange curve, C3. Y-axis: 0 to 10000. Shows a slow response reaching steady state.
- **p70S6K_pT389**: Orange curve, C3. Y-axis: 0 to 20000. Shows a slow response reaching steady state.

Row 4:
- **IR_RasGAP_complex**: Orange curve, C3. Y-axis: 0.0 to 3.0. Shows a slow response reaching steady state.
- **IRS1_SHP2_complex**: Green curve, C2. Y-axis: 0 to 20000. Shows a fast overshooting response.
- **aGS**: Black curve (no cluster oval, but appears to be a decay curve). Y-axis: 300000 to 350000. (Note: This curve is black, not matching the cluster colors, and lacks a cluster oval in the image).
- **IRS1_GS_complex**: Green curve, C2. Y-axis: 0 to 400. Shows a fast overshooting response.
- **aSrc**: Blue curve, C1. Y-axis: 0 to 20. Shows a fast response reaching steady state.

Row 5:
- **RasGTP**: Green curve, C2. Y-axis: 0 to 4000. Shows a fast overshooting response.
- **aRaf**: Purple curve, C4. Y-axis: 0 to 10000. Shows a slow overshooting response.
- **aaRaf**: Purple curve, C4. Y-axis: 0 to 7000. Shows a slow overshooting response.
- **Mek_pS218_S222**: Purple curve, C4. Y-axis: 0 to 15000. Shows a slow overshooting response.
- **Erk_ppY204_Y187**: Purple curve, C4. Y-axis: 0 to 10000. Shows a slow overshooting response.::>

Fig. 3 Clustering of simulated profiles. Four clusters were identified for the predicted profiles of the active species, according to their dynamic behaviour: 1) Fast response reaching the steady state within 2–5 min (blue); 2) Fast overshooting responses reaching a peak within 2–5 min and descending to a steady state after 10–20 min (green); 3) Slow response reaching the steady state in 10–20 min (orange); 4) Slow overshooting responses reaching a peak in 5–10 min and descending to a steady state in 30–60 min (purple)

<!-- PAGE BREAK -->

<a id='1f8db38b-6f9e-4ed0-bf35-7418e549645d'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='c783d7f6-8652-4abe-9601-4c19dfdceab8'></a>

Page 7 of 13

<a id='3c3966b8-8b56-4ec4-b9f1-21f215dd54a3'></a>

mTOR pathway and playing a role in Ser- phosphoryl-ation of IRS1 are characterized by a relatively slow not-overshooting response (case 3, orange in Fig. 3). As observed above, the RAS-MAPK pathway assumes in its upstream components a rapid response, which becomes noticeably slower for the downstream ones (case 4, purple in Fig. 3).

<a id='89fac704-262d-452e-9a68-e1228cb754b0'></a>

In general, molecules downstream the pathway, related to relatively slow processes such as transcription activation or interaction with the environment outside the cell, such as ERK1/2 and GLUT4, are characterized by slow response whereas molecules upstream the pathway are characterized by a fast response so to elicit a rapid signal propagation. In this context, the overshooting response followed by the return to a steady state might help to achieve a rapid signal propagation on one signalling route, making molecules again available for other signalling routes immediately after.

<a id='6cb48f44-1c16-4522-9b54-ab0a2aec6113'></a>

# Model predictions in absence of control mechanisms
A number of simulations were then performed to investigate the robustness of the system on two target effects of ISP: GLUT4 translocation and ERK1/2 phosphorylation. In particular, the role of two major control mechanisms in regulating the target effects was analysed:
* P70S6K-IRS1 negative feedback loop (red line in Fig. 1);
* ERK1/2-GRB2/SOS negative feedback loop (blue line in Fig. 1);

<a id='28a716e9-75b5-4b62-b0e1-3eb6cf856cdb'></a>

To this purpose, the time course of GLUT4 and ERK1/2 response in presence and absence of the two regulatory mechanisms listed above was compared (Fig. 4). The dynamic of doubly phosphorylated ERK1/2 is strongly affected by both P70S6K-IRS1 and ERK1/2-GRB2/SOS negative feedback loops. On the other hand, the steady state and dynamic behaviour of GLUT4 in membrane are not affected by ERK1/2, but are strongly affected by P70S6K-IRS1 negative feedback loop, thus confirming the remarkable importance of this latter control mechanism in determining the system dynamics.

<a id='93ea4c86-4240-4312-92a2-0846cb1b37a4'></a>

It is well known that insulin resistance is associated with defects in IRS-dependent signalling, implicating its dysregulation in the initiation and progression of metabolic disease. An emerging view is that the positive/ negative regulation of IRS by autologous pathways is subverted in disease by increased basal and other temporally inappropriate serine/threonine phosphorylations [37], which lead to a reduced glucose uptake. Compensatory hyperinsulinaemia may rise at this point and lead, ultimately, to diabetes. Although IRS1 (and IRS2) are regulated through a complex mechanism involving phosphorylation of more than 50 different serine/threonine

<a id='e0fd519b-ad54-427c-a128-781a132a67e3'></a>

<::chart: Fig. 4 Simulated ppERK1/2-T202-Y204 (upper panel) and GLUT4 membrane concentration (lower panel) profiles upon 100 nM insulin stimulation, with the complete model (black), the model without p70S6K-IRS1 feedback (red) and the model without the ERK1/2-GS feedback (blue). This latter does not affect GLUT4 membrane concentration; therefore GLUT4 simulated profiles with and without the ERK1/2-GS feedback are superimposable. The figure consists of two line graphs stacked vertically, sharing a common x-axis labeled "Time (min)" ranging from 0 to 60. The y-axis of the top panel is labeled "ppERK1/2-T202-Y204 (# molecules/cell)" with values from 0 to 4e+4. The y-axis of the bottom panel is labeled "GLUT4_memb (# molecules/cell)" with values from 2e+6 to 8e+6. Both graphs display three distinct lines: a black line representing the "Complete model", a red line representing the "Model wo p70S6K-IRS1 feedback", and a blue line representing the "Model wo ERK1/2-GRB2/SOS feedback". In the upper panel (ppERK1/2-T202-Y204), the red line shows a higher peak and slower decay compared to the black and blue lines. The black and blue lines show similar profiles, with the blue line peaking slightly lower than the black line. In the lower panel (GLUT4_memb), the red line shows a higher plateau compared to the black and blue lines. The black and blue lines are almost entirely superimposable, as noted in the caption.::>

<a id='1ca42cad-0fc3-4b19-bfe0-d2febaef8c79'></a>

residues, in our model P70S6K-IRS1 negative feedback loop seems essential for a good control of glucose uptake. Enhancement of P70S6K-IRS1 negative feedback loop is able to explain a reduced insulin sensitivity and glucose uptake (Fig. 5). Similarly (although they also hypothesize a positive feedback from mTOR to a

<::GLUT4 in membrane
(#molecules/cell)

9.4e+6
9.0E+6
8.6e+6
8.2e+6
7.8e+6

1e-10 1e-9 1e-8 1e-7 1e-6
Insulin Input (M)

-GLUT4_memb_wo_FB
-GLUT4_complete
-GLUT4_enhanced_FB
: chart::>

Fig. 5 Simulated GLUT4 membrane concentration at 60 min upon different insulin stimulation, with the complete model (black), the model without p70S6K-IRS1 feedback (red) and the model with enhanced p70S6K-IRS1 feedback, obtained by increasing parameter k15 by 100 % of its vaue (green)

<!-- PAGE BREAK -->

<a id='da75a2ff-acfc-455a-9ece-d1ae32aab13d'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='bcc8bc81-3665-4c6c-a321-872ff879ae10'></a>

Page 8 of 13

<a id='869864e5-e106-4c91-8a70-1ce2a75fffc0'></a>

different IRS1 Serine residue), Brännmark et al. [21],
using a minimal model of insulin signalling, show that a
decreased positive feedback mechanism is able to ex-
plain a reduced glucose uptake.

<a id='7f54d33f-f6bd-40af-a47a-6b97f4314069'></a>

On the other hand, both P70S6K-IRS1 and ERK1/2-GRB2/SOS negative feedback loops seem essential to guarantee that doubly phosphorylated ERK shows a transient behaviour, with a peak at 10 min followed by a return to the baseline condition. This behaviour has already been reported in the literature under insulin stimulus and under epidermal growth factor stimulus [42]. A transient ERK response prevents a sustained acti-vation of ERK that would result in continual cell prolif-eration [42].

<a id='04ff3f16-3cf1-4021-88ec-1365ef423c5c'></a>

## Sensitivity analysis
To further investigate the role of the two major control mechanisms in regulating the target effects, local sensitivity analysis was performed by applying a small perturbation (0.1% of parameter value) to one model parameter at a time and evaluating the resulting relative changes of GLUT4 translocation and ERK1/2 phosphorylation (see Methods). Tables 1 and 2 show the sensitivity coefficients of the model parameters, ranked accordingly to their absolute value and compared to the value the coefficients assume upon removal of P70S6K-

<a id='929b89a2-87c0-449e-9ff0-d03c789e01c0'></a>

IRS1 and ERK1/2-GRB2/SOS negative feedback loops. These coefficients measure the overall effect, i.e. during the observation window, of a parameter change on the outcome, i.e. GLUT4 and ERK response. Positive/negative values mean that increasing the parameter value has the effect of enhancing/reducing the response. Since small absolute values mean that the parameter changes do not significantly affect the outcome, in Tables 1 and 2, only coefficient greater than 0.1 % (absolute value), either in the original or modified model, are reported.

<a id='16043fb9-4d34-417c-81d0-f655baa73e30'></a>

Parametric sensitivity analysis of the complete model for GLUT4 response reveals that the most sensitive parameters are related to GLUT4 translocation to plasma membrane, followed by those related to lipid formation and IRS1_PI3K complex formation/dissociation. The absence of p70S6K_IRS1 feedback has a strong impact on augmenting the sensitivity (absolute value) of parameters related to lipid formation and IRS1_PI3K complex formation/dissociation.

<a id='0b66f3ca-545c-4719-94f5-396142086ad4'></a>

Parameters related to baseline IRS1 phosphorylation/
dephosphorylation at Tyr/Ser, have lower sensitivity,
which diminishes (absolute value), in general, by remov-
ing P70S6K-IRS1 feedback, with the exception of param-
eter k7p, related to IRS1 phosphorylation at Ser.
Parameters related to PKC mediated IRS1 phosphoryl-
ation at Ser also show increased values after removal of

<a id='af7d2a2c-c74b-4800-98a8-67fc324565df'></a>

Table 1 Parametric sensitivity analysis of the complete model for GLUT4 membrane translocation
<table id="7-1">
<tr><td id="7-2">Parameter</td><td id="7-3">Complete model</td><td id="7-4">wo_feedback p70S6K</td><td id="7-5">wo_feedback ERK1/2</td><td id="7-6">Process</td></tr>
<tr><td id="7-7">k_13</td><td id="7-8">-84.89%</td><td id="7-9">-83.59%</td><td id="7-a">-84.89%</td><td id="7-b">GLUT4 translocation</td></tr>
<tr><td id="7-c">k13p</td><td id="7-d">66.02%</td><td id="7-e">66.76%</td><td id="7-f">66.02%</td><td id="7-g">GLUT4 translocation</td></tr>
<tr><td id="7-h">k13</td><td id="7-i">19.03%</td><td id="7-j">17.01%</td><td id="7-k">19.03%</td><td id="7-l">GLUT4 translocation</td></tr>
<tr><td id="7-m">n_p70</td><td id="7-n">-15.21%</td><td id="7-o"></td><td id="7-p">-15.21%</td><td id="7-q">p70 mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="7-r">k9a</td><td id="7-s">8.25%</td><td id="7-t">13.87%</td><td id="7-u">8.25%</td><td id="7-v">lipids PI(3,4,5)P3 formation</td></tr>
<tr><td id="7-w">k9s</td><td id="7-x">-8.25%</td><td id="7-y">-13.86 %</td><td id="7-z">-8.25%</td><td id="7-A">lipids PI(3,4,5)P3 formation</td></tr>
<tr><td id="7-B">k8</td><td id="7-C">7.36%</td><td id="7-D">10.88%</td><td id="7-E">7.36%</td><td id="7-F">IRS1_PI3K complex formation</td></tr>
<tr><td id="7-G">k_8</td><td id="7-H">-7.36%</td><td id="7-I">-10.87%</td><td id="7-J">-7.35%</td><td id="7-K">IRS1_PI3K complex formation</td></tr>
<tr><td id="7-L">k_14</td><td id="7-M">-5.25%</td><td id="7-N">-5.19%</td><td id="7-O">-5.25%</td><td id="7-P">GLUT4 degradation</td></tr>
<tr><td id="7-Q">k_7</td><td id="7-R">-5.05 %</td><td id="7-S">-2.68 %</td><td id="7-T">-5.05 %</td><td id="7-U">IRS1 dephosphorylation at Tyr</td></tr>
<tr><td id="7-V">k7</td><td id="7-W">5.05 %</td><td id="7-X">2.68 %</td><td id="7-Y">5.05 %</td><td id="7-Z">IRS1 phosphorylation at Tyr</td></tr>
<tr><td id="7-10">k_7p</td><td id="7-11">4.45 %</td><td id="7-12">0.53 %</td><td id="7-13">4.45 %</td><td id="7-14">IRS1 dephosphorylation at Ser</td></tr>
<tr><td id="7-15">k15</td><td id="7-16">-4.30 %</td><td id="7-17"></td><td id="7-18">-4.30 %</td><td id="7-19">IRS1 phosphorylation by P70S6K</td></tr>
<tr><td id="7-1a">Kd_p70</td><td id="7-1b">0.72 %</td><td id="7-1c"></td><td id="7-1d">0.72 %</td><td id="7-1e">p70 mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="7-1f">Vmax</td><td id="7-1g">0.65%</td><td id="7-1h">2.18%</td><td id="7-1i">0.65%</td><td id="7-1j">PKC and p70 mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="7-1k">k4p</td><td id="7-1l">-0.51%</td><td id="7-1m">-0.27%</td><td id="7-1n">-0.52%</td><td id="7-1o">Phosphorylated receptor internalization</td></tr>
<tr><td id="7-1p">k_21</td><td id="7-1q">-0.18%</td><td id="7-1r"></td><td id="7-1s">-0.18%</td><td id="7-1t">TSC1-TSC2 T1462_phosphorylation_by_Akt_pT309</td></tr>
<tr><td id="7-1u">k7p</td><td id="7-1v">-0.15%</td><td id="7-1w">-0.54%</td><td id="7-1x">-0.15%</td><td id="7-1y">IRS1 phosphorylation at Ser</td></tr>
<tr><td id="7-1z">k41</td><td id="7-1A">0.14%</td><td id="7-1B">0.46%</td><td id="7-1C">0.14%</td><td id="7-1D">IRS1-GS and IRS1-SHP2 complex disruption</td></tr>
</table>
Sensitivity coefficients are ranked accordingly to their absolute values and their corresponding values upon P70S6K-IRS1 and ERK1/2-GRB2/SOS negative feedback
loop removal are also shown. Only coefficient greater than 0.1 % (absolute value) either in the original or modified model are reported. The column "Process" de-
scribes the biological process to which the parameter takes place

<!-- PAGE BREAK -->

<a id='e19c5afd-0b78-452e-a51f-58b7a814c7fc'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='2840d3bf-0faf-432a-82d5-1b00152d7a57'></a>

Page 9 of 13

<a id='bc75eaf5-d71c-4980-8dc2-99efa8b8a791'></a>

Table 2 Parametric sensitivity analysis of the complete model for ERK1/2 activation
<table id="8-1">
<tr><td id="8-2">Parameter</td><td id="8-3">Complete model</td><td id="8-4">wo_feedback P7056K</td><td id="8-5">wo_feedback ERK1/ 2</td><td id="8-6">Process</td></tr>
<tr><td id="8-7">n_p70</td><td id="8-8">-433.62 %</td><td id="8-9"></td><td id="8-a">-553.98%</td><td id="8-b">p70 mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="8-c">kcat33</td><td id="8-d">158.53 %</td><td id="8-e">159.60 %</td><td id="8-f">207.34 %</td><td id="8-g"># Mek phosphorylation</td></tr>
<tr><td id="8-h">kcat32</td><td id="8-i">-157.47 %</td><td id="8-j">-158.57 %</td><td id="8-k">-202.56 %</td><td id="8-l"># Raf inactivation</td></tr>
<tr><td id="8-m">k7</td><td id="8-n">154.53 %</td><td id="8-o">23.76 %</td><td id="8-p">183.15 %</td><td id="8-q"># IRS-1 phosphorylation at Tyr</td></tr>
<tr><td id="8-r">k_7</td><td id="8-s">-154.50%</td><td id="8-t">-23.96%</td><td id="8-u">-183.05%</td><td id="8-v"># IRS-1 dephosphorylation at Tyr</td></tr>
<tr><td id="8-w">kcat28</td><td id="8-x">152.95%</td><td id="8-y">65.18%</td><td id="8-z">189.32%</td><td id="8-A">Ras activation</td></tr>
<tr><td id="8-B">kcat29</td><td id="8-C">-152.78%</td><td id="8-D">-65.23%</td><td id="8-E">-188.99%</td><td id="8-F"># Raf activation</td></tr>
<tr><td id="8-G">kcat30</td><td id="8-H">150.90%</td><td id="8-I">62.38%</td><td id="8-J">185.97 %</td><td id="8-K"># Raf activation</td></tr>
<tr><td id="8-L">k_7p</td><td id="8-M">140.15%</td><td id="8-N">4.82%</td><td id="8-O">161.27%</td><td id="8-P"># IRS-1 dephosphorylation at Ser</td></tr>
<tr><td id="8-Q">k15</td><td id="8-R">-135.17 %</td><td id="8-S"></td><td id="8-T">-155.79 %</td><td id="8-U"># IRS1 phosphorylation by P7056K</td></tr>
<tr><td id="8-V">kcat35</td><td id="8-W">79.97 %</td><td id="8-X">79.91 %</td><td id="8-Y">104.72 %</td><td id="8-Z">Erk phosphorylation</td></tr>
<tr><td id="8-10">kcat36</td><td id="8-11">77.83 %</td><td id="8-12">79.00 %</td><td id="8-13">101.60 %</td><td id="8-14">Erk phosphorylation</td></tr>
<tr><td id="8-15">k41</td><td id="8-16">-34.20 %</td><td id="8-17">-16.98 %</td><td id="8-18">-43.11 %</td><td id="8-19"># IRS1-GS and IRS1-SHP2 complex disruption</td></tr>
<tr><td id="8-1a">kcat39</td><td id="8-1b">-23.10 %</td><td id="8-1c">-25.16 %</td><td id="8-1d"></td><td id="8-1e">GS inhibition</td></tr>
<tr><td id="8-1f">Kd_p70</td><td id="8-1g">20.02%</td><td id="8-1h"></td><td id="8-1i">26.18%</td><td id="8-1j">p70 mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="8-1k">Vmax</td><td id="8-1l">15.35%</td><td id="8-1m">19.63%</td><td id="8-1n">21.95%</td><td id="8-1o">PKC and p70 mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="8-1p">k8</td><td id="8-1q">-13.39 %</td><td id="8-1r">-9.24%</td><td id="8-1s">-17.15%</td><td id="8-1t"># IRS-1_PI3-K complex formation (PI3-K activation)</td></tr>
<tr><td id="8-1u">k_8</td><td id="8-1v">13.38%</td><td id="8-1w">9.27%</td><td id="8-1x">17.04%</td><td id="8-1y"># IRS-1_PI3-K complex dissociation</td></tr>
<tr><td id="8-1z">n</td><td id="8-1A">6.66%</td><td id="8-1B">0.11%</td><td id="8-1C">7.10%</td><td id="8-1D">PKC mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="8-1E">k_21</td><td id="8-1F">-5.65%</td><td id="8-1G"></td><td id="8-1H">-6.50 %</td><td id="8-1I">#TSC1-TSC2 T1462_phosphorylation_by_Akt_pT309</td></tr>
<tr><td id="8-1J">k9s</td><td id="8-1K">4.74%</td><td id="8-1L">0.35%</td><td id="8-1M">5.35 %</td><td id="8-1N">#lipids PI(3,4,5)P3 formation</td></tr>
<tr><td id="8-1O">k9a</td><td id="8-1P">-4.71%</td><td id="8-1Q">-0.28%</td><td id="8-1R">-5.48%</td><td id="8-1S"># lipids Pl(3,4,5)P3 formation</td></tr>
<tr><td id="8-1T">k7p</td><td id="8-1U">-4.01%</td><td id="8-1V">-4.79%</td><td id="8-1W">-5.32 %</td><td id="8-1X"># IRS-1 phosphorylation at Ser</td></tr>
<tr><td id="8-1Y">k4p</td><td id="8-1Z">-2.62%</td><td id="8-20">-10.56%</td><td id="8-21">-4.01%</td><td id="8-22"># Phosphorylated receptor internalization</td></tr>
<tr><td id="8-23">k_39</td><td id="8-24">2.62 %</td><td id="8-25">2.10 %</td><td id="8-26"></td><td id="8-27">GS inactivation</td></tr>
<tr><td id="8-28">k_20</td><td id="8-29">2.20 %</td><td id="8-2a"></td><td id="8-2b">-0.21 %</td><td id="8-2c"># p70S6K phosphorylation/dephosphorylation mediated by mTORC1_pS2448</td></tr>
<tr><td id="8-2d">kcat24</td><td id="8-2e">-1.71 %</td><td id="8-2f">87.60 %</td><td id="8-2g">17.49 %</td><td id="8-2h">Src activation</td></tr>
<tr><td id="8-2i">kcat31</td><td id="8-2j">-1.70 %</td><td id="8-2k">87.58 %</td><td id="8-2l">17.35 %</td><td id="8-2m"># Raf activation</td></tr>
<tr><td id="8-2n">alpha24</td><td id="8-2o">-1.60 %</td><td id="8-2p">87.59 %</td><td id="8-2q">17.48 %</td><td id="8-2r">Src activation</td></tr>
<tr><td id="8-2s">k_4</td><td id="8-2t">0.77%</td><td id="8-2u">2.59%</td><td id="8-2v">0.88%</td><td id="8-2w"># Free receptor externalization</td></tr>
<tr><td id="8-2x">k_16</td><td id="8-2y">0.13%</td><td id="8-2z">-0.07%</td><td id="8-2A">-0.11%</td><td id="8-2B"># AMPK_T172 dephosphorylation mediated by IRS1_pY</td></tr>
<tr><td id="8-2C">Kd_pkc</td><td id="8-2D">0.11%</td><td id="8-2E">-0.02%</td><td id="8-2F">0.00%</td><td id="8-2G">PKC mediated IRS1 phosphorylation at Ser</td></tr>
<tr><td id="8-2H">k12</td><td id="8-2I">0.10%</td><td id="8-2J">0.04%</td><td id="8-2K">-0.03%</td><td id="8-2L"># PKC phosphorylation at Threonine</td></tr>
<tr><td id="8-2M">k6</td><td id="8-2N">0.08%</td><td id="8-2O">0.12%</td><td id="8-2P">-0.01%</td><td id="8-2Q"># Receptor unbinding and dephosphorylation (inside the cell)</td></tr>
<tr><td id="8-2R">k_2</td><td id="8-2S">0.05%</td><td id="8-2T">-0.11%</td><td id="8-2U">-0.17%</td><td id="8-2V"># Receptor binding 2nd insulin molecule</td></tr>
</table>
Sensitivity coefficients are ranked accordingly to their absolute values and their corresponding values upon P70S6K-IRS1 and ERK1/2-GRB2/SOS negative feedback loop removal are also shown. Only coefficient greater than 0.1 % (absolute value) either in the original or modified models are reported. The column “Process” describes the biological process to which the parameter takes place

<a id='8060b974-1523-49d2-8ea8-ce769316bc31'></a>

P70S6K-IRS1 feedback. Since ERK1/2-GRB2/SOS feedback removal has no effect on GLUT4 translocation, the sensitivity coefficients do not change with and without this feedback.

<a id='e01f69b8-c260-43d5-bb27-5ae37f7dad58'></a>

Parametric sensitivity analysis of the complete model for ERK1/2 response shows that the most sensitive

<a id='78784fc3-8d75-4240-84e8-75669b6d3ba9'></a>

parameters are related to RAS, MEK and RAF activation
and to IRS1 phosphorylation at Tyr and Ser, this latter
mediated by p70S6K.Along both the PI3K-AKT and the
RAS-ERK1/2 pathway, ERK1/2-GRB2/SOS feedback
seems to have an important role on the system robust-
ness. The system dynamics are weakly affected by its

<!-- PAGE BREAK -->

<a id='7b63361f-ac44-490a-966c-5b80fd4af565'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='d2700089-4fac-4d5b-bfc7-21fe15c48046'></a>

Page 10 of 13

<a id='81b0e845-c131-4f8c-ba53-1679205f1b12'></a>

absence (see Fig. 4), whereas the parameter sensitivity increases (in absolute value) in almost all cases if this feedback is removed.

<a id='c99bc926-c8e1-45d9-893d-6b7cd39fd209'></a>

Conclusions about the effect of P70S6K-IRS1 feedback
on ERK1/2 response are more controversial. Removing
this feedback has the effect of reducing parameter sensi-
tivity along PI3K_AKT pathway, whereas, along RAS-
ERK1/2 pathway, it has almost no effect for parameters
related to MEK phosphorylation, RAF inactivation and
ERK phosphorylation. It diminishes the sensitivity for
parameters related to RAS, RAF activation and to IRS1-
GRB2/SOS and IRS1-SHP2 complex disruption. It
strongly augments the sensitivity of parameters related
to SRC and RAF activation.

<a id='724a9edc-69f1-4719-89dc-6ec3a16c420d'></a>

These results highlight the central role of negative
feedback loops in determining not only the dynamics
of a biological system but also its robustness. This
property is of remarkable importance because it pre-
serves the dynamic behaviour of the system against
noise and small biological fluctuations commonly due
to intercellular variability.

<a id='fd6974ef-b515-4de3-8b59-64e173287172'></a>

## Conclusions
We implemented a computational model of the ISP, including its most important regulatory mechanisms known at present. The model provides a comprehensive description of the system, since it integrates three previously published models [22,24,26] addressing distinct aspects of insulin signalling, such as the PI3K-AKT pathway, the TSC1/2-mTOR pathway, and the RAS-ERK1/2 pathway.

<a id='cd4245ea-38bf-4654-9463-92b4fa18d7ee'></a>

The model was implemented using the RBM approach, especially suitable for the specification of complex bio-chemical systems models, such as signalling networks. In particular, we made use of the BioNetGen software to provide a clear and compact representation of the chem-ical species and the reactions populating the system. RBM is based on the key assumption that molecular in-teractions are "modular", meaning that the network dy-namics is mostly determined by the local properties of the proteins involved in the interactions, and thus the same rate law can be assigned to a defined "class" of re-actions. Hence, differently from the traditional approach in which a system is directly described by a number of ODEs equal to the number of possible interactions and transformations of chemical species, in the RBM ap-proach the same system can be described using a re-duced number of "rules". In the case of the ISP model here presented, the dynamic of 61 distinct chemical spe-cies was encoded by only 42 rules.

<a id='54e655c9-6615-4678-a525-8b0be4323cdf'></a>

The RBM-ISP model was partially validated using ex-
perimental data of some of the phosphorylated proteins
involved in ISP such as pAKT-S473, ppERK1/2-T202-
Y204, and pmTOR-S2448, measured at 0, 2, 5, 30 and

<a id='d26e6f36-6abe-4eb3-ba11-6e3c4c4f4cef'></a>

60 min after insulin stimulation. Despite some minor
discrepancy at 60 min for ppERK1/2-T202-Y204, the ex-
perimental and predicted profiles are in good agreement.

<a id='fa0f3a54-3d51-4839-824d-5fa623827b3b'></a>

As already noted in [41], since a wide range of signals, including nutrients, energy levels, growth factors, and amino acids are known to affect insulin signalling pathway, it is likely that experimental results strongly depend on the availability of combinations of the above variables. Moreover, the proteins involved in the insulin signalling pathway are known to exhibit a number of different phosphorylation sites, able to interact in different ways with different molecules, a complex set of regulatory mechanisms, which are not yet completely understood. In this respect, our model represents the state of the art knowledge of ISP and can be used together with experimental data as a useful simulation tool for the generation of new hypotheses. Moreover, since the RBM approach allows, thanks to its modularity, the easy integration of different pathways and the inclusion of new finer details as soon as they become available, our model might constitute a starting point model, ready for the inclusion of new regulatory mechanisms such as those regarding the regulation of IRS1 through its numerous phosphorylation sites [19,37]. Another example of regulatory mechanisms that might be integrated within our model in future studies, is given by Yugi et al. [43], in which the authors have reconstructed the insulin signal flow from phosphoproteome and metabolome data and developed a kinetic model of the glycolytic pathway.

<a id='8dc64ab0-5ff3-41a8-bfba-cc672b3d9da6'></a>

Besides presenting the RBM-ISP model, in this work we showed one of its possible applications in the analysis of network robustness. Robustness is a fundamental property that permits to biological systems to preserve their specific functionality despite external and internal perturbations due, respectively, to unpredictable environmental changes and fluctuation of protein concentrations Kitano [44]. Biological robustness is largely related to the network topology and, in particular, to the presence of control mechanisms, such as positive and negative feedback loops [45, 46]. In this work, we investigated the role of two negative feedback loops involving P70S6K-IRS1 and ERK1/2-GRB2/SOS in controlling GLUT4 translocation and ERK1/2 phosphorylation, respectively. The removal of the P70S6K-IRS1 feedback showed relevant differences in the concentration profiles of both GLUT4 translocation to the cell membrane and ERK1/2 phosphorylation. Removal of the ERK1/2-GRB2/SOS feedback resulted in minor differences in ERK1/2 phosphorylation. However, the comparison between the original model and the model without the ERK1/2-GRB2/SOS feedback revealed that GLUT4 translocation and ERK1/2 phosphorylation are more sensitive to changes in the model parameters in the latter case. The reported results

<!-- PAGE BREAK -->

<a id='06e52efb-1381-4d8a-8353-bae4239f1da7'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='be902d61-023b-4ede-bc4d-b73256c914f4'></a>

Page 11 of 13

<a id='d66cc480-ac74-408d-80f6-b2185f94a705'></a>

highlight how control mechanisms such as negative feed-
back loops may act in a concealed way, determining some
of the fundamental network properties that might not be
observed by simple inspection of the system dynamic be-
haviour, and stress on the need of more and more realistic
models and computational tools, able to deal with large-
scale simulations and interaction of smaller subnetwork
models.

<a id='9aaadfbf-f87f-4bbd-b5a2-bd1cc07f4112'></a>

## Methods

### Initial concentration and unit conversion
We aligned all variables to the same unit, i.e. number of molecules per cells, by multiplying the molar units by NA*V (NA indicates Avogadro number and V the cell volume, considered equal to 3e-12 1).

<a id='b6bb4aed-6ef9-4720-a565-3013684e5698'></a>

To convert the AU concentration used in Sonntag model into number of molecules per cells we considered IRS1, which is present in both Sonntag and Borisov model as reference concentration, and scaled other quantities accordingly. So, for example, initial concentration of mTORC2, which was set to 18.8 AU in Sonntag et al., was multiplied by the initial concentration of IRS1 expressed in number of molecules per cells (as derived from [26]) and divided by IRS1 initial concentration expressed in AU.

<a id='0563d4c1-ae6c-4cbd-ac40-032027f22b48'></a>

As recently pointed out by Nyman et al. [47] the initial concentrations attributed to insulin receptor IR both at plasma membrane and in cytoplasm and to IRS1 and PIK3 molecules in the Sedaghat model, when multiplied by NA*V resulted in less than one molecule per cell. The initial concentrations of these four molecules were thus taken from the Sonntag model.

<a id='cf444ccc-f5e3-4968-afcb-b0f8121a6aed'></a>

Finally, in absence of further information from the literature, concentrations expressed in percentage of the total concentration in Sedaghat model (namely, GLUT4, PKC, PI(3,4,5)P3, PI(3,4)P2 and PI(4,5)P2), were converted into number of molecules per cell by considering a total number of molecules equal to IRS1 for GLUT4 (in membrane plus cytoplasm) and total lipids (i.e. PI(3,4,5)P3 plus PI(3,4)P2 plus PI(4,5)P2) and a total number of molecules equal to AKT for PKC.

<a id='b5dd8592-56a4-4d0e-9b34-fa93beb7bee0'></a>

Initial concentrations are reported in Additional file 1: Table S1.

<a id='9616b978-b37d-42e8-8c8f-793aef8d3c1f'></a>

## Parameter values
Reaction rules and parameters (reported in Additional file 1) were taken from the original models and opportunely rescaled, when necessary, for sake of models integration accordingly to the changes made for the unit of measurements so to express parameters for first order reaction in 1/min and parameters for second order reactions in 1/(molecules*min).

<a id='5b92fe20-43fa-416f-94e0-5f2e1fb1d961'></a>

The feedback of activated PKC and p70S6K on IRS1
and the modulatory effect of AKT on PTP, SHIP2 and
PTEN, were modelled using Hill kinetics rather than lin-
ear kinetics for consistency among different models. De-
tailed functions and parameters are given in the
Additional file 1.

<a id='faf62f3a-a386-4dfe-b6a7-4f05921f3322'></a>

### Experimental design
Muscle cell lines were stimulated with 100 nM insulin at time 0 for the following durations: 0', 2', 5', 10', 30', and 60'. AKT, pAKT-S473, ERK1/2, ppERK1/2-T202-Y204, mTOR, pmTOR-S2448, P70S6K, and pP70S6K-T389 were measured using Western blot in technical triplicates. The experiment was repeated three times, thus three biological replicates are available for each condition.

<a id='3ab2b745-595a-4380-b7bd-14d4ab2dd499'></a>

Cell cultures
Human skeletal muscle cells (SkMCs) and growth medium (SkGM) were purchased from Lonza. SkMCs are isolated from normal donors from gestational tissue usually from the quadriceps or psoas tissue and are sold in second passage. Cells were proliferated on 6-well plates between 5 and 7 passages at 37 °C, 5% CO2, grown to 90% confluence and exposed to differentiation medium (DMEM:F12 w/2 % Horse Serum and gentamy- cin) for ten days. Glucose was not added to the medium, but was present in the DMEM at 1000 mg/L. Cells were serum-starved with DMEM O/N and then switched to Earle's Balanced Salt Solution (EBSS) for one hour, after which they were exposed to EBSS + 100 nM insulin. The 100 nM concentration represents a well-accepted level of insulin stimulation in cell cultures commonly found in the literature [40].

<a id='a3c1ae6c-8a6d-4960-8844-a957c2130312'></a>

Immunoblotting
Cells were lysed with Cell Signalling lysis buffer, soni-cated, and centrifuged at 14KG for 30 min at 4 °C. Cell Signalling Lysis buffer was composed by 20 mM Tris-HCl (pH 7.5), 150 mM NaCl, 1 mM Na2EDTA, 1 mM EGTA, 1 % Triton, 2.5 mM sodium pyrophosphate, 1 mM bglycerophosphate, 1 mM Na3VO4, 1 µg/ml leu-peptin, We also added Halt Protease and Phosphatase inhibitor cocktail. The Pierce 660 reagent was used to determine protein concentrations and lysates were loaded onto Invitrogen Nupage gels for Western blot transfer using the Biorad semi-dry Trans-blot apparatus. Blots were blocked with Licor blocking buffer and incu-bated overnight at 4 °C with target antibodies. Cell Sig-nalling supplied all primary antibodies. In details, the antibodies used were: Akt total - Cell Signalling #2920; Akt Phospho (Ser473) – Cell Signalling #9336; ERK1/2 total – Cell Signalling #4695; ppERK1/2 (T202-Y204) – Cell Signalling #9106; Cell Signalling #9461; mTOR

<!-- PAGE BREAK -->

<a id='572e9a3a-9e8d-48cb-8ed3-e9d88adc2915'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='794b1e65-ba55-47b7-8698-0a0481599a43'></a>

Page 12 of 13

<a id='fea5be01-8e57-4043-b883-9b3bcc251dc2'></a>

Cell Signalling #2983; pmTOR (S2448) – Cell Signalling
#2971; P70S6K – Cell Signalling #9202; pP70S6K (T389)
– Cell Signalling #9206. All were used at a 1:1000
concentration.

<a id='680084b4-3cec-4973-8955-eec09cedb02a'></a>

Band densities were quantified using the Licor Odys-sey system using the integrated intensity value for each band. To correct for the antibody efficiency, all band densities for each protein were expressed relative to the baseline time 0'. Moreover, to allow for comparison among different membranes, the ratios between phos-phorylated and total proteins were calculated; total pro-tein concentration is constant across time points as shown in [41]. Since for each protein, the total and the phosphorylated fractions were loaded in the same lane, this latter step also corrected for possible differences in the quantity of sample loaded in each gel. Finally, tech-nical replicates were averaged.

<a id='e9a0e4fc-5065-4cb4-bbc8-1d1b1857bdbc'></a>

**Computational modelling**
The model of the insulin signalling pathway was implemented using BioNetGen [9], a software for the rule-based modelling.

<a id='b0d38de4-1e16-4455-b6b5-f901e763f54b'></a>

To simulate the network dynamics, we first generated the network of all possible reactions that may occur in the system starting from the listed reaction rules and iteratively applied them to the set of seed species, and then performed a deterministic simulation through numerical solving of a system of ODEs.

<a id='2c50d1ba-43d5-48b4-adf5-4ce39264a7b4'></a>

**Parametric sensitivity analysis**
For a generic prediction depending on λ₁, λ₂ ... λn model
parameters (and initial concentrations) and on time t:

<a id='d853ad6e-b8fc-4278-bb7d-de514c4dc584'></a>

y(t) = f(λ1, λ2, ...λn, t)

<a id='fd73455e-97f2-4b16-ba87-43305bca1371'></a>

the sensitivity of y at time t with respect to λᵢ is defined as:

<a id='e07a33c4-5e9c-46b7-b549-75260ed8a33a'></a>

<::s_i(t) = \frac{\partial f(\lambda_1, ..., \lambda_i, ..., \lambda_n, t)}{\partial \lambda_i} \frac{\lambda_i}{y(t)}
: figure::>

<a id='f9325793-c4b7-42bb-8fd0-3acedd4b6180'></a>

and for each model parameters, the overall sensitivity can be derived as:

<a id='77543c32-0e63-4fc9-9ba1-b5215ccff228'></a>

Sᵢ = ∫ᵗₜ₀ sᵢ(τ)dτ

<a id='ee67e24e-3309-4508-a18a-c522056b87b2'></a>

and averaged across the observed time window [48, 49].
In order to implement the parametric sensitivity ana-
lysis, we exported our model in sbml language and ran
the sensitivity analysis using COPASI [50].

<a id='8835206a-7f0f-487d-a099-f1b2e77d0ac4'></a>

## Additional files

**Additional file 1:** Model_details. Tables listing: (1) model inputs; (2) constant parameters; (3) the initial concentration of different chemical species; (4) the rules and functions used in the model, in BioNetGen syntax; (5) the model parameters. (DOCX 32 kb)

**Additional file 2:** Protein_data. Experimental data of pAKT-S473, pmTORC1-S2448 and ppERK1/2-Y202,Y204 at time 2, 5, 10, 30 and 60 min following insulin plus amino acids, i.e. leucine, stimulation [41]. Data are available in three bioplogical replicates (A, B and C in the file). To correct for the antibody efficiency, all band densities for each protein are expressed relative to the baseline time 0'. Moreover, to allow for comparison among different membranes, the ratios between phosphorylated and total proteins are calculated. (XLSX 9 kb)

<a id='e4768360-15b6-49d2-8659-3f3d5d357caf'></a>

Abbreviations
AKT: protein kinase B; AMPK: AMP-activated protein kinase; AU: arbitrary units;
c-RAF: proto-oncogene serine/threonine-protein kinase; EGF: epidermal growth
factor; ERK1/2: extracellular signal-regulated kinase 1/2; GLUT4: glucose transporter
type 4; GRB2: growth factor receptor-bound 2; IR: insulin receptor; IRS1: insulin
receptor substrate 1; ISP: Insulin signalling pathway; MAPK: mitogen-activated
protein kinase; MEK1/2: mitogen-activated kinase 1/2; mTOR: mammalian target of
rapamycin; P70S6K: Ribosomal protein S6 kinase beta-1; PDK1: phosphoinositide-
dependent protein kinase 1; PDK2: phosphoinositide-dependent protein kinase 2;
PI(3,4)P2: phosphatidylinositol (3,4)-bisphosphate; PI(3,4,5)P3: phosphatidylinositol
(3,4,5)-trisphosphate; PI(4,5)P2: phosphatidylinositol (4,5)-bisphosphate;
PI3K: phosphatidylinositide 3-kinase; PKC: protein kinase C; PTEN: phosphatase and
tensin homolog; PTP: protein tyrosine phosphatase; RBM: rule-based modeling;
SHIP: phosphatidylinositol-3,4,5-trisphosphate 5-phosphatase 1; SHP2: SH2
domain-containing tyrosine protein kinase 2; SOS: son of sevenless complex;
TSC1/2: tuberous sclerosis proteins 1 and 2.

<a id='e32864f9-d561-4228-a5f3-ce14355543b4'></a>

Funding
This work was supported by CARIPARO 2008-2010 "Systems Biology approaches to infer gene regulation from gene and protein time series data".

<a id='cb6224e5-58c5-4a73-8540-6d3886925c3d'></a>

**Availability of data and materials**
All the material used in this work can be found in the following locations:

* The model is available at http://sysbiobig.dei.unipd.it/ was submitted to Biomodels database (https://www.ebi.ac.uk/biomodels-main/ # MODEL 1604100005).
* Protein data used to validate the model are available as Additional file 2.

<a id='93dbe39c-7ca9-4339-b54c-6796a2409aec'></a>

**Authors' contributions**
BDC designed the study, implemented the final model, analysed the data, and wrote the manuscript. AC implemented the draft model and wrote the draft manuscript. FE contributed to study conception and to edit the manuscript. GT participated in the study design and coordination and helped to draft the manuscript. All authors contributed to read and approved of the manuscript.

<a id='f88ca6c9-9bbb-4670-bd15-dcc737fbb116'></a>

**Competing interests**
The authors declare that they have no conflict of interest.

<a id='ef816f21-6c68-4635-bc89-c07804d3e366'></a>

Consent for publication
Not applicable.

<a id='c06f6617-273f-46e1-a829-010fa3290169'></a>

Ethics approval and consent to participate
Not applicable.

<a id='154b56ac-6330-4673-bb5a-2172874fcf21'></a>

**Author details**

¹Department of Information Engineering, University of Padova, Via Gradenigo 6A, Padova 35131, Italy. ²Magnetic Resonance Center (CERM) and Department of Chemistry "Ugo Schiff", University of Florence, Florence, Italy.
³European Molecular Biology Laboratory, European Bioinformatics Institute (EMBL-EBI), Wellcome Trust Genome Campus, Cambridge, UK.

<!-- PAGE BREAK -->

<a id='57a3bbdf-2d10-427e-b618-47b3e42c1f20'></a>

Di Camillo et al. BMC Systems Biology (2016) 10:38

<a id='52633f37-8d43-4d6a-8da6-d33efcac6902'></a>

Page 13 of 13

<a id='9a7f480e-425e-4aa0-bcca-12200607b2c5'></a>

Received: 23 June 2015 Accepted: 12 May 2016
Published online: 01 June 2016

<a id='6cc22011-9faf-47da-8d6b-cd8408030845'></a>

References
1. Sawyers C. Targeted cancer therapy. Nature. 2004;432:294-7.
2. Villaamil V, Gallego G, Cainzos I, Valladares-Ayerbes M, Antón AL. State of the art in silico tools for the study of signalling pathways in cancer. Int J Mol Sci. 2013;13:6561-81.
3. Kitano H. Computational systems biology. Nature. 2002;420(6912):206-10.
4. Papin J, Hunter T, Palsson B, Subramaniam S. Reconstruction of cellular signalling networks and analysis of their properties. Nat Rev Mol Cell Biol. 2005;6:99-111.
5. Aldridge BB, Burk J, Lauffenburger D, Sorger P. Physicochemical modelling of cell signalling pathways. Nat Cell Biol. 2006;8:1195-203.
6. Morris MK, Saez-Rodriguez J, Sorger PK, Lauffenburger DA. Logic-based models for the analysis of cell signaling networks. Biochemistry. 2010;49(15):3216-24.
7. Hlavacek W, Faeder J, Blinov M, Perelson A, Goldstein B. The complexity of complexes in signal transduction. Biotechnol Bioeng. 2003;84:783-94.
8. Danos V, Feret J, Fontana W, Harmer R, Krivine J. Rule-based modelling of cellular signalling. In CONCUR 2007- concurrency theory. Lect Notes Comput Sci. 2007;4703:17-41. Berlin, Heidelberg: Springer Berlin Heidelberg.
9. Faeder J, Blinov M, Hlavacek W. Rule-based modelling of biochemical systems with BioNetGen. Methods Mol Biol. 2009;500:113-67.
10. Smith A, Xu W, Sun Y, Faeder J, Marai G. RuleBender: integrated modelling, simulation and visualization for rule-based intracellular biochemistry. BMC Bioinformatics. 2012;13 Suppl 8:53.
11. Blinov M, Faeder J, Goldstein B, Hlavacek W. A network model of early events in epidermal growth factor receptor signalling that accounts for combinatorial complexity. Biosystems. 2006;83:136-51.
12. Creamer MS, Stites EC, Aziz M, Cahill JA, Tan CW, Berens ME, Han H, Bussey KJ, Von Hoff DD, Hlavacek WS, Posner RG. Specification, annotation, visualization and simulation of a large rule-based model for ERBB receptor signalling. BMC Syst Biol. 2012;6:107.
13. Stefan MI, Bartol TM, Sejnowski TJ, Kennedy MB. Multi-state modeling of biomolecules. PLoS Comput Biol. 2014;25:10(9).
14. Danos V, Feret J, Fontana W, Krivine J. Scalable simulation of cellular signalling networks. Lect Notes Comput Sci. 2007;4807:139-57.
15. Rowland A, Fazakerley D, James D. Mapping insulin/GLUT4 circuitry. Traffic. 2011;12:672-81.
16. Zoncu R, Efeyan A, Sabatini D. mTOR: from growth signal integration to cancer, diabetes and ageing. Nat Rev Mol Cell Biol. 2001;12:21-35.
17. Chen R, Sarnecki C, Blenis J. Nuclear localization and regulation of erk- and rsk-encoded protein kinases. Mol Cell Biol. 1992;12:915-27.
18. Kiselyov W, Gauguin L, De Meyts P. Harmonic oscillator model of the insulin and IGF1 receptors' allosteric binding and activation. Mol Syst Biol. 2009;5:243.
19. Brännmark C, Palmér R, Glad S, Cedersund G, Strålfors P. Mass and information feedbacks through receptor endocytosis govern insulin signalling as revealed using a parameter-free modelling framework. J Biol Chem. 2010;285:20171-9.
20. Cedersund G, Roll J, Ulfhielm E, Danielsson A, Tidefelt H, Strålfors P. Model-based hypothesis testing of key mechanisms in initial phase of insulin signalling. PLoS Comput Biol. 2008;4:e1000096.
21. Brännmark C, Nyman E, Fagerholm S, Bergenholm L, Ekstrand EM, Cedersund G, Strålfors P. Insulin signalling in type 2 diabetes: experimental and modelling analyses reveal mechanisms of insulin resistance in human adipocytes. J Biol Chem. 2013;288(14):9867-80.
22. Sedaghat A, Sherman A, Quon M. A mathematical model of metabolic insulin signalling pathways. Am J Physiol Endocrinol Metab. 2002;283:E1084-101.
23. Dalle Pezze P, Sonntag AG, Thien A, Prentzell MT, Gödel M, Fischer S, Neumann-Haefelin E, Huber TB, Baumeister R, Shanley DP, Thedieck K. A dynamic network model of mTOR signalling reveals TSC-independent mTORC2 regulation. Sci Sgnal. 2012;5:ra25.
24. Sonntag A, Dalle Pezze P, Shanley D, Thedieck K. A modelling-experimental approach reveals insulin receptor substrate (IRS)-dependent regulation of adenosine monosphosphate-dependent kinase (AMPK) by insulin. FEBS J. 2012;279:3314-28.

<a id='b4db2235-c83d-40e9-bba5-ad47d4a6e4b7'></a>

25. Vinod P, Venkatesh K. Quantification of the effect of amino acids on an integrated mTOR and insulin signalling pathway. Mol Biosyst. 2009;5: 1163–73.
26. Borisov N, Aksamitiene E, Kiyatkin A, Legewie S, Berkhout J, Maiwald T, et al. Systems-level interactions between insulin-EGF networks amplify mitogenic signalling. Mol Syst Biol. 2009;5:256.
27. Kwei E, Sanft KR, Petzold LR, Doyle FJ. Systems analysis of the insulin signalling pathway. IFAC Proceedings Volumes (IFAC-PapersOnline). 2008;17: PART 1.
28. Luni C, Sanft KR, Petzold LR, Doyle FJ. Modelling of detailed insulin receptor kinetics affects sensitivity and noise in the downstream signalling pathway. IFAC Proceedings Volumes (IFAC-PapersOnline). 2010;9(PART 1):326–31.
29. Le Novère N et al. The systems biology graphical notation. Erratum in: Nat Biotechnol. 2009;27(8):735–41. 27(9):864.
30. Copp J, Manning G, Hunter T. TORC-specific phosphorylation of mammalian target of rapamycin (mTOR): phospho-Ser2481 is a marker for intact mTOR signalling complex 2. Cancer Res. 2009;69:1821–7.
31. Jacinto E, Lorberg A. TOR regulation of AGC kinases in yeast and mammals. Biochem J. 2008;410:19–37.
32. Pearce L, Komander D, Alessi D. The nuts and bolts of AGC protein kinases. Nat Rev Mol Cell Biol. 2010;11:9–22.
33. Gual P, Le Marchand-Brustel Y, Tanti J. Positive and negative regulation of insulin signalling through IRS-1 phosphorylation. Biochimie. 2005;87:99–109.
34. Zick Y. Uncoupling insulin signalling by serine/threonine phosphorylation: a molecular basis for insulin resistance. Biochem Soc Trans. 2004;32:812–6.
35. Tremblay F, Marette A. Amino acid and insulin signaling via the mTOR/p70 S6 kinase pathway. A negative feedback mechanism leading to insulin resistance in skeletal muscle cells. J Biol Chem. 2001;276(41):38052–60.
36. Tsuchiya A, Kanno T, Nishizaki T. PI3 kinase directly phosphorylates Akt1/2 at Ser473/474 in the insulin signal transduction pathway. J Endocrinol. 2013; 220:49–59.
37. Copps KD, White MF. Regulation of insulin sensitivity by serine/threonine phosphorylation of insulin receptor substrate proteins IRS1 and IRS2. Diabetologia. 2012;n55(10):2565–82.
38. Skolnik EY, Lee CH, Batzer A, Vicentini LM, Zhou M, Daly R, Myers MJ Jr, Backer JM, Ullrich A, White MF, Schlessinger J. The SH2/SH3 domain-containing protein GRB2 interacts with tyrosine-phosphorylated IRS1 and Shc: implications for insulin control of ras signalling. EMBO J. 1993;12(5): 1929–36.
39. Kholodenko B, Hancock J, Kolch W. Signalling ballet in space and time. Nat Rev Mol Cell Biol. 2010;11:414–26.
40. Xiao F, Huang Z, Li H, Yu J, Wang C, Chen S, Meng Q, Cheng Y, Gao X, Li J, Liu Y, Guo F. Leucine deprivation increases hepatic insulin sensitivity via GCN2/mTOR/S6K1 and AMPK pathways. Diabetes. 2011;60:746–56.
41. Di Camillo B, Eduati F, Nair SK, Avogaro A, Toffolo GM. Leucine modulates dynamic phosphorylation events in insulin signalling pathway and enhances insulin-dependent glycogen synthesis in human skeletal muscle cells. BMC Cell Biol. 2014;15:9.
42. Orton RJ, Adriaens ME, Gormand A, Sturm OE, Kolch W, Gilbert DR. Computational modelling of cancerous mutations in the EGFR/ERK signalling pathway. BMC Syst Biol. 2009;3:100.
43. Yugi K et al. Reconstruction of insulin signal flow from phosphoproteome and metabolome data. Cell Rep. 2014;8(4):1171–83.
44. Kitano H. Biological robustness. Nat Rev Genet. 2004;5:826–37.
45. Bhalla U, Iyengar R. Robustness of the bistable behaviour of a biological signalling feedback loop. Chaos. 2001;11:221–6.
46. Freeman M. Feedback control of intercellular signalling in development. Nature. 2000;408:313–9.
47. Nyman E, Cedersund G, Strålfors P. Insulin signalling - mathematical modelling comes of age. Trends Endocrinol Metab. 2012;23:107–15.
48. Hu D, Yuan J. Time-dependent sensitivity analysis of biological networks: coupled MAPK and PI3K signal transduction pathways. J Phys Chem A. 2006;110:5361–70.
49. Perumal T, Gunawan R. Understanding dynamics using sensitivity analysis: caveat and solution. BMC Syst Biol. 2011;5:41.
50. Hoops S, Sahle S, Gauges R, Lee C, Pahle J, Simus N, Singhal M, Xu L, Mendes P, Kummer U. COPASI–a COmplex PAthway SImulator. Bioinformatics. 2006;22(24):3067–74.