<a id='fcc3461d-74ea-4586-9f7e-c70703a6ef6b'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe surrounded by dots, followed by the text "PLOS" and "ONE" separated by a vertical line, all in black on a white background.::>

<a id='f9e74f63-9828-4bef-87d5-52338feb7722'></a>

RESEARCH ARTICLE

Modeling the Mechanisms by Which HIV-
Associated Immunosuppression Influences
HPV Persistence at the Oral Mucosa

<a id='a119df2e-bfb9-4081-a452-e60794c8427e'></a>

Meghna Verma¹, Samantha Erwin², Vida Abedi¹, Raquel Hontecillas¹, Stefan Hoops¹,
Andrew Leber¹, Josep Bassaganya-Riera¹*, Stanca M. Ciupe²*
1 Nutritional Immunology and Molecular Medicine Laboratory, Biocomplexity Institute of Virginia Tech,
Blacksburg, VA, United States of America, 2 Department of Mathematics, Virginia Tech, Blacksburg, VA,
United States of America

<a id='9721011b-8c36-4bac-bd64-b2a9a524a062'></a>

<::logo: [Unknown] Check for updates A colorful circular ribbon with a red bookmark icon is centered above the text "Check for updates" on a gray rectangular button.::>

<a id='60efc5b5-c29a-49ac-8e45-752ed448c9c6'></a>

OPEN ACCESS
Citation: Verma M, Erwin S, Abedi V, Hontecillas R,
Hoops S, Leber A, et al. (2017) Modeling the
Mechanisms by Which HIV-Associated
Immunosuppression Influences HPV Persistence
at the Oral Mucosa. PLoS ONE 12(1): e0168133.
doi:10.1371/journal.pone.0168133

<a id='2afde698-755c-4c53-bf5e-57bdb76f7e50'></a>

**Editor:** Guido Poli, Universita Vita Salute San Raffaele, ITALY

<a id='78aa59fc-611a-401a-9c23-a0d0ebbdbc36'></a>

Received: May 3, 2016
Accepted: November 24, 2016

<a id='a5fb50ab-ebf4-4923-9dd8-2f2325e88e47'></a>

Published: January 6, 2017

<a id='9a216f20-3bcf-44bb-a0b6-cda3e39f94f3'></a>

**Copyright:**  2017 Verma et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

<a id='808baa37-9fca-46a8-be63-82a46844ad41'></a>

Data Availability Statement: The complete SBML compliant model was deposited in www.biomodels.net and assigned the identifier MODEL 1605030001. All the other relevant data are within the paper and its Supporting Information files.

<a id='66c2a112-84c6-47d6-a5b2-c51b5c0e3fc4'></a>

**Funding:** The study was supported by the funds from the Nutritional Immunology and Molecular Medicine Laboratory (www.nimml.org).

<a id='fe76f85a-b327-43f0-9768-b2c5f7ab3b44'></a>

**Competing Interests:** The authors have declared that no competing interests exist.

<a id='25bad4e7-d318-4d4d-866e-2ec8e2b4e809'></a>

☯ These authors contributed equally to this work.
* jbassaga@vt.edu (JBR); stanca@math.vt.edu (SC)

<a id='312d72a6-3eab-4313-809c-5870e9c077fe'></a>

Abstract
Human immunodeficiency virus (HIV)-infected patients are at an increased risk of co-infection with human papilloma virus (HPV), and subsequent malignancies such as oral cancer. To determine the role of HIV-associated immune suppression on HPV persistence and pathogenesis, and to investigate the mechanisms underlying the modulation of HPV infection and oral cancer by HIV, we developed a mathematical model of HIV/HPV co-infection. Our model captures known immunological and molecular features such as impaired HPV-specific effector T helper 1 (Th1) cell responses, and enhanced HPV infection due to HIV. We used the model to determine HPV prognosis in the presence of HIV infection, and identified conditions under which HIV infection alters HPV persistence in the oral mucosa system. The model predicts that conditions leading to HPV persistence during HIV/HPV co-infection are the permissive immune environment created by HIV and molecular interactions between the two viruses. The model also determines when HPV infection continues to persist in the short run in a co-infected patient undergoing antiretroviral therapy. Lastly, the model predicts that, under efficacious antiretroviral treatment, HPV infections will decrease in the long run due to the restoration of CD4+ T cell numbers and protective immune responses.

<a id='fba1eb3a-b525-40ee-97a4-c079af51311b'></a>

# Introduction
Infection with the human immunodeficiency virus (HIV) afflicts over 35 million people world-
wide and results in impaired immune responses which may affect defenses against other
pathogens. In the absence of protective vaccines, current management of HIV consists of
administration of combination antiretroviral therapy (cART)—which suppresses viral replica-
tion and, consequently, drastically reduces morbidity and mortality [1, 2]. cARTs are 99%
effective; however, antiviral drug resistance (mainly caused by non-compliance) against some
of the anti-HIV drugs has been reported in up to 60% of the patients [3]. Moreover, a cure for

<a id='64e17d4c-f662-42fc-93ae-d8cf34bd79fd'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='1976e899-5c81-4688-8714-5a0f0c48d699'></a>

1/20

<!-- PAGE BREAK -->

<a id='741e66a1-3a25-41bc-b0b3-0807301b19ca'></a>

<::PLOS | ONE logo with a stylized globe icon: figure::>

<a id='e3c743ca-307a-4cf2-a0e5-21f4606a78fc'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='22eef2e3-a0f5-447a-aae3-b403a59f8502'></a>

HIV is challenging due to the strict need for lifelong treatment to avoid virus rebound from activation of latent reservoirs.

<a id='46c93991-4bc0-4547-a943-ec03ae9ae69b'></a>

Apart from the acquired immunodeficiency syndrome (AIDS), HIV increases the risk of developing opportunistic infections by other infectious agents, including viruses: papillomavirus, herpesviruses, flaviviruses; and bacteria: _Helicobacter pylori_, _Salmonella typhimurium_, _Chlamydophila pneumonia_ [4]. Epidemiological data suggests that HIV patients have an increased risk for developing human papillomavirus (HPV)-induced cancers such as oropharyngeal cancer, cervical cancer, anogenital cancer and anal cancers [5-10]. However, the cellular and molecular mechanisms explaining the correlation between increased susceptibility of HPV-associated diseases and HIV-induced immune suppression remain largely unknown.

<a id='424ee543-ea00-42ba-b409-0b0010f82efe'></a>

The oropharyngeal cancers are a subset of head and neck cancers (HNCs) which account for approximately 4% of all the cancers in the United States. The incidence of disease was twice as high in men than in women in 2015 [11]. The oropharyngeal cancers, in their clinically distinct form of squamous cell carcinoma, are commonly detected in HIV patients with a higher number of lifetime oral sexual partners, immunosuppression, smoking, and current tobacco use. The causal role of oral HPV infection is supported by substantial molecular and cellular evidence [5-7, 12].

<a id='3b6ff04d-d506-4556-9253-c30ef3dc3340'></a>

Recent studies suggested that the interaction between HIV and HPV might be responsible for the increased risk of cervical cancers [13, 14]. Similarities in risk factors for the acquisition of HIV and HPV infections, such as high-risk sexual behavior, multiple sexual partners, and disease-related immunosuppression makes the demarcation between the HPV and HIV-associated malignancies challenging. It has been hypothesized that HIV patients who have been infected for a long period of time have a higher prevalence of oral HPV infection and subsequently are at a higher risk for HPV-associated HNCs [15]. HIV-induced immunosuppression also increases the risk of HPV-associated cancer. Other factors that can increase the risk of severe HPV infections in HIV patients include immune senescence, aging, impaired immune response to HPV, and direct interaction between the two viruses [13, 14, 16]. The immunological changes caused by HIV create a permissive immune environment, thereby decreasing the overall immune responses against HPV. However, the mechanisms by which HIV-induced reduction in CD4+ T cell levels impairs the immune response against HPV or other pathogens remain largely unknown.

<a id='92c54dda-2a22-4337-8933-edad037b82fc'></a>

Besides immunological factors, interactions at the molecular level between HIV genes _tat_, _rev_ and _vpr_ and HPV have also been reported. Multiple studies indicate an up-regulation of HPV oncogenic genes (_E6_ and _E7_) expression by _tat_ [14, 17, 18]. _Tat_ increases HPV shedding which suggests that HIV infection may contribute to the pathogenesis of HPV-associated disease by molecular interactions through _tat_ [16].

<a id='416f9473-e8af-44f6-b6b6-8939a6b6f3e6'></a>

Currently, there are two commercially available HPV preventive vaccines, the quadrivalent human papillomavirus vaccine (QHPV) (Gardasil; Merck) against HPV types 6, 11, 16 and 18 and a bivalent vaccine (Cervarix, Glaxosmithkline) against HPV types 16 and 18. Both vaccines are known to be 98–100% effective against HPV types 16 and 18 [19]. Recent studies demonstrated the efficacy of the anti-HPV vaccine Cervarix in HIV-infected-oral-HPV-negative patients where more than 90% of patients produced high antibody titers against HPV [20]. However, more data is needed to address cross-reactivity between the induced antibody and other HPV strains [21]. Moreover, additional efficacy trials of QHPV in HIV infected individuals are needed to properly determine the correlation between vaccines dose, timing and protection against all HPV genotypes in immunocompromised HIV patients. The mechanistic investigation of co-infection scenario is experimentally challenging. The disadvantages of interrupted treatment of HIV and limited efficacy for the HPV vaccine against all the HPV strains further adds to the complexity. The limited clinical information about treatment and

<a id='0823c593-ac4e-4c71-ace5-cb9aa187704a'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='942bba49-81a7-4561-b7b8-3cb60e2d07d0'></a>

2/20

<!-- PAGE BREAK -->

<a id='665b5154-f3c8-46f9-b215-02548b2dcb02'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe icon surrounded by dots, with the text "PLOS" in bold, followed by a vertical line and "ONE" in a lighter font::>

<a id='cf2a61e8-2e82-4156-8df4-dfc936589943'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='8d5e888d-88bf-49b6-94b2-09e0c9a85d58'></a>

prevention options against HPV in an HIV/HPV co-infection has lead us to an alternative
mode of investigation.

<a id='bf0f1e06-b1a6-485b-9a7f-dd07a329784d'></a>

To gain new insights into the underlying mechanistic interactions between HIV and HPV, in an HIV/HPV co-infection we developed a mathematical model of HIV and HPV interactions. Building on previous models of HIV [22] and HPV [23] single infections, this novel model captures the molecular interactions between HIV and HPV due to _tat_ and the effect of progressive depletion of CD4+ T cell due to HIV infection. Using the model, we aim to investigate why the prevalence of oral HPV infection is increased in HIV-infected individuals. We demonstrate how the dynamics of HPV changes in an HIV/HPV co-infection when the patient undergoes combined antiretroviral therapy. The findings can be used to further advance our understanding of the mechanisms underlying oral immune plasticity. Lastly, modeling can help propose new hypotheses for reversing residual inflammation in individuals following the start of cART and guide clinical practice.

<a id='fbe560e8-e7bf-4af7-8ac3-d94ea221c9f6'></a>

# Methods
## Mathematical model of HIV infection
We model the interaction between HIV and CD4+ T cells as in [22, 24]. Briefly, we consider the interaction between three populations: i) target CD4+ T cells (T), ii) productively infected CD4+ T cells (I), and iii) HIV (V). Target cells are produced at rate s, die at rate d, and become productively infected at rate \u03b2 proportional to the interaction between target cells and the virus. Infected cells produce N\u2081 virions throughout their lifetime, which are released through bursting, and die at rate \u03b4. The virus is cleared at a rate c\u2081 per day. The following system of ordinary differential equations (ODE) represents these dynamics:

<a id='d23ec6cf-2c07-4151-b80b-9d43f0f1aec3'></a>

dT/dt = s - dT - βTV,
dI/dt = βTV - δI,
dV/dt = N₁δI - c₁V,
(1)

<a id='f1b0891c-1dc6-4d7b-aa6a-50bcc7dfe955'></a>

with initial conditions T(0) = To, I(0) = Io, and V(0) = Vo.
The effect of cART has been modeled as a reduction of the virus infectivity in the presence
of reverse transcriptase inhibitors to β (1- ε_RT) and a reduction in the production of infectious
virions in the presence of protease inhibitors to N_I(1- ε_PI). Here 0 ≤ ε_RT, ε_PI ≤ 1 are the drug
efficacies [24, 25].

<a id='9a7df522-5a75-4bb0-99b0-fd762c4ceca7'></a>

The model in the presence of cART becomes:

$\frac{dT}{dt} = s - dT - (1 - \epsilon_{RT})\beta TV,$

$\frac{dI}{dt} = (1 - \epsilon_{RT})\beta TV - \delta I,$

$\frac{dV}{dt} = (1 - \epsilon_{PI})N_1\delta I - c_1V,$
(2)

<a id='36437610-1a1c-4505-be39-b219c2880ec1'></a>

with initial conditions T(0) = T₁, I(0) = I₁, and V(0) = V₁. Note that models (1) and (2) do not take into account the HIV latent reservoirs in the form of resting long-lived memory CD4+ T cells with integrated HIV in their genome [26].

<a id='999e8709-cb9a-4e1a-89ad-ee96f534c119'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='a3e4c625-59ee-41f6-ac5f-7a83cecfc6fb'></a>

3/20

<!-- PAGE BREAK -->

<a id='a9413c8a-8f82-4aee-905f-c0b96cc59e3d'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe icon surrounded by dots, with the text "PLOS" in bold, followed by a vertical line and "ONE" in a lighter font::>

<a id='910d6f58-e889-40cb-a4ff-c81f352718e1'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='23c52d60-7e83-4586-9e8c-5d884c0ae46c'></a>

## Mathematical model of HPV infection

