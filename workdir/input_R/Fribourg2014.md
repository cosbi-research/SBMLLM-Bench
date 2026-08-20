<a id='5d56c78c-f785-4705-8cbb-d26d8f783e5a'></a>

NATIONAL INSTITUTES OF HEALTH

NIH Public Access
**Author Manuscript**
*J Theor Biol. Author manuscript; available in PMC 2015 June 21.*

<a id='b7d3ae8c-efa9-4411-bc2e-aff97c5b3637'></a>

Published in final edited form as:
_J Theor Biol._ 2014 June 21; 351: 47-57. doi:10.1016/j.jtbi.2014.02.029.

<a id='9110d6f6-e5e7-43b1-9c84-5556fe7a66b4'></a>

**Model of influenza A virus infection: dynamics of viral antagonism and innate immune response**

M. Fribourg¹, B. Hartmann¹, M. Schmolke²,³, N. Marjanovic¹, R.A. Albrecht²,³, A. García-Sastre²,³,⁴, S. C. Sealfon¹, C. Jayaprakash⁵, and F. Hayot¹´*

¹Department of Neurology and Center for Translational Systems Biology, Icahn School of Medicine at Mount Sinai, New York, NY, 10029

²Department of Microbiology, Icahn School of Medicine at Mount Sinai, New York, NY, 10029

³Global Health and Emerging Pathogens Institute, Icahn School of Medicine at Mount Sinai, New York, NY, 10029

⁴Department of Medicine, Division of Infectious Diseases, Icahn School of Medicine at Mount Sinai, New York, NY, 10029

⁵Department of Physics, Ohio State University, Columbus, OH 43210

<a id='fbacd8e2-8e58-4e2c-b49a-e9d51051f273'></a>

# Abstract

Viral antagonism of host responses is an essential component of virus pathogenicity. The study of the interplay between immune response and viral antagonism is challenging due to the involvement of many processes acting at multiple time scales. Here we develop an ordinary differential equation model to investigate the early, experimentally-measured, responses of human monocyte-derived dendritic cells to infection by two H1N1 influenza A viruses of different clinical outcome: pandemic A/California/4/2009 and seasonal A/New Caledonia/20/1999. Our results reveal how the strength of virus antagonism, and the time scale over which it acts to thwart the innate immune response, differ significantly between the two viruses, as is made clear by their impact on the temporal behavior of a number of measured genes. The model thus sheds light on the mechanisms that underlie the variability of innate immune responses to different H1N1 viruses.

<a id='92624233-4891-47da-aee8-461136589f50'></a>

## 1. Introduction

Despite advances in treatment and vaccination, influenza A virus remains a major international health concern [1]. Influenza virus strains vary in their pathogenicity, and epidemiological features. The causes of these differences are not fully understood and may include a combination of viral dynamics, previous immunity, and the virus specific effects

<a id='81ceed6c-e220-4875-9074-be99355e9557'></a>

 2014 Elsevier Ltd. All rights reserved.
*To whom correspondence should be addre

<a id='53a8db8a-77c9-498e-9deb-8a7eef0e8877'></a>

**Publisher's Disclaimer:** This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

<a id='1d85a11a-51f7-4b5b-bcc7-4c3ec1b8efbe'></a>

NIH-PA Author Manuscript

<a id='358c33df-15f6-42b1-8d27-05094e00ca9c'></a>

NIH-PA Author Manuscript

<a id='95916bba-a898-452a-b614-be16fe471c9a'></a>

NIH-PA Author Manuscript

<a id='f577a65f-e0c8-42e9-830c-c449a0b0e470'></a>

ssed: fernand.hayot@mssm.edu.

<!-- PAGE BREAK -->

<a id='46d2293b-efbf-4897-9d35-b74b2261ad11'></a>

Fribourg et al.

<a id='dad41355-cb5d-4388-ab62-9f472518484a'></a>

Page 2

<a id='040c2265-5127-4443-8ba9-56cf992af2d5'></a>

of antagonism on the innate immune response (for reviews see [2, 3, 4]). The interplay between these two opposing forces—the immune response and the virus strategy to evade it—is complex and involves multiple processes acting at different time scales. This complexity makes the study of the early dynamics of response to viral infection and the comparison between different viral strains challenging.

<a id='4016f4e5-55ca-4630-984c-f384a236f364'></a>

Many cellular components are involved in the innate immune response to infection, including epithelial barriers, phagocytes such as neutrophils and macrophages (the first line of defense against microbes if they breach these barriers), natural killer cells, and dendritic cells. Dendritic cells (DCs) are particularly interesting because they possess the unique capability of triggering and directing adaptive cell-mediated immune responses in a way that is dependent on their innate immune responses to microbes. In that way, differences in the early response may have a major impact on the immune response following infection.

<a id='12bfec10-1443-40a8-8ef8-dd69b9b4e842'></a>

The first steps of DCs early immune response upon virus detection are interferon IFNΒ production, its secretion and binding to interferon receptors, and subsequent activation of signal transduction pathways that trigger the coordinated induction of a diverse set of genes, the so-called ISGs (Interferon stimulated genes) that establish an antiviral state in uninfected cells and in infected cells. While many details of this complex process have not been fully characterized, the main ingredients have been identified. We developed a theoretical model for the early-time dynamics of the DC immune response to different viral strains based on key steps in the virus-DC interaction, and compared our results with our recent experimental measurements. Viral entry into the cell is detected by a cytoplasmic protein RIG-I. This detection leads initially to the activation of a number of transcription factors, which are responsible for the induction of genes, such as TNFα, and most importantly IFNΒ. Protein IFNΒ is secreted, and binds in an autocrine and paracrine manner to its cognate receptors on cell surfaces. Its binding activates the Jak/Stat pathway. This pathway, via phosphorylation and dimerization of STAT1 and STAT2, leads to the induction of many genes, some of which give rise to antiviral proteins such as OAS and MX1, others to RIG-I which is instrumental in detecting the virus, and to IRF7, which in infected cells enhances IFNΒ induction and is the transcription factor of IFNα.

<a id='bfe39dc2-bf62-4462-bea9-24a48f09cbf9'></a>

Influenza A virus has developed multiple strategies to thwart DCs cellular response to infection. One of its main weapons in evading DC response is the viral non-structural NS1 protein coded by one of the eight negative-sense segments of the viral RNA [5, 6]. NS1 is a multifunctional protein that interferes with the immune response at many levels [7], starting with the detection of viral presence by the cell. It reduces the level of IFNẞ induction [8], prevents dendritic cell maturation and consequently the activation of adaptive immunity [9]. In the early stages of infection, the NS1 protein counteracts the immune response at two main points, by limiting on the one hand virus detection, and by interfering on the other with antiviral gene induction by the host cell. The virus escapes detection because the NS1 protein prevents in different ways [3] the activation of the cytoplasmic viral sensor RIG-I. It blunts antiviral gene induction through binding to the host CPSF protein [10, 11] which is essential for pre-mRNA processing, and also to proteins of the nuclear export system, blocking nuclear export [12]. Lack of activation of RIG-I leads to curtailment of the signaling pathways that activate NFκB, IRFs, and AP-1, which participate in the formation

<a id='0f3a103a-dac8-4b9a-82dd-7221cedfbff8'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='d851c087-71af-4f6e-8ba4-850c971ed429'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='da0ef1ca-f4ca-40b3-95a7-621aa2a6bb1c'></a>

Fribourg et al.

<a id='c0d72579-c703-4b0b-a6b9-70075e828a30'></a>

Page 3

<a id='0ab3332b-143c-4dbe-bded-a0e50038e45c'></a>

of the enhanceosome responsible for IFNβ induction. The suppression of IFNβ induction is a serious blow to the cell's antiviral response, since it entails reduced secretion of IFNβ, and therefore diminished paracrine and autocrine signaling. For many strains of influenza A virus such as pandemic A/California/4/2009, this appears to be the principal aspect of their antagonistic function [3, 13]. For others such as seasonal A/New Caledonia/20/1999, there is, in addition, inhibition of pre-mRNA processing and nuclear mRNA export and therefore curtailment of cytoplasmic mRNA levels. There is a time window of opportunity for the host cell to mount a strong response before the virus can produce enough NS1 proteins to block the anti-viral functions of the host cell. Therefore, both understanding this competing dynamics in the first few hours after infection and extracting the differences between flu strains are of great interest and therefore the focus of our modeling study.

<a id='a304bf86-adc9-4031-987c-67d6348c27be'></a>

In order to shed light on the interplay, for different viruses, between the processes involved in NS1 antagonism and the immune response, we studied the infection of human monocyte-derived DCs by two influenza A H1N1 viruses, either the pandemic swine-origin A/California/4/2009 (Cal/09), or the seasonal A/New Caledonia/20/1999 (NC/99). We developed an ordinary differential equation (ODE) model applicable to both types of viral infection. The model embodies the contest between the cell's defense system following viral entry and detection, and the virus' attempts to thwart it. We tested the model results against experimental time course data for a reduced set of genes. Our model is—to the best of our knowledge—the first one to incorporate viral antagonism at the scale of intracellular interactions. This ODE model enabled us to explain the differences in the immune response to the two viruses, which are illustrated in Figure 1 by the time courses of IFNβ gene expression for Cal/09 and NC/99. It allowed us to extract the specific features, such as strength and time scale, of NS1 antagonism for each viral strain, and its impact on gene expression in IFNβ induction and in IFNβ signaling pathways.

<a id='9d11ba10-cbeb-4633-b738-675dcb6b5658'></a>

## 2. Methods

### 2.1. Model description and assumptions

The present model is built from one [14, 15] we developed for understanding data on infection of human monocyte-derived DCs with influenza virus PR8 after pretreatment with IFNß, or with Newcastle Disease Virus (NDV) expressing Nipah virus proteins [16, 17]. The similarity of the equations in the two models is the consequence of a common early immune response of DCs. The equations differ by the ways viral antagonism acts, because the latter does so very differently for Nipah chimeras and influenza A viruses.

<a id='cfa9a885-d8af-489c-95d8-7dd075a56c0b'></a>

Our model comprises main elements of the innate immune network of genes and proteins in DCs. The schematic of the innate immune response network described by the ordinary differential equation (ODE) model is shown in Figure 2, where, additionally, the points of viral NS1 protein antagonist activity are marked. There are three compartments, external medium, cytoplasm and nucleus, and a positive feedback loop associated with IFNβ/α, and TNFα. The cellular protein RIG-I detects viral intrusion and initiates a signaling pathway that leads to the induction of TNFα and IFNβ. Upon secretion the latter activates the Jak/ Stat pathway through phosphorylation of Tyk2/JAK1*, followed by phosphorylation of STAT, formation of dimers, translocation to the nucleus, and induction of IRF7 which

<a id='cba97ff7-606d-41d2-9838-4ca5a035e191'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='505c3d3f-d2bf-4ab5-b2a4-1636900872ef'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='93268afe-3351-4151-bdda-0166a10a51d8'></a>

Fribourg et al.

<a id='6e0ff4e0-66a6-4811-ac97-0b7c4f16d82e'></a>

Page 4

<a id='19491190-7aad-4f8a-a82c-1706b6ab192a'></a>

contributes to IFN̑̆́/́̈ induction. There is induction as well of SOCS which impedes STAT
phosphorylation, and therefore the upstream activation of the interferon-induced signaling
pathway.

<a id='5a302488-efc4-437b-ad21-e5cf04c2ac14'></a>

