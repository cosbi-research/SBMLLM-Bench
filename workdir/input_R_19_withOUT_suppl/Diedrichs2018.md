<a id='43d01924-2eaa-43ef-9a45-ecd13771e40e'></a>

MBoC | ARTICLE

<a id='98973588-6fa0-4fb6-82b2-9d1f2a217e79'></a>

A data-entrained computational model for
testing the regulatory logic of the vertebrate
unfolded protein response

<a id='deb3e8d9-58ee-4856-b2ea-482dbc0df4f6'></a>

Danilo R. Diedrichsⁱ,†,‡, Javier A. Gomez⁳,†, Chun-Sing Huang⁳, D. Thomas Rutkowski⁳,⁴,*, and Rodica Curtuⁱ,*
ⁱDepartment of Mathematics, College of Liberal Arts and Sciences, and ⁳Department of Anatomy and Cell Biology, and ⁴Department of Internal Medicine, Carver College of Medicine, University of Iowa, Iowa City, IA 52242

<a id='f253b14f-43ca-4e00-b487-0ccfefcc3e01'></a>

**ABSTRACT** The vertebrate unfolded protein response (UPR) is characterized by multiple interacting nodes among its three pathways, yet the logic underlying this regulatory complexity is unclear. To begin to address this issue, we created a computational model of the vertebrate UPR that was entrained upon and then validated against experimental data. As part of this validation, the model successfully predicted the phenotypes of cells with lesions in UPR signaling, including a surprising and previously unreported differential role for the elF2a phosphatase GADD34 in exacerbating severe stress but ameliorating mild stress. We then used the model to test the functional importance of a feedforward circuit within the PERK/ CHOP axis and of cross-regulatory control of BiP and CHOP expression. We found that the wiring structure of the UPR appears to balance the ability of the response to remain sensitive to endoplasmic reticulum stress and to be deactivated rapidly by improved protein-folding conditions. This model should serve as a valuable resource for further exploring the regulatory logic of the UPR.

<a id='dfd436bb-f732-49c3-9f82-5bb0358ae679'></a>

Monitoring Editor
Reid Gilmore
University of Massachusetts

<a id='3189a417-68c6-4184-917c-c296d80d3fe3'></a>

Received: Sep 26, 2017

Revised: Mar 27, 2018

Accepted: Apr 9, 2018

<a id='c552d79b-5e5d-46b3-9128-f3dd5ff3592a'></a>

INTRODUCTION
The vertebrate unfolded protein response (UPR) is a complex signal-
transduction pathway with multiple points of overlap and feedback
(both positive and negative) and feedforward loops. At least three

<a id='2089f34a-0a69-430d-9e62-01875f56e298'></a>

