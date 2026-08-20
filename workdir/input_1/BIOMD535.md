Citation: CPT Pharmacometrics Syst. Pharmacol. (2014) 3, e89; doi:10.1038/psp.2013.64  
© 2014 ASCPT   All rights reserved 2163-8306/12 <!-- marginalia, from page 0 (l=0.465,t=0.041,r=0.925,b=0.069), with ID 9e53c968-e44a-454b-b678-68a1a2a00868 -->

www.nature.com/psp <!-- text, from page 0 (l=0.464,t=0.070,r=0.577,b=0.086), with ID f7203a28-b15f-44f0-9bfb-c427900d9cb9 -->

ORIGINAL ARTICLE

A Multiscale Model of Interleukin-6–Mediated Immune Regulation in Crohn’s Disease and Its Application in Drug Discovery and Development <!-- text, from page 0 (l=0.071,t=0.088,r=0.914,b=0.198), with ID f2494c81-2046-4d79-9477-225eedf24df3 -->

G Dwivedi¹, L Fitz², M Hegen³, SW Martin⁴, J Harrold⁵, A Heatherington⁶ and C Li⁶ <!-- text, from page 0 (l=0.073,t=0.209,r=0.594,b=0.231), with ID f0039f2a-183c-4dd9-99e1-bdbd2905ab3a -->

In this study, we have developed a multiscale systems model of interleukin (IL)-6–mediated immune regulation in Crohn’s disease, by integrating intracellular signaling with organ-level dynamics of pharmacological markers underlying the disease. This model was linked to a general pharmacokinetic model for therapeutic monoclonal antibodies and used to comparatively study various biotherapeutic strategies targeting IL-6–mediated signaling in Crohn’s disease. Our work illustrates techniques to develop mechanistic models of disease biology to study drug–system interaction. Despite a sparse training data set, predictions of the model were qualitatively validated by clinical biomarker data from a pilot trial with tocilizumab. Model-based analysis suggests that strategies targeting IL-6, IL-6Rα, or the IL-6/sIL-6Rα complex are less effective at suppressing pharmacological markers of Crohn’s than dual targeting the IL-6/sIL-6Rα complex in addition to IL-6 or IL-6Rα. The potential value of multiscale system pharmacology modeling in drug discovery and development is also discussed.

*CPT Pharmacometrics Syst. Pharmacol.* (2014) 3, e89; doi:10.1038/psp.2013.64; published online 8 January 2014 <!-- text, from page 0 (l=0.073,t=0.236,r=0.923,b=0.395), with ID 8f2ce084-7820-4b04-984e-39fa5919e230 -->

INTRODUCTION

Among the factors impeding discovery of new drugs is a lack of understanding of the complex biological systems underlying diseases and systemic repercussions of drug candidate–target interactions.¹ Model-based drug discovery and development has been increasingly utilized to address this challenge²; in recent years, the multidisciplinary approach of systems pharmacology that combines systems biology with pharmacokinetic/pharmacodynamic (PK/PD) modeling principles has progressively drawn attention in the pharmaceutical industry.³ Systems pharmacology holds promise as a discipline that can help develop holistic understanding of interactions between drugs and complex biological systems underlying disease and has been termed the “next iteration” of model-based drug discovery and development.⁴⁻⁶ In this study, we have developed a multiscale systems model of Crohn’s disease to investigate candidate therapeutic strategies and to demonstrate the potential of quantitative systems pharmacology in drug discovery and development. <!-- text, from page 0 (l=0.073,t=0.408,r=0.489,b=0.689), with ID 5bf92dfc-55c3-429f-925c-4e039c45af7e -->

Crohn’s disease is an inflammatory bowel disease that is thought to be caused by a combination of genetic and environmental factors,^7 resulting in a proinflammatory environment in the mucosal layer of the gastrointestinal (GI) tract.^8 Along with several other cytokines that are perturbed in Crohn’s disease, interleukin (IL)-6 has been shown to be increased in intestinal mucosa and in peripheral blood.^9–12 IL-6 signaling is thought to be an important player in Crohn’s disease contributing to enhanced T-cell survival and apoptosis resistance in the lamina propria along with elevated chemokine secretion.^13 <!-- text, from page 0 (l=0.072,t=0.689,r=0.490,b=0.843), with ID b71466ae-0d2a-4d62-abf8-da6ae2e44839 -->

IL-6 signaling can occur via membrane-bound IL-6 receptor (IL-6Rα)—mediated classical pathway as well as soluble IL-6 receptor (sIL-6Rα)—mediated trans-signaling pathway (Figure 1a). The membrane-bound IL-6/IL-6Rα dimer or the circulating preformed complex of IL-6/sIL-6Rα can recruit a membrane-bound gp130 coreceptor, forming a heterotrimer which subsequently dimerizes, resulting in an active hexameric IL-6R receptor complex.14–16 This complex initiates phosphorylation of gp130-bound Janus kinase (Jak) family proteins and subsequent signal transducer and activator of transcription 3 (STAT3) phosphorylation.17 Trans-signaling may be important in disease because transmembrane IL-6Rα is expressed only in a small number of cell types, e.g., hepatocytes and a subset of leukocytes, whereas gp130 is almost ubiquitously expressed.18 Alternative gene splicing and shedding of transmembrane IL-6Rα are thought to be responsible for production of sIL-6Rα.19 IL-6Rα shedding was suggested to be accelerated by proteins including C-reactive protein (CRP).20 The coreceptor gp130 can also exist in a soluble form (sgp130), acting as a natural inhibitor of trans-signaling by sequestering the IL-6/sIL-6Rα complex16 (Figure 1a). The downstream effects of IL-6 signaling are multifarious, ranging from differentiation of lymphocytes to expression of acute-phase proteins such as CRP.18 The reported increase in serum concentrations of CRP,21 sIL-6Rα,22 and pSTAT3 in colon biopsies23 of Crohn’s disease patients may be due to trans-signaling via IL-6, acting on the broad range of cells that express gp130. <!-- text, from page 0 (l=0.507,t=0.411,r=0.921,b=0.787), with ID d73c4260-240c-4ac9-9c87-f43b3ab030bf -->

A pilot clinical trial with anti–IL-6R antibody, tocilizumab,
has shown positive clinical activity in Crohn’s disease,24 sug-
gesting inhibition of IL-6 signaling as a therapeutic strategy.
Several other strategies that modulate IL-6 signaling have <!-- text, from page 0 (l=0.507,t=0.786,r=0.922,b=0.844), with ID 038bc62f-863d-4978-9e7e-68f6f866bd67 -->

¹The Wallace H. Coulter Department of Biomedical Engineering, Georgia Institute of Technology and Emory University, Atlanta, Georgia, USA; ²Biotherapeutics Clinical Research, Pfizer Inc, Cambridge, Massachusetts, USA; ³Immunoscience, Pfizer Inc, Cambridge, Massachusetts, USA; ⁴Global Clinical Pharmacology, Pfizer Inc, Cambridge, Massachusetts, USA; ⁵Pharmacokinetics, Dynamics & Metabolism, Pfizer Inc, Cambridge, Massachusetts, USA; ⁶Quantitative Clinical Sciences, Biotherapeutics, Pfizer Inc, Cambridge, Massachusetts, USA. Correspondence: C Li (cheryl.li@pfizer.com)
Received 30 May 2013; accepted 14 October 2013; advance online publication 8 January 2014. doi:10.1038/psp.2013.64 <!-- text, from page 0 (l=0.075,t=0.866,r=0.920,b=0.933), with ID b93fa738-a39f-49ea-824e-331086a74801 -->

logo: npg <!-- marginalia, from page 1 (l=0.031,t=0.042,r=0.064,b=0.067), with ID b6731d1b-6b47-45cc-a0d1-2df77489b838 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn's Disease
Dwivedi et al <!-- marginalia, from page 1 (l=0.111,t=0.041,r=0.491,b=0.067), with ID 16459ce3-76b9-4f80-881f-b8b86f8ed2ad -->

Summary : This figure presents a schematic of a multiscale model for IL-6 signaling, comparing classical and trans-signaling pathways, their downstream effects, and the integration of these pathways into a compartmental model representing liver and gastrointestinal (GI) tract interactions.

flowchart:  
# Panel a: Classical and Trans-Signaling Pathways  
Nodes :  
  • IL-6 (ellipse)  
  • IL-6R (rectangle, membrane-bound)  
  • sIL-6R (rectangle, soluble)  
  • gp130 (rectangle, membrane-bound)  
  • Jak (rectangle, cytoplasmic)  
  • STAT3 (ellipse, cytoplasmic)  
  • pSTAT3 (ellipse, phosphorylated STAT3)  
  • pSTAT3:STAT3 dimer (ellipse)  
  • pSTAT3:E1v1SD dimer (ellipse)  
  • Transcription (rectangle)  
  • SOCS (rectangle, gene product)  
  • Other gene products (rectangle)  

Connectors :  
  • IL-6 binds IL-6R (classical) or sIL-6R (trans) at the membrane.  
  • Both complexes recruit gp130, activating Jak.  
  • Jak phosphorylates STAT3 to pSTAT3.  
  • pSTAT3 forms dimers (pSTAT3:STAT3 or pSTAT3:E1v1SD).  
  • Dimers translocate to the nucleus, initiating transcription of SOCS and other genes.  
  • sIL-6R/IL-6 can be sequestered by sgp130.  

Layout :  
  • Two parallel vertical pathways (classical left, trans right), converging at STAT3 activation and gene transcription.  

# Panel b: Reduced Model of IL-6 Signaling  
Nodes :  
  • IL-6  
  • IL-6R  
  • sIL-6R  
  • gp130  
  • STAT3  
  • pSTAT3  
  • Gene products  

Connectors :  
  • IL-6 binds IL-6R or sIL-6R, then gp130, leading to STAT3 phosphorylation and gene product expression.  

Layout :  
  • Simplified, linear pathway with fewer intermediates.  

