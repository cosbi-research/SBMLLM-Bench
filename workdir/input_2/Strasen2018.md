<a id='9c835d68-0056-4644-945c-aae5119ad81c'></a>

Molecular Systems Biology

<a id='7655e850-6003-4220-8552-600960c27126'></a>

Cell-specific TGFβ signaling

<a id='1846828a-1455-4cd5-b4d9-3ba6fc5bf55d'></a>

Jette Strasen et al

<a id='29f8a04e-5426-4f80-9d5c-ac3fa9b949af'></a>

prevents uncontrolled tissue growth by inducing cell cycle arrest and apoptosis and can trigger epithelial-to-mesenchymal transition (EMT), a conversion of adherent epithelial cells into a migratory, mesenchymal phenotype (Gonzalez & Medici, 2014). TGFβ signaling is dysregulated during pathological conditions such as organ fibrosis and cancer. In tumorigenesis, the pathway plays a dual role: Many early-stage tumors evade the tumor-suppressive, cell cycle inhibi-tory role of TGFβ, whereas its EMT-promoting function frequently induces metastasis of late-stage tumors (Ikushima & Miyazono, 2010). Thus, a specificity switch from one cellular response to another can occur in TGFβ signaling. The underlying molecular changes are currently unclear and may involve changes in the expression of transcription factors (Mullen *et al*, 2011) and signaling proteins (Piek *et al*, 2001), or altered temporal dynamics of the pathway (Nicolás & Hill, 2003).

<a id='d05c9c8e-94ff-4d9e-96fb-55caae9b49e0'></a>

TGFβ initiates signaling through binding to and activation of its serine/threonine kinase transmembrane receptors (TGFβRI and TGFβRII). Ligand binding triggers receptor-mediated phosphorylation of SMAD2/3, which then heterotrimerize with SMAD4, translocate to the nucleus and bind to target gene promoters for transcriptional regulation (Feng & Derynck, 2005). This results in gene expression changes including the downregulation of classical epithelial and cell cycle genes and upregulation of mesenchymal markers (Massagué, 2005). Additionally, TGFβ target genes include negative feedback regulators of the pathway.

<a id='cda2dcb3-4b8d-474c-84bd-1aed502fbe23'></a>

Previous experimental and theoretical studies quantitatively characterized the mechanisms shaping the temporal dynamics of SMAD signaling (Clarke & Liu, 2008; Schmierer *et al*, 2008; Zi *et al*, 2012). One important mechanism that limits the duration of the signal is the depletion of extracellular TGFβ due to internaliza- tion of receptor–ligand complexes, followed by lysosomal TGFβ degradation (Clarke *et al*, 2009; Zi *et al*, 2011). Internalization of signaling complexes may also deplete TGFβ receptors from the cell membrane (Vizan *et al*, 2013), thereby contributing to a refractory period in which cells are insensitive to further TGFβ stimuli (Vizan *et al*, 2013; Sorre *et al*, 2014). In the nucleus, phosphatases such as PPM1A revert the phosphorylation of SMAD2/3 and facili- tate their export to the cytoplasm (Lin *et al*, 2006). Finally, tran- scriptional feedbacks acting at multiple levels including receptor deactivation (Valdimarsdottir *et al*, 2006; Wegner *et al*, 2012) or SMAD dephosphorylation (Wang *et al*, 2014a) contribute to signal termination.

<a id='cc02b4b4-0c1e-44a9-bb69-db31458a5fb3'></a>

Previous quantitative analyses of SMAD signaling mainly focused on average behavior of a cell population at defined time points, whereas the long-term response at the level of individual cells is much less well characterized. Recent studies revealed that SMAD2-SMAD4 complex formation and nuclear translocation of fluorescently labeled SMAD proteins occur with pronounced cell-to-cell variability (Warmflash _et al_, 2012; Zieba _et al_, 2012). Heterogeneous signaling behavior at selected time points post-stimulation was shown to be partially related to cell density and cell cycle stage (Zieba _et al_, 2012). However, to understand how TGFβ signaling elicits defined responses in a cell-specific and concentration-dependent manner, we need to systematically characterize its dynamics on the single-cell level and integrate experimental measurements with quantitative mathematical models of the underlying molecular interactions. This would allow us to predict how individual cells react to a given input and to design

<a id='d3bdce9f-622c-4e9c-bb1d-12368f090067'></a>

targeted perturbations of the pathway to exploit its role in health and disease.

<a id='54993004-e511-44ef-92e3-14fc1af724ee'></a>

To this end, we combined live-cell imaging of fluorescent SMAD2 and SMAD4 fusion proteins with automated image analyses to quantitatively characterize long-term dynamics of TGFβ signaling in individual cells. Based on clustering of thousands of time courses, we identified six cellular subpopulations with qualitatively distinct signaling behavior and concluded that the phenotypic response of an individual cell is determined by the temporal dynamics of SMAD nuclear translocation. We described the dynamics of these subpopulations and of the complete heterogeneous cell population using a quantitative modeling approach. This theoretical and experimental approach revealed that heterogeneity in signaling arises from varying levels of signaling proteins. A CRISPR/Cas9-mediated knock-out of SMAD7 confirmed our model prediction that a major part of the observed heterogeneity can be attributed to fluctuations in feedback proteins. Taken together, we present a framework to characterize the response of cellular subpopulations to external cues and to quantitatively model the underlying molecular mechanisms of signaling heterogeneity. Furthermore, our results place the cell-specific temporal dynamics of SMAD signaling as an important determinant of the variegated cell fates elicited by TGFβ stimuli.

<a id='1d1d0b5b-2f22-4258-a0db-dff4a2b9ca68'></a>

# Results

## Quantitative imaging of SMAD nuclear translocation at the single-cell level

A key step in TGFΒ signaling is the translocation of SMAD transcription factor complexes from the cytoplasm to the nucleus. To monitor this translocation event in individual cells with high temporal and spatial resolution, we established a live-cell reporter system based on the breast epithelial cell line MCF10A, an established model for TGFΒ signaling (Zhang et al, 2014). To this end, we generated a stable clonal cell line expressing a YFP-SMAD2 fusion protein under the control of a constitutive promoter as well as histone H2B-CFP as a nuclear marker (Fig 1A). Western blot analysis revealed that the amount of SMAD2-YFP fusion protein corresponds to approximately 50% of the endogenous SMAD2 protein (Fig 1B). We validated that this overexpression did not perturb the dynamics of SMAD2 signaling by monitoring TGFΒ1-induced phosphorylation of endogenous SMAD2 in the parental and reporter cell lines (Figs 1C and EV1A). Furthermore, qPCR analysis revealed that the induction of well-characterized SMAD target genes in response to TGFΒ1 stimulation remained essentially unchanged (Fig EV1B).

<a id='2c02cffe-7a3f-47ae-b1fa-ac2f73bf408d'></a>

To measure SMAD2-YFP translocation in living cells, we performed time-lapse imaging over a 24-h time interval after a saturating TGFB1 stimulus. In the example cell shown, SMAD2 predominantly located to the cytoplasm in the absence of TGFB1 as expected and strongly accumulated in the nucleus within 1 h of stimulation (Fig 1D). After this initial response, SMAD2 relocalized to the cytoplasm, before it accumulated in the nucleus again about 5 h post-stimulation. Nuclear SMAD2 then remained elevated at varying levels throughout the experiment. As we aimed to compare SMAD2 dynamics in hundreds of cells, we employed automated image analysis to quantify the nuclear and cytoplasmic SMAD2 concentrations and expressed the signaling pathway activity as their ratio (nuc/cyt

<a id='ca26e8b4-2db1-4ef0-9ea9-71e045f61993'></a>

2 of 17

<a id='fbb1b405-3253-4e34-9fd3-e4b838638387'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='a72479b4-bccb-42af-973e-b41668059aa9'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='a81954c8-3514-4fc3-9f87-f5125d3be1e2'></a>

Jette Strasen et al Cell-specific TGFβ signaling

<a id='aa9c4b59-ce91-45e9-90c8-452cf17b8ad7'></a>

Molecular Systems Biology

<a id='6a64352b-f4e2-4b81-9f27-0ae5a9d70c5f'></a>

A SMAD2 reporter
<::diagram showing two DNA constructs within a dashed box. The top construct consists of: a grey box labeled "UbCp", an arrow pointing right to a yellow box labeled "YFP SMAD2", and another arrow pointing right to a green box labeled "G418R". Below this, a "+" symbol indicates co-transfection or co-expression. The bottom construct consists of: a grey box labeled "UbCp", an arrow pointing right to a light yellow box labeled "H2B CFP", and another arrow pointing right to a light blue box labeled "HygroR".: diagram::>

B
<::western blot image. The blot is divided into two sections: "parental" and "SMAD2 reporter". Each section contains two lanes. Bands are visible for: YFP-SMAD2 (a higher band present in the SMAD2 reporter lanes), SMAD2 (a lower band present in all lanes), and GAPDH (a control band present in all lanes at the bottom).: western blot::>

C
<::western blot image showing protein levels over time. The blot is divided into two main sections: "parental" and "SMAD2 reporter". Each section has 7 lanes, corresponding to time points: 0, 0.25, 0.75, 1.5, 3, 4, and 6 hours. The right side labels indicate the proteins detected: pYFP-SMAD2 (a higher band), pSMAD2 (a lower band, phosphorylated SMAD2), and GAPDH (a loading control band at the bottom).: western blot::>

<a id='292f4585-cf4f-4097-a514-208d634d2a48'></a>

D <::A series of microscopic images showing cellular changes over time. Each image displays a cell with an inner white outline and an outer red outline. The images are arranged in two rows, with each image labeled by time:
Row 1: 0min, 20min, 40min, 80min, 100min, 120min, 140min, 160min, 180min, 200min
Row 2: 240min, 300min, 360min, 420min, 480min, 540min, 600min, 660min, 720min, 780min
: figure::>

<a id='5906e906-af08-4dec-be8e-46c5ceebc35b'></a>

<::chart:Figure 1. Dynamics and variability of SMAD2 signaling in single cells. E. Live-cell time-lapse microscopy images of MCF10A cells expressing SMAD2-YFP following treatment with 100 pM TGFβ1 (D). White circles indicate the segmented nucleus, and the estimated cytoplasmic area is represented by red annuli. The indicated cell was tracked over 24 h and the corresponding nuclear-to-cytoplasmic (nuc/cyt) SMAD2-YFP ratio plotted over time (E). The graph shows Nuc/cyt SMAD2 ratio on the y-axis (ranging from 0 to 2) against Time [h] on the x-axis (ranging from 0 to 25). A single blue line plots the ratio over time, showing fluctuations with peaks around 2.5 h and 9.5 h, and values generally between 0.5 and 1.5. F. Time-resolved analysis of the SMAD2 nuclear to cytoplasmic localization for eight individual cells (thin lines) compared to the median nuc/cyt SMAD2 ratio of the entire population (thick line) upon stimulation with 100 pM TGFβ1. See Appendix Table S1 for number of cells analyzed. The graph shows Nuc/cyt SMAD2 ratio on the y-axis (ranging from 0 to 2) against Time [h] on the x-axis (ranging from 0 to 25). Multiple thin lines in varying shades of blue/grey represent individual cells, showing diverse oscillatory patterns. A thicker light blue line represents the median nuc/cyt SMAD2 ratio of the entire population, which initially peaks and then stabilizes around 0.5. G. Median nuc/cyt SMAD2 ratio for reporter cells stimulated with 100 pM TGFβ1 and treated with TGBβRI kinase inhibitor (SB431542) at indicated time points. At all time points, SMAD2 nuclear translocation was dependent on TGFβ receptor activity. See Appendix Table S1 for number of cells analyzed. The graph shows Nuc/cyt SMAD2 ratio on the y-axis (ranging from 0 to 2) against Time [h] on the x-axis (ranging from 0 to 25). Five distinct lines are plotted: -DMSO (black line, low and flat around 0.25) -TGFβ (dark blue line, peaks around 1.5 at 2.5 h, then slowly decreases and stabilizes around 0.75) -TGFβ + TGFβRi (0h) (yellow line, low and flat around 0.25) -TGFβ + TGFβRi (1h) (dark green line, peaks around 1.5 at 2.5 h, then rapidly decreases to around 0.25) -TGFβ + TGFβRi (6h) (light green line, peaks around 1.5 at 2.5 h, then decreases to around 0.5 by 6h, and then rapidly decreases to around 0.25).::>A Fluorescent reporter system to measure SMAD signaling dynamics in individual cells. SMAD2 was fused to the yellow fluorescent protein mVenus (YFP) under the control of the human ubiquitin C promoter (UbCp) with the selection marker G418 (Geneticin). As a nuclear marker, histone 2B (H2B) was fused to the cyan fluorescent protein mCerulean (CFP) under the control of UbCp with the selection marker hygromycin.B Western blot analysis of endogenous and YFP-tagged SMAD2 in a stable clonal reporter cell line and the corresponding parental cell line. Cells were stimulated with 100 pM TGFβ1 and analyzed after 3 h. GAPDH was used as a loading control.C Western blot analysis of SMAD2 activation in SMAD2-YFP reporter and parental MCF10A cells. Cells were stimulated with 100 pM TGFβ1, and SMAD2 phosphorylation was analyzed at indicated time points. GAPDH was used as a loading control.

<a id='4e0e05f3-9133-48e9-b96d-93d34757c703'></a>

ratio, Figs 1E and EV1C–F, Appendix Fig S1 and Appendix II.A and II.B). This measure was robust against correlated fluctuations due to heterogeneity of transgene expression or measurement aberrations such as photobleaching and reproducible between biological replicates (Fig EV1G). We validated that changes in the nuc/cyt ratio of SMAD2 reflect the kinetics of receptor-mediated phosphorylation of endogenous SMAD2 (Fig EV1H and I). When cells divided during the duration of the experiment, we only followed one of the daughter cells and merged mother and daughter trajectories before and after division (see Appendix II.A).