We model HPV in-host dynamics as in [23]. We consider the interaction between four populations: i) HPV infected basal epithelial cells (Y1), ii) the HPV infected transit-amplifying cells, in the suprabasal epithelial layer (Y2), iii) HPV (W) and iv) HPV-specific cytotoxic T lymphocytes (CTL) (E). We assume that N2 is the total concentration of epithelial cells at the beginning of HPV infection and the basal layer is formed of uninfected basal epithelial cells, targeted by HPV. Upon HPV infection, the basal epithelial cells become infected Y1 when HPV interacts with uninfected cells at rate ψ. We denote the difference N2 - Y1 as the concentration of uninfected epithelial cells. The basal infected cells, Y1 traverse up through the epithelial column and transform into Y2 cells, which move further into the suprabasal epithelial layer [27][28]. The Y2 cells become transit-amplifying cells which start assembling virions to be released at the surface [29, 30]. Therefore, both Y1 and Y2 cells are HPV infected cells but differentially located in the epithelial cell layer, wherein Y2 cells are assumed to have higher expression of the oncogenes E6 and E7 compared to Y1 [23]. For simplification, we assume that the uninfected cells and infected cells have an equal probability of interaction with the HPV virions irrespective of the spatial architecture of the tissue. A more generalized model which takes into account the infectivity and layer transition terms, or one which would consider spatial structures for epithelial cells in different layers requires extensive knowledge of numerous parameters, which are currently unknown. We assume that the infection is density dependent with φ representing the uninfected cell concentration where the infection is half-maximal. We assume that infected cell populations Y1 and Y2 differ in terms of the oncogene expression such that the Y2 (located in the suprabasal epithelial layer) have higher oncogene expression compared to Y1 cells (located in the basal epithelial layer) [31]. The rate of oncogene expression of the HPV type present in an infected cell, given by ε controls the conversion of Y1, into the transit-amplifying infected cells, Y2. Cells, Y2, grow at rate rε, proportional to their own density and die at rate μ. Due to higher expression of oncogenes, the transit-amplifying cells, Y2 divide more before death, compared to the basal infected cells Y1. Since, both infected cell population have an expression of oncogene, as in [23], both types of infected cells produce free virions (W), at production rates k1 and k2, that are released through bursting. For simplicity, we consider an equal virion production rate of k1 = k2 = k. The HPV virions are cleared at rate c2 [23]. The c2 clearance rate captures the antibody clearance rate implicitly.

<a id='f298e17a-16fd-4701-9ce9-a30ecb32ac78'></a>

The clearance of HPV in the infected cells, is associated with a successful immune response that includes the trigger of innate immune responses targeted against the virions released from the surface as well as infected cells [30]. In addition to the innate immune responses, the HPV-specific CTLs recruited during the adaptive immune response aid in the elimination of the infected basal cells [32]. Here, we assume that, after encountering transit-amplifying infected cells Y2, effector cells specific to HPV, E, expand with a maximum per capita rate w and carrying capacity K. This carrying capacity is an addition to the original work [23]. In the current model, the CTL response E is initiated only by Y2 cells which have higher oncogene E6 *expression* [33] [34] compared to Y1.

<a id='41ad2fea-540b-469c-adf3-dc34c2a35c2f'></a>

We disregard the differential CTL response against the infected cell populations and consider that HPV-specific CTL population _E_ kills both classes of infected cells at the same rate _a_, since both infected cells populations express oncogenes _E6_ and _E7_ [30][32]. Additionally, the model does not take into account the virus specific gene expression at any particular epithelial site. Finally, the functional differences in _E6_ and _E7_, which are major determinants of HPV pathogenicity between HPV types [35], are also neglected.

<a id='bc11aa85-950e-4bb0-b39e-bf26f898a82a'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='56444823-8a04-4415-a44b-57e4d2fe1444'></a>

4/20

<!-- PAGE BREAK -->

<a id='e7c3a5a8-417f-47d9-b860-a64454fe25b4'></a>

<::PLOS | ONE logo with a stylized globe icon: figure::>

<a id='e1f3780a-d1c6-4cc6-ae54-8fae2ebc4961'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='39139114-0bc9-4985-a8b6-39026014ae8c'></a>

The following system of differential equations represents these dynamics:

<a id='aa140855-c1d5-404e-a9c5-132bacbab635'></a>

dY₁/dt = ψW (N₂ - Y₁)/(φ + N₂ - Y₁) - εY₁ - μY₁ - aY₁E,
dY₂/dt = εY₁ + rεY₂ - μY₂ - aY₂E,
dW/dt = μk(Y₁ + Y₂) - c₂W,
dE/dt = ωY₂E(1 - E/K),
(3)

<a id='b73e1342-e1af-4651-a6a0-839d7fc6e99a'></a>

with initial conditions Y₁(0) = Y₁₀, Y₂(0) = Y₂₀, W(0) = W₀ and E(0) = E₀.

<a id='9db5872d-45f5-4afd-a766-fa6fa9872b17'></a>

## Co-infection Model

**The effect of _tat_ protein.** HIV-protein _tat_, secreted from HIV-infected intraepithelial immune cells, is known to play an important role in the disruption of epithelial tight junctions, thereby facilitating the entry of HPV into the mucosal epithelium [36]. We model the _tat_-induced increased likelihood of HPV infection through increasing the total available epithelial cells from N₂ to N₂ (1+pV), where (_p_) is the effect of _tat_ protein secreted by an HIV virion (_V_), given in Eq (4). The term (1+pV) incorporates the HIV-associated epithelial disruption as one of the major underlying mechanisms that increases the susceptibility of epithelial cells to the HIV/HPV co-infection [36].

<a id='753ae1e9-45ea-42e9-a0d5-b5c090959b4d'></a>

$$\frac{dY_1}{dt} = \psi W \frac{(1 + pV)N_2 - Y_1}{\varphi + (1 + pV)N_2 - Y_1} - \varepsilon Y_1 - \mu Y_1 - aY_1E. \quad (4)$$

<a id='53d2acbf-0e2f-4697-bda5-5c95345e9839'></a>

**The effect of immunosuppression.** In HIV-infected individuals, the loss of CD4+ T cells leads to consecutive loss of CD4+ T cell-mediated immune responses against other pathogens such as HPV. Naïve CD4+ T cells are depleted in mucosal tissues in all the stages of HIV infec- tion [26, 37], and progressive decline of CD4+ T cells affects the differentiation process of naïve CD4+ T cells into the different subsets. Such a subset, Th1, is known to play a major role in immune responses against HPV [34] through induction of cell-mediated immunity in the presence of IL-2, IL-12 and IFN-γ cytokines [38].

<a id='a441d90c-9b4e-454e-b6e1-a021dad1cde3'></a>

To model the decrease in the availability of CD4+ T cell population due to HIV; and the subsequent effect of such loss on HPV-specific CTL (E) responses, we assume that the carrying capacity of the E population decreases in an immunosuppressed patient. In particular, we represent K as the carrying capacity of CTLs and thus the maximum E population. We make K a function of CD4+ T cell population, such that K is given by, K = K(T) = bT, where T are the uninfected CD4+ T cells in the model (1). When T decreases during the progressive loss of CD4+ T cells, T, K(T), the maximum carrying capacity decreases at a linear rate. We assume that the CTL carrying capacity is directly proportional to the amount of CD4+ T cells. Other modeling options, such as a T dependent source with a death term were explored, however the maximum proliferation term K(T) best explained the homeostatic mechanistic behavior of the CTLs.

<a id='188ba62c-a465-491a-9b07-593029e75db7'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='d8694137-a96c-453a-a415-424f315937eb'></a>

5/20

<!-- PAGE BREAK -->

<a id='6fd203f7-fae3-4922-a456-4dd1c5a871e3'></a>

<::Logo for PLOS ONE, featuring a stylized globe icon with radiating dots to the left of "PLOS", separated by a vertical line from "ONE": figure::>

<a id='3975a159-087b-41ac-a7c1-f11feffe9393'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='ebf0abea-caba-4c89-8378-536029f5f3cc'></a>

<::flowchart: Diagram showing HIV and HPV dynamics. The diagram is split into two main sections by a vertical dashed line. A legend in the top right indicates:
- Death: [red arrow]
- Stimulation: [green arrow]
- Inhibition: [red bar]

**Left section: HIV dynamics**

1.  A bone symbol, labeled 's', points to 'CD4+ T cell (T)'.
2.  'CD4+ T cell (T)' has a red arrow, labeled 'd', pointing to 'Dead CD4+ T cell'.
3.  'CD4+ T cell (T)' has a green arrow, labeled 'β', pointing to 'Infected CD4+ T cell (I)'. This arrow is stimulated by 'HIV (V)'.
4.  'HIV (V)' has a red arrow, labeled 'c1', indicating death.
5.  'HIV (V)' has a red inhibition bar, labeled 'εPI', coming from 'PI'.
6.  The green arrow from 'CD4+ T cell (T)' to 'Infected CD4+ T cell (I)' has a red inhibition bar, labeled 'εRT', coming from 'RT'.
7.  'Infected CD4+ T cell (I)' has a red arrow, labeled 'δ', pointing to 'Dead infected CD4+ T cell'.
8.  'Infected CD4+ T cell (I)' has a green arrow, labeled 'N1', pointing to 'HIV (V)'.

**Right section: HPV dynamics**

1.  'Effector CD8+ T cells (E)' has a green arrow, labeled 'ω', pointing to itself, indicating self-stimulation or production related to the other cells.
2.  'Effector CD8+ T cells (E)' has a red arrow, labeled 'a', pointing to 'HPV Infected epithelial cells (Y1)' and 'HPV infected self-proliferating cells (Y2)', indicating inhibition.
3.  'HPV Infected epithelial cells (Y1)' has a green curved arrow, labeled 'ψ', pointing to itself, indicating self-proliferation.
4.  'HPV Infected epithelial cells (Y1)' has a red arrow, labeled 'μ', indicating death.
5.  'HPV Infected epithelial cells (Y1)' has a green arrow, labeled 'k', pointing to 'HPV (W)'.
6.  'HPV (W)' has a red arrow, labeled 'c2', indicating death.
7.  'HPV (W)' has a green arrow, labeled 'k', pointing to 'HPV infected self-proliferating cells (Y2)'.
8.  'HPV Infected epithelial cells (Y1)' has a gray arrow, labeled 'ε', pointing to 'HPV infected self-proliferating cells (Y2)'.
9.  'HPV infected self-proliferating cells (Y2)' has a green curved arrow, labeled 'rε', pointing to itself, indicating self-proliferation.
10. 'HPV infected self-proliferating cells (Y2)' has a red arrow, labeled 'μ', indicating death.::>

<a id='c9250831-e52d-4723-b2cb-c767fb7efc36'></a>

Fig 1. HIV HPV Diagram. A diagram for the co-infection model (5). The left side of the figure represents the HIV dynamics wherein the interaction between target CD4+ T cells (7), productively infected CD4+ T cells (1) and HIV (V) are shown. The figure also includes the effect of reverse transcriptase (RT) and protein inhibitor (PI) (shown by red line---inhibition). The right side of the figure represents the HPV dynamics wherein the interaction between infected basal cells (Y1), suprabasal transit-amplifying cells (Y2), HPV specific (E) cells and HPV (W) are shown. The systems biology markup language (SBML) compliant network of interactions between HIV (V) and HPV (W) is created using CellDesigner [40] (S1 Fig).

<a id='f075ab50-2a66-488e-806b-7dc54dadaaaf'></a>

doi:10.1371/journal.pone.0168133.g001

<a id='e47acdca-cf01-439f-abdc-51101daf6677'></a>

The co-infection model becomes (see Fig 1):

<a id='2ecbbdec-caf1-433a-a7c6-3713317a824b'></a>

dT/dt = s - dT - (1 - ε_RT)βTV,
dI/dt = (1 - ε_RT)βTV - δI,
dV/dt = (1 - ε_PI)N_1δI - c_1V,
dY_1/dt = ψW ((1 + pV)N_2 - Y_1) / (φ + (1 + pV)N_2 - Y_1) - εY_1 - μY_1 - aY_1E, (5)
dY_2/dt = εY_1 + rεY_2 - μY_2 - aY_2E
dW/dt = μk(Y_1 + Y_2) - c_2W,
dE/dt = ωY_2E (1 - E/K(T)),

<a id='470720b7-edf3-44a2-bf63-8b7321b3537d'></a>

with initial conditions $T(0) > 0$, $I(0) > 0$, $V(0) > 0$, $Y_1(0) = Y_{10}$, $Y_2(0) = Y_{20}$, $W(0) = W_0$ and $E(0) = E_0$ where $t = 0$ is the time of co-infection.

<a id='609e5e2e-6615-45c3-a617-ff976717aa05'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='cbde2eab-0e48-428f-b038-52b5efb2a8ea'></a>

6/20

<!-- PAGE BREAK -->

<a id='aa4e20ee-7dc0-45cd-ba83-5f262de903ea'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe icon surrounded by dots, with the text "PLOS" in bold, followed by a vertical line and "ONE" in a lighter font::>

<a id='31c4a0ae-f480-4be4-bf66-d6fc75d50c55'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='d0ee153a-2277-4e20-b875-64e183f7bc36'></a>

The complete SBML compliant model was deposited in BioModels [39] and assigned the identifier MODEL 1605030001.

<a id='7fe3e242-e3bd-49cf-bb04-77cd5538f193'></a>

# Results
## Analytical results
Analytically, we can find a necessary condition for the HPV infection to be cleared (data in S1 File). We assume that we have a chronically infected HIV subject who reached steady state values (T̄, Ī, V̄). Under these conditions, the carrying capacity for population E becomes K̄ = bT̄.
System (5) reduces to:

<a id='7ff6183c-fc7e-4002-9e67-77964068c59e'></a>

dY₁/dt = ψW ((1+p V̄)N₂ - Y₁) / (φ + (1+p V̄)N₂ - Y₁) - εY₁ - μY₁ - aY₁E,
dY₂/dt = εY₁ + rεY₂ - μY₂ - aY₂E,
dW/dt = μk(Y₁ + Y₂) - c₂W,
dE/dt = ωY₂E (1 - E/K).

(6)

<a id='e1f96ca0-0cef-4e5d-a35c-1a15e67c09e8'></a>

Then, HPV will clear when:
$$\frac{\psi\kappa\mu(1 + p \bar{V})N_2}{c_2(\varphi + (1+p\bar{V})N_2)} < \frac{(\varepsilon + \mu + aE)(-er + aE + \mu)}{(\varepsilon + \mu + aE - r\varepsilon)} \quad (7)$$


<a id='05e19d71-033c-4302-9b33-c7da49c93d4a'></a>

where _E_ is any CTL level (data in S1 File). Biologically, this means that when the product between HPV infection rate and the HPV production rate (in the presence of HIV) is less than the combined effect of effector cells and natural death rate of HPV, clearance of HPV will be observed.

