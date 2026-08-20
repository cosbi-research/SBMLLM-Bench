<a id='bb87453c-5a3c-4382-ade7-e5030bdbe655'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='6e3e19f8-693b-49bd-8419-6642d75492d5'></a>

A Mathematical Model for the Immune-Mediated
Theory of Metastasis

<a id='4508a570-4a97-4fe0-aa41-7d710cc98aee'></a>

Adam Rhodesª,*, Thomas Hillena
ªDepartment of Mathematical and Statistical Sciences, University of Alberta, Edmonton,
Alberta, Canada

<a id='00c70a76-d413-493f-b53d-86317a3cd974'></a>

## Abstract

Accumulating experimental and clinical evidence suggest that the immune response to cancer is not exclusively _anti-tumor_. Indeed, the _pro-tumor_ roles of the immune system — as suppliers of growth and pro-angiogenic factors or defenses against cytotoxic immune attacks, for example — have been long appreciated, but relatively few theoretical works have considered their effects. Inspired by the recently proposed “immune-mediated” theory of metastasis, we develop a mathematical model for tumor-immune interactions at two anatomically distant sites, which includes both _anti-_ and _pro-tumor_ immune effects, and the experimentally observed tumor-induced phenotypic plasticity of immune cells (tumor “education” of the immune cells). Upon confrontation of our model to experimental data, we use it to evaluate the implications of the immune-mediated theory of metastasis. We find that tumor education of immune cells may explain the relatively poor performance of immunotherapies, and that many metastatic phenomena, including metastatic blow-up, dormancy, and metastasis to sites of injury, can be explained by the immune-mediated theory of metastasis. Our results suggest that further work is warranted to fully elucidate the pro-tumor effects of the immune system in metastatic cancer.

<a id='4fcd2ef8-ebb5-495f-8372-a0a0c07d3f27'></a>

Keywords: metastasis, ordinary differential equations, immune response, immunotherapies, metastatic cascade

<a id='736756a8-dea3-4be5-b528-6123e209cbae'></a>

*CAB 632, University of Alberta, Edmonton, Alberta, Canada, T6G 2G1

Email addresses: arhodes@ualberta.ca (Adam Rhodes), thillen@ualberta.ca
(Thomas Hillen)

<a id='ee5c0e05-2f01-4a41-b722-79704ae98671'></a>

Preprint submitted to Journal of Theoretical Biology                                March 1, 2019

<!-- PAGE BREAK -->

<a id='a204d6a2-de9c-49fd-9c3f-5e51d1e11e5d'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='81013263-d0e3-497c-aa63-a916854ec022'></a>

# 1. Introduction

Although metastasis is implicated in over 90% of all cancer related deaths (Gupta and Massague, 2006; Liu and Cao, 2016; Valastyan and Weinberg, 2011), a full understanding of the process remains elusive. Accumulating evidence, including the observation that patients who received peritoneovenous shunts that inadvertently released large numbers of cancer cells directly into the patients' blood stream saw no increased rate of metastasis (Tarin et al., 1984), and the immune-mediated preparation of the pre-metastatic niche (PMN) by Kaplan and collaborators (Kaplan et al., 2005), has brought into question the prevailing view of metastasis as a passive, random process. Of particular interest is the recent hypothesis that the immune system — in addition to its well-known *anti-tumor* role — plays an active *pro-tumor* role in metastatic disease Cohen et al. (2015); de Mingo Pulido and Ruffell (2016); Shahriyari (2016). Well supported by experimental and clinical observations, this hypothesis and its consequences has yet to be fully investigated. The goal of the present work is to begin this investigation through the development and analysis of a mathematical model for the immune-mediated theory of metastatic cancer. In the following section, we briefly highlight the biological evidence for this theory to justify our mathematical model, which is introduced in Section 2. We also include a short discussion of previous mathematical models of metastasis in order to contrast them against our approach.

<a id='338d2ede-3b6e-45dc-b9ce-db78d4693a9b'></a>

## 1.1. The Immune-Mediated Theory of Metastasis
A link between the immune system and cancer has been noted for a long time (Balkwill and Coussens, 2004; Walter et al., 2011), with investigators referring to tumors as "wounds that do not heal" (Dvorak, 1986, 2015) or suggesting that they are the result of an uncontrolled healing process (Meng et al., 2012). Recently, "avoiding immune destruction" and "tumor-promoting inflammation" were identified as an emerging hallmark and an enabling characteristic of cancer, respectively (Hanahan and Weinberg, 2011). More specifically, a number of authors have synthesized the accumulating evidence implicating the immune system in metastasis to formulate the immune-mediated theory of metastasis (Cohen et al., 2015; Shahriyari, 2016). In this section we present a brief summary of the relevant evidence to support this theory organized using the "metastatic cascade" framework. Within the well-used metastatic cascade framework, metastasis is seen as a sequence of

<a id='84cc379f-bae9-47be-8863-0e03cd3b4a3f'></a>

2

<!-- PAGE BREAK -->

<a id='05db2b79-87f4-467e-a105-dfac83b752f0'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='2895c7b9-b5f8-4f23-9be2-b4c6659437d7'></a>

<::Cartoon model of the immune-mediated model of metastasis. The diagram is divided into two main sections: Primary (left, green background) and Secondary (right, blue background), both situated above a blood vessel.

**Primary Section (Green Background):**
- **Top Left:** "Tumor Education" is indicated by a blue droplet, a beaker, and a graduation cap icon.
- A large, irregular mass composed of numerous orange "Cancer Cells" and some gray "Dead Cells" represents the primary tumor.
- Arrows depict processes originating from the primary tumor:
    - An arrow points right to "Immune Response Chronic Inflammation," surrounded by several asterisk-like icons representing "Cytotoxic Immune" cells.
    - An arrow points down and left, indicating "Local (1) Invasion" where cancer cells breach a green tissue layer and enter a blood vessel.
    - The entry into the vessel is labeled "(3) Intravasation" and is associated with a graduation cap icon (representing "Tumor-Educated Immune").
- Inside the blood vessel, orange cancer cells are shown flowing. The flow is indicated by an arrow and labeled "(4) Circulation."

**Secondary Section (Blue Background):**
- **Top Right:** "(2) Immune Preparation of Pre-Metastatic Niche" is shown with cytotoxic immune cells, a beaker (Growth Factors), and a graduation cap icon.
- **Top Left:** "(6) Establishment and Growth of metastasis" depicts a smaller, irregular cluster of orange cancer cells and gray dead cells, along with cytotoxic immune cells, a blue droplet (Immune Protection), and a graduation cap icon.
- **Bottom Right:** An "Injury Site" is marked by a cluster of orange and gray cells near the blood vessel.
- Arrows depict processes involving the blood vessel and secondary site:
    - Cancer cells are shown exiting the vessel into the tissue. This process is labeled "(5) Extravasation Immune homing" and is associated with a graduation cap icon.
- Inside the blood vessel, there are "Platelet-Cancer Clusters" (orange cells surrounded by smaller orange cells), cytotoxic immune cells, blue droplets, and graduation cap icons.

**Legend (Bottom of the Diagram):**
- Orange circle: "Cancer Cells"
- Gray circle: "Dead Cells"
- Cluster of small orange cells around a larger orange cell: "Platelet-Cancer cell Cluster"
- Asterisk-like icon: "Cytotoxic Immune"
- Graduation cap icon: "Tumor-Educated Immune"
- Beaker icon: "Growth Factors"
- Blue droplet: "Immune Protection" (*Based on figure from Chaffer & Weinberg (2011))
: flowchart::>
Figure 1: Cartoon model of the immune-mediated model of metastasis. Based on figure from Chaffer and Weinberg (2011).

<a id='15a5fd8b-a9c3-4372-a60d-9823cb1545d2'></a>

biological processes beginning with the development, growth, and local inva-sion of a primary tumor, and followed by the preparation of a pre-metastatic niche, entrance into, travel through, and exit from the vascular system, and concluding with the growth and development of a secondary, metastatic tu-mor. The metastatic cascade is depicted in Figure 1, with special attention paid to the immune effects at each step. We now highlight the specific im-mune cells involved at each step of the metastatic cascade and outline their roles.

<a id='8e3b5ae9-8826-4e45-bbe4-864facd7efad'></a>

Step (1): Primary Tumor Growth and Local Invasion: Before cancer can spread throughout the body, an initial _primary_ tumor must first develop (see Figure 1, (1)). Immune involvement in this stage of metastasis has long been acknowledged (Dvorak, 1986; Hanahan and Weinberg, 2011).
A large amount of research suggests that the role of the immune system in tumor progression is hardly straightforward (de Mingo Pulido and Ruffell, 2016; Erdman and Poutahidis, 2010). Indeed, while the _anti-tumor_ roles of the immune system are well known — the cytotoxic effects of natural killer (NK) cells, "classically activated" M1 macrophages, and CD8+ T cells, for example (Joyce and Pollard, 2009) — many immune cells have also been shown to play _pro-tumor_ roles in primary tumor development (de Mingo Pulido

<a id='a5a49b8a-5b80-434a-8aea-1b71d5a690aa'></a>

3

<!-- PAGE BREAK -->

<a id='99d0f904-55a9-4cff-9804-265c301b465f'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='f5b88448-712c-4ad5-a6b0-b9873b297e62'></a>

and Ruffell, 2016; Joyce and Pollard, 2009). For example, regulatory T cells (Tregs), T helper type 2 (Th₂) cells, neutrophils, and "alternatively" activated (M2) macrophages can all promote growth through inhibition of cytotoxic immune responses (Joyce and Pollard, 2009) or promotion of an- giogenesis (de Mingo Pulido and Ruffell, 2016). For extensive reviews of the specific roles played by different immune cells, please see the reviews by de Mingo Pulido and Ruffell (2016) and Joyce and Pollard (2009).

<a id='f746043c-483c-43e3-a679-a7f6662ff7f1'></a>

In addition to the contradictory anti- and pro-tumor roles played by immune cells, there is evidence suggesting that tumors can "convert" or "educate" anti-tumor cytotoxic (CT) immune cells into pro-tumor immune cells (Oleinika et al., 2013). Shahriyari (2016) has proposed that, at sites of chronic inflammation, the local immune cells become adapted to the wound healing process, resulting in increased proliferative signaling and decreased cytotoxic activity. Liu et al. (2007) have demonstrated that tumor-derived transforming growth factor (TGF) \u03b2, derived from the murine prostate tumor TRAMPC2 and renal cell carcinoma RENCA, can induce the transition of anti-tumor CD4+CD25- T cells into pro-tumor CD4+CD25+ Tregs. Such results allow for the notion of "tumor educated" (TE) immune cells (Liu and Cao, 2016); a term that will be used throughout this paper. This experimentally-validated notion of phenotypic plasticity amongst sub populations of immune cells is not entirely new, and has been considered for some time in the context of macrophages, with a continuum between anti-tumor M1 macrophages and pro-tumor M2 macrophages being proposed (Balkwill and Coussens, 2004; den Breems and Eftimie, 2016).

<a id='8672d304-4874-424b-b0ce-1a749875ba6c'></a>

**Step (2): Preparation of the Pre-Metastatic Niche:** Often, metastatic dissemination is viewed as a passive process in which cancer cells shed from the primary tumor establish metastatic tumors at sites "downstream" of the primary tumor, in locations that the circulating tumor cells (CTCs) become stuck in small vessels (Chaffer et al., 2011; Hiratsuka et al., 2006). It has been shown, however, that this model of metastasis can only account for approximately 66% of all observed patterns of metastasis (Chambers et al., 2002), suggesting that there are additional factors to consider. In an update of Paget's classic "seed and soil" hypothesis (Paget, 1989), the concept of a pre-metastatic niche (PMN) has been developed by several investigators. While the precise definition of a PMN is still being debated (Qian and Pollard, 2010), the key concept is that the PMN is a supportive *setting* in which metastatic tumors can more efficiently establish themselves, and which may (Dos Anjos Pultz et al., 2017) or may not be influenced by the primary tumor

<a id='87c880f1-cc7d-4417-8008-42efd0a298f8'></a>

4

<!-- PAGE BREAK -->

<a id='35ff9fe2-52d0-4fe8-b2fe-966ef58e9b26'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='cd884246-0ff6-407f-93af-fc1a593bf61c'></a>

itself.
Of particular interest is the implication of the immune system in the development of the PMN. Numerous cells, proteins, and factors have been implicated in the preparation of the PMN, ranging from (primary tumor associated) vascular endothelial growth factor (VEGF)-A, tumor necrosis factor (TNF) ̓ and TGF ̣ (Liu and Cao, 2016), to immuno-attractant S100 proteins (Joyce and Pollard, 2009; Kitamura et al., 2015; Qian and Pollard, 2010) and matrix-degrading MMPs (Kitamura et al., 2015), to bone marrow derived cells (BMDCs) (Coughlin and Murray, 2010; Joyce and Pollard, 2009; Kaplan et al., 2005) and platelets (Joyce and Pollard, 2009; Shahriyari, 2016) (which can produce their own pro-tumor factors). The work of Kaplan and collaborators (Kaplan et al., 2005) showed that, not only did BMDCs arrive at the site of future metastasis prior to the arrival of any cancer cells, but once cancer cells did arrive, they localized to regions of high BMDC density, suggesting a supportive role for immune cells in metastatic establishment. Further implication of the immune system in metastatic establishment comes from Shahriyari (2016), who has suggested that wound healing sites, which are naturally populated with immune cells producing growth promoting and CT immune inhibiting factors, may act as a metastasis-supporting PMN, thereby providing a possible explanation for observations of metastasis to sites of injury (Kumar and Manjunatha, 2013).

<a id='b405f585-045e-4ead-b129-26e727628a1a'></a>

Taken together, such results suggest a supportive role for the immune system in metastatic establishment, wherein the immune cells may aid in successful establishment of newly arrived cancer cell(s) by supplying growth factors (ex: platelets secreting pro-growth and angiogenic factors such as stromal-derived factor (SDF) 1 (de Mingo Pulido and Ruffell, 2016)) and protection from CT immune cells (ex: Tregs or adapted immune cells (Shahriyari, 2016)) (Figure 1 (2)).

<a id='4e261cdd-08e0-4430-9e9e-f831c377c617'></a>

**Step (3): Intravasation:** In order to establish a secondary tumor at an anatomically distant location from the primary tumor, cancer cells must travel from the primary site to the secondary site. Although cancer cells can be found in lymph nodes, it is believed that the major method of distant dissemination is through the vascular system rather than the lymphatic system (Chambers et al., 2002; Joyce and Pollard, 2009). In order to gain access to the vascular system, cancer cells, or small clusters of cancer cells (Friedl and Mayor, 2017), must leave the parenchyma and enter a blood vessel in a process called intravasation. While the precise mechanism underlying intravasation remains obscure, tumor-associated macrophages (TAMs) have