<a id='d931964c-4d45-4212-af74-0929d7f31d9e'></a>

Using this approach, we observed substantial heterogeneity in the response to the saturating stimulus (Fig 1F). Most cells showed nuclear SMAD2 accumulation shortly after the initial stimulus. However, some cells immediately adapted to a low signaling plateau afterward, whereas others were characterized by renewed nuclear translocation of SMAD2. The average response of all cells in the population revealed signaling dynamics similar to biochemical measurements of cell populations in previously published studies (Inman et al, 2002; Clarke et al, 2009; Zi et al, 2011; Vizan et al, 2013). Importantly, nuclear translocation of SMAD2 was dependent

<a id='f6f6f33e-5cf0-464f-941c-2fbba0a1bb88'></a>

© 2018 The Authors

<a id='61fcca76-32b3-4246-a3f4-64eb257fea98'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='b65a5dec-5933-46ff-b1a6-325604df0a48'></a>

3 of 17

<!-- PAGE BREAK -->

<a id='a4ab6702-c9db-401a-8679-c0463566c5e4'></a>

Molecular Systems Biology

<a id='2c312f67-1f5a-4889-95a0-60af64a606f1'></a>

Cell-specific TGFβ signaling

<a id='b161679f-ad8c-4e5a-9ada-6ae2a62fd2d0'></a>

Jette Strasen et al

<a id='fac452ea-c66a-4824-baf9-bbf70d427652'></a>

on TGFβ receptor activity at all time points, as signaling was
rapidly and synchronously terminated in all cells by the specific
inhibitor SB431542 (Fig 1G; Inman et al, 2002). We observed
comparable heterogeneous dynamics for SMAD4 nuclear transloca-
tion using a similarly engineered and validated reporter cell line
(Appendix Fig S2).

<a id='74a35e4d-c6b5-49a2-8c40-77d5bbf8fb99'></a>

## Dynamic features of SMAD signaling encode phenotypic responses

Next, we investigated whether heterogeneous signaling was limited to saturating TGFB1 concentrations or a characteristic feature of the pathway at all stimulus levels. We treated cells with varying TGFB1 doses and quantified SMAD2 localization over a 24-h period. Interestingly, we again observed pronounced cell-to-cell variability (Fig 2A). At low stimulation levels, cells either showed almost no response to the input or transient nuclear SMAD2 accumulation over the first 5 h. At higher TGFB1 concentrations, most cells showed an initial response to the input. However, the extent and duration of renewed nuclear SMAD2 translocation at later time points were highly variable: A single-cell response to 25 PM TGFB1 could be transient and of limited amplitude, resembling trajectories typically observed upon stimulation with 5 PM TGFB1 (Fig 2A). In essence, dynamic signaling responses were overlapping between input levels and therefore only partially determined by the strength of the extracellular stimulus.

<a id='633fb365-02ce-4fe9-b53f-02d52af0fcce'></a>

TGFβ is known to control cell fate in a dose-dependent manner (Schmierer & Hill, 2007). Accordingly, we find that changing the TGFβ1 stimulus alters the median SMAD2 response and expression levels of selected target genes in cell populations (Figs 2B and EV2A and B). How does the SMAD pathway encode dose-dependent information despite the strong cellular heterogeneity observed in our single-cell measurements? We hypothesized that phenotypic responses are determined by the individual pattern of SMAD translocation in a given cell rather than by the amount of ligand applied to a population. To quantify pair-wise differences between single-cell time courses, we used dynamic time warping (DTW), a method for non-linear alignment in the time domain, which is frequently employed in speech analysis (Sakoe & Chiba, 1978). Compared to simpler metrics such as Euclidean distance, DTW is more robust against distortions in the time domain and therefore emphasizes dynamic patterns while preserving dif-ferences in amplitudes (Fig EV2C). To improve its applicability to biological systems, we modified DTW by introducing an elastic constraint on stretching a given time series (cDTW, see Appendix Fig S3 and Appendix II.C for more information on cDTW implementation and performance).

<a id='7cce8510-8cf8-4619-9008-14997f81ae7e'></a>

Using this approach, we calculated the similarity between time courses for thousands of cells stimulated with six different doses of TGFβ1, grouped them using hierarchical clustering, and defined six response classes of SMAD signaling (Fig EV2D-F, Appendix II.D). The median time courses of the response classes showed qualitatively distinct signaling behavior (Fig 2C). Class 1 is defined by a minimal response to stimulation; its members can therefore be considered non-responders. The other classes show either transient (classes 2 and 3) or sustained dynamics (classes 4–6) of varying levels and duration. As expected, increasing ligand concentrations induced a shift from non-responders toward

<a id='d7bcb6ff-b611-4bef-a3b8-a1a53453bdeb'></a>

transient and then sustained signaling (Fig 2D). However, this
transition is not sharp, but gradual, implying that cells from
several signaling classes can be observed upon stimulation with a
given dose. Accordingly, cells stimulated with the same TGFβ
concentration are more distinct in their dynamics than cells
grouped into a common signaling class: This was visualized by a
higher number of cells with positive silhouette scores in the lower
versus the upper panel of Fig 2E. Positive silhouette scores indi-
cate that trajectories were more similar to others in their own
group compared to any other group according to cDTW scores
(see also Appendix II.D).

<a id='a63fa133-4421-4a5b-9567-29cc37b857ba'></a>

We next investigated whether phenotypic responses are primar-
ily determined by the extracellular concentration of the ligand or by
the dynamics of SMAD signaling. To this end, we analyzed TGFβ-
induced changes in proliferation for all cells belonging to a signaling
class or treated with the same extracellular stimulus. We observed
that in general, SMAD signaling activity correlated with reduced cell
divisions as expected. Sorting cells according to signaling classes
indicated that sustained accumulation of SMAD in the nucleus
affected cell cycle progression more profoundly then transient
SMAD translocation (Fig 2F). Cell motility was altered both by tran-
sient and sustained SMAD signaling, although changes remained
modest for the first 24 h after (Fig 2G). We detected more robust
increases in motility when directed movements were analyzed for a
60-h period post-stimulation (Fig EV2G and H). In all cases, signal-
ing classes provided a better separation of phenotypic outcomes
compared to ligand concentration as judged by the magnitude of
effects and the appearance of gradual differences between groups
(Figs 2F–G and EV2I–J) This supports our hypothesis that the
dynamics of signaling, and not the stimulus dose, encode for cellu-
lar behavior.

<a id='b465eeab-cb45-40cf-8343-a13a273e0ba1'></a>

# Dynamics of SMAD signaling are determined by the state of individual cells

Our results so far suggest that heterogeneity in the signaling pathway disturbs transmission of the extracellular signal, that is, the ligand concentration. As a consequence, cells respond to a given input with individual SMAD dynamics that can be grouped in signaling classes. What determines which signaling class a cell belongs to? Previous studies investigating single-cell responses suggest at least three potential sources of cell-to-cell variability: cell cycle, local density, or variations in protein levels (Loewer & Lahav, 2011; Snijder & Pelkmans, 2011).

<a id='0c83f8cf-4ba6-4b53-8495-3bc71095f98a'></a>

To determine whether cell cycle state impacts TGF̑ signaling,
we imaged cells for 24 h before stimulating them with different
TGF̑1 concentrations (Fig EV3A). We then sorted cells either
according to the last division before the stimulus or according to the
amplitude of the response. However, we did not observe any obvi-
ous correlation between cell cycle state and SMAD signaling compe-
tence (Figs 3A and EV3B). To quantify their relation, we mapped
SMAD signaling responses for each individual cell in the new
dataset to the previously defined signaling classes (Fig 3B). This
mapping was achieved by calculating Euclidian distances of
single-cell time courses in both datasets and assigning new trajecto-
ries to the signaling class of the most similar single-cell response
from the previous experiment (Appendix II.H). As expected, we
observed similar distributions of cell division times for all signaling

<a id='07d7c8eb-4c36-47e4-b1c4-903cac7990e2'></a>

4 of 17

<a id='2f1a142f-8dd8-48f6-98c1-e369c9a75848'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='fd084c74-a619-4129-aa95-d10316908caf'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='a1e7a62e-9350-4233-afae-f8dcb189ab7e'></a>

Jette Strasen et al Cell-specific TGFβ signaling

<a id='eeb563f9-b08e-4055-b5ae-743c7710ca2a'></a>

Molecular Systems Biology

<a id='0cee840c-1d63-41da-a5c2-dc630c148865'></a>

A<::Three line graphs showing Nuc/cyt SMAD2 ratio versus Time [h]. Each graph displays multiple thin lines representing individual cells and one thicker line representing the average. The graphs are titled: '1pM', '5pM', and '25pM'. Y-axis: Nuc/cyt SMAD2 ratio (0 to 2.5). X-axis: Time [h] (0 to 25).: line_chart::>B<::Line graph showing Nuc/cyt SMAD2 ratio versus Time [h] for different TGFβ concentrations. Legend: 0pM (light grey), 1pM (light blue), 2.5pM (medium blue), 5pM (darker blue), 25pM (purple), 100pM (dark purple). Y-axis: Nuc/cyt SMAD2 ratio (0 to 1.6). X-axis: Time [h] (0 to 25).: line_chart::>C<::Line graph showing Nuc/cyt SMAD2 ratio versus Time [h] for different cell classes. Legend: Class # 1 (dark blue), 2 (light blue), 3 (orange), 4 (yellow), 5 (light green), 6 (dark green). Y-axis: Nuc/cyt SMAD2 ratio (0 to 2.5). X-axis: Time [h] (0 to 25).: line_chart::>D<::Stacked bar chart showing the fraction of cells for different TGFβ concentrations, categorized by class. X-axis: TGFβ concentration [pM] (0, 1, 2.5, 5, 25, 100). Y-axis: Fraction of cells (0 to 1). Each bar is segmented by colors corresponding to Class # 1 to 6, as defined in the legend for C.: bar_chart::>E<::Two silhouette plots. The top plot shows silhouette scores for cells grouped by TGFβ concentration. The bottom plot shows silhouette scores for cells grouped by class number. Both plots have 'Silhouette score' on the x-axis (-0.8 to 0.8) and 'Cells' on the y-axis. A legend for the top plot indicates 0pM, 1pM, 2.5pM, 5pM, 25pM, 100pM. A legend for the bottom plot indicates Class # 1 to 6. Arrows above the x-axis indicate 'More similar to: other group(s)' to the left and 'own group' to the right.: silhouette_plot::>F<::Two stacked bar charts showing the fraction of cells based on the number of cell divisions (2, 1, 0). The top chart categorizes cells by TGFβ concentration (0pM, 1pM, 2.5pM, 5pM, 25pM, 100pM). The bottom chart categorizes cells by Class # (1 to 6). X-axis: Fraction of cells (0 to 1). Y-axis labels for each bar are the concentration or class. Legend indicates the number of cell divisions (2, 1, 0) with corresponding shades of blue/grey.: bar_chart::>G<::Two box plots. The top box plot shows 'Distance [µm]' versus 'TGFβ concentration [pM]' (0, 1, 2.5, 5, 25, 100). The bottom box plot shows 'Distance [µm]' versus 'Class' (1, 2, 3, 4, 5, 6). Both Y-axes range from 0 to 70 µm. Red dots represent outliers.: box_plot::>

<a id='4d26b372-85b2-4f4f-ac93-5f98fac2c6f4'></a>

**Figure 2. SMAD dynamics decompose into distinct signaling classes.**
A Time-resolved analysis of SMAD2 nuclear to cytoplasmic localization for varying stimulus levels. Nuc/cyt SMAD2 ratios for eight individual cells (thin lines) as well as the population median (thick line) are shown. See Appendix Table S1 for number of cells analyzed.
B Median nuc/cyt SMAD2 ratio of cells stimulated with varying concentrations of TGFB1 over 24 h. See Appendix Table S1 for number of cells analyzed.
C Individual cells were clustered into six signaling classes according to their time-resolved nuc/cyt SMAD2 ratio using dynamic time warping (DTW). Each line represents the median over all cells of the indicated cluster. Cells stimulated with varying TGFB1 concentrations as indicated in (B) were included in the analysis.
D Distributions of signaling classes depending on TGF̒ dose.
E Silhouette plots of cells sorted according to TGF̒ concentration (upper panel) or signaling classes (lower panel). Plots provide a graphical representation of how well the nuc/cyt SMAD2 ratios of each cell correspond to trajectories of other cells in its own group according to the cDTW measure. Positive silhouette scores indicate that SMAD2 responses are more similar to the own group, while negative scores signify that the corresponding trajectory is closer to any of the other groups. In general, signaling classes provide better separation than sorting according to stimulus levels.
F Cell proliferation shown as number of cell divisions per cell within 24 h after a TGF̒ stimulus. Cells were sorted according to TGF̒ concentrations (upper panel) or signaling classes (lower panel).
G Motility of each cell as summed distance covered between 20 and 24 h after stimulation with TGF̒ (in pixel). Cells were sorted according to TGF̒ concentrations (upper panel) or signaling classes (lower panel). White lines indicate median; boxes include data between the 25th and 75th percentiles; whiskers extend to maximum values within 1.5× the interquartile range; crosses represent outliers. See Appendix Table S1 for number of cells analyzed.

