<a id='23e7e853-5858-45ae-8ce8-57712d6889f9'></a>

<::logo: [JCB]Article
The logo features the letters "JCB" in a light gray font, with the word "Article" in bold black text next to it.::>

<a id='d48614a1-4442-4313-a215-9a5842206a67'></a>

Mathematical model of the morphogenesis checkpoint
in budding yeast

<a id='a20a5713-687e-457e-9bc6-68c6f51db4ec'></a>

Andrea Ciliberto,<sup>1</sup> Bela Novak,<sup>2,3</sup> and John J. Tyson<sup>1</sup>
<sup>1</sup>Department of Biology, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061
<sup>2</sup>Molecular Network Dynamics Research Group of Hungarian Academy of Sciences and <sup>3</sup>Department of Agricultural Chemical Technology, Budapest University of Technology and Economics, H-1521 Budapest, Hungary

<a id='99df3996-6e79-4024-8602-8086d1d482a6'></a>

The morphogenesis checkpoint in budding yeast delays progression through the cell cycle in response to stimuli that prevent bud formation. Central to the checkpoint mechanism is Swe1 kinase: normally inactive, its activation halts cell cycle progression in G2. We propose a molecular network for Swe1 control, based on published observations of budding yeast and analogous control signals in fission yeast. The proposed Swe1 network is merged with a model of cyclin-dependent kinase regulation, converted into a set of differential equations and studied by numerical

<a id='9a4eac6c-2c62-4c49-9aae-bada48b1ad10'></a>

simulation. The simulations accurately reproduce the
phenotypes of a dozen checkpoint mutants. Among other
predictions, the model attributes a new role to Hsl1, a kinase
known to play a role in Swe1 degradation: Hsl1 must also be
indirectly responsible for potent inhibition of Swe1 activity.
The model supports the idea that the morphogenesis
checkpoint, like other checkpoints, raises the cell size
threshold for progression from one phase of the cell cycle
to the next.

<a id='a2a5a16f-3dca-4d42-bdc0-df50dcb72a82'></a>

# Introduction
During the cell division cycle, a cell first replicates its hereditary material (S phase) and then segregates the chromosomes to the newborn daughter cells (mitosis). Alternation of mitosis and DNA replication is necessary for the cycle to be successful: two consecutive rounds of mitosis cause lethal mis-segregation of the genome, and successive rounds of DNA synthesis are usually disadvantageous (Enoch and Nurse, 1991). In molecular terms, the proper order of the events is ensured by the alternation of different Cdk activities (Morgan 1995).
Cdk activities are subject to multiple controls: they are activated by binding to cyclins, and they can be inhibited by tyrosine phosphorylation or by stoichiometric binding with a Cdk inhibitor (Sicl in budding yeast). Waves of different classes of cyclins alternate during the cycle, and the resulting Cdk–cyclin complexes are responsible for various cell cycle events. In budding yeast (where the cell-cycle regulating Cdk is Cdc28), the first complex to arise during the cycle is Cdc28–Cln3, which senses growth of the cell in G1, followed by Cdc28–Cln1 and Cdc28–Cln2, which are responsible for bud initiation and spindle pole body duplication. They are

<a id='69b5e93b-650a-4a02-9ebe-356de82e8775'></a>

The online version of this article contains supplemental material.
Address correspondence to John J. Tyson, Dept. of Biology, M.C. 0406,
Virginia Polytechnic Institute and State University, Blacksburg, VA
24061. Tel.: (540) 231-4662. Fax: (540) 231-9307. email: tyson@vt.edu
Key words: molecular networks; dynamical systems; cell cycle; size
control; Swe1 kinase

<a id='08f6d92b-61cd-4889-b973-e435506eadcd'></a>

followed by Cdc28–Clb5 and Cdc28–Clb6, which are
primarily responsible for S phase, and finally by the mitotic
complexes Cdc28–Clb1 and Cdc28–Clb2.

<a id='b88d205b-b8f7-47e2-8da4-afe540a949de'></a>

The main transitions of the cell division process—the onset of DNA replication (Start), entry into mitosis (G2-M transition), and exit from mitosis—are controlled by surveillance mechanisms, also known as checkpoints (Hartwell and Weinert, 1989). The G2-M checkpoint plays a major role in fission yeast (_Schizosaccharomyces pombe_), where it forestalls mitosis until the cell grows to a critical size and properly replicates its DNA (Nurse, 1999). The molecular events which control this transition are the inhibitory phosphorylation of tyrosine-15 of Cdc2 (the fission yeast homologue of Cdc28), executed by the protein kinase Wee1, and the activating dephosphorylation of this site, catalyzed by the phosphatase Cdc25. If DNA is damaged or not properly replicated, the checkpoint is engaged, Cdc2 is phosphorylated on tyrosine-15, and cell cycle progression is halted. The inhibitory phosphorylation is relieved when DNA is fully replicated or the damage is repaired (Enoch and Nurse, 1991).

<a id='67f6dd64-c1ff-40d9-8d2d-7cf4904a4b29'></a>

Budding yeast contains homologues of Wee1 and Cdc25,
known respectively as Swe1 kinase (Booher et al., 1993) and
Mih1 phosphatase (Russell et al., 1989). But in budding
yeast, Mih1 and Swe1 are not used to check cell size, nor are

<a id='ad059f27-e49f-4a5a-b516-2189c73fa6c8'></a>

Abbreviations used in this paper: MPF, M-phase promoting factor; ND, nuclear division.

<a id='d9884518-b6e1-45f0-b7fc-7d26f5e5faea'></a>

© The Rockefeller University Press, 0021-9525/2003/12/1243/12 $8.00
The Journal of Cell Biology, Volume 163, Number 6, December 22, 2003 1243–1254
http://www.jcb.org/cgi/doi/10.1083/jcb.200306139

<a id='f577cb83-d68d-4885-9206-ec1058e6d0b6'></a>

1243

<a id='ed760db9-73e1-4aac-84e3-b6c46bacfca7'></a>

The Journal of Cell Biology

<!-- PAGE BREAK -->

<a id='f0a51304-420e-4c26-98c5-6660cabf594b'></a>

1244 The Journal of Cell Biology | Volume 163, Number 6, 2003

<a id='1d9c6ebe-388e-431b-a6c4-262781c1361b'></a>

Table 1. Comparing experiments and simulations
<table id="1-1">
<tr><td id="1-2"></td><td id="1-3"></td><td id="1-4" colspan="2"></td><td id="1-5" colspan="6">Nuclear division time</td></tr>
<tr><td id="1-6"></td><td id="1-7"></td><td id="1-8" colspan="2">Cell cycle properties</td><td id="1-9" colspan="2">α-factor</td><td id="1-a" colspan="2">cdc24ts α-factor</td><td id="1-b" colspan="2">cdc24ts elutriation</td></tr>
<tr><td id="1-c">Genotypes</td><td id="1-d">Parameters</td><td id="1-e">E</td><td id="1-f">S</td><td id="1-g">E</td><td id="1-h">S</td><td id="1-i">E</td><td id="1-j">S</td><td id="1-k">E</td><td id="1-l">S</td></tr>
<tr><td id="1-m"></td><td id="1-n"></td><td id="1-o"></td><td id="1-p"></td><td id="1-q">min</td><td id="1-r">min</td><td id="1-s">min</td><td id="1-t">min</td><td id="1-u">min</td><td id="1-v">min</td></tr>
<tr><td id="1-w">Wild type</td><td id="1-x"></td><td id="1-y"></td><td id="1-z">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-A">65-75a,b</td><td id="1-B">79</td><td id="1-C">135-160ª,b</td><td id="1-D">150</td><td id="1-E">250ª</td><td id="1-F">225</td></tr>
<tr><td id="1-G">swe1Δ</td><td id="1-H">kS,swe = 0</td><td id="1-I">same size and cycle as wild typec</td><td id="1-J">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-K"></td><td id="1-L">79</td><td id="1-M">80a,d</td><td id="1-N">79</td><td id="1-O">145a</td><td id="1-P">131</td></tr>
<tr><td id="1-Q">mih1Δ</td><td id="1-R">kS,mih1 = 0</td><td id="1-S">G2 delay and cells 15% bigger than wild typec,e</td><td id="1-T">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-U">80a</td><td id="1-V">82</td><td id="1-W">G2 blocka</td><td id="1-X">G2 block</td><td id="1-Y">&gt;300a</td><td id="1-Z">G2 block</td></tr>
<tr><td id="1-10">hsl1Δ</td><td id="1-11">khsl1 = 0</td><td id="1-12">same as wtd</td><td id="1-13">CT = 139 mab = 0.8 mad = 1.7</td><td id="1-14"></td><td id="1-15">81</td><td id="1-16">165d</td><td id="1-17">171</td><td id="1-18"></td><td id="1-19">255</td></tr>
<tr><td id="1-1a">mih1Δ hsl1Δ</td><td id="1-1b">khsl1 = 0 kS,mih1 = 0</td><td id="1-1c">G2 arrestd</td><td id="1-1d">G2 block</td><td id="1-1e"></td><td id="1-1f">G2 block</td><td id="1-1g"></td><td id="1-1h">G2 block</td><td id="1-1i"></td><td id="1-1j">G2 block</td></tr>
<tr><td id="1-1k">mih1Δ swe1Δ</td><td id="1-1l">kS,swe = 0 kS,mih1 = 0</td><td id="1-1m">same size and cycle as wild typed</td><td id="1-1n">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-1o"></td><td id="1-1p">79</td><td id="1-1q"></td><td id="1-1r">79</td><td id="1-1s"></td><td id="1-1t">131</td></tr>
<tr><td id="1-1u">clb2Δ mih1Δ</td><td id="1-1v">ks,clb2 = 0.005 Kmih1 = 0</td><td id="1-1w">elongated cells, G2 delay</td><td id="1-1x">CT = 139 mab = 2.1 mad = 4.2</td><td id="1-1y"></td><td id="1-1z">105</td><td id="1-1A"></td><td id="1-1B">G2 block</td><td id="1-1C"></td><td id="1-1D">G2 block</td></tr>
<tr><td id="1-1E">clb2Δ hsl1Δ</td><td id="1-1F">ks,clb2 = 0.005 Khsl1 = 0</td><td id="1-1G">elongated cells (longer than clb2Δ mih1Δ), G2 delay</td><td id="1-1H">CT = 139 mab = 2.5 mad = 5.1</td><td id="1-1I"></td><td id="1-1J">105</td><td id="1-1K"></td><td id="1-1L">G2 block</td><td id="1-1M"></td><td id="1-1N">G2 block</td></tr>
<tr><td id="1-1O">GAP-SWE1</td><td id="1-1P">ks,swe = 0 ks,sweC = 0.001</td><td id="1-1Q"></td><td id="1-1R">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-1S">75ª</td><td id="1-1T">79</td><td id="1-1U">118ª</td><td id="1-1V">118</td><td id="1-1W"></td><td id="1-1X">163</td></tr>
<tr><td id="1-1Y">GAL-SWE1</td><td id="1-1Z">ks,swe = 0 ks,swec = 2.5</td><td id="1-20">G2 block</td><td id="1-21">G2 block</td><td id="1-22"></td><td id="1-23">G2 block</td><td id="1-24"></td><td id="1-25">G2 block</td><td id="1-26"></td><td id="1-27">G2 block</td></tr>
<tr><td id="1-28">swe1-SWE1</td><td id="1-29">ks.swe 0.00125</td><td id="1-2a"></td><td id="1-2b">CT = 139</td><td id="1-2c"></td><td id="1-2d"></td><td id="1-2e"></td><td id="1-2f"></td><td id="1-2g"></td><td id="1-2h"></td></tr>
<tr><td id="1-2i">MIH1-MIH1</td><td id="1-2j"></td><td id="1-2k"></td><td id="1-2l">mab = 0.8 mad = 1.6</td><td id="1-2m"></td><td id="1-2n">79</td><td id="1-2o"></td><td id="1-2p">94</td><td id="1-2q">190ª</td><td id="1-2r">150</td></tr>
<tr><td id="1-2s">SWE1-SWE1 MIH1-mih1</td><td id="1-2t">k_s,mih1 = 0.05</td><td id="1-2u"></td><td id="1-2v">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-2w"></td><td id="1-2x">79</td><td id="1-2y"></td><td id="1-2z">299</td><td id="1-2A">385a</td><td id="1-2B">368</td></tr>
<tr><td id="1-2C">SWE1-2X</td><td id="1-2D">k_s,swe = 0.005</td><td id="1-2E">same as wt8</td><td id="1-2F">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-2G"></td><td id="1-2H">79</td><td id="1-2I">330d</td><td id="1-2J">381</td><td id="1-2K"></td><td id="1-2L">445</td></tr>
<tr><td id="1-2M">SWE1-4X</td><td id="1-2N">k_s, swe = 0.01</td><td id="1-2O"></td><td id="1-2P">CT = 139 mab = 0.8 mad = 1.6</td><td id="1-2Q"></td><td id="1-2R">79</td><td id="1-2S">&gt;300d</td><td id="1-2T">&gt;300</td><td id="1-2U"></td><td id="1-2V">G2 block</td></tr>
</table>

<a id='793ce581-74aa-45f3-bb45-e7776a37c106'></a>