<a id='5c1b76ca-e4d7-41b5-821c-9f816e29158a'></a>

5

<!-- PAGE BREAK -->

<a id='b6240dee-6c75-46c0-8e51-4ac86a0d86cf'></a>

bioRxiv preprint doi: [https://doi.org/10.1101/565531](https://doi.org/10.1101/565531); this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='ccdacc90-3b22-406e-b969-76752fb741a4'></a>

been implicated in the process. In fact, specific studies have reported that intravasation occurred only where perivascular TAMs were located (see Joyce and Pollard (2009); Liu and Cao (2016) and references therein) (see Figure 1 (3)).

<a id='bd2181e1-9aa2-4809-9ce4-10ba6f52621f'></a>

Step (4): Circulation: Upon entrance into the blood vessel, the cancer cells are subject to a litany of new dangers, including shear forces and immune defenses (see Figure 1 (4)). It is believed that platelets play a critical role in the protection of the cancer cell clusters while in circulation. Not only can they protect from the effects of shear force by forming clumps with the cancer cells, they may also act as shields against cytotoxic immune attack from NK cells (Joyce and Pollard, 2009; Kitamura et al., 2015). While the precise role of platelets is still debated (Coupland et al., 2012; Shahriyari, 2016), it has been shown that treatments with anti-coagulant and non-steroidal anti-inflammatory drugs (NSAIDs) can significantly decrease the rates of metastasis (Joyce and Pollard, 2009; Marx, 2004).

<a id='aa7c4cd4-fe76-4404-b1e5-de74f70d8036'></a>

Step (5): Extravasation: It has been estimated that a primary tumor can shed tens of thousands of cells into the vasculature every day (Weiss, 1990). Experimental models of metastasis suggest that upwards of 80% of all those cells shed will successfully exit from the blood vessel (extravasate) at a distant secondary site (Cameron et al., 2000; Luzzi et al., 1998). As is the case with intravasation, macrophages have been implicated in the reverse process of extravasation (Kitamura et al., 2015; Liu and Cao, 2016; Qian and Pollard, 2010). In addition to the survival and growth factors (ex: TGFβ, CCL2, VEGF-A) supplied by metastasis-associated macrophages (MAMs) as the tumor cells work to exit the vessel and enter the surrounding parenchyma (see Figure 1 (5)), tumor-MAM contact has also been shown to aid in cancer cell movement through the vessel wall. Platelets have also been shown to play a pro-tumor role in this setting (Kitamura et al., 2015; Shahriyari, 2016), however they are not necessary for successful extravasation (Coupland et al., 2012). Another immune cell type that has been implicated in metastatic disease are neutrophils (Demers et al., 2012; Park et al., 2016) through the use of neutrophil extracellular traps (NETs) which can trap circulating tumor cells at a distant, hospitable site, or even increase local vascular permeability, allowing for easier extravasation of cancer cells into the surrounding parenchyma.

<a id='d4fb4538-5d6e-4fae-8b49-24bbe0ef0575'></a>

Step (6): **Metastatic Establishment**: Even though a large majority of cells shed from the primary tumor will successfully extravasate at a secondary site, less than 0.01% of them will successfully colonize a macroscopic

<a id='dd911863-72f9-46d1-a9a6-f8970c463c04'></a>

6

<!-- PAGE BREAK -->

<a id='075efa29-b7fa-453b-9d11-623bdf7835c8'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='5dd924cc-3cfe-435b-9a8e-93741e65760b'></a>

metastatic tumor (Cameron et al., 2000; Luzzi et al., 1998) (see Figure 1 (6)). The experimental results of Cameron and colleagues (Cameron et al., 2000; Luzzi et al., 1998) suggest that this precipitous drop in survival occurs after the cells transition from quiescent to proliferative states, whereby they become more vulnerable to local defenses. While this transition can occur relatively soon after initial metastatic seeding of the secondary site, it is often the case that the newly arrived cancer cells lay dormant for an extended period of time before entering a proliferative phase (Hanahan and Weinberg, 2011). A possible explanation for the low efficiency of establishment observed may be found in an effective CT immune response (Eikenberry et al., 2009). However, the immune system plays contradictory roles in this step of metastasis, with a pro-tumor response mediated by BMDCs (Hanahan and Weinberg, 2011; Joyce and Pollard, 2009) or MAMs (Kitamura et al., 2015), which provide survival and proliferation signals, or inflammatory stromal cells (Joyce and Pollard, 2009), which provide protection from the cytotoxic effects of NK cells. Additionally, immune preparation of the PMN (see previous section) may also support metastatic development, and similar pro-tumor immune effects on growth and development may be common between primary and secondary sites.

<a id='c5b25570-7191-4fb5-85ee-21baffa6d755'></a>

## 1.2. Previous Mathematical Models of Metastasis

Metastasis, with its multi-step complexity and apparent stochasticity, is relatively difficult to study experimentally. Consequently, there is a great deal of uncertainty concerning the underlying dynamics of the process. Theoretical and mathematical models of the process are therefore of significant interest as they allow for detailed theoretical investigations of the underlying processes in order to test hypotheses and guide future biological research. In this section, we present a brief summary of the most relevant mathematical descriptions of metastasis that have been previously investigated.

<a id='176ca0f3-0eb3-4611-a56f-fd218d372cb1'></a>

Focusing on the supposed stochasticity of the process, many authors have developed stochastic models for cancer metastasis. From a stochastic modeling framework, Liotta et al. (1977) derived an expression for the probability of being *metastasis-free* as a function of time from primary tumor implantation. The Michor lab has spent significant effort investigating stochastic models for the emergence of the *metastatic phenotype* (Haeno and Michor, 2010; Michor et al., 2006). The *natural history of cancer* — that is, determining dates of disease initiation, first metastasis inception, etc. from clinical data — is the focus of the stochastic models emerging from the Hanin group (Hanin

<a id='a42fe771-943f-440d-be74-f3ab04049b5a'></a>

7

<!-- PAGE BREAK -->

<a id='8b525e6f-84b8-48dc-9e88-69931ba3d754'></a>

bioRxiv preprint doi: [https://doi.org/10.1101/565531](https://doi.org/10.1101/565531); this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='982c193b-73d4-430a-be6a-f239a0b34ac5'></a>

et al., 2006; Hanin and Rose, 2018). Recently, Frei et al. (2018) introduced a spatial model for cancer metastasis that takes the form of a branching stochastic process with settlement, providing one of the first models which explicitly accounts for travel between metastatic sites.

<a id='ed1c0099-9623-4ee9-88b7-cefda93b104d'></a>

Based on their ease of analysis in comparison to stochastic models, many investigators have chosen to analyze deterministic models of metastasis. Saidel et al. (1976) introduced one of the earliest models of metastasis in the 1970s, using a simple compartmental ordinary differential equation (ODE) model that took into account the different steps in the metastatic cascade. More recently, Iwata (Iwata et al., 2000) introduced a partial differential equation (PDE) model describing the colony size distribution of metastases that takes the form of a transport equation subject to a non-local boundary condition. The Iwata model has since been adapted, analyzed, and confronted to data by several investigators — notably Benzekry and colleagues (Baratchart et al., 2015; Benzekry, 2011; Benzekry et al., 2014, 2017) — and has provided important insights into, among others, the effects of primary resection on metastatic tumor growth. To investigate the role of immune cell trafficking between metastatic sites and the so-called *abscopal effect* — in which cytotoxic treatment at one tumor site elicits an effect at a secondary site — the Enderling group has developed a model for tumor-immune interactions at multiple sites (Poleszczuk et al., 2016, 2017; Walker et al., 2018, 2017). While these works provide insight regarding tumor-immune dynamics in the metastatic setting, they are unable to provide details of the metastatic process itself. Franßen et al. (2018), on the other hand, have developed a multi-site model with spatially explicit dynamics at each of the sites that successfully captures the steps of the metastatic cascade.

<a id='6d6fb0eb-01c3-4417-b8a1-de36b26758fb'></a>

Our model builds on Kuznetsov's tumor-immune model (Kuznetsov et al., 1994) which has been the starting point for several investigators (Kuznetsov and Knott, 2001; Poleszczuk et al., 2016; Walker et al., 2018). Whereas modeling of tumor-immune dynamics has been a popular topic for some time (see the reviews in (Eftimie et al., 2011, 2016)), the number of such models that include *pro-tumor* immune effects are limited. den Breems and Eftimie (2016) incorporated M1 and M2 type macrophages in a 6-dimensional ODE model of tumor immune dynamics which included phenotypic switching between *anti-tumor* M1 macrophages and *pro-tumor* M2 macrophages. A more refined model of macrophage phenotypic plasticity was included in a more recent paper (Eftimie and Eftimie, 2018) concerning tumor-immune dynamics in the presence of an oncolytic virotherapy. Wilkie and Hahnfeldt (2017)

<a id='a4628035-9813-4447-b115-3c0f9d050b85'></a>

8

<!-- PAGE BREAK -->

<a id='40877855-35de-46b1-9f4f-67525e41c182'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='a0b8e7b3-33fb-47f8-8618-7efd6bbe5b46'></a>

have also developed a model of tumor-immune interactions that includes pro-
tumor immune effects by including an immune-dependent carrying capacity
for the tumor population. While a few models include the pro-tumor effect of
the immune response, this effect has not yet been included in a mathematical
model for metastasis, as we do here.

<a id='482d10cc-eb4c-49ed-9cb0-08fe41b03b2e'></a>

1.3. Paper Outline
Section 2 is devoted to the development and basic analysis of the two-site
model of tumor-educated immune mediated metastasis, including a subsec-
tion on parameter estimation and confrontation of the model to experimental
data (Section 2.3). Once the model has been introduced and parameterized,
we use it in Section 3 to perform three numerical experiments: simulations of
primary resection, immunotherapy, and injury at a secondary site are shown.
Model simulations demonstrate that tumor "education" of immune cells can
significantly impair the effectiveness of immunotherapies and provide a po-
tential explanation for rapid metastatic growth at the sites of injuries. We
conclude with a discussion of our results and conclusions in Section 4.

<a id='5603ade0-034d-46e5-a9b8-9a76f9320e3b'></a>

## 2. Two Site Model of Immune-Mediated Metastasis

In this section, we describe our model for tumor-immune interactions at two anatomically distant sites. The modeling assumptions and the model itself are described in Section 2.1. We present the steady states of the model, including results concerning stability, in Section 2.2, and Section 2.3 introduces the functional coefficients and the parameter values used in the simulations that are the focus of Section 3. The section concludes with a comparison of our parameterized model predictions with experimental data from Kaplan et al. (2005).

<a id='90c44911-1fd0-4fec-82e0-1f535e952c56'></a>

## 2.1. The Model

Let us assume that there are two tumor sites of interest: the *primary* site, where the initial tumor develops, and a *secondary* site where a metastatic tumor will establish and grow. At both the primary and secondary sites (subscripts $i = 1,2$, respectively) we model the time dynamics of four local cell populations: tumor cells, $u_i(t)$, necrotic cells, $v_i(t)$, cytotoxic (CT) immune cells, $x_i(t)$, and tumor-educated (TE) immune cells, $y_i(t)$. As we are modeling metastatic spread, the tumor cells of interest are those that are highly tumorigenic. Consequently, the tumor cells in our model can be interpreted

<a id='51ca9158-db28-47b6-b64d-50792737272f'></a>

9

<!-- PAGE BREAK -->

<a id='1011f685-3875-45ca-a61e-dcc502c43d6c'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='cbf04905-96cb-4b53-9729-f1c1b27d4f79'></a>

<::flowchart: The diagram illustrates a cartoon model of an 8 ODE model of metastasis, divided into 'Primary' (left, green background) and 'Secondary' (right, blue background) sections. Each section contains representations of different cell types and their interactions. The legend at the bottom clarifies the symbols: Orange circle for 'Tumor Cell', Grey circle for 'Necrotic Cell', Biohazard symbol for 'CT Immune Cell', and Graduation cap symbol for 'TE Immune Cell'. Arrows indicate positive effects, and flat ends indicate inhibitory effects. Solid lines represent direct effects, and dashed lines denote indirect influence. The diagram shows the following interactions: Within the Primary section: - Tumor cells (orange) positively influence themselves (solid arrow loop). - Tumor cells positively influence Necrotic cells (grey) (solid arrow). - Necrotic cells inhibit Tumor cells (solid flat end). - CT Immune cells (biohazard) inhibit Tumor cells (solid flat end). - Tumor cells positively influence CT Immune cells (dashed arrow). - CT Immune cells positively influence TE Immune cells (graduation cap) (solid arrow). - TE Immune cells inhibit Tumor cells (solid flat end). - Tumor cells positively influence TE Immune cells (dashed arrow). - TE Immune cells positively influence CT Immune cells (dashed arrow). Within the Secondary section: - Tumor cells (orange) positively influence themselves (solid arrow loop). - Tumor cells positively influence Necrotic cells (grey) (solid arrow). - Necrotic cells inhibit Tumor cells (solid flat end). - CT Immune cells (biohazard) inhibit Tumor cells (solid flat end). - Tumor cells positively influence CT Immune cells (dashed arrow). - CT Immune cells positively influence TE Immune cells (graduation cap) (solid arrow). - TE Immune cells inhibit Tumor cells (solid flat end). - Tumor cells positively influence TE Immune cells (dashed arrow). - TE Immune cells positively influence CT Immune cells (dashed arrow). Interactions between Primary and Secondary sections: - Primary Tumor cells positively influence Secondary Tumor cells (solid arrow). - Secondary Tumor cells positively influence Primary Tumor cells (solid arrow). - Primary CT Immune cells positively influence Secondary CT Immune cells (dashed arrow). - Secondary CT Immune cells positively influence Primary CT Immune cells (dashed arrow). - Primary TE Immune cells positively influence Secondary TE Immune cells (dashed arrow). - Secondary TE Immune cells positively influence Primary TE Immune cells (dashed arrow). - Primary Necrotic cells positively influence Secondary Necrotic cells (dashed arrow). - Secondary Necrotic cells positively influence Primary Necrotic cells (dashed arrow). Figure 2: Cartoon model of the 8 ODE model of metastasis — Equations (1) – (8). Arrows indicate *positive* effects, and flat ends indicate *inhibitory* effects. Solid lines represent *direct* effects and dashed lines denote *indirect* influence. See text for details. Color figure available online.::>

<a id='286194af-c0ec-4037-b1d2-f70da35ec7e8'></a>

as cancer stem cells (CSCs) or cells possessing the metastatic phenotype (see Section 1). In any case, we assume that a fraction, $\theta_i^{-1}$, of the tumor cells are capable of metastasizing. The full model is depicted graphically in Figure 2 and in Equations (1)-(8). The time-evolution of the eight quantities of interest in our model is governed by the following system of equations:

<a id='e95733be-6a42-4970-ae3d-27101a6986c1'></a>

$$\frac{du_1}{dt} = \gamma_1(y_1)g_1(u_1)u_1 - \sigma_1(x_1, y_1)u_1 - s_1u_1 \quad (1)$$

$$\frac{dv_1}{dt} = \theta_1\sigma_1(x_1, y_1)u_1 - \mu_1v_1 \quad (2)$$

$$\frac{dx_1}{dt} = \alpha_1 + \lambda_1(u_1, v_1)x_1 - \rho_1u_1x_1 - \omega_1x_1 - ed_1(u_1)x_1 \quad (3)$$

$$\frac{dy_1}{dt} = ed_1(u_1)x_1 - \tau_1y_1 - \tilde{s}_1y_1 + f_1(u_1)y_1 \quad (4)$$

$$\frac{du_2}{dt} = \gamma_2(y_2)g_2(u_2)u_2 - \sigma_2(x_2, y_2)u_2 + est(v_2, y_2, x_2)s_1u_1 \quad (5)$$

$$\frac{dv_2}{dt} = \theta_2\sigma_2(x_2, y_2)u_2 - \mu_2v_2 \quad (6)$$

$$\frac{dx_2}{dt} = \alpha_2 + \lambda_2(u_2, v_2)x_2 - \rho_2u_2x_2 - \omega_2x_2 - ed_2(u_2)x_2 \quad (7)$$

$$\frac{dy_2}{dt} = ed_2(u_2)x_2 - \tau_2y_2 + p\tilde{s}_1y_1 + f_2(u_2)y_2 \quad (8)$$

<a id='ce3ad657-f28b-4b74-ad38-07e2fc7f96bc'></a>

10

<!-- PAGE BREAK -->

<a id='7970518e-c21b-4567-94a5-9c7074d41ea2'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='8779505d-2e9e-4713-b956-5a8ed041da11'></a>

The equations above incorporate the following biological assumptions (for details and references, please see Sections 1 and 2.3):

*   In the absence of any immune cells, both tumor cell populations, $u_i$ ($i = 1,2$), proliferate according to the density-dependent growth rates, $g_i(u_i)$, and perish at some non-negative rate $\sigma_i(x_i, y_i)$, thereby giving rise to necrotic cells, $v_i$. CT immune cells, $x_i$, can increase this tumor cell death rate, while TE immune cells, $y_i$, can inhibit this CT immune response. Hence $\sigma_i(x_i, y_i)$ is decreasing in TE immune population, $y_i$, and increasing in CT immune population, $x_i$. In addition to their ability to suppress CT immune activity, TE immune cells can also stimulate tumor growth according to the increasing, bounded functions $\gamma_i(y_i)$.
*   Tumorigenic tumor cells are shed from the primary tumor into the surrounding vasculature proportionally to the primary tumor size with rate $s_1$. A fraction, $est(v_2, x_2, y_2)$, of these cells will successfully navigate the blood stream, arrive at the secondary location, and contribute to the development of a metastatic tumor. The fraction of such cells depends on the local immune populations at the secondary site, $x_2$ and $y_2$, in addition to the necrotic cells populating the secondary site, $v_2$. The fraction of successful cells, $est(v_2, x_2, y_2)$, is increasing in the TE immune cells, $y_2$, and necrotic cell populations, $v_2$, and decreasing in the local CT immune cell population, $x_2$. We assume that establishment is more likely in the presence of necrotic cells (Shahriyari, 2016), but not impossible in their absence.
*   At both sites ($i = 1,2$) necrotic cells arise as a consequence of tumor cell death, and are lysed at rate $\mu_i$. Assuming that the $u_i$ describe only a fraction of the total tumor burden, we include necrotic cells arising from the death of non-tumorigenic tumor cells by using the factors $\theta_i$.
*   In addition to natural CT immune cell influx rates, $\alpha_{1,2}$, both local tumor cells and necrotic cells induce CT immune responses, described by the functions $\lambda_i(v_i, x_i)$, which are increasing in both arguments. CT immune cells perish at rates $\omega_i$, and are killed in interactions with tumor cells with rates $\rho_i$. Finally, the local tumor population can induce a phenotypic transition of anti-tumor CT immune cells into pro-tumor TE immune cells. This "education" of immune cells is described by the increasing functions $ed_i(u_i)$, $i = 1, 2$.

<a id='d9ea956d-9750-4f53-b831-944d00838020'></a>

11

<!-- PAGE BREAK -->

<a id='56a76d03-c10f-46ce-8715-a4b7aa5933aa'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='d776b1f8-9fcc-45ad-a5ee-05e97491c57b'></a>

- In the absence of a tumor population at the primary site, there will be no TE immune cells. However, once a tumor is established at the primary site, TE immune cells can accumulate at the primary site in two ways: (1) by means of a tumor-induced phenotypic transition between CT and TE immune cell populations, and (2) by direct tumor recruitment of pro-tumor immune cells governed by the function $f_i(u_i)$, $i = 1, 2$. The TE immune population at the primary site can decrease through natural death at rate $\tau_1$, or through loss into the circulatory system at rate $\tilde{s}_1$.
- A fraction, $p$, of those TE immune cells shed from the primary site arrive at the secondary site to supplement the previously described methods of TE immune cell accumulation \textemdash namely tumor "education" of CT immune cells and tumor-mediated recruitment. TE immune cells at the secondary site perish at rate $\tau_2$.
- We have assumed that the only significant shedding events occur from the primary site, a choice justified by previous theoretical work showing that shedding from the secondary site had negligible effects on the observed dynamics (Hartung et al., 2014).

<a id='f9c61f61-d521-4e7f-9e83-082e6b868897'></a>

## 2.2. Steady States
We quickly summarize the steady states of model (1)-(8) and their stability, without presenting the details of the analysis. Three different steady state expressions characterize the model:

1. A disease-free steady state, given by

$$(u_1, v_1, x_1, y_1, u_2, v_2, x_2, y_2) = \left(0, 0, \frac{\alpha_1}{\omega_1}, 0, 0, 0, \frac{\alpha_2}{\omega_2}, 0\right).\quad(9)$$

2. A metastatic-only steady state, given by

$$(u_1, v_1, x_1, y_1, u_2, v_2, x_2, y_2) = \left(0, 0, \frac{\alpha_1}{\omega_1}, 0, \bar{u}_2, \bar{v}_2, \bar{x}_2, \bar{y}_2\right),\quad(10)$$

where the barred values (when they exist) are defined by the following

<a id='ea5ed539-b948-47fc-b86d-ff4c0e26c070'></a>

12

<!-- PAGE BREAK -->

<a id='caa12aa9-06ca-4bd4-96ee-19cd1837a594'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='51fad886-5401-4bb7-a754-f2fbf5922b10'></a>

equations:

$g_2(\bar{u}_2) = \frac{\sigma_2(\bar{x}_2, \bar{y}_2)}{\gamma_2(\bar{y}_2)}$,

$\bar{v}_2 = \frac{\theta_2}{\mu_2} \sigma_2(\bar{x}_2, \bar{y}_2) \bar{u}_2$,

$\bar{y}_2 = \frac{ed_2(\bar{u}_2)\bar{x}_2}{\tau_2 - f_2(\bar{u}_2)}$

$\bar{x}_2 = \frac{-\alpha_2}{\lambda_2(\bar{u}_2, \bar{v}_2) - \rho_2\bar{u}_2 - \omega_2 - ed_2(\bar{u}_2)}$

(11)

<a id='02214a95-54f7-4d2c-a7dd-28a4c606368a'></a>

3. And a full-disease steady state expression, given by

$(u_1, v_1, x_1, y_1, u_2, v_2, x_2, y_2) = (\tilde{u}_1, \tilde{v}_1, \tilde{x}_1, \tilde{y}_1, \tilde{u}_2, \tilde{v}_2, \tilde{x}_2, \tilde{y}_2)$ (12)

<a id='f0c2df9f-54a2-4a2b-a09c-413cead713d5'></a>

where the values on the RHS (when they exist) are defined by the
following equations,

<a id='e4a5bbc5-4576-4f56-8cc5-3b0d0c94c5ee'></a>

$$g_1(\tilde{u}_1) = \frac{\sigma_1(\tilde{x}_1, \tilde{y}_1) + s_1}{\gamma_1(\tilde{y}_1)}, \quad \tilde{v}_1 = \frac{\theta_1}{\mu_1}\sigma_1(\tilde{x}_1, \tilde{y}_1)\tilde{u}_1$$

$$\tilde{x}_1 = \frac{-\alpha_1}{\lambda_1(\tilde{u}_1, \tilde{v}_1) - \rho_1\tilde{u}_1 - \omega_1 - ed_1(\tilde{u}_1)}, \quad \tilde{y}_1 = \frac{ed_1(\tilde{u}_1)\tilde{x}_1}{\tau_1 + s_1 - f_1(\tilde{u}_1)}$$

$$\tilde{u}_2 = \frac{est(\tilde{v}_2, \tilde{y}_2, \tilde{x}_2)s\tilde{u}_1}{\sigma_2(\tilde{x}_2, \tilde{y}_2) - \gamma_2(\tilde{y}_2)g_2(\tilde{u}_2)}, \quad \tilde{v}_2 = \frac{\theta_2}{\mu_2}\sigma_2(\tilde{x}_2, \tilde{y}_2)\tilde{u}_2$$

$$\tilde{x}_2 = \frac{-\alpha_2}{\lambda_2(\tilde{u}_2, \tilde{v}_2) - \rho_2\tilde{u}_2 - \omega_2 - ed_2(\tilde{u}_2)}, \quad \tilde{y}_2 = \frac{ed_2(\tilde{u}_2)\tilde{x}_2 + ps_1\tilde{y}_1}{\tau_2 - f_2(\tilde{u}_2)}. \quad (13)$$

<a id='69933298-c3c2-4081-bad9-506ba005041e'></a>

Representative solutions of the model illustrating the three different steady states are shown in Figure 3. Explicit conditions to ensure the stability of the disease-free and metastatic-only steady states are obtained, and presented in the following proposition.

<a id='02432e92-de58-4579-ba90-240c08fc245e'></a>

Proposition 2.1. If

$g_1(0) < s_1 + \sigma_1 \left( \frac{\alpha_1}{\omega_1}, 0 \right)$,

<a id='c4949ce5-488d-470e-a9c4-31b714726700'></a>

then extinction of the primary tumor is stable. Further, the disease-free steady state is stable if and only if both

$g_1(0) < s_1 + \sigma_1 \left(\frac{\alpha_1}{\omega_1}, 0\right)$

<a id='8b8d6a53-dabf-419b-ae6e-aeafd51fce02'></a>

13

<!-- PAGE BREAK -->

<a id='82ee6190-e6e2-4662-bd98-a97e75193567'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='543fe9b5-8256-41f2-8ecf-a77c82c4b37d'></a>

A<::chart: Two line plots side-by-side, labeled 'A'. The left plot is titled 'Primary' and the right plot is titled 'Secondary'. Both plots show 'Number of Cells' on the y-axis against 'Time' on the x-axis. The legend for both plots is: -Tumor Cells (black dashed line), ---Necrotic Cells (red dashed line), ...CT Immune Cells (blue dotted line), -TE Immune Cells (green solid line). In the 'Primary' plot, Number of Cells ranges from 0 to 10, and Time from 0 to 400. Tumor Cells, Necrotic Cells, and TE Immune Cells initially rise and then decrease to near zero, while CT Immune Cells remain at a high level (around 8-9). In the 'Secondary' plot, Number of Cells ranges from 0 to 8, and Time from 0 to 400. All cell types except CT Immune Cells decrease to near zero, while CT Immune Cells remain at a high level (around 8).::>B<::chart: Two line plots side-by-side, labeled 'B'. The left plot is titled 'Primary' and the right plot is titled 'Secondary'. Both plots show 'Number of Cells' on the y-axis against 'Time' on the x-axis. The legend for both plots is: -Tumor Cells (black dashed line), ---Necrotic Cells (red dashed line), ...CT Immune Cells (blue dotted line), -TE Immune Cells (green solid line). In the 'Primary' plot, Number of Cells ranges from 0 to 10, and Time from 0 to 400. Tumor Cells, Necrotic Cells, and TE Immune Cells initially rise and then decrease to near zero, while CT Immune Cells remain at a high level (around 8-9). In the 'Secondary' plot, Number of Cells ranges from 0 to 6 x 10^8, and Time from 0 to 400. CT Immune Cells start at a high level (around 2 x 10^8) and then decrease. Tumor Cells and Necrotic Cells remain low for a period, then rise sharply around Time 300, peaking around 5 x 10^8, and then decrease. TE Immune Cells also rise and fall, peaking later than Tumor and Necrotic Cells.::>C<::chart: Two line plots side-by-side, labeled 'C'. The left plot is titled 'Primary' and the right plot is titled 'Secondary'. Both plots show 'Number of Cells' on the y-axis (log scale from 10^-15 to 10^10) against 'Time' on the x-axis (0 to 400). The legend for both plots is: -Tumor Cells (black dashed line), ---Necrotic Cells (red dashed line), ...CT Immune Cells (blue dotted line), -TE Immune Cells (green solid line). In the 'Primary' plot, Tumor Cells, Necrotic Cells, and TE Immune Cells all increase and stabilize at high levels (around 10^5-10^6). CT Immune Cells start high, decrease, and then stabilize at a lower level (around 10^0). In the 'Secondary' plot, Tumor Cells, Necrotic Cells, and TE Immune Cells all increase and stabilize at high levels (around 10^5-10^6). CT Immune Cells start high, decrease, and then stabilize at a lower level (around 10^0).::>Figure 3: Solutions of the model (1) – (8) illustrating the three qualitatively different steady states. Left column: dynamics at the primary site. Right column: dynamics at the secondary site. Colors as indicated. Convergence to A: disease-free steady state. B: metastatic-only steady state. C: full disease steady state. Parameters from Table 1 used in C, and appropriately modified parameters used in A and B according to the conditions in Proposition 2.1. Color figure available online.

<a id='47ce47ce-9ec5-4aa1-8b69-9c95d3f0b6b7'></a>

14

<!-- PAGE BREAK -->

<a id='2734fe28-766d-49e8-9d36-803554341074'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='acc8429e-73fd-4db0-bc4d-2b1afa6c4912'></a>

and                                                      g2(0) < σ2(α2/ω2, 0)

are satisfied.

<a id='63ad2e6f-c50f-439b-aba8-31e8abbdd758'></a>

**Remark 2.2.** *Note that the expressions for many of the non-trivial steady states have denominators which could potentially change signs. In order for these values to be biologically relevant, we insist on non-negativity of all the steady state expressions. In particular, the denominators cannot be allowed to change signs in our domains of interest. Using the literature-derived parameter estimates in Table 1 this requirement is satisfied.*

<a id='b6049917-c748-4342-bd96-d8c04634b638'></a>

2.3. Parameter Estimation
Numerical exploration of the model necessitates that certain choices are made for the general functional coefficients in the model (1)-(8). In this section, we make our choices and parameterize the resulting model. As a simplifying generalization, we have assumed, as have others (Poleszczuk et al., 2016), that many of the model parameter values are shared between primary and secondary sites. This assumption is almost certainly incorrect (Hanin and Rose, 2018), but as a first approximation we contend it suffices. Table 1 summarizes the parameter values used in this paper together with appropriate references (where applicable).

<a id='a6cf356c-d75f-486a-ba34-bdb6f0ed75ba'></a>

* Tumor cell growth rates, $g_i(u_i)$, $i = 1,2$, are chosen to be of logistic type,

<a id='92d18ba8-5eac-4561-99e2-1c7d81c825a8'></a>

g_i(u_i) = r_i (1 - u_i / K_i),

<a id='9d4e1eaa-e103-4db5-a027-077dd8a110c8'></a>

where $r_i$ and $K_i$ are growth rates and carrying capacities at sites $i =$
1,2, respectively. Whereas we recognize that logistic growth is not
the ideal choice for modeling tumor growth dynamics in the metastatic
setting (Hartung et al., 2014), we have chosen to assume logistic growth
to mirror the choices of other investigators (den Breems and Eftimie,
2016; Eftimie and Eftimie, 2018; Kuznetsov et al., 1994; Poleszczuk and
Enderling, 2016). In the simulations presented below, we have used
tumor growth rates and carrying capacities determined in Kuznetsov
and Knott (2001) by fitting experimental data, and which were used
again in more recent work in the setting of abscopal effects (Poleszczuk
et al., 2016).

<a id='aeca6a69-cb8c-40c8-b5e2-f63644365900'></a>

15

<!-- PAGE BREAK -->

<a id='38caac09-04cd-42a5-a5ee-ba2a7dc0b873'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='a22542b4-71d1-4d29-a634-571604d890cb'></a>

* Tumor cell death rates, σ₋(x₋, y₋), are chosen to be a product of "switch-like" hyperbolic tangent functions as used by Olobatuyi et al. (2017). We include both an *increasing* version:

v(x; m, M, A, S) =

$\frac{M}{2} \left[ \tanh \left( \frac{6}{S - A} \left( x - \frac{S + A}{2} \right) \right) - \tanh \left( \frac{-3(S + A)}{S - A} \right) \right] + m, \quad (14)$

<a id='92de808a-1b8c-4c23-bbac-2977589f37b6'></a>

which increases from $m$ at $x=0$ to $m+M$ as $x\rightarrow\infty$, and a decreasing version:

$\xi(x;m,M,A,S)=
\frac{M(1-\tanh(\frac{6}{S-A}(x-\frac{S+A}{2})))+m(\tanh(\frac{6}{S-A}(x-\frac{S+A}{2}))-\tanh(\frac{-3(S+A)}{S-A})))}{1-\tanh(\frac{-3(S+A)}{S-A})},
(15)$

<a id='a15c382d-08e4-4e54-98f9-143ce84a4826'></a>

which decreases from $m+M$ at $x = 0$ to $m$ as $x \to \infty$. Both of these "switch-like" functions can be specifically tuned using four parameters: activation ($A$) and saturation ($S$) thresholds together with lower ($m$) and upper ($m + M$) bounds on the domain $[0,\infty)$. The tumor cell death rates are then chosen as the product

<a id='43ede269-66a5-46ce-9ddd-d74ac82d8178'></a>

$\sigma_i(x_i, y_i) = \nu(x_i; minC_i, maxC_i, upC_i, lowC_i)\xi(y_i; 0, 1, upD_i, lowD_i),$

<a id='57f094d4-eb5e-41be-8314-d54139743dea'></a>

which increases in the CT immune cell populations, $x_i$, and decreases in the TE immune cell populations, $y_i$, $i = 1, 2$. The only parameter in this function that we were able to estimate from the literature is the minimum death rates, $minC_i$, with the estimate coming from previous theoretical investigations (Orlando et al., 2013; Saidel et al., 1976). All remaining parameters were estimated conservatively, for example, most CT immune cell thresholds were chosen to be 15% (activation) and 65% (saturation) of the disease-free steady state value of CT immune cells ($\frac{\alpha_i}{\omega_i}$, $i = 1, 2$, which was chosen to be of the order $10^6$ cells by tuning the parameters $\alpha_i$ (den Breems and Eftimie, 2016; Negus et al., 1997; Steidl et al., 2010)), and TE immune cell thresholds were then chosen to be an order of magnitude lower than those for CT immune cells.

<a id='b63168f2-86a6-48d4-b37b-e8b9dfdc4e09'></a>

To model tumor and necrotic cell mediated immune cell expansion, we use the successful Michaelis-Menten type function which is a popular choice in tumor-immune models (Eftimie et al., 2011, 2016; Kuznetsov

<a id='0003e665-5003-4f62-8d5f-fdd6beae2447'></a>

16

<!-- PAGE BREAK -->

<a id='56059a9c-e8f3-45f9-ac0d-a90ab07da05f'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='6aff0761-68d7-4d57-a8da-0901e3b61443'></a>

et al., 1994; Poleszczuk et al., 2016). As a consequence of their ubiq-
uity, estimates have been made by several authors for the associated
CT immune cell parameters. We have assumed that CT immune cell
recruitment by tumor cells and necrotic cells is *additive*, i.e.

<a id='adcc8d20-40ca-489f-9afe-b3eb22f3a123'></a>

\lambda_i (u_i, v_i) = \left( \frac{a_{1i} u_i}{b_{1i} + u_i} \right) + \left( \frac{a_{2i} v_i}{b_{2i} + v_i} \right).

<a id='6ee4d298-89d3-4b5a-be79-5c72193cd3af'></a>

We have also included tumor-mediated recruitment of TE immune cells
using the standard Michaelis-Menten type functions,

<a id='952046d8-4889-4b95-bfde-6482c11ea7ae'></a>

<::f_i(u_i) = \frac{a_{3i}u_i}{b_{3i} + u_i}.:figure::>

<a id='7ac3dd93-f5b3-4618-ac19-19e144f46093'></a>

Whereas CT immune cell related parameters were easily found in the literature, no such estimates exist (to the authors' knowledge) for TE immune cells. As a consequence, we have estimated the TE immune parameters by scaling the corresponding CT immune cell parameters by up to an order of magnitude.

<a id='3e419522-712c-4350-b3e0-36fe7c0b888e'></a>

• Due to its relatively recent experimental discovery, there has been little work done attempting to elucidate the precise mechanisms underlying the tumor-mediated phenotypic plasticity, or "education", of CT immune cells. As a result, the only relevant literature from which we can inform our model is the theoretical work of den Breems and Eftimie (den Breems and Eftimie, 2016), in which the authors use mass-action kinetics to describe the tumor "education" of CT immune cells. Following this approach allows us to choose

$ed_i(u_i) = \chi_i u_i$

<a id='c87f4a21-009e-4ebc-abd3-86b069448d79'></a>

for some non-negative rate constants \(\chi_i\), \(i = 1,2\). In the absence of additional evidence, we have chosen to use den Breem and Eftimie's "polarization" rate as our "education" rate (den Breems and Eftimie, 2016; Kim et al., 2017). For further discussion, see Section 4.

<a id='5c130b66-cdeb-4904-b6e8-b4a3010c53a8'></a>

 - To model the TE immune cell enhancement of tumor growth, we have used the increasing hyperbolic tangent functions (14)

<a id='9764b80a-5152-4743-859f-4111ef5f6e60'></a>

\gamma_i(u_i) = \nu(u_i; 1, max_i, low_i, up_i).

<a id='7e3947b3-e5b0-4c5e-a4e9-c3b30a083958'></a>

Thresholds were chosen as discussed previously, and we have assumed
that TE immune cells could increase the tumor cell growth rate by at
most 50%.

<a id='7ea6a685-814b-4226-8ceb-210ba787447f'></a>

17

<!-- PAGE BREAK -->

<a id='13317b6a-6d56-4f74-b200-957dea834b0c'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='c48118a3-9f82-4f20-a80c-2f638f0490f4'></a>

* Finally, we choose a model for the establishment of circulating tumor cells at the secondary site. Based on the evidence discussed in Section 1 we use

<a id='0e6fcf26-7170-4f3d-bea8-fdfbf3f452ce'></a>

est(v_2, x_2, y_2) = \nu(v_2; min_V, max_V, low_V, up_V)
\times \xi(x_2; 0, max_{CT}, lowEst_{CT}, upEst_{CT})
\times \nu(y_2; minEst_{TE}, maxEst_{TE}, lowEst_{TE}, upEst_{TE}).

<a id='c069e018-9609-488a-bfac-272cfd263597'></a>

Immune cell thresholds were chosen as above, while the necrotic cell thresholds were chosen to be 5% and 55% of the tumor carrying capacities K_i. Estimates of the rates involved have been informed by both previous experimental evidence (Cameron et al., 2000; Chambers et al., 2002; Gorelik, 1983; Joyce and Pollard, 2009; Mehlen and Puisieux, 2006) and the authors' estimates.

<a id='a1603198-0846-405f-8475-792201a5a811'></a>

The above discussion is summarized in Table 1, where the parameter values used in Section 3 are summarized with references (where applicable).

<a id='c40ec837-51c8-4c3d-8fad-31d985add865'></a>

The initial conditions for all presented results (with the exceptions of
Figure 3 A and B, where the number of tumor cells at the primary site as
chosen to be larger for purposes of illustration) were chosen to be

<a id='46530d6e-9372-425d-8f68-5683aa612e45'></a>

$$(u_1(0), v_1(0), x_1(0), y_1(0), u_2(0), v_2(0), x_2(0), y_2(0)) = \left(1, 0, \frac{\alpha_1}{\omega_1}, 0, 0, 0, \frac{\alpha_2}{\omega_2}, 0\right),$$

<a id='1c926aca-e513-4791-bb8b-9fe3febb8d05'></a>

representing a slight perturbation of the disease-free steady state in which a single tumor cell has developed at the primary site. This choice allows for the inclusion of a time-dependent source of circulating tumor cells coming from the growing primary tumor --- dynamics that are often neglected in injection (Cameron et al., 2000) or simulation (Eikenberry et al., 2009; Walker et al., 2018) studies.

<a id='bbb195e2-0b22-49ce-b3fa-b4cb15d6e64c'></a>

As an initial validation of both the model and the chosen parameter values, we compare the calibrated model's predicted dynamics at the secondary site with those observed experimentally by Kaplan et al. (2005). Following intradermal injection of 2 × 10^6 Lewis lung carcinoma (LLC) cells into murine flanks, Kaplan and colleagues measured the proportions of pro-tumor BMDCs and tumor cells at the metastatic site (lungs) at several time points (Figure 4, A (Figure 1 c in Kaplan et al. (2005))). As can be seen in Figure 4 (A) pro-tumor BMDCs arrived at the site of future metastasis well before the arrival of any tumor cells. Our model successfully captures this phenomenon, as seen in Figure 4 (B), with pro-tumor TE immune cells arriving

<a id='73541411-8bf8-4dc0-b718-ad457f2eb0fa'></a>

18

<!-- PAGE BREAK -->

<a id='364e6052-02a6-4d33-ad52-5fe904c8f978'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='60a2e3cb-bfaa-4ae3-9091-64141b9e8186'></a>

at the future metastatic site in advance of any significant tumor colonization. Furthermore, our model accurately captures the approximate scales of this colonization, both in terms of magnitude (peaks of approximately 30% and 10% for BMDCs and tumor cells, respectively) and timing (approximately 2 weeks from initial colonization to tumor cell takeover).

<a id='efb79f18-9e16-47bc-933e-50a824b4a00f'></a>

There are, however, two shortcomings of this comparison. First, in our simulation, the primary tumor reaches a size of approximately 2 × 10<sup>6</sup> cells (matching the size of the injection used by Kaplan et al. (2005)) after 84 days, meaning that the delay to the dynamics presented in Figure 4 is approximately 120 days. While this shortcoming may appear problematic, it may simply be a consequence of the differences between the details of the experiment and the simulation. Second, the *shape* of the pro-tumor immune curve in the experimental data --- and the location of the peak, in particular --- is not well approximated by our simulation results, with the simulated peak occurring much *earlier* than the experimentally observed peak. Although these are both important shortcomings, we note that the data from Kaplan et al. (2005) was not used in the calibration of our model. Consequently, some inconsistencies may be reasonably expected, and we contend that the successes described previously --- those of *order* of arrival and general scales being well approximated --- are sufficient to claim that the parameters in Table 1 are biologically feasible and that the qualitative results of the calibrated model reflect the true biology.

<a id='9f67f517-0043-492b-83bb-b0b63edc1677'></a>

### 3. Model Simulations

Now that we have used experimental evidence and previous literature-derived estimates to specify the model parameters, and we have confirmed that these parameters can accurately reproduce experimental results (Figure 4), we perform three clinically relevant numerical simulations of the model in order to further investigate the implications of the immune-mediated theory of metastasis. This section investigates the effects of primary resection, immune therapies, and injury at the secondary site on disease progression.

<a id='a3d65b55-a4d0-4c72-9b15-8cdd2dc85619'></a>

### 3.1. Primary Resection
When possible, surgical removal (resection) of a tumor can be the preferred method of treatment. Unfortunately, this treatment is not always effective and may only offer temporary relief, with local recurrence or metastatic

<a id='c5946d34-8797-4730-a879-c5ded4842522'></a>

19

<!-- PAGE BREAK -->

<a id='937d9a71-bb5c-4a16-88a9-7b191e609024'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='e6ee9b11-1da9-4802-998d-416237a19f53'></a>

<table id="19-1">
<tr><td id="19-2">Parameter</td><td id="19-3">Description</td><td id="19-4">Value</td><td id="19-5">Units</td><td id="19-6">References</td></tr>
<tr><td id="19-7">r₁,₂</td><td id="19-8">tumor growth rate</td><td id="19-9">0.38</td><td id="19-a">1/day</td><td id="19-b">Poleszczuk et al. (2016)</td></tr>
<tr><td id="19-c">K₁,₂</td><td id="19-d">tumor carrying capacity</td><td id="19-e">5.3196 × 10⁸</td><td id="19-f">cells</td><td id="19-g">Poleszczuk et al. (2016)</td></tr>
<tr><td id="19-h">θ₁,₂</td><td id="19-i">CSC scaling constant</td><td id="19-j">65.67</td><td id="19-k">—</td><td id="19-l">Enderling (2015); Rhodes and Hillen (2016)</td></tr>
<tr><td id="19-m">μ₁,₂</td><td id="19-n">dead cell lysis rate</td><td id="19-o">0.01, 0.05</td><td id="19-p">1/day</td><td id="19-q">Eikenberry et al. (2009); Robertson-Tessi et al. (2015)</td></tr>
<tr><td id="19-r">α1,2</td><td id="19-s">CT immune influx rate</td><td id="19-t">1 × 106</td><td id="19-u">1/day</td><td id="19-v">Eikenberry et al. (2009)</td></tr>
<tr><td id="19-w">ρ1,2</td><td id="19-x">fatal immune-tumor interaction rate</td><td id="19-y">0.001, 0.01</td><td id="19-z">1/day</td><td id="19-A">Eikenberry et al. (2009)</td></tr>
<tr><td id="19-B">ω1,2</td><td id="19-C">CT decay rate</td><td id="19-D">0.59</td><td id="19-E">1/day</td><td id="19-F">Poleszczuk et al. (2016)</td></tr>
<tr><td id="19-G">χ1,2</td><td id="19-H">immune education rate</td><td id="19-I">5 × 10-5</td><td id="19-J">1/day</td><td id="19-K">den Breems and Eftimie (2016); Kim et al. (2017)</td></tr>
<tr><td id="19-L">τ1,2</td><td id="19-M">TE decay rate</td><td id="19-N">0.05</td><td id="19-O">1/day</td><td id="19-P">Eikenberry et al. (2009)</td></tr>
<tr><td id="19-Q">s₁</td><td id="19-R">tumor shedding rate</td><td id="19-S">0.01</td><td id="19-T">1/day</td><td id="19-U">Gupta and Massague (2006); Joyce and Pollard (2009)</td></tr>
<tr><td id="19-V">s̃₁</td><td id="19-W">TE shedding rate</td><td id="19-X">0.05</td><td id="19-Y">1/day</td><td id="19-Z">Eikenberry et al. (2009)</td></tr>
<tr><td id="19-10">p</td><td id="19-11">proportion successful TE</td><td id="19-12">1 × 10⁻⁴</td><td id="19-13">—</td><td id="19-14">—</td></tr>
<tr><td id="19-15">max₁,₂</td><td id="19-16">max (increase) TE growth</td><td id="19-17">0.5</td><td id="19-18">—</td><td id="19-19">—</td></tr>
<tr><td id="19-1a">low₁,₂</td><td id="19-1b">growth activation</td><td id="19-1c">25424</td><td id="19-1d">cells</td><td id="19-1e">—</td></tr>
<tr><td id="19-1f">up_{1,2}</td><td id="19-1g">growth saturation</td><td id="19-1h">110169</td><td id="19-1i">cells</td><td id="19-1j">—</td></tr>
<tr><td id="19-1k">low D_{1,2}</td><td id="19-1l">death activation: TE</td><td id="19-1m">25424</td><td id="19-1n">cells</td><td id="19-1o">—</td></tr>
<tr><td id="19-1p">upD_{1,2}</td><td id="19-1q">death saturation: TE</td><td id="19-1r">110169</td><td id="19-1s">cells</td><td id="19-1t">—</td></tr>
<tr><td id="19-1u">minC_{1,2}</td><td id="19-1v">min death rate</td><td id="19-1w">0.2</td><td id="19-1x">1/day</td><td id="19-1y">Orlando et al. (2013); Saidel et al. (1976)</td></tr>
<tr><td id="19-1z">maxC_{1,2}</td><td id="19-1A">max increase death</td><td id="19-1B">0.1</td><td id="19-1C">1/day</td><td id="19-1D">—</td></tr>
<tr><td id="19-1E">lowC12</td><td id="19-1F">death activation: CT</td><td id="19-1G">254237</td><td id="19-1H">cells</td><td id="19-1I">---</td></tr>
<tr><td id="19-1J">upC12</td><td id="19-1K">death saturation: CT</td><td id="19-1L">1101695</td><td id="19-1M">cells</td><td id="19-1N">---</td></tr>
<tr><td id="19-1O">@11.12</td><td id="19-1P">CT expansion: tumor</td><td id="19-1Q">0.524</td><td id="19-1R">1/day</td><td id="19-1S">Kuznetsov and Knott (2001)</td></tr>
<tr><td id="19-1T">021,22</td><td id="19-1U">CT expansion: dead</td><td id="19-1V">0.786</td><td id="19-1W">1/day</td><td id="19-1X">---</td></tr>
<tr><td id="19-1Y">1,12,21,22</td><td id="19-1Z">immune damping (dead;tumor)</td><td id="19-20">1.61 x 105</td><td id="19-21">cells</td><td id="19-22">Kuznetsov and Knott (2001)</td></tr>
<tr><td id="19-23">a31,32</td><td id="19-24">TE expansion rate</td><td id="19-25">0.04</td><td id="19-26">1/day</td><td id="19-27">Kuznetsov and Knott (2001); Poleszczuk et al. (2016)</td></tr>
<tr><td id="19-28">b31,32</td><td id="19-29">TE expansion damping</td><td id="19-2a">1.6 × 105</td><td id="19-2b">cells</td><td id="19-2c">Kuznetsov and Knott (2001); Poleszczuk et al. (2016)</td></tr>
<tr><td id="19-2d">maxCT</td><td id="19-2e">max (increase) establish rate</td><td id="19-2f">100</td><td id="19-2g">—</td><td id="19-2h">Gorelik (1983)</td></tr>
<tr><td id="19-2i">lowEstCT,TE</td><td id="19-2j">activation level: establish</td><td id="19-2k">254237,25424</td><td id="19-2l">cells</td><td id="19-2m">—</td></tr>
<tr><td id="19-2n">upEstCT,TE</td><td id="19-2o">saturation level: establish</td><td id="19-2p">1101695, 110169</td><td id="19-2q">cells</td><td id="19-2r">—</td></tr>
<tr><td id="19-2s">min Est_{TE}</td><td id="19-2t">min establish rate</td><td id="19-2u">0.001</td><td id="19-2v">1/day</td><td id="19-2w">Cameron et al. (2000); Chambers et al. (2002); Joyce and Pollard (2009); Mehlen and Puisieux (2006)</td></tr>
<tr><td id="19-2x">max Est_{TE}</td><td id="19-2y">max establish rate (increase)</td><td id="19-2z">0.002</td><td id="19-2A">1/day</td><td id="19-2B">—</td></tr>
<tr><td id="19-2C">low_{V}</td><td id="19-2D">activation: dead cells</td><td id="19-2E">2.66 × 10^{7}</td><td id="19-2F">cells</td><td id="19-2G">—</td></tr>
<tr><td id="19-2H">up_{V}</td><td id="19-2I">saturation: dead cells</td><td id="19-2J">2.93 × 10^{8}</td><td id="19-2K">cells</td><td id="19-2L">—</td></tr>
<tr><td id="19-2M">min_{V}</td><td id="19-2N">min establish rate</td><td id="19-2O">0.001</td><td id="19-2P">1/day</td><td id="19-2Q">—</td></tr>
<tr><td id="19-2R">maxy</td><td id="19-2S">max establish rate (increase)</td><td id="19-2T">0.999</td><td id="19-2U">1/day</td><td id="19-2V">—</td></tr>
</table>

<a id='38686fc5-55c7-451a-8421-15a75116e018'></a>

Table 1: Model Parameters and the values used in presented simulations.

<a id='15701be7-aa77-40bc-9650-fc04a44331d8'></a>

20

<!-- PAGE BREAK -->

<a id='596bc9ea-5789-4570-a263-1273e717b3ff'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='183ac381-df6a-414b-9b55-671ae18c1a74'></a>

<::Figure: chart::>A. Kaplan Data. A bar chart showing Cells (%) on the y-axis (from 0 to 40) and Time (days) on the x-axis (from 0 to 12). The legend indicates 'Tumor Cells' in red and 'BMDCs' in green. The bars show low levels of both cell types initially, with BMDCs increasing significantly from day 4 to day 10, peaking around day 8-10, while Tumor Cells remain low but show a slight increase around day 10-12. Error bars are present on the bars. B. Model Predictions. A line chart showing Cells (%) on the y-axis (from 0 to 40) and Time (days) on the x-axis (from 200 to 230). The legend indicates 'Tumor Cells' in red and 'TE Immune Cells' in green. The 'TE Immune Cells' line shows a sharp increase starting around day 210, peaking around day 215 at approximately 28%, and then decreasing. The 'Tumor Cells' line remains low for most of the period, starting to increase slightly around day 225. Figure 4: Comparison of experimental data from Kaplan et al. (2005) (A) to the model predicted dynamics at the secondary site (B). Time in the top plot is measured from the time of injection of 2 × 10⁶ LLC cancer cells, whereas time in the bottom plot is measured from the beginning of the simulation (primary tumor inception). In both cases, green corresponds to pro-tumor immune cells (BMDCs at top, and TE immune cells at bottom) and red corresponds to tumor cells. Color figure available online. A adapted from Kaplan et al. (2005), Figure 1 c.<::>

<a id='58eeeb50-33f1-4a23-84e4-f9038807a894'></a>

21

<!-- PAGE BREAK -->

<a id='cc4a1ec2-92b9-4eae-8338-7ce8214ff800'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='4eade3d2-fc21-461c-ba04-a79b115826ff'></a>

disease appearing after a short period of apparent health. Our model frame-work allows us to interrogate the effect of primary resection on the dynamics of the secondary tumor. We study two cases. In the **first case**, we assume that the disease free equilibrium is locally unstable. In this case, each resec-tion of less than 100% efficiency leads to recurrence of the tumors. Here we are interested in the time delay before re-growth occurs. Figure 5 shows the tumor cell dynamics at the primary (left) and secondary (right) sites using the parameters from Table 1. The untreated dynamics at both sites are repre-sented by the black curves. A primary tumor develops relatively quickly and reaches the local carrying capacity after approximately 100 days, with the secondary tumor only fully developing approximately 150 days later (notice the different time intervals shown on the horizontal-axis).

<a id='3f3f9e08-e8f0-4966-b573-373d785c5c2a'></a>

Note that the saturation observed at both sites can be explained in terms of CSCs. Indeed, we have assumed that the quantities $u_1$ and $u_2$ represent tumorigenic cells within the tumor populations at the primary and secondary sites, respectively. Therefore, saturation may correspond to the homeostatically stable population of CSCs, and may not necessarily represent the end of tumor growth. As the fraction of CSCs within a tumor population is a hotly debated topic (Enderling, 2015), with a number of theoretical results suggesting that pure CSC tumors are possible (Rhodes and Hillen, 2016), this explanation is not unfounded. Alternatively, the rapid saturation at the primary site may suggest that, in this case, the subject would succumb to the primary tumor before the advent of any significant metastatic disease.

<a id='937b670e-1276-4962-a681-9de9186a6589'></a>

We have simulated primary resection by removing a specified fraction
the *resection efficiency* --- of all populations at the primary site at time
*t* = 90 days (vertical dashed line in left plot of Figure 5) (Eikenberry et al.,
2009). The resection time was chosen such that the primary tumor grew suffi-
ciently large so that it could be detected by clinicians (order 10⁷ cells (Friberg
and Mattson, 1997; Eftimie and Eftimie, 2018)). Resection efficiencies in Fig-
ure 5 range from 99.99% (blue) to 100% (red). As expected, increasing the
resection efficiency increases the delay in both local recurrence and metasta-
sis. Using the parameters in Table 1, no resection efficiencies below 100% can
prevent local recurrence, and no resection efficiencies can prevent metastasis.

<a id='5fd5694f-e713-4810-9d6b-9735eb155f7b'></a>

In a **second case** we assume that tumor extinction at the secondary site is stable by reducing the tumor growth rate $r_2$ (see Proposition 2.1). Then the model exhibits more realistic bi-stable behavior at the expense of much slower metastatic growth. The secondary tumor dynamics in response to 100% efficient primary resection are presented in Figure 6 for varying times

<a id='59d9dc32-46be-4e56-b635-1471da814002'></a>

22

<!-- PAGE BREAK -->

<a id='f3abb4bd-c551-4cac-8d8e-04dce4cba364'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='93de647a-9a9a-4272-83ac-32d07dbbc8a0'></a>

<::chart: The image contains Figure 5, which displays two line charts showing the effects of primary resection on tumor population dynamics. The left chart is titled "Primary" and the right chart is titled "Secondary". Both charts have "Time (days)" on the x-axis and "Number of Cells" (scaled by x 10^8) on the y-axis. In the "Primary" chart, the x-axis ranges from 80 to 140 days, and the y-axis from 0 to 6 x 10^8. A vertical dashed line is present at t = 90 days, indicating the time of primary tumor removal. A black dotted curve represents control dynamics, showing an increase in cell number from day 80, reaching a plateau around 5 x 10^8 cells. Multiple colored curves (ranging from blue to red) start from near zero after t=90 days, showing different tumor growth trajectories. An arrow points downwards and to the right, indicating the direction of increasing resection efficiency, with blue curves representing 99.99% efficiency and red curves representing 100% efficiency. In the "Secondary" chart, the x-axis ranges from 240 to 320 days, and the y-axis from 0 to 6 x 10^8. A black dotted curve represents control dynamics, showing an increase in cell number from day 240, reaching a plateau around 5 x 10^8 cells. Similar to the primary chart, multiple colored curves (ranging from blue to red) start from near zero around day 250-260, showing different tumor growth trajectories. An arrow points horizontally to the right, indicating the direction of increasing resection efficiency. Figure 5: Effects of primary resection on tumor population dynamics at the primary (left) and secondary (right) sites. Primary tumor was removed at time t = 90 days (vertical dashed line in left plot) with efficiency ranging from 99.99% to 100% (blue to red). Arrow indicates the direction of increasing resection efficiency. The black dotted curves represent control dynamics. Parameters as in Table 1. Color figure available online.::>

<a id='0d57d8e3-b354-43d0-8147-f9939fd7165d'></a>

of primary resection. As a control, we present the secondary tumor dynamics
in the absence of any primary intervention as the black curve. A consequence
of primary resection is that the secondary site loses a source of tumor cells.
If this primary intervention occurs sufficiently early, the secondary tumor is
too small to support itself, resulting in metastatic extinction (green curves
in Figure 6).

<a id='47ad0a4c-93cd-4df7-b040-e2bf8ead0477'></a>

On the other hand, if enough time has passed with the primary tumor present to ensure that the metastatic tumor is large enough so that it can maintain growth even in the absence of the source of cells from the primary tumor, then we observe rapid metastatic growth, possibly following a period of dormancy (red curves in Figure 6). Two important observations should be made in this case. First, the final metastatic tumor density is smaller when compared to the control case, and second, primary resection can trigger an extended period of dormancy at the secondary site.

<a id='4acd34b9-6d3a-4a5d-8f4c-79696efd8a5d'></a>

3.2. _Immune Therapy_

While there is a significant diversity of immunotherapeutic techniques in cancer treatment, they all share the same goal: increase the number or effectiveness of CT immune cells in order to elicit a strong anti-tumor response. The promise of harnessing the power of the immune system to treat tumors has inspired significant experimental and theoretical investigation. Unfortunately, in many cases, the promises of immunotherapy have not come to

<a id='f96abd58-ff4f-432f-9016-f7f559f4c451'></a>

23

<!-- PAGE BREAK -->

<a id='93562a39-fe8a-4f59-bc52-a01d8f0bb5b8'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='3252142f-260c-4fdb-bdb1-bf43941f409c'></a>

<::chart: Line chart titled "Secondary" showing "Number of Cells" on the y-axis (log scale from 10^0 to 10^3) versus "Time (days)" on the x-axis (from 0 to 5 x 10^4). The chart displays multiple trajectories representing secondary tumor dynamics.
- A black dotted line represents the "Control" curve, showing secondary tumor growth without primary resection.
- Multiple green solid lines, labeled "Metastatic Extinction", show trajectories where the secondary tumor size decreases over time, destined for extinction.
- Multiple red solid lines, labeled "Metastatic Persistence", show trajectories where the secondary tumor size increases rapidly over time, destined for full secondary tumor.
The chart illustrates the effect of primary resection on secondary tumor dynamics for various times of primary resection, ranging between t = 10000 and t = 12500 days. Primary resection was 100% efficient, meaning there was no influence on the secondary site from the primary site following resection. Secondary tumor growth rate was r_2 = 0.2999 so that extinction of metastases was stable.::>

<a id='7def52e1-81f9-40d8-88ad-5ee001b4200f'></a>

24

<!-- PAGE BREAK -->

<a id='7ab8cd8f-6593-4f6e-a874-8792e0ba468a'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='2ea4a4d7-da20-4738-9443-8192ef3a22b3'></a>

<::chart: Figure 7: Effect of immune therapy on growth of the metastatic tumor. Left: Tumor cell dynamics at the secondary site for increasing CT immune cell influx rates, α₁ and α₂. The left plot's Y-axis is 'Number of Cells' (scaled by 10^8), ranging from 0 to 6. The X-axis is 'Time (days)', ranging from 240 to 300. Therapy administered beginning from time t = 90 days, and maintained over the course of the simulation. Values are increasing from blue to red (in direction of arrow). The leftmost (black dotted) curve represents control dynamics, showing tumor growth reaching a carrying capacity around 5.5 x 10^8 cells. Subsequent solid colored curves (blue through red) show delayed tumor growth as CT immune cell influx rates increase. A horizontal dash line at approximately 2.7 x 10^8 cells represents half the carrying capacity, ½ K₂. Right: Time secondary tumor reaches half its carrying capacity as a function of the factor the CT immune cell influx rate increased. The right plot's Y-axis is 'Time to K₂/₂ (days)', ranging from 240 to 300. The X-axis is 'Immune Increase Factor', ranging from 1 to 2.5. The plot shows data points where time to reach half carrying capacity increases from approximately 240 days at an immune increase factor of 1, peaking around 298 days at an immune increase factor of about 1.75, and then slightly decreasing. Color figure available online.::>

<a id='7e7ad5f4-22cf-47fd-990a-e2dcc9cf2679'></a>

fruition, with relatively low response rates for both single (10% - 30%) and combination therapies (50% - 60%) (Emens et al., 2017). A potential ex-planation for this shortcoming may be found in the contradictory roles of the immune system in cancer progression (Section 1), but this possibility has remained largely unexplored. In this section, we consider the implications of immune phenotypic plasticity on the effectiveness of immunotherapies.

<a id='99113ec2-7464-4c73-bccd-bb3275f5982e'></a>

In the following, "immunotherapy" will be simplified to any intervention that results in an increased influx of CT immune cells. Therefore, increasing the CT immune cell influx rates, \(\alpha_1\) and \(\alpha_2\), by some scaling factor will serve as a simplified model of immunotherapy. As was the case for primary resection, therapeutic interventions can only be undertaken in the case that a primary tumor has been identified clinically, so we begin therapy at time \(t =\) 90 days and maintain the therapy until the end of the simulation. Under these conditions, the model predicts little effect on the dynamics at the primary site — not an unexpected result based on the low response rates of many immunotherapies — so we present only the dynamics at the secondary site; thereby shedding light onto the effects of immunotherapy on small, clinically undetectable metastatic tumors, which is particularly relevant to the clinical setting.

<a id='74e60c65-ec46-4d53-afae-e074ff635fe6'></a>

The model predicted results of immotherapy are presented in Figure 7.

<a id='aad6a5ab-3318-4772-83b3-343d6e1829cf'></a>

25

<!-- PAGE BREAK -->

<a id='5bcf828c-da77-4e5c-b01e-7eb6e901c2b4'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='f4538aa7-93df-497f-9000-b489c2c29aaa'></a>

<::chart: This figure contains two plots. The left plot shows Tumor cell dynamics at the secondary site. The y-axis is labeled "Number of Cells" (x10^8), ranging from 0 to 2.5. The x-axis is labeled "Time (days)", ranging from 250 to 400. There are multiple sigmoidal curves, transitioning from blue (leftmost) to red (rightmost), indicating increasing values in the direction of an arrow drawn on the plot. A black dotted curve represents control dynamics. A horizontal dashed line is present at approximately 1.35 x 10^8 cells, representing one quarter of the carrying capacity (1/4 K2). A vertical dotted line is present at Time = 250 days. The right plot shows Time secondary tumor reaches a quarter its carrying capacity. The y-axis is labeled "Time to K2/4 (days)", ranging from 280 to 360. The x-axis is labeled "Immune Increase Factor", ranging from 1 to 2.5. This plot shows a series of data points forming an increasing curve that gradually flattens out.::>Figure 8: Effect of two-pronged immune therapy on growth of the metastatic tumor. Left: Tumor cell dynamics at the secondary site for increasing CT immune cell influx rates, α₁ and α₂, and prevention of immune education, χ₁,₂ = 0. Therapy administered beginning from time t = 90 days, and maintained over the course of the simulation. Values are increasing from blue to red (in direction of arrow). Leftmost (black dotted) curve represents control dynamics. Dash line represents one quarter the carrying capacity, ¼ K₂. Right: Time secondary tumor reaches a quarter its carrying capacity as a function of the factor the CT immune cell influx rate increased. Color figure available online.

<a id='43d2d0ad-d339-45c7-9e53-6915bcbbe160'></a>

Figure 7 (left) shows the dynamics of the secondary tumor cell population for various scaling factors of the CT immune cell influx rates \(\alpha_1\) and \(\alpha_2\), with the scaling factor increasing from blue to red. Figure 7 (right) shows the time to half the carrying capacity (\(\frac{1}{2}K_2\) --- horizontal dashed line in left plot) as a function of the scaling factor; in other words, the right plot shows the intersection times of the solution curves and the dashed line in the left plot. Of note is the non-monotonicity of the rightmost plot. For small increases to the immune influx rates we see significant improvement in tumor delay. However, there is an optimal increase factor, above which the effects of the immunotherapy are actually *detrimental* relative to the optimal and, if increased by a sufficiently large factor, we can have detrimental effects even compared to the control case (results not shown).

<a id='6b8af8fe-5415-4fdd-ace2-560b9fb879be'></a>

In order to determine the mechanism responsible for the non-monotone dynamics in Figure 7, we simulate a modified version of the previous immunotherapy. In addition to the increased CT immune cell influx rate, we assume that our simulated immunotherapy is capable of preventing tumor education of CT immune cells (i.e. the education rates vanish: X1,2 = 0). The model predicted effects of such an intervention are presented in Figure 8. As in the previous figure, the left plot shows the tumor cell dynamics at the secondary site for varying strengths of immunotherapy (increasing from blue

<a id='2384766a-a7db-4a33-b297-21deef26a3d2'></a>

26

<!-- PAGE BREAK -->

<a id='7666f315-ec65-4c67-9a89-3cf96f3b5131'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='dc4695f2-1134-4f1d-9400-5a5996fe3da8'></a>

to red) and the right plot shows the times our solutions reach the endpoint as a function of immunotherapy strength. Note that by preventing tumor education of CT immune cells, the resulting steady state tumor density at the secondary site is significantly diminished, so we use \frac{1}{4}K_2 as our endpoint instead of the previously used \frac{1}{2}K_2.

<a id='f9428ccf-8a75-470f-a45a-f20a1731bdbd'></a>

In contrast to the previous case, the rightmost plot in Figure 8 is monotonically increasing. Although there is a significant slowing of growth in the right plot, the time to endpoint continues to increase for all CT influx rate scalings tested. Noting, in addition, that the ability of the secondary tumor to directly recruit pro-tumor immune cells to the secondary site was not affected by our simulated therapy, it follows that the tumor-induced phenotypic plasticity between CT and TE immune cells is key in the non-monotonic dynamics of Figure 7.

<a id='ba48fc42-ef18-4fb0-8939-987d7d98fc4a'></a>

3.3. Metastasis to Sites of Injury
Our modeling framework provides us the opportunity to investigate whether or not this theory of immune-mediated metastasis is sufficient to explain the observations of metastatic spread to sites of injury. We simulate an injury at the secondary site at time t by pausing the simulation at time t, adding 107 cells to the necrotic compartment, and restarting the simulation with this adjusted initial condition. Evaluation of this injury's effect on the secondary tumor dynamics is done by reporting the time when the secondary tumor reaches a population of K2 cells (referred to hereafter as the "endpoint").

<a id='6ac488df-3a12-4958-af07-f51157db7047'></a>

Figure 9 shows the time to endpoint as a function of the time that an injury at the secondary site is incurred. Control results are presented as the horizontal dashed line, so that times _above_ this line are _beneficial_ to patient survival (green), and those _below_ the line are _detrimental_ (red). The model predicts a clear distinction between _early_ and _late_ injuries. Injuries incurred earlier in the progression of the metastatic tumor are actually beneficial to the patient — delaying metastatic growth by up to nearly 4 months — whereas those that occur in the later stages of disease progression are detrimental to the patient, reducing the time to endpoint by up to two months.

<a id='f9c2f9c7-2163-4632-9ad2-be5eea4a0e6f'></a>

A glimpse into the mechanisms underlying the biphasic dynamics of Fig-
ure 9 are presented in Figure 10, where the dynamics of all cell populations at
the secondary site are presented for three situations: control dynamics (black
dotted curves), an early injury (green curves) and a late injury (red curves).
Early and late injury times were chosen to be the times corresponding to
the maximum and minimum times to endpoint from Figure 9, respectively

<a id='46870c16-0cd0-4f12-b24d-039b93d24e34'></a>

27

<!-- PAGE BREAK -->

<a id='2abdefdc-383f-450d-8d32-959e9ac49e78'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='c0b7d078-cfa1-4b93-b97d-97fbbf18e98b'></a>

<::chart: A scatter plot titled "Time required for secondary tumor to reach $\frac{1}{2}K_2$ cells as a function of the time an injury of $1 \times 10^7$ necrotic cells was incurred." The x-axis is labeled "Time of Injury (days)" ranging from 0 to 200. The y-axis is labeled "Time to Endpoint (days)" ranging from 150 to 350. A horizontal dashed line represents the control value, approximately at y=245. Green plus-shaped markers indicate data points above the dashed line, representing a desirable outcome. These points generally increase from approximately (0, 300) to (80, 360), then drop to (90, 340). Red plus-shaped markers indicate data points below the dashed line, representing an undesirable outcome. These points start around (90, 205), decrease to approximately (100, 185), and then increase towards (200, 235). Parameters as in Table 1. Color figure available online.::>

<a id='91ca3c1e-32f1-4f75-ae12-e093fc89a3f2'></a>

28

<!-- PAGE BREAK -->

<a id='13f2d387-0361-430c-81e8-4697cdc624f8'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='0add21e7-f275-41e3-9e20-c78293dba426'></a>

(indicated by the colored arrows in Figure 10). Note that the early injury
occurs slightly before clinical detectability of the primary tumor (which we
have taken to be 90 days), while the late injury occurs slightly after.

<a id='4fe6ac96-0532-4079-91a1-1f8aa5824bc3'></a>

The dynamics in response to the _early_ injury closely follow the traditional view of both injury response and tumor-immune dynamics: there is a robust, transient CT immune response to the injury (panel (C), green), which inhibits the phase of rapid tumor growth observed in the control dynamics beginning at approximately _t_ = 75 days (panel (A), black). As a consequence of this slowed tumor growth, the TE immune population suffers an extended period of stagnation (panel (D), green), thereby slowing subsequent tumor growth and resulting in a significant delay in tumor progression at the secondary site.

<a id='6bcda12e-2c5e-47b8-abb6-1f96dfb8fe2d'></a>

In contrast, the dynamics in response to the _late_ injury are remarkably different, and instead of delayed tumor growth, metastatic "blow-up" — rapid metastatic growth in response to en external stimulus — is predicted. Although the late injury induces a similar CT immune response, it is significantly foreshortened in comparison to the _early_ injury case (panel (C)). Moreover, the TE immune population undergoes a period of rapid growth coinciding with the CT immune response (panel (D), red). Taken together, and noting that the tumor population has undergone a period of significant growth between the two injury times (panel (A), control), we conclude that the larger secondary tumor present at the time of the late injury more effectively corrupts, or educates, the CT immune response to the local injury. In fact, in simulations where the education rate was _decreased_, the injury no longer elicited a _pro-tumor_ response (results not shown), demonstrating that tumor education of the CT immune response is vital to the dynamics reported in Figures 9 and 10.

<a id='c624daf4-e35f-4c58-a902-4dc174cf8146'></a>

The result of this education is a robust population of pro-tumor TE immune cells which stimulates rapid tumor growth much earlier than in the control case --- that is to say that metastatic "blow-up" is observed. Therefore, our model predicts that rapid metastatic growth at the site of injury necessitates the presence of a sufficiently large local tumor population in order to adequately corrupt/educate the injury-induced CT immune response; otherwise, the immune response to injury is anti-tumor, as traditionally expected. Moreover, our results refine those of Eikenberry et al. (2009), whose mathematical model of metastatic melanoma suggested "blow-up" was the result of a depleted CT immune population. Indeed, "blow-up" in our model was a result of a decrease in the CT immune population and a corresponding

<a id='5b9e5b79-0a71-4868-aa69-6d0228af6562'></a>

29

<!-- PAGE BREAK -->

<a id='7bb248c0-bf05-403d-8437-4444429b9a66'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='3ed23e5c-ec6c-4214-b8fb-d9138b26542a'></a>

<::chart: The figure displays four plots (A, B, C, D) showing cell dynamics over time, with common y-axis label "Number of Cells" (log scale) and x-axis label "Time (days)". Two injury times are indicated by arrows: a green arrow for early injury and a red arrow for late injury. The legend indicates: Control (dotted line), Early Injury (green line), Late Injury (red line).: chart::>
<::chart:
A) Tumor Cells: The plot shows the number of tumor cells over time. The control (dotted black line) starts low, increases, then fluctuates around a high level. The early injury (green line) shows a slow increase, then a rapid increase after approximately 300 days. The late injury (red line) shows an initial increase, then a sharp decrease, followed by another increase. A dashed horizontal line is present at 10^5. The green arrow is at approximately 74 days, and the red arrow is at approximately 102 days.: chart::>
<::chart:
B) Necrotic Cells: The plot shows the number of necrotic cells over time. The control (dotted black line) increases, then decreases, then increases again. The early injury (green line) shows an initial increase, followed by a decrease, and then a rapid increase after approximately 300 days. The late injury (red line) shows a rapid increase followed by a slow decrease. The green arrow is at approximately 74 days, and the red arrow is at approximately 102 days.: chart::>
<::chart:
C) CT Immune Cells: The plot shows the number of CT immune cells over time. The control (dotted black line) starts at a high level, decreases slightly, remains constant, and then decreases rapidly. The early injury (green line) shows a rapid increase, then a rapid decrease to near zero, followed by a slight increase. The late injury (red line) shows a rapid increase followed by a rapid decrease to near zero. The green arrow is at approximately 74 days, and the red arrow is at approximately 102 days.: chart::>
<::chart:
D) TE Immune Cells: The plot shows the number of TE immune cells over time. The control (dotted black line) increases slowly and then stabilizes. The early injury (green line) shows an increase, then a decrease, followed by a rapid increase. The late injury (red line) shows a rapid increase and then stabilization at a higher level. The green arrow is at approximately 74 days, and the red arrow is at approximately 102 days.: chart::>
Figure 10: Dynamics of the tumor cells (A), necrotic cells (B), CT immune cells (C), and TE immune cells (D) at the secondary tumor site upon the simulation of an injury. Two injury times are presented (arrows): an early injury at t = 74.1 days (green) and a late injury at t = 102.5 days (red). Injury was 1 × 10^7 necrotic cells. Dashed line in (A) represents endpoint value of K_2/2. Dotted black curves in each plot denote control dynamics. Parameters as in Table 1. Color figure available online.