<a id='d3652e9c-2d89-46cd-af96-c4bf5c321c8d'></a>

© 2018 The Authors

<a id='cde0e8b2-8772-4860-9760-0be41a08f261'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='6d07a204-bafb-4977-a5d9-dffd70c050ad'></a>

5 of 17

<!-- PAGE BREAK -->

<a id='cd104f91-de46-4a19-ba49-d891cc182c5b'></a>

Molecular Systems Biology

<a id='63513487-e9c7-41aa-ba26-ca23e9086b3d'></a>

Cell-specific TGFβ signaling

<a id='7bc58a19-a37f-484b-90ea-2391a9ce42df'></a>

Jette Strasen et al

<a id='e87acdef-aa7c-49a1-9854-5c8bbc367d9c'></a>

classes (Figs 3C and EV3C). We further excluded a cell cycle effect using a synchronization protocol: Cells arrested in G2 showed a median TGF̢-induced SMAD2 translocation indistinguishable from an unsynchronized population (Fig EV3D).

<a id='30126961-af51-445a-a841-fa69c7ae99a1'></a>

As our data indicated that heterogeneity in SMAD2 signaling is independent of cell cycle state, we next investigated whether SMAD signaling of a given cell is influenced by the number and distance of its neighbors. To this end, we calculated a local cell density score for each cell of the population based on the weighted distance of cells in a 640 µm radius (Fig EV3E, Appendix II.E). We found that cell density is not sufficient to explain signaling heterogeneity under our reference culture conditions, as the distribution of density scores was overlapping for all signal classes (Figs 3D and EV3F). Finally, we used the information theoretical measures mutual information and entropy to calculated to which extent signaling heterogeneity can be explained by cell cycle and cell density and determined an

<a id='98f65a32-f430-466b-b4f9-223fbb48bbda'></a>

upper bound of below 5% for each process (Fig EV3G and H,
Appendix II.E).

<a id='07f17dc0-70b5-4a2f-a85d-823c04912b9d'></a>

Having excluded a major role for cell cycle and cell density, we asked more generally whether signaling heterogeneity arises from differences in the cellular state or from stochastic dynamics of the signaling pathway itself. Previous work on other signaling pathways had shown that sister cells analyses can help tackling this question (Geva-Zatorsky et al, 2006; Spencer et al, 2009; Sandler et al, 2015): If recently divided cells show similar signaling responses, heterogeneity likely arises from cellular state which is assumed to be similar for both sister cells. In contrast, a divergent response in sister cells would indicate that the signaling response is intrinsically unpredictable and stochastic. To analyze the response of sister cells upon TGFβ stimulation, we used a dataset of over 6,000 cells from 11 independent experiments, all treated with 100 pM TGFβ1, and identified cell division events at any time point after stimulation

<a id='6728f3b3-f803-4257-b956-8a2e3d4b0e1e'></a>

<::Figure: A. Two heatmaps showing single cell trajectories. The y-axis is "Single cell trajectories" from 0 to 400. The x-axis is "Time [h]" from 0 to 36. An arrow indicates "TGF" at 24 h. The color bar on the right shows "Nuc/cyt SMAD2 ratio" from 0.2 to 1.8. The left heatmap shows a grey diagonal line. The right heatmap shows similar data without the grey line. Both heatmaps show a transition in color intensity around the 24 h mark, indicating a change in Nuc/cyt SMAD2 ratio. B. A line graph showing Nuc/cyt SMAD2 ratio over time. The y-axis is "Nuc/cyt SMAD2 ratio" from 0 to 2.5. The x-axis is "Time [h]" from 0 to 36. A dashed vertical line at 24 h is labeled "TGF". There are six colored lines representing different classes (1-6), as indicated in the legend: Class # 1 (dark blue), 2 (light blue), 3 (teal), 4 (green), 5 (yellow), 6 (orange). All lines show a peak in Nuc/cyt SMAD2 ratio shortly after 24 h, with varying magnitudes and decay rates. C. A box plot showing the time of division for different classes. The y-axis is "Time of division [h]" from 0 to 20. The x-axis represents "Class" from 1 to 6. Each class has a box plot showing median, interquartile range, and outliers (red crosses). D. A box plot showing the density score for different classes. The y-axis is "Density score [au]" from 0 to 10. The x-axis represents "Class" from 1 to 6. Each class has a box plot showing median, interquartile range, and outliers (red crosses). E. A line graph showing similarity score over time. The y-axis is "Similarity score [au]" from -0.5 to 2. The x-axis is "Time [h]" from 0 to 12. There are two lines: "sister cells" (red) and "cell pairs (unrelated)" (blue), both with shaded error regions. The red line starts higher and gradually decreases, while the blue line starts lower and also decreases, staying close to or below 0. A dashed horizontal line is at 0.::>

<a id='36e1ac61-bb34-4616-82ce-47652798730c'></a>

Figure 3. Heterogeneity in SMAD dynamics determined by cellular state.
A Heat map of SMAD2 translocation in individual cells over time. Cells were imaged for 24 h before stimulation with 100 pM TGFβ1. Each horizontal line represents a single cell, and the nuc/cyt ratio is shown as indicated in the legend. Time of cell division is indicated by white marks. Cells were sorted either by the time of the last division before stimulation (left) or by the amplitude of their response (right). Cell cycle and response are not correlated. See Appendix Table S1 for number of cells analyzed.
B Mapping of SMAD2 translocation dynamics in individual cells to previously identified signaling classes (compare Fig 2C). Cells were imaged for 24 h before stimulation with varying TGFβ1 concentrations (Fig EV3A). For each trajectory, the most similar signaling class was determined using Euclidian distance to the median dynamics of the previously defined clusters (Fig 2C) as a similarity measure. Median nuc/cyt SMAD2 ratios for resulting mapped subpopulations are shown. See Appendix Table S1 for number of cells analyzed.
C Time of last cell division before stimulus for each signaling class (defined in B). Distributions are overlapping; no significant trend in cell division time is observable. White lines indicate median; boxes include data between the 25th and 75th percentiles; whiskers extend to maximum values within 1.5x the interquartile range; crosses represent outliers. See Appendix Table S1 for number of cells analyzed.
D Cell density before stimulus for each signaling class (defined in B). Density scores represent a weighted sum of all neighboring cells within 640 µm distance. Distributions are overlapping; no significant trend in cell density is observable. White lines indicate median; boxes include data between the 25th and 75th percentiles; whiskers extend to maximum values within 1.5x the interquartile range; crosses represent outliers. See Appendix Table S1 for number of cells analyzed.
E Analysis of SMAD2 translocation dynamics in sister cells. SMAD2 translocation dynamics in sister cells after division and unrelated cell pairs with the same nuc/cyt SMAD2 ratio were compared using cDTW. Resulting similarity scores were aligned in time and compared to those from randomly selected cell pairs. Effect size (solid lines) and 95% confidence intervals (shaded areas) were estimated by bootstrapping. The analysis shows that recently divided cells are more similar than control cell pairs and remain correlated over time, indicating that heterogeneity arises from differences in cellular state. See Appendix Table S1 for number of cells analyzed.

<a id='51987b71-eb24-4b31-8285-bf46a1b9b9fb'></a>

6 of 17

<a id='5003b6a5-84e0-42d8-b7ca-341fb91ba380'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='1a6ef3e1-9ac1-419c-bda8-0654c18414d5'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='4a8754f4-f7d7-4989-aa33-178e8ad227ba'></a>

Molecular Systems Biology

<a id='c4c54517-eab6-4032-81a1-c0a97b7c1928'></a>

Cell-specific TGFβ signaling

<a id='e69671f9-f1e3-4995-b20a-1639fb8e4189'></a>

Jette Strasen et al

<a id='25be67c6-af03-4f80-be8c-0a4885c49221'></a>

<::Figure A: A flowchart illustrating a simulation scale process from population to single cells. It begins with a graph titled "Population average fit" showing Nuc/cyt SMAD2 ratio (y-axis, from 0 to 2) against Time [h] (x-axis, from 0 to 1500). The graph contains blue data points and a black dashed model line. This leads to "Fit median of class", which branches into four graphs labeled "Class 1", "Class 2", "Class 3", and "Class 4". Each class graph shows a single curve (blue, green, yellow, orange respectively) with a black dashed model line. These then lead to "Introduce heterogeneity", where each class shows a graph with multiple colored lines diverging from the class median. Finally, these converge to "Reconstruct population", which shows a single graph with numerous colored lines representing individual cells. The process is labeled along the bottom as "Population" --- "Sub-Population" --- "Single cells", with "Simulation scale" indicated below the dashed line. Figure B: A biochemical pathway diagram depicting Receptor module, SMAD module, and Feedback mechanisms across Cell Surface, Cytoplasm, and Nucleus. The diagram shows various molecular species (e.g., R1, R2, L, R1R2-L, S2, S4, S2n, S4n, FB) and their interactions, including binding, phosphorylation (indicated by 'P' in circles), and transport between compartments. For example, R1 and R2 are at the cell surface, binding with L to form complexes like R1R2-L. S2 and S4 are shown in the cytoplasm, undergoing phosphorylation and transport into the nucleus (S2n, S4n). A red line indicates a feedback loop originating from the nucleus, involving FB, and connecting back to the receptor module.::>

<a id='3c8d3658-a044-41bb-8707-c8c1b8917758'></a>

C
<::chart: A line graph with Nuc/cyt SMAD2 ratio on the y-axis (0.2 to 1.6) and Time [h] on the x-axis (0 to 24). Five lines represent different TGFβ concentrations: 1pM, 2.5pM, 5pM, 25pM, and 100pM, with corresponding data points and model curves. The legend indicates "• Data" and "— Model". The 100pM line shows a high peak and slow decay, while lower concentrations show lower peaks and faster decays.::>
Nuc/cyt SMAD2 ratio
1.6
1.4
1.2
1
0.8
0.6
0.4
0.2
0 12 24
Time [h]

D
<::chart: A line graph with TGFβ concentration [pM] on the y-axis (0 to 25) and Time [h] on the x-axis (0 to 24). Asterisks represent data points with error bars, showing a decreasing TGFβ concentration over time. A solid line represents the model fit, surrounded by a shaded area indicating uncertainty. The legend indicates "* Data" and "— Model".::>
TGFβ concentration [pM]
25
0 12 24
Time [h]

E
<::chart: A line graph with Nuc/cyt SMAD2 ratio on the y-axis (0.5 to 1.5) and Time [h] on the x-axis (0 to 24). The graph shows data points (asterisks) and a model curve (solid line) for a 5pM concentration. A dashed vertical line is present at approximately 5 hours. The Nuc/cyt SMAD2 ratio peaks early, then decreases and stabilizes. The legend indicates "* Data" and "— Model".::>
5pM
Nuc/cyt SMAD2 ratio
1.5
1
0.5
0 12 24
Time [h]

F
<::chart: A line graph with Nuc/cyt SMAD2 ratio on the y-axis (0.5 to 1.5) and Time [h] on the x-axis (0 to 24). The graph shows data points (asterisks) and a model curve (solid line) for a 5pM concentration. A dashed vertical line is present at approximately 9 hours. The Nuc/cyt SMAD2 ratio peaks early, decreases, and then shows a second, smaller peak before stabilizing. The legend indicates "* Data" and "— Model".::>
5pM
Nuc/cyt SMAD2 ratio
1.5
1
0.5
0 12 24
Time [h]

G
<::chart: A line graph with Nuc/cyt SMAD2 ratio on the y-axis (0.5 to 1.5) and Time [h] on the x-axis (0 to 24). The graph shows data points (asterisks) and a model curve (solid line) for a 100pM concentration. A dashed vertical line is present at approximately 6 hours. The Nuc/cyt SMAD2 ratio peaks early, then decreases and stabilizes at a relatively high level. The legend indicates "* Data" and "— Model".::>
100pM
Nuc/cyt SMAD2 ratio
1.5
1
0.5
0 12 24
Time [h]

H
<::chart: A line graph with Nuc/cyt SMAD2 ratio on the y-axis (0.5 to 2.5) and Time [h] on the x-axis (0 to 5). Two sets of data points (asterisks) and model curves (solid lines with shaded error bands) are shown: "— Control" (purple) and "— DRB" (red). Both conditions show an initial increase in Nuc/cyt SMAD2 ratio, with DRB showing a higher peak and slower decay compared to Control. The legend indicates "* Data" and "— Model".::>
Nuc/cyt SMAD2 ratio
2.5
2
1.5
1
0.5
0 2.5 5
Time [h]