<a id='8e535021-6d5d-4e69-bad3-6248d09b3b75'></a>

# Numerical results

Using the co-infection model (5), we numerically simulated disease scenarios in order to under-
stand the dynamics of HPV infection in a co-infected individual. A recent clinical trial has investi-
gated the effect of HIV in HPV infection in the presence and absence of combination antiretro-
viral therapy [41]. The levels of oral HPV DNA in the co-infected patients, which was monitored
for 24 weeks after the start of cART, remained elevated throughout therapy. To determine the pos-
sible mechanisms of HPV persistence, we investigate models (5) and (6) for the relative contribu-
tions of co-infection factors: tat, as given by pV, and immunosuppression as given by K(T).

<a id='69e33eff-7529-44c4-b3c8-5fcbd4371b4c'></a>

**Parameter values.** Parameter values from previously published studies are utilized here, as follows. Equilibrium values for HIV RNA per ml and HIV-specific uninfected CD4+ T cells per ml were reported in an HIV/HPV co-infection study to be V̅ = 4.8x10⁴ virions per ml and T̅= 3.3x10⁵ cells per ml [41]. Since the patient is in a chronic HIV steady state, we derive I̅, β and s from steady state conditions I̅ = (c₁V̅)/(N₁δ), β = c₁/(N₁T̅) and s = dT̅ + T̅V̅, to be I̅ = 2.4x10³ cells

<a id='c227dc0d-c29f-43a1-9981-ad4028bd9926'></a>

per ml, β = 1.5x10⁻⁷ ml per cells per day and s = 5.6x10³ cells per ml per day. The remaining parameters are summarized in Table 1.

<a id='f8dcc5b4-78ba-4e57-bea7-1ecbb2e9f08d'></a>

We assume that the _tat_-effect, given by p V, ranges between zero and 20, to account for up to a
20-fold increase in the target epithelial cell population due to co-infection. The immunosuppres-
sion factor, given by K(T) = bT ranges between K(T) = 35 cells and K(T) = 1 cell to account

<a id='cadcf5c2-6ce0-48c4-be8c-b86d3d74497f'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='2d16c161-533f-4f97-9390-f449a29adb30'></a>

7/20

<!-- PAGE BREAK -->

<a id='88a3b2eb-fc27-43a0-9492-13a7b36471ef'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe with radiating dots, followed by the word "PLOS" in bold, and "ONE" separated by a vertical line, all in black on a white background.::>

<a id='9bd3af93-ff79-4dd1-bf18-c3d5a12b3fe3'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='17d8f38b-b654-4621-9b87-a0bf92d34d49'></a>

Table 1. Parameters.
<table id="7-1">
<tr><td id="7-2">Parameter</td><td id="7-3">Value</td><td id="7-4">Description</td><td id="7-5">Reference</td></tr>
<tr><td id="7-6">s</td><td id="7-7">5.6 x 10³ cells ml⁻¹ day⁻¹</td><td id="7-8">CD4+ T cell recruitment rate</td><td id="7-9">See text</td></tr>
<tr><td id="7-a">β</td><td id="7-b">1.5 x 10⁻⁷ ml virions⁻¹ day⁻¹</td><td id="7-c">HIV infection rate</td><td id="7-d">See text</td></tr>
<tr><td id="7-e">d</td><td id="7-f">0.01 day⁻¹</td><td id="7-g">Uninfected CD4+ T cell death rate</td><td id="7-h">[42]</td></tr>
<tr><td id="7-i">δ</td><td id="7-j">1 day⁻¹</td><td id="7-k">Infected CD4+ T cells death rate</td><td id="7-l">[43, 44]</td></tr>
<tr><td id="7-m">N₁</td><td id="7-n">467 virions cells⁻¹</td><td id="7-o">HIV burst size</td><td id="7-p">[45]</td></tr>
<tr><td id="7-q">C₁</td><td id="7-r">23 day⁻¹</td><td id="7-s">HIV clearance rate</td><td id="7-t">[46]</td></tr>
<tr><td id="7-u">ERT</td><td id="7-v">varied</td><td id="7-w">Reverse transcriptase efficacy</td><td id="7-x">See text</td></tr>
<tr><td id="7-y">EρI</td><td id="7-z">varied</td><td id="7-A">Protease inhibitor efficacy</td><td id="7-B">See text</td></tr>
<tr><td id="7-C">T</td><td id="7-D">3.2 x 10⁵ cells ml⁻¹</td><td id="7-E">Uninfected CD4+ T cells at equilibrium</td><td id="7-F">[41]</td></tr>
<tr><td id="7-G">I</td><td id="7-H">2.4 x 10³ cells ml⁻¹</td><td id="7-I">Infected CD4+ T cells at equilibrium</td><td id="7-J">See text</td></tr>
<tr><td id="7-K">V</td><td id="7-L">4.8 x 10⁴ virions ml⁻¹</td><td id="7-M">HIV at equilibrium</td><td id="7-N">[41]</td></tr>
<tr><td id="7-O">N₂</td><td id="7-P">10⁴ cells</td><td id="7-Q">Total concentration of epithelial cells</td><td id="7-R">[23]</td></tr>
<tr><td id="7-S">φ</td><td id="7-T">10⁶ cells</td><td id="7-U">Epithelial cell concentration for which infection is half maximal</td><td id="7-V">[23]</td></tr>
<tr><td id="7-W">Ψ</td><td id="7-X">0.0067 cells virions⁻¹ day⁻¹</td><td id="7-Y">HPV infection rate</td><td id="7-Z">[23]</td></tr>
<tr><td id="7-10">μ</td><td id="7-11">0.048 day⁻¹</td><td id="7-12">Epithelial cell death rate</td><td id="7-13">[23]</td></tr>
<tr><td id="7-14">r</td><td id="7-15">0.1</td><td id="7-16">Transit-amplifying cells recruitment rate</td><td id="7-17">[23]</td></tr>
<tr><td id="7-18">ε</td><td id="7-19">varied</td><td id="7-1a">Oncogenic expression</td><td id="7-1b">See text</td></tr>
<tr><td id="7-1c">ω</td><td id="7-1d">10⁻³ cell⁻¹ day⁻¹</td><td id="7-1e">CTL expansion rate</td><td id="7-1f">[23]</td></tr>
<tr><td id="7-1g">K</td><td id="7-1h">varied</td><td id="7-1i">CTL carrying capacity</td><td id="7-1j">See text</td></tr>
<tr><td id="7-1k">a</td><td id="7-1l">0.01 day cells</td><td id="7-1m">CTL killing rate</td><td id="7-1n">[23]</td></tr>
<tr><td id="7-1o">k</td><td id="7-1p">1000 virions cells-1</td><td id="7-1q">HPV burst size</td><td id="7-1r">[23]</td></tr>
<tr><td id="7-1s">C2</td><td id="7-1t">0.05 day</td><td id="7-1u">HPV clearance rate</td><td id="7-1v">[23]</td></tr>
</table>
doi:10.1371/journal.pone.0168133.t001

<a id='36010060-8da7-43bd-a1bc-111f7fbc23dc'></a>

for changes in available CTL concentrations between an HPV infection and HIV/HPV co-infection. Lastly, the oncogene expression ε ranges from zero to one.

<a id='3b4f11b3-9a82-4c34-a9f0-a6e4fb37a689'></a>

**The viral dynamics of HPV infected individuals.** We first study the dynamics of HPV infection in the absence of HIV, as given by model (6) with _I_ = _V_ = 0 cells per ml, and _T_ = 10⁶ cells per ml. We let _ε_ = 0.5 per day, _K_(_T_) = 35 cells, _b_ = 3.5x10⁻⁵ and the other parameters are listed in Table 1. Under these assumptions, model (6) predicts HPV and CTL levels similar to those in [23]. In particular, HPV reaches a maximum of 1.4x10⁵ copies at day 174 and eventual clearance (see Fig 2, panel b, green solid line). The CTL expansion is delayed by 80 days, and reaches an equilibrium value of 27 cells by day 240 (see Fig 2, panel b, purple dashed line). Transit-amplifying cells, _Y_₂ with high oncogenic gene expression, are 12-times higher than cells with low oncogenic expression, _Y_₁ (see Fig 2, panel a). This result is dependent on the oncogene expression rate _ε_ (not shown).

<a id='d806ab2c-6808-4cab-b0ff-d2d4c8a74b61'></a>

The viral dynamics of HIV/HPV co-infected individuals. We start by assuming that the _tat_ effect leads to the doubling of available target epithelial cells, _i.e._ N₂(1 + pV) = 2N₂. We then account for HIV induced immunosuppression in an HIV/HPV co-infected individual, by changing K(T) as follows. We have shown in the previous section that an HIV-naïve individual has a CTL carrying capacity K(T) = 35 cells, where T = 10⁶ CD4+ T cells per ml and b = 3.5x 10⁻⁵. We keep the b = 3.5x10⁻⁵ and decrease the T number to i) T = 5x10⁵ cells per ml, corresponding to average chronic HIV CD4+ T cell numbers [47]; ii) T = 3.3x10⁵ cells per ml as in the HIV/HPV co-infection study [41]; and iii) T = 2x10⁵ cells per ml, corresponding to AIDS.

<a id='6ec28290-3af5-4726-aec7-b61ec2c9eb1c'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='9e054cf1-33fd-49e1-b2a0-39c3063afe0c'></a>

8/20

<!-- PAGE BREAK -->

<a id='1192224f-13ec-4721-97a5-e0a8c4c7063a'></a>

<::logo: PLOS
PLOS ONE
The logo features the text "PLOS ONE" with a stylized globe icon to the left of "PLOS", surrounded by small dots, and a vertical line separating "PLOS" and "ONE".::>

<a id='aebb4338-09fd-42eb-989a-cb44767402c9'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='6b9967ed-92e6-4f55-8ad9-e221da6ee25c'></a>

<::Figure: The figure titled "HPV infection" consists of two plots, (a) and (b), depicting cell counts over time. Plot (a) shows "Infected basal cells Y₁" (blue solid line) and "suprabasal, transit-amplifying cells, Y₂" (red dashed line). The x-axis is "Time in days" from 0 to 500, and the y-axis is "cells" on a logarithmic scale from 10⁻⁴ to 10⁴. Both Y₁ and Y₂ start around 10⁰ cells, with Y₁ peaking at approximately 10¹ and Y₂ peaking above 10² between 150 and 200 days, then both decline. Plot (b) shows "HPV W" (green solid line) and "CTL E" (purple dashed line). The x-axis is "Time in days" from 0 to 500, and the y-axis is "cells" on a logarithmic scale from 10⁻⁴ to 10⁶. HPV W increases from below 10⁰ to a peak above 10⁵ around 200 days, then decreases. CTL E increases from below 10⁻² to a plateau around 10¹-10² after 200 days. The parameters for plot (b) are ε = 0.5 per day and K(T) = 35 cells, with other parameters listed in Table 1.::>doi:10.1371/journal.pone.0168133.g002

<a id='500e325d-c62b-4386-853e-ad065011870b'></a>

Under these assumptions and parameters in Table 1, model (6) predicts HPV clearance in cases (i) and HPV persistence in cases (ii) and (iii). In case (i), HPV levels reaches a maximum of 2.4x105 copies at day 128 and clears by day 1050. In cases (ii) and (iii), HPV reaches steady state values of 3.5x106 and 6.7x107 DNA cells after 20 and 2.1 years, respectively (see Fig 3, panel a). CTL levels decrease to 17.5, 11.5 and 7 cells per ml for cases (i), (ii) and (iii), respectively (see Fig 3, panel b).

<a id='64f8169c-14b3-47ab-9ff4-b5335daa8b80'></a>

To determine the relative contributions of the _tat_-effect and immunosuppression in the transition between HPV clearance and HPV persistence, we derived a bifurcation diagram showing the asymptomatic dynamic of HPV as given by model (6) when both p$\bar{V}$ and K($\bar{T}$) are varied. As expected, an increase in the available epithelial cells requires a larger CTL population for the clearance to occur (see Fig 4, red dashed lines). In particular, if the _tat_ effect is increased to 100% such that (1+p$\bar{V}$) = 2, then the CTL carrying capacity has to be K >11.9 cells for clearance to occur. Moreover, a carrying capacity as low as K($\bar{T}$) = 7 cells is enough to ensure HPV clearance in the HIV-naïve case (80% lower than the considered base value of K($\bar{T}$) = 35 cells).

<a id='61136e70-e92b-468f-926c-85ca89de3a70'></a>

**Changing oncogene expression rates.** We have considered that the oncogenic expression is ε = 0.5. In an HIV-naïve host, this corresponds to transit-amplifying cells, Y₂ exceeding the infected basal cells, Y₁ by 12-times (see Fig 2, panel a). In the mathematical model from [23], the authors showed that in an HIV-naïve, HPV-unvaccinated individual, a decrease in the oncogenic expression ε leads to a slower growth of Y₁, Y₂ and W, a delayed and weak CTL response E and, consequently, a delayed HPV clearance. To determine whether this effect is carried over in an HIV/HPV co-infected individual, we compared clearance regions for ε = 0.1 per day, ε = 0.5 per day and ε = 0.9 per day for varying p V and K(T) values (see Fig 4, panel a). We find that the clearance regions (defined as the area under the curve) are higher for low ε values, similar to the results from an HIV-naïve patient [23].

<a id='f4f3d515-023f-4e28-afd1-840bba32162d'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='5bff4d77-7f01-4ca0-99b4-6be481158dfe'></a>

9 / 20

<!-- PAGE BREAK -->

<a id='7f6ac371-2379-4ef5-ba4d-7f81a185340a'></a>

<::logo: PLOS ONE
PLOS | ONE
This logo features a stylized globe with surrounding dots, followed by the word "PLOS" in bold, a vertical line, and then "ONE" in a smaller font.::>

<a id='9ef39002-f4ac-40ad-b601-ecb28b99482a'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='a86761cd-994e-4e90-82f2-4cb857c0187c'></a>