# Panel c: Compartmental Multiscale Model  
Entities :  
  • Liver compartment (box)  
  • GI tract compartment (box)  
  • Circulation (dashed box connecting compartments)  
  • CRP (C-reactive protein)  
  • sIL-6R  
  • IL-6  
  • IL-6:sIL-6R complex  
  • IL-6:sIL-6R:sgp130 complex  
  • sgp130  
  • Gene products  

Relationships :  
  • Liver and GI tract exchange molecules via circulation.  
  • CRP is produced in the liver.  
  • Gene products are produced in the GI tract.  
  • sIL-6R is produced by CRP-mediated shedding.  
  • All molecules have basal production and decay.  

Layout :  
  • Two main organ compartments (liver, GI tract) connected by a central circulation box.  
  • Arrows indicate molecular exchange and production.  

# Analysis :  
  • The figure illustrates how both classical and trans IL-6 signaling pathways converge on the same downstream STAT3-mediated gene expression, with the possibility of pathway inhibition by sgp130.  
  • The reduced model (panel b) abstracts the essential steps for computational modeling.  
  • The compartmental model (panel c) integrates organ-level interactions, highlighting the role of CRP in sIL-6R production and the exchange of signaling molecules between liver and GI tract via circulation.  
  • The schematic emphasizes the multiscale nature of the model, from molecular interactions to organ-level communication. <!-- figure, from page 1 (l=0.078,t=0.084,r=0.494,b=0.574), with ID 587c7c3a-1e82-431c-92f3-391cb9b3aed8 -->

been proposed, which include targeting IL-6^25^ or IL-6R,^24^
using sgp130 as a natural antagonist of IL-6 trans-signal-
ing,^15,16^ or simultaneously inhibiting classical (target IL-6 or
IL-6R) and trans (target IL-6/sIL-6R complex) IL-6 signaling.^15^
Antibodies against these targets in Crohn’s disease are in
early clinical development; however, clinical biomarker or effi-
cacy data are currently unavailable. <!-- text, from page 1 (l=0.079,t=0.581,r=0.493,b=0.680), with ID 088cb24f-9908-43be-93b8-669c4a933bf0 -->

Systems biology models of IL-6–mediated immune signaling have been published previously,26–29 but these are single-scale models at the cellular level, and their translation to clinical end points has not been established. At a very different level of detail, PK/PD relationships of Ab–receptor interaction and biomarker or efficacy modulations are characterized in vitro and in vivo in preclinical and clinical studies. However, the PK/PD understanding is often limited by models based on limited data and lack of incorporation of biology. With various new IL-6–related therapeutic agents in the pipeline, we have developed a multiscale system model that integrates current knowledge about the biology of IL-6–mediated immune response in Crohn’s and used it for mechanistic assessment and comparison of several proposed therapeutic strategies. We have further used the model to explore the value of quantitative system pharmacology modeling in discovery and development, particularly in the areas of target selection, candidate optimization, and dose selection. <!-- text, from page 1 (l=0.080,t=0.681,r=0.493,b=0.931), with ID 79214609-4f6e-4bb5-89c4-4c0e72f70962 -->

RESULTS
Construction of the multiscale model of IL-6 signaling in Crohn’s disease
The multiscale model comprises three overlapping structural modules spanning spatial scales from cellular to organ levels. The first module describes events at the cellular level and consists of a reduced model of IL-6–mediated signal transduction. The second module is made up of target organs relevant in Crohn’s disease, and the first module (the cell signaling model) is embedded within these organs. The third and final module is a general PK model for monoclonal antibodies, including specific target binding that is linked to the first two modules to study the action of drug on the system. Each of these modules is described below. <!-- text, from page 1 (l=0.513,t=0.097,r=0.926,b=0.294), with ID e5ccf258-b9d2-48f4-abab-bb41d99ed415 -->

*Module 1: IL-6–mediated cellular signal transduction.*  
Detailed models of IL–mediated Janus kinase-Signal Transducer and Activator of Transcription (Jak-STAT) signaling, including IL-6/STAT3 signaling, have been described previously.26,30–32 Starting from the canonical structure of these models (schematic diagram in **Figure 1a**), we reduced the signaling network using a rationale-based approach to obtain a more parsimonious description while retaining the essential features of the IL-6 signaling pathway (**Figure 1b**). Simplifying assumptions used to reduce the model are listed in **Supplementary Text S1**. <!-- text, from page 1 (l=0.514,t=0.300,r=0.926,b=0.455), with ID efb12ba3-96ad-4dbf-896e-bf53fc1ffbb5 -->

*Module 2: integrating cell signaling with organ-level kinetics.* Instead of constructing a large-scale, physiologically based model accounting for all major organs in the body, we chose a parsimonious description by identifying the two most important target organs in Crohn’s disease and modeling them as separate, communicating compartments (**Figure 1c**). The first of these compartments represents the GI tract, which is the organ affected directly by Crohn’s disease.⁸ ¹³ The second compartment models the liver, which was included for its prominent role in the upregulation of acute-phase proteins associated with Crohn’s disease, such as CRP.²⁷ We further assumed that each of these organs was separately made up of homogeneous cell populations with identical signaling dynamics with minor differences (see **Supplementary Text S1** and <!-- text, from page 1 (l=0.514,t=0.469,r=0.926,b=0.676), with ID 09047951-660d-4127-b3c1-b00b61e713b3 -->

S2). Assuming that the IL-6 signaling network topology and reaction rate parameters remain conserved across different organs, we embedded the IL-6 signaling module into the cells of these organs. The organs were allowed to exchange soluble components through blood serum, which was modeled as a separate compartment representing the circulation. Briefly, starting from a single cell model, we scaled up to organs, modeling them as compartmentalized collections of cells and connected the organs through blood circulation (Figure 1c). Assumptions accompanying this module are listed in Supplementary Text S1. <!-- text, from page 1 (l=0.515,t=0.677,r=0.926,b=0.831), with ID a5756f28-8694-48a9-a2da-71182ff8ebde -->

*Module 3: PK of monoclonal antibodies.* To study the effects
of different therapeutic agents, we developed a module to
incorporate drug PK. The antibody PK model comprises
target-binding, dynamic exchange of free and bound drug
between organ compartments, and clearance of free as well
as bound antibody (**Supplementary Figure S1**). This model <!-- text, from page 1 (l=0.515,t=0.845,r=0.924,b=0.931), with ID 5ba7b97c-e6a9-48d2-9581-80e9297f4880 -->

CPT Pharmacometrics Syst. Pharmacol. <!-- marginalia, from page 1 (l=0.033,t=0.942,r=0.288,b=0.957), with ID 46fbc110-27ef-4923-b8b8-b1de0d208b5f -->

of drug PK describes the equilibration between multiple com-
partments incorporating both linear and target-mediated dis-
position of the antibody. <!-- text, from page 2 (l=0.074,t=0.097,r=0.487,b=0.144), with ID 9761af6f-b5d4-461f-a5d9-13977fb21b46 -->

Parameter estimation
We exploited the modular structure of our model to break
down the parameter estimation problem into a two-step
process. In the first step, the model was divided into struc-
tural modules, and parameters were either assigned values
available from the literature or estimated for each module in
isolation using any published data we could find (example
in Figure 2a). The model was reassembled by putting the
modules together, and the parameters were assigned val-
ues obtained from the first step as initial estimates. It was
expected that the estimates obtained from isolated mod-
ules would no longer be accurate with complex interactions
between the modules. Accordingly, in the second step, the
initial parameter estimates were further fine-tuned to fit the
system-level behavior of the whole model to available data.

When optimizing the parameters in step 2, we hypothe-
sized that observed differences in concentrations of molecu-
lar markers between healthy subjects and Crohn’s disease
patients are a systemic outcome of the differences in IL-6
concentrations. Therefore, although the model does not <!-- text, from page 2 (l=0.073,t=0.153,r=0.489,b=0.434), with ID d02830dc-bc1f-4510-a16a-7bffb999c37d -->

Summary : This multi-panel figure presents parameter estimation and pharmacokinetic (PK) modeling for IL-6 signaling and anti–IL-6 antibody distribution, including model fitting to experimental and literature data, and simulation of antibody concentrations in different tissues and dosing regimens.

line and scatter plots:  

# Panel a: Model Fitting to In Vitro Data  
Title & Axes :  
  • No explicit title; panel shows "Numbers/cell" vs. "Time (hour)".  
  • X-axis: Time (hour), ticks at 0, 2, 4, 6, 8.  
  • Y-axis: Numbers/cell, ticks at 0, 1,000, 2,000, 3,000, 4,000, 5,000.  
Data Points :  
  • Surface bound (model): solid brown line.  
  • Internalized (model): solid red line.  
  • Surface bound (exp): brown circles at (0, ~4,500), (1, ~2,500), (2, ~1,000), (4, ~500), (6, ~200).  
  • Internalized (exp): blue triangles at (0, ~0), (1, ~1,000), (2, ~1,500), (4, ~500), (6, ~200).  
Design Encodings :  
  • Solid lines for model predictions, filled circles and triangles for experimental data.  
Distribution & Trends :  
  • Surface bound peaks at time 0, declines rapidly.  
  • Internalized rises to a peak at ~2 hours, then declines.  

# Panel b: Model Fit to Literature Data  
Title & Axes :  
  • No explicit title; y-axis is "Fitted value / Target value" (log scale), x-axis lists biomarkers.  
  • X-axis: Serum IL-6, Serum sIL-6R, Serum CRP, Serum sgp130, Gut IL-6, Gut pSTAT3.  
  • Y-axis: Fitted value / Target value, log scale from 10^-2 to 10^2.  
Data Points :  
  • Healthy (red circles) and CD (blue triangles) for each biomarker, all within shaded area (10-fold range).  
Design Encodings :  
  • Red circles (Healthy), blue triangles (CD), shaded area for 0.1–10 range.  
Distribution & Trends :  
  • All points cluster near 1, within 10-fold of target values.  

