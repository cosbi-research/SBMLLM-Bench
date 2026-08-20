<a id='4743361a-2276-4b8e-bc25-3c856b09abb0'></a>

Check for updates

<a id='4b1e3225-a02f-4302-93a5-8031199ef5ab'></a>

The FASEB Journal • Research Communication

<a id='15a2df94-11b0-462c-b91f-922207bac0d8'></a>

Network topology determines dynamics of the
mammalian MAPK1,2 signaling network: bifan motif
regulation of C-Raf and B-Raf isoforms by FGFR
and MC1R

<a id='b57758e6-de47-45eb-bdd2-6258b293234b'></a>

Melissa Muller, Mandri Obeyesekere, Gordon B. Mills, and Prahlad T. Ram
Department of Systems Biology, University of Texas M.D. Anderson Cancer Center, Houston, Texas, USA

<a id='557a5ce5-2ccf-462d-8fd9-32f8de896639'></a>

ABSTRACT Activation of the fibroblast growth factor (FGFR) and melanocyte stimulating hormone (MC1R) receptors stimulates B-Raf and C-Raf isoforms that regulate the dynamics of MAPK1,2 signaling. Network topology motifs in mammalian cells include feed-forward and feedback loops and bifans where signals from two upstream molecules integrate to modulate the activity of two downstream molecules. We computationally modeled and experimentally tested signal processing in the FGFR/MC1R/B-Raf/C-Raf/MAPK1,2 network in human melanoma cells; identifying 7 regulatory loops and a bifan motif. Signaling from FGFR leads to sustained activation of MAPK1,2, whereas signaling from MC1R results in transient activation of MAPK1,2. The dynamics of MAPK activation depends critically on the expression level and connectivity to C-Raf, which is critical for a sustained MAPK1,2 response. A partially incoherent bifan motif with a feedback loop acts as a logic gate to integrate signals and regulate duration of activation of the MAPK signaling cascade. Further reducing a 106-node ordinary differential equations network encompassing the complete network to a 6-node network encompassing rate-limiting processes sustains the feedback loops and the bifan, providing sufficient information to predict biological responses.-Muller, M., Obeyesekere, M., Mills, G. B., Ram., P. T. Network topology determines dynamics of the mammalian MAPK1,2 signaling network: bifan motif regulation of C-Raf and B-Raf isoforms by FGFR and MC1R. FASEB J. 22, 1393-1403 (2008)

<a id='2ae6f295-764d-40c8-84b6-4811cad2eaa9'></a>

Key Words: computational modeling • proteomics • melanoma

<a id='0299fa50-240b-41fb-b30f-2716173b28ed'></a>

B-RAF IS MUTATIONALLY ACTIVATED in 60-80% of malignant melanomas as well as a large number of benign nevi, indicating a role in the initiation of malignant melanoma. Melanoma is the most aggressive form of skin cancer. Recently, protein kinase inhibitors have demonstrated remarkable clinical benefit in diseases that have been resistant to traditional chemotherapy, including chronic myelogenous leukemia (CML), gastrointestinal stromal tumors (GISTs), HER2/Neu- amplified breast cancer, and renal cell carcinoma (1-

<a id='83276811-7d82-49f3-b547-c6685440261d'></a>

8). Each of these diseases is characterized by genetic aberrations that activate protein signaling networks, which appears to be critical to the efficacy of protein kinase inhibitors. Activating mutations of B-Raf result in constitutive activation (phosphorylation) of MAPK (9, 10). This pathway is also activated by mutation of N-Ras, which occurs in ~15% of melanomas (11, 12). Mutant N-Ras activates the RAS-RAF-MEK-MAPK as well as the PI3K-AKT-mTOR pathways in vitro. Mutations of B-Raf and N-Ras appear to be mutually exclusive in melanoma tumors and cell lines (12-14).

<a id='7100bb6d-8251-495d-8ba8-8e7d7f4db6a4'></a>

The high prevalence of activating mutations of com-ponents of the RAS-RAF-MEK-MAPK pathway suggests that it may be an effective therapeutic target in mela-noma. The first B-Raf inhibitor to be used in clinical trials is sorafenib (Nexavar®), also known as BAY43-9006 (15). Sorafenib is a small molecule inhibitor of wild-type B-Raf, mutant (V600E) B-Raf, and a number of tyrosine kinase receptors (16). A Phase II single-agent study in patients with metastatic melanoma yielded disappointing results (16). Among 20 patients, only 1 partial response was observed, and 3 patients had stable disease. The lack of a complete understanding of the underlying homeostatic mechanisms regulating the RAS/RAF/MEK/MAPK pathway and the effects of B-Raf mutations on this pathway may contribute to the failure of monotherapy targeting individual compo-nents of the pathway. We thus sought to further define the homeostatic mechanisms controlling information transfer through the RAS/RAF/MEK/MAPK pathway (17).

<a id='373c702d-3fa2-46cf-a85f-e4bb1a161e33'></a>

Analysis of mammalian signaling networks shows that
a large percentage of signaling subnetwork motifs are
feed-forward/feedback loops and bifans (18). A recent
analysis of network motifs of a 545 component 1259
interaction mammalian signaling network revealed 300
feed-forward loops and 1000 bifan subnetworks (18).
The role these network motifs play in regulating signal-
ing is not entirely clear. These subnetwork motifs could

<a id='ba8ffdf0-7d32-4297-bf45-870cd23580fb'></a>

¹ Correspondence: Department of Systems Biology, Unit 950, UT M.D. Anderson Cancer Center, 7435 Fannin St., Houston, TX 77054, USA. E-mail: pram@mdanderson.org doi: 10.1096/fj.07-9100com

<a id='9d5184bd-7f60-4a0a-bf3f-72631b0be801'></a>

0892-6638/08/0022-1393 © FASEB

<a id='93a8a82b-4bf4-46f6-81f3-dcce41565a72'></a>

1393

<!-- PAGE BREAK -->

<a id='b0de5b10-108d-4923-aa24-89102c8511db'></a>

serve both to prolong signaling on initiation by a
stimuli and also to terminate the signal (18–20). Given
the high frequency of occurrence of bifan motifs in
signaling and transcriptional networks (18, 21), we
investigated whether coherent or incoherent bifan mo-
tifs regulate the mammalian MAPK1,2 network.

<a id='3265cfb3-3940-48bb-890a-ec5d895727fd'></a>

Signaling networks receive inputs from multiple up-stream stimuli or receptor and must appropriately process this information into a clear message that results in the appropriate cellular outcomes. The MAPK1,2 network can be activated by signals from RTKs that activate Ras-C-Raf (22) and also by GPCR signals that activate B-Raf in a cAMP-dependent manner (23, 24) (see Supplemental Figs. S1 and S2). Signals from the Gαs-cAMP pathway also activate protein kinase A (PKA), which in turn phosphorylates C-Raf at Ser-259 and causes C-Raf to bind 14-3-3 proteins rendering C-Raf inactive (25-28). Identified feedback loops in this network include a positive feedback loop from MAPK1,2 involving PKC and potentially C-Raf (20), a negative loop from MAPK1,2 to B-Raf (29), a negative feedback loop from MAPK to C-Raf (30), a positive feedback loop from MAPK to C-Raf (31), and a feed-forward loop from PKC to adenylyl cyclase (32) (See Supplemental Figs. S2A, B and S3A, B, D and Fig. 2A). In summary, these interactions form a partially incoherent bifan, where C-Raf receives a positive and a negative input from FGFR and MC1R, respectively, while B-Raf receives positive inputs from both receptors. Given this complexity in connectivity within the GPCR-RTK-MAPK network, it is a priori difficult to understand how signals are processed to modulate the temporal duration of MAPK1,2 activity and what molecules and motifs can regulate the response. However, a computational model incorporating these concepts offers the potential to both characterize the dynamics of signal transduction through a network and define combinational therapies that could improve patient outcome.

<a id='ea495990-cbc0-43b1-979b-76fd669470ed'></a>

Sustained vs. transient activation of signaling molecules and pathways is an important regulatory mechanism within the cell. For example, sustained activation of MAPK1,2 (90 min or more) has been shown to increase gene expression and activation of c-Fos leading to cellular proliferation, whereas the transient activation of MAPK1,2 (less than 30 min) does not activate c-Fos (33, 34). Similar effects are seen in NFkB signaling, where a transient or a sustained activation results in distinct changes in gene expression (35). Physiological responses such as differentiation and cell division are often dependent on temporal duration of activation of signaling molecules such as MAPK1,2 (36, 37). We have previously shown that the MAPK1,2 network can exists as a bistable system and can elicit either a sustained or transient response (20).

<a id='c764d702-dfd7-4a21-a1d3-ad32ba25055d'></a>

In this study, we determined how bifan and loop
motifs regulate the system properties of the mamma-
lian MAPK1,2 network in human melanoma cells. To
address this problem, we used an integrated approach
of computational modeling and experimental analysis.

<a id='eb769152-d2fd-4bf4-88b1-754bb53de2ed'></a>

For the experimental analysis, we used SB2 human melanoma cells. This model system and cell line were chosen for several reasons. Melanocytes and melanoma cell lines endogenously express both fibroblast growth factor receptor (FGFR) (38) as well melanocortin 1 receptor (MC1R) (39), which are important in their biology and the pathophysiology of melanoma. Fibroblast growth factor is an important mitogen for melanoma cells (40), and the melanocortin 1 receptor, which is coupled to Gs, is important in normal biology as well as in the pathophysiology of melanoma (41). Single-nucleotide polymorphisms of the MC1R that result in a loss-of-function variant of the receptor are a risk factor for the development of melanoma (42). At the signaling level, B-Raf mutations occur in ~70% of melanomas, and B-Raf is a target for therapy (10). The cell line we have used in this study endogenously expresses FGFR and MC1R, as well as wild-type B-Raf and C-Raf, and contains the V90 MC1R loss-of-function SNP. The computational model encompassed ordinary differential equations (ODE) to simulate the MAPK1,2 signaling network.

<a id='e06f182b-a41a-4079-801a-959282345e8d'></a>

# MATERIALS AND METHODS

## Computational modeling

Two computational models were developed: Model A, a detailed 106 ODE system; and Model B, a reduced 6 ODE system. A previously published MAPK1,2 network model (20) and a published Gs-PKA module (43) were integrated to form Model A. The same parameter values and rate constants were used, except for FGF and FGFR, the values for which are in Table S1. These two models were connected by the following interactions: 1) cAMP binding and activation of cAMP-GEF; 2) cAMP-GEF activation of Ras; 3) Ras activation of B-Raf; 4) B-Raf activation of MEK1; 5) PKA phosphorylation of Ser-259 of C-Raf; and 6) PP2A dephosphorylation of Ser-259 C-Raf. The connection from cAMP-GEF to B-Raf is mediated by a small G protein. The small G protein it is most commonly reported as Rap in many cell types. However, in melanoma it is not clear whether cAMP-GEF activates Rap or Ras. Regarding melanoma cells, Busca et al. (24) and Dumaz et al. (9) present data to suggest that Ras mediates the cAMP signal; whereas Gao et al. (44) suggest that Rap mediates the cAMP signal. Since the connection from cAMP-GEF to Rap/Ras is not well defined in melanoma, we chose to use the cAMP-GEF to Ras connection for the model. A coupled ordinary differential equation computational model of the network was developed and solved in Genesis/Kinetikit (19). Parameter variation analysis was done on the network through iterations of modeling and experimental analysis. A parameter set was chosen such that the model output closely matched the experimental data. These parameter values were used for subsequent simulations. The biochemical parameters and concentrations that were used for the added components are shown in Supplemental Table S1. The second model, Model B, of the reduced network was built and solved using MatLab. The parameters and constants are shown in Supplemental Table S2.

<a id='9c5fdfeb-8179-4a34-96c8-4acd4fd5a548'></a>

## Cell culture and stimulation
Human SB2 melanoma cells were kindly provided by Dr. Menashe Bar-Eli (M.D. Anderson Cancer Center, Houston,

<a id='cfaa249e-5486-4637-8a9e-ac5776e14fe9'></a>

1394 Vol. 22 May 2008

<a id='88f6580e-365f-45b7-aa16-040d957f0fff'></a>

The FASEB Journal

<a id='c674476c-c66c-463f-b5cb-374f8a0c1ec4'></a>

MULLER ET AL.

<a id='2df1607f-fda6-4603-9415-dc1c1bfdd284'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='61ccef02-f5b5-43c2-b435-fe3ce64da0e9'></a>

TX, USA). SB2 melanoma cells endogenously express wild-type B-Raf, C-Raf, FGFR, and the V90 MC1R SNP (unpublished results, Drs. J. Ellerhorst and E. Grimm, Department of Experimental Therapeutics, University of Texas M.D. Anderson Cancer Center, Houston, TX, USA).
Cells were routinely maintained in modified essential medium supplemented with 10% FBS. For signaling experiments, logarithmically growing cells were starved in 1% FBS for 16 h and then subjected to stimulations using basic fibroblast growth factor (FGF 20 ng/ml) (Cell Signaling Technology, Danvers, MA, USA) and/or melanocyte stimulating hormone (MSH, 2 μM; Sigma-Aldrich, St. Louis, MO, USA). For washout experiments, cells were stimulated with fibroblast growth factor (FGF) and/or MSH for 5 min, washed, and incubated at 37°C in 1% medium for time periods indicated in figure legends. Where specified, cells were pretreated with the PKA inhibitor H89 (20 μM) for 2 h prior to incubation with FGF and/or MSH. Controls were incubated for corresponding times with dimethyl sulfoxide. For some experiments, cells were treated with short interfering RNA (siRNA) for 48 h prior to treatment to knock down C-Raf (Cell Signaling Technology).

<a id='44278ccd-b777-412e-ad8a-080419ad667f'></a>

## Antibodies
The following antibodies were used for immunoblotting and reverse phase protein microarrays (RPPAs): antiphospho-p44/42 MAPK, p42MAPK (Cell Signaling Technology); anti-C-Raf (Upstate Biotechnology, Waltham, MA, USA); and anti-β-Actin (Sigma-Aldrich).

<a id='f801af50-d926-486b-95ad-adb8a87e9fbd'></a>

# SDS-PAGE and immunoblotting

Cells were lysed by incubation on ice for 15 min in a sample lysis buffer (50 mM HEPES; 150 mM NaCl; 1 mM EGTA; 10 mM sodium pyrophosphate, pH 7.4; 100 nM NaF; 1.5 mM MgCl2; 10% glycerol; and 1% Triton X-100 plus protease inhibitors aprotinin, bestatin, leupeptin, E-64, and pepstatin A). Cell lysates were centrifuged at 15,000 g for 20 min at 4°C. The supernatant was frozen and stored at -20°C. Protein concentrations were determined using a protein-assay system (BCA, Bio-Rad, Hercules, CA, USA), with BSA as a standard.

For immunoblotting, proteins (25 µg) were separated by SDS-PAGE and transferred to Hybond-C membrane (GE Healthcare, Piscataway, NJ, USA). Blots were blocked for 60 min and incubated with primary antibodies overnight, followed by goat anti-mouse IgG-HRP (1:30,000; Cell Signaling Technology) or goat anti-rabbit IgG-HRP (1:10,000; Cell Signaling Technology) for 1 h. Secondary antibodies were detected by enhanced chemiluminescence (ECL) reagent (GE Healthcare). All experiments were repeated a minimum of three independent times.

<a id='fef68452-0d86-41ff-b782-13fa2e3757ef'></a>

RPPA

Lysates were prepared as for Western blotting. Cell lysates
(1 μg/µl) were boiled in 1% SDS and hybridized under
stringent conditions mimicking the conditions used in
Western blotting. Using a GeneTac G3 DNA arrayer
(Genomic Solutions, Ann Arbor, MI, USA), seven two-fold
serial dilutions of cell lysates are arrayed on multiple
nitrocellulose-coated glass slides (FAST Slides, Whatman
Schleicher & Schuell, Keene, NH, USA). RPPA slides were
produced in batches of 20. Printed slides were stored in
desiccant at -20°C. Antibodies were screened for specific-
ity by Western blotting with 25 µg of lysate protein per
lane. An antibody was accepted only if it produced a single
predominant band at the expected molecular weight and