<::chart: The image displays two line plots, (a) and (b), illustrating HIV/HPV co-infection dynamics. Both plots have "Time in days" on the x-axis. (a) HPV W: The y-axis is labeled "HPV DNA cells" and ranges from 10^0 to 10^8 on a logarithmic scale. Four lines are plotted, representing different total cell concentrations (T) and pV values:  - Blue solid line: W, T = 10^6, pV = 0  - Red dashed line: W, T = 5 x 10^5, pV = 1  - Green dotted line: W, T = 3.3 x 10^5, pV = 1  - Purple dashed-dotted line: W, T = 2.5 x 10^5, pV = 1. (b) CTL E: The y-axis is labeled "cells" and ranges from 10^-2 to 10^2 on a logarithmic scale. Four lines are plotted, representing different total cell concentrations (T) and pV values:  - Blue solid line: E, T = 10^6, pV = 0  - Red dashed line: E, T = 5 x 10^5, pV = 1  - Green dotted line: E, T = 3.3 x 10^5, pV = 1  - Purple dashed-dotted line: E, T = 2.5 x 10^5, pV = 1. The caption states that the plots show (a) HPV W and (b) CTL E as given by model (6) for ε = 0.5 per day, with parameters listed in Table 1. The T values are specified as: T = 10^6 cells per ml (blue solid lines); T = 5x10^5 cells per ml (red dashed lines); T = 3.3x10^5 cells per ml (green dotted lines); and T = 2x10^5 cells per ml (purple dashed-dotted lines).::>
doi:10.1371/journal.pone.0168133.g003

<a id='9eb8af6b-31b8-4cf6-9382-c56f160d2c83'></a>

<::Figure 4: Varying oncogene expression rates. The figure consists of three subplots. (a) Bifurcation diagram showing cleared W (area below the curve) versus chronic W (area above the curve) as the tat effect pV and CTL carrying capacity K(T) vary. Here, the criterion for HPV clearance is given by Eq (7). The x-axis is 'CTL carrying capacity, K' ranging from 0 to 50. The y-axis is 'tat effect, pV' ranging from 0 to 10. There are three lines representing different epsilon values: a blue solid line for epsilon = 0.1, a red dashed line for epsilon = 0.5, and a green dotted line for epsilon = 0.9. The region above these lines is labeled 'Chronic HPV' and the region below is labeled 'Cleared HPV'. (b) HPV W over time. The x-axis is 'Time in days' ranging from 0 to 1500. The y-axis is 'HPV DNA cells' on a logarithmic scale from 10^-2 to 10^6. Three curves are shown: a blue solid line for W, epsilon = 0.1; a red dashed line for W, epsilon = 0.5; and a green dotted line for W, epsilon = 0.9. These curves show an initial rise followed by a decline, with the peak occurring earlier and being higher for lower epsilon values. (c) CTL E over time. The x-axis is 'Time in days' ranging from 0 to 500. The y-axis is 'cells' on a logarithmic scale from 10^-2 to 10^2. Three curves are shown: a blue solid line for E, epsilon = 0.1; a red dashed line for E, epsilon = 0.5; and a green dotted line for E, epsilon = 0.9. These curves show an increase in E, eventually stabilizing at a value around 10^1. The rise is faster for higher epsilon values. (b) HPV W; and (c) CTL E as given by model (6) for parameters listed in Table 1 and epsilon = 0.1 (blue solid lines), epsilon = 0.5 (red dashed lines), and epsilon = 0.9 (green dotted lines).: chart::>

<a id='7b13767c-949d-4a43-99ce-6601c1ce0ce7'></a>

doi:10.1371/journal.pone.0168133.g004

<a id='27c08546-7446-4909-8e0e-538b651ad3fd'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='8f15da12-23c8-4cb2-aa45-16bc7dad0203'></a>

10 / 20

<!-- PAGE BREAK -->

<a id='1a3ca6d5-8fb0-481d-a2d3-4c251ba08dcb'></a>

<::PLOS | ONE logo with a stylized globe icon: figure::>

<a id='e1319663-6d19-4e8d-9dac-b951ef71139f'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='bd40eb28-e132-40ff-b366-cddc53fdb1ba'></a>

<::chart: Fig 5. HIV/HPV dynamics when cART and HPV infection coincide. The figure contains two main plots, (a) and (b), each with an inset. (a) HPV W: The main plot shows HPV DNA cells (W) on a logarithmic y-axis (from 10^0 to 10^6) versus Time in days on the x-axis (from 0 to 160). A blue line labeled "W" shows HPV DNA cells increasing over time from an initial value near 10^0 to approximately 10^5 at 160 days. The inset for panel (a) shows a zoomed-out view of HPV DNA cells (logarithmic y-axis from 10^0 to 10^2) over a longer time scale (x-axis from 0 to 500 days). The blue line peaks around 10^1 at approximately 120 days and then decreases, indicating HPV clearance in the long term. (b) CD4+ T cells (T) as given by model (5) under cART: The main plot shows cells per ml on a linear y-axis (from 1 to 7 x 10^5) versus Time in days on the x-axis (from 0 to 160). A green line labeled "T" shows CD4+ T cells increasing over time from an initial value of approximately 3 x 10^5 to over 5 x 10^5 at 160 days. The inset for panel (b) shows a zoomed-out view of cells per ml (linear y-axis from 3 to 7 x 10^5) over a longer time scale (x-axis from 0 to 500 days). The green line shows CD4+ T cells increasing and then plateauing at around 5.5 x 10^5. Here, ε = 0.5, εRT = 0.95, εPI = 0.5, and all other parameters are listed in Table 1. Initial conditions are T₀ = 3.3x10⁵ cells per ml, I₀ = 2.4x10⁵ cells per ml, V₀ = 4.8x10⁴ virions per ml, Y₁₀ = 1 cells, E₀ = 0.01 cells, Y₂₀ = W₀ = 0, and t = 0 is the start of cART. Over the first 24 weeks HPV persists (panel a), and in the long term HPV is cleared (zoomed out panel a).::>

<a id='660940fd-e9cb-495d-b0c3-d7428db98e3c'></a>

doi:10.1371/journal.pone.0168133.g005

<a id='93672618-5833-41cb-b995-671bec7607b5'></a>

To determine the timing of clearance, we fixed the *tat*-effect to (1 + pV) = 2 and the CTL carrying capacity to K(T) = 17.5 cells and determined the changes in W and E dynamics for various values of ε (see Fig 4, panels b and c). We find that HPV levels are slightly higher for high oncogenic expression, ε, and they take significantly longer to get cleared (see Fig 4, panel b). This happens in spite of the fact that CTL levels grow faster for high oncogenic expression (see Fig 4 panel c).

<a id='fc3ea0fb-b4a5-4302-ada4-ed38396966c5'></a>

**The effect of cART on an HIV/HPV co-infection.** A recent trial has investigated the dynamics of oral HPV DNA in HIV/HPV co-infected individuals undergoing cART. They found that 28% of the co-infected individuals had a persisting infection with at least one of the HPV genotypes. Moreover, 42% of co-infected individuals experienced either a persisting infection with the same genotype, or an acquired infection with a different genotype 24 weeks after the start of therapy [41]. We use model (5) to determine the *tat* effect *pV*, CTL numbers *K*(T), and oncogenic expression *ε* that can explain this observation.

<a id='9db04bbc-cf5b-4041-b73e-78d6ccfe5d66'></a>

The patients in [41] have T̄ = 3.3x10⁵ uninfected CD4+ T cells per ml and V̄ = 4.8x10⁴ virions per ml at day _t_ = 0, when cART begins. We assume that the drug efficacies are ε₁₁ = 0.95, ε₁₁ = 0.5 and the oncogenic factor is ε = 0.5. If the co-infection with HPV is not included _i.e._ p̄V̄ = 0 and _K_(̄T̄) = 35 cells, then HIV RNA levels decrease to below limit of detection (of 50 copies per ml) in 6.5 days. CD4+ T cell concentration increases to a maximum of 5.6x10⁵ cells per ml by day 329 (161 days after the end of the study).

<a id='a981e89c-9da8-42b1-82b0-7188688c7af1'></a>

We next add co-infection into our model and apply it to the setup of the oral co-infection
trial [41]. If pV = 1 and K(T) = 11.5 cells (corresponding to CD4+ T cell concentration of T =
3.3x10⁵ per ml), then HPV is cleared under the cART conditions ε₁₄ = 0.95 and ε₁₁ = 0.5. The
timing of clearance depends on two factors: the HPV stage and the level of CD4+ T cells at the
start of cART. If HPV infection occurs at the same time as the start of cART, then the HPV lev-
els increase to a peak value of 1.4x10⁵ DNA cells and stay elevated throughout the 24 weeks of
the study (see Fig 5, panel a). HPV starts to decay at day 180 (see Fig 5, panel a, zoomed out

<a id='20e49942-2d58-4067-a27e-9edeb2eee885'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='7cf42791-4adb-486d-8d27-31668a6e1073'></a>

11/20

<!-- PAGE BREAK -->

<a id='38518843-a193-4a26-9e75-2c88965c0ed0'></a>

<::PLOS | ONE logo with a stylized globe icon: figure::>

<a id='650663f6-6007-4a55-a64a-994ff8656e46'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='5bd04eb6-603d-4dff-93f7-a6bf04c64a8e'></a>

<::chart::>  
**Fig 6. HIV/HPV dynamics under chronic HPV at the start of cART.**  
(a) HPV W  
This plot shows the concentration of HPV DNA cells (W) over time in days, on a logarithmic y-axis. The y-axis ranges from 10^6 to 10^8 HPV DNA cells. The x-axis ranges from 0 to 160 days. A blue line, labeled 'W', starts around 2x10^7 HPV DNA cells at day 0 and decreases continuously to approximately 1.5x10^6 HPV DNA cells by day 160.  
(b) CD4+ T cells T as given by model (5) under cART.  
This plot shows the concentration of CD4+ T cells (T) over time in days. The y-axis is labeled 'cells per ml' and ranges from 1x10^5 to 7x10^5 cells per ml. The x-axis ranges from 0 to 160 days. A green line, labeled 'T', starts around 3.3x10^5 cells per ml at day 0 and increases continuously to approximately 5.2x10^5 cells per ml by day 160.  
  
Here, ε = 0.5 per day, ε_RT = 0.95, ε_PI = 0.5, and all other parameters are listed in Table 1. Initial conditions are T_0 = 3.3x10⁵ cells per ml; I_0 = 2.4x10⁵ cells per ml; V_0 = 4.8x10⁴ virions per ml; Y_10 = 3.2x10³ cells; Y_20 = 1.6 x10⁴ cells; W_0 = 1.8x10⁷ virions; E_0 = 0.01 cells, and t = 0 is the start of cART. Moreover, we found two instances when HPV infection stays chronic in the presence of cART, namely strong drug efficacy, ε_RT = 0.95 and ε_PI = 0.5, and AIDS level CD4+ T cells, T ≤ 1.7×10⁵ cells per ml; and, inefficient drug therapy, ε_RT = 0.2 and ε_PI = 0 and intermediate CD4+ T cell levels T ≤ 2.6×10⁵ cells per ml.::>

<a id='0cd7e598-438e-4ef1-84b9-7b68d9f2ba26'></a>

doi:10.1371/journal.pone.0168133.g006

<a id='7a412dc2-2aba-4099-b297-a59d52577bee'></a>

graph) when CD4+ T cells reached 5.2x10^5 cells per ml (see Fig 5, panel b) which is the low level of CD4+ T cell counts for healthy individuals.

<a id='6456c0f6-c822-43d9-b827-dd52878d5cd0'></a>

In contrast, if HPV infection reached its chronic state at the start of cART, then cART helps to initiate HPV decay by day 8 (see Fig 6, panel a), when the CD4+ T cell population is still low, i.e., T = 3.5×105 cells per ml (see Fig 6, panel b). It is worth noting that cART removes HIV, and consequently the _tat_ effect, but it does not control how fast CD4+ T cells rebound.

<a id='ead30653-efe5-4f5a-9af2-87dbdf5935b4'></a>

Lastly, we investigated how the dynamics of HPV infection in a co-infected individual undergoing cART change with the oncogenic expression e. We found that HPV levels stay high throughout the first 24 weeks of cART, but are eventually cleared for all levels of onco-genic expression (see Fig 7, panel a). This is due to the fact that the dynamics of CD4+ T cells are not affected by the oncogenic expression (see Fig 7, panel b), and, in all cases, the patients return to healthy CD4+ T cell levels. HPV has lower peak levels but longer time until clearance for low oncogenic expression, e = 0.1 (see Fig 7, panel a, blue solid line) compared to high oncogenic expression & = 0.9 (see Fig 7, panel a, green dotted line).

<a id='c2efb100-9600-4b1b-bf33-95e70d5c69d0'></a>

An intriguing finding in [41] showed higher frequency of HPV DNA in individuals with the strongest rebound in absolute CD4+ T cell count post cART [41]. To investigate possible underlying mechanisms explaining this unexpected finding, we considered two virtual patients: patient 1 has a rebound to 6.5x10^5 cells per ml CD4+ T cell count as in [41], and patient 2 has a rebound to 5.6x10^5 cells per ml. We further assume that patient 1 has high oncogenic expression level \epsilon=0.9 per day, and patient 2 has low oncogenic expression level \epsilon=0.1 per day. This increase in oncogene expression leads to higher HPV DNA production in patient 1 (see Fig 8 panel a, solid blue vs dashed green line) in spite of its better cART outcome (see Fig 8, panel b, solid blue versus dashed green lines).

<a id='b2484245-fad6-4995-99a0-55495ace4283'></a>

We investigated the coinfection model using the full model from [23] and found that it gives similar results (data in S2 File) to the coinfection model (6) and the differences are negligible (Fig A in S2 Fig and Fig B in S2 Fig).

<a id='9f43b018-9e22-453d-bc96-f21e724c95c2'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='0c74208b-5250-4469-8509-26cd06d92d8e'></a>

12 / 20

<!-- PAGE BREAK -->

<a id='df25889d-656c-4f29-9280-485d8eaf8263'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe icon surrounded by dots, with the text "PLOS" in bold, followed by a vertical line and "ONE" in a lighter font::>

<a id='13e5f12e-95c0-4782-acea-e71fd0e59a26'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='ea1087f8-24f6-4136-87aa-cb2a7c2d3247'></a>

<::chart: Fig 7. Effect of oncogene expression rates and cART on HIV/HPV co-infections. The figure consists of two panels: (a) and (b).

Panel (a): HPV W
- Title: (a)
- Y-axis: HPV DNA per ml (logarithmic scale from 10^-2 to 10^6)
- X-axis: Time in days (0 to 1000)
- Legend:
  - W, ε=0.1 (blue solid line)
  - W, ε=0.5 (red dashed line)
  - W, ε=0.9 (green dotted line)