The following assumptions have been introduced in the model. We do not distinguish STAT1 and STAT2, SOCS1 and SOCS3, and do not introduce explicitly the transcriptional trimer ISGF3 that comprises IRF9 besides the STAT dimer [3, 4] in order to avoid the introduction of numerous unknown parameters while preserving the basic mechanistic structure of the response. We take into account a possible Jak/Stat pathway-independent induction of SOCS [18], but neglect the indirect influence of TNFα on the Jak/Stat pathway through induction of IFNβ with the help of IRF1 [19], as well as interferon-independent pathways for induction of interferon-stimulated genes (ISGs) [20].

<a id='91217685-ce7e-4763-9a19-22a4e699baa9'></a>

IRF7 is singled out for two reasons. It is the transcription factor of the IFNa gene, and it contributes strongly to the formation of the IFNΒ transcription complex [21]. More importantly, the measured time course of IRF7 gene expression after viral infection is typical of similar genes induced by the same trimeric complex (ISGF3), genes such as RIG- I, and the antiviral genes MX1 and OAS [18, 22]. This is seen in our experimental data on IRF7, MX1, DDX58 (the gene that codes for the cytoplasmic viral sensor RIG-I), OAS1/2, and EIF2AK2 (PKR) (Figure 3), all of them genes induced in the Jak/Stat pathway by interferon signaling. The data show that, for the same infecting virus, the time course behavior of any one of these genes is similar. Furthermore, the relative magnitude of gene expression levels for the two viral infections (NC/99 and Cal/09) is approximately maintained across the genes. Thus, for the sake of model simplification, IRF7 can be taken as the representative gene of this class of interferon-stimulated genes important in the immune response.

<a id='10359fa2-d5e3-4b23-b3f2-9c04b6db00d3'></a>

## 2.2. Model equations
The equations of the model represent the network and its interactions shown in Figure 2. They describe the temporal behavior of IFNβ/α mRNA and TNFα mRNA and their respective proteins in the environment, of STAT mRNA and its protein denoted STAT, of the phosphorylated STAT dimer STATP2n in the nucleus, of SOCS mRNA, and of IRF7 mRNA and activated IRF7 protein IRF7Pn in the nucleus. There are thus 12 network components and equations. Apart from the crucial factors in the equations that describe the antagonism carried by the viral NS1 protein, the equations are similar to those in reference [15], which includes a detailed derivation based on an extensive review of the literature.

<a id='6af927a3-0ec7-4010-ac6a-681f99e2cbe2'></a>

In the present model, NS1 antagonism of the immune response is characterized by expressions IC1 and IC2, explained below (section 2.3.), that embody the principal, dual aspect of viral antagonism of both interferon induction and mRNA preprocessing. The equations are:

<a id='7734f23b-e0c7-478f-bde9-6c423feceab7'></a>

dIFN βm/dt=(r0 * IC1+k15 IRF7Pn) * IC2-IFN βm * log(2)/τ1 (1)

<a id='5af6da87-ba16-43e2-a75e-39e89c553b4c'></a>

$$dIFN\beta_{env}/dt = \gamma C v_{max2}IFN\beta_m / (K_2+IFN\beta_m) \quad (2)$$

<a id='504a6eb1-32bf-46c8-9bd6-0575ea0a5417'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='6f62c51e-1f22-40a9-af35-496095bdd8ab'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='b84eddf3-1dee-4679-a3f6-2903d22510ed'></a>

Fribourg et al.

<a id='fa26e95a-f6af-4a7c-814d-aa660dbaabfb'></a>

Page 5

<a id='5e22eabe-fea3-43d8-9465-c03c8d2df492'></a>

dSTATP2n/dt=k5TJ * STAT/2(K5+STAT)-STATP2n *log(2)/τ3 (3)
dSOCSm/dt=(r3*IC1+k8STATP2n) * IC2-SOCSm *log(2)/τ4 (4)
dIRF7m/dt=(k11 STATP2n+k14IRF7Pn) * IC2-IRF7m*log(2)/τ6 (5)

<a id='40462f5b-607c-447f-b769-846fd33f2479'></a>

dIRF7Pn/dt=k12IRF7m * IC1 (6)

<a id='a95d6606-7c9d-4bf3-a57a-244661a1e3a0'></a>

$$dIFN\alpha_m/dt = k_{16}IRF7Pn * IC2 - IFN\alpha_m * \log(2)/\tau_8 \quad (7)$$

<a id='95ba1bb9-40aa-4585-93a3-4b6b64d79154'></a>

$$dIFN\alpha_{env}/dt = \gamma Cv_{max17} IFN\alpha_m / (K_{17} + IFN\alpha_m) \quad (8)$$

<a id='15b3f65c-c2ee-428f-a47d-c15baa152e02'></a>

$$ \frac{dTNF\alpha_m}{dt} = \left( r1 * IC1 + \frac{r20 * TNF_{env}}{K20 + TNF_{env}} \right) * IC2 - TNF\alpha_m * \frac{\log(2)}{\tau_9} \quad (9) $$

<a id='ceb1fc09-2dab-48c2-b6b3-7a4a61010c9f'></a>

dTFN_env/dt = \gamma C v_{max19} TFN\alpha_m / (K_{19} + TFN\alpha_m) (10)

<a id='21240f6a-ce79-435d-8128-c3f18f09be12'></a>

dSTAT_m/dt = (r_4 * IC1 + k_{26} STATP_{2n}) * IC2 - STAT_m * log(2) / τ_{12} (11)

<a id='8c62ec69-8af0-43c5-b970-41309af6e2a0'></a>

dSTAT/dt = k₂₆STATm - STAT * log(2)/τ₁₃ (12)

<a id='c5a60bca-888b-4dad-8f14-185ece5aa14b'></a>