# Panel c: Serum Antibody PK at Different Doses  
Title & Axes :  
  • No explicit title; y-axis "Serum Ab (nmol/l)", x-axis "Time (week)".  
  • X-axis: Time (week), ticks at 0, 5, 10, 15.  
  • Y-axis: Serum Ab (nmol/l), log scale from 1 to 10^3.  
Data Points :  
  • 10 mg: red solid line, dashed line.  
  • 100 mg: blue solid line, dashed line.  
  • 500 mg: yellow-green solid line, dashed line.  
Design Encodings :  
  • Solid lines: model; dashed lines: expected behavior from literature.  
  • Log scale y-axis.  
Distribution & Trends :  
  • All doses show repeated peaks and declines, higher doses yield higher concentrations.  

# Panel d: Tissue Distribution of Antibody  
Title & Axes :  
  • No explicit title; y-axis "Ab concentration (nmol/l)", x-axis "Time (week)".  
  • X-axis: Time (week), ticks at 0, 5, 10, 15.  
  • Y-axis: Ab concentration (nmol/l), log scale from 10^-1 to 10^2.  
Data Points :  
  • Serum: red line.  
  • Liver: blue line.  
  • GI tract: yellow-green line.  
Design Encodings :  
  • Distinct colors for each tissue, log scale y-axis.  
Distribution & Trends :  
  • Serum concentrations highest, followed by liver, then GI tract; all show periodic peaks and declines.  

# Analysis :  
  • The model fits both in vitro and literature data well, with most fitted/target ratios within a 10-fold range.
  • Antibody concentrations in serum, liver, and GI tract show periodic peaks corresponding to dosing, with higher doses producing higher concentrations.
  • Serum concentrations are consistently higher than in liver or GI tract.
  • The model captures both the kinetics of antibody distribution and the dynamics of IL-6 signaling components in health and Crohn’s disease. <!-- figure, from page 2 (l=0.075,t=0.445,r=0.923,b=0.933), with ID 15e28014-18ee-4653-92e7-e5bea06feb1b -->

www.nature.com/psp <!-- marginalia, from page 2 (l=0.820,t=0.943,r=0.968,b=0.957), with ID 6dee4f9f-a206-400a-8256-fe467af7596c -->

npg <!-- marginalia, from page 2 (l=0.938,t=0.044,r=0.968,b=0.066), with ID d1f02c42-7d40-4883-be8e-e7e0c62b4a52 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn’s Disease  
Dwivedi et al <!-- marginalia, from page 2 (l=0.510,t=0.043,r=0.888,b=0.066), with ID 6398d414-ca37-4f0e-adcf-f3adc6930f0d -->

logo: npg <!-- marginalia, from page 3 (l=0.030,t=0.041,r=0.065,b=0.067), with ID 78851e59-004c-41e8-943c-97b6ac8c0bb0 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn's Disease
Dwivedi et al <!-- marginalia, from page 3 (l=0.109,t=0.041,r=0.492,b=0.067), with ID 8bec7f54-ec9a-4726-bd6a-26d7520730e1 -->

4 <!-- marginalia, from page 3 (l=0.030,t=0.070,r=0.050,b=0.082), with ID 9bce40fb-5e5f-414f-9b75-f7a1bf05219f -->

Table 1 Concentrations of biomarkers used to optimize model parameters
<table><thead><tr><th>Marker</th><th>MW (kDa)</th><th>Healthy subject</th><th>Crohn's patient</th><th>References</th></tr></thead><tbody><tr><td>Serum IL-6</td><td>23.7ᵃ</td><td>1 pg/ml</td><td>10 pg/ml</td><td>10–12</td></tr><tr><td>Serum sIL-6R</td><td>50 (ref. 37)</td><td>80 ng/ml</td><td>140 ng/ml</td><td>10–12,20</td></tr><tr><td>Serum CRP</td><td>25.0ᵃ</td><td>1 mg/l</td><td>7 mg/l</td><td>20,21</td></tr><tr><td>Serum sgp130</td><td>100 (ref. 16)</td><td>390 ng/ml</td><td>280 ng/ml</td><td>10,11</td></tr><tr><td>Gut IL-6</td><td>23.7ᵃ</td><td>14 pg/ml</td><td>250 pg/ml</td><td>9 (see Supplementary Text S2)</td></tr><tr><td>Gut pSTAT3</td><td>–</td><td>1 au</td><td>3 au (fold change)</td><td>23,38</td></tr></tbody></table>
We used representative values for concentrations that had multiple sources in the literature. Molecular weights used to convert mass concentrations to molar concentrations are indicated in the second column. Fold change value was used for pSTAT3 in gut cells.
CRP, C-reactive protein; IL, interleukin; MW, molecular weight.
ᵃValues obtained from the Uniprot Protein Knowledgebase at www.uniprot.org. <!-- table, from page 3 (l=0.079,t=0.099,r=0.492,b=0.345), with ID 44b4cc94-e645-481c-8937-b8897417226f -->

treatment with placebo or 8 mg/kg anti–IL-6Rα antibody at intervals of 4 or 2 weeks (Figure 3a). The simulated anti–IL-6Rα antibody was assigned a Kd of 1 nmol/l as an order of magnitude estimate based on target-binding studies on tocilizumab.29 The PK profile of anti–IL-6Rα antibody in our simulation was in agreement with the reported PK profile of tocilizumab24 (Supplementary Figure S2). Comparing the simulation results with the mean CRP levels measured by Ito et al. under identical dose, we found that the model was successful at capturing the trend shown by the clinical study even though it could not reproduce the data quantitatively (Figure 3b). Similar to the clinical data, the model showed that an every 4-week intravenous (i.v.) administration of tocilizumab transiently reduced serum CRP, only to be restored to baseline level by the end of each 4-week cycle. For an every 2-week i.v. dosing schedule, both the model and clinical data showed a sustained reduction in serum CRP levels. However, under both dose schedules, the model underestimated the reduction in serum CRP when compared with the clinical data (compare Figure 3a and 3b). <!-- text, from page 3 (l=0.079,t=0.360,r=0.494,b=0.641), with ID bd58f004-03d1-471e-a428-78ade9dce6ac -->

Dose–response characteristics of anti–IL-6 and
anti–IL-6R antibodies are distinct
Using the optimized model, we simulated the effects of anti–
IL-6 and anti–IL-6Rα on PD biomarkers including serum
CRP, pSTAT3 activity in the GI tract, and IL-6 levels in the GI
tract and serum after every 4-week i.v. dosing for a 12-week
period. To examine the role of drug dose and antibody tar-
get–binding affinity in determining drug efficacy, we ran
multiple simulations while systematically varying the dose
and binding affinities of the antibodies. When administered
at sufficiently high doses, both anti–IL-6 and anti–IL-6Rα
(assumed to target both transmembrane and soluble IL-6Rα)
treatments lead to the suppression of serum CRP and gut
pSTAT3 in a time-dependent manner (Figure 4a,d, respec-
tively). Measured in terms of CRP suppression at the end of
the 12-week treatment, anti–IL-6 antibody had a graded dose
response tending toward saturation at high dose (Figure 4b).
Anti–IL-6Rα antibody, on the other hand, remained ineffective
over a large dose range but suddenly transitioned to high effi-
cacy at a certain dose threshold (Figure 4e). We found that <!-- text, from page 3 (l=0.078,t=0.650,r=0.494,b=0.935), with ID e54b3e0f-e2fb-43d0-b594-cc3ae6ada18c -->

Summary : This figure shows the effect of anti–IL-6Rα antibody treatment on serum CRP concentration over time, comparing model simulation and clinical trial data for placebo, every-4-week (Q4W), and every-2-week (Q2W) dosing regimens.

line and scatter plots:
# Panel a: Model Simulation
Title & Axes :
  • No explicit title in the panel, but context is "Simulation with placebo or 8 mg/kg intravenous dose of anti–IL-6Rα antibody at every 4-week (Q4W) and 2-week (Q2W) intervals".
  • X-axis: "Time (week)", ticks at 0, 2, 4, 6, 8, 10, 12.
  • Y-axis: "CRP (% of baseline)", ticks at 50, 70, 90, 110.
Data Points :
  • Placebo (red line): Flat at 100% CRP across all time points.
  • Q4W (blue line): Starts at 100%, drops to ~80% at week 2, rises and falls in a wave pattern, minimums around 70%, maximums near 100%.
  • Q2W (yellow-green line): Starts at 100%, drops to ~60% at week 2, oscillates with minimums near 55%, maximums near 80%.
Design Encodings :
  • Placebo: solid red line.
  • Q4W: solid blue line.
  • Q2W: solid yellow-green line.
  • No markers, no error bars.
Distribution & Trends :
  • Placebo remains constant.
  • Q4W and Q2W show periodic decreases in CRP, with Q2W achieving lower nadirs and more frequent oscillations.

# Panel b: Clinical Trial Data
Title & Axes :
  • No explicit title in the panel, but context is "Clinical data from a pilot trial with tocilizumab".
  • X-axis: "Time (week)", ticks at 0, 2, 4, 6, 8, 10, 12.
  • Y-axis: "CRP (% of baseline)", ticks at 0, 20, 40, 60, 80, 100, 120.
Data Points :
  • Placebo (red circles): (0, 100), (2, ~100), (4, ~90), (6, ~100), (8, ~90), (10, ~90), (12, ~90).
  • Q4W (blue triangles): (0, 100), (2, ~60), (4, ~100), (6, ~60), (8, ~100), (10, ~60), (12, ~100).
  • Q2W (yellow-green squares): (0, 100), (2, ~10), (4, ~10), (6, ~10), (8, ~10), (10, ~10), (12, ~10).
Design Encodings :
  • Placebo: red filled circles, connected by lines.
  • Q4W: blue open triangles, connected by lines.
  • Q2W: yellow-green open squares, connected by lines.
  • No error bars.
Distribution & Trends :
  • Placebo remains near 100% throughout.
  • Q4W alternates between ~100% and ~60% at each time point.
  • Q2W drops sharply to ~10% at week 2 and remains low.