The first column catalogs genotypes and changes of parameter values compared to the wild type (Table S2). In the second column, experimental (E) observations of exponentially growing cells are compared with simulated (S) cell cycles in terms of mass at division (mad), mass at birth (mab), and cycle time (CT, min). The third column, comprised of three sub-columns, shows a comparison between experimental nuclear division (ND) times and simulations. In the sub-columns are collected ND data measured in different conditions: in cells grown after synchronization by α-factor arrest and release, in cells synchronized with the same method and grown in cdc24ts mutants at restrictive temperature (same parameters as wild type, except for k'mih = 0.5, k''mih = 0.05, and khsl1 = 0, i.e., checkpoint engaged), and finally in cells synchronized by elutriation and grown in cdc24ts mutants at restrictive temperature.

aSia et al., 1996.
bSia et al., 1998.
cBooher et al., 1993.
dMcMillan et al., 1999a; ND in SWE1-2X extrapolated from Fig. 3.
eRussell et al., 1989.
fLew, D.J., personal communication.
gMcMillan et al., 1998.

<a id='21df0913-a73f-4f7c-9c78-039913591c68'></a>

they involved in monitoring DNA replication, as evidenced
by the fact that cells containing a mutant form of Cdc28
lacking the tyrosine phosphorylation site are still perfectly
viable in the presence of inhibitors of DNA synthesis (Amon
et al., 1992; Sorger and Murray, 1992). Recently, Lew and
coworkers have shown in an elegant series of papers that
these tyrosine phosphorylation–dephosphorylation reactions
in budding yeast are involved in a different kind of check-

<a id='7621ff03-1ca8-42ca-805c-5f29e725a921'></a>

point, called the morphogenesis checkpoint (for review see Lew, 2000). This surveillance mechanism halts cell cycle progression when bud formation is impaired, which is a plausible event for yeast cells growing in natural conditions because several external stimuli (such as heat shock and osmotic shock) are able to arrest or delay the formation of a bud (Sia et al., 1998). By arresting or delaying cell cycle progression, the morphogenesis checkpoint prevents formation

<!-- PAGE BREAK -->

<a id='2914a1dd-5967-468e-b77a-cb4706f57c38'></a>

Mathematical model of the morphogenesis checkpoint | Ciliberto et al.

<a id='b381160c-e14b-4bd3-9524-a74d18d71f19'></a>

1245

<a id='e0809b10-2b6a-45ec-b0d6-65b2548444c3'></a>

<::figure: flowchart::>Figure 1. Molecular mechanism of the cell-cycle engine in budding yeast. The diagram illustrates a complex regulatory network. At the top left, 'Mass' input activates 'SBF' to 'SBF*', which in turn leads to the formation of 'Cdc28' bound to 'Cln'. 'AA' (amino acids) also contributes to the system. The central component is 'Cdc28' complexed with 'Clb2'. This 'Cdc28-Clb2' complex activates 'Mcm1' to 'Mcm1*' (an asterisk denotes a more active form). 'Cdc28-Clb2' also activates 'IE' to 'IE*'. 'Cdc28-Clb2' promotes the phosphorylation of 'Sic1' to 'PSic1', which is then targeted by 'SCF' for degradation (indicated by five small circles). 'Sic1' inhibits 'Cdc28-Clb2'. 'Cdc28-Clb2' also activates 'APC' to 'APC+'. 'APC+' in conjunction with 'Cdc20' targets 'Clb2' for degradation. 'APC+' in conjunction with 'Cdh1' also targets 'Clb2' for degradation. 'Cdc20' is formed and subsequently degraded. 'Cdh1' is also formed and degraded. 'Cdc28-Clb2' inhibits 'Cdh1'. There's a feedback loop where 'IE*' promotes 'Cdc20' formation. 'Cdc20' activates 'Cdh1'. 'Cdc28-Cln' (formed from SBF* and Cdc28) also plays a role in inactivating 'Sic1' and 'Cdh1'. Degradation fragments are represented by five small circles. AA, amino acids; APC, anaphase promoting complex; Cdc20 and Cdh1, proteins that target Clb2 to the APC; Cln, G1 cyclins; IE, intermediary enzyme; Mcm1, transcription factor for Clb2; SBF, transcription factor for Cln; SCF, Skp1–Cdc53–F-box protein complex; Sic1, stoichiometric inhibitor of Cdc28–Clb2; five small-circles, degradation fragments. Notice that Cdc28–Clb2 has two major antagonists, Sic1 and Cdh1. In G1 phase, Sic1 and Cdh1 are active and Cdc28–Clb2 is repressed, and vice versa in S-G2-M. Cln-dependent kinase activity pushes the engine from G1 to S-G2-M by inactivating Sic1 and Cdh1. Cln synthesis turns on when the cell grows to a critical size, because Mass activates SBF. The transition from S-G2-M back to G1 is driven by Cdc20, which targets Clb2 for degradation and (indirectly) activates Cdh1. For further details, see Tyson and Novak (2001) and Chen et al. (2000). The asterisk identifies the more active form of a protein.::>

<a id='239c38ad-a198-4e51-895b-80b5d25e3cd1'></a>

of dinucleated cells, which are less viable than mononucleated cells (Sia et al., 1996). The arrest is not complete; after several hours, unbudded cells undergo mitosis (called "adaptation") and become dinucleate (Sia et al., 1996).

<a id='3dcfbb78-e08a-449a-8357-2c67a737177f'></a>

In this paper, we propose a molecular network for the morphogenesis checkpoint, based largely on Lew's work (Lew, 2000), and we translate it into a set of differential equations. Our main goal is to explain the observed properties of cells under checkpoint-free and checkpoint-induced conditions in terms of the temporal dynamics of the underlying molecular regulatory system. The model provides a common framework for describing many diverse features of the checkpoint; not only G2 delay, but also adaptation and cell death. The model also suggests a number of experiments that would be especially revealing about the molecular regulatory system.

<a id='316368e7-4096-47ad-a39b-6fc4ac97ef84'></a>

# Results
## A mathematical model
In Table I and online supplemental material (Experimental basis of the model, available at http://www.jcb.org/cgi/ content/full/jcb.200306139/DC1), we summarize the experimental results that support a hypothetical molecular mechanism for the morphogenesis checkpoint, based on posttranslational modification of Swe1. Obviously, the checkpoint mechanism cannot be separated from the whole

<a id='d399bf18-9c57-41f7-89f3-79c397db22e0'></a>

network of cell-cycle regulatory proteins. Cdc28-Clb2 is the key regulator of mitosis and as such it is the main target of Swe1 kinase activity, but there are other connections. For example, the transcription factor SBF controls Swe1 expres- sion as well as Cln1-2 expression; and bud formation, needed for Hsl1 activation, is due to Cdc28-Cln1-2. There- fore, if we want to model the morphogenesis checkpoint, we must start with a model of the cell cycle engine.

<a id='b3b28f31-4cf5-4ad9-a3da-d9d96d71fe19'></a>

**Cell cycle engine.** Tyson and Novak (2001) have proposed a simplified version (Fig. 1) of a model by Chen et al. (2000) of the budding yeast cell cycle. In the Tyson-Novak model, Cln1, Cln2, Clb5, and Clb6 are lumped together as "Cln", and Clb1 and Clb2 are lumped together as "Clb2". Cln synthesis is due to SBF, and therefore is a function of cell size (Dirick et al., 1995). Cln-dependent kinase activity induces degradation of Sic1, and initiates DNA synthesis (via Clb5-6). Moreover, Cln-dependent kinase activity inactivates Cdh1, permitting Clb2 level to rise. Cdc28–Clb2 activity, relieved from Sic1 and Cdh1 inhibition, turns on its own transcription through Mcm1, and turns off Cln transcription by inhibiting SBF. The cell enters into M phase, and Cdc28–Clb2 starts a negative feedback loop by activating a putative intermediate enzyme, and by enhancing Cdc20 transcription. The ultimate effect of the loop is to activate the anaphase promoting complex, which degrades Clb2 and drives the cell out of mitosis.

<a id='2f5045c6-7665-4bec-bb95-c9df55192456'></a>

In addition to Mcm1-dependent transcription of _CLB2_,
we assume a background transcription rate, independent of
Mcm1. After Tyson and Novak (2001), we assume that the
rate of Clb2 synthesis increases with cell size (_M_), and even-
tually saturates. This relationship mimics the accumulation
of Clb2 in the nucleus as the cell grows. To this engine, we
now graft our mechanism for the morphogenesis checkpoint
(Fig. 2).

<a id='ee9bd467-7e34-4171-a49f-bc9532945501'></a>

**Hsl1-Hsl7-Bud.** To keep the model simple, while preserving its main biological properties, we do not take into account any spatial features; first, we assume simply that bud formation is turned on by the Clns (see Other rules). Second, we do not keep track of Hsl1 synthesis, degradation, and activation. Because Hsl1 activation depends on bud presence, we assume that when the bud is formed, Hsl1 is able to "modify" Swel (Swe1M denotes the modified form of Swel). The nature of this modification is not clear, as Swel does not appear to be a substrate for Hsl1 (Cid et al., 2001; Theesfeld et al., 2003). Whatever the modification may be, we assume that it does not affect Swel stability but makes Swel inactive (0.5% of the fully active form). Finally, we ignore Hsl7 because Hsl1 catalyzes the rate-limiting step for Swel modification (McMillan et al., 1999a). Many other proteins are involved in this step (septins, Kcc4, Gin4, Cla4, and Nap1), but again, as a first approximation, we ignore them.

<a id='2e884f6c-f5fc-49aa-bd70-baee99049955'></a>

Swe1. Swe1 does not play a major role during the normal cell cycle of S. cerevisiae even though it is able to phosphorylate Cdc28 on tyrosine-19 (Booher et al., 1993). The cell cycle is perfectly normal in swe1Δ (Booher et al., 1993). Nonetheless, Swe1 can affect cell cycle progression, as swe1Δ cells are slightly smaller than wild-type cells (Harvey and Kellogg, 2003), and Swe1 overexpression (GAL-SWE1, wild-type gene controlled by a GAL promoter) leads to a G2 block and very elongated buds (Booher et al., 1993).

<!-- PAGE BREAK -->

<a id='7e29e849-a9be-4d99-a529-b9b6c22b50ba'></a>

1246 The Journal of Cell Biology | Volume 163, Number 6, 2003

<a id='a6835d15-1a4a-4f0b-9fb8-af1dffbc4458'></a>

<::chart: Diagram titled "The Swe1 box" illustrating the different forms of Swe1 and its interactions with other proteins during the cell cycle.

The diagram shows the following entities and their interactions:

**Top Section:**
- A state represented by two black circles, connected to PSwe1M by an arrow labeled "fast" and to PSwe1 by an arrow labeled "slow".

**Swe1 Forms and Modifications:**
- **PSwe1M** (Phosphorylated and Modified Swe1) and **Swe1M** (Modified Swe1) are interconnected by bidirectional arrows.
- **PSwe1** (Phosphorylated Swe1) and **Swe1** (Unchanged Swe1) are interconnected by bidirectional arrows.
- PSwe1M and PSwe1 are interconnected by bidirectional arrows.
- Swe1M and Swe1 are interconnected by bidirectional arrows.
- A dashed arrow labeled "BUD/Hsl1" points to Swe1.

**Cdc28-Clb2 Complex:**
- A boxed "Cdc28" with an oval "Clb2" represents the Cdc28-Clb2 complex.
- A dashed arrow points from Cdc28-Clb2 to PSwe1M.
- The Cdc28-Clb2 complex is interconnected by bidirectional arrows with a boxed "PCdc28" with an oval "Clb2" (Phosphorylated Cdc28-Clb2).
- A dashed arrow points from Cdc28-Clb2 to Mih1.
- A dashed arrow points from Cdc28-Clb2 to PSwe1.

**Mih1 Interactions:**
- **Mih1** and **Mih1*** are interconnected by bidirectional arrows.
- A dashed arrow points from Mih1 to PCdc28 (Clb2).
- A dashed arrow points from Mpk1 to Mih1*.

**SBF Interactions:**
- **SBF*** and **SBF** are interconnected by bidirectional arrows.
- A dashed arrow points from PCdc28 (Clb2) to SBF.
- A dashed arrow points from SBF* to Swe1.
- A dashed arrow points from "mass" to SBF.

**Bottom Section:**
- Swe1M and Swe1 each have an arrow pointing to a state represented by two black circles, both labeled "slow".

Figure 2. The **Swe1 box**. Swe1 can be present in four different forms during the cell cycle: unchanged (Swe1), phosphorylated by Cdc28–Clb2 (PSwe1); or modified by Hsl1 (Swe1M) or both (PSwe1M). The doubly modified form we assume to be less stable than the others. The unphosphorylated, unmodified form of Swe1 is assumed to be most active in phosphorylating Cdc28–Clb2. Cdc28 is dephosphorylated by Mih1. We assume that Cdc28–Clb2 phosphorylates and activates Mih1, and MAPK (Mpk1) inactivates Mih1. The asterisk identifies the more active form of a protein.::>

<a id='9585f2a1-d901-4170-a528-d0e91d1408cb'></a>

Cdc28-Clb2 phosphorylates Swe1 in vitro (McMillan et al., 2002), and we assume that Cdc28-Clb2 catalyzes the same reaction in vivo (we call the phosphorylated form PSwel). We assume that PSwel has 10% of Swe1 kinase activity.

<a id='6769064c-6755-40ea-8c46-ae3eaa72de33'></a>

Swe1 is degraded by proteasomes, after polyubiquitina-tion by the Skp1-Cdc53-F-box protein complex (Kaiser et al., 1998). We assume that Swe1, like other substrates of this complex, must be phosphorylated in order to be ubiqui-tinated. The phosphorylation we assume to be necessary but not sufficient (i.e., PSwe1 is as stable as Swe1). Efficient deg-radation of Swe1, we assume, requires modification by both Cdc28-Clb2 and Hsl1 (i.e., PSwe1M is both catalytically inactive and highly unstable).

<a id='ea194ac8-911e-4cfe-a4df-91c2a9b93e57'></a>

In the model, Hsll and Cdc28–Clb2 act along the same degradation pathway, each introducing a different posttranslational modification in Swel. Either modification alone renders Swel less active, whereas both are needed to make it unstable. Based on recent data (McMillan et al., 2002), we assume that these two modifications can occur in either order, although Hsll acts first in wild-type cells. The four different forms (Swel, SwelM, PSwel, and PSwelM) comprise the “Swel box” in Fig. 2.

<a id='992c66f1-2e21-4568-963f-a09f6ebf7d11'></a>

The antagonistic relationship between Cdc28–Clb2 and Swel is at the core of our model of the morphogenesis checkpoint. When the checkpoint is induced, Swel phos-phorylates and inhibits Cdc28–Clb2 (Booher et al., 1993). (Swel can also function as a stoichiometric inhibitor of Cdc28–Clb2 [McMillan et al., 1999b], but we do not keep track of this effect in the model.) On the other hand, Cdc28–Clb2 down-regulates Swel in three ways. By phos-phorylating Swel, it reduces Swel activity and prepares Swel for degradation. In addition, Cdc28–Clb2 inhibits the transcription factor, SBF, and thereby shuts off synthesis of Swel. If Cdc28–Clb2 successfully down-regulates Swel,

<a id='6e8592b6-0a2f-4f2d-abfb-e6124302ba64'></a>

then the cell proceeds into mitosis. If Swe1 successfully inhibits Cdc28–Clb2, then the cell arrests in G2 phase.

<a id='5afc8341-fb11-444a-a70e-f0bb69fce2d6'></a>

Mih1. In frog egg extracts (where the homologues of Mih1 and Cdc28–Clb2 are called Cdc25 and M-phase promoting factor [MPF]), Cdc25 has been shown to be involved in a positive feedback loop with MPF, whereby MPF activates Cdc25 by phosphorylation, and Cdc25 activates MPF by de-phosphorylating it (Izumi et al., 1992). Although there are no data to confirm the presence of such a feedback loop in S. cerevisiae, we assume it is operational in our model.

<a id='a4d7ab6d-9ce1-46e9-be31-d39302f99361'></a>

MAPK pathway. When bud formation fails, Hsl1 is un-able to down-regulate Swe1 activity. In addition, a second signaling pathway, operating through a MAPK (Mpk1) is thought to inhibit Mih1 and thereby alter the ratio of Mih1 to Swe1 activities (Harrison et al., 2001). Rather than intro-duce a full MAPK pathway, we simply assume that the rate constants characterizing Cdc28-Clb2 dephosphorylation by Mih1 are decreased 10-fold as an effect of Mpk1 activation, in response to bud failure.

<a id='db89ecf6-9cbd-4672-9844-56d866dbdb01'></a>

Equations and parameters. The wiring diagrams of Figs. 1 and 2 have been translated into a set of ordinary differential equation (Table S1, available at http://www.jcb.org/cgi/content/full/jcb.200306139/DC1) using mass-action kinetics for the most part. Where we use Michaelis-Menten kinetics, we are treating the posttranslational modification as a "Goldbeter-Koshland switch" (Goldbeter and Koshland, 1981), which is a convenient and reasonable way to model information processing in signal transduction pathways. For transcriptional control of Cdc20 synthesis by Cdc28–Clb2, we use a Hill function for convenience; other assumptions would work just as well. The parameter values used in our simulations are shown in Table S2, available at http://www.jcb.org/cgi/content/full/jcb.200306139/DC1. Degradation rates for the four different forms of Swel have been computed from Sia et al. (1998), whereas those parameter values relative to Fig. 1 are derived from Tyson and Novak (2001). All other parameter values for Fig. 2 have been chosen to fit the experimental data summarized in Table I.

<a id='cbaf6fca-5820-4cd9-b146-fac0779c2a4c'></a>

Other rules. A nontrivial aspect of modeling gene networks is to link physiological observations with molecular states of the model. Our variables are concentrations, but bud formation, nuclear division (ND) and cell death are the experimental observables. We have adopted the following six rules to relate our calculations to experimental observations:
(1) cell size increases exponentially ($M = M_0e^{\mu t}$, $\mu$ = specific growth rate). Cell division ($M \to M/2$) occurs when Cdc28-Clb2 decreases below a threshold, [Clb2] = 0.2; (2) we introduce a variable [BE] that represents the extent of phosphorylation of proteins targeted by Cdc28-Cln. We assume that a bud is formed ([BUD] = 1) and Hsl1 is activated when [BE] increases above a threshold value (0.6). The bud is removed ([BUD] = 0) and Hsl1 is inactivated when the cell divides. We model $hsl1\Delta$ by setting $k_{hsl1}$ = 0; (3) the MAPK signal is modeled by reducing the activity of Mih1 by 90% ($k_{mih}$ = 0.5, $k''_{mih}$ = 0.05); (4) most experiments report the percentage of cells that undergo ND as a function of time. Because our model is deterministic, all cells divide at the same time. We identify the experimental time when 50% of the cells have undergone ND with the time in the model when anaphase occurs, i.e., when Cdc20

<!-- PAGE BREAK -->

<a id='387d6c54-7481-4f87-9c65-b70d39950ff7'></a>

Mathematical model of the morphogenesis checkpoint | Ciliberto et al. 1247

<a id='b5248b83-a774-4dcb-9c1b-74b2da5e4d22'></a>

is activated (increases above a threshold value of 0.3); (5) experimentally, cell synchronization is obtained by treating cells for 2-3 h with a-factor, and then releasing them from the block. We simulate this experiment by allowing growth for 120 min at one half the specific growth rate of normal cells, and setting SBF activity to 0, so that *CLN* and *SWE1* are not transcribed (Sia et al., 1996). The variables at the end of the 120 min simulation are used as the initial conditions for the ND timing experiment. In some experiments, synchronization was obtained by elutriation. In this case, we choose our initial conditions at the minimum mass value of a regular cell cycle; and (6) we use the following rule to determine whether the cell is viable or not: a mononucleated cell (dinucleated cell) is dead if its size exceeds four times (five times) the size of a wild-type cell at division.

<a id='32f838e2-2c09-4a0e-b6bc-bdaf81f9231a'></a>

**Kinetic data in cdc24^ts background strains**
In the laboratory, the morphogenesis checkpoint can be induced by treating cells with inhibitors of actin polymerization (Latrunculin-A [McMillan et al., 1998]), by expressing mutations that interfere with actin polymerization (tpm1Δ [McMillan et al., 1998]), or with bud formation in general (cdc24^ts [Lew and Reed, 1995]). In this paper, we address only experiments using cdc24^ts mutants (Sia et al., 1996, 1998; McMillan et al., 1999a). A summary of the experimental data used to constrain the model is presented in Table I, together with the corresponding simulation results.

<a id='aa0e2c69-37e0-47f0-ac05-fe5825577b32'></a>

The effect of the morphogenesis checkpoint is commonly measured as a delay of ND in *cdc24ts* mutants relative to *CDC24* control cells (Lew and Reed, 1995). In most experiments, yeast cells are synchronized by α-factor arrest and release, and then, while the cells are growing at the restrictive temperature, the time of the first ND is measured (Sia et al., 1996). ND occurs much later in *cdc24ts* cells at the restrictive temperature (checkpoint invoked) than in *CDC24* cells (checkpoint silent). The delay depends, of course, on what other mutations are introduced into the *cdc24ts* and *CDC24* strains (Table I).

<a id='ad09fb1d-efa5-4f65-8432-fad0913495dd'></a>

The basic mutant, _cdc24_ at the restrictive temperature, is unable to develop a bud; nevertheless, it undergoes ND 135–165 min after release from α-factor (Sia et al., 1996; Mc-Millan et al., 1999a). In other words, the morphogenesis “checkpoint” in this mutant is not very tight; after 2–3 h the cell adapts to it (Sia et al., 1996). The checkpoint depends on _Swe1_ because _cdc24_ _swe1_Δ does not show any delay of ND compared with wild type (Sia et al., 1996). _Mih1_ is necessary for adaptation because _cdc24_ _mih1_Δ is irreversibly blocked in G2 (Sia et al., 1996). On the other hand, _cdc24_ _hsl1_Δ does not show a phenotype more severe than _cdc24_, suggesting that _Hsl1_ is already inactive in _cdc24_ (McMillan et al., 1999a); not surprisingly because septins, required for full ac-tivation of _Hsl1_, are not properly organized in this mutant.

<a id='a974779f-d5be-4ed1-87a9-7ab94d878ba5'></a>

Finally, we want to explore mutants where Swe1 is overex-
pressed. Swe1 production can be made constitutive by cou-
pling the *SWE1* gene to either the GAL or GAP promoter.
(Transcriptional efficiency is lower from the GAP promoter
than from the GAL promoter.) *GAL-SWE1* is blocked in G2
phase even when the morphogenesis checkpoint is not active
(Booher et al., 1993). In *cdc24ts GAP-SWE1*, ND is delayed
(118 min) but not as much as in *cdc24ts* cells (Sia et al.,

<a id='23c5eec4-840a-4df9-a572-f2a9ea8a9640'></a>

<::Four line graphs showing time courses of mass and concentrations of various proteins. All graphs share a common x-axis labeled "time (min)" ranging from 0 to 100 (or slightly more).

Top-left graph:
- Y-axis ranges from 0.0 to 1.5.
- Plots include: Sic1 (solid line, peaks around 1.25), SBF* (dotted line, step-like increase and decrease), Clb2 (solid line, peaks around 0.7), Cln (dashed line, peaks around 0.9), and BUD (dashed line, step-like increase and decrease).

Top-right graph:
- Y-axis ranges from 0.0 to 2.0.
- Plots include: Cdc20* (dashed line, starts high, drops, then rises again), Cdh1* (dashed line, starts at 1.0, drops to 0, then rises again), Clb2 (solid line, peaks around 0.7), and IH* (dashed line, rises sharply at the end).

Bottom-left graph:
- Y-axis ranges from 0.00 to 0.15.
- Plots include: PSwe1M (dotted line), Swe1T (dashed line), Swe1M (solid line), and Swe1 (dashed line). All show fluctuations with peaks and troughs.

Bottom-right graph:
- Y-axis ranges from 0.4 to 1.6.
- Plots "mass" (dotted line) which increases linearly from approximately 0.8 to 1.6, then drops sharply.

Figure 3. **Time courses of mass and concentrations during the** **cycle of wild-type cells.** Numerical solution of equations in Table S1, given the parameter values and initial conditions from Table S2. Because Cdc28 is present in excess and binds quickly to cyclins, there are no free cyclins in the model: a curve marked by a cyclin, such as Cln, always refers to the concentration of the relevant complex with Cdc28, such as [Cdc28–Cln]. Swe1T refers to total Swe1 concentration. The concentration of the phosphorylated form of Swe1 is negligible and not depicted. The asterisk identifies the more active form of a protein.::>

<a id='4fe1b54f-e096-4b57-b99d-7e3a2623ea33'></a>

1996). Clearly, transcriptional control of Swel synthesis is not necessary for a working morphogenesis checkpoint, but the length of the delay depends sensitively on the level of Swel expression. This sensitivity is even more evident in *cdc24ts* SWE1-2X and *cdc24ts* SWE1-4X mutants (McMillan et al., 1999a), where ND occurs much later (over 5 h in both cases) than in *cdc24ts* (135–165 min; Sia et al., 1996, 1998). Actually, the system is sensitive to the ratio of Mih1 to Swel rather than to the absolute value of Swel expres- sion, as shown in an elegant experiment by Sia et al. (1996). They altered systematically the Mih1/Swel ratio by creating diploid strains (*MIH1-mih1* and *mih1-mih1*) in a back- ground homozygous for *SWE1* and *cdc24ts*. They repeated the same experiment, this time altering *SWE1* dosage in a diploid strain homozygous for *MIH1* and *cdc24ts*. In these four mutants, the delay of ND is shown to increase with the ratio of active Swel to active Mih1 (Sia et al., 1996). We simulate these and other mutants in two stages: first with the checkpoint turned off (*cdc24ts* at 25°C) and then with the checkpoint turned on (*cdc24ts* at 37°C).

<a id='b928e3b0-eed3-4a99-aebc-9cb8d2ee4c53'></a>

**Checkpoint inactive (permissive temperature)**
wild type, _mih1∆_, and _hsl1∆_. Although Swel is able to phosphorylate Cdc28–Clb2 and it is transcribed earlier than Clb2, the morphogenesis checkpoint is not operational during normal cell division. How does the model explain this apparent contradiction? Fig. 3 shows that, as soon as bud formation occurs, most of the active Swel is modified by Hsl1 into SwelM and therefore inactivated. Cdc28–Clb2 rises rapidly and phosphorylates SwelM, converting it into PSwe1M, which is rapidly degraded. The time course of total Swel (SwelT) agrees with published data (Sia et al.,

<!-- PAGE BREAK -->

<a id='e08dad88-66e4-4fbf-963b-5cbb7f40bcd2'></a>

1248 The Journal of Cell Biology | Volume 163, Number 6, 2003

<a id='358b36dd-36c0-4d81-83e0-ebcf31e13b0b'></a>

<::chart: The figure displays two stacked line graphs showing dynamics over time (min). The x-axis for both graphs ranges from 0 to approximately 150 min. The top graph has two y-axes: the left y-axis is labeled "mass" and ranges from 0.5 to 2.0; the right y-axis is labeled "Clb2" and ranges from 0.0 to 0.8. A dotted line represents mass, showing a linear increase from about 0.8 to 1.5. A solid line represents Clb2, starting at 0.0, rising to a peak of about 0.7 at around 120 min, and then sharply decreasing to 0.0. The bottom graph is titled "Swe1T" and has a y-axis ranging from 0.0 to 0.2. A solid line labeled "Swe1" starts at approximately 0.15, dips slightly, then rises to a peak of about 0.18 around 100 min, and then decreases. A dashed line labeled "PSwe1" starts at 0.0, rises to a peak of about 0.18 around 120 min, and then sharply decreases. Figure 4. *hsl1*Δ cells. (Parameter values as in Table S2, except for alterations specified in row 4 of Table I.) Mass and Cdc28–Clb2 dynamics (top, dotted and solid lines, respectively) resemble closely the wild-type cycle, whereas Swe1 dynamics is different (bottom) because Swe1 cannot be modified by Hsl1.::>

<a id='fc75c7fe-2c64-4189-922c-1d02acfa92a5'></a>

1998). Concentration of the phosphorylated unmodified form (PSwe1) is negligible during a wild-type cell cycle, according to the model. A similar timing of Swel redistribution among its four forms occurs in mih1Δ (unpublished data), because Swel never gets a chance to phosphorylate Cdc28–Clb2. On the other hand, in hsl1Δ (Fig. 4), Swel follows a completely different path in the Swel box (Fig. 2). Because the left part of the box is unavailable, Swel oscillates between its active form and its phosphorylated form. Total Swel undergoes small amplitude oscillations because Cdc28– Clb2 transiently inhibits its transcription factor, SBF, but it does not undergo large amplitude oscillations, as in wild type and mih1Δ, because Swel is never transformed into the highly unstable form (PSwe1M) in hsl1Δ (McMillan et al., 1999a). Although this redistribution of Swel among its four possible forms is completely different from wild type and mih1Δ, the overall timing of cell division is not affected. Even though Cdc28–Clb2 is inhibited, it accumulates enough active form to switch on its transcription, to activate Mih1, and eventually to phosphorylate and inhibit Swel.

<a id='cece65fa-bc90-4f96-b057-3d335324bb75'></a>

_mih1Δ clb2Δ_ compared to _hsl1Δ clb2Δ_. The different roles of Hsl1 and Mih1 become even more evident in the double mutant cells _mih1Δ clb2Δ_ and _hsl1Δ clb2Δ_. Even though the single mutants, _mih1Δ_ and _hsl1Δ_, are very similar, the double mutants with _clb2Δ_ are not; _hsl1Δ clb2Δ_ showing a more severe phenotype (longer cells) than _mih1Δ clb2Δ_ (Lew, D.J., personal communication). In our model, Clb1 and Clb2 are lumped together as Clb2. Based on evidence in Cross et al. (2002), we assume that Clb2 transcription accounts for two thirds of the total Clb1 + Clb2 transcription, whereas Clb1 transcription is the remaining one third. Hence, in _clb2Δ_ we reduce Clb transcription rate

<a id='552526fa-ea87-49df-a068-0237e5b0234e'></a>

<::transcription of the content: chart::>Figure 5. Comparison of *hsl1Δ clb2Δ* and *mih1Δ clb2Δ*. (Parameter alterations specified in rows 7 and 8 of Table I.) Both cells grow larger than wild-type cells (top: dotted line is mass, solid line is Cdc28–Clb1), but *hsl1Δ clb2Δ* cells are 21% larger than *mih1Δ clb2Δ*. The Swe1 dynamics explains the different behavior: in *mih1Δ clb2Δ* the delay is only due to *CLB2* deletion, whereas in *hsl1Δ clb2Δ*, Swe1 also contributes to Cdc28–Clb1 inhibition. Notice that total Swe1 does not oscillate in *hsl1Δ clb2Δ* because mass is big enough (as measured by Cln-dependent kinase activity) to keep SBF always active (not depicted). The figure displays two main panels, side-by-side, each representing a different cell type. Each panel contains two subplots stacked vertically. The x-axis for all subplots is 'time (min)' ranging from 0 to 100. Left Panel: *hsl1Δ clb2Δ*. Top subplot: Y-axis left is 'mass' (2 to 6), Y-axis right is 'Clb1' (0.0 to 0.8). A dotted line, labeled 'mass', increases steadily from ~2.5 to ~5.5. A solid line, labeled 'Cdc28–Clb1', starts at 0, rises to a peak of ~0.6 at ~90 min, then sharply drops to 0. Bottom subplot: Y-axis from 0.0 to 0.4. A long-dashed line, labeled 'Swe1T', is constant at ~0.35. A solid line, labeled 'Swe1', starts at ~0.35, sharply drops to 0 at ~80 min, and then rises back to ~0.35 at ~100 min. A short-dashed line, labeled 'PSwe1', starts at 0, sharply rises to ~0.35 at ~80 min, and then drops back to 0 at ~100 min. Right Panel: *mih1Δ clb2Δ*. Top subplot: Y-axis left is 'mass' (2 to 6), Y-axis right is 'Clb1' (0.0 to 0.8). A dotted line, labeled 'mass', increases steadily from ~2.5 to ~4.5. A solid line, labeled 'Cdc28–Clb1', starts at 0, rises to a peak of ~0.5 at ~90 min, then sharply drops to 0. Bottom subplot: Y-axis from 0.0 to 0.2. A long-dashed line, labeled 'Swe1T', starts at ~0.05, rises to a peak of ~0.18 at ~70 min, then decreases to ~0.05. A short-dashed line, labeled 'Swe1M', starts at ~0.02, rises to a peak of ~0.15 at ~70 min, then decreases to ~0.02. A solid line, labeled 'Swe1', starts at 0, rises to a peak of ~0.02 at ~10 min, then drops to 0, rises again to ~0.02 at ~50 min, drops to 0, and then rises to ~0.02 at ~100 min. A dotted-dashed line, labeled 'PSwe1M', starts at 0, rises to a peak of ~0.15 at ~70 min, then decreases to ~0.02. A short-dashed line, labeled 'Swe1' (this label seems to be misplaced or duplicated from the solid line in the plot), shows a similar pattern to the solid line for Swe1.::>

<a id='b4ecb385-d6d1-4e63-859b-3d9577f31838'></a>

(k_s,clb) to one third of its wild-type value. In our simulation, we get similar qualitative results (Fig. 5): hsl1Δ clb2Δ cells are 21% larger than mih1Δ clb2Δ cells. The reason why mih1Δ clb2Δ shows a less severe phenotype is that Hsl1 creates inactive Swe1M. This way, even though only Clb1 is transcribed, it is enough to lead the cell into mitosis. On the other hand, in hsl1Δ clb2Δ, there is a battle between Swe1 and Cdc28-Clb1, which is initially won by Swe1 because it is transcribed first. Clb1 transcription is initially kept low, the cell is stuck in G2 and increases in size. However, an increasing amount of Clb1 accumulates in the nucleus as the cell becomes larger, and eventually it is able to transform Swe1 to its inactive phosphorylated form PSwe1, and to lead the cell through mitosis.

<a id='5af36326-fac2-4814-be95-ce087cc0fbfc'></a>

_mih1Δ hsl1Δ._ It is known that either Hsl1 alone or Mih1 alone is sufficient to help Cdc28–Clb2 against Swe1, whereas the double mutant is inviable. In the model, we obtain a similar result (Fig. 6). Comparing the double mutant with _hsl1Δ_ (Fig. 4), we see that, without any help from Mih1 and Hsl1, Cdc28–Clb2 is unable to win against Swe1. As a result, the cell is blocked in G2; it grows very large and dies.

<a id='b72add85-a463-4b6d-9982-f329408f2c8e'></a>

Checkpoint active (restrictive temperature)

cdc24^ts, cdc24^ts hsl1Δ, and cdc24^ts mih1Δ. At the restrictive temperature, cdc24^ts cells are similar to hsl1Δ mih1Δ, but not as extreme, because we assume that Mih1 preserves 10% of its activity when the checkpoint is invoked. As a result, ND is delayed, giving rise to dinucleated cells (ND but not cell division). ND timing in the simulation is compara-

<!-- PAGE BREAK -->

<a id='c68c5c9d-66b1-4375-8f92-c56258977657'></a>

<::Figure with two stacked line graphs.The top graph shows 'mass' (dotted line, left y-axis 0-10) and 'Clb2' (solid line, right y-axis 0.0-0.2) increasing over time. The bottom graph, sharing the x-axis 'time (min)' (0-400), shows 'Swe1T' (dashed line) and 'Swe1' (solid line) increasing from 0.0 to approximately 0.35, while 'PSwe1' (dotted line) remains low, near 0.0. The y-axis for the bottom graph ranges from 0.0 to 0.4.: chart::>

Figure 6. *hsl1*Δ *mih1*Δ cells. (Parameter alterations specified in
row 5 of Table I.) Mass and Cdc28–Clb2 (top, dotted and solid lines,
respectively) increase during the G2 arrest, until the cell dies (Other
rules). G2 block is due to active Swe1, which represents the largest
fraction of the total Swe1 pool (bottom).

<a id='e797f962-3e1b-49f1-8836-70e8cc69f4f5'></a>

ble to experimental observations (Table I and Fig. 7). According to the model, *cdc24<sup>ts</sup> hsl1Δ* has the same parameter set as *cdc24<sup>ts</sup>*, whereas *cdc24<sup>ts</sup> mih1Δ* shares the same parameter set with the double mutant *hsl1Δ mih1Δ* (Table I).

<a id='b7da8450-d02a-4235-9951-efd0b58a9242'></a>

**GAP-SWE1** and **GAL-SWE1**. Swe1 transcription is controlled by SBF, but transcriptional control is not critical for the dynamics of the system (Sia et al., 1996). To model **GAP-SWE1**, we set k_s,swe = 0 and k_s,sweC = 0.001. In this case, for **GAP-SWE1** cells, ND occurs at the same time as in wild-type cells, but for **GAP-SWE1** cdc24ts cells, ND occurs ~35 min later. On the other hand, **GAL-SWE1** has a more severe phenotype, which can be reproduced by increasing still more the rate of SWE1 transcription (Table I).

<a id='f5c024e2-1eed-410b-886a-08a56bc92fc9'></a>

cdc24ts _SWE1-2X_ and cdc24ts _SWE1-4X_. To fine-tune the parameters controlling Swe1 transcription, we want to reproduce experiments where Swe1 expression is increased two- and fourfold. The simulations are again in good quantitative agreement with experimental data (Table I).

<a id='e51ce545-4781-4d8a-be59-9cde4f8dc9aa'></a>

Mih1 to Swe1 ratio in diploid cells. This ratio is at the core of the morphogenesis checkpoint: if Swe1 (Mih1) prevails, the checkpoint is (is not) operational. Sia et al. (1996) investigated thoroughly the effect of altering the ratio in diploid strains, and discovered that ND increases with [Swe1]/[Mih1]. Simulations are in agreement with experimental data (Fig. 8). (This experiment was performed on diploid cells. We assume that the biochemical parameters are the same in the haploids and diploids, except for the transcription rates. We assume a homozygous strain AA has the same transcription rate as the haploid A, whereas transcription rate for the heterozygous Aa is one half of the haploid; Table I.)

<a id='a56d637c-d767-4744-805b-d31410cee4d5'></a>

## Parameter analysis
A thorough analysis of parameter space exceeds the aim of this work, but it is possible to investigate the behavior of the model to changes in parameter values of special biological interest (see Materials and methods). We choose not to vary

<a id='98accd9f-179f-4529-a0ed-387382ba0360'></a>

Mathematical model of the morphogenesis checkpoint | Ciliberto et al. 1249
<::chart: A multi-panel line chart showing the time course of various protein concentrations and cell mass in cdc24^ts cells.

All panels share a common x-axis labeled "time (min)" ranging from 0 to 150.

Panel 1 (Top-Left):
- Y-axis range: 0.0 to 2.0
- Lines:
  - Sic1 (dashed line): Starts high (~1.8), drops sharply to 0 around 25 min, stays low, then rises sharply around 140 min to ~1.8.
  - SBF* (dash-dot line): Rises from 0 to ~1.0 by 25 min, plateaus until ~125 min, then drops sharply to 0.
  - Cln (solid line): Rises from 0 to ~1.0 by 25 min, plateaus until ~125 min, drops to 0, then rises sharply to ~0.5 around 140 min.
  - Clb2 (dotted line): Stays at 0 until ~120 min, then rises sharply to ~1.0 around 130 min, and drops to ~0.5 by 150 min.

Panel 2 (Top-Right):
- Y-axis range: 0.0 to 2.5
- Lines:
  - mass (dotted line): Starts at ~1.0 and steadily increases to ~2.4 by 150 min.
  - Cdh1* (solid line): Starts at ~1.0, drops sharply to 0 by 25 min, and remains at 0.
  - Cdc20* (dash-dot line): Stays at 0 until ~130 min, then rises sharply to ~2.0 by 150 min.
  - IE* (dashed line): Stays at 0 until ~130 min, then rises sharply to ~1.0 by 150 min.

Panel 3 (Bottom-Left):
- Y-axis range: 0.0 to 0.2
- Lines:
  - Swe1T (dash-dot line): Rises from 0 to ~0.2 by 100 min, plateaus, then drops sharply to ~0.1 by 150 min.
  - Swe1 (solid line): Rises from 0 to ~0.2 by 100 min, plateaus, then drops sharply to ~0.05 by 150 min.
  - PSwel (dashed line): Stays at 0 until ~120 min, then rises to ~0.2 by 130 min, and drops sharply to 0 by 150 min.

Panel 4 (Bottom-Right):
- Y-axis range: 0.0 to 0.9
- Lines:
  - Mih1* (dotted line): Stays at 0 until ~120 min, then rises sharply to ~0.9 by 130 min, and drops to ~0.6 by 150 min.
  - PClb2 (dash-dot line): Rises from 0 to ~0.7 by 125 min, then drops sharply to ~0.1 by 150 min.
  - Clb2 (solid line): Rises from 0 to ~0.8 by 125 min, then drops sharply to ~0.2 by 150 min.

Figure 7. cdc24^ts cells. Notice that these cells are synchronized by α-factor arrest and release, and their starting size is bigger than wild-type cells. Moreover, Cln and SBF start from zero as the positive feedback loop involving Cln and SBF is switched off during synchronization by α-factor. Parameters as wild type (Table S2) except for k'mih = .5, kmih = .05, and khsl1 = 0. The asterisk identifies the more active form of a protein.::>


<a id='5c51b172-83bb-4346-b042-68ffa54e9b48'></a>

the kinetic constants of the cell cycle engine (Fig. 1) because
they are based on a different set of experimental data (Tyson
and Novak, 2001). Nor do we question the assumptions
that Cdc28-Clb2 down-regulates Swe1 synthesis (by inacti-
vating SBF) and up-regulates its degradation (phosphory-
lated Swe1 is a better substrate for ubiquitinylation), which
are well founded experimentally (Sia et al., 1996, 1998). In
contrast, we have made several assumptions for which there
is no experimental evidence in budding yeast: that Swe1 ac-
tivity is reduced by Hsl1-dependent modification and by
Cdc28-Clb2-dependent phosphorylation, and that Mih1
activity is increased by Cdc28-Clb2-dependent phosphory-
lation. Three main questions can be formulated concerning

<a id='094f7a00-c692-4b0f-9ad2-b7d8541d57a1'></a>

<::chart: Bar chart showing Nuclear Division Time (min) versus SWE1 to MIH1 ratio. The y-axis is labeled "Nuclear Division Time (min)" and ranges from 0 to 400. The x-axis is labeled "SWE1 to MIH1 ratio" with values 0, 0.5, 1, and 2. For each ratio, there are two bars: a gray bar representing experimental data and a black bar representing simulated results. Above the bars for ratio 0, the text "swel/swel MIHI/MIHI" is displayed. Above the bars for ratio 0.5, the text "SWE1/swel MIHI/MIH1" is displayed. Above the bars for ratio 1, the text "SWE1/SWEI MIHI/MIHI" is displayed. Above the bars for ratio 2, the text "SWEI/SWEI MIH1/mih1" is displayed. The heights of the bars are approximately: Ratio 0: Gray ~150, Black ~130; Ratio 0.5: Gray ~190, Black ~150; Ratio 1: Gray ~250, Black ~220; Ratio 2: Gray ~380, Black ~370. Figure 8. ND is delayed as the ratio of SWE1 to MIH1 increases. Gray histograms, experimental data (Table I, 9th column). Black histograms, simulated results (parameter alterations specified in rows 1, 2, 11, and 12 of Table I).::>

<!-- PAGE BREAK -->

<a id='e2bada74-fe3d-4b0c-847f-9a69b5a9de73'></a>

1250 The Journal of Cell Biology | Volume 163, Number 6, 2003

<a id='a4f9738a-82e6-48eb-b3c7-9518e733b0a2'></a>

these assumptions. (1) How much activity can be given to Swe1M (rate constant k''swe) as opposed to the fully active form, Swe1 (k'swe)? (2) Is Swe1 inactivation by Cdc28–Clb2 needed? In other words, what is the maximum activity that can be assigned to PSwe1 (k'''swe)? (3) Is Mih1 activation by Cdc28–Clb2 required? Has the activity of the nonphosphorylated form of Mih1 (kmih) to be smaller than the activity assigned to Mih1* (k'mih)?

<a id='f58e5f5c-b3bf-462d-a6a5-0bb64f1d90c7'></a>

Swe1M. To determine how much Swe1M activity is tol-
erated by the model, we increased the rate constant k''swe.
The second parameter to be varied is the Mih1* rate con-
stant k'mih, which controls the reverse reaction (dephosphor-
ylation) on the same substrate, Cdc28-Clb2. Mih1 back-
ground rate constant k''mih is set to k'mih/10. Results (Fig. 9
A) show that already for k''swe = 0.1 (5% of Swe1 activity) it
is impossible to reproduce the 13 different genotypes. In-
deed, a more detailed analysis (Fig. 9 B) shows that k''swe can
be maximum 1.75% of k''swe. Notice in Fig. 9 A that a much
larger region of the parameter space (where k''swe reaches
20% of k''swe) fits 12 genotypes, the missing one being always
due to the fact that the size of clb2Δ hsl1Δ fails to exceed the
size of clb2Δ mih1Δ. This is not surprising, because as soon
as some activity is given to Swe1M, it becomes harder for
Cdc28-Clb2 to overcome Swe1 in clb2Δ mih1Δ mutants,
whereas it has no effect on clb2Δ hsl1Δ where Swe1M is not
present. We conclude that these unpublished data put a se-
vere constraint on the activity of Swe1.

<a id='cf657ccf-0b72-4c15-95d4-52e1086287c5'></a>

**PSwe1 and Mih1.** A second two-parameter analysis was performed to investigate the requirements of activation of Mih1 by Cdc28-Clb2 and inactivation of Swe1 by Cdc28-Clb2. First, we want to know whether Swe1 inactivation alone can be sufficient. The positive feedback between Cdc28-Clb2 and Mih1 is eliminated by assigning the same activity to Mih1 and Mih1* (i.e., k'mih = k''mih). Their common value is the first parameter to be varied. The second parameter is k'''swe, the activity assigned to PSwe1, whereas Swe1 activity (k'swe) is kept constant. As k'''swe approaches k'swe = 2 (Table S2), Swe1 regulation disappears. If any combination of these two parameters can fit all 13 genotypes, we conclude that, for those particular parameter values, the positive feedback loop between Mih1 and Cdc28-Clb2 is not needed. As shown in Fig. 9 C, such a parameter region exists.

<a id='ed2ebbee-047e-4559-b315-1ac8190b41e8'></a>

Second, we are interested in the possibility that neither the positive feedback between Cdc28–Clb2 and Mih1 nor the negative effect of Cdc28–Clb2 on Swe1 is present. This possibility indeed exists for k′<sub>mih</sub> = k″<sub>mih</sub> = 1.5 and k‴<sub>swe</sub> = k′<sub>swe</sub> = 2 (Fig. 9 C).

<a id='52bae8e7-9a65-41a6-9500-8d139eabc554'></a>

In Fig. 9 D, we show that when both Swe1 and Mih1 are regulated (the two parameters varied in this analysis are k'swe and k'mih, whereas k''swe = k'swe/10 and k''mih = k'mih/10), the model is consistent with the data on all 13 genotypes for k'mih/k'swe ≈ 1.5. Parameter analysis (unpublished data) reveals that this region of consistency is ~50% larger than in the completely unregulated model (i.e., k'mih = k''mih and k''swe = k'swe).
For this reason, we prefer a model in which both Swe1 and Mih1 activities are affected by phosphorylation by Cdc28-Clb2. In addition, this preference is consistent with known properties of Swe1 and Mih1 homologues in fission yeast (Tang et al., 1993) and Xenopus laevis (Izumi et al., 1992).

<a id='7fa80771-63c7-4643-ad09-ae27fe306bc6'></a>

<::Figure 9: Four 3D surface plots showing parameter analysis. Each plot displays the number of successfully simulated genotypes (z-axis) as two parameters are varied (x and y axes). Black contour lines at level 12.5 encircle regions where all 13 genotypes have been successfully simulated. A: A 3D surface plot with 'Kswe"' on one horizontal axis ranging from 0 to 0.8, 'Kmih'' on the other horizontal axis ranging from 4 to 6, and a vertical axis ranging from 0 to 13. The surface shows a peak around Kswe" = 0.4 and Kmih' = 5. B: An enlargement of plot A. The 'Kswe"' axis ranges from 0 to 0.04, 'Kmih'' from 4.5 to 5.5, and the vertical axis from 0 to 13. The surface shows a plateau at the top. C: A 3D surface plot with 'Kswe''' on one horizontal axis ranging from 0 to 2, 'Kmih'' on the other horizontal axis ranging from 0 to 3, and a vertical axis ranging from 0 to 13. The surface shows a peak and a valley, with a black contour line indicating a region of high success. D: A 3D surface plot with 'Kswe''' on one horizontal axis ranging from 0 to 2, 'Kmih'' on the other horizontal axis ranging from 0 to 6, and a vertical axis ranging from 0 to 10. The surface shows a distinct peak.::>Figure 9. Parameter analysis. The number of successfully simulated genotypes (to within ±20% of experimental results) changes with parameter values. Each node of the grids corresponds to a simulation run. Black contour lines (at level 12.5) encircle regions of parameter space where all 13 genotypes have been successfully simulated. (A) The activity of Swe1M, k''swe1, is varied against the activity of Mih1*, k'mih. (B) Enlargement of A. (C) PSwe1 kinase activity k'''swe1 is varied simultaneously with unregulated Mih1 activity k''mih = k'mih. (D) Both Swe1 and Mih1 are regulated, k'''mih = k'mih/10 and k'''swe = k''swe/10.

<a id='5b7d4eb8-b061-4c1b-9c86-77a6c3b6481a'></a>

Summarizing, parameter analysis shows that, for our
model to be consistent with the data in Table I, Swe1M has
to be less active than Swe1, but phosphorylation-dependent
inactivation of Swe1 and activation of Mih1, although
present in the model, can be relaxed.

<a id='717988f0-06a7-426e-b90a-5c6fe4b34fa4'></a>

## Discussion
When bud formation is impaired, the morphogenesis checkpoint delays ND to allow for a bud to be formed. The molecular mechanism underlying this G2 delay relies on the antagonism between Swe1 and Cdc28–Clb2. These two protein kinases inhibit each other, and engagement of the checkpoint depends on the outcome of their fight. During a normal cell cycle, Cdc28–Clb2 is able to overcome Swe1 activity, whereas when bud formation is impaired, Swe1 is stabilized and active, and the cell cycle is delayed in G2 phase. The morphogenesis checkpoint inhibits the activity of Cdc28–Clb2 in two different ways. First, because bud formation is impaired, Hsl1 cannot act to inhibit Swe1 and to label it for degradation. Moreover, if actin cannot polymerize, then a second inhibitory signal impinges on the cell cycle through a MAPK pathway, whose ultimate effect is to alter the ratio of activities of Mih1 and Swe1 (by inactivating Mih1, or possibly by activating Swe1). Reviewing the current literature, we have formulated a hypothesis (wiring diagram) of the way these genes and proteins interact.

<a id='c06ca98b-6a90-466c-ab91-3b46028cecad'></a>

The main objective of our analysis is to verify whether the proposed mechanism can reproduce in quantitative detail the relevant experimental data. Because intuition and qualitative arguments are inadequate to predict the behavior of the complex network controlling yeast cell cycle dynamics (Fig. 1) and the morphogenesis checkpoint (Fig. 2), we have tried to put this problem in a rigorous mathematical context.

<!-- PAGE BREAK -->

<a id='d6a19b01-7f6f-4e8b-bc90-4c7f66db6f5b'></a>

Mathematical model of the morphogenesis checkpoint | Ciliberto et al.

<a id='1c465557-178c-4ceb-80b4-5d19dee27fb2'></a>

1251

<a id='77c56005-de10-45a3-961b-b35bbe3efbf4'></a>

## Model's assumptions
The molecular network controlling yeast cell cycle dynamics has been studied in detail (Chen et al., 2000), and the wiring diagram we use to describe it is simple but effective. On the other hand, the network we propose for the morphogenesis checkpoint is based on three assumptions that have not been experimentally verified: (1) Swe1 is inactivated when phosphorylated by Cdc28–Clb2; (2) Cdc28–Clb2 and Mih1 activate each other (a positive feedback loop); and (3) Swe1 is inactivated by a posttranslational modification introduced (indirectly) by Hsl1.

<a id='c0c87404-a4c4-406a-995a-b0fdc1c873b4'></a>

Performing a parameter analysis to investigate the extent to which these assumptions can be relaxed, we discovered that the first and second are not necessary to explain the phenotypes of the checkpoint mutants we are studying. This result is somehow surprising because assumptions 1 and 2 are based on clear experimental evidence in X. laevis and S. pombe. It is possible that these assumptions will be needed in the future, when more experiments characterizing the morphogenesis checkpoint must be taken into account. We decided to include them in the basal parameter set, because of analogies with other organisms and because these assumptions make the model more robust.

<a id='041cd122-f01e-4db7-8134-14eb880c43cd'></a>

As for the third assumption, parameter analysis shows that it cannot be relaxed. In particular, D.J. Lew (personal communication) showed that *clb2Δ hsl1Δ* cells are larger than *clb2Δ mih1Δ* cells. This observation poses a strict constraint on the activity of Swe1M, the Hsl1-modified form. Were this constraint ignored, the other data in Table I would permit a larger activity for Swe1M. Nonetheless, even without this constraint some regulation of Swe1M activity is required, as other genotypes fail when Swe1M activity reaches 20% of Swe1 activity. Summarizing, our model predicts that Hsl1 indirectly inactivates Swe1 activity.

<a id='7cd774b1-b560-4167-925d-9d68ae4ff22b'></a>

The size difference between clb2Δ hsl1Δ and clb2Δ mih1Δ plays a crucial role in constraining parameter values of the model. For the basal parameter set we propose, clb2Δ hsl1Δ cells are only 21% larger than clb2Δ mih1Δ cells. The size differential cannot be made much larger without bringing the model into contradiction with some other property of the mutant set. Most parameter changes away from the basal set reduce the size differential and quickly bring the model's prediction below our acceptance threshold (size ratio >1.15). Given the importance of this observation in constraining the model, we suggest that the size ratio of these two mutants be measured accurately.

<a id='96602960-34e9-4576-a66c-81f9028274bc'></a>

# Model's behavior
According to the model, Swe1 can be present in four different forms, and the way Swe1 is distributed among these forms depends on whether the checkpoint is invoked or not. In wild-type cells, the morphogenesis checkpoint is normally switched off because as soon as the bud is formed Hsl1 is activated and Swe1 is converted into the inactive form, Swe1M. If *HSL1* is deleted, the unmodified Swe1 is able to phosphorylate and inactivate Cdc28. In this case, dephosphorylation of Cdc28 (i.e., the presence of Mih1) becomes necessary. On the other hand, if *MIH1* is deleted, Swe1 can still be converted into the doubly modified form (PSwe1M) and degraded. This basic difference between *mih1Δ* and

<a id='bf3d6008-4f36-4a29-b8ea-b85a40c3433c'></a>

hsl1Δ is particularly evident in the double mutants clb2Δ hsl1Δ and clb2Δ mih1Δ. These cells experience a G2 delay because they rely on Clb1 alone to enter mitosis. In hsl1Δ clb2Δ the delay lasts longer than in mih1Δ clb2Δ, because Swe1 cannot be converted into its modified inactive form Swe1M. Not surprisingly, when both HSL1 and MIH1 are deleted, the cell is blocked in G2.

<a id='d0a0aa4b-3931-4c05-8456-3aa06441f372'></a>

These behaviors set the stage for understanding the morphogenesis checkpoint. A cdc24^ts cell has a similar, but milder, phenotype than a mih1Δ hsl1Δ cell, as we assume that the signal transduction pathway operating through Mpk1 does not completely inhibit Mih1. Therefore, the G2 block in mih1Δ hsl1Δ becomes a G2 delay in cdc24^ts. After a time the checkpoint-induced cell (cdc24^ts) undergoes adaptation, i.e., ND without bud formation. The selective advantages of this control loop are clear: becoming dinucleate is to be avoided, if possible, but it is better than death.

<a id='7098486e-dd7f-4279-b32a-0919904c661c'></a>

Bifurcation diagrams
The morphogenesis checkpoint acts like a "governor" to the cell cycle engine, slowing progression through the cell cycle when a particular danger signal (failure to bud) is perceived. To understand the relationship between the engine and its governor, it is useful to introduce the notion of a bifurcation diagram. In Fig. 10, we plot Cdc28-Clb2 activity (the state of the engine) as a function of cell size (the motive force for cell cycle progression in yeast; see Bifurcation analysis, available at http://www.jcb.org/cgi/content/full/jcb.200306139/ DC1; Tyson et al., 2001, 2002). Under normal conditions (Fig. 10 A), the Cdc28-control system has two characteristic states: a stable steady state (at small size) and a stable oscillatory state (at large size). A small newborn cell is attracted to the stable steady state of low Cdc28-Clb2 activity; kept low by active Cdh1 and Sic1 (Fig. 1). The cell is trapped in G1 because it is too small to warrant a new round of DNA replication and division. When the cell grows to a critical size (Fig. 10 A, mass = 1), the stable steady state is lost, and the cell cycle engine begins an oscillation that drives Cdc28-Clb2 to larger activity. The cell replicates its DNA and enters mitosis. The mitotic state is intrinsically unstable, because high levels of Cdc28-Clb2 turn on Cdc20, which destroys Cdc28's cyclin partner. As Cdc28 activity drops, the cell divides and the control system is reset to the domain of the stable steady state. The duration of the budded phase (S-G2-M) is fixed at ~60 min, the time it takes to complete one oscillation. The duration of G1 phase is variable, depending on growth rate and asymmetry of division.

<a id='9798521e-5ae5-414d-a2d0-549d55a7641d'></a>

When the morphogenesis checkpoint is invoked (no bud),
active Swe1 creates a second stable steady state of the cell cy-
cle engine at intermediate Cdc28-Clb2 activity (higher than
the G1 steady state, lower than the peak of the oscillation;
Fig. 10 B). Cdh1 and Sic1 are gone, Cdc28-Cln activity is
high, and Cdc28-Clb2 activity is depressed by Swe1-depen-
dent tyrosine-phosphorylation. High activity of Cdc28-Cln
drives the cell into DNA synthesis, but low activity of
Cdc28-Clb2 is insufficient for mitosis. Hence, the interme-
diate steady state corresponds to a cell stuck in G2. A new-
born daughter cell will grow to mass = 1 and enter S phase,
as usual. But then it arrests in G2 phase until it grows large
enough to bypass the G2 arrest and enter mitosis. The delay

<!-- PAGE BREAK -->

<a id='a14a65a9-e12f-4bf2-8b1b-4c0a5a6f20cc'></a>

1252 The Journal of Cell Biology | Volume 163, Number 6, 2003

<a id='2f77db0b-40cd-4cda-806d-aa541c55c31e'></a>

A<::Bifurcation diagram labeled 'A' with 'Cdc28/Clb2 activity' on the y-axis (log scale from 0.01 to 1) and 'mass' on the x-axis (from 0.5 to 4). A dashed line represents Cdc28/Clb2 activity, showing a low stable state (gray bar) from mass 0.5 to ~1, a sharp increase around mass 1, and a high activity range (gray vertical arrows) from mass 1 to 4. Another gray bar indicates a higher stable state around 0.1 activity, starting around mass 0.7. Below the x-axis, cell cycle phases are labeled: 'G1' from mass 0.5 to 1, and 'S-G2-M' from mass 1 to 4.:chart::>

B<::Bifurcation diagram labeled 'B' with 'Cdc28/Clb2 activity' on the y-axis (log scale from 0.01 to 1) and 'mass' on the x-axis (from 0.5 to 4). A dashed line represents Cdc28/Clb2 activity, showing a low stable state (gray bar) from mass 0.5 to ~1, an increase around mass 1, a higher stable state (gray bar) from mass ~0.7 to ~2, and oscillatory behavior (gray vertical arrows and dashed line) from mass 2 to 4. Below the x-axis, cell cycle phases are labeled: 'G1' from mass 0.5 to 1, 'S' around mass 1, 'G2 delay' from mass 1 to 2, 'M' around mass 2, 'G1' around mass 2, and 'S-G2-M' from mass 2 to 4. Additional labels below the x-axis include 'dinucleate' and 'tetranucleate re-replicate' with arrows pointing to specific mass values.:chart::>

Figure 10. Bifurcation diagrams for the cell cycle engine. We plot Cdc28–Clb2 activity, representative of the state of the cell cycle control system against cell mass, which is the driving force for

<a id='89b7d880-726a-47af-bf23-57fa7e6fa5ef'></a>

Figure 10. Bifurcation diagrams for the cell cycle engine. We plot Cdc28-Clb2 activity, representative of the state of the cell cycle control system, against cell mass, M, which is the driving force for progression through the cell cycle. That is, for a fixed value of M, we solve the differential equations in Table S1 until the control system reaches a stable, self-maintaining state, which is either a steady state (no further change in activities of the regulatory proteins) or an oscillatory state (perfectly repeated fluctuations of their activities). Horizontal bars are placed at the Cdc28-Clb2 level characteristic of steady states, and vertical arrows represent the range of fluctuations of Cdc28-Clb2 activity in an oscillatory state. These diagrams are schematic cartoons; for accurately computed bifurcation diagrams, see online supplemental material (Bifurcation analysis) and Fig. S1. Notice the axes are scaled logarithmically. Because we assume cells grow exponentially, equal distances along the log(mass) axis repre- sent equal intervals of time. Along the log(activity) axis we associate low activity with G1, intermediate activity with S-G2, and high activity with M phase. (A) Checkpoint silent. The bold dashed line is a cell-cycle trajectory: as the cell grows, the Cdc28 control system is attracted to the stable, self-maintaining state at its current cell mass. A small cell persists in the G1-state until that state disappears at M = 1. Thereafter, the cell executes an oscillation in Cdc28-Clb2 activity, passing through S, G2 and M phases. When Cdc28 activity falls, as the cell exits mitosis, the cell divides and the newborn progeny are attracted to the stable G1-state. (B) Checkpoint invoked. At the restrictive temperature, a cdc24ts cell continues to grow but fails to make a bud. Consequently, Swe1 is stabilized, and a new self- maintaining steady state, with intermediate activity of Cdc28-Clb2, is created. The cell arrests in S-G2 phase for about one mass-doubling time, until it grows to M = 2, where the G2-arrested state disappears. At this time, the cell adapts to the checkpoint signal, enters mitosis, and becomes dinucleate. Because the cell does not divide, it stays in the oscillatory regime and rereplicates its DNA after a very short G1 phase. The cell reenters mitosis and becomes tetranucleate. The time between NDs is the period of the underlying oscillatory state, ~60 min in the model.

<a id='d5a451ba-6aca-45da-a3c0-537792f456ed'></a>

will be 2–3 h, depending on growth rate and critical mass at the end of the G2-arrested state. When the cell reaches this size (Fig. 10 B, mass = 2), it adapts to the checkpoint, un-dergoes ND, and becomes dinucleate (the cell cannot divide because it never made a bud). At this point the model makes a noteworthy prediction. Because the engine is still in the os-cillatory domain, it will pause only briefly in G1, then rerep-licate its DNA and enter mitosis, becoming tetraploid (Sia et al., 1996). To see the predicted shortening of G1 phase, this experiment is best done at slow growth rates, for which the duration of G1 phase is usually long.

<a id='52d032cb-7797-4dc4-9987-e2eba6484246'></a>

Summary of the model's predictions and suggestions
The model makes two particularly clear and unexpected predictions. Regarding Hsl1 kinase, it is evidently involved in Swe1 degradation because Swe1 is stable in _hsl1Δ_ (deletion) mutants and Swe1 is degraded more rapidly in _HSL1OP_ (overproduction) mutants (McMillan et al., 1999a). The effect is indirect, because Swe1 does not appear to be a substrate for Hsl1 (Cid et al., 2001). Our model calculations show that, in order to account for known dynamical features of the checkpoint mutants in Table I, Hsl1-dependent modification of Swe1 (whatever it may be) must also inhibit Swe1 kinase activity by at least 80%. To test this prediction will require reliable assays of Swe1 kinase activity, which are currently under development in Lew's laboratory (Lew, D.J., personal communication). Regarding adaptation, it is well known that _cdc24ts_ cells, which cannot bud at the restrictive temperature, will nonetheless, after several hours delay, proceed through mitosis and become dinucleate. The model predicts that these cells will rereplicate their DNA soon after ND. To readily observe the predicted shortening of G1 phase, cell growth should be restricted, so that unperturbed daughter cells have a long G1 period.

<a id='2244064f-dfbe-4a13-947f-f520b8a0eff0'></a>

The model can be used to predict mutant phenotypes (such as the many blank spaces under the E columns in Table I). Right or wrong, such predictions are handy in designing experiments and extremely valuable in interpreting the behavior of newly characterized mutants in the context of all previously studied mutants (Cross, 2003). In addition, the values assigned to most of the kinetic parameters in Table S2 are predictions. In our experience, similar predictions made on the cell cycle regulatory system of frog eggs proved to be remarkably accurate (Marlovits et al., 1998).

<a id='a254adcb-6142-466d-b7f6-656ab7c7f3f3'></a>

The model also points to other experiments that would provide critical information for refining our understanding of the morphogenetic checkpoint. For instance, first, we would like to have precise measurements of the sizes of clb2Δ mih1Δ and clb2Δ hsl1Δ cells, because these numbers would provide strict constraints on the parameters in the model. Second, we would like to know whether Cdc28–Clb2 and Mih1 are indeed involved in a positive feedback loop in budding yeast, or not. The mutant phenotypes in Table I are insufficient to resolve this issue. Third, the kinase activity of PSwe1 relative to Swe1 should be measured, to resolve the uncertainty about this ratio. Finally, for future modeling purposes, it would be nice to know whether the MAPK pathway acts by down-regulating Mih1 or up-regulating Swe1.

<!-- PAGE BREAK -->

<a id='43632111-d5a0-47d5-93aa-3291318b3eac'></a>

Mathematical model of the morphogenesis checkpoint | Ciliberto et al. 1253

<a id='68db142c-7665-4bbf-92c5-7c214c384f7a'></a>

## Morphogenesis checkpoint or size control?
Harvey and Kellogg (2003) have recently challenged the notion of a “morphogenesis checkpoint,” claiming that Lew's data are rather a consequence of a size control checkpoint in G2 phase of the budding yeast cell cycle. Because *swe1Δ* cells are slightly smaller than wild-type cells, they propose that wild-type budding yeast cells, like fission yeast, have a size requirement for passing from G2 into M phase, as well as a size requirement for Start (G1-S transition). Harvey and Kellogg (2003) suggest that the G2 size requirement can be met only by bud growth (not by continued expansion of the mother cell). Hence, when bud formation or growth is blocked (by the *cdc24ts* mutation or by Latrunculin-A treatment, respectively), the cell finds it difficult or impossible to meet the G2 size requirement, and so mitosis is delayed or blocked completely. In this view, there is no such thing as a morphogenesis checkpoint particular to budding yeast cells; the phenomenon is just a consequence of a minimum size for the G2-M transition and growth problems in cells that lack buds.

<a id='40f2c64d-67ed-4af1-aee5-31d2f1ccef7e'></a>

In Lew's view and in our model (Fig. 10 A), the primary size requirement for wild-type cells is at Start (the G1-S transition). After passing Start, cells normally pass through S into M (without stopping in G2) and back to G1. A G2-M size requirement manifests itself only when bud formation is blocked (Fig. 10 B).

<a id='090df22f-7e5f-4dad-99a8-b56cf87a2150'></a>

The fundamental difference between these two views is whether bud failures impair progress toward a minimum bud size for the G2-M transition (Kellogg's view) or create a large threshold for entering into M phase (Lew's view). Both views can explain equally well the observation that actin dis- ruption (by treatment with Latrunculin-A) delays mitotic entry indefinitely. The two views give very different ac- counts of cell cycle mutants. In Lew's picture, when a bud fails to form, a surveillance mechanism, involving Hsl1 and Mpk1, creates a stable G2-arrested steady state (Fig. 10 B), by activating Swe1 and inhibiting Mih1. The cdc24ts cell continues to grow at the restrictive temperature, but it must now satisfy a large size requirement for passing from G2 into M phase. After a characteristic delay, the cell enters M phase and becomes dinucleate.

<a id='488f96ec-6c90-4af7-84e1-4acd101193db'></a>

In Kellogg's picture, it is difficult to explain why *cdc24*^ts
cells, which fail to make a bud at all, are only delayed in en-
tering mitosis. Why is not mitosis delayed indefinitely, as in
Latrunculin-treated cells? In this case, some fraction of
mother cell growth must count toward meeting the G2-M
transition size. Kellogg's view also cannot explain why
*mih1*Δ causes strikingly different effects in *CDC24* and
*cdc24*^ts backgrounds (no delay in cell cycle progression and
cell cycle block, respectively).

<a id='005bd4d3-475e-4914-a25e-25fb29a74599'></a>

As we have shown by mathematical modeling, the concept of a morphogenesis checkpoint (with the assumption that Hsl1 down-regulates Swe1 activity) is compatible with most of the observed phenotypes of cdc24ts cells. Just like check-points for damaged or unreplicated DNA or for spindle de-fects, the morphogenesis checkpoint responds to a signal (bud failure) by arresting the cell cycle engine in a stable steady state. The arrest can be bypassed if the cell grows large enough, which is a common feature of other checkpoint mechanisms (Toczyski et al., 1997).

<a id='50d26b1b-8823-441f-a583-47e041e246a6'></a>

# Materials and methods

## Simulations

The differential equations (Table S1) were solved numerically using XPP, which is software developed by Bard Ermentrout and freely downloadable from his FTP site (http://www.math.pitt.edu/~bard/xpp/xpp.html). We used the CVODE integration method provided by XPP, with the default settings for the integration parameters, except relative tolerance = absolute tolerance = 3 \u00d7 10-16. The model's ".ode" file (input to XPP) is provided as online supplemental material (see Ciliberto_XPP.zip), available at http://www.jcb.org/cgi/content/full/jcb.200306139/DC1.

<a id='f09979da-72d9-46d5-a3fb-5aef2ca8df71'></a>

## Parameter search
To investigate the sensitivity of the model to kinetic constants in the Swe1 box (Fig. 2), we chose two parameters from the box to vary simultaneously. For each pair of parameter values, we computed the model's predictions of the data reported in Table I. Each simulated data point (call it Rsim, R for results) is checked against the corresponding experimental observation (call it Rexp). If | Rsim - Rexp | / Rexp <0.2, we assume that the simulation "fits" the experimental result, otherwise it does not.

<a id='8e7c45c7-64d6-4b85-b5e0-55789eea59ae'></a>

In Table I are reported data for 14 different genotypes, the wild type plus 13 mutants. Some genotypes are characterized by more than one experimental observation: we assume that a simulated genotype fits an observed genotype only if all of its characteristics have been reproduced to within ±20%. For example, in _GAP-SWE1_ two conditions have to be matched: ND in cells arrested with α-factor has to occur between 60 and 90 min, and ND in _cdc24ts_ cells arrested in α-factor has to occur between 141.6 and 94.4 min. Because we do not know precisely how much larger _clb2Δ hsl1Δ_ cells are than _clb2Δ mih1Δ_ cells, we assume that the simulated result is satisfactory if _clb2Δ hsl1Δ_ is at least 15% larger than _clb2Δ mih1Δ_. A successful simulation should fit all 14 genotypes. Because _clb2Δ mih1Δ_ and _clb2Δ hsl1Δ_ are grouped together (the experimental result is the ratio of their sizes), the number of independent genotypes is 13.

<a id='31a707ce-1d6b-4aba-ac6a-eaec5cae5a78'></a>

Summarizing, parameter search is performed in the following way: ex-perimental data reproduced in Table I are computed for each parameter set. Simulations are compared with experimental data for each of the ge-notypes. If all data characterizing a particular genotype are within ±20% of experimental results, that particular genotype fits experimental data. When every genotype has been computed, a natural number in the inter-val [0,13] is associated with the parameter set, according to the number of genotypes that have been successfully reproduced.

<a id='e79fbed8-df29-484f-b33e-679aa7fb4fd3'></a>

## Online supplemental material
Online supplemental material includes description of the experimental basis for the model and bifurcation analysis. Also, differential equations (Table S1) and initial conditions and parameter values (Table S2) are provided. Ciliberto_XPP.zip contains the ".ode" file of the model equations and parameter values for use with XPP, as well as .set files appropriate for each of the figures. All online supplemental material is available at http://www.jcb.org/cgi/content/full/jcb.200306139/DC1.

<a id='14c5eaae-662f-44a0-bf2b-668b7515abab'></a>

We thank Daniel Lew, Attila Csikasz-Nagy, Kathy Chen, and Jason Zwolak
for much useful advice as we formulated the model, and Daniel Lew for
sharing unpublished results with us.

<a id='f41ee4ea-647b-444b-8003-55ee69e7ef9f'></a>

This work has been supported by the Defense Advanced Research
Project Agency (grant AFRL F30602-02-0572), the James S. McDonnell
Foundation (grant 21002050), and the National Science Foundation of
Hungary (grant T 032015). We thank the Collegium Budapest and the
Volkswagen Stiftung for a pleasant environment in which to prepare this
work for publication.

<a id='736df05d-8aca-47bb-86a6-a3ba4a6e918d'></a>

Submitted: 25 June 2003
Accepted: 30 October 2003

<a id='c256e449-bd08-47f0-a11e-5def8a59efac'></a>

## References

Amon, A., U. Surana, I. Muroff, and K. Nasmyth. 1992. Regulation of p34CDC28 tyrosine phosphorylation is not required for entry into mitosis in S. cerevisiae. Nature. 355:368-371.

Booher, R.N., R.J. Deshaies, and M.W. Kirschner. 1993. Properties of Saccharomyces cerevisiae wee1 and its differential regulation of p34cdc28 in response to G1 and G2 cyclins. EMBO J. 12:3417-3426.

Chen, K.C., A. Csikasz-Nagy, B. Gyorffy, J. Val, B. Novak, and J.J. Tyson. 2000. Kinetic analysis of a molecular model of the budding yeast cell cycle. Mol. Biol. Cell. 11:369-391.

<!-- PAGE BREAK -->

<a id='ee92fa2c-af43-48f6-80cf-43a7a572f75a'></a>

1254 The Journal of Cell Biology | Volume 163, Number 6, 2003

<a id='b2726be4-b7fb-4d96-b4f9-542d7f1ce71f'></a>

Cid, V.J., M.J. Shulewitz, K.L. McDonald, and J. Thorner. 2001. Dynamic localization of the Swe1 regulator Hsl7 during the *Saccharomyces cerevisiae* cell cycle. *Mol. Biol. Cell.* 12:1645–1669.
Cross, F.R. 2003. Two redundant oscillatory mechanisms in the yeast cell cycle. *Dev. Cell.* 4:741–752.
Cross, F.R., V. Archambault, M. Miller, and M. Klovstad. 2002. Testing a mathematical model for the yeast cell cycle. *Mol. Biol. Cell.* 13:52–70.
Dirick, L., T. Bohm, and K. Nasmyth. 1995. Roles and regulation of Cln-Cdc28 kinases at the start of the cell cycle of *Saccharomyces cerevisiae*. *EMBO J.* 14: 4803–4813.
Enoch, T., and P. Nurse. 1991. Coupling M phase and S phase: controls maintaining the dependence of mitosis on chromosome replication. *Cell.* 65:921–923.
Goldbeter, A., and D.E. Koshland, Jr. 1981. An amplified sensitivity arising from covalent modification in biological systems. *Proc. Natl. Acad. Sci. USA.* 78: 6840–6844.
Harrison, J.C., E.S. Bardes, Y. Ohya, and D.J. Lew. 2001. A role for the Pkc1p/ Mpk1p kinase cascade in the morphogenesis checkpoint. *Nat. Cell Biol.* 3:417–420.
Hartwell, L.H., and T.A. Weinert. 1989. Checkpoints: controls that ensure the order of cell cycle events. *Science.* 246:629–634.
Harvey, S.L., and D.R. Kellogg. 2003. Conservation of mechanisms controlling entry into mitosis: budding yeast Wee1 delays entry into mitosis and is required for cell size control. *Curr. Biol.* 13:264–275.
Izumi, T., D.H. Walker, and J.L. Maller. 1992. Periodic changes in phosphorylation of the *Xenopus cdc25* phosphatase regulate its activity. *Mol. Biol. Cell.* 3:927–939.
Kaiser, P., R.A. Sia, E.G. Bardes, D.J. Lew, and S.I. Reed. 1998. Cdc34 and the F-box protein Met30 are required for degradation of the Cdk-inhibitory kinase Swe1. *Genes Dev.* 12:2587–2597.
Lew, D.J. 2000. Cell-cycle checkpoints that ensure coordination between nuclear and cytoplasmic events in *Saccharomyces cerevisiae*. *Curr. Opin. Genet. Dev.* 10:47–53.
Lew, D.J., and S.I. Reed. 1995. A cell cycle checkpoint monitors cell morphogenesis in budding yeast. *J. Cell Biol.* 129:739–749.
Marlovits, G., C.J. Tyson, B. Novak, and J.J. Tyson. 1998. Modeling M-phase control in *Xenopus* oocyte extracts: the surveillance mechanism for unreplicated DNA. *Biophys. Chem.* 72:169–184.
McMillan, J.N., R.A.L. Sia, and D.J. Lew. 1998. A morphogenesis checkpoint

<a id='a5241d80-2122-4a49-9930-784b474f6d06'></a>

monitors the actin cytoskeleton in yeast. _J. Cell Biol._ 142:1487–1499.
McMillan, J.N., M.S. Longtine, R.A.L. Sia, C.L. Theesfeld, E.S.G. Bardes, J.R.
Pringle, and D.J. Lew. 1999a. The morphogenesis checkpoint in _Saccharo-
myces cerevisiae_: cell cycle control of Swelp degradation by hsl1p and hsl7p.
_Mol. Cell. Biol._ 19:6929–6939.
McMillan, J.N., R.A.L. Sia, E.S.G. Bardes, and D.J. Lew. 1999b. Phosphoryla-
tion-independent inhibition of Cdc28 by the tyrosine kinase swelp in the
morphogenesis checkpoint. _Mol. Cell. Biol._ 19:5981–5990.
McMillan, J.N., L.T. Chandra, J.C. Harrison, E.S.G. Bardes, and D.J. Lew. 2002.
Determinants of Swelp degradation in _Saccharomyces cerevisiae_. _Mol. Biol.
Cell._ 13:3560–3575.
Morgan, D.O. 1995. Principles of Cdk regulation. _Nature_. 374:131–134.
Nurse, P. 1999. Cyclin dependent kinases and regulation of the fission yeast cell
cycle. _Biol. Chem._ 380:729–733.
Russell, P., S. Moreno, and S.I. Reed. 1989. Conservation of mitotic controls in
fission and budding yeast. _Cell._ 57:295–303.
Sia, R.A.L., H.A. Herald, and D.J. Lew. 1996. Cdc28 tyrosine phosphorylation
and the morphogenesis checkpoint in budding yeast. _Mol. Biol. Cell._
7:1657–1666.
Sia, R.A.L., E.S.G. Bardes, and D.J. Lew. 1998. Control of Swelp degradation by
the morphogenesis checkpoint. _EMBO J._ 17:6678–6688.
Sorger, P.K., and A.W. Murray. 1992. S-phase feedback control in budding yeast in-
dependent of tyrosine phosphorylation of p34cdc28. _Nature_. 355:365–368.
Tang, Z., Z.R. Coleman, and W.G. Dunphy. 1993. Two distinct mechanisms for
negative regulation of the Weel protein kinase. _EMBO J._ 12:3427–3436.
Theesfeld, C.G., T.R. Zyla, E.G. Bardes, and D.J. Lew. 2003. A monitor for bud
emergence in the yeast morphogenesis checkpoint. _Mol. Biol. Cell._ 14:
3280–3291.
Toczyski, D.P., D.J. Galgoczy, and L.H. Hartwell. 1997. CDC5 and CKII control
adaptation to the yeast DNA damage checkpoint. _Cell._ 90:1097–1106.
Tyson, J.J., and B. Novak. 2001. Regulation of the eukaryotic cell cycle: molecu-
lar antagonism, hysteresis, and irreversible transitions. _J. Theor. Biol._ 210:
249–263.
Tyson, J.J., K. Chen, and B. Novak. 2001. Network dynamics and cell physiology.
_Nat. Rev. Mol. Cell Biol._ 2:908–916.
Tyson, J.J., A. Csikasz-Nagy, and B. Novak. 2002. The dynamics of cell cycle reg-
ulation. _Bioessays._ 24:1095–1109.

# Supplementary materials

<a id='4ce5a75d-f19f-44a7-ab2b-82b34c9eb95e'></a>

JCB Online Supplemental Material
Ciliberto et al. http://www.jcb.org/cgi/doi/10.1083/jcb.200306139

<a id='0873232a-ee56-4d21-ab15-f7fa31dd99e5'></a>

**Experimental basis of the model**
The morphogenesis checkpoint acts through inhibitory phosphorylation of Cdc28 on Tyr19 (Booher et al., 1993). During the normal cell cycle, Mih1 is more active than Swe1 and phosphorylation of Tyr19 is negligible. When bud formation is impaired, the morphogenesis checkpoint stabilizes Swe1 and inactivates Mih1.

<a id='8ef044a4-e244-42f3-ba79-b9f4c337174d'></a>

Swe1. Swe1 level oscillates during the cell cycle, with a peak in S/G2 (Sia et al., 1998; McMillan et al., 1999). Both the synthesis and degradation of Swe1 are cell-cycle regulated. SWE1 transcription is controlled by SBF. Because Cdc28-Clb2 inhibits SBF, SWE1 mRNA peaks in G1 and bottoms out in G2-M. In addition, Swe1 protein is stable during G1 (t1/2 = 90 min), whereas during G2 phase it is seven times more unstable (Sia et al., 1998). Although the regulation of Swe1 degradation has not been completely determined, it is clear that Cdc28-Clb2 and Hsl1 are both required for Swe1 degradation (Lew, 2000).

<a id='145ef057-b619-4d54-99e9-314b4f49a90a'></a>

**Cdc28–Clb2.** Cdc28 level does not fluctuate during the cell cycle, but Clb2 level does. Clb2 is synthesized during G2/M, when the _CLB2_ transcription factor, Mcm1, is active (Amon et al., 1993). Clb2 is rapidly degraded by the anaphase promoting complex as cells exit mitosis (Irniger et al., 1995). Cdc28–Clb2 activity is required for Swe1 degradation, as Swe1 is unstable in the _GAL-SWE1 CDC28Y19F_ mutant and is stabilized in the _GAL-SWE1 GAL-SIC1 CDC28Y19F_ mutant (Sia et al., 1998). (Sic1 is a stoichiometric inhibitor of Cdc28–Clb1-6 dimers.)

<a id='3fb14262-12ac-4929-96e1-9c50c5650c0a'></a>

**Hsl1 and Hsl7.** Hsl1 (related to *Schizosaccharomyces pombe* Nim1) and Hsl7 (a presumptive protein-arginine methyltransferase) are also involved in Swe1 degradation because Swe1 is stable both in *GAL:SWE1 CDC28Y19F hsl1\u0394* and in *GAL:SWE1 CDC28Y19F hsl7\u0394* (McMillan et al., 1999). Hsl1 controls the rate-limiting step of the degradatory process as *HSL1* overexpression speeds up Swe1 degradation, whereas *HSL7* overexpression does not (McMillan et al., 1999). It has been suggested that the localization of these two proteins is essential for their activity (Shulewitz et al., 1999; Lew, 2000; Longtine et al., 2000); once the bud is formed, Hsl1 localizes to the mother-bud neck where it recruits Hsl7, which acts as a bridge between Hsl1 and Swe1. Colocalization of Swe1, Hsl1, and Hsl7 at the mother-bud neck is required for Hsl1\u2013Hsl7 to induce Swe1 degradation because mutants with impaired septin organization show a *SWE1*-dependent G2 delay (Barral et al., 1999). If bud formation is impaired, then septins do not assemble on the neck, Hsl1 and Hsl7 are not properly localized and activated, and Swe1 is not degraded.

<a id='218365c9-1e5e-44ff-978d-2c93303741f8'></a>

During normal growth, Swe1 stabilization is not sufficient to alter significantly the cell cycle, according to Lew and coworkers, who report that both _hsl1Δ_ and _hsl7Δ_ do not show any phenotypic difference compared with wild-type cells (McMillan et al., 1999). On the other hand, other researchers report an elongated bud phenotype and G2 delay for these mutants (Ma et al., 1996; Tanaka and Nojima, 1996). It has been proposed that the difference resides in the amount of Mih1 present in the cell because stationary phase _hsl1Δ_ cells (i.e., low Mih1 level) are elongated whereas exponentially growing cells (i.e., high Mih1 level) are not (McMillan et al., 1999).

<a id='a747c74b-a0f5-4511-8fdf-79e222bdddc1'></a>

**Swe1 degradation pathway.** Summarizing the experimental data concerning Swe1 degradation, Cdc28–Clb2 and Hsl1–Hsl7 belong to the same Swe1 degradation pathway, and both of them are necessary but neither is sufficient for Swe1 degradation. Swe1 stability is greatly increased in _hsl1Δ CDC28Y19F_ (McMillan et al., 1999), i.e., Cdc28–Clb2 activity alone is not sufficient to induce Swe1 degradation. On the other hand, in a system where Cdc28–Clb2 activity is inhibited (_GAL-SIC1 CDC28Y19F_), Swe1 stability is enhanced (Sia et al., 1998), showing that Hsl1 alone cannot induce Swe1 degradation.

<a id='637d91d7-4976-4086-bf41-49e4a4aacf31'></a>

Mih1. Mih1, the budding yeast homologue of Cdc25 (Russell et al., 1989), is not essential for the normal cell cycle. Indeed, it was originally reported that *mih1*\u0394 is only 15% bigger than wild-type cells (Russell et al., 1989), and that these mutant show a short G2 delay (Booher et al., 1993). Moreover, *mih1*\u0394 and wild type are identical when treated under \u03b1-factor arrest and release (Sia et al., 1996).

<a id='5e52564e-8521-4e9b-ac47-a3b214fb5658'></a>

**Mih1 versus Hsl1.** Although the single mutants, _hsl1_\u0394 and _mih1_\u0394, are both perfectly viable and very similar to wild type, the double mutant _mih1_\u0394 _hsl1_\u0394 is lethal, blocked in G2 (McMillan et al., 1999). Apparently, either Hsl1\u2013Hsl7 or Mih1 is able to prevent Swe1 inhibitory activity on Cdc28\u2013Clb2, but when both these components are missing, Swe1 is able to phosphorylate Cdc28 and block cells in G2.

<a id='f2fb219c-6c7f-4b1c-80bd-44d3b8497a3b'></a>

## Bifurcation analysis
Molecular regulatory circuits in cell biology are governed by nonlinear dynamical systems, usually described in terms of ordinary differential equations. A powerful tool for analyzing the dynamical properties of such equations is bifurcation theory. Recently, Tyson et al. (2001, 2002) have pointed out the relevance of this tool to understanding cell cycle regulation. They show that progress through the yeast cell cycle is governed by a size threshold at G1-S (in budding yeast) or at G2-M (in fission yeast). Growth drives a cell past the threshold and through the chromosome replication-division cycle. Division brings cell size below the threshold, and the process repeats itself. When problems arise (e.g., with DNA replication or chromosome alignment), checkpoint mechanisms stabilize a steady state of the dynamical system (corresponding to arrest in G2 phase or metaphase,

<a id='d6ef184f-12c9-48d3-b053-8faa313aa1eb'></a>

The Journal of Cell Biology © The Rockefeller University Press • 0021-9525
Volume 163 December 22, 2003
http://www.jcb.org/cgi/doi/10.1083/jcb.200306139

<a id='c6aa7ae6-9217-4f44-8a9e-1101732d2da8'></a>

1 of 6

<!-- PAGE BREAK -->

<a id='7f095593-9336-44cf-8d56-5cb10e0d3d67'></a>

http://www.jcb.org/cgi/doi/10.1083/jcb.200306139

<a id='298aede4-6cd2-4e68-a4ae-a0b4d8b7c06c'></a>

2 of 6

<a id='7d2e7dee-4555-4f0d-b80f-85831cb87fd5'></a>

respectively). Cell cycle progression is delayed until the problem is fixed, or the cell grows large enough to override the checkpoint, or the cell dies. In this supplement, we show that the morphogenesis checkpoint, as modeled in this paper, has all the characteristic dynamical properties of more familiar checkpoint mechanisms.

<a id='afa36acb-189d-4a56-9bbf-a9b8633d93b4'></a>

**Dynamical systems.** Our model of the morphogenesis checkpoint consists of 19 differential equations (Table S1) plus a few auxiliary algebraic equations and "rules". The instantaneous state of the system is given by specific numerical values of the 19 time-dependent variables: [Clb2], [Cdc20], [Swe1P], [Cdh1], and so on. For a given set of initial conditions (the state of the system at t = 0), the differential equations determine how the state variables will evolve over time (we call their time courses a "cell-cycle trajectory"). Computation of a cell-cycle trajectory requires not only appropriate initial conditions, but also specifications of all the kinetic parameters that appear on the right-hand sides of the differential equations in Table S1 (_k_s,clb, _V_a,swe, and so on). Parameter values and initial conditions for our simulations are displayed in Table S2. The dependence of cell-cycle trajectories on parameter values and initial conditions has been addressed in the main text. For example, simulated _cdc24_ts cells undergo nuclear division later than simulated wild-type cells because certain crucial parameter values are smaller (in the former _k'_mih1 = 0.5, _k_"_mih1 = 0.05, and _k_hsl1 = 0, whereas in the latter _k'_mih1 = 5, _k_"_mih1 = 0.5, and _k_hsl1 = 1; see Table 1. As for initial conditions, although simulated _mih1_Δ cells (both cycling and synchronized with α-factor) share identical parameter values, synchronized cells undergo nuclear division earlier due to the difference in initial conditions (particularly, mass is larger in synchronized cells; see Other rules).

<a id='e6192143-8fca-4eb4-83f9-fd1346ecd820'></a>

Recurrent solutions. If we fix the parameter values in a system of nonlinear ODEs and vary the initial conditions, we will generate a set of trajectories (variables as function of time, t). As t gets large (t→ ∞), we find, in general, that the trajectories starting from many different initial conditions all converge to the same "recurrent" solution, that may be either a steady-state solution (all variables unchanging in time) or a periodic solution (all variables repeat themselves periodically in time). Such recurrent solutions are called "attractors" of the dynamical system. Recurrent solutions may also be "repellors" or "saddles" (Tyson et al., 2001, 2002). The qualitative properties of a dynamical system are determined in large part by the nature of its recurrent solutions. The characterization of these solutions is a branch of applied mathematics, called bifurcation theory.

<a id='2bb8a105-54db-40ee-b93a-e4952eba2351'></a>

Which are the recurrent solutions of the morphogenesis checkpoint model? Experimentally it is impossible to find steady-state solutions during the cell division process because cells are steadily growing and dividing. However, mathematically it is possible to find recurrent solutions of the molecular regulatory network underlying the cell cycle by fixing mass to a constant value (i.e., treating mass as a parameter) and allowing the system to settle down to steady or oscillatory solutions. Repeating this procedure for all physiologically relevant values of mass, it is possible to identify recurrent states of the cell cycle model as a function of mass (*M*). Notice the difference between cell-cycle trajectories and recurrent states: in the former, *M*(*t*) is a variable that increases steadily until cell division, and the molecular regulatory system never reaches a steady or oscillatory state. In recurrent states, *M* is a parameter and variables are unchanging or repeat periodically in time. Recurrent states for the cell cycle model lack an experimental counterpart, but they are useful for understanding the behavior of the dynamical system because they are the attractors of cell-cycle trajectories, as we shall see shortly.

<a id='d9388bf9-6b37-416c-9016-7a667c927c87'></a>

Bifurcation diagrams. A bifurcation diagram is a plot of the recurrent states of a dynamical system as a function of one of its parameters (called the bifurcation parameter). Bifurcation diagrams for wild-type, cdc24ts and hsl1Δ mih1Δ cells are plotted in Fig. S1. The activity of Cdc28–Clb2 is chosen as the variable representing the state of the control system, and M is the bifurcation

<a id='a0c38843-c632-4337-9c52-b6fd8aa503bc'></a>

Figure S1. Bifurcation diagrams for wild-type, *cdc24*^ts^, and *hsl1Δmih1Δ* cells. Recurrent states of Cdc28/Clb2 are plotted against fixed values of mass: stable and unstable steady-states (solid and dashed lines, respectively) and maxima and minima of the stable oscillatory states (top and bottom closed circles, respectively). In the left and middle panels a cell-cycle trajectory of Cdc28/Clb2 as a function of mass (dotted line) is superimposed on the bifurcation diagram. See accompanying text for details. (Left) In wild-type cells, for small values of mass, there is only one stable steady-state, which is the mathematical analogue of G1 phase. As mass increases to 0.3, two new unstable steady-states are born: this point (closed rectangle) is called a saddle-node bifurcation (SN₁). The region with three steady-states terminates at another saddle node, SN₂, at *M* = 1, after which there is only one unstable steady-state. In fact, a second type of bifurcation occurs at this point, called a SNIC bifurcation, which gives rise to stable oscillatory states (large amplitude, stable limit cycles). SN₂ represents the Start transition: when cell size (*M*) exceeds 1, the dynamical system enters S-G2-M, and is attracted toward the large amplitude limit cycles. (Middle) In *cdc24*^ts^ cells, G1 is followed by a new stable steady-state, G2, which is lost at a saddle node, SN₃, for *M* = 2.1. As in wild-type cells, a SNIC bifurcation occurs at this point as well. (Right) In *hsl1Δ mih1Δ* cells, the G2 state persists until nonphysiological cell size (*M* = 29), when it is lost by a saddle node bifurcation, SN₄.

<!-- PAGE BREAK -->

<a id='d31e279b-4709-4486-b442-bc09ed44521a'></a>

http://www.jcb.org/cgi/doi/10.1083/jcb.200306139

<a id='22d97a70-3ac6-4de6-b86c-42df60790d6a'></a>

3 of 6

<a id='d62130ed-6a9b-4c0e-9b13-a955a8afd411'></a>

parameter. In each panel of Fig. S1, we plot the value of [Clb2] on a recurrent solution as a function of M. For a steady-state solution, [Clb2]$_{\text{ss}}$ is a constant (for a fixed value of M), and as M changes, the point (M, [Clb2]$_{\text{ss}}$) traces a curve on the bifurcation diagram. In the left panel of Fig. S1 (wild-type cells), the curve of steady states is S-shaped. Where the "S" is a solid line, the steady states are attractors (also called "nodes") and where the S is a dashed line, the steady states are repellors or saddles. The turning points of the "S are called "saddle-node bifurcation points" (SN$_{1}$ and SN$_{2}$). For mass values larger than SN$_{2}$ there are not only unstable steady states, but also periodic recurrent solutions represented in Fig. S1 by maxima and minima of the oscillations (large black dots).

<a id='dc8c7373-5953-441b-a151-62c37e2ffbcb'></a>

Cdc28-Clb2 trajectories are superimposed on the bifurcation diagrams in the left and middle panels. To do this, we consult the cell-cycle trajectories of Figs. 3 and 7, where [Clb2] and M are plotted as functions of time. At t = 0, we read the values of [Clb2] and M, and place a small dot at the corresponding point on the [Clb2]-mass plane in Fig. S1. A short time later, say t = 1 min, we read new values of [Clb2] and M, and place a second dot on the [Clb2]-mass plane. Continuing in this way for ever larger values of t, we trace out a cell-cycle orbit (dotted line) on the [Clb2]-mass plane.

<a id='1bdbd30a-4a9c-405b-8000-2a10e498aeef'></a>

In wild-type cells, Fig. S1 (left), cell mass is small at the beginning of the cycle and the cell-cycle orbit (dotted line) is initially attracted to the G1 state, where Sic1 and Cdh1 successfully prevent any Cdc28–Clb2 activity in the cell. As mass grows to a critical threshold (Fig. S1, left, SN2), SBF is activated (biologically, this corresponds to the accumulation of a sufficient quantity of Cln3 in the nucleus) and the start transition occurs. The G1 state disappears because the antagonists of Cdc28–Clb2, namely Cdh1 and Sic1, are made unstable by Cdc28–Cln. Past the start transition, the system is driven to high levels of Clb2 by the positive feedback loop between Cdc28–Clb2 and Mcm1, and then to low levels of Clb2 by the subsequent activation of Cdc20. This rise and fall of Clb2-dependent kinase activity is a reflection of the stable oscillatory solutions indicated by the large black dots in the figure. During the rising phase of the oscillation, the cell sweeps through G2 into mitosis. During the decreasing phase of the oscillation (as Cdc20 and Cdh1 degrade Clb2), the cell exits from mitosis and divides (when [Clb2] drops below 0.2; see Other rules). The reduction in cell mass at division returns the control system to its original state in G1.

<a id='9fb3751f-e2db-425e-967b-1e64c46f0e67'></a>

**Checkpoints.** How does this picture change as a consequence of activating the morphogenesis checkpoint? In *cdc24ts* the checkpoint is engaged: the cell-cycle orbit (Fig. S1, middle, dotted line) is attracted by a G1 state and, as mass increases, undergoes the start transition just like wild-type cells. But after start the system is not immediately attracted by the oscillatory state, because oscillations are separated from start by a new branch of steady states, with intermediate values of [Clb2]. What is the molecular basis for this state? It is not a G1 state because SBF is high in this branch (not depicted). Rather, it is a G2-like state. *SWE1*, an SBF-controlled gene, is fully transcribed in this state and, in the absence of a bud, it is not transformed into the inactive modified form Swe1M. Hence, it phosphorylates and inactivates Cdc28–Clb2, creating a G2 steady state. When cell grows sufficiently large (Fig. S1, middle, *M* exceeds the SN3-point), enough Clb2 has accumulated in the nucleus to start the positive feedback loops with Mih1 and Mcm1 and to phosphorylate Swe1. The control system enters the mitotic state. Because nuclear division does not occur in this mutant, the cell-cycle orbit is not closed.

<a id='79f7641c-a069-43a6-9da2-2afac401ee81'></a>

Finally, _hsl1 mih1Δ_ (Fig. S1, right) shows the most dramatic picture. Because Mih1 is missing, Cdc28–Clb2 cannot engage the positive feedback loop and it is kept in the inactive phosphorylated form by Swe1. Moreover, Swe1 cannot be converted into the inactive form Swe1M. The G2–M transition cannot occur until _M_ reaches a very large (nonphysiological) value (_M_ = 29). Biologically, the cell grows in size until it dies (see Other rules). This is the bifurcation diagram of a cell blocked irreversibly in G2.

<a id='1d8f25f9-6bdb-4b94-baae-49854de3918c'></a>

References
Amon, A., M. Tyers, B. Futcher, and K. Nasmyth. 1993. Mechanisms that help the yeast cell cycle clock tick: G2 cyclins transcriptionally activate G2 cyclins and repress G1 cyclins. Cell. 74:993-1007.
Barral, Y., M. Parra, S. Bidlingmaier, and M. Snyder. 1999. Nim1-related kinases coordinate cell cycle progression with the organization of the peripheral cytoskeleton in yeast. Genes Dev. 13:176-187.
Booher, R.N., R.J. Deshaies, and M.W. Kirschner. 1993. Properties of Saccharomyces cerevisiae wee1 and its differential regulation of p34cdc28 in response to G1 and G2 cyclins. EMBO J. 12:3417-3426.
Irniger, S., S. Piatti, C. Michaelis, and K. Nasmyth. 1995. Genes involved in sister chromatid separation are needed for B-type cyclin proteolysis in budding yeast. Cell. 81:269-277.
Lew, D.J. 2000. Cell-cycle checkpoints that ensure coordination between nuclear and cytoplasmic events in Saccharomyces cerevisiae. Curr. Opin. Genet. Dev. 10:47-53.
Longtine, M.S., C.L. Theesfeld, J.N. McMillan, E. Weaver, J.R. Pringle, and D.J. Lew. 2000. Septin-dependent assembly of a cell cycle-regulatory module in Saccharomyces cerevisiae. Mol. Cell. Biol. 20:4049-4061.
Ma, X.J., Q. Lu, and M. Grunstein. 1996. A search for proteins that interact genetically with histone H3 and H4 amino termini uncovers novel regulators of the Swe1 kinase in Saccharomyces cerevisiae. Genes Dev. 10:1327-1340.
McMillan, J.N., M.S. Longtine, R.A.L. Sia, C.L. Theesfeld, E.S.G. Bardes, J.R. Pringle, and D.J. Lew. 1999. The morphogenesis checkpoint in Saccharomyces cerevisiae: cell cycle control of Swe1p degradation by hsl1p and hsl7p. Mol. Cell. Biol. 19:6929-6939.
Russell, P., S. Moreno, and S.I. Reed. 1989. Conservation of mitotic controls in fission and budding yeast. Cell. 57:295-303.
Shulewitz, M.J., C. Inouye, and J. Thorner. 1999. Hsl7 localizes to a septin ring and serves as an adapter in a regulatory pathway that relieves tyrosine phosphorylation of Cdc28 protein kinase in Saccharomyces cerevisiae. Mol. Cell. Biol. 19:7123-7137.
Sia, R.A.L., H.A. Herald, and D.J. Lew. 1996. Cdc28 tyrosine phosphorylation and the morphogenesis checkpoint in budding yeast. Mol. Biol. Cell. 7:1657-1666.
Sia, R.A.L., E.S.G. Bardes, and D.J. Lew. 1998. Control of Swe1p degradation by the morphogenesis checkpoint. EMBO J. 17:6678-6688.
Tanaka, S., and H. Nojima. 1996. Nik1: a nim1-like protein kinase of S. cerevisiae interacts with the Cdc28 complex and regulates cell cycle progression. Genes Cells. 1:905-921.
Tyson, J.J., K. Chen, and B. Novak. 2001. Network dynamics and cell physiology. Nat. Rev. Mol. Cell Biol. 2:908-916.
Tyson, J.J., A. Csikasz-Nagy, and B. Novak. 2002. The dynamics of cell cycle regulation. Bioessays. 24:1095-1109.

<!-- PAGE BREAK -->

<a id='579a0826-9976-4ff1-ae8d-348f5564f640'></a>

Table S1. Differential equations for the morphogenesis checkpoint.

1.  d[Clb2]/dt = k_s,clb (ε+[Mcm*]) M / (1+(M/J_m)) - (k_d,clb+k'_d,clb [Cdh1*]+k''_d,clb [Cdc20*]) [Clb2] - k_swe [Clb2] + k_mih [PClb2] - k_ass [Sic1] [Clb2] + k_diss [Trim] + (k_d,sic+k'_d,sic [Cln]+k''_d,sic [Clb2]) [Trim]
2.  d[PClb2]/dt = - (k_d,clb+k'_d,clb [Cdh1*]+k''_d,clb [Cdc20*]) [PClb2] + k_swe [Clb2] - k_mih [PClb2] - k_ass [Sic1] [PClb2] + k_diss [PTrim] + (k_d,sic+k'_d,sic [Cln]+k''_d,sic [Clb2]) [PTrim]
3.  d[Trim]/dt = - k_diss [Trim] + k_ass [Sic1] [Clb2] - (k_d,sic+k'_d,sic [Cln]+k''_d,sic [Clb2]) [Trim] - (k'_d,clb+k''_d,clb [Cdh1*]+k'''_d,clb [Cdc20*]) [Trim] - k_swe [Trim] + k_mih [PTrim]
4.  d[PTrim]/dt = - k_diss [PTrim] + k_ass [Sic1] [PClb2] - (k_d,sic+k'_d,sic [Cln]+k''_d,sic [Clb2]) [PTrim] - (k'_d,clb+k''_d,clb [Cdh1*]+k'''_d,clb [Cdc20*]) [PTrim] + k_swe [Trim] - k_mih [PTrim]
5.  d[Mcm*]/dt = - k_i,mcm [Mcm*] / (J_i,mcm+[Mcm*]) + k_a,mcm [Mcm][Clb2] / (J_a,mcm+[Mcm])
6.  d[Sic1]/dt = k_s,sic - (k_d,sic+k'_d,sic [Cln]+k''_d,sic [Clb2]) [Sic1] - k_ass [Sic1] ([Clb2]+[PClb2]) + k_diss ([PTrim]+[Trim]) + (k'_d,clb+k''_d,clb [Cdh1*]+k'''_d,clb [Cdc20*]) ([Trim]+[PTrim])
7.  d[Mih1*]/dt = - V_i,mih [Mih1*] / (J_i,mih+[Mih1*]) + V_a,mih [Clb2][Mih1] / (J_a,mih+[Mih1])
8.  d[IE*]/dt = - k_i,ie [IE*] / (J_i,ie+[IE*]) + k_a,ie [Clb2][IE] / (J_a,ie+[IE])
9.  d[Cdc20*]/dt = k_a,cdc20 [IE*][Cdc20] / (J_a,cdc20+[Cdc20]) - k_i,cdc20 [Cdc20*] / (J_i,cdc20+[Cdc20*]) - k_d,cdc20 [Cdc20*]
10. d[Cdc20]/dt = k_s,cdc20 + k'_s,cdc20 [Clb2]^4 / (J_s,cdc20+[Clb2]^4) - k_a,cdc20 [IE*][Cdc20] / (J_a,cdc20+[Cdc20]) + k_i,cdc20 [Cdc20*] / (J_i,cdc20+[Cdc20*]) - k_d,cdc20 [Cdc20]
11. d[Cdh1*]/dt = - (k_i,cdh [Clb2] + k'_i,cdh [Cln])[Cdh1*] / (J_i,cdh+[Cdh1*]) + (k_a,cdh + k'_a,cdh [Cdc20*])[Cdh1] / (J_a,cdh+[Cdh1])
12. d[Cln]/dt = k_s,cln [SBF*] - k_d,cln [Cln]

<!-- PAGE BREAK -->

<a id='5266b7dd-7050-4640-90e6-afc6f90c15fa'></a>

13. d[SBF*]/dt = (k'i,sbf + k''i,sbf [Clb2])[SBF*] / (Ji,sbf + [SBF*]) + (k'a,sbf M + k''a,sbf [Cln])[SBF] / (Ja,sbf + [SBF])

14. d[Swe1]/dt = ks,swe [SBF*] + ks,sweC - khsl1 [BUD] [Swe1] + khsl1r [Swe1M] - Vi,wee [Clb2][Swe1] / (Ji,wee + [Swe1]) + Va,wee [PSwe1] / (Ja,wee + [PSwe1]) - k'd,swe [Swe1]

15. d[PSwe1]/dt = - khsl1 [BUD] [PSwe1] + khsl1r [PSwe1M] - Va,wee [PSwe1] / (Ja,wee + [PSwe1]) - k'd,swe [PSwe1]

16. d[Swe1M]/dt = khsl1 [BUD] [Swe1] - khsl1r [Swe1M] - Vi,wee [Clb2][Swe1M] / (Ji,wee + [Swe1M]) + Va,wee [PSwe1M] / (Ja,wee + [PSwe1M]) - k'd,swe [Swe1M]

17. d[PSwe1M]/dt = khsl1 [BUD] [PSwe1] - khsl1r [PSwe1M] - Va,wee [PSwe1M] / (Ja,wee + [PSwe1M]) + Vi,wee [Clb2][Swe1M] / (Ji,wee + [Swe1M]) - k''d,swe [PSwe1M]

<a id='7c34d1f2-68ea-4b2c-8516-0c9748c1299a'></a>

18. d[BE]/dt = k_s,bud [Cln] - k_d,bud [BE]
19. dM/dt = μ M
k_mih = k'_mih [Mih1*] + k''_mih [Mih1],
[IE] = [IE]_total - [IE*],
[Mih1] = [Mih1]_total - [Mih1*],
[SBF] = [SBF]_total - [SBF*],
[BUD] = 0, if cell is unbudded; = 1, if cell is budded.
k_swe = k'_swe [Swe1] + k''_swe [Swe1M] + k'''_swe [PSwe1],
[Cdh1] = [Cdh1]_total - [Cdh1*],
[Mcm] = [Mcm]_total - [Mcm*],
[Swe1]_total = [Swe1] + [PSwe1] + [Swe1M] + [PSwe1M],

<a id='2d33a470-d72f-4373-8d36-1ccd10e59d8a'></a>

Bud is formed when [BE] increases above 0.6; budded cell divides when [Clb2] drops below 0.2.
* indicates the more active form of a protein.

<a id='69c987e4-6a12-44c5-ab76-2e424bdac952'></a>

We use a shorthand notation for the molecular species in Figs. 1 and 2: "Clb2" for Cdc28/Clb2, "PClb2" for PCdc28/Clb2, "Trim" for Cdc28/Clb2/Sic1, "PTrim" for PCdc28/Clb2/Sic1, and "Cln" for Cdc28/Cln.

<!-- PAGE BREAK -->

<a id='241100a2-f2f5-4ce8-9677-fd5830b35b68'></a>

Table S2. Initial conditions and parameter values for the differential equations in Table S1.

<a id='ea60c269-2915-42de-ac4e-87e7cbc1fd52'></a>

<table id="5-1">
<tr><td id="5-2">Rate constants (min⁻¹)</td><td id="5-3"></td><td id="5-4"></td><td id="5-5"></td></tr>
<tr><td id="5-6">kₛ,clb = 0.015,</td><td id="5-7">k&#x27; d,clb = 0.015,</td><td id="5-8">k&#x27;&#x27; d,clb = 1,</td><td id="5-9">k&#x27;&#x27;&#x27; d,clb = 0.1</td></tr>
<tr><td id="5-a">k&#x27; swe = 2,</td><td id="5-b">k&#x27;&#x27; swe = .01,</td><td id="5-c">k&#x27;&#x27;&#x27; swe = .2,</td><td id="5-d">k&#x27; mih = 5,</td></tr>
<tr><td id="5-e">k&#x27;&#x27; mih = 0.5,</td><td id="5-f">kass = 300,</td><td id="5-g">kdiss = 0.1,</td><td id="5-h">kₛ,sic = 0.1,</td></tr>
<tr><td id="5-i">k d,sic = 0.01,</td><td id="5-j">k&#x27; d,sic = 1,</td><td id="5-k">k&#x27;&#x27; d,sic = 3,</td><td id="5-l">ka,mcm=1,</td></tr>
<tr><td id="5-m">ki.mcm=.15</td><td id="5-n">Vi.mih = 0.3,</td><td id="5-o">Va.mih = 1,</td><td id="5-p">ka.ie=0.1,</td></tr>
<tr><td id="5-q">ki.ie=0.04,</td><td id="5-r">ka.cdc20 = 1,</td><td id="5-s">ki.cdc20 = 0.25,</td><td id="5-t">kd.cdc20=0.1</td></tr>
<tr><td id="5-u">ks,.cdc20=0.005,</td><td id="5-v">ks.cdc20 = 0.3,</td><td id="5-w">ki.cdh =35,</td><td id="5-x">ki.cdh =2,</td></tr>
<tr><td id="5-y">ka.cdh=1,</td><td id="5-z">ka,cdh =10,</td><td id="5-A">kd,cln = 0.1,</td><td id="5-B">ks.cln = 0.1</td></tr>
<tr><td id="5-C">Ka.sbf=1,</td><td id="5-D">ka.sbf = 0,</td><td id="5-E">ki.sbf = 1,</td><td id="5-F">ki.sbf = 2,</td></tr>
<tr><td id="5-G">kS,swe = 0.0025,</td><td id="5-H">ks,sweC = 0,</td><td id="5-I">khsl1 = 1,</td><td id="5-J">khsllr = 0.01</td></tr>
<tr><td id="5-K">Va,wee=0.3,</td><td id="5-L">Vi,wee=1,</td><td id="5-M">kd,swe = 0.007,</td><td id="5-N">kd,swe = 0.05,</td></tr>
<tr><td id="5-O">kd,bud = 0.1,</td><td id="5-P">ks,bud = 0.1,</td><td id="5-Q">μ = 0.005</td><td id="5-R"></td></tr>
</table>

<a id='13839676-9073-453e-816e-2819a575d746'></a>

## Other constants (dimensionless)

Ja,mcm = 0.1, Ji,mcm = 0.1, Ja,mih = 0.1, Ji,mih = 0.1,
Jm = 10, Js,cdc20 = 0.3, Ja,ie = 0.01, Ji,ie = 0.01,
Ja,cdc20 = 0.001, Ji,cdc20 = 0.001, Ja,sbf = 0.01, Ji,sbf = 0.01,
Ja,cdh = 0.01, Ji,cdh = 0.01, Ja,wee = 0.05, Ji,wee = 0.05

[Cdh1] total = [Mcm] total = [SBF] total = [Mih1] total = [IE] total = 1,
ε = 0.5

<a id='a33d7001-e85c-4362-831f-d24b603f748a'></a>

Initial concentrations (arbitrary units)

[Clb2] = 0.184,
[Mcm*] = 0.933,
[Cdc20*] = 1.438,
[SBF*] = 0.124,
[PSwe1M] = 0.013,

[PClb2] = 0,
[Sic1] = 0.003,
[Cdc20] = 1.172,
[Swe1] = 0,
[BE] = 0,

[Trim] = 0.084,
[Mih1*] = 0.808,
[Cdh1*] = 0.993,
[PSwe1] = 0,
M = 0.802

[PTrim] = 0,
[IE*] = 0.522,
[Cln] = 0.054,
[Swe1M] = 0.018,