The 12 species names denote the corresponding concentrations in µM, C is the experimental concentration of cells in the medium which is 5 × 10⁵ cells/ml. The factor γ = 10⁹/N_A (where N_A is Avogadro's number and equal to 6.023×10²³ molecules/mol) in equations (2), (8) and (10) is a conversion factor from numbers per ml for the right-hand sides of these equations to concentrations in µM for the left-hand sides. *TJ* is a quantity that describes binding of IFNα/β in the environment to their receptors and the effect of the negative feedback loop associated with SOCS. The expression of *TJ* is

<a id='01c79be1-6041-4419-b761-db363a84fe06'></a>

$$TJ = TJ_{tot} \frac{IFN\beta_{env} + IFN\alpha_{env}}{K_3 + IFN\beta_{env} + IFN\alpha_{env}} \frac{1}{1 + \frac{K_9 SOCS_m}{\delta}} (13)$$

<a id='b1beca8f-961d-447f-a0fa-f5a0087dc7ae'></a>

The constants have the same values for the two viruses Cal/09 and NC/99, with $TJ_{tot} = 10^{-4}$
μM, $K_3 = 4.3 \times 10^{-3}$ μM, $K_9 = 7.8 \times 10^2$, and $δ = 0.0003$ μM. Initial values are zero for all
molecules, except for STAT proteins, for which the concentration is taken to be 0.1 μM.

<a id='8c1fe7ad-1aee-49cf-8d52-0e45c6d8f12e'></a>

Each model equation for gene expression is composed of a production term on which NS1 antagonism acts, and a degradation term characterized by a half-life. As an example, consider equation (1) for IFNΒ mRNA induction, the gene whose expression is most crucial

<a id='79f49a48-057d-4ff4-bd52-d5444a5abf70'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='c32acc3c-b952-48b8-a820-db6dbdf89b9b'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='70e925ab-2f3b-4068-92f5-76121a6e040c'></a>

Fribourg et al.

<a id='fd9ae9c1-ab7c-40e6-bbe3-fd6697ddc5f0'></a>

Page 6

<a id='11d1e707-7b4d-4bd0-81a5-b8344d83aa23'></a>

to the innate immune response. The induction of interferon-β mRNA contains an early response term represented in a very simple way by r0 that occurs due to the constitutive presence in the cell of all of the components of the IFNβ enhanceosome (the higher r0, the faster the induction of IFNβm). The degradation term is characterized by a half-life τ1, in such way that the longer the half-live, the slower the degradation of IFNβm. The amount of IFNβm as a function of time is the result of the combined effect of production and degradation. The viral antagonism of the production process is denoted by the factor IC1 defined below (expression (14)) (the lower the IC1 value, the greater the antagonism and its reduction of r0). In addition, there is a positive feedback due to IRF7Pn that is included in the second term. Since the production of mRNA by both processes is curtailed by the CPSF binding mechanism of NS1, both terms are multiplied by the viral antagonism described by IC2 also defined below (expression (15)). The two antagonisms, embodied in the terms IC1 and IC2, depend on the time-dependent concentration of the NS1 protein (expression (16)), which we infer for each viral strain from NS1 mRNA measurements (Figure 4).

<a id='997d40c4-60ae-46e0-b201-50232639770d'></a>

## 2.3. Viral antagonist factors

The viral antagonist factors that appear in the equations above are denoted IC1 and IC2. IC1 represents NS1 protein antagonism in the pathway leading to IFNβ induction which is activated after viral detection by RIG-I. IC2 represents NS1 protein curtailment of cytoplasmic mRNA levels due to viral inhibition of pre-mRNA processing and blocking of mRNA nuclear export. In the absence of antagonism, the factors IC1 and IC2 which multiply the production terms in the model equations are equal to 1. In the presence of antagonism, the smaller their value, the stronger the corresponding antagonism is in suppressing production.

<a id='4c281f7c-76f4-4164-87f9-3b5e4a2f0b5e'></a>

IC1 and IC2 depend on time, because their expression depends on the concentration of the viral NS1 protein (denoted NS) which depends on time (equation (16)). We use the following Hill-type equations for IC1 and IC2:

IC1 = (1 + sp * (NS/δ₁)^n₁) / (1 + (NS/δ₁)^n₁) (14)

IC2 = (1 + sv * (NS/δ₂)^n₂) / (1 + (NS/δ₂)^n₂) (15)

<a id='f5cb61d9-d37a-4c84-85dc-088b2df7cf42'></a>

Here δ1 and δ2 act as thresholds for the action of the antagonism. At saturation values of NS, IC1 and IC2 respectively reach the values of sp and sv. Pre-mRNA processing inhibition is considered very weak for Cal/09 NS1 [13] and therefore we take IC2=1 for Cal/09 infection.

<a id='c09f6ade-53ec-47c7-b99e-71e363ad8bc0'></a>

The inhibitory factors IC1 and IC2 depend on the concentration of the NS1 protein (_NS_), which is not measured in our experiments. However its temporal behavior can be estimated from the measured NS1 mRNA (Figure 4).

<a id='8cbd53e8-40bd-46b6-8c84-1a7be2cab497'></a>

For the growth in time of NS1 protein (_NS_) we use the following Hill function form

<a id='8a0fad27-3768-49ea-b7a8-e1b400bcb0d9'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='1876014e-857b-4486-8773-10399189a18b'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='e9c064d8-6b41-42ca-b3b1-537fdae2864e'></a>

Fribourg et al.

<a id='bbea0701-6be8-4fd8-b566-8c39be51f864'></a>

Page 7

<a id='b53504fb-f682-4765-b5c5-1b9d1f9cbb1d'></a>

NS = r5 * t^n3 / (bm^n3 + t^n3) (16)

<a id='e5102aca-7c71-488f-912c-ab05e402191e'></a>

The value of r5 = 1 µM. The value (in hours) of bm, which describes how fast NS1 protein rises, is estimated from the time behavior of the two viral NS1 mRNAs in Figure 4. Here one sees that the rise of Cal/09 NS1 mRNA is slower and occurs later than the rise of NC/99 NS1 mRNA. The fixed values of n3 and bm in expression (16) reflect this difference (see Table 1), and are taken to be respectively equal to 5 and 6 hr for Cal/09, and 8 and 4.5 hr for NC/99.

<a id='1f162d7f-cdd1-4b40-bd32-08bfb7eb778a'></a>

## 2.4. Simulations and Parameter values

The immune response gene levels were obtained experimentally from luminosity measurements (see Appendix B), whereas the model ones are expressed in terms of concentration. Since there is no accurate calibration of luminosities, the comparison of model results and experimental data requires the use of normalized expression levels. We therefore divide, for both viruses, each gene level at each time point by the corresponding Cal/09 gene expression level at the last measured time point after infection, which is 8 hours.

<a id='b3e8cce5-1fe4-4f0f-9145-c9db902a29f7'></a>

For all parameters in the equations, except those associated with NS1 antagonism, the values found previously for NDV-Nipah virus infection of human DCs [15] serve as calibration. We fit the model results to experimental measurements of the gene expression levels of IFNẞ, IFNa, TNFa, STAT and IRF7. Of the total number of parameters in the model for either virus, most are estimated (see Table 1). The number of parameters varied to achieve fits to the data is reasonably small, 10 parameters for 35 data points for Cal/09 corresponding to the measurements of five genes at eight time points, and 13 parameters for 40 data points for NC/99 obtained from the corresponding measurements of the same five genes. The number of independent data points is smaller for Cal/09 because of the normalization to their eight hour time point for each gene expression level. A comprehensive summary of the parameters fitted and estimated can be found in Table 1.

<a id='0618313c-aa00-425b-bbad-851e8b6c31f8'></a>

The fitting for each viral infection proceeds in stages that rely on comparison of model simulation and of experimental results, with the aim of reducing the differences between them across time for the five genes considered. The fitting procedure is designed to obtain qualitative fits to the data for parameter values in a biologically-reasonable region of parameter space, with emphasis on the time scales involved in the temporal development of gene expression, in particular those that characterize the two NS1 antagonism factors IC1 and IC2 (see section 2.3.). For parameters common to this and our previous work, the starting values are taken from our previous investigations of human DC infections by NDV-Nipah protein chimeras [15]. Many parameters are kept fixed (see Table 1), such as half-lives; we identified by inspection of the model equations and the experimental data those parameters that can be expected to play a dominant role in fitting the model results to the data, and varied them manually. There are 10 parameters that are varied for Cal/09 infection and 13 for NC/99 infection (see Table 1) with 3 less for Cal/09 because IC2=1 (see section 2.3.). The 13 parameters are the rate of IRF7 translation, the rates of gene induction (for

<a id='9786a575-3159-4398-86b9-b963136e7b40'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='e566e7ad-54a3-41e2-90b8-354896b881ce'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='def29211-9dad-4960-b489-f59d12e48d9a'></a>

Fribourg et al.

<a id='59028dda-5a78-45f2-86eb-4d816db982e2'></a>

Page 8

<a id='38cdecc8-ae8a-4487-a735-ac45f2618843'></a>

IFN̢, IRF7, IFŅ, TNF̧, and STAT) which in the model determine the early linear rise of gene production, as well as the strengths, thresholds and exponents for the two factors IC1 and IC2 that define NS1 antagonism and counteract the early linear rise of gene expression levels. The parameter values for IC2, which represents the expression of NS1 antagonism to interferon signaling operative for viral strain NC/99 and not for Cal/09, are mainly determined by the model fits to IRF7 and STAT mRNA expression levels. For these two genes only IC2 antagonism enters directly, because their expression is not part of the IFN̢ induction pathway but is stimulated through interferon signaling. There is also in expression (13) an additional fitted parameter, namely the Michaelis-Menten constant K3, which controls the impact of secreted interferon on downstream gene expression. One obtains in the end a reasonably good fit of the model to experimental results in a domain of parameter values restricted by the above mentioned calibration, though presumably not the best possible one in a much larger parameter space.

<a id='f73367dd-4104-474f-919a-fe13063922f8'></a>

We followed our informed manual fit by the use of an evolutionary algorithm to check whether the parameter values obtained as described above belonged to the family of optimal solutions when the antagonism parameters for IC1 and IC2 (sv, sp, δ₁, δ₂, nl, and n2) are varied in our model over a wide range of parameter values. For this purpose we used a standard genetic algorithm [23] with a fitness function equal to the least-square distance between model and experimental results. Briefly, we generated a starting set of vectors with the parameter values, tested their fit to the experimental data using the least-square cost function, and retained the solutions with the lowest value. These solutions were in turn mutated by changing the values of the parameters, and checked for an improvement in the fit of the model to the data. At each iteration the best solutions were saved and mutated again. The algorithm stopped when no more improvement in fitting the experimental data was achieved. The range of parameter values explored for Cal/09 are n1 = [0.1, 3.16], δ₁ = [0.01, 10], and sp = [0.03, 30]. The range of parameter values explored for NC/99 are n1 = [0.5, 15.81], δ₁ = [0.01, 10], sp = [0.01, 10], n2 = [0.5, 15.81], δ₂ = [0.04, 40], and sv = [0.03, 30]. The results from the evolutionary algorithm support our choice of time scales and relative magnitudes of the parameters for each virus, in particular those parameter values that occur in expressions (14) and (15) of IC1 and IC2 and which characterize the two ways NS1 antagonism acts.

<a id='69ba0f33-0030-4e7f-be07-e558669d72f6'></a>

Viral antagonism determines to a large extent the temporal behavior of gene expression levels, which therefore can show a high sensitivity to certain parameters associated with viral antagonism. In Appendix A we study the sensitivity of IFN̘ and IRF7 with respect to parameters of the antagonist factors IC1 and IC2. This sensitivity is itself a time-dependent quantity because it depends on the characteristic behavior in time of IC1 and IC2 (Appendix A).

<a id='e642e54a-70a9-443d-8eb3-259884fb6b5e'></a>

All simulations were performed in MATLAB (http://www.mathworks.com) with the _ode15s_
solver for the differential equations, and the genetic algorithm functions of the Optimization
Toolbox for the evolutionary algorithms.

<a id='deb5b1cb-eb40-4059-8674-b2c394318e09'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='307bcfc4-c068-4770-b13b-13eaf6c6f621'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='cd6a137c-203b-4589-af99-0416b1761f32'></a>

Fribourg et al.

<a id='d28b0e73-3ed6-42e2-a531-8f30ccf340a4'></a>

Page 9

<a id='be1d4c5b-a6e4-4714-9be7-e185cdea0698'></a>

## 2.5. Data analysis: infected and uninfected cells

Infections of human dendritic cells by influenza A are not productive [24], and thus the amount of infected cells depends exclusively on the initial infection and remains stable during the experiment. The model considered (see section 2.2) describes infected cells. However, experimentally the system contains both infected and uninfected cells, and measurements have contributions from both varieties for those genes expressed as a result of interferon signaling. This poses a problem for comparing model results to experimental data which is resolved below.

<a id='5a5538aa-2c69-443e-a862-b6e6f53e2888'></a>

In our experimental measurements multiplicity of infection (MOI) is equal to 1. At MOI=1, close to 40% of the cells are uninfected. Uninfected cells get stimulated through paracrine signaling by the cytokines secreted by the infected cells as part of their immune response. Any experimental measurement of interferon stimulated genes (ISGs) has contributions from both infected and uninfected cells. The contribution from uninfected cells can dominate ISG gene expression whenever their number is high. NS1 antagonism of ISG mRNA nuclear processing and export, when present, acts in infected cells only, and thus enhances even more the relative contribution to ISG expression from uninfected cells. Comparison of model with experiment for the two viruses, Cal/09 and NC/99, therefore requires a method for estimating the contribution from uninfected cells to the measured expression levels of ISGs, of which there are two in the model, namely IRF7 and STAT1. We obtain this estimate in a semi-quantitative way. As a first approximation, and neglecting the effect of other pathways, we suppose that, for Cal/09, infected and uninfected cells, which bathe in the same cytokine environment, have similar expression levels for ISGs, because of the lack of CPSF binding by the Cal/09-encoded NS1 [18]. If this is a reasonable assumption, the expression levels of ISGs in DCs infected by Cal/09 should only weakly depend on the number of infected versus uninfected cells, i.e. on the value of MOI. A comparison of interferon stimulated gene IP10 expression levels for MOI=0.5, 1 and 2 is consistent with this assumption (data not shown). We then posit that uninfected cells behave the same way for NC/99 as for Cal/09. One neglects thus the differences that may exist between the two viruses as to the magnitude and time dependence of the respective cytokine environments and their impact on cell receptors. One is then led to the prescription that for NC/99 infections, for any ISG, one should subtract from the experimental data the 40% contribution coming from Cal/09 measurements, which represents an estimate of the contribution to each measured gene from the uninfected cells. The same procedure is applied to Cal/09 itself. The remainder of gene expression level for the two ISGs in the model, IRF7 and STAT1, is the amount due to infected cells, which is the amount compared to the numerical solutions of our model. Despite its approximate character, we believe our method for extracting the contribution of uninfected cells to be adequate for our purpose, which is the comparison for the two viruses considered of the mechanisms of NS1 antagonism and their development in time after infection.

<a id='decf1933-a726-4f93-9c28-537210381f7e'></a>

## 3. Results

We constructed an ODE model with a limited set of equations (see Methods section) and fitted it separately to experimental data obtained for two influenza A H1N1 viral strains,

<a id='99f718a7-1269-4bb4-929f-0ee6a01b96c9'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='4f917079-ada4-459e-b704-19b5f2c80bab'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='cbf0d7af-42a2-41e9-bfbc-24f84bea20b1'></a>

Fribourg et al.

<a id='477f8658-adf5-40c0-9983-48342a3cdda2'></a>

Page 10

<a id='f82e2ecf-162b-4d9d-b9a5-92b739086e8a'></a>

Cal/09 and NC/99. The experimental methods are described in Appendix B. Gene
expression levels were measured for IFN̢, IFN̥, TNF̥, STAT1 (STAT) and IRF7, and the
corresponding amounts were computed with the model. The resulting parameter values of
the model (see Table 1) allowed us to compare the action of viral antagonism for the two
strains.

<a id='5c0dde83-89d2-4bc0-b835-3201f8eaf253'></a>

After virus entry into the cell, antagonism to the induction of IFNβ, the initiator of the cellular antiviral response, is first to manifest itself, when the viral NS1 protein attempts to prevent virus detection by the cell's sensor (i.e. RIG-I), and disrupt the activation of transcription factors that lead to IFNβ induction. This antagonism is described in the model by factor IC1 (expression (14), and Figure 5). Once transcribed from the viral gene, the NS1 protein acts to inhibit mRNA nuclear production. It does so for NC/99, but not for Cal/09. This antagonism is represented in the model by factor IC2 (expression (15) and Figure 5). The succession in time of the two antagonisms for NC/99 is implemented in the model by choosing different thresholds of NS1 protein concentration at which the corresponding antagonism becomes effective. The two threshold factors control the point in time when NS1 protein concentration (see expression (16)) reaches a level where the viral antagonism embodied in factors IC1 and IC2, shown in Figure 5, starts inhibiting gene induction. In the model the threshold is smaller for IFNβ induction antagonism (factor IC1) than for mRNA processing antagonism (δ1 = 0.1 µM in (14) for IC1, δ2 = 0.4 µM in (15) for IC2; see Figure 5 and Table).

<a id='613f6579-fc98-4628-aa62-75c21c4b7d11'></a>

The temporal behavior of IC1 and IC2, with the corresponding parameter values, is given in Figure 5 for infections by NC/99 and Cal/09. For IFNβ and TNFα, gene expression levels depend on the product IC1*IC2 (equations (1) and (9)), shown as well in Figure 5 for NC/99 (for Cal/09, IC1*IC2=IC1 as noted in section 2.3.). The shape of IC1*IC2 in Figure 5 illustrates the fact that for NC/99 infection viral antagonism reaches its maximum strength in a short time scale, shown by a sharp drop at about 3.5 hours and determined by IC1. In contrast, for Cal/09 infection viral antagonism acts on a much longer time scale than for NC/99, as indicated by a decrease of IC1 between early and late times that is much slower in comparison. Beyond 4 hours the level of viral inhibition, measured by the smallness of IC1*IC2, is also much higher for NC/99 than for Cal/09 infection.

<a id='3742e489-5d6a-4475-832a-7919ec251c21'></a>

Clearly the time scales that characterize the inhibitory behavior of IC1, IC2 and IC1*IC2, are closely associated with the location in time of the peak of IFN̘ expression for NC/99 infection and of the plateau for Cal/09 infection. Thus, the time of about 3.5 hours at which NS1 antagonism of IFN̘ starts being fully expressed for NC/99 infection (see Figure 5), coincides with the time of peak IFN̘ expression. It must however be noted that the measured temporal shapes of genes (see in particular IFN̘ and TNF̘) are not determined only by the time scales associated with NS1 antagonism, though this antagonism is essential to break the initial rise of gene induction. Other factors in the model that influence gene expression levels over the time period considered are the gene half-life, and at very early times, the rate of gene production. For IFN̘ and TNF̘ genes the values of the model parameters that enter IC1 and IC2 are the same for infection by NC/99 or by Cal/09. NS1 antagonism, embodied in the product IC1*IC2, acts thus with the same strength and over the identical time scale for both infections. Therefore the difference in temporal behavior

<a id='d92ae448-85d4-4109-8f26-dde226206adc'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='93a5c25a-bf5d-45d9-afd9-1147a392406a'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='67bbcd14-29f7-4b1d-a699-fa580f97adf7'></a>

Fribourg et al.

<a id='1210c9c4-3592-4023-9ab1-f7f2147d86a3'></a>

Page 11

<a id='532e28eb-490a-4c73-9586-2bb96d533b5a'></a>

observed for the two genes is mainly due to the difference in their production rates, with the production rate of TNFα (_r_1 in (9)) close to an order of magnitude smaller that of IFNβ (_r_0 in (1)) (see Table 1).

<a id='fa100290-9f49-442d-bb2a-0815bcc89b23'></a>

The model simulations of experimental data (Figures 6) lead to the following insights for viral infection by pandemic Cal/09 and seasonal NC/99, and for the comparison of their respective antagonisms of the innate immune response.

<a id='82034a5f-9c2e-4c3d-abd5-7ab5cff62015'></a>

## 3.1. Cal/09 infection shows mild IFNβ induction antagonism

The comparison of the data (symbols) for IFNβ, IFNα, TNFα, STAT1, and IRF7 mRNAs with a model simulation (continuous line) is shown in Figure 6. The simulation provides a reasonable fit to the data, except perhaps for IFNα for which however the data are noisy with low expression levels relative to control (data not shown). The ISGs, STAT1 and IRF7, are fully expressed since NS1 lacks the CPSF binding and mRNA nuclear export antagonism. The experimental data for these two genes have been adjusted, as described in section 2.5., in order to eliminate the contribution to their expression level from uninfected cells. The leveling-off after four hours of IFNβ, and TNFα, whose shapes are similar, reflects the impact of NS1 antagonism of the interferon induction pathway. This antagonism is relatively weak and delayed in time with a maximum reached beyond 4 hours after infection (see Figure 5), a result consistent with the slow and late rise of Cal/09 NS1 mRNA (see Figure 4) when compared to that of NC/99. The strength of the antagonism, as manifested by the function IC1 (expression (14)), is four times greater for NC/99 than for Cal/09 (Figure 6).

<a id='aca6c1da-2599-4bc5-ada2-2bebbd981940'></a>

**3.2. NC/99 infection shows strong antagonism of both IFNβ induction and nuclear mRNA**
What is striking in the results for NC/99 for both IFNβ and TNFα (see Figure 6) is the very strong early induction starting at 2 hours, combined with a rapid decrease after 3 hours. This behavior of IFNβ induction, reflects the early contest—within one to two hours after infection—between on one hand detection of viral entry by the cell, and on the other hand production of the viral antagonistic protein NS1.

<a id='02977a7d-8da3-4d03-bb12-6094c98526dc'></a>

The other important result in Figure 6 is the low level of STAT1 and IRF7 for NC/99 when compared with Cal/09, particularly at late time points. The experimental data for these two genes have been adjusted, as described in section 2.5., in order to eliminate the contribution to their expression level from uninfected cells. The peak seen at 4.5 hours in the model simulation is associated with the "turning-on" of the inhibition carried by IC2 (see Figure 5). The simulation results lie above the experimental points at later times, an effect which may be influenced by the approximate subtraction of the contribution from uninfected cells as we have described above (Methods section). Clearly, mRNA export inhibition is strong in infected cells, leading to reduced levels of cytoplasmic mRNA. One infers that the ISG experimental expression levels shown in Figure 3 are dominated by the contribution from uninfected cells.

<a id='ad0f6881-d570-4a8d-81a9-0469904d72f0'></a>

The equality in our simulations of the values of IFNΒ for the two viruses close to 8 hours is
a result of higher early production of IFNΒ and faster viral antagonism for NC/99 leading to

<a id='defd0b25-d505-4148-bb69-dbc4396e8e25'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='b2ac6f52-3604-4920-a8b7-02bdacbb5282'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='260f06e6-bd3b-4043-885c-8c9dea84dc1d'></a>

Fribourg et al.

<a id='47e49840-ffa5-4c97-87cf-7869c27c3ca9'></a>

Page 12

<a id='9bc5b0b7-14d3-4337-984e-6adbd037bff3'></a>

the same level of IFNΒ as for Cal/09, where early production is lower and antagonism weaker. If further experiments were to confirm that beyond eight hours after infection IFNΒ expression levels follow nearly equal plateaus, our model, which does not show this feature, would need to be extended to take into account additional processes that contribute to gene regulation.

<a id='84369b47-3b31-4bcc-b884-ea5a8415584e'></a>

### 3.3. Interferon induction antagonism is stronger for NC/99 than for Cal/09
Antagonism of IFN̢ induction for NC/99 is much stronger than for Cal/09, because the maximum strength of that antagonism is larger and is reached sooner for NC/99 (see Figure 5, and compare the values of in Table 1 of parameters _sp_ that controls the strength, and _n1_ that controls the steepness of the increase in equation (14) ). A level of 50% of antagonistic effect by the NS1 protein is achieved shortly after 3 hours after infection for NC/99 infection, and about 1.5h later for Cal/09 (see Figure 5).

<a id='2ca23672-336a-4800-a26e-d7ecb65a8832'></a>

## 4. Discussion

We have proposed an ODE model that extracts what we believe are the principal features of the early time contest between cellular innate immune response in human dendritic cells and viral NS1 protein antagonism after infection by two influenza A H1N1 viruses, pandemic Cal/09 and seasonal NC/99. Our results show that Cal/09, which lacks mRNA nuclear antagonism, exhibits weak IFN̢ induction antagonism, whereas NC/99 has both strong IFN̢ induction antagonism and mRNA nuclear antagonism. We have proposed a phenomenological way to characterize viral antagonism (equations (14) and (15)) that allows us to put these results on a quantitative footing, through the parameter values that determine rates of gene induction and the strength of NS1 antagonism and time scales over which it acts.

<a id='c64fc5a9-69e0-40f9-8901-12958ca39e62'></a>

The model also gives general insight into the two main features of early viral NS1 antagonism, namely antagonism of both interferon induction and interferon signaling processes. For the first process, it takes expression levels of IFNβ as representative, for the second one, those of IRF7 (see Figure 6). The temporal behavior of these genes differs greatly between the two viruses. An inspection—informed by the model results—of those two shapes provides hints for a general characterization of viral antagonism and early immune response in dendritic cells. The interferon levels show a strong correlation between early production, which is the cell's immune response, and NS1 antagonism and its characteristic time and strength. The earlier NS1 antagonizes IFNβ production, the earlier the maximum or flattening of IFNβ expression. Thus, from the results in Figure 6, NS1 antagonism occurs over a faster time scale and more strongly for NC/99 than Cal/09. In the model, the two main NS1 antagonisms act multiplicatively in the interferon induction pathway, but not so for ISGs in the Jak/Stat pathway where only the mRNA export inhibition matters. Here the distinction in the experimental measurements between the contributions of infected and uninfected cells is crucial, since only in the former mRNA export inhibition operates. One can predict that if for infected cells expression levels of ISGs are low—if they can be extracted from the data, or the data is obtained at such high MOI that the number of uninfected cells is small—the relevant virus has weak CPSF binding and nuclear export blockage of mRNA.

<a id='27efdd44-7d93-47f7-8b12-84d342319fff'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='6a638304-48a4-4784-826d-f921feeb54a7'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='441f2244-913d-4d1f-8f80-7fb352bb24cd'></a>

Fribourg et al.

<a id='82e7f6ec-666a-4459-bbe4-c9967436c5bc'></a>

Page 13

<a id='bce82357-db2c-4739-b645-1a38a9687b10'></a>

Our model incorporates a number of simplifications. We have taken the IRF7 gene expression as a representative of a large class of genes induced by the same transcription factor after Jak/Stat pathway activation. We model the cellular processes of influenza A infection, with emphasis on what is believed to be the main weapon of influenza A viral antagonism, namely the viral NS1 protein. NS1 mediates its antagonism predominantly through the disruption on one hand of the IFNẞ induction pathway, and on the other hand of cytoplasmic mRNA accumulation. These antagonistic activities stand as summaries of a number of different mechanistic processes that underlie them [3, 4]. We do not consider other forms of NS1 antagonism, such as its inhibition of elongation initiation factor [25], or its role in apoptosis [26]. By introducing these simplifications, one avoids the introduction in the model of many unknown parameters unconstrained by experimental results. The model organization relies on the assumption that the two NS1 protein antagonisms considered act only at the gene production level, while gene degradation rates (or equivalently half-lives) remain unaffected with their values fixed at biologically reasonable levels. Although virus infection can lead to increased mRNA degradation [2], the corresponding processes, involving antiviral proteins whose fuction can also be antagonized by NS1, are not part of the simple model presented here.

<a id='43c05952-8f9a-4d25-b7f2-78d5c67668c4'></a>

As future work, one could envisage the decomposition of the immune response to viral intrusion into different segments, the development of separate models for each segment as more detailed experimental observations become available, and the subsequent agglomeration of the separate segments into a complete description. Such a decomposition would most certainly include—as we have done here—one segment concerning IFNΒ induction after viral infection, and a second one about induction in the Jak/Stat pathway of interferon stimulated genes, that would consider separately the contributions of infected and uninfected cells.

<a id='c6e071c1-f2b5-42e2-af9a-49e964bd6e36'></a>

In summary, our modeling effort has highlighted the role of the time course of IFNB induction as a sensitive indicator of the contest between its early production following virus entry detection and NS1 antagonism, clarifying the time scales involved, and also the role of IRF7 (or a similar ISG) in revealing the strength of nuclear mRNA inhibition. The mathematical approach is useful, although limited to a small number of genes, because we believe, as we have argued, that it encapsulates typical behavior of many more genes than occur in the equations. This approach could be potentially used to establish a classification of influenza H1N1 viruses in terms of the dynamics associated with NS1 antagonism.

<a id='61a22625-2ccd-4936-87e8-5228a705604c'></a>

## Acknowledgments

We thank Richard Cadagan for technical assistance. We also thank Yongchao Ge and Maria Chikina for helpful discussions. This work was supported by contract HHSN272201000054C from NIAID.

<a id='215d9581-4670-491b-8bbb-6949ebcf986d'></a>

**References**

<a id='5a87b74a-bce3-407e-b842-3360c768175b'></a>

1. Talon J, Salvatore M, O'Neill RE, Nakaya Y, Zheng H, Muster T, Garcia-Sastre A, Palese P. Influenza A and B viruses expressing altered NS1 proteins: A vaccine approach. Proc Nat Acad Sciences. 2000; 97:4309-4314.
2. Garcia-Sastre A. Induction and evasion of type I interferon responses by influenza viruses. Virus Res. 201110.1016/j.virusres.2011.10.017

<a id='88371096-d358-4395-b935-f5eac3f8f671'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='0378ed57-9111-4ac4-b06e-9c1cfa28d287'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='9e20a3c5-8f91-4f89-ae25-463abcc7c4eb'></a>

Fribourg et al.

<a id='69ac2367-66e8-4fe6-af8c-69e2cd19b7b8'></a>

Page 14

<a id='b56e620e-c2b4-42df-9532-14cd6bfc0575'></a>

3. Hale BG, Albrecht RA, Garcia-Sastre A. Innate immune evasion strategies of influenza viruses. Future Microbiol. 2010; 5:23.10.2217/fmb.09.108 [PubMed: 20020828]
4. Randall RE, Goodbourn ST. Interferon and viruses: An interplay between induction, signalling, antiviral responses and viral countermeasures. J Gen Virol. 2008; 89:1–47. [PubMed: 18089727]
5. Kochs G, Garcia-Sastre A, Martinez-Sobrido L. Multiple anti-interferon actions of the influenza A virus NS1 protein. J Virol. 2007; 81:7011–7021. [PubMed: 17442719]
6. Haye K, Bourmakina S, Moran T, Garcia-Satre A, Fernandez-Sesma A. The NS1 protein of a human influenza virus inhibits type I interferon production and the induction of antiviral responses in primary human dendritic and respiratory epithelial cells. J Virol. 2009; 83(13):6849–6862. [PubMed: 19403682]
7. Hale BG, Randall RE, Ortin J, Jackson D. The multifunctional NS1 protein of influenza A viruses. J Gen Virol. 2008; 89:2359–2376. [PubMed: 18796704]
8. Hayman A, Comely S, Lackenby A, Murphy S, McCauley J, Goodbourn S, Barclay W. Variation in the ability of human influenza A viruses to induce and inhibit the IFNB pathway. Virology. 2006; 347:52–64. [PubMed: 16378631]
9. Fernandez-Sesma A, Marukian BJ, Ebersole S, Kaminski D, Park MS, Yuen T, Sealfon SC, Garcia-Sastre A, Moran TM. Influenza virus evades innate and adaptive immunity via the NS1 protein. J Virol. 2006; 80:6295–6304. [PubMed: 16775317]
10. Nemeroff ME, Barabino M, Li Y, Keller W, Krug RM. Influenza virus NS1 protein interacts with the cellular 30 kDa subunit of CPSF and inhibits 3' end formation of cellular pre-mRNA. Mol Cell. 1998; 1:991–1000. [PubMed: 9651582]
11. Noah DL, Twu KY, Krug RM. Cellular antiviral responses against influenza A virus are countered at the posttranscriptional level by the viral NS1A protein via its binding to a cellular protein required for the 3' end processing of cellular pre-mRNAs. Virol. 2003; 307:386–395.
12. Satterly N, Tsai PL, VanDeursen J, Nussenzveig DR, Wang Y, Faria PA, Levay A, Levy DE, Fontoura BMA. Influenza virus targets the mRNA export machinery and the nuclear pore complex. Proc Nat Acad Sciences. 2007; 104:1853–1858.
13. Hale BG, Steel J, Medina RA, Manicassamy B, Ye J, Hickman D, Hai R, Schmolke M, Lowen AC, Perez DR, Garcia-Sastre A. Inefficient control of host gene expression by the 2009 pandemic H1N1 influenza A virus NS1 protein. J Virol. 2010; 84:6909–6922. [PubMed: 20444891]
14. Qiao L, Phipps-Yonas H, Hartmann B, Moran TM, Sealfon SC, Hayot F. Immune response modeling of interferon beta pretreated influenza virus-infected human dendritic cells. Biophys J. 2010; 98:505–514. [PubMed: 20159146]
15. Seto J, Qiao L, Guenzel C, Xiao S, Shaw ML, Hayot F, Sealfon SC. Novel Nipah virus immune-antagonism strategy revealed by experimental and computational study. J of Virology. 2010; 84(21):10965–10973. [PubMed: 20739535]
16. Rodriguez JJ, Parisien JP, Horvath CM. Nipah virus V protein evades alpha and gamma interferons by preventing STAT1 and STAT2 activation and nuclear accumulation. J Virol. 2002; 76:11476–11483. [PubMed: 12388709]
17. Shaw ML, Garcia-Sastre A, Palese P, Basler CF. Nipah virus V and W proteins have a common STAT1 binding domain yet inhibit STAT1 activation from the cytoplasmic and nuclear compartments, respectively. J Virol. 2004; 78:5633–5641. [PubMed: 15140960]
18. Pauli EK, Schmolke M, Wolff T, Viemann D, Roth J, Bode JG, Ludwig S. Influenza A virus inhibits type I IFN signaling via NfkB-dependent induction of SOCS-3 expression. PloS Path. 2008; 4(1):e1000196.
19. Yarilina A, Park-Min KH, Antoniv T, Hu X, Ivashkiv LB. TNF activates an IRF1-dependent autocrine loop leading to sustained expression of chemokinesand STAT1-dependent type I interferon-response genes. Nat Immunol. 2008; 9(4):378–387. [PubMed: 18345002]
20. Hasan M, Koch J, Rakheja D, Pattnaik AK, Brugarolas J, Dozmorov I, Levine B, Wakeland EK, Lee-Kirsch MA, Yan N. Trex1 regulates lysosomal bio-genesis and interferon-independent activation of antiviral genes. Nat Immunol 2013. 2012 Jan; 14(1):61–71.10.1038/ni.2475
21. Marie I, Durbin JE, Levy DE. Differential viral induction of distinct interferon-alpha genes by positive feedback through interferon regulatory factor-7. EMBO J. 1998; 17:6660–6669. [PubMed: 9822609]

<a id='6edc268b-4b0f-4fc5-9784-d152c1802ebb'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='095583a9-cdd0-40e4-9ab1-857826c1fd65'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='d658ce97-0926-4cb0-8b03-32aaa283c151'></a>

Fribourg et al.

<a id='7239a78d-e0c5-4f0f-b45a-f2b8e3228193'></a>

Page 15

<a id='df616ac1-2e4a-43c5-af63-7798a5ca256f'></a>

22. Phipps-Yonas H, Seto J, Sealfon SC, Moran TM, Fernandez-Sesma A. Interferon ß pretreatment of
conventional and plasmacytoid human dendritic cells enhances their activation by influenza virus.
PloS Pathogens. 2008; 4(10):e1000193. [PubMed: 18974865]
23. Multi-objective Optimization using Evolutionary Algorithms. John Wiley & Sons; 2001.
24. Bender A, Albert M, Reddy A, Feldman M, Sauter B, Kaplan G, Hellman W, Bhardway N. The
distinctive features of influenza virus infection of dendritic cells. Immunobiol. 1998; 198(5):552-
567.
25. Katze MG, Krug RM. Translational control in influenza virus-infected cells. Enzyme. 1990;
44:265-277. [PubMed: 2133654]
26. Herold S, Ludwig S, Pleschka S, Wolff T. Apoptosis signaling in influenza virus propagation,
innate host response, and lung injury. J Leuk Biol. 2012; 92:75-82.
27. Borderia AV, Hartmann BM, Fernandez-Sesma A, Moran TM, Sealfon SC. Antiviral-activated
dendritic cells: a paracrine-induced response state. J Immunology. 2008; 181(10):6872-81.
[PubMed: 18981106]
28. Hartmann BM, Li W, Jia J, Patil S, Marjanovic N, Martinez-Romero C, Albrecht RA, Hayot F,
Garcia-Sastre A, Wetmur JG, Moran TM, Sealfon SC. Mouse Dendritic Cell (DC) Influenza Virus
Infectivity Is Much Lower than That for Human DCs and Is Hemagglutinin Subtype Dependent. J
G Virol. 201310.1128/JVI.0.02980-12

<a id='95ff7914-793b-45e6-a65e-2e10398c16b6'></a>

## Appendix A

Using IFNβ and IRF7 gene expression levels as representatives of respectively the interferon induction and the interferon signaling pathway, we study their sensitivity to NS1 antagonism parameters *sp*, δ₁ in IC1 (interferon induction antagonism given by expression (14)) and *sv*, δ₂ in IC2 (cytoplasmic mRNA inhibition given by expression (15)). The parameters *sp* and *sv* describe the strength of NS1 antagonism, while the parameters δ₁ and δ₂ describe the thresholds of NS1 concentrations, which, since the latter depend on time, determine the time scale over which the antagonism acts. From the variations in time of IC1 and IC2 in Figure 5, it is clear that from early to late times the strength of antagonism changes significantly, and the time scale over which this change takes place is characteristic of virus and type of antagonism. One should therefore expect that parameter sensitivity can be large, and that this sensitivity is more or less depending on the time development of gene expression. A consequence is that, overall, the parameters that define NS1 antagonism are well constrained by the experimental time course measurements.

<a id='98524e85-1a52-4bc0-8008-abed01876e15'></a>

We compute, using a finite difference approximation, the normalized sensitivity to small changes in the $j^{th}$ parameter of the temporal behavior of the $i^{th}$ gene in our ODE model, using the formula

<a id='4359d3a2-93b4-458c-a042-9634fef3048b'></a>

S_ij(t) = p_j / y_i(t, p_j) * δy_i(t, p_j) / δp_j (A.1)

<a id='b6f4bee6-a501-4d32-a39e-e6f04fc141e2'></a>

where p_j is one of the parameters considered, and y_i(t,p_j) stands for the expression of gene i of our ODE model at time point t, which depends on the value of parameter p_j. It is necessary to consider time-dependent sensitivities since we are modeling early time, time-varying behavior. The results (Figures A.1 and A.2) show that in most cases sensitivities increase from early to late times. For IFNβm and NC/99 infection (Figure A.1, left panel), the most striking aspect is the precipitous increase of δ_1 sensitivity at 3 hours with a

<a id='c8fcde77-db73-4ec3-a41c-da3fcab9a55b'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='d063a085-6ce0-4bd6-bb44-98765eae59ae'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='cdf4b034-c226-40aa-84ff-d180ad8a47b7'></a>

Fribourg et al.

<a id='28502362-b287-441e-a0ec-2b0d0f791769'></a>

Page 16

<a id='c9e792e3-794b-49b6-a62c-505d6fe30832'></a>

maximum close to 4 hours, which reflects the predominant role played in IFNβm production by the threshold value in IC1. In contrast sensitivities to the two parameters in IC2 occur later and are lower. For IFNβm and Cal/09 (Figure A.2, left panel) sensitivity to sp is strong at late times, reflecting the impact at later times of IFNβ induction antagonism. As to IRF7m, sensitivity to IC2 parameters for NC/99 (Figure A.1, right panel) is strong. Its dominant feature is high sensitivity to δ2 which peaks at 5 hours for NC/99 infection, which is the time when mRNA antagonism starts inhibiting expression of interferon stimulated genes. For IRF7m and Cal/09 (Figure A.2, right panel), for which there is no dependence on the parameters of IC2, sensitivity dependence on both sp and δ1 is weak.

<a id='53763616-0fb5-4f2d-92c6-920a32d646ab'></a>

# Appendix B
## Experimental Methods
### B.1. Differentiation of Dendritic Cells

<a id='c2482ee2-1c1a-412c-9baa-e19432221a7a'></a>

All human research protocols for this work have been reviewed and approved by the IRB of the Icahn School of Medicine at Mount Sinai. Monocyte-derived dendritic cells (DCs) were obtained from two anonymous healthy human blood donors as described before [27].
Briefly, human peripheral blood mononuclear cells were isolated from buffy coats by Ficoll density gradient centrifugation and positive immunomagnetic purification for CD14+ cells followed by a 5 day incubation with 500 U/ml hGM-CSF (Preprotech, Rocky Hill NJ) and 1000 U/ml hIL-4 (Preprotech, Rocky Hill NJ). The parameters of the model presented correspond to one donor. Similar results and parameters were obtained for the second donor (data not shown).

<a id='34d7767e-24f8-478a-bf2b-d5dd82691e85'></a>

## B.2. Viral Infection

DCs from donors were infected in triplicate with the influenza strains A/California/04/09, A/New Caledonia/20/1999, or allantoic fluid for 20 minutes in RPMI medium at 37C. In order to achieve comparable levels of infectivity, titers for each viral strain were determined in DCs at 8h post-infection by an anti-NP (Influenza A nuclear protein) mouse monoclonal antibody (ab20921; Abcam) conjugated to the FITC fluorophore. After infection, cells were centrifuged to remove the viral inoculation media, and resuspended in culture medium. Samples were fixed with RNAprotect Cell Reagent (Qiagen, Valencia, CA) at 0 (control), 2, 2.4, 3.2, 4, 5, 6, 7, and 8 hours post-infection.

<a id='30f77789-bae1-483d-9eca-858b88a85c1c'></a>

## B.3. Gene Expression Measurements
For viral genes, RNA expression was quantified using quantitative RT-PCR. CDNA was synthesized from total RNA using AffinityScript MultiTemp RT (Agilent Santa Clara CA) with an oligo(dT)18 primer. Real-time PCR was performed using PlatinumTaq DNA polymerase (Invitrogen. Carlsbad CA) and SYBR-green (Invitrogen. Carlsbad CA) on an ABI7900HT thermal cycler (Applied Biosystems, Foster City CA). A robust global normalization algorithm, using expression levels of the housekeeping genes ribosomal protein S11 (*rps11*), β-actin (*actb*), and α-tubulin (*tuba*), was used for all experiments, as described elsewhere [27]. In brief, all crossing threshold (Ct) values were first adjusted by median difference of all samples from *actb*. Each individual sample was then further

<a id='60171d73-0bdd-4da3-8eff-c22ce1e63795'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='41c7dbdf-6dd7-46c5-92a5-976b374948e1'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='cadcda57-ab26-4a7f-80e3-43aafb52877d'></a>

Fribourg et al.

<a id='09b339d7-19cf-41d9-82f7-a4203f6e8322'></a>

Page 17

<a id='e8f3af55-333b-47b0-8573-8a0070696d0b'></a>

corrected by the median Ct value of the three corrected housekeeping control for that sample. Finally, nominal copy numbers were calculated by assuming 2500 molecules of _actb_ mRNA per cell, and an amplification efficiency of 93% using the difference in Ct value (ΔCt method). PCR primer sequences for viral NS1 used are GGTGATGCCCCATTCCTTGA for the sense and GGCATGAGCATGAACCAGTC for the antisense.

<a id='9fbf19ea-f62e-4673-9fbc-fe5aee7ea2d6'></a>

Levels of expression of other genes were measured as follows. Total RNA from samples was isolated using Rneasy Plus Micro Kit Qiagen, Valencia, CA) or a Rneasy 96 BioRobot 8000 Kit with on-column DNAse treatment Qiagen, Valencia, CA), according to the manufacturers protocol. RNA was quantified using a ND-1000 spectrophotometer (NanoDrop, Wilmington DE). The RNA integrity of all samples was confirmed using an Agilent Bioanalyzer 2100 (Agilent Santa Clara CA), according to the manufacturers protocol. Gene expression analysis was performed utilizing the human HT-12 v4