- Description: This panel shows the concentration of HPV DNA over time for different values of ε. The blue solid line (ε=0.1) shows a peak around 500 days and then declines. The red dashed line (ε=0.5) and green dotted line (ε=0.9) show an earlier and higher peak (around 10^5) before rapidly declining to very low levels by approximately 600-800 days.

Panel (b): CD4+ T cells T
- Title: (b)
- Y-axis: cells per ml (linear scale from 3.5 x 10^5 to 6 x 10^5)
- X-axis: Time in days (0 to 1000)
- Legend:
  - T, ε=0.1 (blue solid line)
  - T, ε=0.5 (red dashed line)
  - T, ε=0.9 (green dotted line)
- Description: This panel shows the count of CD4+ T cells over time for different values of ε. All three lines (blue solid, red dashed, green dotted) start around 3.5 x 10^5 cells per ml, rapidly increase, and then plateau at approximately 5.7 x 10^5 cells per ml by around 600 days. The lines are very close to each other, indicating little difference in CD4+ T cell counts for the different ε values.

Contextual information for the figure: Here, ε = 0.1 (blue solid line); ε = 0.5 (red dashed line); ε = 0.9 (green dotted line), εRT = 0.95, εPI = 0.5, and all other parameters are listed in Table 1. Initial conditions are T₀ = 3.3x10⁵ cells per ml, I₀ = 2.4x10⁵ cells per ml, V₀ = 4.8x10⁴ virions per ml, Y₁₀ = 1 cells, E₀ = 0.01 cells, Y₂₀ = W₀ = 0 and t = 0 is the start of cART.::>

<a id='07cfa271-76de-42ab-9921-892387ecf538'></a>

doi:10.1371/journal.pone.0168133.g007

<a id='65915eda-36f1-4547-b3a7-0512a413ca41'></a>

## Discussion
The model presented here is a mechanistic ordinary differential equation (ODE)-based model that studies the dynamical interaction between the host and two virus populations: HIV and HPV. The model is aimed towards determining the mechanistic interactions leading to HPV

<a id='1581de8d-ecb7-40ca-88d5-cceb1901a795'></a>

<::chart: The image displays two line plots, (a) and (b), both showing data over 'Time in days' on the x-axis, ranging from 0 to 150. Figure (a) is titled 'HPV DNA cells' on the y-axis, which is on a logarithmic scale from 10^0 to 10^6. It shows two curves representing 'W' (HPV viral load) for different epsilon (ε) values. The green dashed line represents W with ε = 0.1, showing a gradual increase from approximately 10^2 to about 2x10^3 cells over 150 days. The blue solid line represents W with ε = 0.9, showing a sharp increase from approximately 10^2 to a peak of about 2x10^5 cells around 100 days, followed by a slight decrease. Figure (b) is titled 'cells per ml' on the y-axis, which is on a linear scale from 3x10^5 to 8x10^5. It shows two curves representing 'T' (CD4+ T cells) for different epsilon (ε) values. The green dashed line represents T with ε = 0.1, showing an increase from approximately 3.3x10^5 to about 5.2x10^5 cells per ml over 150 days. The blue solid line represents T with ε = 0.9, showing an increase from approximately 4.2x10^5 to about 6.2x10^5 cells per ml over 150 days.::>Fig 8. Effect of CD4+ T cell levels on HIV/HPV co-infections. (a) HPV W; (b) CD4+ T cells, T, as given by model (5) under cART. Here, ε = 0.1 (green dashed line), ε = 0.9 (blue solid line), εRT = 0.95, εPI = 0.5, and all other parameters are listed in Table 1. Initial conditions are T₀ = 3.3x10⁵ (green dashed line) or T₀ = 4.5x10⁵ (blue solid line) cells per ml, I₀ = 2.4x10⁵ cells per ml, V₀ = 4.8x10⁴ virions per ml, Y₁₀ = 1 cells, E₀ = 0.01 cells, Y₂₀ = W₀ = 0 and t = 0 is the start of cART.

<a id='3ff940ce-d5e3-4fc5-bce0-fe16b8e175ac'></a>

doi:10.1371/journal.pone.0168133.g008

<a id='fc3fe0f3-24db-4ab4-bb25-a1aae5449c7c'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='388afd3d-8901-4c22-8bd2-884c06ad6d28'></a>

13 / 20

<!-- PAGE BREAK -->

<a id='c566893c-2a2c-4a0c-8f2f-b46707ac45f2'></a>

<::PLOS | ONE logo with a stylized globe icon: figure::>

<a id='986e0889-91f9-4a73-854d-cf3e94155aef'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='ca909af5-1fb2-4830-98ae-39b35fdc1457'></a>

clearance or persistence in HIV/HPV co-infected individuals post cART, and increased risk of HPV infection in HIV infected individuals as reported clinically [41] [48] [15, 36]. Indeed, a recent study reported an increased prevalence of oral HPV infection in an HIV-infected cohort, where HPV DNA levels in the patients were not reduced following treatment with antiretroviral therapy [41]. This result is corroborated by other studies, suggesting that HPV may be present chronically in oral sites among HIV infected individuals undergoing combina- tion antiretroviral therapy [49, 50].

<a id='ffa0d65c-6796-485a-afd2-c91579e514f4'></a>

To address the possible interactions leading to HPV persistence, we highlighted specific sce-narions presenting an increased persistence of HPV due to the permissive immune environ-ment created in an HIV-infected individual. Our model predicted that among the HIV infected individuals, those who had CD4+ T cells corresponding to average chronic HIV CD4 + T cell levels were more likely to clear HPV than those who had the CD4+ T cell levels reported in the co-infection clinical study [41], or those who had CD4+ T cell levels corre-sponding to AIDS. These results are dependent on the oncogenic expression levels, with HPV DNA levels increasing and taking a longer time to clear for high oncogenic expression levels. Interestingly, for high oncogenic expressions, HPV clearance is delayed despite the faster expansion of CTL levels. This is due to an increase in the amount of HPV transit-amplifying cells.

<a id='c0d69d9b-be86-4d07-9c81-f9b15c553304'></a>

We used the model to study the impact of cART on HPV persistence in HIV/HPV co-infected individuals and compared the findings with those from the clinical study [41], which showed that 28% of the co-infected patients had at least one detectable HPV DNA genotype 12–24 weeks after the start of cART. Our mechanistic model predicts that, for the median CD4 + T cell levels in [41], HPV levels decrease in co-infected individual receiving cART by 24 weeks. In addition, our model showed persistence of HPV DNA levels between 12–24 weeks post cART in the patients with the highest CD4 T cell rebound, as in [41]. The HPV DNA levels may be higher in the patients with the higher CD4 T cell rebound after cART if these patients have a higher HPV oncogenic expression. However, for these individuals with restored high levels of CD4+ T cells post cART, we predict clearance for HPV levels at 48 weeks. These findings, which differ from those in [41], can be explained by the absence of consideration for latent HIV reservoirs and latent HPV infection. Thus, reactivation of the latent HIV reservoirs and latent HPV infection is an integral part of immune reconstitution in the co-infected individuals and is guaranteed to impact HIV/HPV co-infection dynamics. Some studies have investigated the prevalence of anal human papillomavirus infection in HIV-infected patients receiving long-term cART. Piketty et al, showed that the incidence of anal cancer was higher in HIV-infected patients particularly in MSM (men who have sex with men) and the incidence of anal HPV infections did not reduce despite the increased CD4+ T cell count following cART [51], suggesting that cART- associated immune restoration does not play a role in reduction of the incidence of anal cancers [52]. Other studies have analyzed the effects of HIV and cART on HPV persistence and cervical squamous intraepithelial lesions. Blitz et al reported higher rate of acquisition and reduced clearance of oncogenic high-risk HPV types among HIV positive women. The study reported that cART improved clearance of high risk HPV type other than oncogenic HPV type 16/18 [53]. Interestingly, the findings from the study are in accordance with the findings from our model, wherein the oncogenic high risk HPV types persisted in the patients restored to high CD4+ T cell level post 24 weeks of cART.

<a id='d2e04055-33f7-4ebc-aa99-97088dd06d34'></a>

Our study predicts that the timing of viral clearance is determined by the timing of cART
compared to the timing of HPV co-infection, as well as the CD4 T cell level. When cART is
started shortly after HPV infection, HPV will expand and will not be controlled in the 24
weeks of cART as described for the 28% cases in [41]. This can be explained by the fact that

<a id='f567d149-f604-47e4-9b7a-8cfdce04c5ba'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='882a51ac-7422-43c8-964b-485085ee8afb'></a>

14 / 20

<!-- PAGE BREAK -->

<a id='973ef626-2f9f-4b37-8f48-590297163726'></a>

<::PLOS ONE logo with a stylized globe icon surrounded by dots: figure::>

<a id='5b38b263-b078-4001-a073-4b94697e44fc'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='5c51ae01-3610-48e9-a9c5-f0c8c1c439da'></a>

CTL expansion and control of HPV is delayed due to both recruitment and size limitation observed when CD4+ T cell reconstitution following cART is delayed. If, however, the cART starts at the peak anti-HPV CTL response, then HPV is cleared as soon as CD4+ T cell reconstitution allows for the adequate CTL levels to control HPV infection. Thus, our findings support the conclusion that increased risk of infection [48] due to immunosuppression may play a role in the reduced clearance of HPV. Specifically, we showed that chronic HPV levels were maintained at- i) AIDS level CD4+ T cell count and ii) inefficient drug therapy, εRT = 0.2 and εPI = 0 with intermediate CD4+ T cell levels such that T ≤ 2.6×10⁵ cells. These results provide further evidence to support the findings from other studies that show immunosuppression plays a role prior to cancer diagnosis [48] and facilitates HPV related head and neck carcinogenesis [15,30]. The results from our model are independent of the molecular effects induced by tat, which are removed when HIV is removed, and therefore do not influence HPV clearance. Finally, our results show that when HPV infection occurs at the same time as the start of cART, HPV levels increase and stay elevated throughout the 24 weeks of study. The findings support previous reports that predicted an increased risk of oral HPV infection among immunosuppressed individuals, which can be explained by the reactivation or reacquisition of a previously acquired infection [48]. We further investigated the possibility of HPV persistence and found that weak cART or AIDS level CD4+ T cells, which do not rebound to high enough levels, are needed for HPV to remain chronic following cART. These results highlight the important role played by CD4+ T cells in the resolution and control of HPV infection. It also demonstrates the importance of cART in controlling molecular mechanisms such as tat and CD4+ T cell rebound. A finding from our model highlights the need of a higher carrying capacity in a co-infected individual for HPV clearance to occur. This suggests a potentially clinically testable hypothesis that—if a HIV/HPV co-infected individual is immunosuppressed, then they should be treated for immunosuppression first. Once the CD4+ T cell levels are restored, the individual can be treated against HPV. Moreover, if a person treated for HIV has restored CD4+ T cell levels, HPV treatment should be tailored towards type specific HPV. In particular, our simulation result show that individuals with high CD4+ T cell levels post cART, produce more HPV when their oncogenic expression is high, compared with a patient with a weaker CD4+ T cell restoration but a lower oncogenic expression. Hence, the treatment (vaccine) against the type specific HPV, may aid the viral clearance.

<a id='14777bdc-c26d-4943-bf8b-2276b73af1d2'></a>

This work is one of the first HIV/HPV co-infection models that investigates the dynamics of HPV in HIV-infected individuals. The only other published HIV/HPV co-infection model is a transitional probability-based model [54], which was used to study the relationship between immune status and the probability of the type of HPV clearance in HIV infected patients. The model [54] showed that HPV clearance was mainly based on the level of CD4+ T cell count. The main difference between our findings compared to [54] stems from the fact that the current model takes into account that HPV clearance not only depends on the levels of CD4+ T cell count but also the stage of HPV infection. Our results are consistent with observed associations between immunosuppression and HPV persistence in several clinical studies [41] [48] [15, 36].

<a id='9d54b3d5-96b6-45b3-a2b6-4867dda2dbd3'></a>

To understand the mechanisms responsible for progression to AIDS and for CD4+ T cell
rebound following cART, it is necessary to understand the impact of HIV in the dynamics of
each functional CD4+ T cell subsets [55–58]. Th17 cells [59] [60] appear to play a central role
in the HIV pathogenesis. Th1/17 CD4+ T cells have a role as a long-term reservoir for HIV-1
infection, and are unaffected by cART [61]. Tfh serve as reservoirs of virus-infected cells [62]
in the lymph node and peripheral blood. The central memory (TCM) are the major cellular res-
ervoirs for HIV in the peripheral blood [63]. Furthermore, long-term cART is known to only

<a id='cd2e5c80-3dd7-4969-9b84-417b94312698'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='fcdbb753-733c-4bc8-b8fc-d0f580459454'></a>

15/20

<!-- PAGE BREAK -->

<a id='7e351750-9c3f-4651-b7c3-c85b6cb42b9b'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe icon surrounded by dots, with the text "PLOS" in bold, followed by a vertical line and "ONE" in a lighter font::>

<a id='b5d6bf67-50fe-4408-8427-c811c1840919'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='b4485b6b-c772-44c1-972f-894278c3e7f1'></a>

partially restore the CD4+ T cell pool [64, 65] in the oral mucosal sites. Thus, investigating the
T cell subsets involved in the HIV/HPV co-infection in our model would aid in better under-
standing of these mechanisms and the development of approaches for their therapeutic
manipulations.

<a id='6376917a-8abd-476c-9153-d1827fc3bc22'></a>

The present modeling study should be evaluated in the context of several limitations. First, it does not take into account the spatial structure of the epithelial tissue. A generalized model that takes in to account the infectivity and layer transition terms described by probabilities or one which would consider spatial structures for epithelial cells in different layers, requires extensive knowledge of numerous parameters, that are currently unknown. The second limitation concerns the immune clearance of lesions caused by HPV infections, which can lead to asymptomatic or latent infections with possibility of increased virion production upon immunosuppression [66-69]. This further necessitates the need for consideration of both the cellular environment and the site of infection which are important determinants of virus activity [35]. Third, the simplistic modeling approach employed in the current modeling study does not take into account the feed-back from the HPV to HIV infection. Due to absence of feedback from HPV to HIV, we disregard the effects of cART induced immune reconstitution. Additionally, our study does not consider the activation of latent HIV reservoirs post cART, which may contribute to the emergence new HPV genotype infections in co-infected individuals as shown in [41].