This article was published online ahead of print in MBoC in Press (http://www .molbiolcell.org/cgi/doi/10.1091/mbc.E17-09-0565) on April 18, 2018.
†These authors contributed equally to this work.

<a id='c0f9e54c-372d-4edb-90e3-04ea5d83832e'></a>

*Present address: Department of Mathematics and Computer Science, Wheaton College, Wheaton, IL 60187.

<a id='3b2be363-b314-4267-85a5-e44dd6acd177'></a>

Author contributions: D.T.R. and R.C. conceived and designed the study; D.R.D. and R.C. were responsible for creation, parameterization, and refinement of the model; J.A.G., C.-S.H., and D.T. generated experimental data; J.A.G. and R.C. performed in silico experiments; D.R.D., J.A.G., D.T.R., and R.C. wrote the manuscript. All authors read and approved the manuscript.
*Address correspondence to: Thomas Rutkowski (Thomas-rutkowski@uiowa.edu); Rodica Curtu (Rodica-curtu@uiowa.edu).

<a id='973ad4f3-7090-46c6-80cf-c70419971060'></a>

Abbreviations used: ATF, activating transcription factor; CHOP, C/EBP homolo-gous protein; eIF, eukaryotic initiation factor; ER, endoplasmic reticulum; GADD, growth arrest and DNA damage inducible; IRE, inositol-requiring enzyme; MEF, mouse embryonic fibroblast; ODE, ordinary differential equation; qRT-PCR, quan-titative reverse transcription PCR; RIDD, regulated IRE1-dependent decay; S1/2P, site 1/2 protease; TG, thapsigargin; UPR, unfolded protein response; XBP, X-box binding protein.

<a id='63bb3c4b-1170-4c08-adaa-a2cc7811f5bd'></a>

© 2018 Diedrichs, Gomez, et al. This article is distributed by The American Society for Cell Biology under license from the author(s). Two months after publication it is available to the public under an Attribution–Noncommercial–Share Alike 3.0 Unported Creative Commons License (http://creativecommons.org/licenses/by-nc-sa/3.0).

<a id='7dfbe193-c975-4a2e-a37c-8592f4e6590e'></a>

"ASCB®," "The American Society for Cell Biology®," and "Molecular Biology of the Cell®" are registered trademarks of The American Society for Cell Biology.

<a id='4ae921f4-90a6-455c-8ee8-776f8802a6d0'></a>

pathways constitute the UPR, initiated by IRE1 (the ubiquitous α and tissue-specific β paralogues), PERK, and the partially redundant ATF6 α and β pathways (Parmar and Schröder, 2012). Although IRE1 mediates degradation of endoplasmic reticulum (ER)-associated mRNAs (known as regulated IRE1-dependent decay, or RIDD) (Hollien and Weissman, 2006; Hollien et al., 2009) and PERK effects translational arrest (Harding et al., 1999), each UPR pathway also culminates in transcriptional control. IRE1 does so through splicing of Xbp1 mRNA, PERK through eIF2α-dependent translation of the transcription factor ATF4, and ATF6 through S1P/S2P-dependent cleavage, which liberates an active transcription factor (Walter and Ron, 2011). The genes up-regulated by the UPR include most notably the gene encoding BiP (heavy-chain binding protein), which is one of the most abundant ER proteins and plays a central role in ER protein translocation and folding and ER-associated degradation (Gething, 1999; Nishikawa et al., 2005). While in principle each pathway might regulate a distinct set of downstream genes, in reality there is considerable overlap among the targets regulated by each; the PERK pathway, in particular, appears to regulate a broad swath of target genes, including those also regulated by ATF6 and IRE1 (Harding et al., 2003; Teske et al., 2011).

<a id='d5ba4c63-dc88-4115-86e9-d97f9259b709'></a>

One essential function of the vertebrate UPR is the need to bal-ance the ability of cells to adapt to ER stress with the imperative to commit to apoptosis if the stress is too severe (Tabas and Ron, 2011;

<a id='6af3a3c7-9e58-48d0-b7cc-bcd941da5dc4'></a>

1502

<a id='2243fbb4-5382-4924-8bb2-a0342d1e26b9'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='e906e173-6a78-45b2-9ccf-8038e04f75b6'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='c3525df5-98b0-4dbe-bd25-d5c110710ca5'></a>

Hetz, 2012). Adaptive and apoptotic signaling could in principle be under the control of different pathways. Yet none of the vertebrate UPR pathways is intrinsically apoptotic: each initiates both survival and cell death programs, and selective activation of only a subset of UPR pathways is not strictly required for cells to escape death and adapt to persistent stress (Rutkowski et al., 2006). One example of this paradox is expression of the transcription factor C/EBP homolo- gous protein (CHOP). CHOP is strongly associated with ER stress-in- duced cell death. Several mechanisms have been proposed to ac- count for CHOP-induced cell death (Marciniak et al., 2004; Puthalakath et al., 2007; Li et al., 2009), and so its exact role in the process is still uncertain. However, CHOP is of clear functional im- portance in that cells or animals lacking CHOP are protected from a wide variety of genetic, pharmacological, or biological insults that elicit ER stress (Zinszner et al., 1998; Oyadomari et al., 2002; Pennuto et al., 2008; Song et al., 2008; Namba et al., 2009; Thorp et al., 2009; Gao et al., 2011). Yet CHOP expression alone is insufficient to commit cells to death, as even stresses that cells can survive without appreciable cell death elicit transient up-regulation of CHOP (Rutkowski et al., 2006). In fact, one indicator that cells will not sur- vive ER stress is persistent, rather than transient, expression of CHOP (Rutkowski et al., 2006). Thus, a key requirement for under- standing how cells live or die during ER stress is to determine how their expression of death-promoting factors such as CHOP is con- trolled directly by transcriptional regulation, and also indirectly by the expression of proteins such as BiP that alleviate ER stress and deactivate the UPR.

<a id='3f1085a7-b20d-4ba6-bb3c-22831681ebf2'></a>

While important in adaptation and apoptosis, respectively, BiP and CHOP are also exemplars of the regulatory complexity of the vertebrate UPR. BiP mRNA expression is directly regulated by ATF6 (Yoshida et al., 2000; Wu et al., 2007; Yamamoto et al., 2007), and yet its induction during stress depends partly on PERK activity as well (Luo et al., 2003; Wu et al., 2007; Teske et al., 2011; Han et al., 2013). Conversely, CHOP transcription is strongly regulated by PERK activation (Harding et al., 2000a, 2003), but ATF6 also directly contributes to its expression (Ma et al., 2002; Wu et al., 2007). The purpose of this overlap is unclear, as are its consequences for cell survival versus cell death. However, this and many other related questions about why the UPR is structured the way it is are challenging to test experimentally.

<a id='dda8033a-a9d8-48f1-9584-b4925eb66963'></a>

We reasoned that a computational model that allowed disrup-
tive alterations to be tested in silico could overcome this problem
and illuminate the regulatory logic of the vertebrate UPR. The key
elements in the UPR survival-versus-death axes appear to strongly
depend on timing—it is persistent stress that sustains expression of
CHOP and that elicits cell death. For this purpose, then, an ordinary
differential equation (ODE) model holds the most promise, as it is
appropriate when the components of a pathway are known but the
temporal relationships among them must be investigated (Kim
et al., 2009). There have been several attempts to build ODE mod-
els of the UPR either in part or in full, each with its own strengths and
limitations. The first rudimentary attempt modeled production and
degradation of BiP and CHOP in order to test whether the discrep-
ant degradation kinetics of these two components was sufficient to
account for the phenotype seen in stress-adapted cells, where only
stable BiP expression is observed (Rutkowski et al., 2006). This ap-
proach left entirely open the question of how the upstream stress-
sensing molecules (IRE1, PERK, and ATF6) influence response out-
put. Later, a model examining the interplay between chaperone
synthesis and translational attenuation in alleviating stress illustrated
how translational attenuation protects better against distinct types
of stresses (Trusina et al., 2008; Trusina and Tang, 2010). We then

<a id='f0c6a923-b518-4c43-803a-7eaea6874b18'></a>

described a more complete ODE model of the UPR, accounting for both its activation and output (Curtu and Diedrichs, 2010). This model provided a framework of the UPR signaling network but was not parameterized. A more recent fully parameterized complete ODE model of the UPR described cell death versus adaptation as an emergent property of the response, but this model was not entrained on experimental data and was sparingly validated (Erguler et al., 2013).

<a id='864e8e60-40da-43a3-90f8-1688ffe7ed9c'></a>

Our ultimate goal is to develop a computational model of the UPR that is biologically trustworthy, predicative, and explanatory. Toward that end, and starting from our existing framework (Curtu and Diedrichs, 2010), we strove to parameterize a UPR model that not only was entrained on experimental data, but also could be validated against genetically modified mouse embryonic fibroblasts (MEFs)—and that could then be used to query the regulatory logic of the response.

<a id='f797391f-cd14-482d-b7c5-04f12f27eec5'></a>

## RESULTS
### Describing the contributions of each UPR pathway to its output
To entrain, parameterize, and refine our initial ODE model of the UPR, we examined the behavior of MEFs treated with the ER calcium-depleting agent thapsigargin (TG). TG was chosen because it is robust, activates all three UPR pathways even at low doses (Rutkowski et al., 2006), and does not depend on protein synthesis to elicit ER stress as does the other oft-used ER stressor tunicamycin. MEFs are a useful model cell type because they can be isolated even from knockouts that lead to prenatal lethality.

<a id='c6320690-e415-4297-bc17-8b38659ccb48'></a>

We first examined the response of MEFs lacking each of the three UPR stress sensors—PERK (Harding et al., 2000b), ATF6α (Wu et al., 2007), and IRE1α (Zhang et al., 2011)—to varying doses of TG from 2.5 to 100 nM for 8 h in order to confirm the regulatory interactions among these sensors and the UPR targets BiP and CHOP. In this cell type, 2.5 nM TG is the lowest dose still capable of eliciting ER stress but allowing cells to adapt, 10 nM is the lowest dose that precludes net cell survival, and doses over 10 nM are superphysiological (Rutkowski et al., 2006). As expected, CHOP protein up-regulation was essentially completely lost in Perk-/- MEFs, due to the effects of both ATF4 on Chop transcription and eIF2α phosphorylation on CHOP translation (Palam et al., 2011; Figure 1, A and B). In addition, while there appeared to be little effect of Perk deletion on up-regulation of BiP protein, at least at this time point (Figure 1A), it had a modest but significant effect on up-regulation of Bip mRNA, as shown previously (Wu et al., 2007; Figure 1B). Also consistent with previous findings (Wu et al., 2007; Yamamoto et al., 2007), deletion of Atf6α diminished (but did not eliminate) up-regulation of both BiP and CHOP (Figure 1, C and D). In contrast, the response of cells lacking IRE1α was more complex. BiP up-regulation at the protein level was, if anything, enhanced in Ire1α-/- cells, and Bip mRNA expression was not significantly different (Figure 1, E and F). CHOP up-regulation was compromised at low doses of stress but not at high doses (Figure 1, E and F). These results are consistent with the idea that IRE1 signaling contributes only indirectly to the up-regulation of either of these genes (Lee et al., 2003) and with the absence of XBP1 binding sites (unfolded protein response elements, or UPREs) in both gene promoters.

<a id='bdab0527-c867-4ca9-98a0-50cd71db0f2f'></a>

Modification of the UPR wiring diagram
One feature of the experimental system used here that is appar-
ent from these results is that UPR signaling can vary somewhat in

<a id='5ab5c4aa-c7e3-4f9a-8011-bb6b0ece92c5'></a>

Volume 29 June 15, 2018

<a id='c6a07cb9-07b0-4471-8f58-e47433bd7348'></a>

ODE model of UPR regulatory logic

<a id='64cb761c-5d11-405b-9eba-1e2bfd073fb0'></a>

1503

<!-- PAGE BREAK -->

<a id='af97bf58-7417-4255-a22f-9312ee8a4e4b'></a>

<::FIGURE 1: Contributions of PERK, ATF6α, and IRE1α to UPR output in MEFs. MEFs of the indicated genotype were treated with increasing concentrations of TG ranging from 2.5 to 100 nM, or with vehicle as a control. Cells were harvested for analysis by either immunoblot (A, C, E) or qRT-PCR (B, D, F). Statistical significance was calculated by two-way analysis of variance (ANOVA) for concentration and genotype; the p-value for genotype is shown (ANOVA for concentration was highly significant in all cases). Individual data points (three biological replicates) for qRT-PCR are shown as open circles, along with means ± SDM from those replicates. The loading control for immunoblots was calnexin, the expression of which is not regulated by ER stress in MEFs. Note that the apparent enhanced up-regulation of Bip and Chop mRNA at low TG concentrations in Atf6α+/+ cells is a somewhat atypical result relative to other wild-type MEF lines.
: chart::>

A. Immunoblot showing protein levels of BiP, CHOP, and loading control in Perk+/+ and Perk-/- MEFs treated with increasing concentrations of TG (from left to right: vehicle, 2.5, 5, 10, 50, 100 nM). B. Bar charts displaying relative mRNA expression. Top chart: Bip mRNA expression in Perk+/+ (dark grey bars) and Perk-/- (light grey bars) MEFs, showing p=0.0036 for genotype. Bottom chart: Chop mRNA expression in Perk+/+ (dark grey bars) and Perk-/- (light grey bars) MEFs, showing p=10^-8 for genotype. X-axis for both charts: NT, 2.5, 5, 10, 50, 100 nM TG. Y-axis: relative mRNA expression.

C. Immunoblot showing protein levels of BiP, CHOP, and loading control in Atf6α+/+ and Atf6α-/- MEFs treated with increasing concentrations of TG (from left to right: vehicle, 2.5, 5, 10, 50, 100 nM). D. Bar charts displaying relative mRNA expression. Top chart: Bip mRNA expression in Atf6α+/+ (dark grey bars) and Atf6α-/- (light grey bars) MEFs, showing p=10^-14 for genotype. Bottom chart: Chop mRNA expression in Atf6α+/+ (dark grey bars) and Atf6α-/- (light grey bars) MEFs, showing p=10^-12 for genotype. X-axis for both charts: NT, 2.5, 5, 10, 50, 100 nM TG. Y-axis: relative mRNA expression.

E. Immunoblot showing protein levels of BiP, CHOP, and loading control in Ire1α+/+ and Ire1α-/- MEFs treated with increasing concentrations of TG (from left to right: vehicle, 2.5, 5, 10, 50, 100 nM). F. Bar charts displaying relative mRNA expression. Top chart: Bip mRNA expression in Ire1α+/+ (dark grey bars) and Ire1α-/- (light grey bars) MEFs, showing N.S. for genotype. Bottom chart: Chop mRNA expression in Ire1α+/+ (dark grey bars) and Ire1α-/- (light grey bars) MEFs, showing p=10^-5 for genotype. X-axis for both charts: NT, 2.5, 5, 10, 50, 100 nM TG. Y-axis: relative mRNA expression.

<a id='65856b34-4d2b-4226-b319-03d4c152b127'></a>

magnitude and duration from experiment to experiment, even under carefully standardized conditions. This is apparent even from the data in Figure 1, where different wild-type cells from highly backcrossed (>10 generations) animals—effectively iso-genic cell lines—up-regulate Bip and Chop mRNA to different extents. The intensity of the response is subject to a number of influences, including cell passage number, degree of confluence, nutrient level, batch of stressor, cellular epigenetic status, and the individual conditions under which each line was isolated from its corresponding embryo, which are controllable to greater or lesser degrees. Thus, a useful computational model must be entrained on experimental data yet not overfit; rather than recapitulating the precise magnitude of any event, it must cap-ture the trends that are consistent from one experiment to another.

<a id='6fda6418-3cec-4acc-b176-57b86b9aff2a'></a>

We set about building an ODE model of the UPR based on the framework of our existing base model, which incorporated all three limbs of the UPR (Curtu and Diedrichs, 2010). A schematic diagram showing the components of this model and their interactions with each other is shown in Figure 2A, with the corresponding wiring diagram in Figure 2B. To avoid overspecification, we chose to model only relationships within the core framework of UPR signaling. These are as follows:

<a id='f384bc20-7ecd-4780-98db-40eb62b39144'></a>

1. Unfolded proteins are generated by an input stress, which causes
those proteins to associate with BiP.

<a id='cf58c251-9741-4077-ab29-4f2a01b82d55'></a>

2. Unfolded protein accumulation leads to activation of PERK and IRE1 by phosphorylation and activation of ATF6 by cleavage (Harding et al., 1999; Haze et al., 1999).
3. Activated IRE1 induces production of XBP1, the product of the spliced form of Xbp1 mRNA (Xbp1s) (Shen et al., 2001; Yoshida et al., 2001; Calfon et al., 2002; Lee et al., 2002). Even though XBP1 does not directly up-regulate Bip mRNA, we modeled that relationship as a proxy for its general effect in improving protein folding through its action on other UPR target genes that are not part of the model. Activated IRE1 also activates a RIDD function (Hollien and Weissman, 2006; Hollien et al., 2009). We modeled this effect as a diminution in the rate constants for unfolded proteins being synthesized and associating with BiP. We also modeled activated IRE1 as contributing to degradation of Bip mRNA via its RIDD function, as has been suggested by us (Gomez and Rutkowski, 2016) and others (Han et al., 2009). Notably, because IRE1 has only modest effects in this system (Figure 1), the contribution of each of these pathways to overall model output is small.
4. Activated PERK phosphorylates eIF2α (Harding et al., 1999), which inhibits global protein synthesis (Wong et al., 1993) to alleviate ER stress (Harding et al., 2000b) and stimulates translation of Atf4 mRNA (Harding et al., 2000a).
5. ATF4 transcriptionally regulates CHOP (Harding et al., 2000a), which, along with ATF4, transcriptionally regulates GADD34 (Novoa et al., 2001; Ma and Hendershot, 2003).

<a id='adc5b4cf-0184-41c6-9b8a-6eefa85c13cd'></a>

1504

<a id='d82a84ff-d8f9-4805-8fa1-4ded2d60c5d4'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='f6b73cac-bca7-4301-9478-0f6789fa42cd'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='4d4292b8-75ea-4dd1-94bc-b15823f7d2d5'></a>

A<::Biological pathway diagram showing the unfolded protein response (UPR) during ER stress.: flowchart::>ER stress, represented by a burst icon on the ER membrane, leads to the activation of three major pathways: PERK, ATF6, and IRE1. The diagram also shows regulatory feedback loops involving BiP and GADD34.

**1. PERK Pathway:**
- ER stress (blue dashed arrow) activates PERK (phosphorylated, PERK-P).
- PERK-P activates eIF2α (phosphorylated, eIF2α-P) (blue solid arrow).
- eIF2α-P activates ATF4 (blue dashed arrow).
- ATF4 activates CHOP (blue solid arrow).
- CHOP activates GADD34 (blue solid arrow).
- GADD34 inhibits eIF2α-P (red dashed line).
- BiP inhibits PERK (red solid line).

**2. ATF6 Pathway:**
- ER stress (blue dashed arrow) activates ATF6.
- Activated ATF6 (ATF6cl, cleaved) moves to the cytoplasm/nucleus (indicated by the large blue oval) and activates BiP (blue solid arrow).
- BiP inhibits ATF6 (red solid line).

**3. IRE1 Pathway:**
- ER stress (blue dashed arrow) activates IRE1 (phosphorylated, IRE1-P).
- IRE1-P processes Xbp1-s mRNA, leading to its translation into a protein (Xbp1-s) that moves to the cytoplasm/nucleus.
- Xbp1-s activates BiP (blue solid arrow).
- IRE1-P also undergoes RIDD (Regulated IRE1-dependent decay) (indicated by (RIDD) with a red solid line from IRE1-P to IRE1-P, possibly indicating self-regulation or degradation).
- BiP inhibits IRE1 (red solid line).

**General Regulatory Elements:**
- Red lines with a bar indicate inhibition.
- Blue solid arrows indicate activation.
- Blue dashed arrows indicate activation (possibly indirect or weaker).
- Dashed red lines with a bar indicate inhibition (possibly indirect or weaker).
- The ER stress icon also has red lines with bars pointing to PERK, ATF6, and IRE1, implying that these sensors are normally kept inactive, and ER stress relieves this inhibition (e.g., by dissociating BiP). However, direct activation by ER stress is also shown with blue dashed arrows.
- BiP is activated by ATF6 and Xbp1-s.
- BiP provides negative feedback, inhibiting PERK, ATF6, and IRE1.
- ATF4 activates BiP (blue dashed arrow).
- CHOP activates BiP (blue dashed arrow).

<a id='a70181d4-58a9-4e1e-8ea4-598c1cb284ef'></a>

B<::Diagram: A biological pathway diagram illustrating the unfolded protein response (UPR) and its downstream effects. The diagram shows various proteins and their interactions, including activation (arrows), inhibition (blunt arrows), and conversions, with some rate constants indicated (e.g., kd.b, kd.B). The main components are:<br>Processes/States:<br>- Stress (S) leads to U (Unfolded proteins).<br>- U (Unfolded proteins) can lead to BiP and then Folded Proteins.<br>- Translation Repression (eIF2α-P) is influenced by eIF2α-P.<br>- RIDD (Regulated IRE1-Dependent Decay) is associated with U and IRE1-P.<br><br>Proteins/Genes (Rectangular boxes are proteins, ovals are genes/transcripts, green boxes are activated/phosphorylated forms):<br>- U (Unfolded proteins): A pink box, central to the stress response.<br>- BiP: A pink box.<br>- ATF6 (cleaved): A pink box.<br>- IRE1-P: A green box, activated form of IRE1.<br>- PERK-P: A green box, activated form of PERK.<br>- eIF2α: A pink box.<br>- eIF2α-P: A pink box, phosphorylated eIF2α.<br>- ATF4: A pink box.<br>- CHOP: A pink box.<br>- GADD34: A pink box.<br>- XBP1: A faded pink box.<br><br>Genes/Transcripts (Yellow ovals):<br>- bip<br>- sp-xbpl<br>- chop<br>- gadd34<br><br>Interactions:<br>- Stress (S) activates U (Unfolded proteins).<br>- U inhibits BiP.<br>- U interacts with IRE1-P and PERK-P.<br>- BiP, along with U, influences ATF6 (cleaved), IRE1-P, and PERK-P.<br>- ATF6 (cleaved) leads to bip (gene) and chop (gene), and is associated with ATF4, ATF6.<br>- IRE1-P leads to sp-xbpl (gene).<br>- sp-xbpl inhibits XBP1.<br>- PERK-P phosphorylates eIF2α to eIF2α-P.<br>- eIF2α-P is dephosphorylated by GADD34 back to eIF2α.<br>- eIF2α-P activates ATF4.<br>- ATF4, along with ATF6, influences bip and chop.<br>- ATF4 activates gadd34 (gene).<br>- CHOP activates gadd34 (gene).<br>- bip (gene) converts to BiP (protein) with rate kd.b.<br>- chop (gene) converts to CHOP (protein) with rate kd.c.<br>- gadd34 (gene) converts to GADD34 (protein) with rate kd.g.<br><br>Rate constants shown on arrows:<br>- kd.b (bip to BiP)<br>- kd.B (from BiP)<br>- kd.A6 (from ATF6 (cleaved))<br>- kd.x (from sp-xbpl)<br>- kd.c (chop to CHOP, and from CHOP)<br>- kd.g (gadd34 to GADD34)<br>- kd.G (from GADD34)<br>- kd.A4 (from ATF4)::>

<a id='af7a805b-e50e-4c72-9f9c-87ad6a975199'></a>

FIGURE 2: Modeled relationships among UPR components. (A) Schematic showing the relationships among UPR components accounted for by the model, with blue lines indicating stimulatory interactions and red lines inhibitory ones. Dashed lines denote relationships examined by in silico manipulation. (B) Wiring diagram depicting the same relationships shown in A, along with the relevant rate constants. The model simulates the concentration level for four specific mRNA (ellipse; yellow) and seven specific protein (rectangle; red) species (see Table 1, Eqs. 4-14). It also shows unfolded proteins. It defines PERK and IRE1 phosphorylation (rectangle; green) and free BiP (not shown in the wiring diagram) as functions of the unfolded proteins and total BiP (Table 1, Eqs. 1-3). For simplification purposes, Bip mRNA is here responsive to Xbp1 mRNA, used as a proxy for XBP1 protein, which is not explicitly modeled.

<a id='ddde799c-16d9-49ca-b088-0c591eab1879'></a>

6. Phosphorylated eIF2\u03b1 also translationally regulates both CHOP and GADD34 (Lee et al., 2009; Palam et al., 2011).
7. Cleaved ATF6 transcriptionally regulates both Bip and Chop (Haze et al., 1999; Ma et al., 2002).
8. ATF4 transcriptionally regulates BiP (Luo et al., 2003; Han et al., 2013).

<a id='75fc5b4e-f3a8-4c32-a119-3466bbb00ecd'></a>

9. BiP alleviates ER stress (by improving protein folding; Kassenbrock et al., 1988; Morris et al., 1997) and also directly suppresses acti- vation of PERK and ATF6 (Bertolotti et al., 2000; Shen et al., 2002).
The list of equations is given in Table 1, and the definitions of each component and interaction are in Table 2. The model as con- structed rests on the following simplifying assumptions:

<a id='2ae290db-ca07-4e0e-b871-19fc09ad6c97'></a>

Volume 29 June 15, 2018

<a id='6c5f5563-f834-427c-afc8-fb63febddea9'></a>

ODE model of UPR regulatory logic

<a id='69445e57-d2ed-4eef-a17d-5f310f357c60'></a>

1505

<!-- PAGE BREAK -->

<a id='004e14ba-09d2-4347-a7b2-8c1ee8fcb120'></a>

B = \frac{B_{tot}}{1 + \frac{U}{K_{BU}}} (1)

P_p = \frac{1}{f} \frac{U}{K_{UP} + \frac{K_{UP}}{K_{BP}} B + U} (2)

I_p = \frac{1}{f_i} \frac{U}{K_{UI} + \frac{K_{UI}}{K_{BI}} B + U} (3)

\frac{dU}{dt} = \frac{k_{s,U}}{1 + K_{UI}(I_p - I_p^*)} + S(t) - \delta \frac{U}{1 + K_{II}(I_p - I_p^*)} B \frac{1}{1 + \frac{E_p}{K_E} + \left(\frac{U}{K_{UU}}\right)^4} (4)

\frac{dE_p}{dt} = \frac{k_{ph} P_p (E_{tot} - E_p)}{K_{ph} + (E_{tot} - E_p)} - \frac{(k_{deph1} + k_{deph2}(G - G^*)) E_p}{K_{deph} + E_p} (5)

\frac{dx}{dt} = \frac{k_{sp} I_p (x_{tot} - x)}{K_X + (x_{tot} - x)} - k_{d,x} x (6)

\frac{dA6}{dt} = k_{cl}(U - U^*) \frac{A6_{tot} - A6}{1 + \frac{B}{K_{BA6}}} - k_{d,A6}(A6 - A6^*) (7)

\frac{dA4}{dt} = \gamma(U - U^*) E_p - k_{d,A4}(A4 - A4^*) (8)

\frac{db}{dt} = \alpha_{A6}(1 + K_{b6} A4) \frac{(A6 - A6^*)^2}{(A6 - A6^*)^2 + K_{A6}^2(1 + K_{th6} A4^n)} + \alpha_{A4}(1 + K_{b4} A6) \frac{(A4 - A4^*)^2}{(A4 - A4^*)^2 + [K_{A4}(1 + K_{th4} A6)]^2} + \alpha_X \frac{x - x^*}{K_{Xb} + (x - x^*)} - k_{d,b} \frac{1 + \alpha_I (I_p - I_p^*)}{1 + \beta_I (I_p - I_p^*)} (b - b^*) (9)

<a id='7cb0cef6-0584-4ea1-a143-9af074ad543f'></a>

dBtot / dt = kt,B b - kd,B Btot

<a id='f3694451-1de1-4e13-8c9e-ce3a38f352d9'></a>

dc/dt = μA4(1 + Kc4 A6) * (A4 - A4*)^2 / [(A4 - A4*)^2 + [KA4c (1 + Kth4c A6)]^2] (11)

<a id='93c05552-2711-4749-a3eb-265043f0340c'></a>

-k_{d,c}(c-c^*)

<a id='2b10b4f7-2565-476a-be67-25703fada222'></a>

dC/dt = [k_{t0,c} + k_{t,c}(E_p - E_p^*)]c - k_{d,c}C (12)

<a id='af7f1224-53d4-49a0-8fad-d4b8c7e80411'></a>

dg/dt = ηC ( (A4 - A4*) + KA4g(A4 - A4*)(C - C*) ) / ( (A4 - A*) + Kth4g(A4 - A4*)(C - C*) + KC ) (13)

<a id='e5366d1d-bbe4-44e6-81c0-dabb220f6c7d'></a>

-k_d,g(g-g*)

dG/dt = [k_t0,G + k_t,G(E_p - E_p*)]g - k_d,GG (14)

<a id='9cadde7e-d667-4b61-9370-c76c1e641cb4'></a>

TABLE 1: Model equations.

<a id='49549512-f0b9-493c-a66a-f8c06a7038d6'></a>

1. Separate differential equations are provided for both mRNA and protein species of BiP, CHOP, and GADD34. As the regulation of ATF4 is predominantly (though not exclusively) translational (Scheuner et al., 2001; Lu et al., 2004; Dey et al., 2010), its transcription is not considered. UPR activation alters mRNA expression of several species in this model (_Atf4_, _Atf6_, and _Perk_) on the order of twofold (unpublished data), and these effects were not

<a id='a21496f6-ad01-46d0-9915-936542a73f69'></a>

considered here because of their relatively small magnitude,
although further model refinement should include them.

<a id='13cddc05-de0c-4c96-af52-62d68f274de8'></a>

2. The total amounts of PERK (phosphorylated and unphosphorylated), IRE1 (phosphorylated and unphosphorylated), eIF2̕ (phosphorylated and unphosphorylated), and ATF6 (cleaved and uncleaved) are held constant.
3. XBP1 protein is presumed to be directly proportional to its spliced mRNA (Xbp1s), and thus the protein is not explicitly modeled. There is evidence that XBP1 protein produced from unspliced Xbp1 mRNA can interfere with XBP1 protein produced from spliced Xbp1 mRNA (Yoshida et al., 2006), but given the relatively minor contribution of the entire IRE1/XBP1 pathway to this particular system, this species is not included.
4. BiP is known to bind to PERK, IRE1, and ATF6, but BiP is much more abundant than these sensors (Ron and Walter, 2007); thus the total BiP concentration is approximated as the sum of free BiP and BiP in complex with unfolded proteins ([BiPtot] = [BiP] + [BU]).
5. BiP is taken as a proxy for transcriptionally up-regulated proteins that augment the ER protein folding capacity. In reality, there are dozens of such proteins, many of which, like BiP, are transcriptionally regulated by both the ATF6 and PERK axes (Wu et al., 2007; Teske et al., 2011), but there is little doubt that, as the most abundant chaperone in the ER lumen and the one with the widest substrate binding specificity, up-regulation of BiP is central to adaptation to stress.
6. The folding process can be modeled by the following reactions: BiP + U → BU → BiP + F.

<a id='84c2298a-3e64-4ca5-a909-29efbb78efd1'></a>

A free chaperone BiP associates with an unfolded protein U, converting it to a folded protein F, which releases the chaperone. Because these two reactions happen fast (within a few minutes) compared with the time scale of the other reactions of interest in the UPR (several hours), we made a quasi-steady-state assumption for BU. Using a mass-action law to model the kinetics of these reactions and setting

d[BU]
---
 dt
= 0

<a id='5a80e9c8-b47c-4834-9186-b9033a964e1e'></a>

we determined that

[BU] = [BiP] · [U]
---
K_BU

<a id='9194527a-442e-489b-b0b1-cedb33a908e7'></a>

where KBU is a positive constant. Equation 1 of the model (Table 1) is then obtained by incorporating this result into the equation for total BiP (see above).

<a id='126439c4-6b16-4a92-bf50-c7c998b47cd7'></a>

7. Under unstressed conditions, PERK exists in a complex with BiP (here called "BP"). An increase in unfolded proteins (induced by stress) causes the BiP—PERK complexes to dissociate. PERK is then free to come into contact with the unfolded proteins and multi- merize (Gardner et al., 2013), promoting its autophosphorylation and activating its downstream signaling function. Therefore, we assume that PERK is phosphorylated when it is associated with lumenal unfolded proteins ([PERK-P] = [UP], where "UP" repre- sents these PERK-unfolded protein complexes). The dissociation of PERK from BiP and its subsequent association with unfolded proteins are fast reactions (a few minutes) compared with the time scales of interest in the UPR (several hours). Therefore, we made a quasi-steady-state assumption for the following reactions:

<a id='3311c6ec-0773-41a6-b3f6-f52a0b0d0b1b'></a>

<::BP ↔ BiP + PERK
U + PERK ↔ UP
: figure::>

<a id='e6cd3812-8b44-42fb-bdb9-46afa201658b'></a>

1506

<a id='7aad93e9-c694-4c0e-b219-55def8ad42a5'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='c91982aa-0309-4612-9d5f-993276177d55'></a>

Molecular Biology of the Cell

<a id='0bb847c4-95b2-45d2-86e1-6a90ca72d8f9'></a>

(10)

<!-- PAGE BREAK -->

<a id='c1a2cdaf-4748-4fb8-a67a-27f9ae438206'></a>

<table id="5-1">
<tr><td id="5-2">Appears in equation for variable</td><td id="5-3">Parameter</td><td id="5-4">Value</td><td id="5-5">Units</td><td id="5-6">Appears in equation for variable</td><td id="5-7">Parameter</td><td id="5-8">Value</td><td id="5-9">Units</td></tr>
<tr><td id="5-a">B, free BiP</td><td id="5-b">KBU</td><td id="5-c">0.8</td><td id="5-d">—</td><td id="5-e">b, Bip mRNA</td><td id="5-f">k d,b</td><td id="5-g">0.001284</td><td id="5-h">min⁻¹</td></tr>
<tr><td id="5-i">protein</td><td id="5-j"></td><td id="5-k"></td><td id="5-l"></td><td id="5-m"></td><td id="5-n">α A6</td><td id="5-o">0.012</td><td id="5-p">min⁻¹</td></tr>
<tr><td id="5-q">Pp,</td><td id="5-r">f</td><td id="5-s">0.02</td><td id="5-t">—</td><td id="5-u"></td><td id="5-v">K b6</td><td id="5-w">0.56</td><td id="5-x">—</td></tr>
<tr><td id="5-y">Phosphorylated</td><td id="5-z">KBP</td><td id="5-A">0.01</td><td id="5-B"></td><td id="5-C"></td><td id="5-D">K A6</td><td id="5-E">3</td><td id="5-F">—</td></tr>
<tr><td id="5-G">PERK</td><td id="5-H">Kup = &quot;(1/f-1)U*&quot; (formula)</td><td id="5-I"></td><td id="5-J"></td><td id="5-K"></td><td id="5-L">Kth6</td><td id="5-M">0.00001</td><td id="5-N">–</td></tr>
<tr><td id="5-O"></td><td id="5-P">1+&quot;B*tot&quot; / 1</td><td id="5-Q">1.07824</td><td id="5-R"></td><td id="5-S"></td><td id="5-T">n</td><td id="5-U">7</td><td id="5-V">–</td></tr>
<tr><td id="5-W"></td><td id="5-X">KBP 1+U* /KBU</td><td id="5-Y"></td><td id="5-Z"></td><td id="5-10"></td><td id="5-11">αA4</td><td id="5-12">0.007</td><td id="5-13">min-1</td></tr>
<tr><td id="5-14">Ip,</td><td id="5-15">f;</td><td id="5-16">0.01</td><td id="5-17">–</td><td id="5-18"></td><td id="5-19">Kb4</td><td id="5-1a">0.5</td><td id="5-1b">–</td></tr>
<tr><td id="5-1c">Phosphorylated</td><td id="5-1d">KBI</td><td id="5-1e">0.01</td><td id="5-1f"></td><td id="5-1g"></td><td id="5-1h">KA4</td><td id="5-1i">3</td><td id="5-1j">–</td></tr>
<tr><td id="5-1k">IRE1α</td><td id="5-1l">(1/fi-1)U*</td><td id="5-1m" rowspan="2">2.17848</td><td id="5-1n"></td><td id="5-1o"></td><td id="5-1p">Kth4</td><td id="5-1q">0.167</td><td id="5-1r">—</td></tr>
<tr><td id="5-1s"></td><td id="5-1t">KUI = 1, B*tot 1</td><td id="5-1u"></td><td id="5-1v"></td><td id="5-1w">αχ</td><td id="5-1x">0.002</td><td id="5-1y">min-1</td></tr>
<tr><td id="5-1z"></td><td id="5-1A">KBI 1+U*/KBU</td><td id="5-1B"></td><td id="5-1C"></td><td id="5-1D"></td><td id="5-1E">KXb</td><td id="5-1F">8</td><td id="5-1G">—</td></tr>
<tr><td id="5-1H">U,</td><td id="5-1I">ks.U</td><td id="5-1J">0.89</td><td id="5-1K">min-1</td><td id="5-1L"></td><td id="5-1M">αι</td><td id="5-1N">0.2</td><td id="5-1O">—</td></tr>
<tr><td id="5-1P">Unfolded</td><td id="5-1Q">KUI</td><td id="5-1R">0.01</td><td id="5-1S">—</td><td id="5-1T"></td><td id="5-1U">Pi</td><td id="5-1V">0.1</td><td id="5-1W">—</td></tr>
<tr><td id="5-1X">proteins</td><td id="5-1Y">Kᴇ</td><td id="5-1Z">3</td><td id="5-20">—</td><td id="5-21">Btot, total BiP</td><td id="5-22">k d,B</td><td id="5-23">0.0002514</td><td id="5-24">min⁻¹</td></tr>
<tr><td id="5-25"></td><td id="5-26">Kᴜᴜ</td><td id="5-27">6</td><td id="5-28">—</td><td id="5-29">protein</td><td id="5-2a">k t,B = (k d,B B*tot) / b*</td><td id="5-2b">0.0002514</td><td id="5-2c">min⁻¹</td></tr>
<tr><td id="5-2d"></td><td id="5-2e">δ</td><td id="5-2f">1.5</td><td id="5-2g">min⁻¹</td><td id="5-2h"></td><td id="5-2i"></td><td id="5-2j"></td><td id="5-2k"></td></tr>
<tr><td id="5-2l"></td><td id="5-2m">K</td><td id="5-2n">0.01</td><td id="5-2o">—</td><td id="5-2p">c, Chop mRNA</td><td id="5-2q">μ A4</td><td id="5-2r">0.1</td><td id="5-2s">min⁻¹</td></tr>
<tr><td id="5-2t">Ep,</td><td id="5-2u">kph</td><td id="5-2v">0.00651</td><td id="5-2w">min⁻¹</td><td id="5-2x"></td><td id="5-2y">k d,c</td><td id="5-2z">0.00393</td><td id="5-2A">min⁻¹</td></tr>
<tr><td id="5-2B">Phosphorylated</td><td id="5-2C">Kₗₒ</td><td id="5-2D">14</td><td id="5-2E">—</td><td id="5-2F"></td><td id="5-2G">K₀₄</td><td id="5-2H">0.56</td><td id="5-2I">–</td></tr>
<tr><td id="5-2J">elF2͡</td><td id="5-2K"></td><td id="5-2L">20</td><td id="5-2M"></td><td id="5-2N"></td><td id="5-2O">Kₐ₄ₐ</td><td id="5-2P">2</td><td id="5-2Q">–</td></tr>
<tr><td id="5-2R"></td><td id="5-2S">Eₒₒₒ</td><td id="5-2T">20</td><td id="5-2U">—</td><td id="5-2V"></td><td id="5-2W">Kₗₕ₄ₐ</td><td id="5-2X">0.25</td><td id="5-2Y">–</td></tr>
<tr><td id="5-2Z"></td><td id="5-30">kₐₑₕₕ1</td><td id="5-31">0.03</td><td id="5-32">minRRR</td><td id="5-33"></td><td id="5-34"></td><td id="5-35"></td><td id="5-36"></td></tr>
<tr><td id="5-37"></td><td id="5-38">kₐₑₕₕ2</td><td id="5-39">0.08</td><td id="5-3a">minRRR</td><td id="5-3b">C, CHOP</td><td id="5-3c">kₑ,ₒ</td><td id="5-3d">0.005478</td><td id="5-3e">min⁻¹</td></tr>
<tr><td id="5-3f"></td><td id="5-3g">Kdeph</td><td id="5-3h">7</td><td id="5-3i">—</td><td id="5-3j">protein</td><td id="5-3k">k t,c</td><td id="5-3l">0.0001</td><td id="5-3m">min⁻¹</td></tr>
<tr><td id="5-3n">x, Spliced Xbp1</td><td id="5-3o">kd,x</td><td id="5-3p">0.006546</td><td id="5-3q">min-1</td><td id="5-3r"></td><td id="5-3s">k t0.c = (k d.c C*)/c*</td><td id="5-3t">0.005478</td><td id="5-3u">min⁻¹</td></tr>
<tr><td id="5-3v">mRNA</td><td id="5-3w">Xtot</td><td id="5-3x">16</td><td id="5-3y">—</td><td id="5-3z">g, Gadd34</td><td id="5-3A">η C</td><td id="5-3B">0.012</td><td id="5-3C">min⁻¹</td></tr>
<tr><td id="5-3D"></td><td id="5-3E">ksp</td><td id="5-3F">0.00785</td><td id="5-3G">min-1</td><td id="5-3H">mRNA</td><td id="5-3I">K A4g</td><td id="5-3J">0.75</td><td id="5-3K">—</td></tr>
<tr><td id="5-3L"></td><td id="5-3M">Kx</td><td id="5-3N">3</td><td id="5-3O">—</td><td id="5-3P"></td><td id="5-3Q">K th4g</td><td id="5-3R">0.1</td><td id="5-3S">—</td></tr>
<tr><td id="5-3T">A6, Cleaved</td><td id="5-3U">kcl</td><td id="5-3V">4</td><td id="5-3W">min-1</td><td id="5-3X"></td><td id="5-3Y">Kₒ</td><td id="5-3Z">5</td><td id="5-40">–</td></tr>
<tr><td id="5-41">ATF6α</td><td id="5-42">KBA6</td><td id="5-43">0.000016</td><td id="5-44">—</td><td id="5-45"></td><td id="5-46">k𝘥,g</td><td id="5-47">0.003468</td><td id="5-48">min⁻¹</td></tr>
<tr><td id="5-49"></td><td id="5-4a">A6tot</td><td id="5-4b">15</td><td id="5-4c">—</td><td id="5-4d" rowspan="2">G, GADD34 protein</td><td id="5-4e" rowspan="2">k d,G k t,G</td><td id="5-4f" rowspan="2">0.003852 0.0015</td><td id="5-4g">min⁻¹</td></tr>
<tr><td id="5-4h"></td><td id="5-4i">kd, A6</td><td id="5-4j">0.00384</td><td id="5-4k">min-1</td><td id="5-4l">min⁻¹</td></tr>
<tr><td id="5-4m">A4, ATF4</td><td id="5-4n">Y</td><td id="5-4o">0.001</td><td id="5-4p">min-1</td><td id="5-4q"></td><td id="5-4r">k = k₁ + k₂ (G*V / V₀*)</td><td id="5-4s" rowspan="2">0.003852</td><td id="5-4t">min⁻¹</td></tr>
<tr><td id="5-4u">protein</td><td id="5-4v">k₂,A4</td><td id="5-4w">0.00384</td><td id="5-4x">minⁱ</td><td id="5-4y"></td><td id="5-4z">Kt0,G = (Kd,G0 / g</td><td id="5-4A">image of 5 vertical bars</td></tr>
</table>

<a id='b279d782-3185-4a6d-8fe7-a2fe2b164c23'></a>

All steady state values are normalized under unstressed conditions: P*p = I*p = x* = U* = E*p = A6* = A4* = b* = B*tot = c* = C* = g* = G* = 1.

<a id='fed44291-63ec-4f23-abbd-58a13b546439'></a>

TABLE 2: Definitions of variables and parameter values.

<a id='04d198ea-2911-468c-96ec-975f1a27e035'></a>

We modeled these reactions using a mass-action law in their steady state, setting the reaction speed in their differential equations to zero

$\frac{d[BP]}{dt} = \frac{d[UP]}{dt} = 0$

<a id='35c9edd4-3198-401e-9c51-5f344f7af420'></a>

and solving the equations for [BP] and [UP], respectively, effec-
tively converting these variables to dependent variables:

[BP] = [BiP] · [PERK]
-------
K_BP

, [UP] = [U] · [PERK]
-------
K_UP

<a id='687fb900-bd9c-472b-9b19-6698fbfd8199'></a>

where KBP and KUP are positive constants.

<a id='bc25b3f4-fc16-444a-83ba-edc1629c5517'></a>

Because the total quantity of PERK is constant, we then ob-
tained the amount of phosphorylated PERK from

<a id='215c5752-4a49-4bf6-881f-f9730f3269ef'></a>

[PERK - tot] = [PERK] + [BP] + [UP]

= [PERK] + [BiP] * [PERK] / K_BP + [U] * [PERK] / K_UP

= [PERK] (1 + [BiP] / K_BP + [U] / K_UP)

≈ [PERK - P] K_UP / [U] (1 + [BiP] / K_BP + [U] / K_UP).

<a id='d16927ea-9872-4cd1-b25b-9ea00d09a1b1'></a>

Volume 29 June 15, 2018

<a id='a2640719-9185-4841-bb1c-c645f2416db4'></a>

ODE model of UPR regulatory logic

<a id='9ac7aeba-ba64-4f2c-922e-bd7cb24f5bb3'></a>

1507

<!-- PAGE BREAK -->

<a id='5b469ebb-0c96-44ab-bbc4-01d8cab16f84'></a>

With a notation for the percentage of total PERK that is phosphorylated under unstressed conditions ($f = [PERK-P] / [PERK - tot]$), this becomes

<a id='39d198f8-fde2-4a50-8523-d08b478643db'></a>

[PERK-P] = [PERK-P](1/f) \frac{[U]}{K_UP + \frac{K_UP}{K_BP}[BiP] + [U]}

<a id='b36d9f3f-fd9c-433a-9a41-4ab64d585596'></a>

which gives rise to Eq. 2 in the model. The same assumptions
were made in modeling IRE1 (Eq. 3).

<a id='fa4244fe-a7d2-4aed-913a-ce2f54568e71'></a>

### Model specification and fit
The model was entrained upon a representative data set quantifying mRNA expression of _Bip_, _Chop_, and _Gadd34_ taken from wild-type MEFs. We chose RNA concentrations as the basis for entrainment because RNA species can be more easily and precisely quantified than can protein species by virtue of quantitative reverse transcription PCR (qRT-PCR). In addition, the use of only these three measures should in principle guide the model toward biological relevance without unnecessarily constraining it. A sense of the intrinsic biological variability of the response can be gained from Supplemental Figure S1, which compares the entrainment data set with an independent data set collected from a separate line of wild-type cells.

<a id='051508e0-f17d-4538-98de-4d0d60428c03'></a>

Of the 61 parameters (Table 2), nine degradation rates were previously experimentally determined: those of BiP mRNA and protein, CHOP mRNA and protein, GADD34 mRNA and protein, Xbp1 mRNA, ATF4 protein, and cleaved ATF6 protein (Rutkowski et al., 2006). In addition, we set k<sub>t,B</sub> = k<sub>dB</sub>, k<sub>t0,C</sub> = k<sub>d,C</sub>, and k<sub>t0,G</sub> = k<sub>d,G</sub> to ensure that the variables B<sub>tot</sub>, C, and G (quantities of BiP, CHOP, and GADD34 proteins) remain at steady state levels under unstressed conditions. We also constrained the parameters K<sub>UP</sub> and K<sub>UI</sub> to ensure that P<sub>P</sub> and I<sub>P</sub> (phosphorylated PERK and IRE1, respectively) have their steady states normalized to 1. The remaining 47 parameters were unknown and had to be determined by fitting the solutions of the model to the experimental data using COPASI software.

<a id='7ea044b1-80d7-4b1b-a8b5-ffdf6e85e197'></a>

There are, in principle, an infinite number of possible wiring dia-grams and structures that could have been used to specify the model. Therefore, qualitative judgments about the likely relation-ships among components and how best to represent them mathe-matically drove the model creation. Furthermore, determining the numerical value of the parameters was an underdetermined prob-lem, as the model had a large number of degrees of freedom, given by the number of unknown parameters, and a relatively sparse data set to constrain its solution.

<a id='28d848a3-2d3c-4962-8ac4-ab1e06dab3ad'></a>

The system was solved hundreds of times, each with a different
set of parameters θ, and COPASI's numerical optimization algo-
rithms guided the parameter search toward a set that best repli-
cated the experimental data by finding a local minimum for the
weighted residual sum of squares (RSS(θ)) between experimental
data and simulation for all variables at all time points:

<a id='ee87cd6c-d7c0-44df-9d21-71148088bea4'></a>

RSS(θ) = Σ_ij w_j (x_ij - y_ij (θ))^2

<a id='102914e5-c652-47fd-8ba5-03cd930b43a0'></a>

where x_ij is the experimental measurement of variable j at time step i and y_ij (θ) is the corresponding value given by the model using parameter set θ. COPASI's default method multiplies each squared residual by a weight factor w_j = 1/<x_j^2>, where <x_j^2> is the mean value of the points x_j^2 in the trajectory for variable j. The purpose of this weight factor is to give the trajectories of each variable similar importance in the fit, regardless of their magnitude in relation to the other variables. The weight factors were scaled so that the maximal occurring weight for each stress level was 1, and all other weights

<a id='ade6e23d-492f-4fb3-b226-d38048bd886b'></a>

scaled accordingly. Thus, the RSS tests the goodness of fit of a pa-
rameter set against all other parameter sets, given the input equa-
tions. To further constrain the parameter search, we constrained
each parameter to vary by a mean of no more than two orders of
magnitude.

<a id='b4a12a50-10d8-4443-8f3f-a2cb1ff2a70a'></a>

Our parameter search methodology combined this quantitative
approach to the fit of the model to the variables for which we had
experimental data with qualitative judgements as to reasonable
simulation results in the other variables, in order to define an opti-
mum parameter set θ* with a low RSS and qualitatively correct solu-
tions for all variables. Thus, although the optimal parameter set is
not the one with the absolute lowest local minimum RSS determined
by the search algorithm, it is not far from it. A random sampling of
200 parameter sets in our parameter space generated RSS values
ranging from 43 to 4996. Only 3% of these parameter sets give RSS
values below the RSS for our optimum parameter set (224). Supple-
mental Figure S2 shows a bee-swarm representation of the distribu-
tion of RSS values obtained from this simulation, which was repeated
multiple times with similar results. This figure also shows an example
of unsatisfactory model output arising from a lower-RSS parameter
set, illustrating that the optimum model is one that combines a low
RSS value with qualitatively faithful outputs.

<a id='ac523a6a-c51d-479e-a140-db724d52d1a3'></a>

The solutions to the ODE system with these parameters, modeled at stress levels of 2.5 or 10 nM TG based solely on varying the stress input function S(t), are shown in Figure 3, compared with the entrainment data set for the mRNA expression of Bip, Chop, and Gadd34 (also Supplemental Figure S1). The simulation shows both activation and deactivation/recovery phases of the UPR. The most important feature that we strove to recapitulate in parameter selection was the relative kinetics of both phases of the response. As is evident in Supplemental Figure S1, the model solution was faithful to real UPR kinetics within the context of inter- and intraexperiment variability. It is important to note that model fitting inevitably entails compromises; for example, attempts to make the resolution of Gadd34 expression under the 2.5 nM condition more closely match the experimental data (by, for instance, peaking at 8 h rather than 12 h; Supplemental Figure S1C) resulted in a poorer fit under the 10 nM condition. The model represented the best-fit solution given these constraints.

<a id='76f8c980-51c7-457e-af6e-e6255d42c81a'></a>

The other qualitative feature that we wished the model to repro-
duce was the complete loss of CHOP and GADD34 up-regulation
under conditions where cells can survive (i.e., 2.5 nM TG) but their
persistence under conditions where cells cannot survive (i.e., 10 nM;
Rutkowski et al., 2006). The presented solution was able to success-
fully recreate this response (Figure 3, H and J), and was accompanied
by a nearly complete resolution of unfolded proteins—i.e., a return
to basal levels—under the 2.5 nM condition but not the 10 nM con-
dition (Figure 3A). Finally, up-regulation of BiP protein had to persist
long past the resolution phase of the response under both condi-
tions (Rutkowski et al., 2006); this behavior is seen in Figure 3M.

<a id='54db6f12-87f8-4f16-a8ee-4f61d96622e9'></a>

**Validation of the model against knockouts**
To test the biological trustworthiness of the model, we next tested the effects of in silico deletion of integral UPR components against the phenotypes of cells lacking those same components, both as reported in the literature and in our own experimental testing. The first of these deletions was PERK (Supplemental Figure S3); the most salient features that we expected the model to reproduce were nearly complete dependence of the downstream proteins ATF4, CHOP and GADD34 on PERK, and also a partial dependence of BiP up-regulation (Harding et al., 2000a). Indeed, we observed these relationships (Supplemental Figure S3, F, H, J, and M), which

<a id='649be616-7f98-4a21-a67b-b4f2ffe3f19c'></a>

1508

<a id='7dedab7d-7af4-49d7-a8fd-046f8f62f89e'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='a45abbd1-aeb6-4738-825e-49ec8fafbd14'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='6b249a5e-3a67-4f83-b1c9-c38be336dc33'></a>

<::A multi-panel figure displays 14 line graphs (A-N) comparing model predictions against experimental data for various cellular components. The legend at the top indicates: '2.5 model' (blue solid line), 'o 2.5 experimental' (blue open circles), '10 model' (red solid line), and 'o 10 experimental' (red open circles). All graphs share a common x-axis labeled 'time in hours' ranging from 0 to 72. The y-axis in all graphs represents 'fold induction'. A gray shaded area at the bottom of each graph defines the basal value for each component. The panels are as follows: A) Unfolded Proteins, y-axis from 0 to 12. B) P-IRE1, y-axis from 0 to 40. C) XBP1, y-axis from 0 to 16. D) P-PERK, y-axis from 0 to 28. E) P-eIF2α, y-axis from 0 to 9. F) ATF4, y-axis from 0 to 11. G) Chop mRNA, y-axis from 0 to 70, showing both model predictions and experimental data points. H) CHOP, y-axis from 0 to 60. I) Gadd34 mRNA, y-axis from 0 to 18, showing both model predictions and experimental data points. J) GADD34, y-axis from 0 to 12. K) ATF6cl, y-axis from 0 to 10. L) Bip mRNA, y-axis from 0 to 16, showing both model predictions and experimental data points. M) BiP, y-axis from 0 to 6. N) BiPfree, y-axis from 0 to 1.4.: chart::>FIGURE 3: Comparison of model prediction against experimental data. The various outputs of the model under simulations of 2.5- or 10-nM TG treatment are shown (solid lines), with fold induction as the y-axis value. Superimposed (open circles) are experimental data for the same conditions, with only mean values shown for simplicity; means were collected from experiments conducted in biological triplicate. In this and subsequent figures, the gray shaded areas define the basal value for each component, and the x-axis denotes time in hours. See also Supplemental Figure S1. 