# Analysis :
  • Both model and clinical data show that anti–IL-6Rα antibody treatment reduces CRP levels compared to placebo.
  • Q2W dosing achieves the greatest and most sustained reduction in CRP, with clinical data showing a rapid and persistent drop to ~10% of baseline.
  • Q4W dosing produces oscillations in CRP, with periodic returns to baseline in clinical data and less pronounced oscillations in the model.
  • Placebo groups remain near 100% of baseline CRP in both panels.
  • The model qualitatively matches the clinical data, especially in the pattern of oscillations and the relative efficacy of Q2W vs Q4W dosing. <!-- figure, from page 3 (l=0.513,t=0.097,r=0.927,b=0.578), with ID fd412a7d-e0f2-43c7-b619-3bf671aa0b8e -->

this qualitative difference of graded vs. switch-like response
was not CRP specific and was maintained across multiple
biomarkers (**Supplementary Figure S3**). Furthermore, both
antibodies showed increased effectiveness with increasing
target-binding affinity. <!-- text, from page 3 (l=0.513,t=0.584,r=0.927,b=0.656), with ID 7681a974-87ba-41a0-8216-9fb3b1a98779 -->

To explain this difference in response to the two antibod-
ies, we examined their PK and found that despite identical
parameters of distribution and linear clearance, the two
types of antibodies could have very different PK time profiles
depending on dose. For example, at 200 mg dose adminis-
tered every 4 weeks, the anti–IL-6 antibody concentration
was sustained at high enough levels to suppress IL-6 sig-
naling (Figure 4c), whereas the anti–IL-6Rα antibody was
severely depleted in 2 weeks (Figure 4f). Increasing the
dose to 500 mg sustained anti–IL-6Rα over the dose cycle
in a manner similar to anti–IL-6, resulting in higher effi-
cacy (Figure 4c,f). Increasing the dosing frequency also
resulted in greater efficacy at lower doses of anti–IL-6Rα
(Supplementary Figure S4). <!-- text, from page 3 (l=0.513,t=0.656,r=0.928,b=0.853), with ID 00b94d10-e444-44cc-874a-e3393435b6e1 -->

**Targeting the IL-6/sIL-6R complex in addition to free IL-6 or IL-6R as a therapeutic approach**
In all the simulations presented so far, it was assumed that the anti–IL-6 and anti–IL-6Rα antibodies bind only to free IL-6 and IL-6Rα, respectively. Given the hypothesized importance <!-- text, from page 3 (l=0.513,t=0.859,r=0.929,b=0.934), with ID b268e174-91c8-4a4e-8658-66b04841df46 -->

CPT Pharmacometrics Syst. Pharmacol. <!-- marginalia, from page 3 (l=0.031,t=0.941,r=0.290,b=0.958), with ID fcccbea5-3c0c-4487-980d-879c55ceb2c5 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn’s Disease  
Dwivedi et al <!-- marginalia, from page 4 (l=0.507,t=0.041,r=0.892,b=0.069), with ID a3e01eac-950c-44f4-a4dc-6717015b5c30 -->

logo: npg <!-- marginalia, from page 4 (l=0.936,t=0.043,r=0.969,b=0.065), with ID f27a0a0d-82a8-462d-85c1-b4aee85bcc24 -->

Summary : This figure presents two line plots (panels a and d) showing the time-course of four biomarkers (Serum CRP, Gut pSTAT3, Gut IL-6, Serum IL-6) over a 12-week period, with concentrations plotted on a logarithmic scale.

line plot:
# Panel Overview :
  • Two panels labeled "a" (top) and "d" (bottom), each showing four biomarker concentrations over time.
  • Both panels share the same x-axis (Time, in weeks) and y-axis (Concentration, in pmol/l).

# Title & Axes :
  • No explicit main title; panels labeled "a" and "d".
  • X-axis: "Time (week)", ticks at 0, 2, 4, 6, 8, 10, 12.
  • Y-axis: "Concentration (pmol/l)", logarithmic scale.
    – Panel a: y-axis range from 10^-7 to 10^2.
    – Panel d: y-axis range from 10^-2 to 10^4.

# Data Points :
  • Four series in each panel:
    – Serum CRP (red line)
    – Gut pSTAT3 (green line)
    – Gut IL-6 (yellow line)
    – Serum IL-6 (blue line)
  • Data are continuous lines, not discrete points.
  • All series are plotted across the full 12-week time course.

# Design Encodings :
  • Colour coding: Serum CRP (red), Gut pSTAT3 (green), Gut IL-6 (yellow), Serum IL-6 (blue).
  • All lines are solid.
  • Logarithmic y-axis.
  • No error bars or confidence intervals shown.
  • Legend present in the upper right of each panel.

# Distribution & Trends :
  • Panel a:
    – Serum CRP and Serum IL-6 start high and gradually decrease over time.
    – Gut pSTAT3 and Gut IL-6 start low, with stepwise increases at weeks 4 and 8.
    – All series show smooth, non-noisy trends.
  • Panel d:
    – Serum CRP and Serum IL-6 start high, with two noticeable dips (around weeks 2 and 6), then decrease.
    – Gut pSTAT3 and Gut IL-6 remain relatively flat, with Gut IL-6 higher than Gut pSTAT3.
    – All series are smooth.

# Analysis :
  • In both panels, Serum CRP and Serum IL-6 are consistently higher than Gut pSTAT3 and Gut IL-6.
  • Panel a shows stepwise increases in gut markers, while panel d shows more stable gut marker levels.
  • Both panels show a general decline in serum markers over time, with panel d displaying transient dips not seen in panel a.
  • The log scale highlights large differences in concentration between serum and gut markers. <!-- figure, from page 4 (l=0.080,t=0.091,r=0.345,b=0.449), with ID 8b96ba3d-2e4e-4123-97c3-2c697c5f38ff -->

Summary : This figure presents two line plots comparing the effect of antibody dose and binding affinity (K_d) on serum CRP suppression, for anti-IL-6 antibody (panel b) and anti-IL-6R antibody (panel e), at three different K_d values.

line plots:
# Panel b: Anti-IL-6 Ab dose vs. Serum CRP suppression
Title & Axes :
  • No explicit panel title, but context is "Anti-IL-6 Ab dose (mg)" vs. "Serum CRP suppression (%)".
  • X-axis: "Anti-IL-6 Ab dose (mg)", tick labels: 0, 200, 400, 600.
  • Y-axis: "Serum CRP suppression (%)", tick labels: 0, 20, 40, 60, 80, 100.

Data Points :
  • Three series, each representing a different K_d value:
    – K_d = 2.5 pmol/l (red circles): rises steeply, approaching 100% suppression by ~200 mg.
    – K_d = 25 pmol/l (blue triangles): moderate increase, reaching ~40% at 600 mg.
    – K_d = 250 pmol/l (yellow-green squares): minimal increase, plateauing below 20% at 600 mg.

Design Encodings :
  • Red circles for 2.5 pmol/l, blue triangles for 25 pmol/l, yellow-green squares for 250 pmol/l.
  • Solid lines connect points for each series.
  • Legend at upper right with marker shapes and K_d values.

Distribution & Trends :
  • For K_d = 2.5 pmol/l, rapid, saturating increase in suppression.
  • For K_d = 25 pmol/l, gradual, submaximal increase.
  • For K_d = 250 pmol/l, very low, flat response.

# Panel e: Anti-IL-6R Ab dose vs. Serum CRP suppression
Title & Axes :
  • No explicit panel title, but context is "Anti-IL-6R Ab dose (mg)" vs. "Serum CRP suppression (%)".
  • X-axis: "Anti-IL-6R Ab dose (mg)", tick labels: 0, 200, 400, 600.
  • Y-axis: "Serum CRP suppression (%)", tick labels: 0, 20, 40, 60, 80, 100.

Data Points :
  • Three series, each representing a different K_d value:
    – K_d = 2.5 pmol/l (red circles): flat at 0% until ~200 mg, then sharp increase to 100% by 400 mg.
    – K_d = 25 pmol/l (blue triangles): flat at 0% until ~400 mg, then sharp increase to 100% by 600 mg.
    – K_d = 250 pmol/l (yellow-green squares): flat at 0% until ~400 mg, then increase to ~60% at 600 mg.

Design Encodings :
  • Red circles for 2.5 pmol/l, blue triangles for 25 pmol/l, yellow-green squares for 250 pmol/l.
  • Solid lines connect points for each series.
  • Legend at upper right with marker shapes and K_d values.

Distribution & Trends :
  • For K_d = 2.5 pmol/l, threshold-like response: no effect until 200 mg, then rapid maximal suppression.
  • For K_d = 25 pmol/l, threshold at higher dose (400 mg), then rapid maximal suppression.
  • For K_d = 250 pmol/l, threshold at 400 mg, but only partial suppression (~60%) at highest dose.

# Analysis :
  • In both panels, lower K_d (higher affinity) antibodies achieve greater CRP suppression at lower doses.
  • Anti-IL-6 Ab (panel b) shows a gradual, saturating dose-response, especially for high-affinity antibody.
  • Anti-IL-6R Ab (panel e) shows a threshold effect: little suppression until a critical dose, then rapid increase.
  • At the highest K_d (lowest affinity), both antibodies are less effective, but anti-IL-6R Ab still achieves partial suppression at high dose.
  • The data visually demonstrate the importance of antibody affinity and target in determining dose-response characteristics for CRP suppression. <!-- figure, from page 4 (l=0.352,t=0.094,r=0.635,b=0.440), with ID 13b63cf6-54be-4dce-af9d-5b80ce99ee2c -->

Summary : This figure shows two line plots (panels c and f) comparing serum anti-IL-6 antibody (Ab) concentrations over 12 weeks following repeated dosing of either 500 mg or 200 mg, with dosing intervals and decay patterns visualized.

line plot:  