<a id='e41f1cb4-453e-4c7a-8b62-ccb348f6f3f7'></a>

30

<!-- PAGE BREAK -->

<a id='c55299af-892c-42d8-a676-26e8215c0ccf'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='055d4d37-4d07-4cdf-9f23-87c6d35ac435'></a>

increase in the TE immune population as a consequence of tumor "educa-
tion."

<a id='d9f796b5-2a23-4860-98f7-fe56eae5901f'></a>

## 4. Discussion

There is a growing body of evidence implicating pro-tumor effects of the immune system in cancer development and metastatic spread (see the extended list of references in Section 1). Inspired by Shahriyari's synthesis of this evidence (Shahriyari, 2016) to formulate a theory of metastasis in which the immune system plays a major role — which we have called the "immune-mediated" theory of metastasis (Cohen et al., 2015) — we have developed a mathematical model of tumor-immune interactions at two anatomically distant sites to interrogate the validity and the implications of this hypothesis.

<a id='66196498-23f9-4f0a-b57d-007d0fa3ab1e'></a>

Validation of our modeling approach and our literature-derived parame-ter estimates was done by confronting the model to experimental data from Kaplan et al. (2005). We found that the model correctly predicted the prepa-ration of the PMN by pro-tumor TE immune cells *prior* to the arrival of any tumor cells in addition to accurately reproducing the relative *magnitude* and *timing* of this PMN preparation (see Figure 4). It is important to note that these results were in the absence of any explicit fitting to the Kaplan data, and that the Kaplan data was not used to calibrate the model. Consequently, the discrepancies between data and model predictions are not be particularly concerning.