<a id='8dd15c92-2cbf-4d8d-b13d-f78957b6214e'></a>

Figure 4. Mathematical modeling of TGFβ signaling.
A Outline of a tiered approach to model heterogeneous signaling in single cells (see text for details).
B Topology of TGFβ pathway model. The oval shapes represent free receptors (blue), ligand (yellow), and ligand–receptor complex (gray). Extension "-e" signifies endosomal species. Rectangles represent SMAD2 (blue), SMAD4 (green), and generic feedback regulator (yellow). Extensions "p" indicate phosphorylated and "n" nuclear species. Production and degradation are shown by phi symbols. State transitions and intercompartmental shuttling are indicated with arrows, enzyme catalysis with circle headed bars, and feedback inhibition with blunt headed bars.
C Calibration of population-average model by fitting to median SMAD2 translocation dynamics of cells stimulated with different TGFβ concentrations. Experimental data points correspond to Fig 2B. Model fits to other datasets are shown in Fig EV4 (see also Appendix Table S4); parameter values are provided in Appendix Table S5 and Table EV1.
D Medium TGFβ degradation over time. Blue line shows the ligand concentration after an initial stimulus with 25 pM TGFβ1 as predicted by the best-fit mathematical model. Shaded area represents the range of predictions from 30 fits with similar goodness of fit obtained from local multistart optimization (see Appendix III.D). Black stars indicate corresponding experimental measurements. Error bars represent standard deviation from three replicates.
E–G Time-dependent restimulation of the TGFβ pathway at varying input levels. Measured median nuc/cyt SMAD2 ratios (*) and model predictions (—) are shown. Solid lines represent the best-fit model and shaded areas the range of predictions from 30 independent fits (see D). Dashed vertical lines indicate time of second stimulus, which replenishes the extracellular ligand pool to its initial concentration. (E) 5 pM TGFβ1 was applied at 0 h and 3 h. (F) 5 pM TGFβ was applied at 0 h and 8 h. (G) 100 pM TGFβ1 was applied at 0 h and 8 h. See Appendix Table S1 for number of cells analyzed.
H Effect of the global transcriptional inhibitor DRB on SMAD signaling. Cells were stimulated with 100 pM TGFβ1 in the presence or absence of DRB. Measured median nuc/cyt SMAD2 ratios (*) and model predictions (—) are shown. Solid line represents the best-fit model and shaded area the range of predictions from 30 independent fits (see D). See Appendix Table S1 for number of cells analyzed.

<a id='4855cfed-0b78-4409-9fa4-68a1e0c4fcc1'></a>

8 of 17

<a id='07212703-76ba-4808-ba0f-792753b08d8c'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='03895576-9276-4477-97a8-ed8c4174df8c'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='951ea692-3085-432f-983b-66f466022be1'></a>

Jette Strasen et al

<a id='e5f5e9c3-4d24-4166-aabd-fe692a6e9bb9'></a>

Cell-specific TGFβ signaling

<a id='fd7e8e73-eb03-4fa9-840b-0833d8843aed'></a>

Molecular Systems Biology

<a id='29629c00-0278-4995-ba39-3e793fd1bfe9'></a>

cell-to-cell variability and decomposition into signaling classes. To this end, we quantitatively described signaling classes upon stimulation with 100 pM TGFβ1 by fitting six subpopulation models to the average cluster dynamics (Fig 5A, χ² = 1957.8; N = 1,723). These subpopulation models comprised the same kinetic parameter values as the population-average fit, only signaling protein concentrations (e.g., TGFβ receptors or SMAD transcription factors) were allowed to change within a range of 0.5- to twofold around the initial value corresponding to the typical cell-to-cell variation observed for intracellular proteins (Appendix IV.A; Sigal et al, 2006a; Feinerman et al, 2008; Spencer et al, 2009).

<a id='44f51792-7348-4c9b-bdbf-b700c445c871'></a>

Finally, we converted subpopulation models to an ensemble of
artificial cells representing the heterogeneity of the entire cell popu-
lation. Artificial single cells belonging to a signaling class were
generated by repeated simulation with signaling protein concentra-
tions varying around the best-fit values of the corresponding
subpopulation model (Appendix IV.B). The full cell population was
assembled in silico by selecting artificial cells from ensembles
according to the proportion of corresponding signaling class
observed experimentally at a stimulus of 100 pM TGFβ1 (Fig 2D).

<a id='1bcdf8f1-a2f4-4699-8438-4fde0b9a7272'></a>

The unknown degree of signaling protein level variation between individual cells was estimated by comparing the SMAD dynamics in simulated populations with experimental measurements from live-cell imaging. To do so, we extracted four signaling features from the single-cell time courses of SMAD2 translocation (100 pM TGFβ1, Fig 5B): the amplitude of the response at about 60 min (E); the plateau after the initial response at about 300 min (L); the ratio of these two quantities characterizing the degree of signal adaptation (E/L); and the time of the maximal nuc/cyt SMAD2 ratio (T). The distribution of these features among the cell population was assessed and the deviation of simulated and measured distributions quantified as a sum of squared distances (Fig 5C, Appendix IV.B and IV.C). This model-data comparison was done while assuming that protein level variation consists of a linear combination of two log-normally distributed noise contributions: a correlated noise that simultaneously affects all signaling proteins in a given cell simulation and arises from fluctuations in the global gene expression machinery (e.g., RNA polymerases and ribosomes), and an uncorrelated noise specific for each signaling protein arising from stochasticity in gene expression (Elowitz et al, 2002; Sigal et al, 2006b; Rhee et al, 2014; Sherman et al, 2015). For simplicity, we assumed the same extent and type of variation for all signaling proteins. By systematically altering the magnitude of correlated and uncorrelated fluctuations, we observed that simulated cell populations robustly matched the experimental measurements over a wide range of noise levels around an optimal combination of both values (Fig 5C). Importantly, using these noise levels, the heterogeneity of the same signaling features at a lower TGFβ concentration could be successfully predicted without further fitting (Fig 5E). The total signaling protein concentrations in the assembled population were continuous and log-normally distributed as expected for biological cell populations (Fig EV5A).

<a id='c3346662-3822-4aa5-9706-faa660f38447'></a>

To assess whether our tiered modeling approach with quantita- tive fitting of signaling classes improves the description of cellular heterogeneity, we compared our results to a simpler modeling approach in which signaling protein concentrations were directly sampled around the best-fit values of the population-average model (Spencer et al, 2009; Paulsen et al, 2011; Gaudet et al, 2012).

<a id='0dd4f250-eb00-4193-ae45-d5d894308bf6'></a>

Interestingly, this simpler ensemble model described the experimen-
tal data less well and was more sensitive to variation in the corre-
lated and uncorrelated noise contributions (Fig 5D and Appendix
IV.C). Taken together, our modeling approach indicates that varia-
tion in signaling protein concentration is sufficient to quantitatively
explain cell-specific SMAD dynamics.

<a id='e055b294-c383-4e58-94cc-8dd80f444232'></a>

## Negative feedback determines cell-specific responses to TGF̒

Having single-cell simulations reflecting cellular heterogeneity at different TGF̒ concentrations at hand, we asked whether our model gives rise to the same proportions of signaling classes as experimentally observed. Therefore, we mapped simulated SMAD2 trajectories from the artificial cell population to the previously observed signaling classes, which resulted in distributions consistent with the experimental data (compare Figs 2D and 6A). Importantly, as for the measured data, grouping simulated cells according to signaling classes yielded a more homogenous separation than grouping according to stimulus strength (Fig EV5B).

<a id='3e1acb1d-2874-454a-bb8e-5f9335bfb802'></a>