<a id='881de7e7-c7e3-4128-bacc-58d5ceba8aa5'></a>

where proteins behaved similarly on Western blotting and arrays following manipulation of signaling pathways or across multiple cell lines with a wide dynamic range. Each array was incubated with specific primary antibody, which was detected by using the catalyzed signal amplification (CSA) system (DAKO, Carpinteria, CA, USA). Briefly, each slide was washed in a mild stripping solution of Re-Blot Plus (Chemicon International, Temecula, CA, USA) then blocked with I-block (Tropix, Bedford, MA, USA) for at 30 min. Following the DAKO universal staining system, slides were then incubated with hydrogen peroxide, followed by avidin for 5 min, and biotin for 5 min. Slides were incubated with primary and secondary antibodies then incubated with streptavidin-peroxidase for 15 min, biotinyl tyramide (for amplification) for 15 min, and 3,3-diamino- benzidine tetrahydrochloride chromogen for 5 min. Between steps, the slide was washed with TBS-T buffer. Loading is determined by comparing phosphorylated and nonphosphorylated antibodies. Multiple controls are placed on each slide to facilitate quantification and valida- tion of the assay. Spot intensity was measured using Image J (http://rsb.info.nih.gov/ij/l). Protein phosphorylation levels are expressed as a ratio to equivalent total proteins. Fold increases in spot intensities were calculated against nonstimulated control samples.

<a id='d78cf4d7-fab1-45f8-ac40-06742286a1e1'></a>

# RESULTS

## MSH transiently activates MAPK1,2

A detailed 106 ODE model of the MAPK1,2 network receiving inputs from FGF and MSH through the FGFR and MC1R was constructed (Model A). Model A includes two previously published subnetworks, the RTK-MAPK1,2 (20) and the Gs-PKA (43) subnetworks connected through cAMP-GEF activation of Ras-B-Raf and PKA inhibition of C-Raf. The table of molecules, initial concentrations, interactions, and constants are shown in Supplemental Table S1. The network includes a putative bifan, two positive feedback loops, three negative feedback loops, and two feed-forward loops based on published literature (18, 21, 45). We had previously shown that activation with platelet-derived growth factor (PDGF) leads to a sustained activation of MAPK1,2 (20). Initially, investigations were performed to determine the duration of MAPK1,2 activity in response to a stimulus received through activation of a GPCR (MC1R). Computational modeling of the MAPK1,2 network with Model A, predicted that a 5-min stimulus of 0.02 µM MSH would lead to only a transient increase in MAPK1,2 phosphorylation with a return to near basal levels 10 min after stimulus (Fig. 1A) if a positive feedback loop exists from MAPK to C-Raf. The MSH stimulus was predicted to result in a maximal activation of 0.16 µM of active MAPK1,2, 5 min after stimulus. We have operationally defined a sustained activation as being at least 6 times longer than the stimuli. In our computational and experimental studies, the length of stimuli was 5 min and simulations were made up to 60 min after stimuli. However, computational modeling of a positive feedback loop to both C-Raf and B-Raf from

<a id='950b57be-cc60-45b2-8f9a-31b014397022'></a>

REGULATORY MOTIF IN SIGNALING NETWORKS

<a id='85020a3a-8e3e-4ab2-9b7b-39ad025d79a0'></a>

1395

<a id='1de262b0-ef07-4b72-8f0b-3e3a2ea73d50'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='c18258c6-2467-4cae-a74d-79e4dc0032dc'></a>

A<::Line graph titled 'Active MAPK 1,2 (μM) over Time (min)'. The y-axis is 'Active MAPK 1,2 (μM)' ranging from 0.00 to 0.20. The x-axis is 'Time (min)' ranging from 0 to 60. A horizontal bar labeled 'Stimulus' is present from 0 to approximately 7 minutes on the x-axis. The line shows a rapid increase from 0 to a peak of about 0.16 μM around 5 minutes, then a rapid decrease, approaching 0 by 20 minutes and remaining low thereafter.: chart::>D<::Figure D consists of two parts. The top part shows three dot blot images representing protein levels at different time points after FGF (20ng/ml) stimulation: '0 min', '5 min', and '65 min'. On the left, 'P-MAPK1,2' and 'MAPK2' are labeled. For P-MAPK1,2, the dots appear darker at 5 min compared to 0 min and 65 min. For MAPK2, the dot intensity appears relatively consistent across all time points. The bottom part is a line graph titled 'Fold increase p-MAPK1,2 over Time (Min)'. The y-axis is 'Fold increase p-MAPK1,2' ranging from 0.5 to 2. The x-axis is 'Time (Min)' ranging from 0 to 70. A horizontal bar labeled 'Stimulus' is present from 0 to approximately 7 minutes on the x-axis. The line graph shows an initial fold increase from 1 at 0 min, peaking around 1.6-1.75 fold increase between 5 and 15 minutes, and then maintaining this elevated level up to 65 minutes with error bars indicating variability.: chart::>

<a id='e3e4b41d-260b-442b-9a32-e8a9b6129ae5'></a>

<::figure: Figure 1. B) Experimental data from RPPA slides show phosphorylation of MAPK1,2 in SB2 melanoma cell lysates following stimulation with MSH (2 μM) for 5 min. RPPA spots were scanned, and band intensities were quantified and graphed as fold increases in band intensity as compared to nonstimulated cells after normalizing for ERK2. The panel includes: 1) RPPA spots showing MSH (2μM) stimulation at 0 min, 5 min, and 65 min for P-MAPK1,2 and MAPK2. At 0 min, P-MAPK1,2 spots are faint, MAPK2 spots are moderate. At 5 min, P-MAPK1,2 spots are dark, MAPK2 spots are moderate. At 65 min, P-MAPK1,2 spots are faint, MAPK2 spots are moderate. 2) A line graph titled 'Fold increase p-MAPK1,2' on the y-axis (ranging from 0.5 to 2.0) versus 'Time (Min)' on the x-axis (ranging from 0 to 70). A black bar labeled 'Stimulus' is shown from 0 to 5 min on the x-axis. The graph shows a sharp increase in p-MAPK1,2 fold increase, peaking at approximately 2.0 at 5 min, then decreasing rapidly and stabilizing around 1.0 from 10 min to 65 min. Error bars are present at each time point. C) FGF stimulation leads to a sustained activation of MAPK. Computational modeling data show a sustained increase in MAPK1,2 after a 5-min pulse of FGF. The bar at the x-axis denotes length of stimulus. The panel includes a line graph titled 'Active MAPK 1,2 (μM)' on the y-axis (ranging from 0.00 to 0.20) versus 'Time (min)' on the x-axis (ranging from 0 to 60). A black bar labeled 'Stimulus' is shown from 0 to 5 min on the x-axis. The graph shows a rapid increase in active MAPK 1,2, reaching a plateau around 0.17 μM from approximately 15 min to 30 min, then slowly decreasing to about 0.13 μM by 60 min.::>A) MSH transiently activates MAPK1,2. Computational modeling data show a transient increase in MAPK1,2 after a 5 min pulse of MSH. The bar at the *x*-axis denotes length of stimulus. D) Experimental data from RPPA slides show phosphorylation of MAPK1,2 in SB2 melanoma cell lysates following stimulation with FGF (20 ng/ml) for 5 min. RPPA spots were scanned, and band intensities were quantified and graphed as fold increases in band intensity as compared to nonstimulated cells after normalizing for MAPK.

<a id='7ac01c11-614a-47ea-8055-0d55ce75c4b2'></a>

MAPK1,2 shows a biphasic activation of MAPK1,2 in response to MSH (Supplemental Fig. S1C). Given these two different potential outputs from Model A, we experimentally determined the MAPK1,2 response to MSH stimulation in SB2 melanoma cells. SB2 melanoma cells were serum-starved for 16 h and stimulated with 2 µM MSH for 5 min. The cells were washed with serum-free medium and incubated for various lengths of time. The resulting phosphorylation of MAPK1,2 was determined by RPPA analysis. Experimental data show that MSH stimulation results in peak activity of phosphorylated MAPK1,2, 5 min after stimulus with a return to basal levels 10 min after stimulus (Fig. 1B). Similar results were observed in MeWo human melanoma cells (data not shown). The same sets of lysates were probed for phospho-MAPK1,2 and total MAPK on a Western blot confirming that MAPK1,2 phosphorylation is only transiently increased in response to MSH (Supplemental Fig. S3A). Therefore, based on the experimental results we eliminated the positive feedback from MAPK1,2 to B-Raf from the model and operated with a single positive feedback loop to C-Raf. The iterative use of computational simulation and experimental data is thus used to test and constrain the model.

<a id='6cca0d39-d250-4009-8f6f-5d968d4ce66e'></a>

FGF leads to a sustained activation of MAPK1,2

We have previously shown that stimulation by PDGF
leads to a sustained activation of MAPK1,2 in mouse
fibroblast cells (20). We wanted to determine whether
other growth factors that activate receptor tyrosine
kinases, such as bFGF, can also elicit a sustained activa-
tion of MAPK1,2 in melanoma cells. Computational
modeling of the network using the revised Model A,

<a id='e5bd5fa2-7c65-4dc9-88f4-69c8e876e918'></a>

with a positive feedback from MAPK1,2 to C-Raf, sug-
gested that a brief 5-min pulse of FGF would lead to a
sustained increase in phosphorylated MAPK1,2 (Fig.
1C) with a maximal increase of activated MAPK1,2 of
0.17 µM. Additional reported pathway connection
within the network include a negative feedback from
MAPK1,2 to PKC (46). We modeled these interactions
individually and simulated the MAPK1,2 response with
these different connections. The results from these
simulations show that including a negative feedback
from MAPK to PKC results in a more rapid reduction in
MAPK1,2 activity as compared to the simulations with
only a positive feedback loop (Supplemental Fig. S2C).
Interestingly, adding a feed-forward loop from PKC to
AC (Supplemental Fig. S2D) changed the predicted
MAPK1,2 activation to a biphasic response (Supple-
mental Fig. S2E). Given these different computational
predictions, we determined the effects of bFGF on SB2
melanoma cells. Cells were serum-starved and stimu-
lated with bFGF (20 ng/ml) for 5 min. The FGF was
washed out, and cells were incubated for different
lengths of time. The RPPA data show that a brief
stimulus of FGF leads to a sustained increase in
MAPK1,2 phosphorylation (Fig. 1D) with a maximal
increase in phosphorylated MAPK1,2, 10 min after
stimulus. Similar results were obtained using Western
blot analysis (Supplemental Fig. S3B). Constraining the
model based on the observed biological data, we elim-
inated the feed-forward loop from PKC to AC (Supple-
mental Fig. S2D), as well as the negative feedback loop
from MAPK1,2 to C-Raf (Supplemental Fig. S2B). The
resulting Model A used for further work contains a
positive feedback loop from MAPK1,2 to C-Raf (Fig.
2A).

<a id='c7b37153-ae85-43f6-86d8-ed084b742240'></a>

1396 Vol. 22 May 2008

<a id='1ea24625-cc94-458c-9d16-373fbeb7e1fe'></a>

The FASEB Journal

<a id='8c12b113-5b5c-4b02-9fb0-6a0db556c884'></a>

MULLER ET AL.

<a id='667c5b55-1fea-4b53-9507-1ea7d40fc204'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='bf3e7833-8b67-4f69-9df4-d02950dd24a3'></a>

<::figure::>A) Detailed network model of the FGFR-MC1R-B-Raf-C-Raf-MAPK1,2 network based on the experimental data from Fig. 1. The diagram shows the following pathway: FGF-R activates Ras. Ras activates cAMP-GEF. cAMP-GEF activates C-Raf. C-Raf activates MEK. MEK activates MAPK1,2. MAPK1,2 activates MKP1. MKP1 inhibits MAPK1,2. MAPK1,2 also inhibits C-Raf. B-Raf activates MEK. Ras activates B-Raf. MC1R activates Gas. Gas activates AC. AC produces cAMP. cAMP activates PKA. PKA inhibits C-Raf. PKA also inhibits B-Raf. B) Connection diagram shows the reduced network structure of the FGFR-MC1R-B-Raf-C-Raf-MAPK1,2 network dynamics of MAPK1,2 activity. The diagram shows the following interactions: FGFR activates C-Raf and B-Raf. MC1R inhibits C-Raf and B-Raf. C-Raf activates B-Raf and MAPK1,2. B-Raf activates C-Raf and MAPK1,2. C-Raf inhibits B-Raf. MAPK1,2 activates C-Raf and B-Raf. C) The reduced motif model was trained using the experimental data from MSH stimulation. The model shows only a transient increase in active MAPK on a 5-min MSH pulse. This is a line chart with 'Time (min)' on the x-axis, ranging from 0 to 100, and 'Active MAPK1,2' on the y-axis, ranging from 0 to 1.4. A stimulus is applied at Time 0. The line shows a rapid increase in Active MAPK1,2 to a peak of approximately 1.35 at around 5 minutes, followed by a gradual decrease back to 0 by approximately 40-50 minutes. D) The same model was also trained using the FGF experimental data. The model shows a sustained activation of MAPK on FGF stimulation. This is a line chart with 'Time (min)' on the x-axis, ranging from 0 to 100, and 'Active MAPK1,2' on the y-axis, ranging from 0 to 3. A stimulus is applied at Time 0. The line shows a rapid increase in Active MAPK1,2 to a plateau of approximately 2.4-2.5 by around 10 minutes, which is then sustained for the remainder of the 100-minute period.<::figure::>

<a id='8ae9b825-469d-489c-945e-0dc171fa6934'></a>

The MC1R, FGFR, B-Raf, C-Raf bifan network

Based on the data from Fig. 1, the detailed network we developed is shown in Fig. 2A. This final network Model A (Fig. 2A) was used for the remainder of the work in this paper. The various interactions within the MAPK1,2 network predicts that signaling from MC1R and FGFR to B-Raf and C-Raf forms a partially incoherent bifan motif. This bifan motif is described as partially incoherent since B-Raf has coherent inputs (both positive from MC1R and FGFR), while C-Raf is incoherent (positive from FGFR and negative from MC1R). The bifan drives a positive feedback loop from MAPK,1,2 to C-Raf, this network structure is shown in Fig. 2B.

<a id='0a85f0b1-6fce-42e2-b439-cdd1db701f2d'></a>

Reduction of network and computing the signal processing based on network structure

<a id='99b23dde-912e-4c03-a7b5-79bbd3ec15d5'></a>

Based on connectivity to B-Raf and C-Raf we wanted to determine whether a reduced network could be developed into a predictive computational model. This reduction is a very important issue in the development of large quantitative predictive models of signaling networks. Our detailed ODE model already contains 106 equations, and adding on any other signaling pathways would very rapidly increase the model to several hundred ODEs. Computing hundreds of ODE's increases the likelihood of errors and, with the difference in time scales, can lead to stiff systems. We thus determine whether reducing the model to include only nodes that integrate signals would decrease the number of equations required to solve, while still maintaining the ability to predict experimental outcomes. Preserving the signatures of the network, feedbacks, and bifans, the network was reduced to the minimum informative network structure. A reduced network model was developed, Model B (Supplemental Fig. S5), and tuned using the experimental data from Fig. 1B, D. The simulation from the reduced model predicts a transient activation of MAPK1, 2 on MSH stimulus (Fig.

<a id='5fefd343-4264-44e2-842d-33c0ad004b23'></a>

2C). Model B was constrained using the experimental data with resulting simulations predicting that activation of FGFR results in sustained activation of MAPK1,2 (Fig. 2D). Having developed this reduced model and tuning it using the experimental data, we used Model B to predict the behavior of the system and compared it to predictions from the large, detailed Model A in the ensuing sets of studies.