<a id='dea8fcea-2680-4ff7-b101-0c34fd079a24'></a>

Once validated, the model was used to numerically explore the implica-
tions of the immune-mediated theory of metastasis. We simulated primary
resection surgeries, immunotherapeutic interventions, and injuries at the sec-
ondary site. Metastasis is relatively robust in the face of primary resection,
with metastatic extinction only possible in certain parameter regimes, and
only if the primary tumor is completely removed sufficiently early (Figure 6).
In response to the loss of cells arriving from the primary tumor, metastatic
dormancy could be observed. A second set of numerical experiments con-
cerned the effects of tumor-education on the efficacy of immunotherapies.
We found that tumor-induced phenotypic plasticity between anti- and pro-
tumor immune cells provides a potential explanation for the relatively poor
performance of many immunotherapies (Emens et al., 2017). Moreover, our
model predicts that the most successful approach to improving the efficacy of
immunotherapies is to inhibit tumor-induced phenotypic plasticity thereby
allowing the CT immune cells to play their anti-tumor roles. This result has

<a id='cb19b7d9-6d37-417a-a047-e596f9c25725'></a>

31

<!-- PAGE BREAK -->

<a id='e8c69d84-e60e-4600-8e10-beea232f0070'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='27991967-54ee-4ae4-8d08-cc74918bdb82'></a>