Using these simulations, we further investigated features of cellu- lar heterogeneity that are not directly accessible experimentally, and analyzed how cells transition between signaling classes with increasing TGFβ stimulus (Fig 6B). Interestingly, we observe a massive transition from non-responding and transient signaling (classes #1-3) to sustained pathway activation (classes #4-6) between 5 and 25 PM TGFβ1. Model analysis indicates that the switch to sustained signaling emerges because external TGFB rapidly decays within ~10 h for 5 PM TGFβ1, whereas it remains elevated for about 20 h at 25 PM (Fig 4D). Yet, subpopulation of cells with transient signaling persist at 25 and 100 PM (classes #1-3), indicating that SMAD signaling is restricted despite the continuing presence of ligand, possibly due to high activity of tran- scriptional negative feedback. To confirm this hypothesis, we systematically lowered feedback expression in artificial cells and observed a strong accumulation of cells with high intensity signaling as expected (Fig 6C; class #6). Importantly, cells with none or tran- sient SMAD activation (classes #1-3) completely disappear upon depletion of feedback in the model, providing evidence that signal termination in these subpopulations indeed relies on negative feed- back. Similar results were obtained upon stimulation with 25 pM TGFβ1, while transient signaling classes persisted at 5 PM TGFB1 even in the absence of feedback (Fig EV5C). Importantly, these model predictions were robust despite uncertainties in the estimated kinetic parameter values (Fig EV5D, Table EV1 and Appendix IV.D). Thus, feedback regulation may underlie the decomposition into qualitatively distinct signaling classes at high TGFβ concentrations.

<a id='3d1e990a-6ae5-4396-b69c-579aa6232ef1'></a>

To further confirm the role of feedback in decomposing SMAD
responses into signaling classes, we analyzed signaling protein
distributions for each of the six signaling classes using independent
model fits with a comparable goodness of fit (Appendix Fig S5A).
As these distributions were complex without any parameter provid-
ing a clear discrimination between signaling classes, we employed
methods from information theory and determined the entropy of
model parameters in our subpopulation models (Fig 5A;
Appendix IV.D). If the fitted protein concentration values are similar
in all subpopulation models, they contain little information to distin-
guish between response classes and its entropy will be close to
maximum (2.6 bits). The more heterogeneous parameter values are

<a id='5963d44c-f840-4a20-a42a-ccda146ccbba'></a>

© 2018 The Authors

<a id='514d3ff9-a263-45ba-a393-50bc02ac2992'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='e7b4256b-b4fe-48fd-93c1-5d280251fedf'></a>

9 of 17

<!-- PAGE BREAK -->

<a id='f443c3a0-75cd-465c-b9d2-3b4c5df47b0d'></a>

Molecular Systems Biology

<a id='ae8e1766-24a0-4f93-a3ff-3e4626fe74e0'></a>

Cell-specific TGFβ signaling

<a id='c64c12b4-9aaa-40be-a645-1de9aad35fe6'></a>

Jette Strasen et al

<a id='151b77cf-9111-4dc7-a14c-00151c6d747f'></a>

A. 100pM TGFβ concentration: Six line plots showing Nuc/cyt SMAD2 over Time [h] (0-24 h) for different classes. Each plot compares 'Data' (blue circles) with a 'Model' (black dashed line). The Y-axis is Nuc/cyt SMAD2, ranging from 0 to 2. Class 1 shows a moderate initial rise followed by a stable phase. Classes 2-6 show a more pronounced initial peak, followed by a decline and then a stable phase, with variations in peak amplitude and decay rate across classes. B. Line plot illustrating signal characteristics: Peak time (T), Amplitude (E), and Adaptation (L). The plot shows a signal rising to a peak (marked by T), then decreasing to an adaptation level (L), with the maximum height labeled as Amplitude (E). The X-axis is Time [h] (0-24 h). C. Subpopulation-based model heatmap. The heatmap shows a grid of values across Uncorrelated noise [au] (Y-axis, from 0.05 to 0.3) and Correlated noise [au] (X-axis, from 0.05 to 0.3). A color bar ranges from 0 (blue) to 1 (red), indicating that higher values are concentrated in a central region, particularly around 0.2 Correlated noise and 0.175 Uncorrelated noise. D. Direct ensemble model heatmap. Similar to C, this heatmap displays values across Uncorrelated noise [au] (Y-axis, from 0.05 to 0.3) and Correlated noise [au] (X-axis, from 0.05 to 0.3). The color bar ranges from 0 (blue) to 1 (red), showing that higher values (red/orange) are predominantly located in the upper-left region, corresponding to lower correlated noise and lower uncorrelated noise values.

<a id='ca542b13-2e52-409b-b622-ed0ea25cce3c'></a>

<::Figure E: This figure presents two rows of four line graphs each, comparing experimental data with model predictions for cellular responses. The y-axis for all graphs is "Fraction of cells". The top row displays "Experimental data", and the bottom row displays "Model prediction". Each row contains four sub-plots titled "Amplitude (E)", "Adaptation (L)", "Ratio (E/L)", and "Peak time (T)". Each sub-plot shows two curves, one in green representing "2.5pM" and one in blue representing "100pM".

**Experimental data:**
- **Amplitude (E):** The x-axis is "Nuc/cyt SMAD2 ratio", ranging from 0 to 3. The green curve (2.5pM) peaks around 0.5-0.7, while the blue curve (100pM) peaks around 1.0-1.2.
- **Adaptation (L):** The x-axis is "Nuc/cyt SMAD2 ratio", ranging from 0 to 3. The green curve (2.5pM) peaks around 0.5, while the blue curve (100pM) peaks around 0.75.
- **Ratio (E/L):** The x-axis is "Nuc/cyt SMAD2 ratio", ranging from 0 to 5. Both curves peak around 1.0-1.5, with the green curve slightly higher.
- **Peak time (T):** The x-axis is "Time [h]", ranging from 0 to 3. Both curves show similar profiles, peaking around 1.0-1.2 hours.

**Model prediction:**
- **Amplitude (E):** The x-axis is "Nuc/cyt SMAD2 ratio", ranging from 0 to 3. The green curve (2.5pM) peaks around 0.5-0.7, while the blue curve (100pM) peaks around 1.0-1.2, similar to experimental data.
- **Adaptation (L):** The x-axis is "Nuc/cyt SMAD2 ratio", ranging from 0 to 3. The green curve (2.5pM) peaks around 0.5, while the blue curve (100pM) peaks around 0.75, similar to experimental data.
- **Ratio (E/L):** The x-axis is "Nuc/cyt SMAD2 ratio", ranging from 0 to 5. Both curves peak around 1.0-1.5, with the green curve slightly higher, similar to experimental data.
- **Peak time (T):** The x-axis is "Time [h]", ranging from 0 to 3. Both curves show similar profiles, peaking around 1.0-1.2 hours, similar to experimental data.
: chart::>

<a id='5e2c904c-f49e-4021-a457-d75a20e21bce'></a>

Figure 5. Modeling heterogeneous signaling dynamics in single cells.
A The model of TGFΒ signaling was fitted to six signaling classes observed upon stimulation with 100 pM TGFΒ1. Median nuc/cyt SMAD2 ratios (circles) and model fits (solid lines) are shown.
B Features of SMAD2 translocation dynamics. We considered the amplitude (E) and timing (T) of the first peak of nuclear translocation as well as the amplitude at 300 min (L) as a measure for the signaling activity upon adaptation of the pathway.
C, D Model performance at varying noise levels. Heterogeneous signaling in response to a 100 pM TGFΒ1 stimulus was simulated by signaling class-based modeling (C) or a direct ensemble modeling (D) (see main text). Noise in protein expression is modeled as a combination of correlated and uncorrelated noise (see Appendix IV.B). The differences among single-cell signaling features between model and data are calculated as sum of squared errors and normalized to the maximal deviation observed (color bar). For each combination of correlated and uncorrelated noise, 10,000 cells were simulated.
E Measured and predicted distributions of signaling features for two TGFΒ stimuli (2.5 and 100 pM). A population of artificial cells was assembled according to signaling class distributions observed upon stimulation with 100 pM TGFΒ1 using optimal noise contributions (see panel C). Signaling features were extracted from simulations at different TGFΒ concentrations.

<a id='3f23a04d-4111-41cc-8d5e-95d422dc590b'></a>

among subpopulations, the lower the measured entropy is and the
more they may contribute to the divergent signaling dynamics of the
classes (Fig 6D). While many signaling protein concentrations show

<a id='26e54cb6-6f25-43d9-9dbb-f5577af36364'></a>

relatively similar values in all subpopulation models (entropy ~2.6 bits), the level of feedback protein indeed carried the most information to distinguish between signaling classes.

<a id='bb9473f0-407e-471d-b072-2ab9fcae6490'></a>



<a id='98d05992-f461-4260-823b-8984f7649494'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='b67a698a-7a58-44aa-831b-b78f0c7f5cdf'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='50e735ea-b569-4e9c-8c40-27dacc9dd3fe'></a>

Jette Strasen et al Cell-specific TGFβ signaling

<a id='c645771c-e9bc-47e3-8d06-7fffbb1af6d7'></a>

Molecular Systems Biology

<a id='42ce29b8-342c-4d4c-8bc4-f10f0126a187'></a>

A Model prediction<::stacked bar chart::>  The y-axis is labeled "Fraction of cells" from 0 to 1. The x-axis is labeled "TGF concentration [pM]" with values 1, 2.5, 5, 25, and 100. The legend shows "Class #" with colors corresponding to classes 1 through 6. The bars show the distribution of cell classes at each TGF concentration.::>B Class<::sankey-like diagram::>  The y-axis is labeled "Class" with values 1 through 6. The x-axis is labeled "TGF concentration [pM]" with values 1, 2.5, 5, 25, and 100. Circles at each class and concentration are connected by lines, indicating transitions between classes. The size of the circles and the thickness of the lines vary.::>C Class 100pM TGFβ<::sankey-like diagram::>  The y-axis is labeled "Class" with values 1 through 6. The x-axis is labeled "Feedback expression [%]" with values 100, 50, 30, 27, 25, 20, 18, 15, 11, and 0.01. Circles at each class and feedback expression are connected by lines, indicating transitions between classes. The size of the circles and the thickness of the lines vary.::>D Entropy [bit]<::box plot::>  The x-axis is labeled "Entropy [bit]" with values from 2 to 2.6. The y-axis lists different variables: "R1 clusters", "R2 clusters", "Internalization R1", "Internalization R2", "S2 total", "S2 export", "S2 import", "S4 total", "S4 export", "S4 import", "Dephosphorylation", "FB protein", "FB protein production", "Basal FB mRNA production", and "Induced FB mRNA production". Each variable has a corresponding box plot showing its entropy distribution.::>E parental<::stacked bar chart::>  The y-axis is labeled "Fraction of cells" from 0 to 1. The x-axis is labeled "TGFβ concentration [pM]" with values 1, 2.5, 5, 25, and 100. The bars show the distribution of cell classes at each TGFβ concentration.::>SMAD7-/-<::stacked bar chart::>  The y-axis is labeled "Fraction of cells" from 0 to 1. The x-axis is labeled "TGFβ concentration [pM]" with values 1, 2.5, 5, 25, and 100. The legend shows "Class #" with colors corresponding to classes 1 through 6. The bars show the distribution of cell classes at each TGFβ concentration.::>F<::scatter plot::>  The y-axis is labeled "Distance to SMAD7-/- [au]" from 0.05 to 0.1. The x-axis is labeled "Feedback expression [%]" with values 100, 50, 30, 27, 25, 20, 18, 15, and 11. Points are plotted showing the distance at different feedback expression levels.::>G Model - 30% feedback expression<::stacked bar chart::>  The y-axis is labeled "Fraction of cells" from 0 to 1. The x-axis is labeled "TGFβ concentration [pM]" with values 1, 2.5, 5, 25, and 100. The legend shows "Class #" with colors corresponding to classes 1 through 6. The bars show the distribution of cell classes at each TGFβ concentration.::>

<a id='5eff2738-d742-44ff-b37f-e8b33dcdf7d0'></a>

To experimentally test the predicted role of feedback in signaling heterogeneity, we deleted SMAD7 in SMAD2 reporter cells using Cas9-mediated gene knock-out (Fig EV5E and F). SMAD7 is consid- ered to be one of the main feedback regulators of TGFβ-induced signaling, and acts at the level of TGFβ receptors as implemented in our model (Moustakas & Heldin, 2009). We measured SMAD2 dynamics in response to various doses of TGFβ1 in the parental and knock-out cell line and mapped the resulting time series to the initial observed signaling classes (Figs 6E and EV5G). As predicted by the model, we observed a shift in signaling classes toward those with higher signaling strength. We next aimed to compare the measured single-cell responses to model simulations. As we assumed that some feedback activity is retained in SMAD7 knock-out cells due to the presence of redundant transcriptional feedback regulators in TGFβ signaling (Wegner et al, 2012), we compared signaling class distributions from experimental data and model simulations with

<a id='96aa8c6d-38fe-44ba-bf46-5e29d98cca99'></a>

Figure 6. Negative feedback determines decomposition into signaling classes.
A Predicted distributions of signaling classes depending on TGFβ dose. Simulations were performed as described for Fig 5E. The simulated time courses were mapped onto the original clusters dynamics (Fig 2C) as described in Appendix II.H.
B Transition between signaling classes depending on stimulus strength. Same data as in (A). Black lines and their thickness indicate the direction and extent of transitions between signaling classes. Filled circle size indicates the proportion of artificial cells in the corresponding signaling class.
C Transition between signaling classes depending on feedback strength. The response of a reassembled population of artificial cells to 100 pM TGFβ1 was simulated with reduced feedback expression as indicated (see Appendix IV.D) and mapped to previously observed signaling classes. Black lines and their thickness indicate the direction and extent of transitions between signaling classes. Transitions with a probability below 1% were excluded for better visualization.
D Variation of model parameters across signaling classes. For 30 independent model fits to the experimentally observed signaling classes upon stimulation with 100 pM TGFβ1 (see Appendix), the variation of the indicated parameters between signaling classes was calculated as entropy. Lower entropies indicate more variation between signaling classes; uniform parameter distribution would lead to the maximal entropy of 2.6 bits. White lines indicate median; boxes include data between the 25^th and 75^th percentiles; whiskers extend to maximum values within 1.5x the interquartile range.
E Distribution of signaling classes in parental and SMAD7 knock-out cells. Cells were stimulated with indicated concentrations of TGFβ and measured SMAD2 translocation dynamics mapped to the previously observed signaling classes (Fig 2C).
F Calibration of feedback level. Signaling class distributions at varying levels of feedback expression (C) were compared to experimentally observed distribution upon SMAD7 knock-out (E). Minimal divergence between model and data was observed at 30% feedback expression.
G Predicted distributions of signaling classes depending on TGFβ dose at 30% feedback expression. Simulations were mapped to the previously observed signaling classes (Fig 2C)

<a id='150b30ef-176b-4cc8-b00f-73e21e984b0c'></a>

varying feedback strength and observed the best match at 30% feed-
back strength (Fig 6F and G and Appendix IV.D). In both model and
experiment, feedback depletion led to a disappearance of the non-
responding and transient classes #1–3 at high doses of TGFβ1 (25
and 100 pM). In contrast, cells remained in transient signaling
classes at or below 5 pM TGFβ1, confirming that ligand depletion
dominates signal termination at low input levels. Interestingly, loss
of SMAD7 did not alter the population-median signal duration
(Fig EV5G), further suggesting that it affected this feature only in a
subpopulation of cells.

<a id='5d60af95-0b37-4ef0-bbcc-60920e3bbf72'></a>

A noticeable difference between model and experiment was that
the model predicted a lower fraction of non-responding cells in
SMAD7 knock-out cells at TGF̒ concentrations below 5 pM when
compared to experimental measurements. To explain this discrep-
ancy, we further analyzed parameter variations between signaling
classes using independent model fits. We observed that the non-
responding signaling class #1 differs from the remaining signaling
classes, as it is characterized by a high ratio of feedback protein to
receptor levels (Appendix Figs S5B and S6). We hypothesized that
knock-out cells compensate the loss of SMAD7 by downregulating
TGF̒ receptor levels, thereby increasing the feedback-to-receptor
ratio and the fraction of non-responding cells. Western Blot analyses
support this hypothesis as we observed reduced TGF̒RII levels in
SMAD7 knock-out cells (Appendix Fig S7). Taken together, we
conclude that negative feedback leads to decomposition into

<a id='4909e2fa-df45-486f-9d91-5f8e54fd1c22'></a>

© 2018 The Authors

<a id='3f658950-2333-445c-b537-7f1f0b24de5e'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='944863b7-6259-439a-ab73-cca2830a70bf'></a>

11 of 17

<!-- PAGE BREAK -->

<a id='2dd61587-db4a-48c0-af39-90f5de7287be'></a>

Jette Strasen et al

<a id='364b9646-85e2-4a33-8490-34a8eb732b04'></a>

Cell-specific TGFβ signaling

<a id='68c0bfa7-374d-41f1-b3e8-cce977957f89'></a>

Molecular Systems Biology

<a id='6125eaf1-2769-47c6-bcab-43673f66c32b'></a>

ensembles of single cells were simulated by sampling the signaling protein concentrations around the population median (Spencer et al, 2009; Paulsen et al, 2011; Gaudet et al, 2012). However, the detailed description of defined subpopulations ensured a robust and more precise description of heterogeneity, while minimizing compu- tational cost compared to individually fitting parameters for each cell (Kallenberger et al, 2014; Yao et al, 2016). It would therefore be easy to translate the concept to other cellular systems where time- resolved data at the single-cell level is available, such as NF-kB or p53 signaling (Nelson et al, 2004; Geva-Zatorsky et al, 2006; Tay et al, 2010). However, the current approach relies on temporally stable differences in protein production rates. While this assumption holds true on limited timescales, it will break down when consider- ing response times longer than cell cycle length. Time-varying production rates may solve this issue but will complicate fitting procedures. Moreover, truly stochastic processes such as the proposed stochastic changes in TGFß sensitivity during later signal- ing phases will not be accessible by this approach and require fully stochastic models to provide further insights.

<a id='f1333456-6372-4600-8b00-5d1fbe77af6d'></a>