<a id='3d4ff7e0-c642-47ff-9600-658408f5edcf'></a>

C-Raf is essential for a sustained but not transient
activation of MAPK1,2

Regulation of the temporal characteristics of the
MAPK1,2 network by the two RAF isoforms is not
known. Reports suggest that C-Raf is needed for activa-
tion of MAPK1,2 by B-Raf stimulatory pathways (47,
48). We wanted to investigate how changing the relative
protein levels of C-Raf and B-Raf would alter the
MAPK1,2 response. Parameter variation of the concen-
trations of B-Raf and C-Raf was performed with the
resultant computational data suggesting that the
MAPK1,2 response is acutely sensitive to the relative
concentrations of the two Raf isoforms (Fig. 3A). Sen-
sitivity analysis suggests that the relative amount of
C-Raf would be critical for eliciting a sustained
MAPK1,2 response. If the initial C-Raf protein concen-
tration is equal to or higher than the B-Raf protein
concentration, the MAPK1,2 network is predicted to
respond to stimulus resulting in a sustained activation
of MAPK1,2 (Fig. 3A). We experimentally determined
the relative expression of C-Raf and B-Raf in SB2
melanoma cells. Immunoprecipitation of C- and B-Raf
followed by Coomassie blue staining of the immuno-
precipitate showed that the expression levels of C-Raf
and B-Raf are almost equal (Fig. 3B). Closer examina-
tion of the MAPK1,2 response suggests that a steep
C-Raf concentration dependency would be required to
elicit a sustained MAPK1,2 response (Fig. 3C). Based on
Model B, we simulated the FGF activation of MAPK

<a id='f0c69475-3ea2-4c96-b015-9488776d77a7'></a>

REGULATORY MOTIF IN SIGNALING NETWORKS

<a id='d62f32fd-4259-4e63-a8a7-c3e7b278a22d'></a>

1397

<a id='2261ec82-14e8-47b3-84f2-59dc0258b442'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='508b3471-69ea-4e1f-9933-826895e8de25'></a>

<::Figure 3. A) Line graph showing Active MAPK1,2 (μM) on the y-axis from 0.0 to 0.2, and C-Raf/(C-Raf+B-Raf) on the x-axis from 0.00 to 1.25. The curve starts low, increases, and then plateaus at approximately 0.18 μM. B) Immunoprecipitation gels and a bar graph. The top part shows SDS-PAGE gels for B-Raf and C-Raf, with lanes labeled 'Pre-IP' and 'Post-IP'. The middle part shows an SDS-PAGE gel labeled 'Raf IP' with lanes for CRaf and BRaf, and a band labeled 'Heavy chain'. The bar graph shows 'Percentage Total Raf' on the y-axis (0-80) for 'CRaf' (approx. 60%) and 'BRaf' (approx. 40%) on the x-axis. C) Line graph showing Active MAPK1,2 (μM) on a logarithmic y-axis from 0.0001 to 1, and Time (min) on the x-axis from 0 to 60. Multiple colored lines indicate different sustained levels of MAPK1,2 activity, with a gradient representing varying C-Raf levels. D) Line graph showing Active MAPK1,2 on the y-axis from 0 to 3, and Stimulus Time (min) on the x-axis from 0 to 100. A solid line shows a sustained response (peaks at ~2.5, then plateaus), and a dotted line shows a transient response (peaks at ~1.5, then drops to 0). E) Western blot images and a line graph. The top part shows western blot bands for P-MAPK1,2, MAPK1,2, C-Raf, and Actin, for 'Non-specific siRNA' and 'C-Raf siRNA' conditions, at FGF (20 ng/ml) time points 0, 5, and 45 minutes. The bottom line graph shows 'Fold increase p-MAPK1,2' on the y-axis from 0 to 2, and 'Stimulus Time (Min)' on the x-axis from 0 to 50. A dashed line with circles represents 'Non-specific siRNA', showing higher and sustained p-MAPK1,2. A solid line with squares represents 'C-Raf siRNA', showing lower p-MAPK1,2. A) C-Raf is essential for sustained MAPK1,2 activation. Computational modeling of FGF activation of MAPK1,2 activity 30 min after stimulus with different ratios of C-Raf to B-Raf. B) Experimental data show immunoprecipitated B-Raf and C-Raf from SB2 melanoma cells resolved on SDS-PAGE and stained with Coomassie blue. Band intensities were quantified and shown on the bar graph as relative expression of B-Raf and C-Raf after normalizing against the IgG heavy chain and for the change in B-Raf and C-Raf after immunoprecipitation, as compared to the levels in the pre-IP lysate. C) Sensitivity analysis of the sustained vs. transient response of MAPK1,2 activity to FGF as a function of varying the total amount of C-Raf suggests that the sustained MAPK1,2 response is dependent on C-Raf levels. D) The reduced motif model shows inhibition of the activation of C-Raf by MAPK (dotted line) when the biological system is stimulated by FGF for 5 min. E) Experimental data from SB2 cells transfected with either C-Raf specific siRNA or nonspecific siRNA. Seventy-two hours after transfection, cells were serum-starved and stimulated with FGF for 5 min, washed out, and incubated for the times shown. Cell lysates were probed for phospho-MAPK1,2, C-Raf, and β-Actin as shown. Graph shows changes in phopsho-MAPK1,2 after normalization for β-Actin.: figure::>

<a id='3368263a-d67b-4b72-bfa7-cdc3b4ab4150'></a>

under conditions where the feedback to C-Raf was inhibited. The modeling simulation predicted only a transient activation of MAPK when feedback to C-Raf is blocked (Fig. 3D). These computational modeling results predict that if C-Raf levels are decreased, FGF will no longer elicit a sustained MAPK1,2 response (Fig. 3D; dotted line). To experimentally test this hypothesis, cells were transfected with C-Raf specific siRNA and the levels of C-Raf were measured 72 h after transfection. The data show that C-Raf was knocked down by 60% using C-Raf siRNA with little effect on B-RAF (Supplemental Fig. S3D). We then determined the MAPK1,2 response to stimulation by FGF under conditions of low C-Raf. Cells transfected with either C-Raf or nonspecific siRNA were serum-starved and stimulated with FGF for 5 min and the phosphorylation of MAPK1,2 measured over time. The data show that if C-Raf is knocked down, FGF can no longer elicit a sustained MAPK1,2 response, while a transient response is still present (Fig. 3E). These data suggest that the expression level of C-Raf is critical for a sustained MAPK1,2 response.

<a id='8e588578-3b58-4db5-b101-76b4d30ccd1b'></a>

The bifan motif can regulate the duration of MAPK1,2 activation

Having observed the differential regulation of the dynamics of MAPK1,2 activity by C-Raf, we wanted to determine whether the duration of MAPK1,2 activation can be modulated in a completely endogenous system. Activation of the Gs-PKA pathway phosphorylates C-Raf and inhibits C-Raf activity (28). Therefore, we wanted to determine whether activation of the Gs-PKA pathway would gate the FGF-induced sustained activation of MAPK1,2 by inhibiting C-Raf. Computational modeling data from Model A (Fig. 2A) predicted that a prepulse of MSH would inhibit FGF-induced sustained phosphorylation of MAPK1,2 (Fig. 4A). While a pulse of FGF alone activated MAPK1,2 for longer than 70 min (Fig. 1C), a prepulse of MSH followed by a pulse of FGF phosphorylated MAPK1,2 for less than 30 min (Fig. 4A). Model B also predicted a transient activation of MAPK on a prepulse of MSH followed by FGF (Fig. 4B). SB2

<a id='ace4b506-3e1b-4f67-af9c-1f298bbd9e59'></a>

1398 Vol. 22 May 2008

<a id='153c059b-e0e5-480e-8107-e4668721fd06'></a>

The FASEB Journal

<a id='2146204d-0a94-4e2d-9a99-6b884850c6d0'></a>

MULLER ET AL.

<a id='c3a00e6d-58e2-420b-b533-780ed6f99849'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='890445b3-d158-4e25-9ca3-6d288e6f1c16'></a>

A <::line graph: The x-axis is labeled "Time (min)" and ranges from 0 to 60. A black bar labeled "Stimulus" is present on the x-axis from 0 to approximately 2.5 min. The y-axis is labeled "Active MAPK1,2 (?M)" and ranges from 0.00 to 0.25. A line shows that Active MAPK1,2 increases sharply from 0 to a peak of approximately 0.20 at around 2.5 min, then gradually decreases to near baseline by 60 min::> D MSH then FGF 0 5 10 25 (Min) <::western blot: The western blot shows protein levels over time (0, 5, 10, 25 minutes) for P-MAPK1,2, MAPK1,2, and Actin. The top set of blots is for the condition "+H89", and the bottom set is for the condition "-H89". In each set, the top row shows P-MAPK1,2, the middle row shows MAPK1,2, and the bottom row shows Actin::> <::line graph: The x-axis is labeled "Time (Min)" and ranges from 0 to 40. A black bar labeled "Stimulus" is present on the x-axis from 0 to approximately 2.5 min. The y-axis is labeled "Fold increase p-MAPK1,2" and ranges from 0 to 3. Two lines are plotted: a solid line with square markers labeled "-H89" and a dashed line with star markers labeled "+H89". Both lines show an initial increase, peaking between 5 and 10 minutes, with the +H89 line generally showing a higher or sustained fold increase compared to the -H89 line over time::>

<a id='87287803-1fb5-4e63-afdf-6480fcda5312'></a>

<::chart:Figure 4. A) MSH gates the FGF activation of MAPK1,2. Computational modeling data show a transient increase in MAPK1,2 after a 5-min pulse of MSH followed by a 5-min pulse of FGF. B) The reduced motif model shows only a transient increase in MAPK1,2 activity following a stimulus of MSH at 0–5 min and then a stimulus of FGF at 5–10 min. The graph labeled B is a line graph with 'Time (min)' on the x-axis (0 to 100) and 'Active MAPK1,2' on the y-axis (0 to 1.5). A horizontal bar labeled 'Stimulus' is present from 0 to 10 min on the x-axis. The line shows a sharp increase from 0, peaking at approximately 1.5 around 7-8 min, then gradually decreasing to near 0 by 40 min and remaining low. C) Experimental data from RPPA slides show phosphorylation of MAPK1,2 in SB2 melanoma cell lysates following stimulation with MSH (2 µM) for 5 min, followed by FGF (20 ng/ml) for 5 min. RPPA spots were scanned, band intensities quantified and shown on graph as fold increase in band intensities as compared to nonstimulated cells after normalizing for ERK2. The graph labeled C contains dot blots at the top and a line graph below. The dot blots show 'P-MAPK1,2' and 'MAPK2' at '0 min', '5 min', and '65 min'. At 0 min, P-MAPK1,2 dots are faint, while MAPK2 dots are distinct. At 5 min, P-MAPK1,2 dots are much darker and more prominent, while MAPK2 dots are distinct. At 65 min, P-MAPK1,2 dots are faint again, and MAPK2 dots are distinct. The line graph below has 'Time (Min)' on the x-axis (0 to 70) and 'Fold increase p-MAPK1,2' on the y-axis (0.5 to 1.75). A horizontal bar labeled 'Stimulus' is present from 0 to 10 min on the x-axis. The data points show an increase from approximately 0.75 at 0 min to a peak of about 1.5 at 5 min, then a decrease to approximately 0.8 at 10 min, followed by a slight increase and stabilization around 1.0 from 20 min to 65 min.::>D) SB2 cells were serum starved and treated with either 20 mM H89 or vehicle for 2 h to block PKA activity. Cells were then stimulated with MSH for 5 min followed by FGF for 5 min. The ligands were washed out, and the cells were incubated in 1% medium for times indicated. Lysates were probed for phospho-MAPK1,2 and β-Actin. Graph shows fold change in phospho-MAPK1,2 after normalization for β-Actin.

<a id='ab3cb4d9-634b-4059-805d-9e7d737bf42c'></a>

melanoma cells were serum-starved and stimulated
with 2 μΜ MSH for 5 min, followed by 20 ng/ml FGF
for 5 min. Ligands were then washed out, and cells
were incubated in serum-free media for different
lengths of time. The data show that a prepulse of
MSH does indeed inhibit the FGF-induced sustained
activation of MAPK1,2 (Fig. 4C). Similar data were
obtained from Western blot analysis (Supplemental
Fig. S3C).

<a id='9bffdd40-7c89-4ee4-a1b3-db02fa5aa34a'></a>

PKA is a key regulator determining the state of the
MAPK1,2 network

The data thus far show that the levels and activation of
specific Raf isoforms determine the temporal duration
of activation of the MAPK1,2 network, whereby either
knocking down C-Raf or inhibiting its function by
activating PKA inhibits a sustained MAPK1,2 response.
We further investigated the role of PKA in the MSH
gating of the FGF-mediated MAPK1,2 network. The
MSH regulation of MAPK1,2 is dependent on cAMP
and PKA, where cAMP has been reported to activate
B-Raf (24, 49) but PKA inhibits C-Raf (50). This diver-
gence of the signal occurs on two different hierarchical
steps, where cAMP is at a level higher than PKA.
Therefore, it should be possible to inhibit PKA activity
using a pharmacological inhibitor (H89), while at the
same time allowing cAMP activation of B-Raf. Under
this condition, we determined whether inhibiting PKA,
and therefore not inhibiting C-Raf, would alter the

<a id='3f7ab751-54c2-41eb-874d-85092d0cf23b'></a>

MSH gating of MAPK1,2. SB2 melanoma cells were serum-starved, and PKA activity was blocked with the incubation of H89. Cells were stimulated with MSH for 5 min followed by FGF for 5 min, and the activity of MAPK1,2 was measured. The data show that if PKA is inhibited, MSH cannot gate the FGF activation of MAPK1,2 (Fig. 4D).

<a id='d2ccefab-73cb-4860-9f27-3a5131d779f2'></a>

Inhibiting the negative input into the bifan switches
MAPK1,2 activation from transient to sustained

<a id='7e35a48f-0047-413a-bef9-abc133457516'></a>

Computational modeling using Model A (Fig. 2A), of the MSH activation of MAPK1,2 under conditions where PKA is inhibited predicted that MSH stimulation would lead to a sustained activation of MAPK1,2 when PKA activity is blocked (Fig. 5A). SB2 melanoma cells were serum-starved and incubated with 20 μM H89 for 2 h to inhibit PKA activity. The cells were then stimulated with MSH for 5 min, and MAPK1,2 activity was measured over time. The data show that inhibiting PKA with H89 changes the MSH activation of MAPK1,2 from a transient response (Fig. 1B) to a sustained activation of MAPK1,2 in melanoma cells (Fig. 5B).

<a id='0962fd2a-aeb2-4a07-8722-dbfafdee0c0c'></a>

DISCUSSION
Signaling networks are complex with numerous subnet-
work motifs that can dramatically alter the activation of
important regulatory molecules. We constructed a

<a id='dabe496a-a89d-480a-9e28-71dc60f3f3d3'></a>

REGULATORY MOTIF IN SIGNALING NETWORKS

<a id='6514e3b7-1a9d-4323-9819-8af57a0a5275'></a>

1399

<a id='f7da0cbf-f428-4e2e-bbee-f62cba5eb028'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='ac24cfd2-f112-4d15-bde3-9484261f6b84'></a>