<a id='3789d5a1-2cae-4cba-9372-736792f61401'></a>

The next step would be investigating the T cell subsets involved in the HIV/HPV co-infection in our model. Additionally, the findings of the modeling study and associated limitations guarantees and necessitates inclusion of latent T cell reservoirs which are involved in the activation of residual cART induced immune reconstitution. Furthermore, incorporating the immune activation in the T cells under the effect of cART during a HIV/HPV co-infection would corroborate the findings regarding the presence of new detectable HPV DNA.

<a id='93fc43ad-12f4-4295-b055-5e0e129b9d9d'></a>

In summary, we developed a novel mathematical and computational model of HIV/HPV co-infection and used it to present hypotheses for the mechanisms underlying HPV persis-tence in HIV/HPV co-infected individuals. Our model can be applied to studying interactions between HIV and other widespread microbes to gain a better mechanistic understanding, guide the rational for the design of clinical trials, and accelerate the path to safer and more effective vaccines and therapeutics. We use this study as an alternative approach to determin-ing how overall CD4+ T cell levels influence HPV prognosis in an HIV-infected individual. Overall, a better understanding of the cell specificity of HIV infection integrated with the cellu-lar environment in HPV infection would facilitate the development of more effective therapeu-tic strategies in HIV/HPV co-infections.

<a id='e349df46-dcbc-4bdd-a61e-4b2baf4f6584'></a>

The model was deposited in BioModels [39] and assigned the identifier MODEL 1605030001.

<a id='bf51264f-d521-4c37-8026-303eb9d17d3a'></a>

# Supporting Information

S1 Fig. Systems biology markup language (SBML) compliant network of interactions between HIV (V) and HPV (W) created using CellDesigner. The left side of the figure represents the HIV dynamics wherein the interaction between target CD4+ T cells (T), productively infected CD4+ T cells (I) and HIV (V) are shown. The figure also includes the effect of reverse transcriptase (RT) and protein inhibitor (PI) (shown by red line—inhibition). The right side of the figure represents the HPV dynamics wherein the interaction between infected basal cells (Y1), suprabasal transit-amplifying cells (Y2), HPV specific (E) cells and HPV (W) are shown.
(PDF)

<a id='6f0ff8f1-76cd-4afb-95bd-c17fa33d99f3'></a>

S2 Fig. Full model comparison. (A) HIV/HPV co-infection model comparison. (a) HPV W and (b) CTL E as given by model (5), solid blue lines and model (26), dashed red lines, for ɛ = 0.5 per day, parameters are listed in Table 1 for different T levels- T = 10⁶ cells per ml (first

<a id='a3eb88ed-c44f-4976-a017-a9ab11dee6f6'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='4e532117-e43a-41ee-be9c-65fa7a8368df'></a>

16 / 20

<!-- PAGE BREAK -->

<a id='5c4751c7-a502-484c-bd17-6467885aa596'></a>

<::logo: PLOS
PLOS ONE
The logo features a stylized globe surrounded by dots, with the text "PLOS ONE" next to it, separated by a vertical line.::>

<a id='ce403ace-ae40-4abd-9036-93263e31b401'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='9f13befe-66c7-466a-aaae-9fba977560ea'></a>

row); T = 5x10⁵ cells per ml (second row); T = 3.3x10⁵ cells per ml (third row); and T = 2x10⁵ cells per ml (fourth row). (B) HIV/HPV dynamics when cART and HPV infection coincide.
(a) HPV W; (b) CD4+ T cells (T) as given by model (5) solid blue lines and model (26) dashed red lines under cART. Here, ε = 0.5, εRT = 0.95, εP1 = 0.5, and all other parameters are listed in Table 1 and t = 0 is the start of cART. Over the first 24 weeks HPV persists (panel a), and in the long term HPV is cleared (zoomed out panel a).
(PDF)

**S1 File. Analytical results.**
(PDF)

**S2 File. Analysis of the coinfection model using the full model.**
(PDF)

<a id='8afe0c81-a87d-49ec-82ec-551a00449788'></a>

# Acknowledgments
We thank Dr. Isaac Rodriguez-Chavez from National Institute of Dental and Craniofacial research who provided meaningful feedback on the co-infection model.

<a id='3de17a79-b9fd-4306-aaed-e12a83135bda'></a>

# Author Contributions

**Conceptualization**: MV SE VA RH SH AL JBR SC.

**Data curation**: MV SE SH SC.

**Formal analysis**: MV SE SC.

**Funding acquisition**: RH JBR SC.

**Methodology**: MV SE SH JBR SC.

**Project administration**: VA RH SH JBR SC.

**Resources**: RH SH JBR SC.

**Software**: MV SE SH SC.

**Supervision**: VA RH SH JBR SC.

**Validation**: MV SE SH SC.

**Visualization**: MV SE SC.

**Writing - original draft**: MV SE JBR SC.

**Writing - review & editing**: MV SE VA RH SH AL JBR SC.

<a id='3e5d0791-88aa-4ab2-a551-43ca49482478'></a>

# References
1. Grierson J, Koelmeyer RL, Smith A, Pitts M (2011) Adherence to antiretroviral therapy: factors independently associated with reported difficulty taking antiretroviral therapy in a national sample of HIV-positive Australians. HIV Med 12: 562–569. doi: 10.1111/j.1468-1293.2011.00928.x PMID: 21554524
2. (2008) Life expectancy of individuals on combination antiretroviral therapy in high-income countries: a collaborative analysis of 14 cohort studies. Lancet 372: 293–299. doi: 10.1016/S0140-6736(08)61113-7 PMID: 18657708
3. Gupta R KR (2016) Global epidemiology of drug resistance after failure of WHO recommended first-line regimens for adult HIV-1 infection: a multicentre retrospective cohort study. Lancet Infect Dis.
4. De Flora S, La Maestra S (2015) Epidemiology of cancers of infectious origin and prevention strategies. J Prev Med Hyg 56: E15–20. PMID: 26789827

<a id='99022728-f5d7-4650-b32f-bcc25eb904a3'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='f03275c2-c46a-4595-9d21-32d9418cd474'></a>

17 / 20

<!-- PAGE BREAK -->

<a id='e793024f-b8fd-495a-ac19-23e7ecf3d1c9'></a>

<::A logo for PLOS ONE, featuring a stylized globe icon to the left of the text "PLOS | ONE".: figure::>

<a id='29bfede7-88b8-4666-8813-f23bd3a056e1'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='47d3a938-a186-412a-8f7b-938265119796'></a>

5. D'Souza G, Kreimer AR, Viscidi R, Pawlita M, Fakhry C, et al. (2007) Case-control study of human pap-illomavirus and oropharyngeal cancer. N Engl J Med 356: 1944–1956. doi: 10.1056/NEJMoa065497 PMID: 17494927
6. Denny LA, Franceschi S, de Sanjose S, Heard I, Moscicki AB, et al. (2012) Human papillomavirus, human immunodeficiency virus and immunosuppression. Vaccine 30 Suppl 5: F168–174.
7. Fuchs W, Kreuter A, Hellmich M, Potthoff A, Swoboda J, et al. (2015) Asymptomatic anal sexually trans-mitted infections in HIV-positive men attending anal cancer screening. Br J Dermatol.
8. Picard A, Badoual C, Hourseau M, Halimi C, Pere H, Dib F, et al. HPV prevalence in HIV patients with head and neck squamous cell carcinoma. AIDS (London, England). 2016. Epub 2016/01/26.
9. Mooij SH, van Santen DK, Geskus RB, van der Sande MA, Coutinho RA, et al. (2016) The effect of HIV infection on anal and penile human papillomavirus incidence and clearance: a cohort study among MSM. Aids 30: 121–132. doi: 10.1097/QAD.0000000000000909 PMID: 26474302
10. Geskus RB, Gonzalez C, Torres M, Del Romero J, Viciana P, et al. (2016) Incidence and clearance of anal high-risk human papillomavirus in HIV-positive men who have sex with men: estimates and risk factors. Aids 30: 37–44. doi: 10.1097/QAD.0000000000000874 PMID: 26355673
11. Society AC (2015) Cancer Facts and Figures 2015
12. Gillison M, Lowy D (2004) A causal role for human papillomavirus in head and neck cancer. The Lancet 363: 1488–1489.
13. Vernon SD, Hart CE, Reeves WC, Icenogle JP (1993) The HIV-1 tat protein enhances E2-dependent human papillomavirus 16 transcription. Virus Res 27: 133–145. PMID: 8384765
14. Kim RH, Yochim JM, Kang MK, Shin KH, Christensen R, et al. (2008) HIV-1 Tat enhances replicative potential of human oral keratinocytes harboring HPV-16 genome. Int J Oncol 33: 777–782. PMID: 18813791
15. Beachler DC, D'Souza G (2013) Oral HPV infection and head and neck cancers in HIV-infected individ-uals. Current opinion in oncology 25: 503. doi: 10.1097/CCO.0b013e32836242b4 PMID: 23852381
16. Syrjanen S (2011) Human papillomavirus infection and its association with HIV. Adv Dent Res 23: 84–89. doi: 10.1177/0022034511399914 PMID: 21441487
17. Nyagol J, Leucci E, Onnis A, De Falco G, Tigli C, et al. (2006) The effects of HIV-1 Tat protein on cell cycle during cervical carcinogenesis. Cancer Biol Ther 5: 684–690. PMID: 16855377
18. Buonaguro FM, Tornesello ML, Buonaguro L, Del Gaudio E, Beth-Giraldo E, et al. (1994) Role of HIV as cofactor in HPV oncogenesis: in vitro evidences of virus interactions. Antibiot Chemother (1971) 46: 102–109.
19. Harper DM, Franco EL, Wheeler C, Ferris DG, Jenkins D, et al. (2004) Efficacy of a bivalent L1 virus-like particle vaccine in prevention of infection with human papillomavirus types 16 and 18 in young women: a randomised controlled trial. Lancet 364: 1757–1765. doi: 10.1016/S0140-6736(04)17398-4 PMID: 15541448
20. Fontes A, Andreoli MA, Villa LL, Assone T, Gaester K, et al. (2016) High specific immune response to a bivalent anti-HPV vaccine in HIV-1-infected men in São Paulo, Brazil. Papillomavirus Research.
21. Weinberg A, Song LY, Saah A, Brown M, Moscicki AB, et al. (2012) Humoral, mucosal, and cell-medi-ated immunity against vaccine and nonvaccine genotypes after administration of quadrivalent human papillomavirus vaccine to HIV-infected children. J Infect Dis 206: 1309–1318. doi: 10.1093/infdis/jis489 PMID: 22859825
22. Perelson AS, Neumann AU, Markowitz M, Leonard JM, Ho DD. HIV-1 dynamics in vivo: virion clearance rate, infected cell life-span, and viral generation time. Science (New York, NY). 1996; 271(5255):1582–6. Epub 1996/03/15.
23. Murall CL, Bauch CT, Day T (2015) Could the human papillomavirus vaccines drive virulence evolution? Proc Biol Sci 282: 20141069. doi: 10.1098/rspb.2014.1069 PMID: 25429011
24. P Perelson AS, Ribeiro RM (2013) Modeling the within-host dynamics of HIV infection. BMC Biol 11: 96. doi: 10.1186/1741-7007-11-96 PMID: 24020860
25. Perelson AS, Ribeiro RM (2008) Estimating drug efficacy and viral dynamic parameters: HIV and HCV. Statistics in medicine 27: 4647–4657. doi: 10.1002/sim.3116 PMID: 17960579
26. Chun TW, Carruth L, Finzi D, Shen X, DiGiuseppe JA, et al. (1997) Quantification of latent tissue reser-voirs and total body viral load in HIV-1 infection. Nature 387: 183–188. doi: 10.1038/387183a0 PMID: 9144289
27. Doorbar J. Molecular biology of human papillomavirus infection and cervical cancer. Clin Sci (Lond). 2006; 110(5):525–41
28. Murall C, McCann KS, Bauch CT. Revising ecological assumptions about Human papillomavirus inter-actions and type replacement. J of Theor Biol 2014; 350:98–109.

<a id='630269e7-a939-4ba3-b8e8-ff931cbd35a3'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='6c8e130d-5972-429e-ab91-330340c3c34b'></a>

18 / 20

<!-- PAGE BREAK -->

<a id='387e547e-d7af-4092-8fab-0d2bb503503b'></a>

<::A logo for PLOS ONE, featuring a stylized globe icon to the left of the text "PLOS | ONE".: figure::>

<a id='f2af0797-5f2e-469f-ac10-d2693a1d7c71'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='4512651a-d08c-4309-ae2c-c2a891907c8b'></a>