While our modeling approach highlights the importance of protein level variations, the source of these variations remains elusive. Through many studies in the past years, it became evident that protein level variations represent a combination of fluctuations caused by the stochastic nature of biochemical reactions (Bar-Even et al, 2006; Pedraza & Paulsson, 2008; Lestas et al, 2010), cell-specific activity of regulatory processes (Colman-Lerner et al, 2005) and influences from population microenvironment (Snijder et al, 2009; Snijder & Pelkmans, 2011). These processes affect mammalian signaling systems to varying degrees (Feinerman et al, 2008; Snijder et al, 2009; Spencer et al, 2009; Kallenberger et al, 2014; Frechin et al, 2015; Adamson et al, 2016). Depending on the lifetime of the associated biomolecules, fluctuations from stochastic processes are supposed to vary on shorter time scales compared to regulated sources of cellular heterogeneity. Our sister cell analysis indicates a fast decaying component (within 6 h) as well as stable differences between cells that last beyond the observation period. As the grouping of cells in signaling classes is relatively stable over time, we assume that the long-lasting component dominates cellular heterogeneity. This may reflect differences in signaling history of individual cells, leading to varying states of the TGFß network due to the activity of interacting signal pathways (Guo & Wang, 2009). Depending on the strength of the input, these varying states of the pathway will translate into transient or sustained activation of SMAD signaling and therefore a transition of cells between signaling classes. We find that the levels of few signaling proteins are governing these transitions and provide evidence that feedback expression is a main determinant of signaling classes. At this point, we can only speculate how differences in feedback and specifically SMAD7 expression could arise in genetically identical cells. In addition to stochastic gene expression, cell-specific activation of signaling pathways controlling SMAD7 expression could contribute to the observed cell-to-cell variability. Such pathways may include IFN-γ/ Stat1 (Ulloa et al, 1999), PKC (Tsunobuchi et al, 2004), hepatocyte growth factor (Shukla et al, 2009) or mir21 (Li et al, 2013). Further experiments are needed to clarify sources of heterogeneous feedback expression.

<a id='8212c854-bd52-4751-9eb4-4564308a3673'></a>

Feedback is an essential part of most signaling pathways
(Legewie *et al*, 2008) and is known to support different features of

<a id='08462017-7f30-4ce5-874b-b8fa0eef6f2b'></a>

information transmission depending on network topology and kinetic parameters (Leibler & Barkai, 1997; Yi et al, 2000; Rosenfeld et al, 2002; Yu et al, 2008; Voliotis et al, 2014). Our analysis indicates that in the TGFβ network, feedback mainly acts at high input levels to limit sustained pathway activation, thus promoting adaptation as reported for other signaling systems (Yi et al, 2000; Ma et al, 2009). This could be due to non-linear induction of SMAD7 or a stronger contribution of other parameters such as receptor levels at lower ligand concentrations. In contrast to previous studies (Leibler & Barkai, 1997; Yi et al, 2000; Paulsen et al, 2011), we do not find that negative feedback reduces signaling variability as measured by SMAD2 translocation, but provide evidence that it promotes heterogeneity by establishing signaling classes with transient dynamics at high TGFβ concentrations. Additionally, feedback modulates the amplitude of the response as indicated by transitions within transient and sustained signaling classes, for example, from class 2 to 3 at 5 pM TGFβ or from class 4 to 6 at higher stimulus levels. As our experimental study was limited to SMAD7, it would now be interesting to investigate the contribution of the remaining negative feedbacks. Do they indeed provide redundancy or do they regulate specific features of information transmission?

<a id='2fa326cc-01e2-410d-bb9a-0e9ea123a501'></a>

Our single-cell analysis shows that cell-specific long-term dynam-ics of SMAD translocation determine the phenotypic response to TGF̒ activation. Interestingly, it seems that migration and prolifera-tion may be controlled by different features of SMAD signaling: migration tended to be affected already by a transient SMAD translo-cation (class 2–3), whereas anti-proliferative effects seemed to require sustained SMAD signaling (class 4, 5, and mainly 6). These findings are consistent with previous studies in cancer cell lines in which transient SMAD activation was sufficient to alter cellular motility and induce EMT-like processes, while sustained signaling was required to influence proliferation (Nicol&aacute;s & Hill, 2003; Giampieri et al, 2009). Hence, our analysis shows that dynamic information encoding observed at the level of cell lines may be conserved at the level of heterogeneous single-cell signaling and reflect the regulatory potential of the pathway: By fine-tuning the level of signaling proteins through interacting signaling pathways, the sensitivity of individual cells to TGF̒ inputs can be adjusted within a tissue. This would allow stratifying the cellular response depending on the state of the cell. During therapy, this property of the TGF̒ pathway could be exploited by specifically modulating the levels or enzymatic activities of selected proteins to switch the response from EMT-like processes to proliferation control. As TGF̒ activity is often tightly linked to tumor progression, such a targeted approach may help to improve therapies against advanced cancers.

<a id='29dcd861-ec80-437f-b7b0-3e5af543eb66'></a>

## Materials and Methods

### Cell line and constructs

Human breast epithelial MCF10A cells were cultured in DMEM/F-12 medium supplemented with 5% horse serum, 20 ng/ml epidermal growth factor (EGF), 0.5 µg/ml hydrocortisone, 100 ng/ml cholera toxin, and 10 µg/ml insulin, penicillin, and streptomycin (Debnath et al, 2003). When required, the medium was supplemented with selective antibiotics to maintain transgene expression (400 µg/ml G418, 50 µg/ml hygromycin or 0.5 µg/ml puromycin). We

<a id='cd9de25a-4d1a-4761-86d7-e9686b004538'></a>

© 2018 The Authors

<a id='eab556a3-ab5d-45aa-abc8-ec1bca8bdb37'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='24f7c7d0-58dd-4b87-85fd-6a6d670549dc'></a>

13 of 17

<!-- PAGE BREAK -->

<a id='7a6e67a1-65b9-4687-8bf7-060d064bfa2c'></a>

Molecular Systems Biology

<a id='73fb9dff-75c6-43dd-818b-7e1c2bce84e6'></a>

Cell-specific TGFβ signaling

<a id='1245d7b2-6b6b-4cd1-a064-08beee864bc9'></a>

Jette Strasen et al

<a id='0be39131-6349-422a-b7e6-5ed11e99871f'></a>

generated lentiviral reporter constructs for SMAD2 and 4 using the MultiSite Gateway recombination system (Thermo Fisher Scientific) by fusing the protein coding sequence to the yellow fluorescent protein Venus (YFP) under the control of a constitutive human Ubiquitin C promoter (UbCp). We infected MCF10A cells with corre- sponding lentiviral particles together with viruses expressing histone 2B fused to cyan fluorescent protein (H2B-CFP) under the control of UbCp as a nuclear marker. Subsequently, stable clonal cell lines were established and validated. To knock-out SMAD7, we first infected SMAD2 reporter cells with lentiviruses expressing Cas9 under control of a doxycycline-inducible promoter (Wang et al., 2014b). A stable, clonal cell line was further infected with viruses expressing an sgRNA targeting exon 2 of SMAD7 (TCCTTTACTCCA GATACCCGA) (Shalem et al., 2014) and cultured for 2 weeks in the presence of doxycycline. Finally, we screened clonal cell lines for alterations of the SMAD7 locus by genomic PCR (Thermo Fisher Scientific) and sequencing and selected a line with non-sense muta- tions in both alleles (Fig EV5E).

<a id='deb3f521-bccb-40a7-9edf-ce074b5759be'></a>

## Antibodies and reagents