<::Figure 5: A) Line graph titled 'A' with y-axis 'Active MAPK1,2 (µM)' ranging from 0.00 to 0.25 and x-axis 'Time (min)' ranging from 0 to 30. Two lines are plotted: a solid line labeled 'Non-PKA inhibited' showing a peak around 3-4 min and then decreasing, and a dashed line labeled 'PKA inhibited' showing a peak around 3-4 min and then decreasing to a higher steady state. B) Western blot images and a line graph. The western blots show MSH (20 µM) stimulation at time points 0, 5, 10, 25 (Min). There are two conditions: '+H89' and '-H89'. For each condition, bands for P-MAPK1,2, MAPK1,2, and Actin are shown across the time points. Below the western blots is a line graph titled 'B' with y-axis 'Fold increase p-MAPK1,2' ranging from 0 to 3 and x-axis 'Stimulus Time (Min)' ranging from 0 to 25. Two lines with square markers are plotted: a dashed line labeled '+ H89' and a solid line labeled '- H89', both showing a peak around 5 min and then decreasing. A) Computational modeling of the MSH activation of MAPK1,2 under control conditions (solid line) or with PKA activity inhibited (dashed line). B) SB2 cells were serum-starved and treated with either 20 mM H89 or vehicle for 2 h to block PKA activity. Cells were then stimulated with MSH for 5 min and washed out, and cells were incubated in serum-free medium for times indicated. Lysates were probed for phospho-MAPK1,2 and β-Actin. The graph shows fold change in phospho-MAPK1,2 after normalization for β-Actin.: figure::>

<a id='4041d753-46e9-4246-a087-48e6376c23a4'></a>

MAPK1,2 network in silico based on our previous studies and on the literature and experimentally tested it to understand the design principles of this signaling module. The model was constrained based on experimental data to result in Model A (Fig. 2A). From these studies we show that the temporal duration of MAPK1,2 is distinct, depending on the activation signal. MC1R stimulation by MSH leads to only a transient activation of MAPK1,2. However, activation of FGFR leads to a sustained activation of MAPK1,2. These two incoming signals can interact such that the MC1R signal gates the FGFR signal to change it from a sustained to a transient activation of MAPK1,2 when the signals are processed through the partially incoherent bifan motif. The FGFR signal is coherent within the bifan to activate both

<a id='a1edc3af-4849-4c14-aa2e-01f1ee0868d4'></a>

C-Raf and B-Raf. C-Raf then couples to a positive feedback loop from C-Raf to MAPK1,2 back to C-Raf, resulting in a sustained activation of MAPK1,2. However, the MC1R signal is incoherent within the bifan where it activates B-Raf but inhibits C-Raf. This condition results in an inhibition of the C-Raf coupled feedback loop to and from MAPK1,2. The difference we observe in the sustained *vs*. transient activation of MAPK1,2 is explained by this difference in the connection within the bifan. While it is known that both B-Raf and C-Raf can activate MAPK1,2 (12, 13), here we show that the two isoforms have distinct roles in regulating the systems response of MAPK1,2. The system's response of MAPK1,2 activation is dependent on the nature of connectivity of the two receptors to B-Raf and C-Raf, which form a partially incoherent bifan. The incoherent bifan is the locus of signal integration from RTK and GPCR to MAPK1,2 with C-Raf acting as a logic gate. Computational modeling of the network of functional connections predicted the behavior of the system.

<a id='82a69375-1f5d-4bd9-aea1-fd5828f10781'></a>

The bifan network controls the state of a positive feedback loop downstream from C-Raf to regulate the dynamics of MAPK1,2 activation. We have previously described the bistable properties of the MAPK1,2 network, which is dependent on a positive feedback loop from MAPK1,2 to C-Raf (20). Here we show that altering the connectivity to the bifan motif changes the state of MAPK1,2 from a transient to a sustained response. Removing the inhibitory or incoherent connectivity by inhibiting PKA switches the MC1R mediated transient activation of MAPK1,2 to a sustained response. Activation of PKA by GPCR's serves to limit the duration of MAPK1,2 activity, and ligands that activate Gs receptors can balance growth factor activation of MAPK1,2 (18). The FGFR signal leads to a sustained activation of MAPK1,2. However if C-Raf levels are knocked down or if C-Raf activity is inhibited, FGFR only elicits a transient activation of MAPK1,2. While FGFR can still transiently activate MAPK1,2 when C-Raf is knocked down, the sustained activation of MAPK1,2 is dependent on C-Raf. Our studies presented here show that sustained vs. transient activation of MAPK1,2 can be regulated by a feedback loop to C-Raf, which drives the systems response. PC12 rat pheochromocytoma cells also exhibit a temporal difference in MAPK phosphorylation in response to either EGF or NGF. Work by Santos et al. (51) using PC12 cells shows that a positive feedback loop from MAPK to C-Raf mediates sustained MAPK activity in response to NGF, while a negative feedback loop from MAPK to C-Raf leads to a transient activation of MAPK in response to EGF. Work by Sasagawa et al. (52), however, suggests that the differential regulation of either Ras or Rap1 by modulation of GTPase activating proteins (Ras-GAP or Rap-GAP) can lead to sustained vs. transient activation of MAPK in response to either EGF or NGF in PC12 cells. Here we show that a positive feedback to C-Raf and differential regulation of C-Raf vs. B-Raf in response to FGF or MSH can lead to transient vs. sus-

<a id='c74a0c23-d422-4ab6-b6cf-0b85925ebb67'></a>

1400 Vol. 22 May 2008

<a id='75276e77-257d-4cce-a06c-2a6a3e2a0390'></a>

The FASEB Journal

<a id='b5085204-a41b-43fc-b755-dc42e6ca85ed'></a>

MULLER ET AL.

<a id='9d5f81ef-3b61-4339-b522-fe5f3a0fc209'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='26ce6cb9-657d-4574-8054-f1e4ced9caec'></a>

tained activation of MAPK in human melanoma cells. The two isoforms of Raf can activate MAPK1,2 with distinct temporal patterns of activity, suggesting that inhibiting C-Raf rather than B-Raf may have a greater effect on inhibiting MAPK1,2 activity. A previous modeling study of a linear pathway from B-Raf and C-Raf to MAPK1,2, which lacked the physiologically relevant feedback loops, suggested that a high concentration of B-Raf can lead to a sustained activation of MAPK1,2 (53) based on the parameters used in the model. We find that the concentration and activity of C-Raf is more important in maintaining the sustained response due to the feedback connectivity to C-Raf. Note that the immunoblot showed a darker band for B-Raf than C-Raf, but in fact when we immunodepleted the two Raf isoforms from aliquots of the same lysate and determined Raf levels by Coomassie blue staining, we observed that SB2 cells express more C-Raf than B-Raf. The role of C-Raf in maintaining the sustained MAPK activity may also explain why no C-Raf mutations have been found in melanoma. While B-Raf mutations are found in 70% of melanoma, B-Raf mutant expression by itself is not sufficient to drive transformation of cells but requires the addition of FGF (54). While both B-Raf and C-Raf can activate MAPK1,2 (12, 13), our studies here show for the first time that the two isoforms have distinct systems properties in differentially regulating the temporal duration of MAPK1,2 activation based on feedback loops and signaling motifs within the MAPK1,2 subnetwork. Activating mutations of B-Raf are highly prevalent in melanoma while activating mutations in C-Raf have not been reported. A possible reason for this is that while the B-Raf mutation increase MAPK1,2 by constant activation, the increase in MAPK1,2 phosphorylation is only ~2 fold (9), possibly keeping the cells in an increased proliferative state and thus increasing the chances of additional mutations. Note that B-Raf mutations are found in all stages, including preneoplastic nevi and melanocytic lesions, suggesting that B-Raf mutations may be an early event in the development of melanoma. Activating mutations of C-Raf have not been reported; one possible mechanistic reason could be that activating mutations of C-Raf may result in cell death by driving MAPK1,2 and the positive feedback loop.

<a id='144798a1-3ecc-4f96-8aee-ea2a09d2d0df'></a>

Developing large quantitative models of signaling net-
works is very important as we try to predict how signals are
processed in response to activators and change in re-
sponse to targeted manipulations. Building detailed ODE
models of large networks is impractical due to the scale of
the model. Alternative methods such as Boolean models
have been suggested, but due to feedback loops the
Boolean models are frequently unstable and lead to
oscillatory behavior. Here we demonstrate that reduction
of the network based on the biology of the connectivity is
a very useful method to reduce the network while main-
taining all subtle complexities resulting in a model able to
robustly predict the effects of network perturbations.
Development of such systems biology methods is highly
dependent on very close co-operation between mathema-

<a id='cb9c8a4f-1807-44fe-b614-1386abffb196'></a>

ticians and biologists and experimental validation and
constraining of the model is vital. Indeed, as indicated
herein a number of different models were predicted from
the literature. We tested these directly resulting in the
evolution of Model A (Supplemental Fig. S1A) to the
refined version of Model A depicted in Fig. 2A, which is
considerably different in topology and in predictions.

<a id='f9e9780c-6b61-41df-8dad-58ca712d598f'></a>

Determining the systems function of signaling networks using an integrated approach of computational modeling, experimental biology, and targeted manipulations is very useful in identifying components and motifs that can regulate network function. These regulatory molecules could then serve as targets for therapeutic purposes. While a molecule might be an attractive target in the context of a linear pathway when one considers the feedback loops and interactions at a systems level, the same molecule may no longer provide to be a good target. Indeed, experimental and patient data for example suggest that a feedback loop in the phosphatidylinositol-3-kinase pathway limits the efficacy of targeting mTOR (55). Thus, understanding the systems properties and design principles of signaling networks and developing models of the relevant interactions validated with experimental testing could aid in development and validation of targeted therapeutics.

<a id='1c7fd421-2871-45e7-86f6-4e19168eb3a3'></a>

Medium-to-high throughput biological methods such as RPPA have allowed us to measure changes in several signaling molecules in parallel from the same set of cell lysates. Using these data, we can begin to construct larger networks and determine how signals from the cell surface are processed through the signaling network. Computational analysis has allowed us to reverse-engineer the system and direct some of the experimental work. Such analysis is important in allowing us to fully understand complex biological networks permitting reverse engineering to achieve desirable outputs from biological systems. FJ

<a id='e1a60b8e-27cb-44ee-9f1d-5e0ecf0931bf'></a>

The work was supported in part by startup funds from the M.D. Anderson Cancer Center, Melanoma SPORE P50 CA093459 (PP-CDP3), and U.S. Department of Defense grant BC044268 to P.T.R.

<a id='6fef4732-5cea-4737-ac24-dcf410059770'></a>

## REFERENCES

1.  Druker, B. J., Talpaz, M., Resta, D. J., Peng, B., Buchdunger, E., Ford, J. M., Lydon, N. B., Kantarjian, H., Capdeville, R., Ohno-Jones, S., and Sawyers, C. L. (2001) Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. N. Engl. J. Med. **344**, 1031–1037
2.  O'Brien, S. G., Guilhot, F., Larson, R. A., Gathmann, I., Baccarani, M., Cervantes, F., Cornelissen, J. J., Fischer, T., Hochhaus, A., Hughes, T., Lechner, K., Nielsen, J. L., Rousselot, P., Reiffers, J., Saglio, G., Shepherd, J., Simonsson, B., Gratwohl, A., Goldman, J. M., Kantarjian, H., Taylor, K., Verhoef, G., Bolton, A. E., Capdeville, R., Druker, B. J., and the IRIS Investigators (2003) Imatinib compared with interferon and low-dose cytarabine for newly diagnosed chronic-phase chronic myeloid leukemia. N. Engl. J. Med. **348**, 994–1004
3.  Demetri, G. D., von Mehren, M., Blanke, C. D., Van den Abbeele, A. D., Eisenberg, B., Roberts, P. J., Heinrich, M. C., Tuveson, D. A., Singer, S., Janicek, M., Fletcher, J. A., Silverman, S. G., Silberman, S. L., Capdeville, R., Kiese, B., Peng, B., Dimitrijevic, S., Druker, B. J., Corless, C., Fletcher, C. D., and

<a id='1caac712-cdcd-4855-813c-89feed7acbf4'></a>

REGULATORY MOTIF IN SIGNALING NETWORKS

<a id='bac320cb-f9e4-46b4-8658-86c599ea354e'></a>

1401

<a id='97cc8506-6729-4566-99a5-d6b6a3e23823'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='028ec976-16bf-4a63-a325-d3ba0467d941'></a>

Joensuu, H. (2002) Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. N. Engl. J. Med. 347, 472–480

4. Slamon, D. J., Leyland-Jones, B., Shak, S., Fuchs, H., Paton, V., Bajamonde, A., Fleming, T., Eiermann, W., Wolter, J., Pegram, M., Baselga, J., and Norton, L. (2001) Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N. Engl. J. Med. 344, 783–792

5. Romond, E. H., Perez, E. A., Bryant, J., Suman, V. J., Geyer, C. E., Jr., Davidson, N. E., Tan-Chiu, E., Martino, S., Paik, S., Kaufman, P. A., Swain, S. M., Pisansky, T. M., Fehrenbacher, L., Kutteh, L. A., Vogel, V. G., Visscher, D. W., Yothers, G., Jenkins, R. B., Brown, A. M., Dakhil, S. R., Mamounas, E. P., Lingle, W. L., Klein, P. M., Ingle, J. N., and Wolmark, N. (2005) Trastuzumab plus adjuvant chemotherapy for operable HER2-positive breast cancer N. Engl. J. Med. 353, 1673–1684

6. Piccart-Gebhart, M. J., Procter, M., Leyland-Jones, B., Goldhirsch, A., Untch, M., Smith, I., Gianni, L., Baselga, J., Bell, R., Jackisch, C., Cameron, D., Dowsett, M., Barrios, C. H., Steger, G., Huang, C.-S., Andersson, M., Inbar, M., Lichinitser, M., Lang, I., Nitz, U., Iwata, H., Thomssen, C., Lohrisch, C., Suter, T. M., Ruschoff, J., Suto, T., Greatorex, V., Ward, C., Straehle, C., McFadden, E., Dolci, M. S., Gelber, R. D., and the Herceptin Adjuvant (HERA) Trial Study Team (2005) Trastuzumab after adjuvant chemotherapy in HER2-positive breast cancer. N. Engl. J. Med. 353, 1659–1672

7. Motzer, R. J., Michaelson, M. D., Redman, B. G., Hudes, G. R., Wilding, G., Figlin, R. A., Ginsberg, M. S., Kim, S. T., Baum, C. M., DePrimo, S. E., Li, J. Z., Bello, C. L., Theuer, C. P., George, D. J., and Rini, B. I. (2006) Activity of SU11248, a multitargeted inhibitor of vascular endothelial growth factor receptor and platelet-derived growth factor receptor, in patients with metastatic renal cell carcinoma. J. Clin. Oncol. 24, 16–24

8. Ratain, M. J., Eisen, T., Stadler, W. M., Flaherty, K. T., Kaye, S. B., Rosner, G. L., Gore, M., Desai, A. A., Patnaik, A., Xiong, H. Q., Rowinsky, E., Abbruzzese, J. L., Xia, C., Simantov, R., Schwartz, B., and O’Dwyer, P. J. (2006) Phase II placebo-controlled randomized discontinuation trial of sorafenib in patients with metastatic renal cell carcinoma. J. Clin. Oncol. 24, 2505–2512

9. Dumaz, N., Hayward, R., Martin, J., Ogilvie, L., Hedley, D., Curtin, J. A., Bastian, B. C., Springer, C., and Marais, R. (2006) In melanoma, RAS mutations are accompanied by switching signaling from BRaf to CRaf and disrupted cyclic AMP signaling. Cancer Res. 66, 9483–9491

10. Davies, H., Bignell, G. R., Cox, C., Stephens, P., Edkins, S., Clegg, S., Teague, J., Woffendin, H., Garnett, M. J., Bottomley, W., Davis, N., Dicks, E., Ewing, R., Floyd, Y., Gray, K., Hall, S., Hawes, R., Hughes, J., Kosmidou, V., Menzies, A., Mould, C., Parker, A., Stevens, C., Watt, S., Hooper, S., Wilson, R., Jayati-lake, H., Gusterson, B. A., Cooper, C., Shipley, J., Hargrave, D., Pritchard-Jones, K., Maitland, N., Chenevix-Trench, G., Riggins, G. J., Bigner, D. D., Palmieri, G., Cossu, A., Flanagan, A., Nicholson, A., Ho, J. W., Leung, S. Y., Yuen, S. T., Weber, B. L., Seigler, H. F., Darrow, T. L., Paterson, H., Marais, R., Marshall, C. J., Wooster, R., Stratton, M. R., and Futreal, P. A. (2002) Mutations of the BRaf gene in human cancer. Nature 417, 949–954