<a id='788bb331-e4fb-4e07-8a33-208f22532c7e'></a>

followed naturally from ablation of eIF2̘̘̘ phosphorylation (Supplemental Figure S3E). The attenuation of _Bip_ up-regulation was seen despite elevated ATF6 cleavage (Supplemental Figure S3K), which followed presumably from an increased burden of unfolded proteins (Supplemental Figure S3A). We also modeled in silico deletion of IRE1; these results are shown in Supplemental Figure S4. As described above, the parameter set was chosen so that the contribution of the IRE1/XBP1 pathway would be modest, although its inclusion in the model means that its contribution can be more heavily weighted when other systems are being considered.

<a id='80f4da8c-9529-4bde-9420-ccfea53d8c4c'></a>

More stringent tests of the model would include ablation of com-ponents whose contribution to downstream targets was partial rather than complete, as these are likely to affect UPR output in more complex ways. Thus, we compared the result of in silico ATF6 deletion against cells lacking ATF6 (Figure 4; Supplemental Figure S5), since ATF6 contributes to but is not absolutely essential for the regulation of both BiP and CHOP (Wu et al., 2007). Under both 2.5-and 10-nM stress conditions, in silico loss of ATF6 perpetuated ER stress (Figure 4A) and consequently, PERK activation (Figure 4B). Up-regulation of CHOP was blunted in the early phase of the