We used antibodies against total SMAD2 (D43B4, #5339) and pSMAD2 (Ser465/467, 138D4, #3108) from Cell Signaling, SMAD4 (B-8, #sc-7966) and TGFβRII (E-6, #sc-17792) from Santa Cruz, and GAPDH (#G9545) from Sigma-Aldrich. Recombinant human TGFβ1 was obtained from R&D Systems (#240-B-002) and stored at -80°C in 4 mM HCl, 1 mg/ml bovine serum albumin at 390 nM. DRB (5,6-dichlorobenzimidazole 1-β-D-ribofuranoside) was purchased from Cayman (used at 100 μM), TGFβRI kinase inhibitor VI SB431542 from Calbiochem (used at 10 μM) and CDK1 inhibitor RO 3306 (used at 3 μM) from Axon.

<a id='71b44f68-59e6-4dc8-b8c4-1c428af28acb'></a>

# Time-lapse microscopy

For live-cell time-lapse microscopy, 2\times10^5 cells were plated in 35-mm poly-D-lysine-coated glass bottom plates (MatTek or ibidi) 2 days before experiments. Before starting the experiment, cells were washed twice with 1 \times PBS and media was changed to RPMI lacking phenol red and riboflavin supplemented with all growth factors, 5% horse serum and antibiotics. The microscope was surrounded by a custom enclosure to maintain constant temperature (37\u00b0C), CO_2 concentration (5%), and humidity. Cells were imaged on a Nikon Ti inverted fluorescence microscope with a Hamamatsu Orca R2 or Nikon DS-Qi2 camera and a 20\times plan apo objective (NA 0.75) using appropriate filter sets (Venus: 500/20 nm excitation (EX), 515 nm dichroic beam splitter (BS), 535/30 nm emission (EM); CFP: 436/20 nm EM, 455 nm BS, 480/40 nm EX). Images were acquired every 5 min for the duration of the experiment using Nikon Elements software. TGF\u03b2 1 was prepared in 500 \u00b5l media and added, if not noticed otherwise, after one round of images to achieve the final concentration in 2.5 ml media.

<a id='4d4f5a70-d0ca-43b3-8b04-3d3a4be623e0'></a>

**Image analysis and cell tracking**

Cells were tracked throughout the duration of the experiment using custom-written MATLAB (MathWorks) scripts based on code developed by the Alon laboratory (Cohen et al, 2008) and the CellProfiler project (Carpenter et al, 2006). In brief, we applied flat field

<a id='e5ea620d-2e03-47ff-888b-41f1bc6ddad9'></a>

correction and background subtraction to raw images before segmenting individual nuclei from nuclear marker images using thresholding and seeded watershed algorithms. Segmented cells were then assigned to corresponding cells in following images using a greedy match algorithm. Only cells tracked from the first to last time point were considered. For most analyses, we tracked cells in forward direction from the first to the last time point. Upon division, we followed the daughter cell closest to the last position of the mother and merged tracks from mothers and offspring. For sister cell analyses, cells were tracked backward from the last to the first time point, tracks from offspring, and mothers were again merged. As a consequence, tracks of sister cells are identical before cell division. We quantified nuclear fluorescence intensity and measured the fluo- rescence intensity in the cytoplasm using a 4-pixel wide annulus around the nucleus. Finally, we estimated the nuc/cyt ratio for each cell over time and analyzed the resulting single-cell trajectories computationally (Appendix II.A). As nuclear envelope breakdown during mitosis prevented meaningful measurements of SMAD translocation, we interpolated corresponding values. See Appendix for further details on image analysis, cell tracking, and data process- ing.

<a id='c7c16cb7-2b5b-4e32-9372-e334ec65be30'></a>

TGFβ measurement

We used Mink lung epithelial cells (MLECs) stably transfected with a reporter containing a truncated PAI-1 promoter (3TP promoter with three consecutive TPA response elements) fused to the firefly luciferase gene and cultured them in 96-well plates using DMEM (Abe et al, 1994). Supernatants from live-cell microscopy experiments were removed at defined time points and added in triplicates to MLEC reporter cells. After incubation overnight, cells were lysed and thawed. Luciferase activity was measured by 10-s per well readings on a 96-well format luminometer (see Appendix II.I for details).

<a id='78a33767-7b05-4a1e-b526-468cc5f40766'></a>

**Western blot analysis**\n\nCells were plated 2 days before experiments. After stimulation, we harvested cells at indicated time points and isolated proteins by lysis in the presence of protease and phosphatase inhibitors. Total protein concentrations were measured by BCA assay (Thermo Fisher Scientific). Equal amounts of protein were separated by electrophoreses on 10% SDS–polyacrylamide gels and transferred to PVDF membranes (GE Healthcare) by electroblotting (Bio-Rad). We blocked membranes with 5% non-fat dried milk or 5% bovine serum albumin, incubated them overnight with primary antibody, washed thenHere is the JSON requested:

<a id='322df349-f245-4db8-8992-fe4d4867a2dd'></a>

## Reverse transcription qPCR

Cells were plated 2 days before experiments. Total RNA was extracted using High Pure RNA Isolation kit (Roche), and concentra- tion was determined by using a photospectrometer (NanoDrop 2000, Thermo Fisher Scientific). 1 µg of RNA sample was converted to complementary DNA using M-MuLV reverse transcriptase (NEB)

<a id='a91160f6-39f9-465f-a4ce-c26bb0574142'></a>

14 of 17

<a id='a0d2868b-2284-483a-a3a5-b65d1e3a57b7'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='c292f5ca-97ff-46fb-abcc-575451d187cb'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='676ea239-8ae0-4c9f-b910-a36b599a43bf'></a>

Jette Strasen et al Cell-specific TGFβ signaling

<a id='31e06030-0c67-49fa-8f27-46dfc6189856'></a>

Molecular Systems Biology

<a id='26b0db17-9789-4bb1-97fb-2ac10b7f7596'></a>

or Proto Script II reverse transcriptase (NEB) and oligo-dT primers.
Quantitative PCR was performed in triplicates using SYBR Green
reagent (Roche) on a StepOnePlus PCR machine (Applied Biosys-
tems). Primer sequences: β-actin forward, GGC ACC CAG CAC AAT
GAA GAT CAA; β-actin reverse, TAG AAG CAT TTG CGG TGG ACG
ATG; SnoN forward, GGCTGAATATGCAGGACAG SnoN reverse,
TGA GTT CAT CTT GGA GTT CTT G; SMAD7 forward, ACC CGA
TGG ATT TTC TCA AAC C SMAD7 reverse, GCC AGA TAA TTC
TAG CCC CCT; PAI1 forward, GGC TGA CTT CAC GAG TCT TTC A;
PAI1 reverse ATG CGG GCT GAG ACT ATG ACA.

<a id='5c761fca-1ff3-4387-8173-bb2a1cb0f011'></a>

## Immunofluorescence

Cells were plated 2 days before experiments on coverslips coated with poly-L-lysine (Sigma-Aldrich) and fixed at indicated time points with 2% paraformaldehyde. Cells were permeabilized with 0.1% Triton X-100 in PBS, blocked with 10% goat serum in PBS, incubated with primary antibody in 1% BSA in PBS, washed with 0.1% Triton X-100 in PBS, and incubated with secondary antibody conjugated with Alexa Fluor 488 (#A-11034) or Alexa Fluor 647 (#A-21245, Thermo Fisher Scientific) in 1% BSA in PBS. After washing, cells were stained with 2 µg/ml Hoechst in 0.1% Triton X-100/ PBS and embedded in Prolong Antifade (Thermo Fisher Scientific). Images were acquired with a 20x plan apo objective (NA 0.75) using appropriate filter sets. Automated segmentation was performed in MATLAB (MathWorks) with algorithms from CellProfiler (Carpenter et al, 2006).

<a id='b2726ea9-af04-4cc7-8735-7c946958b6bb'></a>

**Computational modeling**

Model simulations and fitting were performed using the MATLAB tool-
box Data2Dynamics (Raue *et al*, 2015). The implementation of the
model and the computational methods are described in Appendix III
and IV.

<a id='f76c25d0-f07a-4015-9acf-8d36e827adad'></a>

# Data availability

Reporter cell lines are available upon request. The primary datasets and mathematical models generated in this study are available in the following databases:

* Unprocessed single-cell data: Dryad Digital Repository (https://doi.org/10.5061/dryad.hc5dp).
* Mathematical models: BioModels Database (www.ebi.ac.uk/biomodels-main, MODEL1712050001 - MODEL17120500012).
* SED-ML scripts and simulations reproducing Figs 4C-H and 5A: JWS Online Simulation Database (https://jjj.bio.vu.nl/models/experiments/?id = strasen2018).

<a id='9c4a2146-1fea-4f0e-94cb-89085094dd9c'></a>

Expanded View for this article is available online.

<a id='76f3c0c7-05c8-4e93-9b9e-85acef81dd38'></a>

## Acknowledgements
We thank K. Janes and J. Brugge for providing MCF10A cells, Gitta Blendinger and Andrea Katzer for excellent technical assistance, and Lennart Schnirch for help establishing the SMAD7 knock-out cell line. SL and US were supported by NIH funding (NIH 1R01DK090347), by the e:bio junior group program (FKZ 0316196) and the Virtual Liver Network (FKZ 0316054) of the German Federal Ministry of Education and Research (BMBF).

<a id='afd657fe-0054-4f1c-bae2-21c6dc28a8f5'></a>

## Author contribution
JS and SB performed experiments, MJ data analysis and US mathematical modeling; CS contributed to generating the SMAD7 knock-out cell line; DH and PK performed TGF̒̒ measurements. JS, US, MJ, and AL prepared figures; SL and AL wrote the manuscript with contributions from all authors; SL and AL conceived the study and supervised the research.

<a id='0e3d837c-a4e7-4d30-9186-75e13f1c9468'></a>

## Conflict of interest
The authors declare that they have no conflict of interest.

<a id='227026e4-9fd1-41bd-abd8-5acc3e401c8d'></a>

# References
Abe M, Harpel JG, Metz CN, Nunes I, Loskutoff DJ, Rifkin DB (1994) An assay for transforming growth factor-beta using cells transfected with a plasminogen activator inhibitor-1 promoter-luciferase construct. Anal Biochem 216: 276–284
Adamson A, Boddington C, Downton P, Rowe W, Bagnall J, Lam C, Maya-Mendoza A, Schmidt L, Harper CV, Spiller DG, Rand DA, Jackson DA, White MRH, Paszek P (2016) Signal transduction controls heterogeneous NF-κB dynamics and target gene expression through cytokine-specific refractory states. Nat Commun 7: 12057
Ashall L, Horton CA, Nelson DE, Paszek P, Harper CV, Sillitoe K, Ryan S, Spiller DG, Unitt JF, Broomhead DS, Kell DB, Rand DA, See V, White MRH (2009) Pulsatile stimulation determines timing and specificity of NF-B-dependent transcription. Science 324: 242–246
Bar-Even A, Paulsson J, Maheshri N, Carmi M, O'Shea E, Pilpel Y, Barkai N (2006) Noise in protein expression scales with natural protein abundance. Nat Genet 38: 636–643
Carpenter AE, Jones TR, Lamprecht MR, Clarke C, Kang I, Friman O, Guertin DA, Chang J, Lindquist RA, Moffat J, Golland P, Sabatini DM (2006) Cell Profiler: image analysis software for identifying and quantifying cell phenotypes. Genome Biol 7: R100
Chang HH, Hemberg M, Barahona M, Ingber DE, Huang S (2008) Transcriptome-wide noise controls lineage choice in mammalian progenitor cells. Nature 453: 544–547
Chen Y-G, Meng AM (2004) Negative regulation of TGF-beta signaling in development. Cell Res 14: 441–449
Clarke DC, Liu X (2008) Decoding the quantitative nature of TGF-β/Smad signaling. Trends Cell Biol 18: 430–442
Clarke DC, Brown ML, Erickson RA, Shi Y, Liu X (2009) Transforming growth factor beta depletion is the primary determinant of Smad signaling kinetics. Mol Cell Biol 29: 2443–2455
Cohen AA, Geva-Zatorsky N, Eden E, Frenkel-Morgenstern M, Issaeva I, Sigal A, Milo R, Cohen-Saidon C, Liron Y, Kam Z, Cohen L, Danon T, Perzov N, Alon U (2008) Dynamic proteomics of individual cancer cells in response to a drug. Science 322: 1511–1516
Colman-Lerner A, Gordon A, Serra E, Chin T, Resnekov O, Endy D, Pesce CG, Brent R (2005) Regulated cell-to-cell variation in a cell-fate decision system. Nature 437: 699–706
Debnath J, Muthuswamy SK, Brugge JS (2003) Morphogenesis and oncogenesis of MCF-10A mammary epithelial acini grown in three-dimensional basement membrane cultures. Methods 30: 256–268
Di Guglielmo GM, Le Roy C, Goodfellow AF, Wrana JL (2003) Distinct endocytic pathways regulate TGF-β receptor signalling and turnover. Nat Cell Biol 5: 410–421
Elowitz MB, Levine AJ, Siggia ED, Swain PS (2002) Stochastic gene expression in a single cell. Science 297: 1183–1186

<a id='8eba58ad-15d0-4821-80ab-59c7a3a89c12'></a>

© 2018 The Authors

<a id='45a31b19-3daf-4be3-8d3d-59561330839b'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='69e126fb-1541-4a89-b881-af8bb4146aa9'></a>

15 of 17

<!-- PAGE BREAK -->

<a id='f9b7b520-0ab6-40fa-9b51-0e567cabe90f'></a>

Molecular Systems Biology

<a id='e21ff862-bd92-4376-899e-78d8fc119b9a'></a>

Cell-specific TGFβ signaling

<a id='4e0a2611-2099-4d62-8954-b11977e35823'></a>

Jette Strasen et al

<a id='93d4c7ac-f764-4f5b-a808-2f4691ec20db'></a>

Feinerman O, Veiga J, Dorfman JR, Germain RN, Altan-Bonnet G (2008)
Variability and robustness in T cell activation from regulated
heterogeneity in protein levels. Science 321: 1081–1084
Feng X-H, Derynck R (2005) Specificity and versatility in tgf-beta signaling
through Smads. Annu Rev Cell Dev Biol 21: 659–693
Frechin M, Stoeger T, Daetwyler S, Gehin C, Battich N, Damm E-M, Stergiou L,
Riezman H, Pelkmans L (2015) Cell-intrinsic adaptation of lipid
composition to local crowding drives social behaviour. Nature 523: 88–91
Gaudet S, Spencer SL, Chen WW, Sorger PK (2012) Exploring the contextual
sensitivity of factors that determine cell-to-cell variability in receptor-
mediated apoptosis. PLoS Comput Biol 8: e1002482
Geva-Zatorsky N, Rosenfeld N, Itzkovitz S, Milo R, Sigal A, Dekel E, Yarnitzky
T, Liron Y, Polak P, Lahav G, Alon U (2006) Oscillations and variability in
the p53 system. Mol Syst Biol 2: 2006.0033
Giampieri S, Manning C, Hooper S, Jones L, Hill CS, Sahai E (2009) Localized
and reversible TGFβ signalling switches breast cancer cells from cohesive
to single cell motility. Nat Cell Biol 11: 1287–1296
Gonzalez DM, Medici D (2014) Signaling mechanisms of the epithelial-
mesenchymal transition. Sci Signal 7: re8
Goolam M, Scialdone A, Graham SJL, Macaulay IC, Jedrusik A, Hupalowska A,
Voet T, Marioni JC, Zernicka-Goetz M (2016) Heterogeneity in Oct4 and
Sox2 targets biases cell fate in 4-cell mouse embryos. Cell 165: 61–74
Guo X, Wang X-F (2009) Signaling cross-talk between TGF-B/BMP and other
pathways. Cell Res 19: 71–88
Gurdon JB, Dyson S, St Johnston D (1998) Cells’ perception of position in a
concentration gradient. Cell 95: 159–162
Haghverdi L, Büttner M, Wolf FA, Buettner F, Theis FJ (2016) Diffusion pseudotime
robustly reconstructs lineage branching. Nat Methods 13: 845–848
Heldin C-H, Landström M, Moustakas A (2009) Mechanism of TGF-β signaling
to growth arrest, apoptosis, and epithelial–mesenchymal transition. Curr
Opin Cell Biol 21: 166–176
Ikushima H, Miyazono K (2010) TGFβ signalling: a complex web in cancer
progression. Nat Rev Cancer 10: 415–424
Inman GJ, Nicolás FJ, Hill CS (2002) Nucleocytoplasmic shuttling of Smads 2, 3,
and 4 permits sensing of TGF-beta receptor activity. Mol Cell 10: 283–294
Kallenberger SM, Beaudouin J, Claus J, Fischer C, Sorger PK, Legewie S, Eils R
(2014) Intra- and interdimeric caspase-8 self-cleavage controls strength
and timing of CD95-induced apoptosis. Sci Signal 7: ra23
Koli KM, Arteaga CL (1997) Processing of the transforming growth factor beta
type I and II receptors. Biosynthesis and ligand-induced regulation. J Biol
Chem 272: 6423–6427
Lee REC, Walker SR, Savery K, Frank DA, Gaudet S (2014) Fold change of
nuclear NF-kB determines TNF-induced transcription in single cells. Mol
Cell 53: 867–879
Legewie S, Herzel H, Westerhoff HV, Blüthgen N (2008) Recurrent design
patterns in the feedback regulation of the mammalian signalling network.
Mol Syst Biol 4: 190
Leibler S, Barkai N (1997) Robustness in simple biochemical networks. Nature
387: 913–917
Lestas I, Vinnicombe G, Paulsson J (2010) Fundamental limits on the
suppression of molecular fluctuations. Nature 467: 174–178
Li Q, Zhang D, Wang Y, Sun P, Hou X, Larner J, Xiong W, Mi J (2013) MiR-21/
Smad 7 signaling determines TGF-B1-induced CAF formation. Sci Rep 3: 512
Lin X, Duan X, Liang Y-Y, Su Y, Wrighton KH, Long J, Hu M, Davis CM, Wang J,
Brunicardi FC, Shi Y, Chen Y-G, Meng A, Feng X-H (2006) PPM1A functions
as a smad phosphatase to terminate TGFβ signaling. Cell 125: 915–928
Loewer A, Lahav G (2011) We are all individuals: causes and consequences of non-
genetic heterogeneity in mammalian cells. Curr Opin Genet Dev 21: 753–758

<a id='b3f3a8ba-983a-4f9e-9ec5-dd77b576af89'></a>

Ma W, Trusina A, El-Samad H, Lim WA, Tang C (2009) Defining network
topologies that can achieve biochemical adaptation. Cell 138: 760–773
Massagué J, Kelly B (1986) Internalization of transforming growth factor-beta
and its receptor in BALB/c 3T3 fibroblasts. J Cell Physiol 128: 216–222
Massagué J (2005) Smad transcription factors. Genes Dev 19: 2783–2810
Moustakas A, Heldin CH (2009) The regulation of TGF signal transduction.
Development 136: 3699–3714
Mullen AC, Orlando DA, Newman JJ, Lovén J, Kumar RM, Bilodeau S, Reddy J,
Guenther MG, DeKoter RP, Young RA (2011) Master transcription factors
determine cell-type-specific responses to TGF-β signaling. Cell 147: 565–576
Nallet-Staub F, Yin X, Gilbert C, Marsaud V, Ben Mimoun S, Javelaud D, Leof
EB, Mauviel A (2015) Cell density sensing alters TGF-β signaling in a cell-
type-specific manner, independent from Hippo pathway activation. Dev
Cell 32: 640–651
Nelson DE, Ihekwaba AEC, Elliott M, Johnson JR, Gibney CA, Foreman BE,
Nelson G, See V, Horton CA, Spiller DG, Edwards SW, McDowell HP, Unitt
JF, Sullivan E, Grimley R, Benson N, Broomhead D, Kell DB, White MRH
(2004) Oscillations in NF-kappaB signaling control the dynamics of gene
expression. Science 306: 704–708
Newman JRS, Ghaemmaghami S, Ihmels J, Breslow DK, Noble M, DeRisi JL,
Weissman JS (2006) Single-cell proteomic analysis of S. cerevisiae reveals
the architecture of biological noise. Nat Cell Biol 441: 840–846
Nicolás FJ, Hill CS (2003) Attenuation of the TGF-beta-Smad signaling
pathway in pancreatic tumor cells confers resistance to TGF-beta-induced
growth arrest. Oncogene 22: 3698–3711
Paek AL, Liu JC, Loewer A, Forrester WC, Lahav G (2016) Cell-to-cell variation
in p53 dynamics leads to fractional killing. Cell 165: 631–642
Paulsen M, Legewie S, Eils R, Karaulanov E, Niehrs C (2011) Negative
feedback in the bone morphogenetic protein 4 (BMP4) synexpression
group governs its dynamic signaling range and canalizes development.
Proc Natl Acad Sci USA 108: 10202–10207
Pedraza JM, Paulsson J (2008) Effects of molecular memory and bursting on
fluctuations in gene expression. Science 319: 339–343
Piek E, Ju WJ, Heyer J, Escalante-Alcalde D, Stewart CL, Weinstein M, Deng C,
Kucherlapati R, Böttinger EP, Roberts AB (2001) Functional
characterization of transforming growth factor beta signaling in Smad2-
and Smad3-deficient fibroblasts. J Biol Chem 276: 19945–19953
Pierreux CE, Nicolas FJ, Hill CS (2000) Transforming growth factor beta-
independent shuttling of Smad4 between the cytoplasm and nucleus. Mol
Cell Biol 20: 9041–9054
Purvis JE, Karhohs KW, Mock C, Batchelor E, Loewer A, Lahav G (2012) p53
dynamics control cell fate. Science 336: 1440–1444
Purvis JE, Lahav G (2013) Encoding and decoding cellular information
through signaling dynamics. Cell 152: 945–956
Rand U, Rinas M, Schwerk J, Nöhren G, Linnes M, Kröger A, Flossdorf M, Kály-
Kullai K, Hauser H, Höfer T, Köster M (2012) Multi-layered stochasticity
and paracrine signal propagation shape the type-I interferon response.
Mol Syst Biol 8: 584
Raue A, Steiert B, Schelker M, Kreutz C, Maiwald T, Hass H, Vanlier J, Tönsing
C, Adlung L, Engesser R, Mader W, Heinemann T, Hasenauer J, Schilling M,
Höfer T, Klipp E, Theis F, Klingmüller U, Schöberl B, Timmer J (2015)
Data2Dynamics: a modeling environment tailored to parameter estimation
in dynamical systems. Bioinformatics 31: 3558–3560
Rhee A, Cheong R, Levchenko A (2014) Noise decomposition of intracellular
biochemical signaling networks using nonequivalent reporters. Proc Natl
Acad Sci USA 111: 17330–17335
Rosenfeld N, Elowitz MB, Alon U (2002) Negative autoregulation speeds the
response times of transcription networks. J Mol Biol 323: 785–793

<a id='2edd5f21-7c0f-4f26-979d-0fca39d488ce'></a>

16 of 17

<a id='e0ee2077-bd2f-4c24-8d0d-10beefa57220'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='52970c5d-9f25-4671-bbea-4ecf3f95989c'></a>

© 2018 The Authors

<!-- PAGE BREAK -->

<a id='32467c59-9ab9-4849-a977-a8deb2683a11'></a>

Jette Strasen et al Cell-specific TGFβ signaling

<a id='d6d61fe5-b9ed-475e-bb76-04ea96244a47'></a>

Molecular Systems Biology

<a id='09a645cd-6630-4587-ad81-7f3ab950a75d'></a>

Sakoe H, Chiba S (1978) Dynamic programming algorithm optimization for spoken word recognition. IEEE Trans Acoust Speech Signal Process 26: 43–49
Sandler O, Mizrahi SP, Weiss N, Agam O, Simon I, Balaban NQ (2015) Lineage correlations of single cell division time as a probe of cell-cycle dynamics. Nature 519: 468–471
Schmierer B, Hill CS (2005) Kinetic analysis of smad nucleocytoplasmic shuttling reveals a mechanism for transforming growth factor -dependent nuclear accumulation of smads. Mol Cell Biol 25: 9845–9858
Schmierer B, Hill CS (2007) TGFβ–SMAD signal transduction: molecular specificity and functional flexibility. Nat Rev Mol Cell Biol 8: 970–982
Schmierer B, Tournier AL, Bates PA, Hill CS (2008) Mathematical modeling identifies Smad nucleocytoplasmic shuttling as a dynamic signal-interpreting system. Proc Natl Acad Sci USA 105: 6608–6613
Schneider CA, Rasband WS, Eliceiri KW (2012) NIH image to Image): 25 years of image analysis. Nat Methods 9: 671–675
Shalem O, Sanjana NE, Hartenian E, Shi X, Scott DA, Mikkelsen TS, Heckl D, Ebert BL, Root DE, Doench JG, Zhang F (2014) Genome-scale CRISPR-Cas9 knockout screening in human cells. Science 343: 84–87
Sharma SV, Lee DY, Li B, Quinlan MP, Takahashi F, Maheswaran S, McDermott U, Azizian N, Zou L, Fischbach MA, Wong K-K, Brandstetter K, Wittner B, Ramaswamy S, Classon M, Settleman J (2010) A chromatin-mediated reversible drug-tolerant state in cancer cell subpopulations. Cell 141: 69–80
Sherman MS, Lorenz K, Lanier MH, Cohen BA (2015) Cell-to-cell variability in the propensity to transcribe explains correlated fluctuations in gene expression. Cell Syst 1: 315–325
Shukla MN, Rose JL, Ray R, Lathrop KL, Ray A, Ray P (2009) Hepatocyte growth factor inhibits epithelial to myofibroblast transition in lung cells via Smad7. Am J Respir Cell Mol Biol 40: 643–653
Sigal A, Milo R, Cohen A, Geva-Zatorsky N, Klein Y, Alaluf I, Swerdlin N, Perzov N, Danon T, Liron Y, Raveh T, Carpenter AE, Lahav G, Alon U (2006a) Dynamic proteomics in individual human cells uncovers widespread cell-cycle dependence of nuclear proteins. Nat Methods 3: 525–531
Sigal A, Milo R, Cohen A, Geva-Zatorsky N, Klein Y, Liron Y, Rosenfeld N, Danon T, Perzov N, Alon U (2006b) Variability and memory of protein levels in human cells. Nature 444: 643–646
Snijder B, Sacher R, Rämö P, Damm E-M, Liberali P, Pelkmans L (2009) Population context determines cell-to-cell variability in endocytosis and virus infection. Nature 461: 520–523
Snijder B, Pelkmans L (2011) Origins of regulated cell-to-cell variability. Nat Rev Mol Cell Biol 12: 119–125
Sorre B, Warmflash A, Brivanlou AH, Siggia ED (2014) Encoding of temporal signals by the TGF-β pathway and implications for embryonic patterning. Dev Cell 30: 334–342
Spencer SL, Gaudet S, Albeck JG, Burke JM, Sorger PK (2009) Non-genetic origins of cell-to-cell variability in TRAIL-induced apoptosis. Nature 459: 428–432
Spiller DG, Wood CD, Rand DA, White MRH (2010) Measurement of single-cell dynamics. Nature 465: 736–745
Tay S, Hughey JJ, Lee TK, Lipniacki T, Quake SR, Covert MW (2010) Single-cell NF-κB dynamics reveal digital activation and analogue information processing. Nature 466: 267–271
Tsunobuchi H, Ishisaki A, Imamura T (2004) Expressions of inhibitory Smads, Smad6 and Smad7, are differentially regulated by TPA in human lung fibroblast cells. Biochem Biophys Res Commun 316: 712–719
Ulloa L, Doody J, Massagué J (1999) Inhibition of transforming growth factor-beta/SMAD signalling by the interferon-gamma/STAT pathway. Nature 397: 710–713

<a id='3c3a801f-0b25-4625-a2da-24241566b05a'></a>

Valdimarsdottir G, Goumans M-J, Itoh F, Itoh S, Heldin C-H, ten Dijke P
(2006) Smad7 and protein phosphatase 1alpha are critical determinants
in the duration of TGF-beta/ALK1 signaling in endothelial cells. BMC Cell
Biol 7: 16
Villaseñor R, Nonaka H, Del Conte-Zerial P, Kalaidzidis Y, Zerial M, Pfeffer SR
(2015) Regulation of EGFR signal transduction by analogue-to-digital
conversion in endosomes. eLife 4: e06156
Vizan P, Miller DSJ, Gori I, Das D, Schmierer B, Hill CS (2013) Controlling long-
term signaling: receptor dynamics determine attenuation and refractory
behavior of the TGF- pathway. Sci Signal 6: ra106
Voliotis M, Perrett RM, McWilliams C, McArdle CA, Bowsher CG (2014)
Information transfer by leaky, heterogeneous, protein kinase signaling
systems. Proc Natl Acad Sci USA 111: E326-E333
Wang J, Tucker-Kellogg L, Ng IC, Jia R, Thiagarajan PS, White JK, Yu H (2014a)
The self-limiting dynamics of TGF-β signaling in silico and in vitro, with
negative feedback through PPM1A upregulation. PLoS Comput Biol 10:
e1003573
Wang T, Wei JJ, Sabatini DM, Lander ES (2014b) Genetic screens in human
cells using the CRISPR-Cas9 system. Science 343: 80-84
Warmflash A, Zhang Q, Sorre B, Vonica A, Siggia ED, Brivanlou AH (2012)
Dynamics of TGF- signaling reveal adaptive and pulsatile behaviors
reflected in the nuclear localization of transcription factor Smad4. Proc
Natl Acad Sci USA 109: E1947-E1956
Wegner K, Bachmann A, Schad J-U, Lucarelli P, Sahle S, Nickel P, Meyer C,
Klingmüller U, Dooley S, Kummer U (2012) Dynamics and feedback loops
in the transforming growth factor β signaling pathway. Biophys Chem 162:
22-34
Weinberger LS, Burnett JC, Toettcher JE, Arkin AP, Schaffer DV (2005)
Stochastic gene expression in a lentiviral positive-feedback loop: HIV-1 Tat
fluctuations drive phenotypic diversity. Cell 122: 169-182
Yao J, Pilko A, Wollman R (2016) Distinct cellular states determine calcium
signaling&nbsp;response. Mol Syst Biol 12: 894
Yi TM, Huang Y, Simon MI, Doyle J (2000) Robust perfect adaptation in
bacterial chemotaxis through integral feedback control. Proc Natl Acad Sci
USA 97: 4649-4653
Yu RC, Pesce CG, Colman-Lerner A, Lok L, Pincus D, Serra E, Holl M, Benjamin
K, Gordon A, Brent R (2008) Negative feedback that improves information
transmission in yeast signalling. Nature 456: 755-761
Zhang J, Tian X-J, Zhang H, Teng Y, Li R, Bai F, Elankumaran S, Xing J
(2014) TGF-β-induced epithelial-to-mesenchymal transition proceeds
through stepwise activation of multiple feedback loops. Sci Signal 7:
ra91
Zi Z, Feng Z, Chapnick DA, Dahl M, Deng D, Klipp E, Moustakas A, Liu X
(2011) Quantitative analysis of transient and sustained transforming
growth factor-β signaling dynamics. Mol Syst Biol 7: 492
Zi Z, Chapnick DA, Liu X (2012) Dynamics of TGF-B/Smad signaling. FEBS Lett
586: 1921-1928
Zieba A, Pardali K, Söderberg O, Lindbom L, Nyström E, Moustakas A, Heldin
C-H, Landegren U (2012) Intercellular variation in signaling through the
TGF-B pathway and its relation to cell density and cell cycle phase. Mol
Cell Proteomics 11: M111.013482

<a id='c8250519-7e72-4064-9ca6-9f155b4d4fe7'></a>

CC
BY
License: This is an open access article under the terms of the Creative Commons Attribution 4.0 License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

<a id='d1d13231-725f-4915-8965-cb6cb9c9346f'></a>

© 2018 The Authors

<a id='e03f2bb9-666f-40ce-9d92-950e83ec3678'></a>

Molecular Systems Biology 14: e7733 | 2018

<a id='f27a5775-7325-4d02-9e37-bc05773134f4'></a>

17 of 17