11. Goydos, J. S., Mann, B., Kim, H. J., Gabriel, E. M., Alsina, J., Germino, F. J., Shih, W., and Gorski, D. H. (2005) Detection of B-RAF and N-RAS mutations in human melanoma. J. Am. Coll. Surg. 200, 362–370

12. Goel, V. K., Lazar, A. J., Warneke, C. L., Redston, M. S., and Haluska, F. G. (2006) Examination of mutations in BRAF, NRAS, and PTEN in primary cutaneous melanoma. J. Invest. Dermatol. 126, 154–160

13. Tsao, H., Goel, V., Wu, H., Yang, G., and Haluska, F. G. (2004) Genetic interaction between NRAS and BRAF mutations and PTEN/MMAC1 inactivation in melanoma. J. Invest. Dermatol. 122, 337–341

14. Tsao, H., Zhang, X., Fowlkes, K., and Haluska, F. G. (2000) Relative reciprocity of NRAS and PTEN/MMAC1 alterations in cutaneous melanoma cell lines. Cancer Res. 60, 1800–1804

15. Strumberg, D. (2005) Preclinical and clinical development of the oral multikinase inhibitor sorafenib in cancer treatment. Drugs Today (Barc.) 41, 773–784

<a id='8750477d-8f9c-475c-8317-a711d564f21a'></a>

16. Ahmad, T., Marais, R., Pyle, L., James, B., Schwartz, B., Gore, M., and Eisen, T. (2004) BAY 43-9006 in patients with advanced melanoma: the Royal Marsden experience. J. Clin. Oncol. 22(14S), 7506
17. Lorusso, P. M., Adjei, A. A., Varterasian, M., Gadgeel, S., Reid, J., Mitchell, D. Y., Hanson, L., DeLuca, P., Bruzek, L., Piens, J., Asbury, P., Van Becelaere, K., Herrera, R., Sebolt-Leopold, J., and Meyer, M. B. (2005) Phase I and pharmacodynamic study of the oral MEK inhibitor CI-1040 in patients with advanced malignancies. J. Clin. Oncol. 23, 5281-5293
18. Ma'ayan, A., Jenkins, S. L., Neves, S., Hasseldine, A., Grace, E., Dubin-Thaler, B., Eungdamrong, N. J., Weng, G., Ram, P. T., Rice, J. J., Kershenbaum, A., Stolovitzky, G. A., Blitzer, R. D., and Iyengar, R. (2005) Formation of regulatory patterns during signal propagation in a Mammalian cellular network. Science 309, 1078-1083
19. Bhalla, U. S., and Iyengar, R. (1999) Emergent properties of networks of biological signaling pathways. Science 283, 381-387
20. Bhalla, U. S., Ram, P. T., and Iyengar, R. (2002) MAP kinase phosphatase as a locus of flexibility in a mitogen-activated protein kinase signaling network. Science 297, 1018-1023
21. Kashtan, N., and Alon, U. (2005) Spontaneous evolution of modularity and network motifs. Proc. Natl. Acad. Sci. U. S. A. 102, 13773-13778
22. Garrington, T. P., and Johnson, G. L. (1999) Organization and regulation of mitogen-activated protein kinase signaling pathways. Curr. Opin. Cell Biol. 11, 211-218
23. Vossler, M. R., Yao, H., York, R. D., Pan, M. G., Rim, C. S., and Stork, P. J. (1997) cAMP activates MAP kinase and Elk-1 through a B-Raf- and Rap1-dependent pathway. Cell 89, 73-82
24. Busca, R., Abbe, P., Mantoux, F., Aberdam, E., Peyssonnaux, C., Eychene, A., Ortonne, J. P., and Ballotti, R. (2000) Ras mediates the cAMP-dependent activation of extracellular signal-regulated kinases (ERKs) in melanocytes. EMBO J. 19, 2900-2910
25. Cook, S. J., and McCormick, F. (1993) Inhibition by cAMP of Ras-dependent activation of Raf. Science 262, 1069-1072
26. Wu, J., Dent, P., Jelinek, T., Wolfman, A., Weberr, M. J., and Sturgill, T. W. (1883) Inhibition of the EGF-activated MAP kinase signaling pathway by adenosine 3',5'-monophosphae. Science 262, 1065-1069
27. Dumaz, N., and Marais, R. (2005) Integrating signals between cAMP and the RAS/RAF/MEK/ERK signalling pathways. Based on the anniversary prize of the Gesellschaft fur Biochemie und Molekularbiologie Lecture delivered on 5 July 2003 at the Special FEBS Meeting in Brussels. FEBS J. 272, 3491-3504
28. Dumaz, N., and Marais, R. (2003) Protein kinase A blocks Raf-1 activity by stimulating 14-3-3 binding and blocking Raf-1 interaction with Ras. J. Biol. Chem. 278, 29819-29823
29. Brummer, T., Naegele, H., Reth, M., and Misawa, Y. (2003) Identification of novel ERK-mediated feedback phosphorylation sites at the C-terminus of B-Raf. Oncogene 22, 8823-8834
30. Dougherty, M. K., Muller, J., Ritt, D. A., Zhou, M., Zhou, X. Z., Copeland, T. D., Conrads, T. P., Veenstra, T. D., Lu, K. P., and Morrison, D. K. (2005) Regulation of Raf-1 by direct feedback phosphorylation. Mol. Cell 17, 215-224
31. Balan, V., Leicht, D. T., Zhu, J., Balan, K., Kaplun, A., Singh-Gupta, V., Qin, J., Ruan, H., Comb, M. J., and Tzivion, G. (2006) Identification of novel in vivo Raf-1 phosphorylation sites mediating positive feedback Raf-1 regulation by extracellular signal-regulated kinase. Mol. Biol. Cell 17, 1141-1153
32. Jacobowitz, O., and Iyengar, R. (1994) Phorbol ester-induced stimulation and phosphorylation of adenylyl cyclase 2. Proc. Natl. Acad. Sci. U. S. A. 91, 10630-10634
33. Murphy, L. O., Smith, S., Chen, R. H., Fingar, D. C., and Blenis, J. (2002) Molecular interpretation of ERK signal duration by immediate early gene products. Nat. Cell Biol. 4, 556-564
34. Cook, S. J., and McCormick, F. (1996) Kinetic and biochemical correlation between sustained p44ERK1 (44 kDa extracellular signal-regulated kinase 1) activation and lysophosphatidic acid-stimulated DNA synthesis in Rat-1 cells. Biochem. J. 320(Pt 1), 237-245
35. Hoffman, A., Levchenko, A., Scott, M. L., and Baltimore, D. (2002) The IkappaB-NF-kappaB signaling module: temporal control and selective gene activation. Science 298, 1241-1245
36. Marshall, C. J. (1995) Specificity of receptor tyrosine kinase signaling: transient versus sustained extracellular signal-regulated kinase activation. Cell 80, 179-185

<a id='dfc6a86a-bdf2-4db9-b983-66b76ee338b5'></a>

1402 Vol. 22 May 2008

<a id='1355205e-0813-46f7-8b17-7b493a8be58e'></a>

The FASEB Journal

<a id='f48d3e20-c66a-4915-9f87-d6ae86074540'></a>

MULLER ET AL.

<a id='721e0692-b3c2-46c4-8729-d775924907f1'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- PAGE BREAK -->

<a id='5f32c0cb-190a-4f9b-8fa8-121146a0dbcb'></a>

37. Kholodenko, B. N. (2007) Untangling the signalling wires. Nat. Cell Biol. **9**, 247-249
38. Chin, L. (2003) The genetics of malignant melanoma: lessons from mouse and man. Nat. Rev. Cancer **3**, 559-570
39. Miller, A. J., and Mihm, M. C., Jr. (2006) Melanoma. N. Engl. J. Med. **355**, 51-65
40. Nesbit, M., Nesbit, H. K., Bennett, J., Andl, T., Hsu, M. Y., Dejesus, E., McBrian, M., Gupta, A. R., Eck, S. L., and Herlyn, M. (1999) Basic fibroblast growth factor induces a transformed phenotype in normal human melanocytes. Oncogene **18**, 6469-6476
41. Slominski, A., Tobin, D. J., Shibahara, S., and Wortsman, J. (2004) Melanin pigmentation in mammalian skin and its hormonal regulation. Physiol. Rev. **84**, 1155-1228
42. Landi, M. T., Bauer, J., Pfeiffer, R. M., Elder, D. E., Hulley, B., Minghetti, P., Calista, D., Kanetsky, P. A., Pinkel, D., and Bastian, B. C. (2006) MC1R germline variants confer risk for BRAF-mutant melanoma. Science **313**, 521-522
43. Bhalla, U. S. (2002) Mechanisms for temporal tuning and filtering by postsynaptic signaling pathways. Biophys. J. **83**, 740-752
44. Gao, L., Feng, Y., Bowers, R., Becker-Hapak, M., Gardner, J., Council, L., Linette, G., Zhao, H., and Cornelius, L. A. (2006) Ras-associated protein-1 regulates extracellular signal-regulated kinase activation and migration in melanoma cells: two processes important to melanoma tumorigenesis and metastasis. Cancer Res. **66**, 7880-7888
45. Alon, U. (2003) Biological networks: the tinkerer as an engineer. Science **301**, 1866-1867
46. Hornberg, J. J., Tijssen, M. R., and Lankelma, J. (2004) Synergistic activation of signalling to extracellular signal-regulated kinases 1 and 2 by epidermal growth factor and 4 beta-phorbol 12-myristate 13-acetate. Eur. J. Biochem. **271**, 3905-3913
47. Garnett, M. J., Rana, S., Paterson, H., Barford, D., and Marais, R. (2005) Wild-type and mutant B-RAF activate C-RAF through distinct mechanisms involving heterodimerization. Mol. Cell **20**, 963-969

<a id='d6d76c08-9f30-4bf6-9aa2-0f0071d92314'></a>

48. Wan, P. T., Garnett, M. J., Roe, S. M., Lee, S., Niculescu-Duvaz, D., Good, V. M., Jones, C. M., Marshall, C. J., Springer, C. J., Barford, D., and Marais, R. (2004) Mechanism of activation of the RAF-ERK signaling pathway by oncogenic mutations of B-RAF. Cell 116, 855-867
49. Yamaguchi, T., Wallace, D. P., Magenheimer, B. S., Hempson, S. J., Grantham, J. J., and Calvet, J. P. (2004) Calcium restriction allows cAMP activation of the B-Raf/ERK pathway, switching cells to a cAMP-dependent growth-stimulated phenotype. J. Biol. Chem. 279, 40419-40430
50. Sidovar, M. F., Kozlowski, P., Lee, J. W., Collins, M. A., He, Y., and Graves, L. M. (2000) Phosphorylation of serine 43 is not required for inhibition of c-Raf kinase by the cAMP-dependent protein kinase. J. Biol. Chem. 275, 28688-28694
51. Santos, S. D., Verveer, P. J., and Bastiaens, P. I. (2007) Growth factor-induced MAPK network topology shapes Erk response determining PC-12 cell fate. Nat. Cell Biol. 9, 324-330
52. Sasagawa, S., Ozaki, Y., Fujita, K., and Kuroda, S. (2005) Prediction and validation of the distinct dynamics of transient and sustained ERK activation. Nat. Cell Biol. 7, 365-373
53. Robubi, A., Mueller, T., Fueller, J., Hekman, M., Rapp, U. R., and Dandekar, T. (2005) B-Raf and C-Raf signaling investigated in a simplified model of the mitogenic kinase cascade. Biol. Chem. 386, 1165-1171
54. Satyamoorthy, K., Li, G., Gerrero, M. R., Brose, M. S., Volpe, P., Weber, B. L., Van Belle, P., Elder, D. E., and Herlyn, M. (2003) Constitutive mitogen-activated protein kinase activation in melanoma is mediated by both BRAF mutations and autocrine growth factor stimulation. Cancer Res. 63, 756-759
55. Sun, S. Y., Rosenberg, L. M., Wang, X., Zhou, Z., Yue, P., Fu, H., and Khuri, F. R. (2005) Activation of Akt and eIF4E survival pathways by rapamycin-mediated mammalian target of rapamycin inhibition. Cancer Res. 65, 7052-7058

<a id='d8748b33-302f-492e-ae38-b7a06da454b9'></a>

Received for publication August 20, 2007.
Accepted for publication November 29, 2007.

<a id='c1b08a61-ae62-46db-9c04-58840934609e'></a>

REGULATORY MOTIF IN SIGNALING NETWORKS

<a id='a411c201-62bc-4e51-97e2-8cfdfc965286'></a>

1403

<a id='e59f6aec-7a2b-4843-ba90-ce82d83adbeb'></a>