# Panel c :  
Title & Axes :  
  • No explicit panel title, but y-axis is “Serum anti-IL-6 Ab (nmol/l)” and x-axis is “Time (week)”.  
  • Y-axis range: 0 to 1,400 nmol/l.  
  • X-axis range: 0 to 12 weeks.  
  • Tick labels: Y-axis (0, 200, 400, 600, 800, 1,000, 1,200, 1,400); X-axis (0, 2, 4, 6, 8, 10, 12).  

Data Points :  
  • Two series:  
    – 500 mg (red line): Peaks at ~1,300 nmol/l at weeks 0, 4, and 8, with rapid decline after each dose.  
    – 200 mg (blue line): Peaks at ~500 nmol/l at weeks 0, 4, and 8, with similar rapid decline.  
  • Both series show repeated sharp peaks at dosing times (every 4 weeks), followed by exponential-like decay.  

Design Encodings :  
  • 500 mg: red line.  
  • 200 mg: blue line.  
  • Legend in upper right.  
  • No error bars or confidence intervals shown.  

Distribution & Trends :  
  • Both series show a sawtooth pattern: sharp rise at dosing, then rapid decline.  
  • Higher dose (500 mg) consistently yields higher peak and trough concentrations than 200 mg.  
  • Troughs do not return to zero before next dose.  

# Panel f :  
Title & Axes :  
  • Same axes and labels as panel c: “Serum anti-IL-6 Ab (nmol/l)” vs. “Time (week)”.  
  • Y-axis and x-axis ranges and ticks identical to panel c.  

Data Points :  
  • Two series:  
    – 500 mg (red line): Peaks at ~1,300 nmol/l at weeks 0, 4, and 8, with rapid decline after each dose.  
    – 200 mg (blue line): Peaks at ~500 nmol/l at weeks 0, 4, and 8, with similar rapid decline.  
  • Both series show repeated sharp peaks at dosing times (every 4 weeks), followed by exponential-like decay.  
  • The decay between doses appears slightly steeper than in panel c, with lower troughs before each new dose.  

Design Encodings :  
  • 500 mg: red line.  
  • 200 mg: blue line.  
  • Legend in upper right.  
  • No error bars or confidence intervals shown.  

Distribution & Trends :  
  • Both series show a sawtooth pattern: sharp rise at dosing, then rapid decline.  
  • Higher dose (500 mg) consistently yields higher peak and trough concentrations than 200 mg.  
  • Troughs approach lower values before next dose compared to panel c.  

# Analysis :  
  • Both panels illustrate the pharmacokinetics of anti-IL-6 antibody after repeated dosing, with higher doses producing higher serum concentrations.  
  • The sawtooth pattern indicates rapid absorption and clearance, with incomplete elimination before the next dose.  
  • Panel f shows steeper declines and lower troughs between doses compared to panel c, suggesting a difference in pharmacokinetic parameters or dosing regimen between the two panels.  
  • The 500 mg dose maintains higher antibody levels throughout the 12-week period than the 200 mg dose in both panels. <!-- figure, from page 4 (l=0.643,t=0.097,r=0.918,b=0.443), with ID 60a98db5-81fe-42d6-a413-406fb7dd4854 -->

Figure 4  Response to treatment with anti–IL-6 or anti–IL-6Rα antibody. All panels show results from simulation of intravenous dosing at 4-week intervals for a 12-week period. Anti–IL-6Rα targeted both transmembrane and soluble IL-6Rα. Time courses of a set of biomarkers after treatment with (a) 300 mg anti–IL-6 antibody or (d) anti–IL-6Rα antibody. Dose–response of (b) anti–IL-6 and (c) anti–IL-6Rα antibodies over varying target-binding affinities. The plotted values represent percent decrease in serum CRP from the baseline level after a 12-week treatment. Concentration of free drug in blood serum is maintained at higher levels for (c) anti–IL-6 at 200 and 500 mg doses but (f) anti–IL-6Rα is depleted in about 2 weeks at 200 mg dose. Higher dose of 500 mg helps maintain free anti–IL-6Rα at notable concentration. CRP, C-reactive protein; IL, interleukin. <!-- text, from page 4 (l=0.072,t=0.448,r=0.922,b=0.531), with ID d9efc266-a685-4a93-aa71-b35dd96f16dc -->

of the role of IL-6/sIL-6Rα complex in Crohn’s disease,¹⁵ we
ran simulations to assess the effects of targeting this complex
in addition to free IL-6 or IL-6Rα. <!-- text, from page 4 (l=0.074,t=0.538,r=0.489,b=0.581), with ID 386fb588-4f71-4ed2-a1c4-dacdfa87ad8d -->

When anti–IL-6 was allowed to bind to IL-6 and IL-6/sIL-6Rα complex with the same affinity, the dose–response characteristics of the antibody showed improved pharmacological efficacy over a range of doses and binding affinities in a dose-dependent manner (Figure 5a). However, similar improvement was not observed in the case of anti–IL-6Rα treatment, and the dose response remained largely unchanged (Figure 5b). <!-- text, from page 4 (l=0.074,t=0.581,r=0.488,b=0.695), with ID 2e678658-ccd1-4b6e-9345-fbc7e6a06f6d -->

Evaluating alternative therapeutic approaches using the model  
We performed global sensitivity analysis on the optimized model to assess the sensitivity of steady-state values of a panel of biomarkers to parameters of the model (see Methods section). The parameters to which the output was found to be least and most sensitive are shown in Figure 6a (see Supplementary Figure S5 for a complete list). The parameters that most strongly influenced the output biomarkers were rate of synthesis of IL-6 in the GI tract, rate of degradation of soluble receptor, parameters associated with IL-6–mediated production of CRP and CRP degradation. The production and degradation rates of sgp130 were among the least influential parameters. The sensitivity analysis suggests that while IL-6 and sIL-6Rα are among the best targets, sgp130-based therapies may not be as effective. <!-- text, from page 4 (l=0.073,t=0.704,r=0.489,b=0.931), with ID 9102288a-6e14-4063-b999-b1d0b4f570cf -->

A fusion protein combining the extracellular portion of gp130
with the Fc region of human IgG1 (sgp130Fc) has been shown
to inhibit IL-6 trans-signaling in cultured cells.16 To study the
potential of sgp130 as a therapeutic approach in Crohn’s dis-
ease, we simulated i.v. dosing of sgp130Fc at 4-week intervals.
We assumed that sgp130Fc binds the IL-6/sIL-6Rα complex
with the same affinity as natural sgp130 and that the PK of
sgp130Fc is identical to that of a typical monoclonal anti-
body with linear clearance. Dose–response curves in terms
of CRP suppression for several dose schedules are shown in
Figure 6b. Similar dose–response curves were obtained for
pSTAT3 suppression in gut (Supplementary Figure S6). In
agreement with the sensitivity analysis which suggested rela-
tive insensitivity of the output to sgp130, simulations showed
sgp130Fc to be effective only at very high and frequent doses. <!-- text, from page 4 (l=0.505,t=0.538,r=0.925,b=0.752), with ID 835d4500-0487-48de-b5d5-581d57afc6ef -->

DISCUSSION

We have constructed a system-level, multiscale, deterministic model of IL-6 signaling in Crohn’s disease that elucidates how ideas from traditional pharmacometrics can be combined with strategies from systems biology to design disease models in systems pharmacology. Our work advances existing systems pharmacology modeling methodologies and illustrates model development strategies with particular focus on integrating the role of cell signaling networks in disease. Although highly detailed quantitative models of system dynamics are desirable for several reasons,33 the construction of such models is often <!-- text, from page 4 (l=0.505,t=0.760,r=0.924,b=0.932), with ID 9eaa211a-a61e-4e01-b267-31681c32fff6 -->

www.nature.com/psp <!-- marginalia, from page 4 (l=0.820,t=0.942,r=0.970,b=0.959), with ID 342febe2-cafd-4f3e-85cf-c2e0a4a885fb -->

logo: npg <!-- marginalia, from page 5 (l=0.029,t=0.041,r=0.066,b=0.067), with ID c70a0649-85c7-47de-b2f5-4546c0bcb291 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn's Disease  
Dwivedi et al <!-- marginalia, from page 5 (l=0.109,t=0.041,r=0.492,b=0.067), with ID d6421805-e0a8-41f7-8a9e-435e0564d063 -->

Summary : This figure presents simulated dose-response curves for serum CRP suppression after 12 weeks of intravenous anti-IL-6 antibody treatment, comparing the effects of targeting IL-6/sIL-6Rα complex along with IL-6 or IL-6Rα, at different binding affinities (K_d values).

line chart:
Title & Axes :
  • No explicit main title, but two panels labeled "a" and "b".
  • X-axis: "Anti-IL-6 Ab dose (mg)", range: 0 to 600.
  • Y-axis: "Serum CRP suppression (%)", range: 0 to 100.
  • Tick labels: X-axis (0, 100, 200, 300, 400, 500, 600); Y-axis (0, 20, 40, 60, 80, 100).

Data Points :
  • Three series per panel, corresponding to K_d values:
    – Red circles: K_d = 2.5 pmol/l
    – Blue triangles: K_d = 25 pmol/l
    – Green squares: K_d = 250 pmol/l
  • Panel a:
    – Solid lines: Targeting only IL-6.
    – Dashed lines: Targeting both IL-6 and IL-6/sIL-6Rα.
    – Red circles (solid): Rapid increase in CRP suppression, plateauing near 100% by 100 mg.
    – Red circles (dashed): Similar rapid increase, plateauing at 100%.
    – Blue triangles (solid): Gradual increase, reaching ~40% at 600 mg.
    – Blue triangles (dashed): Steeper increase, reaching ~80% at 600 mg.
    – Green squares (solid): Minimal increase, ~10% at 600 mg.
    – Green squares (dashed): Slightly higher than solid, but still low (~20% at 600 mg).
  • Panel b:
    – Solid lines: Targeting only IL-6Rα.
    – Dashed lines: Targeting IL-6/sIL-6Rα complex.
    – Red circles (solid): No suppression until 400 mg, then jumps to 100%.
    – Red circles (dashed): No suppression until 400 mg, then jumps to 100%.
    – Blue triangles (solid): Gradual increase, sharp rise after 400 mg, reaching 100% at 600 mg.
    – Blue triangles (dashed): Similar trend, but slightly lower at 600 mg.
    – Green squares (solid): Minimal suppression, ~10% at 600 mg.
    – Green squares (dashed): Slightly higher than solid, but still low (~20% at 600 mg).