<a id='f75f68bc-99cb-4ffc-bed0-395b3de16260'></a>

Volume 29 June 15, 2018

<a id='29ac089e-b5ec-4bdf-839f-8a5a83f3fd98'></a>

ODE model of UPR regulatory logic

<a id='3ef58df8-4b00-47ca-ac8e-7482463d2910'></a>

1509

<!-- PAGE BREAK -->

<a id='9897451c-a323-4da9-aae8-cc1e7638f48c'></a>

<::visual content: chart: FIGURE 4: Comparison of model and experimental outputs for deletion of ATF6α. (A-F) Selected model outputs are shown after ATF6α was deleted in silico (dashed lines), compared against outputs in wild-type simulations (solid lines). (G) Wild-type or Atf6-/- MEFs (two independent lines of each; genotype indicated above each panel) were treated with 5 nM TG for the indicated times, and expression of BiP and CHOP was assessed by immunoblot. See also Supplemental Figure S5. Loading control was a-actin. Hairlines are for visual clarity only.::>

<::visual content: chart and immunoblot: 
Legend for charts A-F:
- Blue solid line: 2.5 w.t.
- Blue dashed line: 2.5 Atf6-/-
- Red solid line: 10 w.t.
- Red dashed line: 10 Atf6-/-

(A) Unfolded Proteins chart
- X-axis: Time (0 to 72, increments of 12)
- Y-axis: 0 to 12
- Four curves showing protein levels over time.