<a id='5293effe-0171-4ed9-904e-9e4cbaa5ed14'></a>

Expression BeadChip arrays (Illumina San Diego CA). A control for infectivity levels for each virus was achieved via staining of the viral nuclear protein NP as previously described [28]. Assays were processed at the Yale Center for Genome Analysis; the subset of genes of interest were assayed using the Illumina iScan (Illumina San Diego CA), and data for gene expression obtained.

<a id='58a63812-60df-4a64-8103-eec2f4da668b'></a>

B.4. Signal Processing

Data was first quantile-normalized to their luminosity value for each probe. Since multiple
probes are available for each gene, we measured the quality of the signal associated to each
gene by calculating the signal to noise ratio (SNR) in dBs as follows,

<a id='2087b33d-4b75-4bd0-a0de-fd6c5f82f603'></a>

S = (1/N) * sum_{n=1}^{N} g[n]^2 (17)

A = (1/N) * sum_{n=1}^{N} a[n]^2 (18)

SNR = 10log (S/A) (19)

<a id='91b69076-d0c7-4379-8a8c-9fc367dafa17'></a>

where g[n] is the sequence including the luminosity values for all time points for a specific gene and for all 3 replicates, a[n] is the sequence including the luminosity values for all time points for the allantoic fluid for all 3 replicates, N is the total number of samples for that gene sequence, S is the average signal power for a particular gene, and A is the noise for that gene as determined by the power of the allantoic fluid signal.