been recently demonstrated experimentally by Park et al. (2018), lending
further credibility to the results presented herein.

<a id='c8409ea9-dda2-41b2-abcb-e1d84c32c9f2'></a>

Finally, we asked whether or not the immune-mediated theory of metas-tasis could provide an explanation for metastasis to sites of injury by simulat-ing an injury at the secondary site. We found that the CT immune response elicited by an injury was _anti-tumor_ in the absence of a significant metastatic tumor cell population at the secondary site, and _pro-tumor_ if this population was sufficiently large to corrupt the incoming CT immune cells, forcing them to play a pro-tumor role (Figure 10). Not only do these findings support the suggestion of Kumar and Manjunatha (2013) that a population of tumor cells is required at the injury site _prior_ to the injury to see metastasis establish at that site, but they also suggest that tumor-induced phenotypic plasticity plays a crucial role in such establishment.

<a id='b1a8320b-d34f-48ce-a32f-b96251211008'></a>

In the work above, we considered a secondary _site_, but the secondary
tumor dynamics could also be interpreted as the total _metastatic burden_ by
appropriate choice of growth functions. Furthermore, we considered only
one secondary site, but this could easily be extended to include _N_ sites with
anatomically motivated connection network as in (Poleszczuk et al., 2016;
Franßen et al., 2018). We provide a brief sketch of such a model now. Let
_u_i, _v_i, _x_i, and _y_i denote the number of cancer, necrotic, CT, and TE cells at
tumor site _i_, where _i_ = 1, 2, ... _N_. Let _φ_i,j, _ψ_i,j, and _ζ_i,j denote the number of
tumor cells, TE immune cells, and CT immune cells respectively, leaving site
_j_ and arriving at site _i_. We assume that necrotic cells do not travel between
sites. Under the above assumptions, we arrive at the following _N_ site model
for tumor-immune interactions including both pro- and anti-tumor immune
effects:

<a id='662ff302-6ff7-4e18-b9fc-3ee17697f447'></a>

$$\frac{du_i}{dt} = \gamma_i(y_i)g_i(u_i)u_i - \sigma_i(x_i, y_i)u_i - s_i u_i + est_i(v_i, x_i, y_i) \left(\sum_{j=1}^{N} \phi_{i,j}\right),$$$$\frac{dv_i}{dt} = \theta_i\sigma_i(x_i, y_i)u_i - \mu_i v_i,$$$$\frac{dx_i}{dt} = \alpha_i - \rho_i u_i x_i - \omega_i x_i - ed_i(u_i)x_i + \left(\sum_{j=1}^{N} \zeta_{i,j}\lambda_j(u_j, v_j)x_j\right), \quad (16)$$$$\frac{dy_i}{dt} = ed_i(u_i)x_i - \tau_i y_i - \tilde{s}_i y_i + \left(\sum_{j=1}^{N} \psi_{i,j}f_j(u_j)y_j\right).$$

<a id='6894b1da-21a8-4eb5-b839-c8bee8b633d6'></a>

32

<!-- PAGE BREAK -->

<a id='e56531ec-2ff3-4b55-a865-f5785aebeba0'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='bed353b8-3c06-49c3-bcbc-9bb12e39c586'></a>