Design Encodings :
  • Red circles for K_d = 2.5 pmol/l, blue triangles for K_d = 25 pmol/l, green squares for K_d = 250 pmol/l.
  • Solid lines: Targeting only IL-6 (panel a) or IL-6Rα (panel b).
  • Dashed lines: Targeting both IL-6 and IL-6/sIL-6Rα (panel a), or targeting the complex (panel b).
  • Error bars shown for each data point.
  • Legend in both panels indicating K_d values and marker shapes.

Distribution & Trends :
  • Lower K_d (higher affinity) yields higher CRP suppression at lower doses.
  • Targeting both IL-6 and the complex (panel a, dashed) increases efficacy, especially at intermediate K_d.
  • Targeting the complex (panel b, dashed) does not significantly improve suppression over targeting only IL-6Rα.

Analysis :
  • The efficacy of anti-IL-6 antibody in suppressing serum CRP is strongly dependent on binding affinity (K_d), with higher affinity (lower K_d) producing greater suppression at lower doses.
  • Targeting both IL-6 and the IL-6/sIL-6Rα complex (panel a, dashed) enhances CRP suppression, especially at intermediate affinity (K_d = 25 pmol/l), compared to targeting only IL-6.
  • In contrast, targeting the complex in addition to IL-6Rα (panel b, dashed) does not provide a significant benefit over targeting IL-6Rα alone.
  • For the lowest affinity (K_d = 250 pmol/l), CRP suppression remains low regardless of targeting strategy or dose. <!-- figure, from page 5 (l=0.076,t=0.094,r=0.495,b=0.634), with ID 269b3ba4-3187-4b63-aa0d-37eeacabdedb -->

hindered by the sparsity of pertinent molecular-level kinetic
measurements. Therefore, a balance needs to be struck
between the level of detail in the model against the quality and
quantity of data available to reliably incorporate such detail.
To attain this balance, whenever possible, we have chosen
to favor parsimony in describing the biological processes in
our model. Notably, despite the simplifying assumptions and
limited amount of data available to train the model, we were
able to qualitatively validate the model against an indepen-
dent clinical data set (Figure 3). Particularly, even though the
CRP time course was not exactly replicated quantitatively by
the model in the validation step, the model was successful
at qualitatively predicting the long-term behavior of CRP fol-
lowing drug treatment in the typical Crohn’s disease patient
showing the model’s potential as a tool to study the effects of
perturbation through various treatments. <!-- text, from page 5 (l=0.078,t=0.650,r=0.494,b=0.874), with ID cc6ce055-ef71-470d-a48d-01244fb9adf3 -->

We compared four different strategies that have been proposed to treat Crohn’s disease by inhibition of IL-6 signaling through targeting IL-6, IL-6Rα, IL-6/sIL-6Rα in addition to IL-6 or IL-6Rα, or using sgp130Fc as an antagonist of IL-6 <!-- text, from page 5 (l=0.078,t=0.874,r=0.495,b=0.933), with ID d218a54e-337c-4a16-af78-3c411515b152 -->

Summary : This figure presents two analyses related to targeting strategies for sgp130Fc: (a) a sensitivity analysis bar chart showing which model parameters most influence steady-state biomarker values, and (b) a line plot showing the effect of sgp130Fc dose and dosing schedule on serum CRP suppression.

bar chart:
# a. Sensitivity analysis of model parameters

Title & Axes :
  • No explicit title on chart; described as "Sensitivity analysis".
  • X-axis: Parameter names (categorical; includes VmnDephos, KrmDephos, Kint, ksynfsgp130, kRAct, VmnProSynth, kCRPSecretion, kdegCRP, kdegSR, ksynfIL6Gut).
  • Y-axis: Sensitivity (au), range 0 to 1, tick labels at 0, 0.2, 0.4, 0.6, 0.8, 1.

Data Points :
  • VmnDephos: ~0.03
  • KrmDephos: ~0.03
  • Kint: ~0.03
  • ksynfsgp130: ~0.03
  • kRAct: ~0.03
  • VmnProSynth: ~0.13
  • kCRPSecretion: ~0.65
  • kdegCRP: ~0.7
  • kdegSR: ~0.7
  • ksynfIL6Gut: 1.0

Design Encodings :
  • All bars are cyan, vertical, with equal width and spacing.

Distribution & Trends :
  • Most parameters have low sensitivity (<0.15), except kCRPSecretion, kdegCRP, kdegSR, and ksynfIL6Gut, which are much higher.
  • ksynfIL6Gut is the most sensitive parameter (value = 1).

# b. Dose-response of sgp130Fc on serum CRP suppression

line plot:
Title & Axes :
  • No explicit title on chart; described as "The response to sgp130Fc in terms of serum CRP suppression from baseline".
  • X-axis: sgp30Fc dose (mg), range 0 to 2,000, tick labels at 0, 500, 1,000, 1,500, 2,000.
  • Y-axis: Serum CRP suppression (%), range 0 to 100, tick labels at 0, 20, 40, 60, 80, 100.

Data Points :
  • Three series:
    – Q4W (red circles): (0,0), (250,~5), (500,~10), (750,~13), (1,000,~15), (1,250,~17), (1,500,~18), (1,750,~19), (2,000,~20)
    – Q2W (blue triangles): (0,0), (250,~10), (500,~20), (750,~28), (1,000,~35), (1,250,~41), (1,500,~46), (1,750,~50), (2,000,~54)
    – Q1W (yellow squares): (0,0), (250,~20), (500,~38), (750,~52), (1,000,~63), (1,250,~71), (1,500,~77), (1,750,~82), (2,000,~85)

Design Encodings :
  • Q4W: red circles, solid line.
  • Q2W: blue triangles, solid line.
  • Q1W: yellow squares, solid line.
  • No error bars or confidence intervals shown.

Distribution & Trends :
  • All series show monotonic increase in CRP suppression with increasing dose.
  • Q1W schedule achieves the highest suppression at all doses, but the curve plateaus at higher doses.
  • Q2W is intermediate; Q4W is lowest and nearly linear.

Analysis :
  • The sensitivity analysis reveals that ksynfIL6Gut is the dominant parameter affecting steady-state biomarker values, with kCRPSecretion, kdegCRP, and kdegSR also influential.
  • For serum CRP suppression, more frequent dosing (Q1W) yields greater suppression, but the effect saturates at higher doses, especially for Q1W. Less frequent dosing (Q4W) results in much lower suppression, with a near-linear dose-response.
  • The data suggest diminishing returns for increasing dose at the most frequent dosing schedule. <!-- figure, from page 5 (l=0.514,t=0.097,r=0.931,b=0.652), with ID af5c2fca-1814-4ff2-a293-8270f4823aeb -->

trans-signaling. The model predicts that two of these strategies, targeting IL-6 or IL-6Rα, can effectively suppress markers of inflammation (CRP) and IL-6 signaling in target organs. Using sgp130Fc to exploit the natural ability of sgp130 to inhibit IL-6 signaling was predicted to be effective only at very high and frequent doses. Simulated dose–response curves as well as sensitivity analysis done on the model suggest that targeting IL-6 requires lower and less frequent dosing as compared with anti–IL-6Rα to achieve similar reduction of the systemic effects of IL-6 signaling. This statement must be qualified, however, by our observation that the model underestimated the effect of anti–IL-6Rα treatment when compared with clinical data (Figure 3). Nonetheless, the dose–response characteristics of anti–IL-6Rα are clearly distinct from those of anti–IL-6 (Figure 4b,e). This difference arises due to the immense disparity between the levels of free IL-6 (order of 10 pg/ml ≈ 10^-4 nmol/l)^12,13 and free sIL-6Rα (order of 100 ng/ml ≈ 1 nmol/l) in circulation.^22 At doses below a certain threshold, the antibody becomes the limiting factor in the anti–IL-6Rα/sIL-6Rα <!-- text, from page 5 (l=0.511,t=0.663,r=0.930,b=0.933), with ID 08e4fa97-66a1-4716-a224-c76d37f289ce -->

CPT Pharmacometrics Syst. Pharmacol. <!-- marginalia, from page 5 (l=0.031,t=0.941,r=0.291,b=0.958), with ID a1fa76e3-9e8a-42a4-b821-9a74c0bbdb37 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn's Disease  
Dwivedi et al <!-- marginalia, from page 6 (l=0.508,t=0.041,r=0.891,b=0.067), with ID 838c0db2-1efe-452e-8c01-da422408ea7b -->

logo: npg <!-- marginalia, from page 6 (l=0.937,t=0.043,r=0.969,b=0.065), with ID feb96e5b-8aab-45ad-af26-f99c8587b1dc -->

interaction as most of the antibody is sequestered by sIL-6Rα
(Figure 4f, 200 mg curve). Once this threshold is crossed, the
antibody overwhelms sIL-6Rα production and accumulates
in the system in sufficient amount (Figure 4f, 500 mg curve)
to suppress IL-6 signaling, resulting in the switch-like dose–
response curve seen in Figure 4e. <!-- text, from page 6 (l=0.074,t=0.097,r=0.488,b=0.182), with ID 8ca32d09-da54-43b9-b2df-252f2d7a600b -->

The PK profiles of anti–IL-6 and anti–IL-6Rα antibodies are different in our model (compare Figure 4c and 4f) due to differences in the kinetics of their interactions with their targets. Nonlinear clearance very similar to that predicted by the model for the anti–IL-6Rα antibody has been observed for tocilizumab at therapeutic doses in clinical studies in rheumatoid arthritis.34,35 This provides further validation to our modeling approach and shows that a well-constructed model of the underlying biological system can automatically accommodate target-mediated disposition of the antibody, reducing the need for case-by-case optimization of drug PK. <!-- text, from page 6 (l=0.073,t=0.182,r=0.488,b=0.334), with ID 96775a48-908f-4be8-9624-4f2c0ec24254 -->