(B) P-PERK chart
- X-axis: Time (0 to 72, increments of 12)
- Y-axis: 0 to 28
- Four curves showing protein levels over time.

(C) ATF6cl chart
- X-axis: Time (0 to 72, increments of 12)
- Y-axis: 0 to 10
- Four curves showing protein levels over time.

(D) CHOP chart
- X-axis: Time (0 to 72, increments of 12)
- Y-axis: 0 to 60
- Four curves showing protein levels over time.

(E) BiP chart
- X-axis: Time (0 to 72, increments of 12)
- Y-axis: 0 to 6
- Four curves showing protein levels over time.

(F) BiPfree chart
- X-axis: Time (0 to 72, increments of 12)
- Y-axis: 0 to 1.4
- Four curves showing protein levels over time.

(G) Immunoblot
- Treatments/Time points:
  - 5 nM TG (control, 0h):
    - Atf6α: x, x*
  - 8h:
    - Atf6α: x, x*
  - 12h:
    - Atf6α: x, x*
  - 24h:
    - Atf6α: x, x*
  - 48h:
    - Atf6α: x, x*
- Rows:
  - BiP: Immunoblot bands across all conditions.
  - CHOP: Immunoblot bands across all conditions.
  - loading: Immunoblot bands across all conditions (a-actin loading control).
::>

<a id='98ff336c-94a0-4142-b584-4c7f7c63955c'></a>

response, but persisted long after being resolved or attenuated in the wild-type simulations (Figure 4D). BiP up-regulation was also compromised throughout the time course of the simulation (Figure 4E). The likely consequence of this attenuated BiP up-regulation was failure to restore levels of free (i.e., not bound by unfolded proteins) BiP (Figure 4F). While the true concentrations of unfolded proteins or free BiP are not readily measurable and are thus inferred, the expression of BiP and CHOP in cells was similar to the model's

<a id='45b98ce4-9846-4117-8a6f-c3a97c281681'></a>

predictions. In response to 5 nM TG (i.e., between 2.5 and 10 nM), CHOP up-regulation was reduced at early times but augmented at later times in Atf6a-/- cells, as predicted by the model (Supplemental Figure S5O), while BiP up-regulation lagged throughout (Figure 4G).

<a id='c54c7866-26e4-49e8-9562-5078c44f4d8a'></a>

We next conducted similar experiments comparing in silico deletion of ATF4 to Atf4-/- cells (Figure 5; Supplemental Figure S6). Beyond dramatically compromising up-regulation of CHOP, as expected (Supplemental Figure S6, G and H), the model also predicted persistent phosphorylation of eIF2α, likely due to failure to up-regulate the eIF2α phosphatase GADD34 (Figure 5A). In fact, eIF2α phosphorylation asymptotically approached an elevated steady-state level (Figure 5B) that persisted even when the simulation was continued for 250 h (unpublished data). Mirroring this prediction, eIF2α phosphorylation diminished markedly from its initial 8-h peak in wild-type cells but not in Atf4-/- cells (Figure 5C). ATF4 also directly binds to the Bip promoter (Luo et al., 2003; Han et al., 2013), and so the model predicted suppressed Bip up-regulation in the early phase of the response (Figure 5D). A suppression of Bip mRNA in Atf4-/- MEFs was also seen experimentally (Figure 5E).

<a id='cfdd618c-2471-4fcb-8d8f-fdfe4f50ab06'></a>

Our final validation test of the model was to delete GADD34 (Figure 6; Supplemental Figure S7), which modulates the regulatory step of eIF2α dephosphorylation rather than an initiating step as with PERK, IRE1, ATF6, and ATF4. One of the most surprising previously unaccounted-for features of Gadd34 deletion reported in cells is the failure of those cells to fully transcriptionally up-regulate BiP (Novoa et al., 2003). When we deleted GADD34 in silico, we found a dramatic diminution of unfolded proteins at intermediate times (4–24 h), consistent with the idea that GADD34 exacerbates ER stress by promoting ongoing protein synthesis in the stressed ER (Figure 6B; Marciniak et al., 2004). This diminished unfolded protein accumulation was also presumably responsible for blunted activation of ATF6 (Figure 6C), which in turn compromised up-regulation of Bip mRNA (Figure 6D) and protein (Figure 6E). Thus, our model to some extent mirrors and accounts for the phenotype of Gadd34−/− cells.

<a id='e0c95bd8-50f5-4774-b5cf-c1d3a1d0c89e'></a>

Our model also makes a surprising prediction about the pheno-
type of _Gadd34_−/− cells: at long time points under the 2.5-nM con-
dition, _Gadd34_−/− cells should have a greater unfolded protein
burden (Figure 6B) than wild-type cells, while, paradoxically, the
situation is reversed under the 10-nM condition. In other words, loss
of GADD34 should sensitize cells to low concentrations of TG, but
should protect cells from higher concentrations. Based on the
model, the highest sensitivity to stress should be seen in wild-type

<a id='70a85c89-5df1-4aab-bb00-cef008fb9121'></a>

1510

<a id='eaa98ebc-e79c-4c81-a7d8-f81749a298df'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='b7693c27-95ba-45b7-be35-742cf0e4ba77'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='038c3460-7ba2-4e07-9b2f-a04d0a023cbf'></a>

- 2.5 w.t. - - 2.5 Atf4-/- - 10 w.t. - - 10 Atf4-/-
A GADD34
<::Line graph titled "GADD34" showing relative expression over time (h). The X-axis ranges from 0 to 72 in increments of 12. The Y-axis ranges from 0 to 12 in increments of 2. Four lines are plotted: a solid blue line (2.5 w.t.), a dashed blue line (2.5 Atf4-/-), a solid red line (10 w.t.), and a dashed red line (10 Atf4-/-). There is a gray shaded area at the bottom, spanning from Y=0 to Y=1.
: chart::>

B P-eIF2α
<::Line graph titled "P-eIF2α" showing relative expression over time (h). The X-axis ranges from 0 to 72 in increments of 12. The Y-axis ranges from 0 to 10 in increments of 1. Four lines are plotted: a solid blue line (2.5 w.t.), a dashed blue line (2.5 Atf4-/-), a solid red line (10 w.t.), and a dashed red line (10 Atf4-/-). There is a gray shaded area at the bottom, spanning from Y=0 to Y=1.
: chart::>

C
8h 12h 24h 48h
Atf4 +/+ -/- +/+ -/- +/+ -/- +/+ -/-
PeIF2α
loading
<::Western blot showing protein levels for PeIF2α and a loading control at different time points (8h, 12h, 24h, 48h) and genotypes (Atf4 +/+ and -/-). For each time point and genotype, there are distinct bands for PeIF2α (top row) and loading control (bottom row). The loading control bands appear consistent across all conditions, while PeIF2α bands show varying intensities.
: gel::> 

<a id='c367d8dd-e69b-4337-b28c-7eb2a85ac5e3'></a>

<::D Bip mRNA: line graph::>  The graph shows Bip mRNA levels over time. The y-axis ranges from 0 to 16. The x-axis ranges from 0 to 72, with major ticks at 0, 12, 24, 36, 48, 60, and 72. There are four curves: a solid red line peaking around 15 at x=12, a solid blue line peaking around 11 at x=12, a dashed red line peaking around 6 at x=12, and a dashed blue line peaking around 4 at x=12. All lines start near 0 and decrease after their peak, reaching values between 1 and 4 at x=72. A light grey shaded bar is present at the bottom of the graph, along the x-axis from 0 to 72, near y=0.

<a id='50565775-4809-4bac-910a-ce28e081dd77'></a>

<::Figure E: Line graph titled "Bip mRNA, experimental" with "p=10-3 for genotype". The y-axis ranges from 0 to 9. The x-axis ranges from 0 to 24. The legend indicates: blue filled circles (•) represent "w.t.", blue open circles (o) represent "KO", blue filled squares connected by a solid line (—■—) represent "w.t. avg", and blue open squares connected by a dashed line (—□—) represent "KO avg". The graph shows two lines with error bars: one solid blue line connecting filled squares for "w.t. avg" and one dashed blue line connecting open squares for "KO avg". Individual data points are also plotted as circles for "w.t." and "KO" respectively.::>

<a id='3f983a1b-b584-4617-8342-e63f8ee6fc37'></a>

FIGURE 5: Comparison of model and experimental outputs for deletion of ATF4.
(A, B, D) Selected model outputs are shown after ATF4 was deleted in silico (dashed lines), compared against outputs in wild-type simulations (solid lines). (C) Immunoblot showing the phosphorylated form of eIF2α upon treatment of wild-type or Atf4−/− MEFs with 2.5 nM TG for the indicated times. Loading control was calnexin. (E) qRT-PCR quantifying Bip mRNA expression in wild-type or Atf4−/− MEFs upon treatment with 2.5 nM TG for the indicated times. Data were normalized against expression in cells of the same genotype treated with vehicle. Significance was calculated by two-way ANOVA for time and genotype.

<a id='abf79792-949b-497f-9d24-22e054a8fb68'></a>

cells treated with 10 nM TG, followed by _Gadd34_–/– cells treated with 10 nM TG, then _Gadd34_–/– cells treated with 2.5 nM TG, and last wild-type cells treated with 2.5 nM TG as the most resistant (from Figure 6B). To test this prediction, we treated cells with the GADD34 inhibitor salubrinal (Boyce _et al._, 2005) and found that, indeed, inhibition of GADD34 activity paradoxically sensitizes cells to 2.5 nM TG but protects them from 10 nM (and 100 nM) TG (Figure 6, G and H).

<a id='fbae22cd-a329-4f68-ac8d-e2b1911eb2e9'></a>

Like any drug, salubrinal is an imperfect vehicle for probing
GADD34 ablation; the more recently discovered GADD34 inhibitor
Sephin1 was, in our hands, extremely toxic to MEFs on its own

<a id='23b5d020-ea46-43f8-b580-e1003722acf4'></a>

(unpublished data). In addition, here we are
taking viability as an indicator of sensitivity
to stress. The true unfolded protein burden
is difficult to quantify, and linking the un-
folded protein burden to viability rests on
the assumption that cell death follows from
the ER stress level. Despite these caveats,
the computational and experimental data
are consistent at least to the extent that
GADD34 has opposing effects on the cellu-
lar response to 2.5 versus 10 nM TG. These
data also suggest that GADD34 seems not
so much to accelerate cell dysfunction and
death as to potentiate a steep threshold
between adaptation and death.

<a id='a4dc7d5e-be5a-41e8-bcda-d7d8b630c86f'></a>

**Using the model to explore the regulatory logic of the UPR**

Taken together, the above data show that the model makes predictions about UPR output that can be successfully tested experimentally. The validation experiments above lend confidence to the idea that the model captures the important temporal trends of the response and the relationships among its constituents. We thus used the model as a tool to explore the functional consequences of the regulatory pathways embedded within the UPR in in silico experiments that would be cumbersome to carry out in living cells. While many different questions might be asked with this model, we were particularly interested in examining how the output of a UPR stripped of its various feedbacks, feedforwards, and overlaps would differ from its actual output, and what implications these differences might have for UPR responsiveness and cell fate. We chose two such manipulations for these purposes.

<a id='f45a6902-e35b-40c9-881b-5ef1d72a0c18'></a>

We first tested the significance of translational stimulation of CHOP and GADD34 by eIF2α phosphorylation (Figure 7; Supplemental Figure S8; Lee et al., 2009; Palam et al., 2011), which is consistent with the presence of short open reading frames in the 5' untranslated region of each mRNA akin to those found in Atf4 mRNA. A priori, one might assume that the role of such a feedforward circuit would be to enhance the expression of both components. How-

<a id='362337e8-1c98-4eba-8704-4f7a2eb4adeb'></a>

ever, we found that this was not the case; instead, *ablation* of the contribution of eIF2α to CHOP and GADD34 enhanced maximal up-regulation of both proteins (Figure 7, C and D). Rather, we observed that deletion of this feedforward loop changed the tem- poral sensitivity of the response: in wild-type cells, GADD34 was significantly up-regulated at earlier times than in feedforward- ablated cells and was likewise down-regulated more rapidly in the recovery phase (Figure 7, D and E; note that the dashed lines des- ignating Gadd34-/- cells begin their ascent later than the solid lines denoting wild-type cells). Thus, despite ultimately yielding a greater peak of GADD34 expression, feedforward-ablated cells

<a id='9c4d0aca-5dc4-4651-9526-7a5a4335e756'></a>

Volume 29 June 15, 2018

<a id='d1799a01-178e-42ea-8fca-bf04c84428c6'></a>

ODE model of UPR regulatory logic