Modeling of the connection terms, $\phi_{i,j}$, $\psi_{i,j}$, and $\zeta_{i,j}$, is a complicated
problem (see the works of Poleszczuk et al. (2016); Walker et al. (2018, 2017)
for discussion on the $\zeta_{i,j}$ term) and is left as future research.

<a id='dd676114-5290-476d-996d-5610bef35b1e'></a>

Instead of complicating the present model further, it may also be of in-terest to simplify it in order to perform more rigorous mathematical analysis with the aim of discovering the mechanisms underlying the dynamics de-scribed in Section 3. Such simplification is the focus of a current study, with results forthcoming.

<a id='810a7263-be5e-4f57-97ee-bad06347714e'></a>

As the explicit inclusion of pro-tumor immune cells in mathematical mod-els for tumor-immune dynamics is relatively new, the model for phenotypic plasticity between immune types was chosen to follow simple mass-action ki-netics which are most likely too simplistic. den Breems and Eftimie (2016), in their model of M1/M2 macrophages, also modeled the transition using mass-action kinetics. However, Eftimie and Eftimie (2018) have recently proposed a more sophisticated transition function. Based on the important effect that these phenotypic transitions appear to have on the overall dynamics (above, and in (den Breems and Eftimie, 2016; Eftimie and Eftimie, 2018)), research looking to uncover the underlying dynamics of this phenotypic plasticity is warranted.

<a id='81c938a4-fefa-42fa-bfb0-a77dda1d970e'></a>

The model developed here includes a significant number of parameters, with many of them not previously estimated. Consequently, the results we have presented above should be taken with some degree of caution. We do note that some of the TE immune related parameters — recruitment rate by the tumor, for example — may be underestimated (Oleinika et al., 2013), meaning that the observed effects may be conservative. Further experimental and theoretical work must be done in order to validate the predictions made herein before specific therapeutic recommendations can be made. Specializing the model to focus on specific immune cells in a particular cancer may provide more clinically relevant results, and is the focus of a current study.

<a id='38f0a211-d392-47b3-ac9f-c57ec57c57c1'></a>

Overall, our modeling approach showcases the importance of including pro-tumor effects — and tumor-induced phenotypic plasticity in particular — in models of tumor-immune interactions. By confronting our mathematical model to experimental data, we performed meaningful simulations of complex biological phenomena, which provided important insight into the underlying dynamics; insight that may be obscured in traditional biological experimentation. We believe that our research can help inform the design of future experiments and clinical investigations focused on elucidating the precise nature of the pro-tumor role of the immune system in cancer progression.

<a id='a8ae8d82-6006-4c41-94e1-5789f6d90173'></a>

33

<!-- PAGE BREAK -->

<a id='1897f3d7-279a-4997-988d-df9dc7770577'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='40b00dca-8039-4493-afa8-32e56f36ce9c'></a>

sion and metastasis.

<a id='f97c1796-d4c4-44bf-9b47-493a3e688b5c'></a>

**Acknowledgements:** AR acknowledges support through an NSERC CGS-M scholarship and a PIMS Accelerator Award. TH acknowledges support through an NSERC Discovery Grant.

<a id='89517f7d-33ef-430c-925e-4367bdae808c'></a>

References
Balkwill, F., Coussens, L., 2004. Cancer: An inflammatory link. Nature 431,
405-406.

Baratchart, E., Benzekry, S., Bikfalvi, A., et al., 2015. Computational mod-
elling of metastasis development in renal cell carcinoma. PLoS Computa-
tional Biology 11, e1004626.

Benzekry, S., 2011. Mathematical analysis of a two-dimensional population
model of metastatic growth including angiogenesis. Journal of Evolution
Equations 11, 187-213.

Benzekry, S., Gandolfi, A., Hahnfeldt, P., 2014. Global dormancy of metas-
tases due to systemic inhibition of angiogenesis. PLoS One 9, e84249.

Benzekry, S., Lamont, C., Barbolosi, D., et al., 2017. Mathematical modeling
of tumor-tumor distant interactions supports a systemic control of tumor
growth. Cancer Research 77, 5183-5193.

den Breems, N., Eftimie, R., 2016. The re-polarisation of M2 and M1
macrophages and its role on cancer outomes. Journal of Theoretical Biol-
ogy 390, 23-39.

Cameron, M., et al., 2000. Temporal progression of metastasis in lung: Cell
survival, dormancy, and location dependence of metastatic inefficiency.
Cancer Research 60, 2541-2546.

Chaffer, C., Brueckmann, I., Scheel, C., et al., 2011. Normal and neoplastic
nonstem cells can spontaneously convert to a stem-like state. Proceedings
of The National Academy of Sciences 108, 7950-7955.

Chaffer, C., Weinberg, R., 2011. A perspective on cancer cell metastasis.
Science 331, 1559-1564.

<a id='4b5ee091-970f-4c39-a13b-27e7acaf6b66'></a>

34

<!-- PAGE BREAK -->

<a id='ee767b40-9e2a-4b99-bb8e-95325a77581f'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='bec413a4-d1bb-46dd-9949-857e5985d2c7'></a>

Chambers, A., Groom, A., MacDonald, I., 2002. Dissemination and growth of cancer cells in metastatic sites. Nature Reviews Cancer 2, 563–572.

<a id='352d55dd-e4f8-409f-a0bf-fca15854c8dd'></a>

Cohen, E.N., Gao, H., Anfossi, S., et al. 2015. Inflammation mediated metastasis: Immune induced epithelial-to-mesenchymal transition in inflammatory breast cancer cells. PLoS One 10, e0132710.

<a id='1e9e0b62-2ae4-4c7a-b4e2-aa2837448b65'></a>

Coughlin, C., Murray, J., 2010. Current and emerging concepts in tumour metastasis. The Journal of Pathology 222, 1-15.

<a id='a5464241-46a2-43e4-8931-b0b9fc815d47'></a>

Coupland, L., Chong, B., Parish, C., 2012. Platelets and p-selectin control
tumor cell metastasis in an organ-specific manner and independently of
NK cells. Cancer Res 72, 4662–71.

<a id='25ce7095-4825-4bb2-8cce-40235bb02a37'></a>

Demers, M., Krause, D., Schatzberg, D., et al., 2012. Cancers predispose neutrophils to release extracellular DNA traps that contribute to cancer-associated thrombosis. Proceedings of the National Academy of Sciences 109, 13076-13081.

<a id='a007c34f-d691-4afd-872f-7bd0547b1e33'></a>