<a id='2c21b0e3-d670-488b-8e10-6ef9aaf76e53'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='5ba607d2-1374-499d-93cf-ec41cab22c06'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='b0cd183e-0cc9-498a-98d4-49ba21d5cb0f'></a>

Fribourg et al.

<a id='3ef9782f-42c1-4250-8bb8-f74cd0054b17'></a>

Page 18

<a id='d0dbce00-5e98-452d-a3b9-00c69acdbd55'></a>

* We study two influenza A H1N1 viral strains with different clinical outcomes
* We model the dynamics of the interplay between viral antagonism and the innate immune response.
* We extract the dynamic features of viral antagonism and innate immune response from time course gene expression measurements for a set of selected genes.
* We find that the strength and time scale of action of viral antagonism is significantly different between the two viruses.

<a id='19145a2b-675e-4584-bf3a-33ad51afd768'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='199e3d12-fcd6-4595-9204-fe530fbc91ca'></a>

NIH-PA Author Manuscript NIH-PA Author Manuscript NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='61fe06fa-8b7e-4079-8b80-2b48804e0a89'></a>

Fribourg et al.

<a id='e09e2949-cb01-4bea-af2e-c10a178306d3'></a>

Page 19

<a id='a5b6db58-94ef-469c-a9d5-42d518a08a87'></a>