15306860, 2008, 5, Downloaded from https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.07-9100com by Universita Di Trento, Wiley Online Library on [08/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

# Supplementary materials

<a id='70dc4028-076a-468f-b4ac-88a73c0de668'></a>

07-9100 SUPPLEMENTAL FIGURE LEGENDS

<a id='dffcd16d-e89d-4a1f-b541-9180b2406f90'></a>

TABLE S1 Rate constants and concentrations of molecules in computational model A.

<a id='d85d5146-556a-4cb4-86f0-401dba99d538'></a>

FIGURE S1 Schematics of the FGF-MC1R-MAPK1,2 network. Positive feedback loops are shown in green arrows, negative loops and interaction in red. Arrowheads are activation and plungers are inhibitions. (A) The MC1R-MAPK1,2 network showing a positive feedback loop from MAPK1,2 to C-Raf. This network connection corresponds to computational modeling results shown in Fig 1 A. (B) The MC1R-MAPK1,2 network showing a positive feedback loop to both C-Raf and B-Raf from MAPK1,2. This network connection corresponds to computational modeling results shown in Supplementary Fig S1 C. (C) Computational modeling data of MAPK1,2 activity showing a bi-phasic response to MSH if a positive feedback loop exists from MAPK1,2 to C-Raf and B-Raf.

<a id='879aa04a-92aa-480d-a3b1-ba078e4783d8'></a>

FIGURE S2 (A) The FGF-MAPK1,2 network showing a positive feedback from MAPK1,2 to C-Raf. This network connection corresponds to computational modeling results shown in Fig 1 C. (B) This model of the FGF-MAPK1,2 network includes negative feedback from MAPK1,2 to PKC. These network connections correspond to computational modeling results shown in Supplementary Fig S2 C. (C) Computational modeling of the FGF activation of MAPK with a negative feedback loop from MAPK1,2 to C-Raf. Upper curve includes PP2a de-phosphorylation of C-Raf and the lower curve is without PP2a de-phosphorylation of C-Raf. (D) The FGF-MAPK1,2 network including a negative feedback from MAPK1,2 to PKC, as well as a feed forward from PKC to AC. This network connection corresponds to computational modeling results shown in Supplementary Fig S2 E. (E) Computational modeling of the FGF activation of MAPK1,2 with PKC activation of adenyl cyclase.

<a id='6947a4d7-2933-464f-8bf3-1249949b892e'></a>

FIGURE S3 (A) Experimental data from SB2 cells that were serum starved and stimulated with MSH (2 M) for 5 minutes. Cells were incubated for the times indicated and cell lysates probed for phospho-MAPK1,2. The blots were also probed for ̖-Actin to control for loading. Blots were scanned, band intensities quantified and shown on the graph as fold increase in band intensities as compared to non-stimulated cells after normalizing for ̖-Actin. (B) Experimental data from SB2 cells serum starved, stimulated with FGF (20 ng/ml) and probed for phospho-MAPK1,2. ̖-Actin is shown for loading control. (C) SB2 cells were serum starved and stimulated with MSH for 5 minutes followed by FGF for 5 minutes. The ligands were washed out and cells incubated in 1% medium for times indicated. Lysates were probed for phospho-MAPK1,2 and ̖-Actin. Graph shows fold change in phospho-MAPK1,2 after normalization for ̖-Actin. (D) Experimental data from SB2 cells transfected with either C-Raf specific siRNA or non-specific siRNA. Cell lysates were probed for C-Raf, B-Raf and ̖-Actin as shown.

<a id='3391fe16-ca2a-47e8-9c60-cab5aba1d73a'></a>

FIGURE S4 (A-B) Experimental data obtained from RPPA slides. SB2 cells were serum-starved and stimulated with MSH (2 μM), FGF (20 ng/ml) or MSH followed by FGF for 5 minutes. Cells were then incubated in 1% MEM for times indicated. Cell lysates were serially diluted and spotted on RPPA slides. Slides were probed using (A) phospho-MAPK1,2 and (B) ERK2 antibodies. Spots were scanned, intensities quantified and shown on the graph as fold increase in spot intensities as compared to non-stimulated controls.

<a id='3fba6bb1-fa6b-4755-afa4-7329f9ce6cb1'></a>

FIGURE S5 Network topology model proposed for the activation of MAPK1,2 when initiated due to upstream activation of the FGFR and MC1R.

<a id='ebc3fcf8-74a1-4d24-be57-6677260edfca'></a>

TABLE S2 The following dynamical system of ordinary differential equations depicts the relevant mathematical model shown in Supplementary Figure S5.

<!-- PAGE BREAK -->

<a id='8e53f125-4dc8-43fd-a08e-44cdbd3d7f21'></a>

Table S1 (supplementary data)
**Molecule List**
<table id="1-1">
<tr><td id="1-2">Name</td><td id="1-3">Initial Conc (µM)</td></tr>
<tr><td id="1-4">AA</td><td id="1-5">6.12</td></tr>
<tr><td id="1-6">AA</td><td id="1-7">0</td></tr>
<tr><td id="1-8">AC</td><td id="1-9">0.015</td></tr>
<tr><td id="1-a">AMP</td><td id="1-b">1000</td></tr>
<tr><td id="1-c">APC</td><td id="1-d">30</td></tr>
<tr><td id="1-e">ATP</td><td id="1-f">5000</td></tr>
<tr><td id="1-g">BetaGamma</td><td id="1-h">0</td></tr>
<tr><td id="1-i">B-Raf</td><td id="1-j">0.2</td></tr>
<tr><td id="1-k">Ca</td><td id="1-l">0.08</td></tr>
<tr><td id="1-m">cAMP</td><td id="1-n">0</td></tr>
<tr><td id="1-o">cAMP.R2C2</td><td id="1-p">0</td></tr>
<tr><td id="1-q">cAMP2.R2C2</td><td id="1-r">0</td></tr>
<tr><td id="1-s">cAMP3.R2C2</td><td id="1-t">0</td></tr>
<tr><td id="1-u">cAMP4.R2</td><td id="1-v">0</td></tr>
<tr><td id="1-w">cAMP4.R2C</td><td id="1-x">0</td></tr>
<tr><td id="1-y">cAMP4.R2C2</td><td id="1-z">0</td></tr>
<tr><td id="1-A">cAMP-GEF</td><td id="1-B">0.1</td></tr>
<tr><td id="1-C">cAMP-PDE</td><td id="1-D">0.5</td></tr>
<tr><td id="1-E">cAMP-PDE*</td><td id="1-F">0</td></tr>
<tr><td id="1-G">c-Raf-1</td><td id="1-H">0.2</td></tr>
<tr><td id="1-I">c-Raf-1*</td><td id="1-J">0</td></tr>
<tr><td id="1-K">c-Raf-1*</td><td id="1-L">0</td></tr>
<tr><td id="1-M">DAG-Ca-PLA2*</td><td id="1-N">0</td></tr>
<tr><td id="1-O">DAG-Ca-PLA2*</td><td id="1-P">11.661</td></tr>
<tr><td id="1-Q">FGF</td><td id="1-R">0</td></tr>
<tr><td id="1-S">FGFR</td><td id="1-T">0.10833</td></tr>
<tr><td id="1-U">GAP</td><td id="1-V">0.002</td></tr>
<tr><td id="1-W">GAP*</td><td id="1-X">0</td></tr>
<tr><td id="1-Y">Gbg</td><td id="1-Z">0</td></tr>
<tr><td id="1-10">GDP.Ga</td><td id="1-11">0</td></tr>
<tr><td id="1-12">GDP.Gabc</td><td id="1-13">1</td></tr>
<tr><td id="1-14">GDP-Ras</td><td id="1-15">0.2</td></tr>
<tr><td id="1-16">GEF*</td><td id="1-17">0</td></tr>
<tr><td id="1-18">Grb2</td><td id="1-19">1</td></tr>
<tr><td id="1-1a">Gs.AC</td><td id="1-1b">0</td></tr>
<tr><td id="1-1c">Gs-alpha</td><td id="1-1d">0</td></tr>
<tr><td id="1-1e">GTP-Ras</td><td id="1-1f">0</td></tr>
<tr><td id="1-1g">inact-GEF</td><td id="1-1h">0.1</td></tr>
<tr><td id="1-1i">inhibited-PKA</td><td id="1-1j">0</td></tr>
<tr><td id="1-1k">Internal L.FGFR</td><td id="1-1l">0</td></tr>
<tr><td id="1-1m">L.FGFR</td><td id="1-1n">0</td></tr>
<tr><td id="1-1o">L.R</td><td id="1-1p">0</td></tr>
<tr><td id="1-1q">L.R.GDP.Gabc</td><td id="1-1r">0</td></tr>
<tr><td id="1-1s">MAPK</td><td id="1-1t">0.36</td></tr>
<tr><td id="1-1u">MAPK*</td><td id="1-1v">0</td></tr>
<tr><td id="1-1w">MAPK-*</td><td id="1-1x">0</td></tr>
<tr><td id="1-1y">MAPKK</td><td id="1-1z">0.18</td></tr>
<tr><td id="1-1A">MAPKK*</td><td id="1-1B">0</td></tr>
<tr><td id="1-1C">MAPKK-ser</td><td id="1-1D">0</td></tr>
<tr><td id="1-1E">MAPK-tyr</td><td id="1-1F">0</td></tr>
<tr><td id="1-1G">MC1R</td><td id="1-1H">0.01</td></tr>
<tr><td id="1-1I">MKP-1</td><td id="1-1J">0.0004</td></tr>
<tr><td id="1-1K">MKP-1**</td><td id="1-1L">0</td></tr>
</table>

<a id='6ee69328-fff7-4304-aba9-ed41daa560c6'></a>

Molecule List
<table id="1-1M">
<tr><td id="1-1N">Name</td><td id="1-1O">Initial Conc (µM)</td></tr>
<tr><td id="1-1P">MKP1-RNA</td><td id="1-1Q">1.00E-04</td></tr>
<tr><td id="1-1R">MKP-1-ser359*</td><td id="1-1S">0</td></tr>
<tr><td id="1-1T">MKP-2</td><td id="1-1U">0.002</td></tr>
<tr><td id="1-1V">MSH</td><td id="1-1W">2</td></tr>
<tr><td id="1-1X">nuc MAPK*</td><td id="1-1Y">0</td></tr>
<tr><td id="1-1Z">Nucleotides</td><td id="1-20">0.1</td></tr>
<tr><td id="1-21">PIP2-Ca-PLA2*</td><td id="1-22">0</td></tr>
<tr><td id="1-23">PIP2-PLA2*</td><td id="1-24">0</td></tr>
<tr><td id="1-25">PKA-active</td><td id="1-26">0</td></tr>
<tr><td id="1-27">PKA-inhibitor</td><td id="1-28">0.25</td></tr>
<tr><td id="1-29">PKC-AA*</td><td id="1-2a">1.81E-17</td></tr>
<tr><td id="1-2b">PKC-active</td><td id="1-2c">0.02</td></tr>
<tr><td id="1-2d">PKC-active</td><td id="1-2e">0.02</td></tr>
<tr><td id="1-2f">PKC-basal</td><td id="1-2g">2.00E-02</td></tr>
<tr><td id="1-2h">PKC-Ca-AA*</td><td id="1-2i">1.75E-16</td></tr>
<tr><td id="1-2j">PKC-Ca-DAG</td><td id="1-2k">8.46E-23</td></tr>
<tr><td id="1-2l">PKC-Ca-DAG</td><td id="1-2m">3.72E-17</td></tr>
<tr><td id="1-2n">PKC-Ca-memb*</td><td id="1-2o">1.39E-17</td></tr>
<tr><td id="1-2p">PKC-cytosolic</td><td id="1-2q">1</td></tr>
<tr><td id="1-2r">PKC-DAG</td><td id="1-2s">0</td></tr>
<tr><td id="1-2t">PKC-DAG-AA</td><td id="1-2u">2.52E-19</td></tr>
<tr><td id="1-2v">PKC-DAG-AA*</td><td id="1-2w">4.91E-18</td></tr>
<tr><td id="1-2x">PKC-DAG-memb*</td><td id="1-2y">9.44E-21</td></tr>
<tr><td id="1-2z">PLA2*</td><td id="1-2A">0</td></tr>
<tr><td id="1-2B">PLA2*-Ca</td><td id="1-2C">0</td></tr>
<tr><td id="1-2D">PLA2-Ca*</td><td id="1-2E">0</td></tr>
<tr><td id="1-2F">PLA2-cytosolic</td><td id="1-2G">0.4</td></tr>
<tr><td id="1-2H">PP1-active</td><td id="1-2I">1.8</td></tr>
<tr><td id="1-2J">PP2A</td><td id="1-2K">0.12</td></tr>
<tr><td id="1-2L">PPhosphatase2A</td><td id="1-2M">0.224</td></tr>
<tr><td id="1-2N">R</td><td id="1-2O">0.0833</td></tr>
<tr><td id="1-2P">R.GDP.Gabc</td><td id="1-2Q">0</td></tr>
<tr><td id="1-2R">R2C2</td><td id="1-2S">0.5</td></tr>
<tr><td id="1-2T">Raf-GTP-Ras</td><td id="1-2U">0</td></tr>
<tr><td id="1-2V">RGR</td><td id="1-2W">0</td></tr>
<tr><td id="1-2X">SHC</td><td id="1-2Y">0.5</td></tr>
<tr><td id="1-2Z">SHC*</td><td id="1-30">0</td></tr>
<tr><td id="1-31">Shc*.Sos.Grb2</td><td id="1-32">0</td></tr>
<tr><td id="1-33">Sos</td><td id="1-34">0.1</td></tr>
<tr><td id="1-35">Sos*</td><td id="1-36">0</td></tr>
<tr><td id="1-37">Sos*.Grb2</td><td id="1-38">0</td></tr>
<tr><td id="1-39">Sos.Grb2</td><td id="1-3a">0</td></tr>
<tr><td id="1-3b">temp-PIP2</td><td id="1-3c">2.5</td></tr>
<tr><td id="1-3d">tot MKP1</td><td id="1-3e">0</td></tr>
<tr><td id="1-3f">Ubiquitination</td><td id="1-3g">0</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='797f59dd-9092-4458-b7a3-11ec2be58c5f'></a>

Table S1 (supplementary data) cont.
**Reaction List**

<table id="2-1">
<tr><td id="2-2">Name</td><td id="2-3">Kf</td><td id="2-4">Kb</td></tr>
<tr><td id="2-5">act FGFR</td><td id="2-6">200</td><td id="2-7">0.1</td></tr>
<tr><td id="2-8">Activate-Gs</td><td id="2-9">0.025</td><td id="2-a">0</td></tr>
<tr><td id="2-b">Basal transcription</td><td id="2-c">5.00E-06</td><td id="2-d">0</td></tr>
<tr><td id="2-e">cAMP-bind-site-A1</td><td id="2-f">75</td><td id="2-g">110</td></tr>
<tr><td id="2-h">cAMP-bind-site A2</td><td id="2-i">75</td><td id="2-j">32.5</td></tr>
<tr><td id="2-k">cAMP-bind-site-B1</td><td id="2-l">54</td><td id="2-m">33</td></tr>
<tr><td id="2-n">cAMP-bind-site-B2</td><td id="2-o">54</td><td id="2-p">33</td></tr>
<tr><td id="2-q">cAMP-cAMPGEF</td><td id="2-r">75</td><td id="2-s">3</td></tr>
<tr><td id="2-t">DAG-Ca-PLA2-act</td><td id="2-u">0.003</td><td id="2-v">4</td></tr>
<tr><td id="2-w">Degrade-AA</td><td id="2-x">0.4</td><td id="2-y">0</td></tr>
<tr><td id="2-z">dephosph Shc</td><td id="2-A">0.01</td><td id="2-B">0</td></tr>
<tr><td id="2-C">dephosph Sos</td><td id="2-D">0.001</td><td id="2-E">0</td></tr>
<tr><td id="2-F">dephosph-GAP</td><td id="2-G">0.1</td><td id="2-H">0</td></tr>
<tr><td id="2-I">Dephosph-GEF</td><td id="2-J">0.1</td><td id="2-K">0</td></tr>
<tr><td id="2-L">dephosphorylate-PLA2*</td><td id="2-M">0.17</td><td id="2-N">0</td></tr>
<tr><td id="2-O">Grb2 bind Sos</td><td id="2-P">0.025</td><td id="2-Q">0.0168</td></tr>
<tr><td id="2-R">Grb2 bind Sos*</td><td id="2-S">0.025</td><td id="2-T">0.0168</td></tr>
<tr><td id="2-U">GTPase</td><td id="2-V">0.0667</td><td id="2-W">0</td></tr>
<tr><td id="2-X">inhib-PKA</td><td id="2-Y">60</td><td id="2-Z">1</td></tr>
<tr><td id="2-10">Internalize</td><td id="2-11">0.001</td><td id="2-12">0.00066</td></tr>
<tr><td id="2-13">L.R-bind-Gabc</td><td id="2-14">10.0002</td><td id="2-15">0.1</td></tr>
<tr><td id="2-16">L-bind-R</td><td id="2-17">0.1</td><td id="2-18">0.1</td></tr>
<tr><td id="2-19">L-bind-R.Gabc</td><td id="2-1a">5</td><td id="2-1b">0.1</td></tr>
<tr><td id="2-1c">MKP-1**dephosph</td><td id="2-1d">0.0001</td><td id="2-1e">0</td></tr>
<tr><td id="2-1f">MKP-1*dephosph</td><td id="2-1g">0.0001</td><td id="2-1h">0</td></tr>
<tr><td id="2-1i">MKP1 synth</td><td id="2-1j">0.002</td><td id="2-1k">0</td></tr>
<tr><td id="2-1l">PIP2-Ca-PLA2-act</td><td id="2-1m">0.012</td><td id="2-1n">0.1</td></tr>
<tr><td id="2-1o">PIP2-PLA2-act</td><td id="2-1p">0.0012</td><td id="2-1q">0.5</td></tr>
<tr><td id="2-1r">PKC-act-by-AA</td><td id="2-1s">0.00012</td><td id="2-1t">0.1</td></tr>
<tr><td id="2-1u">PKC-act-by-Ca</td><td id="2-1v">0.6</td><td id="2-1w">0.5</td></tr>
<tr><td id="2-1x">PKC-act-by-Ca-AA</td><td id="2-1y">0.0012</td><td id="2-1z">0.1</td></tr>
<tr><td id="2-1A">PKC-act-by-DAG</td><td id="2-1B">0.0079998</td><td id="2-1C">8.6348</td></tr>
<tr><td id="2-1D">PKC-act-by-DAG-AA</td><td id="2-1E">2</td><td id="2-1F">0.2</td></tr>
<tr><td id="2-1G">PKC-basal-act</td><td id="2-1H">1</td><td id="2-1I">50</td></tr>
<tr><td id="2-1J">PKC-Ca-to-memb</td><td id="2-1K">1.2705</td><td id="2-1L">3.5026</td></tr>
<tr><td id="2-1M">PKC-DAG-to-memb</td><td id="2-1N">1</td><td id="2-1O">0.1</td></tr>
<tr><td id="2-1P">PKC-n-DAG</td><td id="2-1Q">0.0006</td><td id="2-1R">0.1</td></tr>
<tr><td id="2-1S">PKC-n-DAG-AA</td><td id="2-1T">0.018</td><td id="2-1U">2</td></tr>
<tr><td id="2-1V">PLA2*-CaDact</td><td id="2-1W">6</td><td id="2-1X">0.1</td></tr>
<tr><td id="2-1Y">PLA2-Ca-act</td><td id="2-1Z">1</td><td id="2-20">0.1</td></tr>
<tr><td id="2-21">Ras-act-c Raf</td><td id="2-22">60</td><td id="2-23">0.5</td></tr>
<tr><td id="2-24">Ras-act-unphosph-Raf</td><td id="2-25">6</td><td id="2-26">1</td></tr>
<tr><td id="2-27">Ras-B-Raf</td><td id="2-28">0.15</td><td id="2-29">0.1</td></tr>
<tr><td id="2-2a">Ras-intrinsic GTPase</td><td id="2-2b">0.0001</td><td id="2-2c">0</td></tr>
<tr><td id="2-2d">R-bind-Gabc</td><td id="2-2e">0.2</td><td id="2-2f">0.1</td></tr>
<tr><td id="2-2g">Release-C1</td><td id="2-2h">60</td><td id="2-2i">18</td></tr>
<tr><td id="2-2j">Release-C2</td><td id="2-2k">60</td><td id="2-2l">18</td></tr>
<tr><td id="2-2m">Shc bind Sos.Grb2</td><td id="2-2n">0.49998</td><td id="2-2o">0.1</td></tr>
<tr><td id="2-2p">translocation</td><td id="2-2q">0.01</td><td id="2-2r">0.005</td></tr>
<tr><td id="2-2s">Trimerize-Gs</td><td id="2-2t">6</td><td id="2-2u">0</td></tr>
<tr><td id="2-2v">turnover MKP1</td><td id="2-2w">0.00037</td><td id="2-2x">0</td></tr>
<tr><td id="2-2y">turnover MKP1*</td><td id="2-2z">0.0001</td><td id="2-2A">0</td></tr>
<tr><td id="2-2B">turnover MKP1**</td><td id="2-2C">0.0001</td><td id="2-2D">0</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='0eb104e8-0cef-4715-ba4f-a4f9edcc2c48'></a>

Table S1 (supplementary data) cont.
Enzyme List
<table id="3-1">
<tr><td id="3-2">Molecule</td><td id="3-3">Site name</td><td id="3-4">Km</td><td id="3-5">Vmax</td><td id="3-6">Ratio (k2/k3)</td></tr>
<tr><td id="3-7">DAG-Ca-PLA2*</td><td id="3-8">kenz</td><td id="3-9">20</td><td id="3-a">60</td><td id="3-b">4</td></tr>
<tr><td id="3-c">GAP</td><td id="3-d">GAP-inact-ras</td><td id="3-e">1.0104</td><td id="3-f">10</td><td id="3-g">100</td></tr>
<tr><td id="3-h">GEF*</td><td id="3-i">GEF*-act-ras</td><td id="3-j">0.50505</td><td id="3-k">0.02</td><td id="3-l">4</td></tr>
<tr><td id="3-m">L.FGFR</td><td id="3-n">phosph Shc</td><td id="3-o">0.8333</td><td id="3-p">0.05</td><td id="3-q">4</td></tr>
<tr><td id="3-r">L.FGFR</td><td id="3-s">phosph PLC g</td><td id="3-t">0.3333</td><td id="3-u">0.2</td><td id="3-v">4</td></tr>
<tr><td id="3-w">MAPK*</td><td id="3-x">MAPK*</td><td id="3-y">25.641</td><td id="3-z">20</td><td id="3-A">4</td></tr>
<tr><td id="3-B">MAPK*</td><td id="3-C">MAPK*-feedback</td><td id="3-D">25.641</td><td id="3-E">10</td><td id="3-F">4</td></tr>
<tr><td id="3-G">MAPK*</td><td id="3-H">MKP-1-phosph</td><td id="3-I">25.641</td><td id="3-J">1</td><td id="3-K">4</td></tr>
<tr><td id="3-L">MAPK*</td><td id="3-M">MKP-1-phosph2</td><td id="3-N">25.641</td><td id="3-O">1</td><td id="3-P">4</td></tr>
<tr><td id="3-Q">MAPKK*</td><td id="3-R">MAPKKtyr</td><td id="3-S">0.046296</td><td id="3-T">0.15</td><td id="3-U">4</td></tr>
<tr><td id="3-V">MAPKK*</td><td id="3-W">MAPKKThr</td><td id="3-X">0.04693</td><td id="3-Y">0.15</td><td id="3-Z">4</td></tr>
<tr><td id="3-10">MKP-1</td><td id="3-11">MKP-1-thr-deph</td><td id="3-12">0.066667</td><td id="3-13">1</td><td id="3-14">4</td></tr>
<tr><td id="3-15">MKP-1</td><td id="3-16">MKP-1-Tyr-deph</td><td id="3-17">0.066667</td><td id="3-18">1</td><td id="3-19">4</td></tr>
<tr><td id="3-1a">MKP-1**</td><td id="3-1b">MKP1*-thr-deph</td><td id="3-1c">0.066667</td><td id="3-1d">1</td><td id="3-1e">4</td></tr>
<tr><td id="3-1f">MKP-1**</td><td id="3-1g">MKP1*-tyr-deph</td><td id="3-1h">0.066667</td><td id="3-1i">1</td><td id="3-1j">4</td></tr>
<tr><td id="3-1k">MKP-2</td><td id="3-1l">MKP2-thr-deph</td><td id="3-1m">0.066667</td><td id="3-1n">1</td><td id="3-1o">4</td></tr>
<tr><td id="3-1p">MKP-2</td><td id="3-1q">MKP-tyr-deph</td><td id="3-1r">0.066667</td><td id="3-1s">1</td><td id="3-1t">4</td></tr>
<tr><td id="3-1u">nuc MAPK*</td><td id="3-1v">act transcription</td><td id="3-1w">4</td><td id="3-1x">0.0008</td><td id="3-1y">4</td></tr>
<tr><td id="3-1z">PIP2-Ca-PLA2*</td><td id="3-1A">kenz</td><td id="3-1B">20</td><td id="3-1C">36</td><td id="3-1D">4</td></tr>
<tr><td id="3-1E">PIP2-PLA2*</td><td id="3-1F">kenz</td><td id="3-1G">20</td><td id="3-1H">11.04</td><td id="3-1I">4</td></tr>
<tr><td id="3-1J">PKC-active</td><td id="3-1K">PKC-act-Raf</td><td id="3-1L">66.667</td><td id="3-1M">4</td><td id="3-1N">4</td></tr>
<tr><td id="3-1O">PKC-active</td><td id="3-1P">PKC-act-GEF</td><td id="3-1Q">66.667</td><td id="3-1R">4</td><td id="3-1S">4</td></tr>
<tr><td id="3-1T">PKC-active</td><td id="3-1U">PKC-inact-GAP</td><td id="3-1V">66.667</td><td id="3-1W">25</td><td id="3-1X">4</td></tr>
<tr><td id="3-1Y">PLA2*-Ca</td><td id="3-1Z">kenz</td><td id="3-20">20</td><td id="3-21">120</td><td id="3-22">4</td></tr>
<tr><td id="3-23">PLA2-Ca*</td><td id="3-24">kenz</td><td id="3-25">20</td><td id="3-26">5.4</td><td id="3-27">4</td></tr>
<tr><td id="3-28">PPhosphatase2A</td><td id="3-29">craf**-deph</td><td id="3-2a">15.657</td><td id="3-2b">6</td><td id="3-2c">4.1667</td></tr>
<tr><td id="3-2d">PPhosphatase2A</td><td id="3-2e">craf-deph</td><td id="3-2f">15.657</td><td id="3-2g">6</td><td id="3-2h">4.1667</td></tr>
<tr><td id="3-2i">PPhosphatase2A</td><td id="3-2j">MAPKK-deph</td><td id="3-2k">15.657</td><td id="3-2l">6</td><td id="3-2m">4.1667</td></tr>
<tr><td id="3-2n">PPhosphatase2A</td><td id="3-2o">MAPKK-deph-ser</td><td id="3-2p">15.657</td><td id="3-2q">6</td><td id="3-2r">4.1667</td></tr>
<tr><td id="3-2s">Raf*-GTP-Ras</td><td id="3-2t">Raf-GTP-Ras.1</td><td id="3-2u">0.15909</td><td id="3-2v">0.105</td><td id="3-2w">4</td></tr>
<tr><td id="3-2x">Raf*-GTP-Ras</td><td id="3-2y">Raf-GTP-Ras.2</td><td id="3-2z">0.15909</td><td id="3-2A">0.105</td><td id="3-2B">4</td></tr>
<tr><td id="3-2C">RGR</td><td id="3-2D">RGR.1</td><td id="3-2E">0.15909</td><td id="3-2F">0.105</td><td id="3-2G">4</td></tr>
<tr><td id="3-2H">RGR</td><td id="3-2I">RGR.2</td><td id="3-2J">0.15909</td><td id="3-2K">0.105</td><td id="3-2L">4</td></tr>
<tr><td id="3-2M">Shc*.Sos.Grb2</td><td id="3-2N">Sos.Ras GEF</td><td id="3-2O">0.50505</td><td id="3-2P">0.02</td><td id="3-2Q">4</td></tr>
<tr><td id="3-2R">Molecule</td><td id="3-2S">Site name</td><td id="3-2T">Km</td><td id="3-2U">Kcat</td><td id="3-2V">Ratio (k2/k3)</td></tr>
<tr><td id="3-2W">Braf-MEK</td><td id="3-2X">Braf-MEK</td><td id="3-2Y">0.15</td><td id="3-2Z">0.1</td><td id="3-30">4</td></tr>
<tr><td id="3-31">cAMPGEF-Ras</td><td id="3-32">cAMPGEF-Ras</td><td id="3-33">0.5</td><td id="3-34">2</td><td id="3-35">4</td></tr>
<tr><td id="3-36">cyclase</td><td id="3-37">Gs-AC</td><td id="3-38">20</td><td id="3-39">18</td><td id="3-3a">4</td></tr>
<tr><td id="3-3b">MAPK1,2-Braf</td><td id="3-3c">MAPK1,2-Braf</td><td id="3-3d">25</td><td id="3-3e">10</td><td id="3-3f">4</td></tr>
<tr><td id="3-3g">PDE</td><td id="3-3h">cAMP-PDE</td><td id="3-3i">19.8413</td><td id="3-3j">10</td><td id="3-3k">4</td></tr>
<tr><td id="3-3l">PDE*</td><td id="3-3m">cAMP-PDE*</td><td id="3-3n">19.8413</td><td id="3-3o">20</td><td id="3-3p">4</td></tr>
<tr><td id="3-3q">PKA-Craf</td><td id="3-3r">PKA-Craf</td><td id="3-3s">7</td><td id="3-3t">9</td><td id="3-3u">4</td></tr>
<tr><td id="3-3v">PP2A-Craf</td><td id="3-3w">PP2A Craf</td><td id="3-3x">30</td><td id="3-3y">3</td><td id="3-3z">4</td></tr>
</table>

<a id='a5af0a9c-51b6-4b63-9edf-0e64943e94ee'></a>

Kf - µM⁻¹s⁻¹
Kb - s⁻¹
Kf - µM
Kcat - s⁻¹

<!-- PAGE BREAK -->

<a id='cf48be7c-2cd0-4e76-87db-7e9a2089d650'></a>

Figure S1 (supplementary data)

<a id='44804234-9aa6-47db-bc02-ce747df04120'></a>

<::Figure A: A signaling pathway diagram is shown. It depicts two main interconnected pathways: the cAMP/PKA pathway and the MAPK pathway.  On the right, the cAMP/PKA pathway starts with MC1R activating Gαs, which then activates AC. AC produces cAMP, which activates PKA.  On the left, the MAPK pathway starts with Ras activating C-Raf, which activates MEK. MEK then activates MAPK 1,2. MAPK 1,2 leads to gene transcription (indicated by a wavy line and bent arrow).  There are several cross-talks and feedback loops:  1. cAMP activates cAMP-GEF, which in turn activates Ras.  2. PKA activates B-Raf.  3. B-Raf activates MEK.  4. C-Raf inhibits B-Raf (red T-bar).  5. B-Raf inhibits C-Raf (red T-bar).  6. PKA inhibits C-Raf (red T-bar).  7. PKA inhibits MAPK 1,2 (red T-bar).  8. MAPK 1,2 activates MKP1.  9. MKP1 inhibits MAPK 1,2 (red T-bar).  10. MKP1 also leads to gene transcription (indicated by a wavy line and bent arrow).  11. MAPK 1,2 provides positive feedback to C-Raf (green arrow).: diagram::>

<a id='ab6dbb16-570e-462d-81d6-e23f14c84366'></a>

B<::Diagram illustrating signaling pathways. The diagram consists of several molecular components interconnected by arrows (activation) and blunt-ended lines (inhibition). The components are organized into two main branches:

**Right Branch (cAMP pathway):**
- MC1R activates Gαs.
- Gαs activates AC.
- AC produces cAMP.
- cAMP activates PKA.

**Left/Middle Branch (Ras/MAPK pathway and its regulation):**
- cAMP activates cAMP-GEF.
- cAMP-GEF activates Ras.
- Ras activates C-Raf.
- Ras activates B-Raf.
- C-Raf activates MEK.
- B-Raf activates MEK.
- MEK activates MAPK 1,2.
- MAPK 1,2 promotes gene expression (indicated by an arrow pointing to a DNA strand and promoter).
- MAPK 1,2 activates MKP1.

**Regulatory Interactions:**
- cAMP inhibits C-Raf (red blunt line).
- PKA inhibits C-Raf (red blunt line).
- PKA inhibits B-Raf (red blunt line).
- MAPK 1,2 activates C-Raf (green arrow).
- MAPK 1,2 activates B-Raf (green arrow).
- MKP1 inhibits MAPK 1,2 (red blunt line).
- MKP1 inhibits gene expression (red blunt line pointing to the DNA strand and promoter).
: flowchart::>

<a id='6fd6af2d-44eb-44bc-b166-97bd3c15d3f2'></a>

C<::chart: A line graph showing Active MAPK1,2 (uM) on the y-axis and Time (min) on the x-axis. The y-axis ranges from 0.00 to 0.20 in increments of 0.05. The x-axis ranges from 0 to 60 minutes, with major ticks at 0, 10, 20, 30, 40, 50, and 60. A label "Stimulus" is present below the x-axis, with an underline indicating its duration from time 0 to approximately 5 minutes. The line starts at 0, rapidly increases to a peak around 0.16 uM at approximately 3 minutes, then decreases to a trough around 0.08 uM at approximately 8 minutes. It then rises again to a second, broader peak around 0.15 uM at approximately 25 minutes, and gradually declines to about 0.10 uM at 60 minutes.::>

<!-- PAGE BREAK -->

<a id='448a3f1e-8608-4ea7-8087-3c72b15f86b0'></a>

Figure S2 (supplementary data)

<a id='dbb92585-358a-4adf-b3f5-e868ce0b9b6f'></a>

<::Figure A: A signaling pathway diagram. The pathway starts with FGF-R, which activates Ras. Ras then activates both C-Raf and B-Raf. C-Raf activates MEK, and B-Raf also activates MEK. MEK activates MAPK 1,2. MAPK 1,2 has several downstream effects: it activates gene transcription (indicated by an arrow pointing to a gene symbol at the bottom), it inhibits B-Raf (indicated by a red blunt line), and it activates MKP1. MKP1, in turn, inhibits MAPK 1,2 (indicated by a red blunt line). There is also a green arrow from C-Raf looping back to activate MAPK 1,2.::>

<a id='187f4898-7a33-4a1c-8111-47bfd7b5405c'></a>

<::B: A signaling pathway diagram. FGF-R activates Ras. cAMP-GEF also activates Ras. Ras activates C-Raf. Ras also activates MEK. B-Raf activates MEK. C-Raf activates MEK. MEK activates MAPK 1,2. MAPK 1,2 leads to gene transcription, indicated by a DNA strand and an arrow. The pathway also shows feedback loops: C-Raf inhibits Ras. C-Raf shows self-activation (green arrow). MAPK 1,2 inhibits C-Raf. MAPK 1,2 inhibits B-Raf. MAPK 1,2 activates MKP1. MKP1 inhibits MAPK 1,2.: flowchart::>

<a id='b218fec4-8757-4e4c-a76c-d6733bc41f0f'></a>

C<::A line graph titled 'Active MAPK1,2 (μM)' on the y-axis and 'Time (min)' on the x-axis. The y-axis ranges from 0.00 to 0.20 with major ticks at 0.05 intervals. The x-axis ranges from 0 to 60 with major ticks every 10 minutes. A bar labeled 'Stimulus' is present on the x-axis from 0 to approximately 5 minutes. Two curves are plotted: One curve rises from 0, peaks around 15 minutes at approximately 0.11 μM, and then declines sharply back to near zero by 25-30 minutes. The second curve rises from 0, peaks around 15-20 minutes at approximately 0.17 μM, and then gradually declines to about 0.12 μM by 60 minutes.: chart::>

<!-- PAGE BREAK -->

<a id='f96f0a98-bf4c-446b-8869-6a45ded20452'></a>

Figure S2 (supplementary data)

<a id='659e7f71-ae9e-45a9-b923-a8537d1375ec'></a>

<::Signaling pathway diagram labeled D.The pathway starts with FGF-R (Fibroblast Growth Factor Receptor) activating Ras. cAMP-GEF also activates Ras. Ras then activates C-Raf and B-Raf. PKC (Protein Kinase C) activates C-Raf. C-Raf and B-Raf mutually inhibit each other (red inhibition lines). cAMP-GEF activates AC (Adenylyl Cyclase), which produces cAMP. cAMP activates PKA (Protein Kinase A). PKA inhibits both C-Raf and B-Raf. Both C-Raf and B-Raf activate MEK (MAPK/ERK Kinase). MEK activates MAPK 1,2 (Mitogen-Activated Protein Kinase 1,2). MAPK 1,2 activates MKP1 (MAP Kinase Phosphatase 1). MKP1 inhibits MAPK 1,2. MAPK 1,2 also activates PKC. Finally, MAPK 1,2 leads to gene expression, indicated by a transcription initiation complex on a DNA strand. Arrows indicate activation, and red lines with a perpendicular bar indicate inhibition.: diagram::>

<a id='1086f030-95df-40f5-86dd-33e87ff96f60'></a>

E
<::line chart showing the concentration of Active MAPK1,2 (μM) over Time (min). The y-axis ranges from 0.00 to 0.20. The x-axis ranges from 0 to 60 minutes. A horizontal bar labeled "Stimulus" is present on the x-axis from 0 to approximately 5 minutes. The line plot shows an initial sharp increase in Active MAPK1,2 concentration peaking around 0.16 μM at approximately 5 minutes, then decreasing to about 0.08 μM by 10 minutes. Following this, it gradually increases to about 0.11 μM around 30-40 minutes, and then slowly decreases towards 0.08 μM by 60 minutes.: chart::>

<!-- PAGE BREAK -->

<a id='a3b5b987-5d1c-40e1-8d63-4ca1ae751232'></a>

Figure S3 (supplementary data)

<a id='0967fc0f-437c-4928-8299-389134e08891'></a>

<::Figure A: This figure consists of two panels. The top panel shows a Western blot analysis, and the bottom panel displays a corresponding line graph.

Western blot:
MSH (2 µM) treatment times (Min) are indicated across the top: 0, 5, 10, 15, 25, 35, 45, 65.
The blot shows three rows of protein bands:
- p-MAPK1,2: Bands are faint at 0 min, increase significantly at 5 min, remain elevated at 10 and 15 min, then gradually decrease but are still present at 25, 35, 45, and 65 min.
- MAPK1,2: Bands appear relatively consistent across all time points, indicating stable total protein levels.
- Actin: Bands also appear relatively consistent across all time points, serving as a loading control.

Line graph:
- Y-axis: Fold increase pMAPK1,2, with values ranging from 0 to 4.
- X-axis: Time (Min), with tick marks at 0, 10, 20, 30, 40, 50, 60, 70.
- A black line plot shows the fold increase of pMAPK1,2 over time. The value starts around 1 at 0 min, sharply rises to approximately 3.5 at 5 min, drops to about 1.6 at 10 min, then fluctuates between approximately 1.4 and 1.7 from 15 min to 65 min.
- Below the x-axis, a horizontal bar labeled "Stimulus" spans from 0 to approximately 5-10 min, indicating the duration of stimulation.
: figure::>

<a id='a1747035-2225-46a3-91e4-f5e2e12cc839'></a>

B
<:: The figure shows two panels. The top panel is a Western blot, labeled "FGF (20 ng/ml)" across the top, with time points in minutes (0, 5, 10, 15, 25, 35, 45, 65) indicated. The blot shows bands for P-MAPK1,2, MAPK1,2, and Actin. The P-MAPK1,2 bands appear to increase in intensity after stimulation and then decrease. The MAPK1,2 and Actin bands appear relatively constant across time points. The bottom panel is a line graph titled "Fold increase pMAPK1,2". The X-axis is labeled "Time (Min)" ranging from 0 to 70, with a black bar below indicating "Stimulus" from 0 to approximately 5 minutes. The Y-axis is labeled "Fold increase pMAPK1,2" and ranges from 0 to 4. The line graph shows an initial increase in fold increase of pMAPK1,2, peaking around 35 minutes, and then gradually decreasing. : figure::>

<a id='a09bfcca-98d9-4d1d-bae0-cc8bd1a06f37'></a>

C<::MSH then FGF 0 5 10 15 25 35 45 55 65 (Min)Western blot showing three rows of bands.Top row: P-MAPK1,2.Middle row: MAPK1,2.Bottom row: Actin.The lanes correspond to the time points in minutes.Below the Western blot is a line graph.Y-axis: Fold increase pMAPK1,2, with values 0, 1, 2, 3.X-axis: Time (Min), with values 0, 10, 20, 30, 40, 50, 60, 70.A horizontal bar labeled "Stimulus" is present from 0 to approximately 10 minutes on the x-axis.The line shows an initial increase from time 0, peaking around 5-10 minutes, then gradually decreasing and stabilizing at a lower level.: figure::>

<a id='a3b61e5a-3397-4126-8070-4d62ebe33027'></a>

D <::A gel image showing protein expression levels. The image is divided into three rows labeled 'C-Raf', 'B-Raf', and 'Actin' from top to bottom. It has two columns, labeled 'Non-Targeting Control' and 'C-Raf siRNA' from left to right. In the 'C-Raf' row, the 'Non-Targeting Control' lane shows a strong band, while the 'C-Raf siRNA' lane shows a very faint band. In the 'B-Raf' row, both the 'Non-Targeting Control' and 'C-Raf siRNA' lanes show moderately strong bands of similar intensity. In the 'Actin' row, both the 'Non-Targeting Control' and 'C-Raf siRNA' lanes show strong, dark bands of similar intensity, indicating it serves as a loading control.: gel image::>

<!-- PAGE BREAK -->

<a id='905812f6-7e95-47dc-b549-e3fc6689e745'></a>

Figure S4 (supplementary data)

<a id='cbab331a-1eea-4cf6-9aa3-223f91b7858a'></a>

A
ⓟ-MAPK1,2(Thr202/Tyr204)
<table id="8-1">
<tr><td id="8-2">MSH (2µM)</td><td id="8-3">0 min</td><td id="8-4">5 min</td><td id="8-5">10 min</td><td id="8-6">15 min</td><td id="8-7">25 min</td><td id="8-8">45 min</td><td id="8-9">65 min</td></tr>
<tr><td id="8-a"></td><td id="8-b">four light gray dots on a white background</td><td id="8-c">four light gray dots on a white background</td><td id="8-d">four light gray dots on a white background</td><td id="8-e">four light gray dots on a white background</td><td id="8-f">four circular objects</td><td id="8-g">four circular objects</td><td id="8-h">four circular objects</td></tr>
<tr><td id="8-i">FGF (20ng/ml)</td><td id="8-j">0 min</td><td id="8-k">5 min</td><td id="8-l">10 min</td><td id="8-m">15 min</td><td id="8-n">25 min</td><td id="8-o">45 min</td><td id="8-p">65 min</td></tr>
<tr><td id="8-q"></td><td id="8-r">four light gray dots on a white background</td><td id="8-s">four light gray dots on a white background</td><td id="8-t">four light gray dots on a white background</td><td id="8-u">four light gray dots on a white background</td><td id="8-v">four circular objects</td><td id="8-w">four circular objects</td><td id="8-x">four circular objects</td></tr>
<tr><td id="8-y">MSH then FGF</td><td id="8-z">0 min</td><td id="8-A">5 min</td><td id="8-B">10 min</td><td id="8-C">15 min</td><td id="8-D">25 min</td><td id="8-E">45 min</td><td id="8-F">65 min</td></tr>
<tr><td id="8-G"></td><td id="8-H">Four gray circles</td><td id="8-I">Four gray circles</td><td id="8-J">Four gray circles</td><td id="8-K">Four gray circles</td><td id="8-L">Four faint circular marks</td><td id="8-M">Four faint circular marks</td><td id="8-N">Four faint circular marks</td></tr>
</table>

<a id='cbacfdd3-827f-4c50-91a6-07877364291e'></a>

B
MAPK 2
<table id="8-O">
<tr><td id="8-P"></td><td id="8-Q" rowspan="2">MSH (2µM)</td><td id="8-R">0 min</td><td id="8-S">5 min</td><td id="8-T">10 min</td><td id="8-U">15 min</td><td id="8-V">25 min</td><td id="8-W">45 min</td><td id="8-X">65 min</td></tr>
<tr><td id="8-Y"></td><td id="8-Z">gray circles on white background</td><td id="8-10">gray circles on white background</td><td id="8-11">gray circles on white background</td><td id="8-12">four dark circles on light background</td><td id="8-13">four dark circles on light background</td><td id="8-14">four dark circles on light background</td><td id="8-15">four dark circles on light background</td></tr>
<tr><td id="8-16"></td><td id="8-17">FGF (20ng/ml)</td><td id="8-18">0 min</td><td id="8-19">5 min</td><td id="8-1a">10 min</td><td id="8-1b">15 min</td><td id="8-1c">25 min</td><td id="8-1d">45 min</td><td id="8-1e">65 min</td></tr>
<tr><td id="8-1f"></td><td id="8-1g"></td><td id="8-1h">gray circles on white background</td><td id="8-1i">gray circles on white background</td><td id="8-1j">gray circles on white background</td><td id="8-1k">four dark circles on light background</td><td id="8-1l">four dark circles on light background</td><td id="8-1m">four dark circles on light background</td><td id="8-1n">four dark circles on light background</td></tr>
<tr><td id="8-1o"></td><td id="8-1p">MSH then FGF</td><td id="8-1q">0 min</td><td id="8-1r">5 min</td><td id="8-1s">10 min</td><td id="8-1t">15 min</td><td id="8-1u">25 min</td><td id="8-1v">45 min</td><td id="8-1w">65 min</td></tr>
<tr><td id="8-1x"></td><td id="8-1y"></td><td id="8-1z">Image of four circles</td><td id="8-1A">Image of multiple circles</td><td id="8-1B">Image of four circles</td><td id="8-1C">five dark circles on a gray background</td><td id="8-1D">five dark circles on a gray background</td><td id="8-1E">five dark circles on a gray background</td><td id="8-1F">five dark circles on a gray background</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='d2ae6894-248c-4925-a56e-c9160ba6276f'></a>

Figure S5
<::Diagram of a signaling pathway:

**Inputs:**
- (g1) activates a1, leading to FGFR (y1).
- (g2) activates a2, leading to MSH (y2).

**Nodes (Ovals):**
- FGFR (y1)
- MSH (y2)
- C-Raf (y3)
- B-Raf (y4)
- MAPK (y5)

**Nodes (Rectangles):**
- C-Raf (E-y3-y6) inactive
- C-Raf (y6) inactive

**Connections (Arrows):**
- From FGFR (y1):
  - f13 (thick arrow) to C-Raf (y3)
  - f14 (thin arrow) to B-Raf (y4)
- From MSH (y2):
  - f24 (thick arrow) to B-Raf (y4)
- From C-Raf (E-y3-y6) inactive:
  - Thick curved arrow to C-Raf (y3)
- From C-Raf (y3):
  - d3 (output/degradation) with jagged symbol
  - h36 (thin arrow) to C-Raf (y6) inactive
  - f34 (thick arrow) to MAPK (y5)
- From B-Raf (y4):
  - d4 (output/degradation) with jagged symbol
  - f45 (thick arrow) to MAPK (y5)
- From MAPK (y5):
  - d5 (output/degradation) with jagged symbol
  - f53 (thick curved arrow) to C-Raf (y3)
- From C-Raf (y6) inactive:
  - d6 (output/degradation) with jagged symbol

**Outputs (Degradation/Removal):**
- d1 from FGFR (y1) with jagged symbol
- d2 from MSH (y2) with jagged symbol
- d3 from C-Raf (y3) with jagged symbol
- d4 from B-Raf (y4) with jagged symbol
- d5 from MAPK (y5) with jagged symbol
- d6 from C-Raf (y6) inactive with jagged symbol::>


<!-- PAGE BREAK -->

<a id='9f5c4869-efcc-4c6b-8070-5a5003d98bc1'></a>

Table S2 (supplementary data)

<a id='b4fb1b52-3554-4d52-9fff-4439aa6d068c'></a>

d(y1) / dt = a1(g1/(b1 + g1)) - d1(y1)

d(y2) / dt = a2(g2/(b2 + g2)) - d2(y2)

d(y3) / dt = f13[E - y3 - y6][y1] + f53[E - y3 - y6][y5] - h36[y2][y3] - d3[y3]

d(y4) / dt = f14[y1] + f24[y2] - d4[y4]

d(y5) / dt = f35[y3] + f45[y4] - d5[y5]

d(y6) / dt = h36[y2][y3] - d6[y6]

<a id='eb294f11-547c-47d2-996d-39b21dda9ce2'></a>

The base parameter values for the above are as follows:
E=10, a1= 10, a2= 10, b1= 10, b2= 10, f13=0.6, f53= 1.5, f14= 0.1,
f24=0.8, f35=0.3, f45=0.1, h36= 0.1, d1=0.2, d2=0.1, d3=1.0, d4=
1.1, d5= 1.0, d6= 0.001.

<a id='a57b4f2b-b08b-4448-8e8e-10aa3621da37'></a>

Experiment 1: A stimulus of MSH given from time 0-5 minutes.
Simulation: g2=1.0 from t=0 to t=5 minutes; g2=0 for t > 5. Figure 2C
Experiment 2: A stimulus of FGF given from time 0-5 minutes.
Simulation: g1=1.0 from t=0 to t=5 minutes; g1=0 for t > 5. Figure 2D

<a id='f3629b36-9a47-4799-ad1e-fd37c8cc8794'></a>

Experiment 3: A stimulus of MSH given from time 0-5 minutes and
then a stimulus of FGF from time 5-10 minutes.
Simulation: g2=1.0 from t=0 to t=5 minutes; g2=0 for t > 5, and g1=0
from t=0 to t=5; g1=1.0 from t=5 to t=10; and g1=0 for t > 10. See
Figure 4B