The IL-6/sIL-6Rα complex is an important intermediate in
IL-6 signaling and has been proposed as a therapeutic tar-
get.15 We tested the relative gain in the efficacy of biomarker
modulation from combined targeting of the complex in addi-
tion to IL-6 or IL-6Rα. Greater dose-dependent modulation of
the immunological biomarkers was suggested in the case of
anti–IL-6 but not for anti–IL-6Rα. As argued above, at small
drug doses, substantial concentration of sIL-6Rα remains in
circulation and any IL-6/sIL-6Rα complex blocked by the anti-
body is quickly replenished, negating the effect of targeting
the complex. At larger drug doses when sIL-6Rα is effectively
suppressed by the antibody, IL-6/sIL-6Rα complex is natu-
rally depleted because reduced sIL-6Rα concentration drives
the IL-6/sIL-6Rα binding equilibrium toward the unbound
state. Taken together, at both high and low concentrations,
the effect of targeting the complex does not add much to the
efficacy of IL-6Rα targeting. <!-- text, from page 6 (l=0.073,t=0.334,r=0.488,b=0.570), with ID af211b19-ab6e-435c-b855-e51b6ff79ce0 -->

Targeting IL-6/sIL-6Rα alone to inhibit trans-signaling by
sgp130Fc was found to be effective only at very high and
frequent doses (**Figure 6b**). This result was supported by
sensitivity analysis using the model, which indicated that
altering the levels of sgp130 has very little effect on steady-
state values of a set of output parameters. This is explained
by the high baseline level of sgp130 (≈ 300 ng/ml or 3 nmol/l)
as compared with free IL-6 (≈ 10 pg/ml or 4 × 10⁻⁴ nmol/l).¹⁰⁻¹²
This means that sgp130 is basally present in large excess
when compared with the IL-6/sIL-6Rα complex, which is
limited by the low IL-6 concentration. The implication of this
concentration difference is that small perturbations in sgp130
level have minimal effect on system dynamics, and any
observable effects require large changes in sgp130. <!-- text, from page 6 (l=0.073,t=0.570,r=0.488,b=0.764), with ID 3f5abcfe-fa27-4ac1-ab57-d8a4b56dafb8 -->

One of the limitations of the current model is that it under-
estimates the CRP response under anti–IL-6R treatment.
The reasons for this are twofold. First, there was limited data
available to both train and validate the model, meaning that
estimates of some parameters could be inaccurate. Although
it may ultimately be possible to simulate first use of a drug
in humans in silico, achieving this routinely and with confi-
dence requires more two-way flow of information from clini-
cal trial back to the model for model training, and from model-
generated hypothesis to the clinic for testing. Currently, we do
not have sufficient dose–response clinical data available in
the literature to warrant model refinement based on the data. <!-- text, from page 6 (l=0.073,t=0.764,r=0.488,b=0.932), with ID e22bd54f-9f88-4e22-8130-2828532e953f -->

The model will be refined to incorporate emerging data from
ongoing anti-IL-6–related clinical studies to improve its predic-
tive power. Second, the structure of our model is limited by our
biological knowledge about the system, which leaves room for
improvement. For example, while we have singled out IL-6 sig-
naling to study the Crohn’s disease system, other cytokines
such as IL-10 and tumor necrosis factor-α are known to be
important in this disease. Future models could also include
distinct subpopulations of cells, such as T-lymphocyte subsets
in the GI tract which differentially influence the disease state. <!-- text, from page 6 (l=0.508,t=0.097,r=0.921,b=0.237), with ID 81ca7124-4a95-4654-99aa-d7fbee89202f -->

While admitting scope for improvement, the present work
demonstrates the potential of the systems pharmacology
approach in drug discovery and development. As demon-
strated by model-based comparison of the competing IL-6
signaling–related therapeutic strategies, the system model
can be tremendously valuable at the drug discovery stage.
Whereas intuition, simplified experimental systems, and
single-scale computational models are limited in their scope,
a multiscale systems pharmacology model is better able to
predict outcomes arising from system-level interactions and
combination treatment, and has enormous potential in facili-
tating target selection and candidate optimization in drug dis-
covery. The applications of systems pharmacology are not
limited to the discovery stage. Phase I studies in patients are
particularly relevant to the development of a quantitative sys-
tems pharmacology model, because it is at this stage that
the human PK and PD information of the new therapeutic
agent becomes available. Once a system model structure is
in place, integration of phase I biomarker data can facilitate
model refinement, resulting in more quantitative prediction of
clinical efficacy and/or safety responses based on correlation
with biomarker response. The refined model can aid optimal
proof-of-concept phase II design and support an optimal dos-
ing regimen. It is at this stage that one can truly test the correct
selection of targets, drugs, dosing, and therapeutic strategy.
Model development during phase II may be used to address
different questions related to the understanding of drug effect
for both safety and efficacy. Overall continuous integration of
system-level models with data from multiple sources and vari-
ous development stages would permit more complete exploi-
tation and interpretation of clinical response data for new and
existing therapeutic agents and could enhance decision mak-
ing throughout the development process. <!-- text, from page 6 (l=0.507,t=0.237,r=0.922,b=0.696), with ID 29b4c374-28b2-461e-ad3b-b25777937cdd -->

METHODS

Model implementation and parameter optimization. All modeling, simulation and analysis was done in Matlab (R2012b). The SimBiology toolbox of Matlab was used to implement the model (see Supplementary file 1 CD model and example Matlab script to run the model in Supplementary file 2 Sample Matlab code). To facilitate platform-independent exchange, Systems Biology Markup Language (SBML) versions of the models are also provided (Supplementary Files 3–6). Enzymatic reactions in the signaling pathway and pSTAT3-induced protein expression were modeled using Michaelis–Menten kinetics. All other events were modeled using mass action kinetics. All first-order rates have units of 1/hr, second-order rates are in l/(nmol·hr), and all concentrations are defined in nmol/l. All simulations were <!-- text, from page 6 (l=0.507,t=0.719,r=0.922,b=0.932), with ID c1070c9a-b85b-43aa-a8a6-3bf774a67369 -->

www.nature.com/psp <!-- marginalia, from page 6 (l=0.820,t=0.942,r=0.970,b=0.958), with ID 35e2205b-4e59-4182-832c-c641053a73f4 -->

logo: npg <!-- marginalia, from page 7 (l=0.029,t=0.041,r=0.066,b=0.067), with ID f68758c0-307e-441c-ba52-2897516790e4 -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn’s Disease
Dwivedi et al <!-- marginalia, from page 7 (l=0.108,t=0.041,r=0.493,b=0.067), with ID ac4c1830-8afe-4516-8e4c-31a76c08498a -->

performed by first running the model to steady state and then
simulating the effects of exogenous perturbations. Parameter
estimation was performed using a combination of fitting by hand
and functions from the optimization toolbox of Matlab. Further
details of the fitting process are described in **Supplementary
Text S3.** <!-- text, from page 7 (l=0.079,t=0.096,r=0.493,b=0.183), with ID dc565a67-06d7-4e38-a310-e0c27540d36c -->

*Global sensitivity analysis.* Partial rank correlation coefficients between the steady-state output and input parameters were calculated (**Supplementary Text S4**).$^{36}$ To get a single sensitivity measure per parameter, the partial rank correlation coefficients for each parameter were summed over the output species and divided by a constant to scale the highest sensitivity to 1 (see **Supplementary Figure S5**). <!-- text, from page 7 (l=0.080,t=0.188,r=0.493,b=0.289), with ID 42d367dd-a7ad-4d2e-8b9c-ea6543f56036 -->

**Author Contributions.** C.L. and G.D. wrote the manuscript. C.L. and G.D. designed the research. C.L., G.D., L.F., M.H., J.H., and A.H. performed the research. G.D. analyzed the data. <!-- text, from page 7 (l=0.079,t=0.296,r=0.493,b=0.344), with ID 6cefe91a-24f7-4ba1-8b57-caddb0644624 -->

**Conflict of Interest.** The authors declared no conflict of in-
terest. <!-- text, from page 7 (l=0.080,t=0.350,r=0.492,b=0.380), with ID cf9787a1-662e-420d-8e48-8e15b1c24df8 -->

Study Highlights

WHAT IS THE CURRENT KNOWLEDGE ON THE TOPIC?
✓ Strategies for integrating cell signaling information into disease models are evolving. Drug research in Crohn’s disease can benefit from the systems approach as development of biological therapeutics for the disease is in progress.

WHAT QUESTION DID THIS STUDY ADDRESS?
✓ How can traditional modeling techniques used in drug development be combined with systems modeling to develop predictive models of complex diseases? How do different therapeutic strategies for Crohn’s disease compare as predicted by a systems model?

WHAT THIS STUDY ADDS TO OUR KNOWLEDGE
✓ Our study illustrates modeling techniques that can be used in systems pharmacology to develop multiscale, system-level models that integrate information across cellular and organ levels. It provides specific testable hypotheses about multiple therapeutic strategies for Crohn’s disease.

HOW THIS MIGHT CHANGE CLINICAL PHARMACOLOGY AND THERAPEUTICS
✓ We show that system models based on sound biological knowledge have the potential to meaningfully inform the drug discovery and drug development process by providing mechanistic details of drug–system interactions. <!-- text, from page 7 (l=0.079,t=0.410,r=0.489,b=0.928), with ID 343bccc1-9884-47e3-b7bb-8da77830c010 -->