<::Line chart showing IFNβ Gene Expression (a.u.) on the y-axis versus Time (hours post-infection) on the x-axis. The y-axis ranges from 0 to 3000, and the x-axis ranges from 0 to 10 hours. Four data series are presented:
- NC/99: Represented by a solid black line with filled black circles, showing a rapid increase in IFNβ gene expression, peaking around 3 hours post-infection at approximately 2300 a.u., then gradually decreasing.
- Cal/09: Represented by a dotted black line with filled black squares, showing an increase in IFNβ gene expression, peaking around 4-5 hours post-infection at approximately 1200 a.u., with levels consistently lower than NC/99.
- Allantoic Fluid: Represented by a solid grey line with filled grey circles, showing consistently low, near-zero IFNβ gene expression throughout the observed time.
- Control: Represented by an open circle at the origin (0 hours post-infection, 0 IFNβ gene expression), serving as a baseline.
: chart::>

<a id='eb0d4b92-48ec-4f68-acb8-32a3405c8383'></a>

Figure 1.
Experimental gene expression levels for IFNβ in cells infected by NC/99 (●), and Cal/09 (■) as a function of time. For visual clarity, linear segments are drawn connecting the data points. Allantoic fluid (gray line) provides the negative control. A control at 0h (○) is also depicted.

<a id='ad1c40fb-edc6-48de-8e8e-0fdd9392f702'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='0488399e-1abc-4ab8-92b7-54724570937f'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='c7e8d72e-674b-4b90-9ed5-c29f52e26207'></a>

Fribourg et al.

<a id='dad3fbcc-8b14-43fb-b11b-92ad3e0ab793'></a>

Page 20

<a id='39076a94-7008-4eea-b838-216cf4e7627d'></a>

<::Schematic diagram of a cellular signaling model. The diagram shows three main compartments: Medium (top, external to the cell), Cytoplasm (middle section), and Nucleus (bottom section). Arrows indicate activation or movement, while blunt-ended lines indicate inhibition. Dotted circles highlight points of NS1 antagonism. The right side of the diagram is labeled "Cytoplasm" and "Nucleus".  External signals and their interactions are shown at the top (Medium compartment): - TNF-α binds to TNFR. - Virus interacts with a Viral Sensor. - IFN-α and IFN-β bind to IFNAR. In the Cytoplasm: - From Virus: Viral Sensor leads to IRF7, which then leads to IRF7P. NS1 inhibits the Viral Sensor. - From IFN-α/IFN-β: IFNAR activates Tyk2/JAK1*, which is inhibited by PTPs and SOCS. Tyk2/JAK1* activates STAT, which then becomes STATP, and further forms STATP(2) (a dimer). NS1 inhibits Tyk2/JAK1*. - NS1 is shown to inhibit the TNF-α binding to TNFR (indicated by a dotted circle around NS1 near TNFR). In the Nucleus: - IRF7P from the cytoplasm enters the nucleus and activates the transcription of IFN-α and IFN-β. NS1 inhibits the transcription of IFN-α and IFN-β (indicated by a dotted circle around NS1 near the IFN-α/IFN-β gene region). - STATP(2) from the cytoplasm enters the nucleus and activates the transcription of IRF7, STAT, and SOCS. PTPsn (nuclear PTPs) inhibits the activation of these genes by STATP(2). NS1 inhibits PTPsn and also inhibits the transcription of IRF7, STAT, and SOCS (indicated by dotted circles around NS1 near these gene regions). - NS1 also inhibits the transcription of TNF-α (indicated by a dotted circle around NS1 near the TNF-α gene region). Feedback loops are shown: - IFN-α and IFN-β produced in the nucleus are exported to the medium and can bind to IFNAR. - TNF-α produced in the nucleus is exported to the medium and can bind to TNFR.  Figure 2. Schematic of the model considered, where the points of application of NS1 antagonism are highlighted. There are three compartments, medium, cytoplasm and nucleus, and positive feedback loops associated with IFNβ, IFNα, and TNFα.::>

<a id='e749c51d-be15-4c2f-bf59-b2bc9d7d2359'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='5b17e75c-b4a7-4d71-8855-d49a184f6516'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='3a47beae-aa82-46bb-9310-013fabff4b55'></a>

Fribourg et al.

<a id='035aeb96-1da8-4e8b-b348-b2a67aa81f69'></a>

Page 21

<a id='5cdefa3e-0454-4de6-b8ee-c7214809f1ad'></a>