<a id='68b848be-c782-404c-b92f-0358bb42ef56'></a>

1511

<!-- PAGE BREAK -->

<a id='d9ab68c9-008b-484c-9730-dcc786f7f1b8'></a>

<::figure: A multi-panel figure titled "Model-predicted output for deletion of GADD34".

Panels A-F display line graphs showing model-predicted outputs over time (0-72 hours).
Common legend for A-F: "-2.5 w.t.", "-2.5 G34-/-", "-10 w.t.", "-10 G34-/-".
- Panel A: P-eIF2α. Y-axis from 0 to 16.
- Panel B: Unfolded Proteins. Y-axis from 0 to 12.
- Panel C: ATF6cl. Y-axis from 0 to 10.
- Panel D: Bip mRNA. Y-axis from 0 to 18.
- Panel E: BiP. Y-axis from 0 to 6.
- Panel F: BiPfree. Y-axis from 0 to 1.4.
All panels A-F show different colored and dashed/solid lines representing the legend conditions, often with a shaded grey region at the bottom indicating a baseline or threshold.

Panels G-H display line graphs with data points showing percent survival versus concentration (0-100) of TG.
Common Y-axis for G-H: "percent survival" (0-120).
Common legend for G-H: "+Sal" (open circles, dashed line) and "-Sal" (filled circles, solid line).
- Panel G: 2d TG. Shows a decrease in percent survival as TG concentration increases, with "+Sal" generally having higher survival than "-Sal".
- Panel H: 3d TG. Similar trend to G, with "+Sal" showing higher survival than "-Sal" across TG concentrations.

FIGURE 6: Model-predicted output for deletion of GADD34. (A-F) GADD34 was deleted in silico and various model outputs are shown. (G, H) Wild-type MEFs were treated for 2 or 3 d with the indicated concentration of TG in the presence or absence of 50 µM salubrinal (Sal). An MTT assay was used to assess cell number relative to cells without TG. Error bars represent means ± SDM. Individual data points from three samples of each condition are shown as open (+Sal) or filled (-Sal) circles.::>

<a id='c7de43bb-0872-40dd-8076-1be2d321799c'></a>

showed elevated and more persistent phosphorylation of eIF2α
(Figure 7, F and G).

<a id='ed1e0f1d-421d-495b-b577-9692fdcee65b'></a>

Next, we used the model to explore the regulatory logic underly-ing crosstalk between the PERK and ATF6 pathways. Namely, why does ATF6 contribute to CHOP expression when ATF6 largely regu-lates ER chaperones and other adaptive factors (Wu et al., 2007; Adachi et al., 2008)? Likewise, why does the PERK pathway (presum-ably through ATF4) regulate BiP expression when activation of the ATF6 pathway would seem adequate for that purpose? Thus, we either deleted the contribution of ATF6 to Chop, the contribution of ATF4 to Bip, or both (termed "linear," since the crosstalk between pathways is removed; Figure 8; Supplemental Figures S9 and S10). As expected, deleting the ATF4 contribution to Bip caused un-folded proteins to persist (Figure 8B), presumably due to attenuated BiP up-regulation (Figure 8C). In contrast, deleting the ATF6 contri-bution to Chop had no effect on unfolded proteins; even though this deletion had a small effect on GADD34 production, this effect was not sufficient to alter elF2a dephosphorylation (Supplemental Figures S9 and S10). However, both deletions affected CHOP ex-pression, but in distinct ways (Figure 8D). Deletion of the ATF6 con-tribution to CHOP caused CHOP expression to reach a lower peak, but to return to basal levels in the same time as in the wild type. Deletion of the ATF4 contribution to BiP caused CHOP to reach a greater peak. Its clearance occurred with similar kinetics as in the

<a id='2105f22f-f7aa-4b5f-a00d-e1b4968967c8'></a>

wild type, but because of its greater maximum, its expression per-
sisted longer. The linear simulation (i.e., the combination of both
deletions) combined the features of both single deletions, so that
CHOP expression was blunted, yet slower to resolve. This result was
evident for both the 2.5- and 10-nM conditions (Supplemental
Figures S9 and S10).

<a id='d7189f18-5efa-44c0-a049-bdffeb9ed4fb'></a>

We reasoned that the tendency of BiP and CHOP to act at cross purposes in promoting adaptation or death, respectively, might make comparing the relative amounts of these two proteins an enlightening metric. From this ratio, it can be seen that crosstalk between the two pathways creates a condition under which the anti-adaptive pathway is relatively favored at earlier time points (notably, those that occur prior to the commitment to cell death, which occurs in the range of 12–16 h; Harding et al., 2003), but then is rapidly disfavored at later time points (Figure 8, E and F). Absent the contribution of ATF4 to BiP, CHOP was both more favored and more persistent, while absent the contribution of ATF6 to CHOP, initial CHOP induction was blunted.

<a id='f0f16844-6300-4b2c-96ca-5be29a23da06'></a>

## DISCUSSION
This paper establishes the first mathematical model for the dynam-
ics of vertebrate UPR signaling entrained on experimental data. We
constructed a wiring diagram based on qualitative knowledge about
previously studied core UPR components and their hypothetical

<a id='ea16f2f8-2a8c-4538-8532-0697e3ecbfb5'></a>

1512

<a id='457fe960-352a-4dab-8a86-114ac3ab4a3a'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='e3c11fba-9a94-4c0a-99a5-6c8b67643056'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='7faee817-3c0f-4ade-bcf2-be869ab97883'></a>

<::visual content: A schematic diagram shows a biological pathway with components eIF2α (phosphorylated, indicated by 'P'), ATF4, CHOP, and GADD34, connected by dashed blue arrows. Red 'X' marks indicate in silico deletion of feedforward control, specifically targeting the arrows from ATF4 to CHOP and from ATF4 to GADD34. Below the diagram, a legend for panels B-G is provided: "—2.5 w.t." (solid blue line), "--2.5 Δf.f." (dashed blue line), "—10 w.t." (solid red line), "--10 Δf.f." (dashed red line).: diagram and line charts::>
FIGURE 7: In silico deletion of feedforward control of CHOP and GADD34. (A) Schematic showing the steps targeted by in silico deletion (red "X"). (B-G) Model simulations were run after translational control of CHOP and GADD34 was removed by eIF2α (Δf.f.; dashed lines), compared against wild-type output (solid lines). Panels E and G are insets representing times 0–12 h for GADD34 and P-eIF2α, respectively.
<::visual content: (B) A line graph titled "Unfolded Proteins" shows concentration on the Y-axis (0-12) versus time on the X-axis (0-72 h). Four lines (solid blue, dashed blue, solid red, dashed red) depict different conditions. All lines start high, decrease, and then stabilize, with red lines generally showing higher concentrations than blue lines. A shaded gray area is present at the bottom of the graph from 0 to approximately 12 h. (C) A line graph titled "CHOP" shows concentration on the Y-axis (0-90) versus time on the X-axis (0-72 h). Four lines (solid blue, dashed blue, solid red, dashed red) show all conditions peaking around 12-18 h and then declining to near zero. Red lines exhibit higher peak concentrations than blue lines, and dashed lines peak higher than their solid counterparts. (D) A line graph titled "GADD34" shows concentration on the Y-axis (0-20) versus time on the X-axis (0-72 h). Four lines (solid blue, dashed blue, solid red, dashed red) show initial peaks around 12-18 h, similar to panel C. However, the red lines, especially the dashed red line, show a subsequent increase after approximately 48 h. An 'inset' box is highlighted from 0-12 h on the X-axis. (E) A line graph titled "GADD34 inset" shows a zoomed-in view of the data from panel D for the first 12 hours, with concentration on the Y-axis (0-14) versus time on the X-axis (0-12 h). The four lines (solid blue, dashed blue, solid red, dashed red) show the initial rise and fall, with red lines generally higher than blue lines. (F) A line graph titled "P-eIF2α" shows concentration on the Y-axis (0-14) versus time on the X-axis (0-72 h). Four lines (solid blue, dashed blue, solid red, dashed red) all peak sharply around 6-12 h and then rapidly decrease to near zero. Red lines show higher peaks than blue lines, and dashed lines peak higher than their solid counterparts. An 'inset' box is highlighted from 0-12 h on the X-axis. (G) A line graph titled "P-eIF2α inset" shows a zoomed-in view of the data from panel F for the first 12 hours, with concentration on the Y-axis (0-14) versus time on the X-axis (0-12 h). The four lines (solid blue, dashed blue, solid red, dashed red) illustrate the sharp initial peak and subsequent decline, with red lines generally showing higher concentrations than blue lines, and dashed lines peaking higher than solid lines.: line charts::>

<a id='022a7cb3-d852-4cb2-9b5e-5fff5f34d863'></a>

interactions, including the ATF6 and PERK signaling pathways and crosstalk leading to the expression of BiP, CHOP, and GADD34. Then we devised a framework to approach the construction of the ODEs associated with this wiring diagram, based on assumed bio-chemical reactions involving each node in the UPR's network. Unknown kinetic parameters were determined by fitting the model's solutions to experimental time-course data for relative increases of Bip, Chop, and Gadd34 mRNA collected from wild-type MEFS under stress induced by thapsigargin in two different doses: low (2.5 nM TG) and high (10 nM TG). The model was validated by both

<a id='ad81aa90-b13f-4b3d-a3d1-3dadf339f1c7'></a>

its fit to experimental data in wild-type cells
and its ability to successfully predict the
phenotypes of genetically or pharmacologi-
cally manipulated cells.

<a id='15f8509a-fc75-47db-8601-aacf0dc8dd07'></a>

While the bulk of this manuscript is de-voted to the building and validation of our model, the model's ultimate intent was to understand why the UPR is structured the way it is. Toward that end, we conducted two in silico experiments testing manipulations that were not easily tested experimentally: eliminating eIF2a-mediated translational stimulation of CHOP and GADD34 and ab-lating direct crosstalk between the PERK and ATF6 pathways. Both manipulations pro-vided insight into the ways in which the structure of the UPR governs its responsive-ness. The first suggested that the effect of feedforward translational stimulation of CHOP and GADD34 is not to augment their up-regulation, but rather to ultimately po-tentiate more rapid eIF2a dephosphoryla-tion—i.e., that eIF2a initiates an autoregula-tory negative feedback loop. The second manipulation suggested that a functional consequence of pathway crosstalk might be to make the CHOP-dependent apoptotic limb of the UPR maximally responsive to stress—allowing robust induction of CHOP while simultaneously permitting rapid CHOP loss when stress is alleviated. Experimentally testing these sorts of model predictions would require homologous-directed ge-nome editing to make precise changes in the Bip or Chop promoters, or the Chop and Gadd34 5' untranslated regions, plus identi-fying, selecting, and propagating targeted clones (or generating mutations in stem cells and then differentiating them into fibro-blasts). Thus, experimental validation would be laborious, which highlights one of the major utilities of a computational model: by providing testable predictions, it can help identify experiments that are likely to be worth their time, effort, and cost.

<a id='8adf4970-1d6c-4b2d-8ba7-8b4d84cdb576'></a>

How trustworthy are the predictions
made by our model? The fact that the model
recapitulates essential features of the re-
sponse—and, more importantly, captures at
least in general terms the behavior of the re-
sponse when individual components are ab-
lated—suggests that its predictions are likely

<a id='ff84248f-9789-45c2-92ba-064bb67b7b91'></a>

to be relevant. Of course, there are ways in which the model as currently configured can be refined. One of these is expansion of IRE1/XBP1 signaling. There is little doubt that IRE1 mediates essential UPR responses, particularly in professional secretory cells such as plasma lymphocytes, hepatocytes, and pancreatic acinar cells (van Anken and Braakman, 2005). The apparent lack of a direct contribution of IRE1 signaling to BiP and CHOP expression in MEFs (Figure 1, E and F) led us to minimize its contribution here, but its contribution to response output can be differently weighted when the model is applied to other systems. A more complete IRE1/XBP1 module would

<a id='40824bc7-bed2-45ab-9a1d-4aeb22197931'></a>

Volume 29 June 15, 2018

<a id='68a68215-8c3a-4892-8702-209d68b25b67'></a>

ODE model of UPR regulatory logic

<a id='cc108586-d3be-4ef2-bfc3-00109dbd3698'></a>

1513

<!-- PAGE BREAK -->

<a id='c0d1755e-eb72-432e-aad3-085001586ade'></a>

<::figure: diagram and line graphs::>FIGURE 8: In silico removal of direct crosstalk between ATF6 and PERK pathways. (A) Schematic showing the steps targeted by in silico deletion (red "X"). The diagram shows ATF4, CHOP, ATF6, and BiP in ovals. An arrow goes from ATF4 to CHOP, and from ATF6 to BiP. Dashed lines with red 'X's indicate deleted crosstalk: one from ATF4 to BiP, and another from ATF6 to CHOP. (B-F) Model simulations were run after removal of the contribution of ATF6 to transcription of Chop (ΔA6→c; yellow dashed line), the contribution of ATF4 to Bip transcription (ΔA4→b; green dashed line), or both (linear; magenta dotted line). The legend for the graphs is: -w.t. (blue solid line), -- Δ A6->c (yellow dashed line), --- Δ A4->b (green dashed line), --- linear (magenta dotted line). Selected model outputs for the 2.5-nM condition are shown (B-D). The x-axis for all graphs (B-F) represents time from 0 to 72. A gray shaded region from Y=0 to Y=1 is present in graphs B, C, D, E, F. (B) Graph titled "Unfolded Proteins" with y-axis from 0 to 7. (C) Graph titled "BiP" with y-axis from 0 to 4. (D) Graph titled "CHOP" with y-axis from 0 to 24. Panels E and F graph the ratio of CHOP to BiP during the simulation for 2.5- and 10-nM conditions, respectively. (E) Graph titled "CHOP/BiP, 2.5 nM" with y-axis from 0 to 18. (F) Graph titled "CHOP/BiP, 10 nM" with y-axis from 0 to 48.<::>

<a id='396a4aa3-6056-4895-bf9b-9a0c3ef2f993'></a>

explicitly include synthesis of active XBP1 protein from _Xbp1s_ mRNA, as well as inhibition of that protein by XBP1 translated from unspliced _Xbp1_ mRNA (Yoshida _et al._, 2006).

<a id='b6327da7-20d3-4a37-a7cc-023aeb9d400f'></a>

The model's consideration of unfolded proteins will also ulti- mately need to account for different types of stimuli. The model is currently entrained upon only TG stress and could thus be expected to model other stresses that activate all three limbs of the UPR and that do not require protein synthesis to exert their effects, simply by changing the strength and dynamics of the input stress S(t). Differ- ent stressors, such as inhibition of N-linked glycosylation, ER protein overload, or loading with saturated fatty acids, are likely to result in distinctly different activation profiles of the UPR. In fact, there is in- creasing evidence that the cell senses pharmacological ER stress differently from overexpression of a misfolded protein (Bakunts et al., 2017; Bergmann et al., 2018). Protein synthesis is not explicitly modeled in our system; including it would allow greater flexibility in modeling different stresses. Related to this point, the activity of the RIDD pathway in degrading ER-associated RNAs (and thereby re- ducing ER protein import) could then be modeled directly, rather than indirectly, as in our system.