29. Doorbar J, Quint W, Banks L, Bravo IG, Stoler M, Broker TR, et al. The biology and life-cycle of human papillomaviruses. Vaccine. 2012;30.
30. Ryser MD, Myers ER, Durrett R. HPV Clearance and the Neglected Role of Stochasticity. PLoS Comput Biol. 2015; 11(3).
31. Venuti A, Paolini F, Nasir L, Corteggio A, Roperto S, Campo MS, et al. Papillomavirus E5: the smallest oncoprotein with many functions. Mol Cancer. 2011; 10(1):1-18.
32. Moscicki A-B, Schiffman M, Kjaer S, Villa LL. Chapter 5: Updating the natural history of HPV and ano-genital cancer. Vaccine. 2006; 24.
33. Nakagawa M, Stites DP, Patel S, Farhat S, Scott M, et al. (2000) Persistence of human papillomavirus type 16 infection is associated with lack of cytotoxic T lymphocyte response to the E6 antigens. Journal of Infectious Diseases 182: 595-598. doi: 10.1086/315706 PMID: 10915094
34. Scott M, Nakagawa M, Moscicki AB (2001) Cell-mediated immune response to human papillomavirus infection. Clin Diagn Lab Immunol 8: 209-220. doi: 10.1128/CDLI.8.2.209-220.2001 PMID: 11238198
35. Egawa N, Egawa K, Griffin H, Doorbar J (2015) Human papillomaviruses; epithelial tropisms, and the development of neoplasia. Viruses 7: 3863-3890. doi: 10.3390/v7072802 PMID: 26193301
36. Tugizov SM, Herrera R, Chin-Hong P, Veluppillai P, Greenspan D, et al. (2013) HIV-associated disruption of mucosal epithelium facilitates paracellular penetration by human papillomavirus. Virology 446: 378-388. doi: 10.1016/j.virol.2013.08.018 PMID: 24074602
37. Grivel JC, Penn ML, Eckstein DA, Schramm B, Speck RF, et al. (2000) Human immunodeficiency virus type 1 coreceptor preferences determine target T-cell depletion and cellular tropism in human lymphoid tissue. J Virol 74: 5347-5351. PMID: 10799612
38. Sasagawa T, Takagi H, Makinoda S (2012) Immune responses against human papillomavirus (HPV) infection and evasion of host defense in cervical cancer. J Infect Chemother 18: 807-815. doi: 10.1007/s10156-012-0485-5 PMID: 23117294
39. Chelliah V, Juty N, Ajmera I, Ali R, Dumousseau M, et al. (2014) BioModels: ten-year anniversary. Nucleic acids research: gku1181.
40. Funahashi A, Morohashi M, Kitano H, Tanimura N (2003) CellDesigner: a process diagram editor for gene-regulatory and biochemical networks. Biosilico 1: 159-162.
41. Shiboski CH, Lee A, Chen H, Webster-Cyriaque J, Seaman T, et al. (2016) Human papillomavirus infection in the oral cavity of HIV patients is not reduced by initiating antiretroviral therapy. Aids.
42. Mohri H, Perelson AS, Tung K, Ribeiro RM, Ramratnam B, et al. (2001) Increased turnover of T lymphocytes in HIV-1 infection and its reduction by antiretroviral therapy. The Journal of experimental medicine 194: 1277-1288. PMID: 11696593
43. Markowitz M, Louie M, Hurley A, Sun E, Di Mascio M, et al. (2003) A novel antiviral intervention results in more accurate assessment of human immunodeficiency virus type 1 replication dynamics and T-cell decay in vivo. Journal of virology 77: 5037-5038. doi: 10.1128/JVI.77.8.5037-5038.2003 PMID: 12663814
44. Klatt NR, Shudo E, Ortiz AM, Engram JC, Paiardini M, et al. (2010) CD8+ lymphocytes control viral replication in SIVmac239-infected rhesus macaques without decreasing the lifespan of productively infected cells. PLoS Pathog 6: e1000747. doi: 10.1371/journal.ppat.1000747 PMID: 20126441
45. Ciupe MS, Bivort BL, Bortz DM, Nelson PW (2006) Estimating kinetic parameters from HIV primary infection data through the eyes of three different mathematical models. Math Biosci 200: 1-27. doi: 10.1016/j.mbs.2005.12.006 PMID: 16469337
46. Ramratnam B, Bonhoeffer S, Binley J, Hurley A, Zhang L, et al. (1999) Rapid production and clearance of HIV-1 and hepatitis C virus assessed by large volume plasma apheresis. Lancet 354: 1782-1785. doi: 10.1016/S0140-6736(99)02035-8 PMID: 10577640
47. Perelson AS, Kirschner DE, De Boer R (1993) Dynamics of HIV infection of CD4+ T cells. Math Biosci 114: 81-125. PMID: 8096155
48. Beachler DC, Sugar EA, Margolick JB, Weber KM, Strickler HD, et al. (2014) Risk factors for acquisition and clearance of oral human papillomavirus infection among HIV-infected and HIV-uninfected adults. Am J of Epidemiol: kwu247.
49. D'Souza G, Fakhry C, Sugar EA, Seaberg EC, Weber K, et al. (2007) Six-month natural history of oral versus cervical human papillomavirus infection. Int J Cancer 121: 143-150. doi: 10.1002/ijc.22667 PMID: 17354235
50. Cameron JE, Mercante D, O'Brien M, Gaffga AM, Leigh JE, et al. (2005) The impact of highly active antiretroviral therapy and immunodeficiency on human papillomavirus infection of the oral cavity of human immunodeficiency virus-seropositive adults. Sex Transm Dis 32: 703-709. PMID: 16254546

<a id='3fe171c5-6760-4a32-becf-89f4c5a4e9a4'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='5ff431b4-7365-4464-9cb9-9136205d7ca0'></a>

19 / 20

<!-- PAGE BREAK -->

<a id='b6af9cdb-14d3-48ec-bdff-8b0425ac9a8e'></a>

<::A logo for PLOS ONE, featuring a stylized globe icon to the left of the text "PLOS | ONE".: figure::>

<a id='0d5ad5fa-ca8c-4e67-bab4-3d1c288bf6b7'></a>

Modeling Mechanisms by Which HIV-Associated Immunosuppression Influences HPV Persistence

<a id='1d0b120d-2612-40d8-b505-edb3eed5f000'></a>

51. Piketty C, Selinger-Leneman H, Bouvier AM, Belot A, Mary-Krause M, et al. (2012) Incidence of HIV-related anal cancer remains increased despite long-term combined antiretroviral treatment: results from the french hospital database on HIV. J Clin Oncol 30: 4360–4366. doi: 10.1200/JCO.2012.44.5486 PMID: 23091098

52. Palefsky JM, Holly EA, Efirdc JT, Da Costa M, Jay N, et al. (2005) Anal intraepithelial neoplasia in the highly active antiretroviral therapy era among HIV-positive men who have sex with men. Aids 19: 1407–1414. PMID: 16103772

53. Blitz S, Baxter J, Raboud J, Walmsley S, Rachlis A, et al. (2013) Evaluation of HIV and highly active antiretroviral therapy on the natural history of human papillomavirus infection and cervical cytopatholo-gic findings in HIV-positive and high-risk HIV-negative women. J Infect Dis 208: 454–462. doi: 10.1093/infdis/jit181 PMID: 23624362

54. Kravchenko J, Akushevich I, Sudenga SL, Wilson CM, Levitan EB, et al. (2012) Transitional probability-based model for HPV clearance in HIV-1-positive adolescent females. PloS one 7: e30736. doi: 10.1371/journal.pone.0030736 PMID: 22292027

55. d'Ettorre G, Baroncelli S, Micci L, Ceccarelli G, Andreotti M, et al. (2014) Reconstitution of Intestinal CD4 and Th17 T Cells in Antiretroviral Therapy Suppressed HIV-Infected Subjects: Implication for Residual Immune Activation from the Results of a Clinical Trial. PLoS ONE 9: e109791. doi: 10.1371/journal.pone.0109791 PMID: 25340778

56. Carbo A, Hontecillas R, Andrew T, Eden K, Mei Y, et al. (2014) Computational modeling of heterogene-ity and function of CD4+ T cells. Front Cell Dev Biol 2: 31. doi: 10.3389/fcell.2014.00031 PMID: 25364738

57. Carbo A, Hontecillas R, Kronsteiner B, Viladomiu M, Pedragosa M, et al. (2013) Systems modeling of molecular mechanisms controlling cytokine-driven CD4+ T cell differentiation and phenotype plasticity. PLoS Comput Biol 9: e1003027. doi: 10.1371/journal.pcbi.1003027 PMID: 23592971

58. Leber A, Abedi V, Hontecillas R, Viladomiu M, Hoops S, et al. (2016) Bistability analyses of CD4+ T fol-licular helper and regulatory cells during Helicobacter pylori infection. J Theor Biol 398: 74–84. doi: 10.1016/j.jtbi.2016.02.036 PMID: 26947272

59. Klatt NR, Brenchley JM (2010) Th17 cell dynamics in HIV infection. Curr Opin HIV AIDS 5: 135–140. doi: 10.1097/COH.0b013e3283364846 PMID: 20543590

60. Okoye AA, Picker LJ (2013) CD4(+) T-cell depletion in HIV infection: mechanisms of immunological fail-ure. Immunol Rev 254: 54–64. doi: 10.1111/imr.12066 PMID: 23772614

61. Sun H, Kim D, Li X, Kiselinova M, Ouyang Z, et al. (2015) Th1/17 Polarization of CD4 T Cells Supports HIV-1 Persistence during Antiretroviral Therapy. J Virol 89: 11284–11293. doi: 10.1128/JVI.01595-15 PMID: 26339043

62. Perreau M, Savoye AL, De Crignis E, Corpataux JM, Cubas R, et al. (2013) Follicular helper T cells serve as the major CD4 T cell compartment for HIV-1 infection, replication, and production. J Exp Med 210: 143–156. doi: 10.1084/jem.20121932 PMID: 23254284

63. Pallikkuth S, Sharkey M, Babic DZ, Gupta S, Stone GW, et al. (2015) Peripheral T Follicular Helper Cells Are the Major HIV Reservoir within Central Memory CD4 T Cells in Peripheral Blood from Chroni-cally HIV-Infected Individuals on Combination Antiretroviral Therapy. J Virol 90: 2718–2728. doi: 10.1128/JVI.02883-15 PMID: 26676775

64. Brenchley JM, Schacker TW, Ruff LE, Price DA, Taylor JH, et al. (2004) CD4+ T cell depletion during all stages of HIV disease occurs predominantly in the gastrointestinal tract. J Exp Med 200: 749–759. doi: 10.1084/jem.20040874 PMID: 15365096

65. Guadalupe M, Reay E, Sankaran S, Prindiville T, Flamm J, et al. (2003) Severe CD4+ T-cell depletion in gut lymphoid tissue during primary human immunodeficiency virus type 1 infection and substantial delay in restoration following highly active antiretroviral therapy. J Virol 77: 11708–11717. doi: 10.1128/JVI.77.21.11708-11717.2003 PMID: 14557656

66. Strickler HD, Burk RD, Fazzari M, Anastos K, Minkoff H, Massad LS, et al. Natural history and possible reactivation of human papillomavirus in human immunodeficiency virus-positive women. J Natl Cancer Inst. 2005; 97(8):577–86. doi: 10.1093/jnci/dji073 PMID: 15840880

67. Maglennon GA, McIntosh P, Doorbar J. Persistence of viral DNA in the epithelial basal layer suggests a model for papillomavirus latency following immune regression. Virology. 2011; 414(2):153–63. doi: 10.1016/j.virol.2011.03.019 PMID: 21492895

68. Gravitt PE. The known unknowns of HPV natural history. J Clin Invest. 2011; 121(12):4593–9. doi: 10.1172/JCI57149 PMID: 22133884

69. Rositch AF, Burke AE, Viscidi RP, Silver MI, Chang K, Gravitt PE. Contributions of recent and past sex-ual partnerships on incident human papillomavirus detection: acquisition and reactivation in older women. Cancer Res. 2012; 72(23):6183–90. doi: 10.1158/0008-5472.CAN-12-2635 PMID: 23019223

<a id='e2ca61ae-b46d-47e3-a759-3c93606a79a4'></a>

PLOS ONE | DOI:10.1371/journal.pone.0168133 January 6, 2017

<a id='b2ec8ef6-5550-4ce5-b46b-8d81b8ac9b44'></a>

20 / 20

# Supplementary materials

<a id='02489722-d8be-438d-9572-0adce664b466'></a>

## S3 File. Analytical results

We analytically investigate the properties of the co-infection model (5) at a chronic HIV steady state. As described, our model only captures the effect HIV has on HPV dynamics and, hence, we can simplify model (5) to include the four HPV equations, and constant T= 3.2x10^5 cells per

<a id='b69af675-730c-4dfe-bf33-144a33c54150'></a>

ml, $\overline{I} = \frac{c_1\overline{V}}{N_1\delta} = 2.4 \times 10^3$ cells per ml and $\overline{V} = 4.8 \times 10^4$ virions per ml, $i.e. (\overline{T}, \overline{I}, \overline{V})$ are at a steady state. We also assume $k_1=k_2=k$ as listed in Table 1. The reduced model is:

<a id='51ffb349-f794-45f4-8783-7bf6aa267b62'></a>

$$\frac{dY_1}{dt} = \psi W \frac{(1+p\overline{V})N_2-Y_1}{\varphi+(1+p\overline{V})N_2-Y_1} - \varepsilon Y_1 - \mu Y_1 - aY_1E$$
$$\frac{dY_2}{dt} = \varepsilon Y_1 + r\varepsilon Y_2 - \mu Y_2 - aY_2E$$
$$\frac{dW}{dt} = \mu(k_1Y_1 + k_2Y_2) - c_2W \quad (6)$$
$$\frac{dE}{dt} = \omega Y_2E \left(1 - \frac{E}{K}\right)$$

<a id='5f17d5b3-18da-43cc-8ce0-823fcc348b3e'></a>

System (6) has three steady states: A virus free steady state,

$S_0 = (0,0,0,E)$, (8)

<a id='ffc59a32-6f80-4ff0-a425-43f1ce371cad'></a>

a chronic immuno tolerant HPV steady state,

<a id='81512716-2397-4809-a8a9-10839abce9f0'></a>

S_I = (\tilde{Y}_1, \tilde{Y}_2, \tilde{W}, 0),                                 (9)

<a id='cd5752bc-d2e8-404b-9b15-3cddf72fc4ac'></a>

where,

<a id='88fb3587-d2bc-49b6-a0f0-44289ac62620'></a>

Y₁ = Acr(ε + μ) + Bκμψ(1-r) / -kψur + cεr + cur + kμψ'

(10)

<a id='1a647e7d-4db3-4142-928a-80239e52f245'></a>

$\widehat{Y}_{2} = \frac{-Acr(\varepsilon+\mu)+B\kappa\mu\psi(r-1)}{r(-k\psi\mu r+c\varepsilon r+c\mu r+k\mu\psi)}'$ (11)

<a id='197d6702-4941-4fdc-8f5f-5a746b622350'></a>

W̃ = μκ Acr(ε+μ)(r-1)-Bκμψ(r-1)² / rc(-kψμr+cεr+cμr+kμψ)
(12)

<!-- PAGE BREAK -->

<a id='64ad2a7c-7045-43e1-a8b0-e7455997f985'></a>

with A = (1 + p\overline{V})N_2 and B = \varphi + (1 + p\overline{V})N_2 and a chronic immuno competent HPV

<a id='cf852c3e-7d30-4674-8080-28f646251a2b'></a>

steady state,

<a id='2b143586-3cfc-4977-baca-370bfb43fc7d'></a>

S2 = (Y1, Y2, W, E),
(13)

<a id='79a6454d-94ee-403d-984a-138b6b901867'></a>