Dos Anjos Pultz, B., Andres Cordero da Luz, F., Socorro Faria, S., et al.,
2017. The multifaceted role of extracellular vesicles in metastasis: Priming
the soil for seeding. International Journal of Cancer 140, 2397-2407.

<a id='c965547c-69f3-4958-8750-c8254109343b'></a>

Dvorak, H.K., 1986. Tumors: Wounds that do not heal. New England
Journal of Medicine 315, 1650–1659.

<a id='a798ec85-616e-4fb7-9854-9b1952916441'></a>

Dvorak, H.K., 2015. Tumors: Wounds that do not heal - redux. Cancer
Immunol. Res. 3, 1-11.

<a id='fea92a01-dc08-40c8-a789-1898a131315d'></a>

Eftimie, R., Bramson, J., Earn, D., 2011. Interactions between the immune system and cancer: A brief review of non-spatial mathematical models. Bulletin of Mathematical Biology 73, 2-32.

<a id='b7597499-4247-48d9-84b3-ba0c0dd05c3d'></a>

Eftimie, R., Eftimie, G., 2018. Tumor-associated macrophages and oncolytic
virotherapies: a mathematical investigation into a complex dynamics. Let-
ters in Biomathematics 5, S6-S35.

<a id='d52d14ab-afdd-4744-8df3-735e27e01357'></a>

Eftimie, R., Gillard, J., Cantrell, D., 2016. Mathematical models for im-
munology: Current state of the art and future research directions. Bulletin
of Mathematical Biology 78, 2091–2134.

<a id='05e327a8-be07-4381-8073-0580ec4fc735'></a>

35

<!-- PAGE BREAK -->

<a id='6da1e1b6-cea4-47bb-9035-48c23ce07366'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='3c8b4509-b7b4-454b-a7dd-4b2c2c1e8b28'></a>

Eikenberry, S., Thalhauser, C., Kuang, Y., 2009. Tumor-immune interac-
tion, surgical treatment, and cancer recurrence in a mathematical model
of melanoma. PLoS Computational Biology 5, e1000362.

<a id='192aaa8a-e1a0-4362-81ed-7cc3b4e7672c'></a>

Emens, L., Ascierto, P., Darcy, P., et al., 2017. Cancer immunotherapy:
Opportunities and challenges in the rapidly evolving clinical landscape.
European Journal of Cancer 81, 116-129.

<a id='2605d6f1-b81b-4e17-a435-e0f8acc9424d'></a>

Enderling, H., 2015. Cancer stem cells: small subpopulation or evolving
fraction. Integrative Biology 7, 14-23.

<a id='247d3089-52b9-456d-a6c6-6312bc040699'></a>

Erdman, S., Poutahidis, T., 2010. Roles for inflammation and regulatory T cells in colon cancer. Toxicol. Pathol. 38, 78-87.

<a id='c855a426-233a-4b4f-818f-7991e068a78b'></a>

Franßen, L., Lorenzi, T., Burgess, A., et al., 2018. A mathematical framework for modelling the metastatic spread of cancer. BioRxiv : 10.1101/469536.

<a id='81fbfad5-3746-4729-b27d-0c8ff07ac431'></a>

Frei, C., Hillen, T., Rhodes, A., 2018. A stochastic model for cancer metastasis: Branching stochastic process with settlement. Mathematical Medicine and Biology (Submitted). BioRXiv: 10.1101/294157.

<a id='5938ab5e-376e-47ac-bed0-ae592ae5e503'></a>

Friberg, S., Mattson, S., 1997. On the growth rates of human malignant
tumors: Implications for medical decision making. Journal of Surgical
Oncology 65, 284–297.

<a id='e93cca1b-fefc-40de-a9e8-bdf736fb5c59'></a>

Friedl, P., Mayor, R., 2017. Tuning collective cell migration by cell-cell junc-
tion regulation. Cold Spring Harbor Perspectives in Biology 9, a029199.

<a id='6627ae85-3d03-49e3-8743-23fb7593da5a'></a>

Gorelik, E., 1983. Concomitant tumor immunity and the resistance to a second tumor challenge. Advances in Cancer Research 39, 75-120.

<a id='2f688165-008f-4745-9904-0ea6eb519678'></a>

Gupta, G., Massague, J., 2006. Cancer metastasis: Building a framework.
Cell 127, 649-695.

<a id='213e44d0-eee5-4a8b-a61a-248fb99d4a51'></a>

Haeno, H., Michor, F., 2010. The evolution of tumor metastases during clonal expansion. Journal of Theoretical Biology 263, 30–44.

<a id='3415b94f-e31a-420c-a611-ba96b3a6cff0'></a>

Hanahan, D., Weinberg, R.A., 2011. Hallmarks of cancer: The next genera-
tion. Cell 144, 646-674.

<a id='0613daaf-ca0e-40c4-b53e-70a55e22a00e'></a>

36

<!-- PAGE BREAK -->

<a id='f508c14a-8c1e-43df-b6c7-17731909c42d'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='e16a3f79-2687-4b17-8a3e-5403126587f9'></a>

Hanin, L., Rose, J., 2018. Suppression of metastasis by primary tumor and acceleration of metastasis following primary tumor resection: A natural law? Bulletin of Mathematical Biology 80, 519-539.
Hanin, L., Rose, J., Zaider, M., 2006. A stochastic model for the sizes of detectable metastases. Journal of Theoretical Biology 243, 407-417.
Hartung, N., Mollard, S., Barbolosi, D., Benabdallah, A., et al., 2014. Mathematical modeling of tumor growth and metastatic spreading: Validation in tumor-bearing mice. Cancer Research 74, 6397-6408.
Hiratsuka, S., Watanabe, A., Aburatani, H., et al., 2006. Tumor-mediated upregulation of chemoattractants and recruitment of myeloid cells predetermines lung metastases. Nature Cell Biology 8, 1369-1375.
Iwata, K., Kawasaki, K., Shigesada, N., 2000. A dynamical model for the growth and size distribution of multiple metastatic tumors. Journal of Theoretical Biology 203, 177-186.
Joyce, J., Pollard, J., 2009. Microenvironmental regulation of metastasis. Nat. Rev. Cancer 9, 239-252.
Kaplan, R., Riba, R., Zacharoulis, S., et al., 2005. VEGFR1-positive haematopoietic bone marrow progenitors initiate the pre-metastatic niche. Nature 438, 820-827.
Kim, Y., Jeon, H., Othmer, H., 2017. The role of the tumor microenvironment in glioblastoma: A mathematical model. IEEE Transactions on Bio-Medical Engineering 64, 519-527.
Kitamura, T., Qian, B., Pollard, J., 2015. Immune cell promotion of metastasis. Nature Reviews Immunology 15, 73-86.
Kumar, G., Manjunatha, B., 2013. Metastatic tumors to the jaws and oral cavity. Journal of Oral and Maxillofacial Pathology 17, 71-75.
Kuznetsov, V., Knott, G., 2001. Modeling tumor regrowth and immunotherapy. Mathematical and Computer Modelling 33, 1275-1287.
Kuznetsov, V., Makalkin, V., Taylor, I., et al., 1994. Nonlinear dynamics of immunogenic tumors: Parameter estimation and global bifurcation analysis. Bulletin of Mathematical Biology 50, 295-321.

<a id='8e06d93d-772a-4fde-85f1-7d354eafdf68'></a>

37

<!-- PAGE BREAK -->

<a id='d1e7fb34-3c33-4514-8f04-2c385abdda99'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='1ccb3391-241c-4ac1-b430-579bb35db4e9'></a>

Liotta, L., Delisi, C., Saidel, G., Kleinerman, J., 1977. Micrometastasis formation: A probabilistic model. Cancer Letters 3, 203-208.
Liu, V., Wong, L., Jang, T., et al., 2007. Tumor Evasion of the Immune System by Converting CD4+CD25- T Cells into CD4+CD25+ T Regulatory Cells: Role of Tumor-Derived TGF-β. The Journal of Immunology 178, 2883-2892.
Liu, Y., Cao, X., 2016. Immunosuppressive cells in tumor immune escape and metastasis. Journal of Molecular Medicine 94, 509-522.
Luzzi, K., et al., 1998. Multistep nature of metastatic inefficiency: Dormancy of solitary cells after successful extravasation and limited survival of early micrometastases. American Journal of Pathology 153, 865-873.
Marx, J., 2004. Inflammation and cancer: The link grows stronger. Science 306, 966-968.
Mehlen, P., Puisieux, A., 2006. Metastasis: A question of life or death. Nature Reviews Cancer 6, 449-458.
Meng, X., Zhong, J., Liu, S., et al., 2012. A new hypothesis for the cancer mechanism. Cancer and Metastasis Reviews 31, 247-268.
Michor, F., Nowak, M., Iwasa, Y., 2006. Stochastic dynamics of metastasis formation. Journal of Theoretical Biology 240, 521-530.
de Mingo Pulido, A., Ruffell, B., 2016. Immune regulation of the metastatic process: Implications for therapy. Advances in Cancer Research 132, 139-163.
Negus, R., Stamp, G., Hadley, J., et al., 1997. Quantitative assessment of the leukocyte infiltrate in ovarian cancer and its relationship to the expression of c-c chemokines. American Journal of Pathology 150, 1723-1734.
Oleinika, K., Nibbs, R., Graham, G., et al., 2013. Suppression, subversion and escape: The role of regulatory T cells in cancer progression. Clinical and Experimental Immunology 171, 36-45.
Olobatuyi, O., de Vries, G., Hillen, T., 2017. A reaction-diffusion model for radiation-induced bystander effects. Journal of Mathematical Biology 75, 341-372.

<a id='9cc2797f-caa8-4db0-bef3-3eaedf67d8f1'></a>

38

<!-- PAGE BREAK -->

<a id='4d1aa595-ee22-4d36-b891-63e66f694273'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='d58a611c-76d9-4b98-96c1-40ad067e6fd9'></a>

Orlando, P., Gatenby, R., Brown, J., 2013. Tumor evolution in space: the effects of competition colonization tradeoffs on tumor invasion dynamics. Frontiers in Oncology 3, 45.

Paget, S., 1989. The distribution of secondary growths in cancer of the breast. 1889. Cancer Metastasis Review 8, 98-101.

Park, C., Hartl, C., Schmid, D., et al., 2018. Extended release of periopera-tive immunotherapy prevents tumor recurrence and eliminates metastases. Science Translational Medicine 10, eaar1916.

Park, J., Wysocki, R., Amoozgar, Z., et al., 2016. Cancer cells induce metastasis-supporting neutrophil extracellular DNA traps. Science Trans-lational Medicine 8, 361ra138.

Poleszczuk, J., Enderling, H., 2016. Cancer stem cell plasticity as tumor growth promoter and catalyst of population collapse. Stem Cells Interna-tional 2016, 12. Article ID 3923527.

Poleszczuk, J., Luddy, K., Prokopiou, S., et al., 2016. Abscopal benefits of localized radiotherapy depend on activated T-cell trafficking and distribu-tion between metastatic lesions. Cancer Research 76, 1009-1018.

Poleszczuk, J., Moros, E., Fishman, M., et al., 2017. Modeling T-cell traffick-ing to increase the likelihood of radiation-induced abscopal effects. Journal of Targeted Therapies in Cancer 06.17, 36-40.

Qian, B., Pollard, J., 2010. Macrophage diversity enhances tumor progression and metastasis. Cell 141, 39-51.

Rhodes, A., Hillen, T., 2016. Mathematical modeling of the role of survivin on dedifferentiation and radioresistance in cancer. Bulletin of Mathematical Biology 78, 1162-1188.

Robertson-Tessi, M., Gillies, R., Gatenby, R., Anderson, A., 2015. Impact of metabolic heterogeneity on tumor growth, invasion, and treatment out-comes. Cancer Research 75, 1567-1579.

Saidel, G., Liotta, L., Kleinerman, J., 1976. System of dynamics of a metastatic process from an implanted tumor. Journal of Theoretical Biol-ogy 56, 417-434.

<a id='40515268-a7c2-4c81-9204-b204fe3c3ede'></a>

39

<!-- PAGE BREAK -->

<a id='7fe33ce7-ac92-4d90-a8bd-a067823d207c'></a>

bioRxiv preprint doi: https://doi.org/10.1101/565531; this version posted March 1, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license.

<a id='27308d16-4e84-4dd1-b7cd-fce9f3058be1'></a>

Shahriyari, L., 2016. A new hypothesis: some metastases are the result of inflammatory processes by adpated cells, especially adapted immune cells at sites of inflammation. F1000 Research 5, 175.

<a id='91467134-3ac2-425b-bbdb-01ee8deb4d87'></a>

Steidl, C., Lee, T., Shah, S., et al., 2010. Tumor-associated macrophages and
survival in classic Hodgkin's lymphoma. New England Journal of Medicine
365, 875-885.

<a id='af3858f3-ea99-4285-a810-a699b2b8dac4'></a>

Tarin, D., Price, J., Kettlewell, M., et al., 1984. Mechanisms of human tumor metastasis studied in patients with peritoneovenous shunts. Cancer Research 44, 3584-3592.

<a id='974d6d83-0b4a-4cfc-a889-1f42e4c794af'></a>

Valastyan, S., Weinberg, R., 2011. Tumor metastasis: Molecular insights and evolving paradigms. Cell 147, 275-292.

<a id='95ed914c-b9d3-40a3-8efa-b2e8ebcbbd9b'></a>

Walker, R., Poleszczuk, J., Pilon-Thomas, S., et al., 2018. Immune inter-
connectivity of anatomically distant tumors as a potential mediator of
systemic responses to local therapy. Scientific Reports 8, 9474.

<a id='6ab6e869-5684-4787-b808-d9fb463f2862'></a>

Walker, R., Schoenfeld, J., Pilon-Thomas, S., et al., 2017. Evaluating the potential for maximized T cell redistribution entropy to improve abscopal responses to radiotherapy. Convergent Science Physical Oncology 3, 034001.

<a id='1ec1bded-32c2-40c4-8862-379c750020e0'></a>

Walter, N., Rice, P., Redente, E., et al., 2011. Wound healing after trauma
may predispose to lung cancer metastasis: Review of potential mecha-
nisms. American Journal of Respiratory Cell and Molecular Biology 44,
591-596.

<a id='88a8ebf0-6742-4ec0-afcd-73434e32eb1f'></a>

Weiss, L., 1990. Metastatic inefficiency. Advances in Cancer Research 54, 159–211.

<a id='5026fb4a-e0df-4eb4-a795-2b6e4d6543e6'></a>

Wilkie, K., Hahnfeldt, P., 2017. Modeling the dichotomy of the immune
response to cancer: Cytotoxic effects and tumor-promoting inflammation.
Bulletin of Mathematical Biology 79, 1426–1448.

<a id='ed33c31e-9c81-4e95-b695-989f65559ecd'></a>

40