<a id='509df52c-f9c8-4619-ab0b-20251873c715'></a>

Finally, there are many modulatory components that act upon UPR signaling pathways and that are themselves targets of UPR activation; certainly the response biologically cannot be distilled to just BiP, CHOP, and GADD34. Some of them, such as the putative negative regulator of ATF6 signaling WFS1 (Fonseca et al., 2010), have already been included in attempts to model the UPR (Erguler et al., 2013). While we have excluded such components in the interest of avoiding overspecification, a complete model must ultimately include them. It will be interesting to see where the predictions made by our model, as it is expanded by us or others, agree or diverge with those of Erguler et al. (2013). Although the inclusion of new components would necessitate reparameterization, our existing model provides a jumping-off point for such attempts.

<a id='79a602c0-1acf-4ebf-a48a-6543cc8f2f27'></a>

This model opens many directions of future investigation for the vertebrate UPR research community. The model can be used to run a large variety of simulations to study the UPR under various types of external and internal conditions. The stress function S(t) can be customized to model a variety of different external stress stimuli, including stresses that gradually build in intensity, periodic stress corresponding to repeated drug treatments, cyclical stress of vary-ing intensity following the cell's reproductive cycle or the circadian rhythm, a short spike of ER stress lasting a few minutes to model a sudden insult, or a low-intensity stress of long duration to model a chronic disease. The stress function may also include more complex forms of stress that would be challenging to replicate in vitro.

<a id='459a68b0-d86c-4bbf-96dd-835a46ba417d'></a>

In addition, the model can be used to predict how different cell types, which differ in their basal expression of UPR components, might respond to a given type of stress. For example, while the ex- pression of the ER-resident stress sensors IRE1, PERK, and ATF6 is low in MEFs, these components are abundantly expressed in highly secretory cell types such as pancreas and liver. Does this elevated expression make the system more or less readily activated? And what would be the consequence of having one or two sensors highly expressed but not all three? A related question is which of the pa- rameters modeled here are critical determinants of response output and which are minor modulators—a question that can be addressed by sensitivity analysis, which systematically varies parameters to identify those with the greatest contribution to response output (Turányi, 1990; Helton et al., 2006).

<a id='8ab6bdc7-5831-4781-9d47-fb827be1afa3'></a>

Other areas for exploration can include adding stochasticity, de-
fining parameters to be random variables (i.e., to test which might
be subject to biological regulation), and performing a dynamic
Monte Carlo simulation. Identifying potential alternative steady
states for certain variables through bifurcation analysis is another
direction, in particular to test whether UPR signaling migrates
toward competing bistable states that reflect adaptive versus

<a id='4f5239b1-45ec-4876-8dfb-f5530bd0d147'></a>

1514

<a id='3a14761b-dd4a-4555-94fb-e718d57e7703'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='53585720-2ce2-4266-89ff-80c01c3a34f6'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='cc3ad911-7cad-455e-a87d-218903176d97'></a>

apoptotic programs. Our hope is that this model might be used by the field as a starting point for refinement.

<a id='d9bc1b13-8676-4429-994e-ed8f489f0238'></a>

## MATERIALS AND METHODS
### Cell culture experiments
MEFs were harvested, cultured, and treated as described (Wu et al., 2007) from wild-type animals or from Perk-/- (Harding et al., 2000b), Atf6α-/- (Wu et al., 2007), or Atf4-/- (Hettmann et al., 2000) animals or littermate controls. Ire1-/- MEFs were prepared by in vitro deletion of immortalized MEFs isolated from Ire1fl/fl animals (Zhang et al., 2011) and were a gift from R. J. Kaufman (Sanford Burnham Institute). All animals were highly backcrossed (>10 generations) into the C57BL/6J line; thus wild-type MEFs isolated from any of these strains, or from pure C57BL/6J embryos, are considered effectively isogenic, and any differences in response are most likely due to non-genetic variables. Entrainment data displayed in Supplemental Figure S1 were taken from two independent experiments using two separate wild-type lines. Cells were always used prior to passage number five. Twenty-four hours prior to treatment, cells were plated at 2 × 105 cells per well in six-well dishes. TG and salubrinal were purchased from EMD Millipore (Darmstadt, Germany), dissolved in dimethylsulfoxide (DMSO), and aliquoted and stored at -20°C. TG treatments were carried out by preparing 1000x dilutions from stock in DMSO, adding to media in a tube, and then replacing existing media on cells with stressor-containing media. Quantitative RT-PCR and immunoblot experiments were carried out as described (Rutkowski et al., 2006). Statistical analyses were performed as described in the figure legends. Antibodies were from BD (BiP; cat 610978), Santa Cruz (CHOP; sc-793), or Invitrogen (PelF2α; 44728G). For MTT assays, cells were plated on 96-well dishes using a multi-channel pipette. After resting overnight, media were replaced with fresh media containing stressor. After the desired time in culture with media refreshed daily, MTT reduction was measured using the CellTiter 96 Aqueous One kit (Promega) according to the manufacturer's instructions.

<a id='81484cc6-df9b-44b2-8df4-8697506c653c'></a>

## Model construction and validation
Degradation rate constants were taken from Rutkowski et al. (2006),
which in turn were generated from experimental measurements
(RNA degradation rate constants from experiments in the presence
of the transcription inhibitor actinomycin D, and protein degrada-
tion rate constants from experiments in the presence of the transla-
tion inhibitor cycloheximide). In addition, we set the protein synthe-
sis rate constants at time t = 0 equal to the degradation rate
constants for BiP, CHOP, and GADD34 to ensure that the amounts
of BiP, CHOP, and GADD34 remained at a steady state value of "1"
under unstressed conditions. We also constrained the value of pa-
rameters KUP, KUI in Eqs. 2-3 to ensure that in the absence of stress,
phosphorylated PERK and IRE1 were also at steady state "1." The
remaining parameters were derived by fitting the model solutions to
experimental data.

<a id='36f46ab7-5c66-4c15-a1a6-952a94c3adb6'></a>

All variables in the ODE system (Tables 1 and 2) were unitless and normalized to their steady state values under unstressed conditions. Table 3 shows the definition of each variable as well as baseline values for these quantities under unstressed conditions in terms of actual protein and mRNA quantities. The latter were chosen to capture the appropriate relative proportions of each species (Ron and Walter, 2007).

<a id='e4d88682-878b-450a-ac4b-650bd48d381e'></a>

We used COPASI (Hoops et al., 2006) to solve the model numeri-
cally using its ODE solver LSODAR (Petzold, 1983) and normalized
the initial condition of all variables to 1 to reflect in silico the fact
that up-regulatory and down-regulatory events are expressed in

<a id='b9e1ea41-0c5f-4e1b-a3be-c1dde604026c'></a>

<table><thead><tr><th>Normalized variable</th><th>Quantification</th></tr></thead><tbody><tr><td>_B_ = [BIP] / [BIP-tot]</td><td>—</td></tr><tr><td>_P_p = [PERK-P] / [PERK-P]</td><td>[PERK-P] = 30</td></tr><tr><td>_I_p = [IRE1-P] / [IRE1-P]</td><td>[IRE1-P] = 30</td></tr><tr><td>_U_ = [U] / [U]</td><td>[U] = 100</td></tr><tr><td>_E_p = [elF2α-P] / [elF2α-P]</td><td>[elF2α-P] = 500</td></tr><tr><td>_x_ = [xbp1-sp] / [xbp1-sp]</td><td>[xbp1-sp] = 10</td></tr><tr><td>_A_6 = [ATF6-cl] / [ATF6-cl]</td><td>[ATF6-cl] = 100</td></tr><tr><td>_A_4 = [ATF4] / [ATF4]</td><td>[ATF4] = 100</td></tr><tr><td>_b_ = [Bip] / [Bip]</td><td>[Bip] = 1600</td></tr><tr><td>_B_tot = [BIP-tot] / [BIP-tot]</td><td>[BIP-tot] = 200,000</td></tr><tr><td>_c_ = [Chop] / [Chop]</td><td>[Chop] = 100</td></tr><tr><td>_C_ = [CHOP] / [CHOP]</td><td>[CHOP] = 100</td></tr><tr><td>_g_ = [Gadd34] / [Gadd34]</td><td>[Gadd34] = 100</td></tr><tr><td>_G_ = [GADD34] / [GADD34]</td><td>[GADD34] = 100<br>[PERK-tot] = (1/_f_) [PERK-P] = 1500<br>[IRE1-tot] = (1/_f_i) [IRE1-P] = 3000<br>[xbp1-tot] = _x_tot [xbp1-sp] = 160<br>[elF2α-tot] = _E_tot [elF2α-P] = 10,000<br>[ATF6-tot] = _A_6tot [ATF6-cl] = 1500</td></tr></tbody></table>TABLE 3: Model variables in terms of actual protein and mRNA steady state quantifications under unstressed conditions.

<a id='eed82afd-cc24-4af8-a422-084d4df8e87d'></a>

experimental data as fold changes. The units of the simulated time were minutes. The input stress was described as a rate function S(t) measured in [min¯¹] and assumed here to be constant, with the difference between the unstressed condition and the 2.5 and 10 nM TG conditions being S(t) = 0,S(t) = 2, and S(t) = 8 [min¯¹], respectively. We then used S(t) = 4 [min¯¹] to simulate stress at 5 nM TG (Supplemental Figure S5O).

<a id='a1d4574e-731d-4115-9405-6e20df27dc9a'></a>

In silico deletions were created as follows: for PERK deletion,
variable P<sub>p</sub> was set to P<sub>p</sub> = 0; for IRE1 deletion, I<sub>p</sub> = I<sub>p</sub>* = 0; for
ATF6 deletion, A6<sub>tot</sub> = 0 and A6* = 0; for ATF4 deletion, A4* = 0 and
γ = 0. For GADD34 deletion, g* = G* = 0 and dg/dt = 0, dG/dt = 0
in Eqs. 13 and 14; for deletion of the feedforward loop connecting
eIF2α phosphorylation to CHOP and GADD34 translation, k<sub>t,C</sub> and
k<sub>t,G</sub> = 0; for ΔA6→c simulations, K<sub>c4</sub> and K<sub>th4c</sub> = 0; for ΔA4→b, α<sub>A4</sub>,
K<sub>th6</sub>, and K<sub>b6</sub> = 0. The linear model incorporated both sets of
changes. The COPASI file, allowing the model to be run and ma-
nipulated by others, is included in the Supplemental Materials and
is also deposited in the BioModels Database under model ID#
MODEL1803300000 (www.ebi.ac.uk/biomodels/).

<a id='a6e73894-20d9-46bb-980c-8bc1e7ebfdc7'></a>

## ACKNOWLEDGMENTS
We thank R. J. Kaufman (Sanford Burnham Research Institute) for
providing mice from which _Atf6_−/− and _Atf4_−/− MEFs were derived
and for _Ire1_−/− and control MEFs. We thank D. Ron (University of

<a id='75e5e093-40ac-476d-b88d-2f2ef3e1b67c'></a>

Volume 29 June 15, 2018

<a id='ded00055-943d-4425-bbb6-96f0b4d8cc8d'></a>

ODE model of UPR regulatory logic

<a id='16ac04cb-2755-416a-9c48-3cfbf108efb3'></a>

1515

<!-- PAGE BREAK -->

<a id='e659ba94-1306-456a-b3a7-b654d04c58c1'></a>

Cambridge) for _Perk_–/– mice. We also thank A. H. Elcock, A. J. Dupuy, W. S. Moye–Rowley, and C. D. Sigmund for stimulating discussions. Funding sources included National Institutes of Health R01 GM115424 (D.T.R.) and T32 GM067795 (J.A.G.) and National Science Foundation 1029082 (R.C.).

<a id='85aadc62-d768-4163-b461-596dec3c5f46'></a>

REFERENCES
Adachi Y, Yamamoto K, Okada T, Yoshida H, Harada A, Mori K (2008). ATF6
Is a transcription factor specializing in the regulation of quality control
proteins in the endoplasmic reticulum. Cell Struct Funct 33, 75–89.
Bakunts A, Orsi A, Vitale M, Cattaneo A, Lari F, Tade L, Sitia R, Raimondi A,
Bachi A, van Anken E (2017). Ratiometric sensing of BiP-client versus
BiP levels by the unfolded protein response determines its signaling
amplitude. Elife 6, e27518.
Bergmann TJ, Fregno I, Fumagalli F, Rinaldi A, Bertoni F, Boersema PJ,
Picotti P, Molinari M (2018). Chemical stresses fail to mimic the unfolded
protein response resulting from luminal load with unfolded polypep-
tides. J Biol Chem, doi:10.1074/jbc.RA117.001484.
Bertolotti A, Zhang Y, Hendershot LM, Harding HP, Ron D (2000). Dynamic
interaction of BiP and ER stress transducers in the unfolded-protein
response. Nat Cell Biol 2, 326–332.
Boyce M, Bryant KF, Jousse C, Long K, Harding HP, Scheuner D, Kaufman
RJ, Ma D, Coen DM, Ron D, et al. (2005). A selective inhibitor of
eIF2alpha dephosphorylation protects cells from ER stress. Science 307,
935–939.
Calfon M, Zeng H, Urano F, Till JH, Hubbard SR, Harding HP, Clark SG, Ron
D (2002). IRE1 couples endoplasmic reticulum load to secretory capacity
by processing the XBP-1 mRNA. Nature 415, 92–96.
Curtu R, Diedrichs D (2010). Small-scale modeling approach and circuit wir-
ing of the unfolded protein response in mammalian cells. Adv Exp Med
Biol 680, 261–274.
Dey S, Baird TD, Zhou D, Palam LR, Spandau DF, Wek RC (2010). Both
transcriptional regulation and translational control of ATF4 are central to
the integrated stress response. J Biol Chem 285, 33165–33174.
Erguler K, Pieri M, Deltas C (2013). A mathematical model of the unfolded
protein stress response reveals the decision mechanism for recovery,
adaptation and apoptosis. BMC Syst Biol 7, 16.
Fonseca SG, Ishigaki S, Oslowski CM, Lu S, Lipson KL, Ghosh R, Hayashi E,
Ishihara H, Oka Y, Permutt MA, et al. (2010). Wolfram syndrome 1 gene
negatively regulates ER stress signaling in rodent and human cells. J Clin
Invest 120, 744–755.
Gao J, Ishigaki Y, Yamada T, Kondo K, Yamaguchi S, Imai J, Uno K,
Hasegawa Y, Sawada S, Ishihara H, et al. (2011). Involvement of endo-
plasmic stress protein C/EBP homologous protein in arteriosclerosis
acceleration with augmented biological stress responses. Circulation
124, 830–839.
Gardner BM, Pincus D, Gotthardt K, Gallagher CM, Walter P (2013). Endo-
plasmic reticulum stress sensing in the unfolded protein response. Cold
Spring Harb Perspect Biol 5, a013169.
Gething MJ (1999). Role and regulation of the ER chaperone BiP. Semin Cell
Dev Biol 10, 465–472.
Gomez JA, Rutkowski DT (2016). Experimental reconstitution of chronic ER
stress in the liver reveals feedback suppression of BiP mRNA expression.
Elife 5, e20390.
Han D, Lerner AG, Vande Walle L, Upton JP, Xu W, Hagen A, Backes BJ,
Oakes SA, Papa FR (2009). IRE1alpha kinase activation modes control
alternate endoribonuclease outputs to determine divergent cell fates.
Cell 138, 562–575.
Han J, Back SH, Hur J, Lin YH, Gildersleeve R, Shan J, Yuan CL, Krokowski
D, Wang S, Hatzoglou M, et al. (2013). ER-stress-induced transcriptional
regulation increases protein synthesis leading to cell death. Nat Cell Biol
15, 481–490.
Harding HP, Novoa I, Zhang Y, Zeng H, Wek R, Schapira M, Ron D (2000a).
Regulated translation initiation controls stress-induced gene expression
in mammalian cells. Mol Cell 6, 1099–1108.
Harding HP, Zhang Y, Bertolotti A, Zeng H, Ron D (2000b). Perk is essential
for translational regulation and cell survival during the unfolded protein
response. Mol Cell 5, 897–904.
Harding HP, Zhang Y, Ron D (1999). Protein translation and folding are
coupled by an endoplasmic-reticulum-resident kinase. Nature 397,
271–274.
Harding HP, Zhang Y, Zeng H, Novoa I, Lu PD, Calfon M, Sadri N, Yun C,
Popko B, Paules R, et al. (2003). An integrated stress response regulates