<::chart:Six line graphs, arranged in two rows of three, display experimental gene expression levels. Each graph plots 'Gene Expression (a.u.)' on the y-axis against 'Time (hours post-infection)' on the x-axis, ranging from 0 to 8 or 10 hours. The top row shows data for IRF7, MX1, and DDX58. The bottom row shows data for OAS1, OAS2, and EIF2AK2. A legend, visible in the DDX58 graph, applies to all plots: NC/99 is represented by black circles connected by a solid line; Cal/09 is represented by black squares connected by a dashed line; Allantoic Fluid (negative control) is shown as a gray line; and a Control at 0h is depicted by an open circle. Linear segments connect the data points. Figure 3. Experimental gene expression levels for IRF7, MX1, DDX58, OAS1, OAS2, and EIF2AK2 in cells infected by NC/99 (●), and Cal/09 (■) as a function of time. For visual clarity, linear segments are drawn connecting the data points. Allantoic fluid (gray line) provides the negative control. A control at 0h (○) is also depicted.::>

<a id='e2761ed2-0058-4388-b391-c714ca8d2e66'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='ae06fc38-9324-47dd-9582-6cf957a8001c'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='9407464b-bc04-494e-b619-83533cbbdb03'></a>

Fribourg et al.

<a id='fb2d085b-f875-4b35-a51b-fb1698f6f12e'></a>

Page 22

<a id='83883382-985a-4ac0-9e5c-c0a8136884fb'></a>

<::Line graph titled "NS1 mRNA copy number" on the y-axis (ranging from 0 to 50000) versus "Time (hours post-infection)" on the x-axis (ranging from 0 to 8). The graph displays three data series:
1. "NC/99": Represented by a solid black line with circular markers, showing a rapid increase in NS1 mRNA copy number from approximately 4 hours, peaking at around 41000 at 7 hours, then slightly decreasing to about 28000 at 8 hours. Error bars are visible.
2. "Cal/09": Represented by a dotted black line with square markers, showing a more gradual increase in NS1 mRNA copy number starting around 5 hours, reaching approximately 17000 at 8 hours. Error bars are visible.
3. "Allantoic Fluid": Represented by a solid gray line with circular markers, consistently showing a very low (near zero) NS1 mRNA copy number across all time points from 0 to 8 hours.::>

<a id='c4dd985d-694c-418c-aae6-35e2b64dd654'></a>

Figure 4.
RT-PCR measurements of NS1 mRNA expression levels as a function of time after infection by NC/99 (●), and Cal/09 (■).
Allantoic fluid (gray line) serves as a negative control.

<a id='0801744b-a2e0-45ec-ac9c-2fe51e1032cf'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='f5ed24ad-7883-42b6-8b39-0a6b5e3f2341'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='0ad2d702-1a74-402d-af20-c5bb4052536a'></a>

Fribourg et al.

<a id='a69b5da0-bc7c-490d-9b76-857a2dc976e2'></a>

Page 23

<a id='381178ce-6318-47f5-884a-4892f699d55c'></a>

<::Two line graphs titled "Cal/09" and "NC/99" show "Antagonist Factor" on the y-axis (ranging from 0 to 1.0) against "Time (hours post-infection)" on the x-axis (ranging from 0 to 8).

**Top Graph: Cal/09**
- The graph shows a single curve labeled "IC1" (solid gray line).
- The curve starts at an Antagonist Factor of 1.0, remains at 1.0 until approximately 2 hours, then gradually decreases, reaching an Antagonist Factor of about 0.4 by 8 hours.

**Bottom Graph: NC/99**
- The graph shows three curves:
  - "IC1" (solid gray line): Starts at an Antagonist Factor of 1.0, remains at 1.0 until approximately 3 hours, then sharply drops to near 0.1 by 4 hours, and remains low.
  - "IC2" (dashed gray line): Starts at an Antagonist Factor of 1.0, remains at 1.0 until approximately 3.5 hours, then sharply drops to near 0.1 by 5 hours, and remains low.
  - "IC1 * IC2" (solid black line): Starts at an Antagonist Factor of 1.0, remains at 1.0 until approximately 3 hours, then sharply drops to near 0 by 4 hours, and remains very close to 0.

Figure 5.: chart::>

<a id='8e7e47e4-b060-4d9c-98ba-78121f9c699f'></a>

Figure 5.
NS1 protein antagonistic effect as a function of time for Cal/09 (top) and NC/99 (bottom). The solid gray line represents IC1 (IFNβ induction antagonism) and the dashed gray line represents IC2 (nuclear mRNA antagonism). Their expressions are
IC1=[1+sp (NS/δ₁)^n1^]/[1+(NS/δ₁)^n1^] with parameter values sp=0.3, δ₁=0.1 μM, n1=1 for Cal/09 and sp=0.1, δ₁=0.1 μM, n1=5 for NC/99, and IC2=[1+sv (NS/δ₂)^n2^]/[1+(NS/δ₂)^n2^] with parameter values sv=0.1, δ₂=0.4 μM, n2=5 for NC/99 and IC2=1 for Cal/09 since there is no nuclear mRNA antagonism. The product IC1*IC2 for NC/99 is also shown (solid black line). The time dependence of the curves is due to the time-varying amount of NS1 protein (expression (16)) in the expressions for IC1 and IC2 given above. The smaller IC1 and IC2, the stronger the antagonism, since both terms multiply production terms in the model equations.

<a id='cc6f9f02-1f2f-439d-8d9a-edaba4f240dc'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='f7c0d62d-e809-4bcf-927d-075f301fc26f'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='14dd5320-f031-49e5-922d-4cfbc42f2ff0'></a>

Fribourg et al.

<a id='672ac503-17e4-4810-a325-bc278a8cd97d'></a>

Page 24

<a id='cbc0050c-1dd1-4cf2-a035-ac46501dbdd7'></a>

<::chart: The image contains five line graphs, arranged in a 2x3 grid (three graphs in the top row, two in the bottom row), collectively labeled as Figure 6. Each graph displays 'Time (hours post-infection)' on the x-axis, ranging from 2 to 8 hours, and mRNA expression levels on the y-axis, scaled from 0 to 3. The legend in the top right indicates that experimental data for NC/99 is represented by solid lines with circular symbols (●) and for Cal/09 by dashed lines with square symbols (■). Error bars are present on the data points. The individual graphs are: 1. Top-left graph: 'IFNβm' mRNA levels. The NC/99 data (solid line, circles) shows a peak around 3.5-4 hours and then declines. The Cal/09 data (dashed line, squares) shows a gradual increase and then plateaus. Two vertical dashed lines are present, labeled 'IC1' (around 3.5 hours) and 'IC2' (around 4.5 hours). 2. Top-middle graph: 'IFNαm' mRNA levels. The NC/99 data shows a continuous increase and then plateaus, while the Cal/09 data shows a slower, more gradual increase. 3. Top-right graph: 'TNFαm' mRNA levels. The NC/99 data peaks around 3.5-4 hours and then declines. The Cal/09 data shows a slower, more gradual increase and decrease. 4. Bottom-left graph: 'STATm' mRNA levels. The NC/99 data remains consistently low, while the Cal/09 data shows a steady, almost linear increase over time. 5. Bottom-right graph: 'IRF7m' mRNA levels. Similar to STATm, the NC/99 data remains low, while the Cal/09 data shows a steady increase over time. Figure 6. Comparison of experimental data (symbols) and model simulations (lines) for infection with NC/99 (●, 3 replicates, solid lines) or Cal/09 (■, 3 replicates, dashed lines) for IFNβ, IFNα, TNFα, STAT1 (STAT), and IRF7 mRNAs as a function of time after infection. The time at which IFNβ induction antagonism (IC1) and nuclear mRNA antagonism (IC2) reach their respective midpoint in strength also indicated. The data for IRF7 and STAT1 represent the contributions from infected cells only, obtained from the experimental measurements as explained in section 2.5. The data, in each figure, are normalized by the corresponding 8 hr time point expression level for Cal/09.::>

<a id='14171c8f-ff18-4c5e-9a98-86b9a49b7263'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='c40c4aa8-2a68-4370-b767-6d894c535058'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='6ab1ea04-ec98-4f0b-9ca1-eb61464a28ed'></a>

Fribourg et al.

<a id='85ea89da-0922-4e22-a924-15425724bba0'></a>

Page 25

<a id='641de554-df05-40a5-b693-e70cd1f5d867'></a>

<::figure: chart::> Figure A.1. The figure displays two line charts, side-by-side, illustrating the time behavior of normalized parameter sensitivity. Both charts have an x-axis labeled "t (hr)" ranging from 2 to 8. The y-axis for both charts is labeled "Norm. Sens." and ranges from 0.0 to 1.0. A common legend for both charts indicates four parameters: "sp" (solid line), "δ1" (dotted line), "sv" (dashed line), and "δ2" (dash-dotted line). The left chart's y-axis is specifically labeled "Norm. Sens. IFNβm". In this chart, the "δ1" curve shows an initial rise, peaking around 0.35 between 3.5 and 4 hours, then gradually decreasing to about 0.3 at 8 hours. The "sp", "sv", and "δ2" curves all start near 0 and show a slow, gradual increase, remaining below 0.15 throughout the observed time. The right chart's y-axis is specifically labeled "Norm. Sens. IRF7m". In this chart, the "δ1" curve rises sharply, reaching a peak of approximately 0.95 around 5.5 hours, then declines to about 0.4 at 8 hours. The "sv" curve shows a steady increase, reaching approximately 0.55 at 8 hours. The "sp" and "δ2" curves remain low, gradually increasing to values below 0.1 at 8 hours. NC/99 infection: time behavior of normalized parameter sensitivity of NS1 antagonism for IFNβm and IRF7m. Parameters are sp, sv, δ1, and δ2, which characterize NS1 antagonism (see expressions (14) and (15) of IC1 and IC2, and Figure 5). <::

<a id='13f7a479-f1df-4017-818f-a9c2a75544ec'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='4669018e-28bc-4dbc-9bba-c96a5ba8cd4a'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='80c848cd-3e23-4cbe-a082-85d5f41c5d23'></a>

Fribourg et al.

<a id='be342bb3-61e1-4db8-9c98-223395b827b3'></a>

Page 26

<a id='506f67e6-b860-4b04-91e2-f3eeec3dc15c'></a>

<::chart: The visual content displays two line charts side-by-side, illustrating the time behavior of normalized parameter sensitivity for NS1 antagonism. Both charts share the same x-axis, labeled "t (hr)", ranging from 2 to 8 hours. The legends for both charts indicate two parameters: "sp" represented by a solid line and "δ1" represented by a dotted line. The y-axis on the left chart is labeled "Norm. Sens. IFNβm" and ranges from 0.00 to 0.50. The solid line (sp) shows a continuous increase, while the dotted line (δ1) increases initially and then plateaus around 0.20-0.21 after 6 hours. The y-axis on the right chart is labeled "Norm. Sens. IRF7m" and ranges from 0.00 to 0.06. The solid line (sp) shows a gradual increase, starting around 0.025 and ending around 0.053. The dotted line (δ1) starts around 0.01 and increases more sharply than the solid line, reaching around 0.052 at 8 hours.Figure A.2. Cal/09 infection: time behavior of normalized parameter sensitivity of NS1 antagonism for IFNβm and IRF7m. Parameters are sp and δ1, which characterize NS1 antagonism (see expression (14) of IC1). For Cal/09, there is no dependence on parameters sv, and δ2 since IC2=1.::>

<a id='20b080a7-f0f3-4673-88bd-7b681fb5bb9d'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='67014375-1bd8-40b2-b8bb-61e0a6ad2382'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<!-- PAGE BREAK -->

<a id='f5ecd9e3-27b8-40fd-b242-1b89c8984e5a'></a>

NIH-PA Author Manuscript

<a id='20f689ba-1db8-4fe4-b66c-17133b72e929'></a>

NIH-PA Author Manuscript

<a id='771cda9e-0ddb-4424-a0ed-795202fa77da'></a>

NIH-PA Author Manuscript

<a id='e4fff9b2-894b-486e-b1a6-558fa4a5e434'></a>

Table 1