1. Butcher, E.C., Berg, E.L. & Kunkel, E.J. Systems biology in drug discovery. Nat. Biotechnol. 22, 1253–1259 (2004).
2. Derendorf, H. et al. Pharmacokinetic/pharmacodynamic machine in drug research and development. J. Clin. Pharmacol. 40, 1399–1418 (2000).
3. van der Graaf, P.H. & Benson, N. Systems pharmacology: bridging systems biology and pharmacokinetics-pharmacodynamics (PKPD) in drug discovery and development. Pharm. Res. 28, 1460–1464 (2011).
4. Iyengar, R., Zhao, S., Chung, S.W., Mager, D.E. & Gallo, J.M. Merging systems biology with pharmacodynamics. Sci. Transl. Med. 4, 126ps7 (2012).
5. Kitano, H. Computational systems biology. Nature 420, 206–210 (2002).
6. Allerheiligen, S.R. Next-generation model-based drug discovery and development: quantitative and systems pharmacology. Clin. Pharmacol. Ther. 88, 135–137 (2010).
7. Baumgart, D.C. & Carding, S.R. Inflammatory bowel disease: cause and immunobiology. Lancet 369, 1627–1640 (2007).
8. Baumgart, D.C. & Sandborn, W.J. Inflammatory bowel disease: clinical aspects and established and evolving therapies. Lancet 369, 1641–1657 (2007).
9. Mitsuyama, K. et al. Colonic mucosal interleukin-6 in inflammatory bowel disease. Digestion 50, 104–111 (1991).
10. Narazaki, M. et al. Soluble forms of the interleukin-6 signal-transducing receptor component gp130 in human serum possessing a potential to inhibit signals through membrane-anchored gp130. Blood 82, 1120–1126 (1993).
11. Mahida, Y.R., Kurlac, L., Gallagher, A. & Hawkey, C.J. High circulating concentrations of interleukin-6 in active Crohn’s disease but not ulcerative colitis. Gut 32, 1531–1534 (1991).
12. Gustot, T. et al. Profile of soluble cytokine receptors in Crohn’s disease. Gut 54, 488–495 (2005).
13. Mudter, J. & Neurath, M.F. IL-6 signaling in inflammatory bowel diseases: pathophysiological role and clinical relevance. Inflamm. Bowel Dis. 13, 1016–1023 (2007).
14. Boulanger, M.J., Chow, D.C., Brevnova, E.E. & Garcia, K.C. Hexameric structure and assembly of the interleukin-6/IL-6 alpha-receptor/gp130 complex. Science 300, 2101–2104 (2003).
15. Rose-John, S., Waetzig, G.H., Scheller, J., Grötzinger, J. & Seegert, D. The IL-6/sIL-6R complex as a novel target for therapeutic approaches. Expert Opin. Ther. Targets 11, 613–624 (2007).
16. Jostock, T. et al. Soluble gp130 is the natural inhibitor of soluble interleukin-6 receptor transsignaling responses. Eur. J. Biochem. 268, 160–167 (2001).
17. Heinrich, P.C., Behrmann, I., Haan, S., Hermanns, H.M., Müller-Newen, G. & Schaper, F. Principles of interleukin (IL)-6-type cytokine signalling and its regulation. Biochem. J. 374, 1–20 (2003).
18. Maggio, M., Guralnik, J.M., Longo, D.L. & Ferrucci, L. Interleukin-6 in aging and chronic disease: a magnificent pathway. J. Gerontol. A Biol. Sci. Med. Sci. 61, 575–584 (2006).
19. Jones, S.A., Horiuchi, S., Topley, N., Yamamoto, N. & Fuller, G.M. The soluble interleukin 6 receptor: mechanisms of production and implications in disease. FASEB J. 15, 43–58 (2001).
20. Jones, S.A., Novick, D., Horiuchi, S., Yamamoto, N., Szalai, A.J. & Fuller, G.M. C-reactive protein: a physiological activator of interleukin 6 receptor shedding. J. Exp. Med. 189, 599–604 (1999).
21. Schreiber, S. et al.; CDP870 Crohn’s Disease Study Group. A randomized, placebo-controlled trial of certolizumab pegol (CDP870) for treatment of Crohn’s disease. Gastroenterology 127, 807–818 (2004).
22. Mitsuyama, K. et al. Soluble interleukin-6 receptors in inflammatory bowel disease: relation to circulating interleukin-6. Gut 36, 45–49 (1995).
23. Carey, R. et al. Role of IL-6-STAT3-dependent transcription in pediatric-onset steroid- inflammatory bowel disease. Inflamm. Bowel Dis 14, 446–457 (2008).
24. Ito, H. et al. A pilot randomized trial of a human anti-interleukin-6 receptor monoclonal antibody in active Crohn’s disease. Gastroenterology 126, 989–996; discussion 947 (2004).
25. Nishimoto, N. Interleukin-6 as a therapeutic target in candidate inflammatory diseases. Clin. Pharmacol. Ther. 87, 483–487 (2010).
26. Moya, C., Huang, Z., Cheng, P., Jayaraman, A. & Hahn, J. Investigation of IL-6 and IL-10 signaling via mathematical modelling. IET Syst. Biol. 5, 15 (2011).
27. Vermeire, S., Van Assche, G. & Rutgeerts, P. C-reactive protein as a marker for inflammatory bowel disease. Inflamm. Bowel Dis 10, 661–665 (2004).
28. Dirks, N.L. & Meibohm, B. Population pharmacokinetics of therapeutic monoclonal antibodies. Clin. Pharmacokinet. 49, 633–659 (2010).
29. Mihara, M. et al. Tocilizumab inhibits signal transduction mediated by both mIL-6R and sIL-6R, but not by the receptors of other members of IL-6 cytokine family. Int. Immunopharmacol. 5, 1731–1740 (2005).
30. Yamada, S., Shiono, S., Joo, A. & Yoshimura, A. Control mechanism of JAK/STAT signal transduction pathway. FEBS Lett. 534, 190–196 (2003).
31. Zi, Z., Cho, K.H., Sung, M.H., Xia, X., Zheng, J. & Sun, Z. In silico identification of the key components and steps in IFN-gamma induced JAK-STAT signaling pathway. FEBS Lett. 579, 1101–1108 (2005).
32. Singh, A., Jayaraman, A. & Hahn, J. Modeling regulatory mechanisms in IL-6 signal transduction in hepatocytes. Biotechnol. Bioeng. 95, 850–862 (2006).
33. Havellock, W.S. Recent advances in the molecular biology of Stat6. Biol. Soc. 5, 240 (2009). <!-- text, from page 7 (l=0.510,t=0.094,r=0.932,b=0.930), with ID 26171365-fd55-49dd-b680-66b2d1c42068 -->

CPT Pharmacometrics Syst. Pharmacol. <!-- marginalia, from page 7 (l=0.031,t=0.941,r=0.290,b=0.958), with ID 2e25f82d-3f44-4bc8-b05e-f72fa183eafd -->

A Multiscale Model of IL-6–Mediated Immune Regulation in Crohn's Disease  
Dwivedi et al <!-- marginalia, from page 8 (l=0.508,t=0.041,r=0.891,b=0.069), with ID fd48b4a3-b1ed-4e7c-84b6-afa80462e161 -->

Summary : This image is a logo consisting of the lowercase letters "npg" in a serif font, centered within a solid black circle.

logo: npg

Design Elements :
  • Lowercase letters "npg" in white, serif typeface.
  • Letters are centered within a solid black circular background.
  • No additional text, tagline, or graphic elements present.
  • The logo is monochrome (black and white).

Dimensions & Placement :
  • The black circle fully encloses the letters with even margins.
  • The logo is square in aspect ratio.

Analysis :
  • The logo is simple and minimalistic, likely representing a brand or publisher abbreviated as "npg". The use of a serif font and monochrome palette suggests a formal or academic identity. <!-- figure, from page 8 (l=0.937,t=0.043,r=0.969,b=0.065), with ID ffcf5be4-6c91-4cf6-8df9-eb626c6d0539 -->

34.  Nishimoto, N. *et al.* Toxicity, pharmacokinetics, and dose-finding study of repetitive
      treatment with the humanized anti-interleukin 6 receptor antibody MRA in rheumatoid
      arthritis. Phase I/II clinical study. *J. Rheumatol.* **30**, 1426–1435 (2003).
35.  Frey, N., Grange, S. & Woodworth, T. Population pharmacokinetic analysis of tocilizumab in
      patients with rheumatoid arthritis. *J. Clin. Pharmacol.* **50**, 754–766 (2010).
36.  Marino, S., Hogue, I.B., Ray, C.J. & Kirschner, D.E. A methodology for performing global
      uncertainty and sensitivity analysis in systems biology. *J. Theor. Biol.* **254**, 178–196
      (2008).
37.  Yasukawa, K. *et al.* Purification and characterization of soluble human IL-6 receptor
      expressed in CHO cells. *J. Biochem.* **108**, 673–676 (1990). <!-- text, from page 8 (l=0.072,t=0.096,r=0.487,b=0.209), with ID bf5ed5a7-b42e-43e0-bcc0-a153c0491687 -->

38.  Mudter, J. et al. Activation pattern of signal transducers and activators of transcription (STAT) factors in inflammatory bowel diseases. *Am. J. Gastroenterol.* **100**, 64–72 (2005). <!-- text, from page 8 (l=0.508,t=0.095,r=0.916,b=0.125), with ID e444a155-f5d5-41fe-8a5c-3af35182f494 -->

logo: Creative Commons BY-NC-ND

_CPT: Pharmacometrics & Systems Pharmacology_ is an open-access journal published by _Nature Publishing Group_. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivative Works 3.0 License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/3.0/ <!-- text, from page 8 (l=0.507,t=0.136,r=0.923,b=0.210), with ID 9240871c-f560-4e4c-86bd-5aa8f9622149 -->

Supplementary information accompanies this paper on the _CPT: Pharmacometrics & Systems Pharmacology_ website (http://www.nature.com/psp) <!-- text, from page 8 (l=0.140,t=0.216,r=0.854,b=0.248), with ID 094472c4-1bf5-475c-b0de-fe5caf94aacb -->

www.nature.com/psp <!-- marginalia, from page 8 (l=0.819,t=0.942,r=0.970,b=0.959), with ID 267f77af-e0ce-457d-a3ef-b8b38daf2fdb -->