where,

$Y_1 = (\overline{A}\overline{K}^2 a^2 c + \overline{A}\overline{K}^2 ac\mu - \overline{A}\overline{K}ac\overline{\epsilon} r - \overline{B}\overline{K}ak\overline{\mu}\overline{\psi} - \overline{B}\overline{K}k\overline{\mu}^2\overline{\psi} + \overline{B}\overline{\epsilon}k\overline{\mu}\overline{\psi}r$

$+ \overline{A}\overline{K}ac\overline{\epsilon}\overline{\mu} + \overline{A}\overline{K}ac + \overline{A}\overline{K}c\overline{\epsilon}\overline{\mu} + \overline{A}\overline{K}c\overline{\mu}^2 - A\overline{c}\overline{\epsilon}^2 r - A\overline{c}\overline{\epsilon}\overline{\mu}r - \overline{B}\overline{\epsilon}k\overline{\mu}\overline{\psi}) / (\overline{K}^2 a^2 c$

$+ \overline{K}^2 ac\mu - \overline{K}ac\overline{\epsilon}r - \overline{K}ak\overline{\mu}\overline{\psi} - \overline{K}k\overline{\mu}^2\overline{\psi} + \overline{\epsilon}k\overline{\mu}\overline{\psi}r + \overline{K}a\overline{c}\overline{\epsilon} + \overline{K}ac\overline{\mu} + \overline{K}c\overline{\epsilon}\overline{\mu}$

$+ \overline{K}c\overline{\mu}^2 - \overline{c}\overline{\epsilon}^2 r - \overline{c}\overline{\epsilon}\overline{\mu}r - \overline{\epsilon}k\overline{\mu}\overline{\psi}),$ (14)

<a id='5124d869-8634-4ae9-8c51-85e31603b361'></a>

Y_2 = epsilon (bar{A}K^2 a^2 c + bar{A}K^2 a c mu - bar{A}K a c epsilon r - bar{B}K bar{a} k mu psi - bar{B}K k mu^2 psi + B epsilon k mu psi r
+ bar{A}K bar{a} c epsilon + bar{A}K bar{a} c mu + bar{A}K c epsilon mu + bar{A}K c mu^2 - A c epsilon^2 r - A c epsilon mu r - B epsilon k mu psi) / (bar{K}^3 a^3 c
+ 2bar{K}^3 a^2 c mu + bar{K}^3 a c mu^2 - 2bar{K}^2 a^2 c epsilon r - bar{K}^2 a^2 k mu psi - 2bar{K}^2 a c epsilon mu r - 2bar{K}^2 a k mu^2 psi
- bar{K}^2 k mu^3 psi + bar{K} a c epsilon^2 r^2 + 2bar{K} a epsilon k mu psi r + 2bar{K} epsilon k mu^2 psi r - epsilon^2 k mu psi r^2 + bar{K}^2 a^2 c epsilon
+ bar{K}^2 a^2 c mu + 2bar{K}^2 a c epsilon mu + 2bar{K}^2 a c mu^2 + bar{K}^2 c epsilon mu^2 + bar{K}^2 c mu^3 - 2bar{K} a epsilon^2 c r - 2bar{K} a c epsilon mu r
- bar{K} a epsilon k mu psi - 2bar{K} c epsilon^2 mu r - 2bar{K} c epsilon mu^2 r - bar{K} epsilon k mu^2 psi + c epsilon^3 r^2 + c epsilon^2 mu r^2 + epsilon^2 k mu psi r),
(15)

<a id='3c4d9d08-f284-4396-a2e4-95fdf956162e'></a>

$\bar{W} = [A c(\bar{K}^2 a^2 + \bar{K}^2 a \mu - \bar{K} a \epsilon r + \bar{K} a \epsilon + \bar{K} \epsilon \mu + \bar{K} a \mu + \bar{K} \mu^2 \\ - \epsilon^2 r - \epsilon \mu r) - B k \mu \psi (\bar{K} a + \bar{K} \mu + \epsilon - r \epsilon) \mu k](\bar{K} a + \bar{K} \mu - \epsilon r \\ + \epsilon) / c(\bar{K}^3 a^3 c + 2\bar{K}^3 a^2 c \mu + \bar{K}^3 a c \mu^2 - 2\bar{K}^2 a^2 c \epsilon r - \bar{K}^2 a^2 k \mu \psi \\ - 2\bar{K}^2 a c \epsilon \mu r - 2\bar{K}^2 a k \mu^2 \psi - \bar{K}^2 k \mu^3 \psi + \bar{K} a c r^2 \epsilon^2 + 2\bar{K} a k \epsilon \mu \psi r \\ + 2\bar{K} k \epsilon \mu^2 \Psi r - \epsilon^2 k \mu \psi r^2 + \bar{K}^2 a^2 c \epsilon + \bar{K}^2 a^2 c \mu + 2\bar{K}^2 a c \epsilon \mu + 2\bar{K}^2 a c \mu^2 \\ + \bar{K}^2 c \epsilon \mu^2 + \bar{K}^2 c \mu^3 - 2\bar{K} a c \epsilon^2 r - 2\bar{K} a c \epsilon \mu r - \bar{K} a \epsilon k \mu \psi - 2\bar{K} c \epsilon^2 \mu r \\ - 2\bar{K} c \epsilon \mu^2 r - \bar{K} \epsilon k \mu^2 \Psi + c \epsilon^2 r^2 + c \epsilon^2 \mu r^2 + \epsilon^2 k \mu \psi r),$ \\ (16)

<a id='f2d53eb9-a094-4875-a136-e8d9b76fadbc'></a>

Ē = K̄, (17)

<!-- PAGE BREAK -->

<a id='398ffe17-b2d1-4e3f-9e14-6e489a85b19d'></a>

To investigate the asymptotic stability of S₀, we compute the Jacobian for the model (6):

<::J =
$$\begin{bmatrix}
- \psi W - \frac{\varphi}{(\varphi + (1+pV)N_2 - Y_1)^2} - \varepsilon - \mu - aE & 0 & \psi \frac{(1+pV)N_2 - Y_1}{\varphi + (1+pV)N_2 - Y_1} & -aY_1 \\
\varepsilon & r\varepsilon - \mu - aE & 0 & -aY_2 \\
\mu k & \mu k & -c_2 & 0 \\
0 & \omega E(1 - \frac{E}{K}) & 0 & \omega Y_2 - 2\omega aY_2 \frac{E}{K}
\end{bmatrix}$$
(18): figure::>

<a id='0d1e93a5-ab2a-4434-9d3b-ab722111bf81'></a>

At S₀,

$J(S_0) = \begin{bmatrix}
-\varepsilon-\mu-E-\lambda & 0 & \Omega & 0 \\
\varepsilon & r\varepsilon-\mu-E-\lambda & 0 & 0 \\
\mu k & \mu k & -c_2-\lambda & 0 \\
0 & \omega E(1-\frac{E}{K}) & 0 & -\lambda
\end{bmatrix}$

(19)

<a id='4e07227e-f7a9-418f-86e1-180c435439ee'></a>

where, ψ ( (1 + pV)N₂ - Y₁ ) / ( φ + (1 + pV)N₂ - Y₁ ) = Ω The corresponding characteristic equation is:

<a id='4640c975-e1b3-4228-b56c-602b919e2c93'></a>

$$(-\lambda)[\lambda^3 + \lambda^2 (c_2 - \varepsilon r + 2aE + \varepsilon + 2\mu) + \lambda[c_2 (\varepsilon + \mu + aE) + c_2(-\varepsilon r + aE + \mu) - \Omega\mu k + (-\varepsilon - \mu - aE)(\varepsilon r - aE - \mu)] + (\varepsilon + \mu + aE)c_2 (\mu + aE - r\varepsilon) - \varepsilon\mu k\Omega] = 0. \quad (20)$$

<a id='42c2de86-0b1d-4ceb-a7e8-8b4816e6696d'></a>

We know that there is a \lambda such that \lambda= 0.

<a id='d6f4d502-5e88-4076-b4ee-ad97de08dbca'></a>

By Routh-Hurwitz criterion, all other eigenvalues are negative when a₁>0, a₃>0 and a₁a₂>a₃,
where,

<a id='fda51343-0ab6-4e8d-ba45-d92fcbb6f211'></a>

a_1 = c_2 r + 2aE + 2 , (21)

<!-- PAGE BREAK -->

<a id='b0cc2460-804e-496b-a972-9d2acdac9fb5'></a>

a₂ = c₂(ε + μ + aE) + c₂(-εr + aE + μ) - Ωμκ + (-ε - μ - aE)(εr - aE - μ),
(22)

<a id='b76116a3-6fe3-47c7-baea-e2827ac4199d'></a>

a₃ = (ε + μ + aE)c₂(μ + aE – rε) – εμκΩ. (23)

<a id='fae91f40-6701-4f9d-be36-a14be0298cd9'></a>

a₁ > 0 always since r < 1. a₃ > 0 when
$$\frac{\Omega\mu k}{c_2} < \frac{(\varepsilon + \mu + aE)(-\varepsilon r + aE + \mu)}{(\varepsilon + \mu + aE - r\varepsilon)} \quad (24)$$

<a id='cb69bc42-7cdc-4769-a1b4-ea6ef625b8cb'></a>

Finally, a1a2 - a3 > 0 when a3 >0 (not shown).

<a id='d0fa7d54-3233-4641-bfae-b830a22532c5'></a>

Condition (24) translates to

<a id='60260c69-424d-434d-9271-02cfe558e1c4'></a>

$\frac{\psi\kappa\mu(1+\overline{p}\overline{V})N_2}{c_2(\varphi+(1+\overline{p}\overline{V})N_2)} < \frac{(\varepsilon+\mu+aE)(-\varepsilon r+aE+\mu)}{(\varepsilon+\mu+aE-r\varepsilon)}$, (25)

<a id='931cd924-76fe-4b98-9810-5b865530ef38'></a>

which means that when the HPV infection rate times the HPV production rate (in the presence of HIV) is less than the combined effect of effector cells and natural death rate of HPV, HPV will be cleared. The asymptotic stability of chronic states S1 and S2 is messy and will not be presented here.

<a id='11014007-fcff-4b57-a0a8-c5b6cb56d44d'></a>

S2 File. Analysis of the coinfection model using the full model

<a id='80cd0d1b-23b8-4c3a-8f40-d8cb8751a3f3'></a>

We investigate the properties of the co-infection model using the large model developed in the original HPV work's supplementary material from Murall at al 2015. The extended model includes the population of uninfected basal epithelial cells, *X*, which are born at rate *λ(t)* and die at rate *μ*.
HPV, *W*, interacts with uninfected basal epithelial cells, *X*, at rate *ψ* to produce infected cells, *Y₁*.
We assume that the infection is density dependent with *φ* representing the uninfected cell concentration where the infection is half-maximal. Below is the expanded co-infection model wherein we included the effect of *tat*, *pV*, with the birth of uninfected basal epithelium. The term (1 + *pV*)*λ(t)* accounts for the production of epithelial cells that are susceptible for HPV infection.
The rest of the co-infection dynamics are described in the main text.

<a id='53ca808f-b1a2-41aa-9672-058bdf16a893'></a>

The expanded co-infection model becomes:

<a id='9c0ef226-eb21-40d7-8fee-3b69fc572e83'></a>

$$\frac{dT}{dt} = s - dT - (1 - \varepsilon_{RT})\beta TV,$$
$$\frac{dI}{dt} = (1 - \varepsilon_{RT})\beta TV - \delta I,$$
$$\frac{dV}{dt} = (1 - \varepsilon_{PI})N_1\delta I - c_1V,$$
$$\frac{dX}{dt} = (1 + pV)\lambda(t) - \mu X - \psi W \frac{x}{\varphi+x},$$
$$\frac{dY_1}{dt} = \psi W \frac{x}{\varphi+x} - \varepsilon Y_1 - \mu Y_1 - aY_1E,$$
$$\frac{dY_2}{dt} = \varepsilon Y_1 + r\varepsilon Y_2 - \mu Y_2 - aY_2E,$$
$$\frac{dW}{dt} = \mu k(Y_1 + Y_2) - c_2W,$$
$$\frac{dE}{dt} = \omega Y_2E \left(1 - \frac{E}{K(T)}\right) \quad (26)$$


<a id='5684c8e2-6082-473a-819a-ef006f3821b0'></a>

with initial conditions with initial conditions $T(0) > 0$, $I(0) > 0$, $V(0) > 0$, $X(0) > X_1$, $Y_1(0) = Y_{10}$,
$Y_2(0) = Y_{20}$, $W(0) = W_0$ and $E(0) = E_0$ where $t = 0$ is the time of co-infection.

<a id='ce049c4e-a736-438e-a9bf-136bf476bae8'></a>

Since, *tat* is known to play an important role in the disruption of epithelial tight junctions, thereby

<!-- PAGE BREAK -->

<a id='8ed3708c-a259-4803-ad5b-b8191f59806d'></a>

facilitating the entry of HPV into the mucosal epithelium [30]. We compare the dynamics of model (26) against those of main model (5) for the same tat effect (1+pV) = 2.

<a id='9e10effd-e482-4efc-ab73-e1264d9896e7'></a>

When considering HIV induced immunosuppression in HIV/HPV co-infected individuals with different CD4+ T cells levels of i) $\bar{T} = 10^6$ cells per ml, corresponding to a healthy patient ii) $\bar{T} = 5\times10^5$ cells per ml, corresponding to average chronic HIV CD4+ T cell numbers [41]; iii) $\bar{T} = 3.3\times10^5$ cells per ml as in the HIV/HPV co-infection study [35]; and iv) $\bar{T} = 2\times10^5$ cells per ml, corresponding to AIDS; the extended model (26) has similar results as the reduced model (5) (see (A) in Fig. S2). Similarly, when we considered the effects of co-infection under the setup of the oral co-infection trial [35] for $pV = 1$ and $K(T) = 11.5$ cells (corresponding to CD4+ T cell concentration of $\bar{T} = 3.3\times10^5$ per ml) we found that both model (6) and (26) give similar results.
In particular, HPV is cleared under cART conditions $\varepsilon_{RT} = 0.95$ and $\varepsilon_{PI} = 0.5$ and the timing of the clearance depends on two factors: the HPV stage and the level of CD4+ T cells at the start of cART (see (B) in Fig. S2).