<a id='77bc86a5-bb01-4c1b-8fee-85fe76802069'></a>

Model Parameters
List of parameter values for each process described in the model for the different viral strains: Cal/09, and NC/99. Estimated parameters are in black, parameters fitted to the experimental data are in red. Our estimates of parameter values are taken from [15], where they are obtained from the literature or biological considerations, and to which we refer for details. The exceptions are our estimates for parameters _V_max2, _V_max19, and _r_20, which are relevant to secreted proteins: their values are obtained in [15] from the model fits. The value of _s_v for NC/99 is 0.1 for all genes except for IFN_&alpha;_ for which it takes a value of 0.3.

<a id='92619656-0be3-49ea-aaf3-270a28cfd54c'></a>

<table id="26-1">
<tr><td id="26-2" rowspan="2">Process</td><td id="26-3" rowspan="2">Parameter</td><td id="26-4" colspan="2">Value</td><td id="26-5" rowspan="2">Units</td><td id="26-6" rowspan="2">Remarks</td></tr>
<tr><td id="26-7">Cal/09</td><td id="26-8">NC/99</td></tr>
<tr><td id="26-9" rowspan="2">IFNb mRNA induction</td><td id="26-a">r₀</td><td id="26-b">1×10⁻³</td><td id="26-c">3×10⁻³</td><td id="26-d">mM.h⁻¹</td><td id="26-e">Fitted</td></tr>
<tr><td id="26-f">k₁₅</td><td id="26-g" colspan="2">3600×10-8</td><td id="26-h">h⁻¹</td><td id="26-i">Estimated</td></tr>
<tr><td id="26-j">IFNb mRNA degradation</td><td id="26-k">t₁</td><td id="26-l" colspan="2">2.5</td><td id="26-m">h</td><td id="26-n">Estimated</td></tr>
<tr><td id="26-o" rowspan="2">IFNb/a translation and secretion</td><td id="26-p">Vmax2/17</td><td id="26-q" colspan="2">20.1x3600</td><td id="26-r">molecules.h¹.cell¹</td><td id="26-s">Estimated</td></tr>
<tr><td id="26-t">K2/17</td><td id="26-u" colspan="2">2×10⁻³</td><td id="26-v">mM</td><td id="26-w">Estimated</td></tr>
<tr><td id="26-x"></td><td id="26-y">TJtot</td><td id="26-z" colspan="2">1×10⁻⁴</td><td id="26-A">mM</td><td id="26-B">Estimated</td></tr>
<tr><td id="26-C"></td><td id="26-D">K3</td><td id="26-E">4.3×10-3</td><td id="26-F">4.3×10-3</td><td id="26-G">mM</td><td id="26-H">Fitted</td></tr>
<tr><td id="26-I">[1]</td><td id="26-J">d</td><td id="26-K" colspan="2">3×10⁻⁴</td><td id="26-L">mM</td><td id="26-M">Estimated</td></tr>
<tr><td id="26-N"></td><td id="26-O">K9</td><td id="26-P" colspan="2">7.8×10²</td><td id="26-Q">--</td><td id="26-R">Estimated</td></tr>
<tr><td id="26-S" rowspan="2">Formation of STATP2n</td><td id="26-T">K5</td><td id="26-U" colspan="2">3600</td><td id="26-V">h-¹</td><td id="26-W">Estimated</td></tr>
<tr><td id="26-X">K5</td><td id="26-Y" colspan="2">1×10⁻²</td><td id="26-Z">mM</td><td id="26-10">Estimated</td></tr>
<tr><td id="26-11">STATP2n dephosphorylation</td><td id="26-12">13</td><td id="26-13" colspan="2">0.56</td><td id="26-14">h</td><td id="26-15">Estimated</td></tr>
<tr><td id="26-16"></td><td id="26-17">13</td><td id="26-18" colspan="2">1×10⁻⁷</td><td id="26-19">mM.h-1</td><td id="26-1a">Estimated</td></tr>
<tr><td id="26-1b">SOCS mRNA Induction</td><td id="26-1c">k₈</td><td id="26-1d" colspan="2">3600×10-6</td><td id="26-1e">h⁻¹</td><td id="26-1f">Estimated</td></tr>
<tr><td id="26-1g">SOCS mRNA degradation</td><td id="26-1h">t₄</td><td id="26-1i" colspan="2">0.46</td><td id="26-1j">h</td><td id="26-1k">Estimated</td></tr>
<tr><td id="26-1l"></td><td id="26-1m">k₁₁</td><td id="26-1n">3600×10⁻⁷</td><td id="26-1o">3600×10⁻⁷</td><td id="26-1p">h⁻¹</td><td id="26-1q">Fitted</td></tr>
<tr><td id="26-1r">IRF7 mRNA induction</td><td id="26-1s">k₁₄</td><td id="26-1t" colspan="2">3600x8.9x10-11</td><td id="26-1u">h⁻¹</td><td id="26-1v">Estimated</td></tr>
<tr><td id="26-1w">IRF7mRNA degradation</td><td id="26-1x">t₆</td><td id="26-1y"></td><td id="26-1z"></td><td id="26-1A">h</td><td id="26-1B">Estimated</td></tr>
<tr><td id="26-1C">IRF7 translation</td><td id="26-1D">K12</td><td id="26-1E">3600×0.1</td><td id="26-1F">3600x1</td><td id="26-1G">h-1</td><td id="26-1H">Fitted</td></tr>
<tr><td id="26-1I">IFNa mRNA induction</td><td id="26-1J">K16</td><td id="26-1K">3600×10-4</td><td id="26-1L">3600×2×10-4</td><td id="26-1M">h-1</td><td id="26-1N">Fitted</td></tr>
<tr><td id="26-1O">IFNa mRNA degradation</td><td id="26-1P">18</td><td id="26-1Q" colspan="2">2</td><td id="26-1R">h</td><td id="26-1S">Estimated</td></tr>
</table>

<a id='73d38095-613c-4f8e-bcc7-ce3e92b787e7'></a>

Page 27

<a id='264600e2-861c-4c08-93c6-6c9d74ba89c7'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.

<a id='d1ef7cb4-6cd1-4661-bc38-88d37bd6a0d4'></a>

Fribourg et al.

<!-- PAGE BREAK -->

<a id='c3ccbf19-72a8-4024-91ba-f5582938bffd'></a>

NIH-PA Author Manuscript
NIH-PA Author Manuscript
NIH-PA Author Manuscript

<a id='d399e809-782c-40d0-92a6-ed0a80ce3c81'></a>

<table id="27-1">
<tr><td id="27-2" rowspan="2">Process</td><td id="27-3" rowspan="2">Parameter</td><td id="27-4" colspan="2">Value</td><td id="27-5" rowspan="2">Units</td><td id="27-6" rowspan="2">Remarks</td></tr>
<tr><td id="27-7">Cal/09</td><td id="27-8">NC/99</td></tr>
<tr><td id="27-9">TNFa mRNA induction</td><td id="27-a">r₁</td><td id="27-b">1×10⁻⁴</td><td id="27-c">2.5×10⁻⁴</td><td id="27-d">mM.h⁻¹</td><td id="27-e">Fitted</td></tr>
<tr><td id="27-f"></td><td id="27-g">r₂₀</td><td id="27-h"></td><td id="27-i">1×10⁻³</td><td id="27-j">mM.h⁻¹</td><td id="27-k">Estimated</td></tr>
<tr><td id="27-l"></td><td id="27-m">K₂₀</td><td id="27-n"></td><td id="27-o">6×10⁻⁴</td><td id="27-p">mM</td><td id="27-q">Estimated</td></tr>
<tr><td id="27-r">TNFa mRNA degradation</td><td id="27-s">t9</td><td id="27-t"></td><td id="27-u">2</td><td id="27-v">h</td><td id="27-w">Estimated</td></tr>
<tr><td id="27-x" rowspan="2">TNFa translation and secretion</td><td id="27-y">Vmax19</td><td id="27-z"></td><td id="27-A">16×3600</td><td id="27-B">molecules.h-¹.cell-1</td><td id="27-C">Estimated</td></tr>
<tr><td id="27-D">K19</td><td id="27-E"></td><td id="27-F">4x10-3</td><td id="27-G">mM</td><td id="27-H">Estimated</td></tr>
<tr><td id="27-I">STAT mRNA induction</td><td id="27-J">r4</td><td id="27-K"></td><td id="27-L">1×10-6</td><td id="27-M">mM.h-¹</td><td id="27-N">Estimated</td></tr>
<tr><td id="27-O"></td><td id="27-P">K26</td><td id="27-Q">3600×5×10</td><td id="27-R">-6 3600×5×10-6</td><td id="27-S">h-1</td><td id="27-T">Fitted</td></tr>
<tr><td id="27-U">STAT mRNA degradation</td><td id="27-V">t₁₂</td><td id="27-W"></td><td id="27-X">1</td><td id="27-Y">h</td><td id="27-Z">Estimated</td></tr>
<tr><td id="27-10">STAT translation</td><td id="27-11">k₂₈</td><td id="27-12">3</td><td id="27-13">600×10⁻¹</td><td id="27-14">h⁻¹</td><td id="27-15">Estimated</td></tr>
<tr><td id="27-16">STAT degradation</td><td id="27-17">t₁₃</td><td id="27-18"></td><td id="27-19">15</td><td id="27-1a">h</td><td id="27-1b">Estimated</td></tr>
<tr><td id="27-1c"></td><td id="27-1d">r₅</td><td id="27-1e"></td><td id="27-1f">1</td><td id="27-1g">mM</td><td id="27-1h">Estimated</td></tr>
<tr><td id="27-1i">NS1 Protein</td><td id="27-1j">n₃</td><td id="27-1k">5</td><td id="27-1l">8</td><td id="27-1m"></td><td id="27-1n">Estimated</td></tr>
<tr><td id="27-1o"></td><td id="27-1p">b_m</td><td id="27-1q">6</td><td id="27-1r">4.5</td><td id="27-1s">h</td><td id="27-1t">Estimated</td></tr>
<tr><td id="27-1u"></td><td id="27-1v">sp</td><td id="27-1w">0.3</td><td id="27-1x">0.1</td><td id="27-1y"></td><td id="27-1z">Fitted</td></tr>
<tr><td id="27-1A">IFNb induction antagonism (IC1)</td><td id="27-1B">d_1</td><td id="27-1C">0.1</td><td id="27-1D">0.1</td><td id="27-1E">mM</td><td id="27-1F">Fitted</td></tr>
<tr><td id="27-1G"></td><td id="27-1H">n_1</td><td id="27-1I">1</td><td id="27-1J">5</td><td id="27-1K"></td><td id="27-1L">Fitted</td></tr>
<tr><td id="27-1M"></td><td id="27-1N">sv</td><td id="27-1O"></td><td id="27-1P">0.1/0.3</td><td id="27-1Q"></td><td id="27-1R">Fitted</td></tr>
<tr><td id="27-1S">nuclear mRNA antagonism (IC2)</td><td id="27-1T">d₂</td><td id="27-1U">- </td><td id="27-1V">0.4</td><td id="27-1W">mM</td><td id="27-1X">Fitted</td></tr>
<tr><td id="27-1Y"></td><td id="27-1Z">n₂</td><td id="27-20">-</td><td id="27-21">5</td><td id="27-22">- </td><td id="27-23">Fitted</td></tr>
</table>

<a id='f5efdb55-65c8-4b2d-bf12-82a448732d4b'></a>

Fribourg et al.

<a id='716d9025-473a-43ce-84fe-33b5a0e70597'></a>

Page 28

<a id='4eba8e71-5729-49c2-8e4e-e405a9194bbe'></a>

J Theor Biol. Author manuscript; available in PMC 2015 June 21.