<a id='c8572c27-c11e-405f-9178-0fd609ad75fd'></a>

amino acid metabolism and resistance to oxidative stress. Mol Cell 11, 619-633.
Haze K, Yoshida H, Yanagi H, Yura T, Mori K (1999). Mammalian transcription factor ATF6 is synthesized as a transmembrane protein and activated by proteolysis in response to endoplasmic reticulum stress. Mol Biol Cell 10, 3787-3799.
Helton JC, Johnson JD, Sallaberry CJ, Storlie CB (2006). Survey of sampling-based methods for uncertainty and sensitivity analysis. Reliab Eng Sys Safety 91, 1175-1209.
Hettmann T, Barton K, Leiden JM (2000). Microphthalmia due to p53- mediated apoptosis of anterior lens epithelial cells in mice lacking the CREB-2 transcription factor. Dev Biol 222, 110-123.
Hetz C (2012). The unfolded protein response: controlling cell fate decisions under ER stress and beyond. Nat Rev Mol Cell Biol 13, 89-102.
Hollien J, Lin JH, Li H, Stevens N, Walter P, Weissman JS (2009). Regulated Ire1-dependent decay of messenger RNAs in mammalian cells. J Cell Biol 186, 323-331.
Hollien J, Weissman JS (2006). Decay of endoplasmic reticulum-local- ized mRNAs during the unfolded protein response. Science 313, 104-107.
Hoops S, Sahle S, Gauges R, Lee C, Pahle J, Simus N, Singhal M, Xu L, Mendes P, Kummer U (2006). COPASI—a Complex PAthway Simulator. Bioinformatics 22, 3067-3074.
Kassenbrock CK, Garcia PD, Walter P, Kelly RB (1988). Heavy-chain binding protein recognizes aberrant polypeptides translocated in vitro. Nature 333, 90-93.
Kim HD, Shay T, O'Shea EK, Regev A (2009). Transcriptional regulatory circuits: predicting numbers from alphabets. Science 325, 429-432.
Lee AH, Iwakoshi NN, Glimcher LH (2003). XBP-1 regulates a subset of en- doplasmic reticulum resident chaperone genes in the unfolded protein response. Mol Cell Biol 23, 7448-7459.
Lee K, Tirasophon W, Shen X, Michalak M, Prywes R, Okada T, Yoshida H, Mori K, Kaufman RJ (2002). IRE1-mediated unconventional mRNA splicing and S2P-mediated ATF6 cleavage merge to regulate XBP1 in signaling the unfolded protein response. Genes Dev 16, 452-466.
Lee YY, Cevallos RC, Jan E (2009). An upstream open reading frame regulates translation of GADD34 during cellular stresses that induce elF2alpha phosphorylation. J Biol Chem 284, 6661-6673.
Li G, Mongillo M, Chin KT, Harding H, Ron D, Marks AR, Tabas I (2009). Role of ERO1-alpha-mediated stimulation of inositol 1,4,5-triphosphate receptor activity in endoplasmic reticulum stress-induced apoptosis. J Cell Biol 186, 783-792.
Lu PD, Jousse C, Marciniak SJ, Zhang Y, Novoa I, Scheuner D, Kaufman RJ, Ron D, Harding HP (2004). Cytoprotection by pre-emptive condi- tional phosphorylation of translation initiation factor 2. EMBO J 23, 169-179.
Luo S, Baumeister P, Yang S, Abcouwer SF, Lee AS (2003). Induction of Grp78/BiP by translational block: activation of the Grp78 promoter by ATF4 through an upstream ATF/CRE site independent of the endoplas- mic reticulum stress elements. J Biol Chem 278, 37375-37385.
Ma Y, Brewer JW, Diehl JA, Hendershot LM (2002). Two distinct stress signaling pathways converge upon the CHOP promoter during the mammalian unfolded protein response. J Mol Biol 318, 1351-1365.
Ma Y, Hendershot LM (2003). Delineation of a negative feedback regula- tory loop that controls protein translation during endoplasmic reticulum stress. J Biol Chem 278, 34864-34873.
Marciniak SJ, Yun CY, Oyadomari S, Novoa I, Zhang Y, Jungreis R, Nagata K, Harding HP, Ron D (2004). CHOP induces death by promoting protein synthesis and oxidation in the stressed endoplasmic reticulum. Genes Dev 18, 3066-3077.
Morris JA, Dorner AJ, Edwards CA, Hendershot L, Kaufman RJ (1997). Im- munoglobulin binding protein (BiP) function is required to protect cells from endoplasmic reticulum stress but is not required for the secretion of selective proteins. J Biol Chem 272, 4327-4334.
Namba T, Tanaka K, Ito Y, Ishihara T, Hoshino T, Gotoh T, Endo M, Sato K, Mizushima T (2009). Positive role of CCAAT/enhancer-binding protein homologous protein, a transcription factor involved in the endoplasmic reticulum stress response in the development of colitis. Am J Pathol 174, 1786-1798.
Nishikawa S, Brodsky JL, Nakatsukasa K (2005). Roles of molecular chaper- ones in endoplasmic reticulum (ER) quality control and ER-associated degradation (ERAD). J Biochem 137, 551-555.
Novoa I, Zeng H, Harding HP, Ron D (2001). Feedback inhibition of the unfolded protein response by GADD34-mediated dephosphorylation of elF2alpha. J Cell Biol 153, 1011-1022.

<a id='18587e2f-2b12-4c34-9560-184ef025979c'></a>

1516

<a id='81cb7bb9-4f46-4bc2-bc8a-79ba77cb4945'></a>

D. R. Diedrichs, J. A. Gomez, et al.

<a id='166c8ded-ccd6-4460-a8bb-316ef5c454f6'></a>

Molecular Biology of the Cell

<!-- PAGE BREAK -->

<a id='0a186eed-03fb-46c9-b95c-a7820aff3e4e'></a>

Novoa I, Zhang Y, Zeng H, Jungreis R, Harding HP, Ron D (2003). Stress-induced gene expression requires programmed recovery from translational repression. EMBO J 22, 1180-1187.
Oyadomari S, Koizumi A, Takeda K, Gotoh T, Akira S, Araki E, Mori M (2002). Targeted disruption of the Chop gene delays endoplasmic reticulum stress-mediated diabetes. J Clin Invest 109, 525-532.
Palam LR, Baird TD, Wek RC (2011). Phosphorylation of eIF2 facilitates ribosomal bypass of an inhibitory upstream ORF to enhance CHOP translation. J Biol Chem 286, 10939-10949.
Parmar VM, Schröder M (2012). Sensing endoplasmic reticulum stress. Adv Exp Med Biol 738, 153-168.
Pennuto M, Tinelli E, Malaguti M, Del Carro U, D'Antonio M, Ron D, Quattrini A, Feltri ML, Wrabetz L (2008). Ablation of the UPR-mediator CHOP restores motor function and reduces demyelination in Charcot-Marie-Tooth 1B mice. Neuron 57, 393-405.
Petzold L (1983). Automatic selection of methods for solving stiff and nonstiff systems of ordinary differential equations. SIAM J Sci Comput 4, 136-148.
Puthalakath H, O'Reilly LA, Gunn P, Lee L, Kelly PN, Huntington ND, Hughes PD, Michalak EM, McKimm-Breschkin J, Motoyama N, et al. (2007). ER stress triggers apoptosis by activating BH3-only protein Bim. Cell 129, 1337-1349.
Ron D, Walter P (2007). Signal integration in the endoplasmic reticulum unfolded protein response. Nat Rev Mol Cell Biol 8, 519-529.
Rutkowski DT, Arnold SM, Miller CN, Wu J, Li J, Gunnison KM, Mori K, Sadighi Akha AA, Raden D, Kaufman RJ (2006). Adaptation to ER stress is mediated by differential stabilities of pro-survival and pro-apoptotic mRNAs and proteins. PLoS Biol 4, e374.
Scheuner D, Song B, McEwen E, Liu C, Laybutt R, Gillespie P, Saunders T, Bonner-Weir S, Kaufman RJ (2001). Translational control is required for the unfolded protein response and in vivo glucose homeostasis. Mol Cell 7, 1165-1176.
Shen J, Chen X, Hendershot L, Prywes R (2002). ER stress regulation of ATF6 localization by dissociation of BiP/GRP78 binding and unmasking of Golgi localization signals. Dev Cell 3, 99-111.
Shen X, Ellis RE, Lee K, Liu CY, Yang K, Solomon A, Yoshida H, Morimoto R, Kurnit DM, Mori K, et al. (2001). Complementary signaling pathways regulate the unfolded protein response and are required for C. elegans development. Cell 107, 893-903.
Song B, Scheuner D, Ron D, Pennathur S, Kaufman RJ (2008). Chop deletion reduces oxidative stress, improves beta cell function, and promotes cell survival in multiple mouse models of diabetes. J Clin Invest 118, 3378-3389.
Tabas I, Ron D (2011). Integrating the mechanisms of apoptosis induced by endoplasmic reticulum stress. Nat Cell Biol 13, 184-190.
Teske BF, Wek SA, Bunpo P, Cundiff JK, McClintick JN, Anthony TG, Wek RC (2011). The eIF2 kinase PERK and the integrated stress response

<a id='be63ca99-8d54-4220-ac07-4b4d64378c57'></a>

facilitate activation of ATF6 during endoplasmic reticulum stress. Mol Biol Cell 22, 4390-4405.
Thorp E, Li G, Seimon TA, Kuriakose G, Ron D, Tabas I (2009). Reduced apoptosis and plaque necrosis in advanced atherosclerotic lesions of Apoe-/- and Ldlr-/- mice lacking CHOP. Cell Metab 9, 474-481.
Trusina A, Papa FR, Tang C (2008). Rationalizing translation attenuation in the network architecture of the unfolded protein response. Proc Natl Acad Sci USA 105, 20280-20285.
Trusina A, Tang C (2010). The unfolded protein response and translation attenuation: a modelling approach. Diabetes Obes Metab 12(Suppl 2), 27-31.
Turányi T (1990). Sensitivity analysis of complex kinetic systems. Tools and applications. J Math Chem 5, 203-248.
van Anken E, Braakman I (2005). Endoplasmic reticulum stress and the making of a professional secretory cell. Crit Rev Biochem Mol Biol 40, 269-283.
Walter P, Ron D (2011). The unfolded protein response: from stress pathway to homeostatic regulation. Science 334, 1081-1086.
Wong WL, Brostrom MA, Kuznetsov G, Gmitter-Yellen D, Brostrom CO (1993). Inhibition of protein synthesis and early protein processing by thapsigargin in cultured cells. Biochem J 289(Pt 1), 71-79.
Wu J, Rutkowski DT, Dubois M, Swathirajan J, Saunders T, Wang J, Song B, Yau GD, Kaufman RJ (2007). ATF6alpha optimizes long-term endoplasmic reticulum function to protect cells from chronic stress. Dev Cell 13, 351-364.
Yamamoto K, Sato T, Matsui T, Sato M, Okada T, Yoshida H, Harada A, Mori K (2007). Transcriptional induction of mammalian ER quality control proteins is mediated by single or combined action of ATF6alpha and XBP1. Dev Cell 13, 365-376.
Yoshida H, Matsui T, Yamamoto A, Okada T, Mori K (2001). XBP1 mRNA is induced by ATF6 and spliced by IRE1 in response to ER stress to produce a highly active transcription factor. Cell 107, 881-891.
Yoshida H, Okada T, Haze K, Yanagi H, Yura T, Negishi M, Mori K (2000). ATF6 activated by proteolysis binds in the presence of NF-Y (CBF) directly to the cis-acting element responsible for the mammalian unfolded protein response. Mol Cell Biol 20, 6755-6767.
Yoshida H, Oku M, Suzuki M, Mori K (2006). pXBP1(U) encoded in XBP1 pre-mRNA negatively regulates unfolded protein response activator pXBP1(S) in mammalian ER stress response. J Cell Biol 172, 565-575.
Zhang K, Wang S, Malhotra J, Hassler JR, Back SH, Wang G, Chang L, Xu W, Miao H, Leonardi R, et al. (2011). The unfolded protein response transducer IRE1 alpha prevents ER stress-induced hepatic steatosis. EMBO J 30, 1357-1375.
Zinszner H, Kuroda M, Wang X, Batchvarova N, Lightfoot RT, Remotti H, Stevens JL, Ron D (1998). CHOP is implicated in programmed cell death in response to impaired function of the endoplasmic reticulum. Genes Dev 12, 982-995.

<a id='36221de6-80bb-4f67-b4c2-2c7c1ee708f2'></a>

Volume 29 June 15, 2018

<a id='c67a7af5-5075-44bb-bac8-a7376af7a5fb'></a>

ODE model of UPR regulatory logic

<a id='a005b58f-c8ba-4758-a47b-216ce0139455'></a>

1517