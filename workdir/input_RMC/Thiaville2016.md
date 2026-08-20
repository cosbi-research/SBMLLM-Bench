<a id='34ce1f3e-e9d8-47f1-a5af-e22f89fa53e5'></a>

<::logo: Frontiers
frontiers
in Microbiology
A multicolored, abstract cubic shape accompanies the text, resembling stacked blocks.::>

<a id='a58771fa-1d75-4720-bafd-82c0518b9599'></a>

ORIGINAL RESEARCH published: 31 March 2016 doi: 10.3389/fmicb.2016.00431

<a id='c153fc5b-ca50-44b0-af0a-275e333ea3d5'></a>

<::logo: CrossMark
CrossMark
The logo features a black circular outline enclosing a black bookmark-like symbol, with the word "CrossMark" positioned directly beneath the circle::>

<a id='5a1af92a-9a3d-4988-a1f1-8f3ac7278551'></a>

OPEN ACCESS

Edited by:
Biswarup Mukhopadhyay,
Virginia Polytechnic Institute and State
University, USA

<a id='72cde9f7-e55d-439b-9f27-640641f79f75'></a>

**Reviewed by:**
_Haruyuki Atomi,_
_Kyoto University, Japan_
_Jean-Charles Portais,_
_University of Toulouse, France_
_Jacalyn M. Green,_
_Midwestern University, USA_

<a id='25dbb6e3-0941-410d-b627-a521ea3d008a'></a>

*Correspondence:
Andrew D. Hanson
adha@ufl.edu;
Valérie de Crécy-Lagard
vcrecy@ufl.edu*

<a id='2e799e4a-5e0f-4a5c-bb7e-54ffb317613e'></a>

**Specialty section:**
*This article was submitted to*
*Microbial Physiology and Metabolism,*
*a section of the journal*
*Frontiers in Microbiology*

<a id='e88d67ed-1e8e-4514-a534-295b61d4b82e'></a>

**Received**: *14 November 2015*
**Accepted**: *17 March 2016*
**Published**: *31 March 2016*

<a id='045e3efe-d953-4db4-8085-1ba16c83e3ad'></a>

**Citation:**
Thiaville JJ, Frelin O, García-Salinas C,
Harrison K, Hasnain G,
Horenstein NA, Díaz de la Garza RI,
Henry CS, Hanson AD and de
Crécy-Lagard V (2016) *Experimental
and Metabolic Modeling Evidence for
a Folate-Cleaving Side-Activity of
Ketopantoate
Hydroxymethyltransferase (PanB).*
*Front. Microbiol.* 7:431.
doi: 10.3389/fmicb.2016.00431

<a id='420032ba-a0e1-45c2-a15e-8bb251347ac6'></a>

Experimental and Metabolic
Modeling Evidence for a
Folate-Cleaving Side-Activity of
Ketopantoate
Hydroxymethyltransferase (PanB)

<a id='347404cc-1222-4feb-8e67-78466d86d2fd'></a>

Jennifer J. Thiaville  9, Oc1ane Frelin2, Carolina Garc1a-Salinas3, Katherine Harrison1,
Ghulam Hasnain2, Nicole A. Horenstein4, Rocio I. D1az de la Garza3,
Christopher S. Henry5, 6, Andrew D. Hanson2* and Val1rie de Cr1cy-Lagard1,7*

<a id='214e81f8-f1e3-43fd-93d2-6a9e2f3c9722'></a>

1 Department of Microbiology and Cell Science, University of Florida, Gainesville, FL, USA, 2 Horticultural Sciences Department, University of Florida, Gainesville, FL, USA, 3 Tecnológico de Monterrey, Campus Monterrey, Monterrey, Mexico, 4 Department of Chemistry, University of Florida, Gainesville, FL, USA, 5 Mathematics and Computer Science Division, Argonne National Laboratory, Argonne, IL, USA, 6 Computation Institute, The University of Chicago, Chicago, IL, USA, 7 Genetics Institute, University of Florida, Gainesville, FL, USA

<a id='2a4f466c-81fd-46ee-b997-afdb3408b0ec'></a>

Tetrahydrofolate (THF) and its one-carbon derivatives, collectively termed folates, are essential cofactors, but are inherently unstable. While it is clear that chemical oxidation can cleave folates or damage their pterin precursors, very little is known about enzymatic damage to these molecules or about whether the folate biosynthesis pathway responds adaptively to damage to its end-products. The presence of a duplication of the gene encoding the folate biosynthesis enzyme 6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase (FolK) in many sequenced bacterial genomes combined with a strong chromosomal clustering of the *folK* gene with *panB*, encoding the 5,10-methylene-THF-dependent enzyme ketopantoate hydroxymethyltransferase, led us to infer that PanB has a side activity that cleaves 5,10-methylene-THF, yielding a pterin product that is recycled by FolK. Genetic and metabolic analyses of *Escherichia coli* strains showed that overexpression of PanB leads to accumulation of the likely folate cleavage product 6-hydroxymethylpterin and other pterins in cells and medium, and-unexpectedly-to a 46% increase in total folate content. *In silico* modeling of the folate biosynthesis pathway showed that these observations are consistent with the *in vivo* cleavage of 5,10-methylene-THF by a side-activity of PanB, with FolK-mediated recycling of the pterin cleavage product, and with regulation of folate biosynthesis by folates or their damage products.

<a id='0b8e8ccd-aaf7-4201-820c-e7b09fced81d'></a>

Keywords: metabolite repair, side-reaction, _Acinetobacter baylyi_, paralogs, folate biosynthesis

<a id='d7d7ee7a-00ca-4ff3-8abd-2eb8616eebf9'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='1e0866f9-0bae-461c-a6cf-e3c11609c593'></a>

1

<a id='77a942e6-5a8e-4b3c-bd0e-3c3f724f0edc'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='40fb4898-06dd-4e44-8ae8-cd87bcff2791'></a>

Thiaville et al.

<a id='4ce4251a-ec23-49db-8b6c-e63b206c6085'></a>

Folate Cleavage by PanB

<a id='c39d6a25-5a2c-4979-9717-f10004c2808c'></a>

# INTRODUCTION

As carriers for one-carbon (C₁) units in numerous enzymatic reactions, tetrahydrofolate (THF), and its C1-substituted derivatives (collectively referred to as folates) are essential in all kingdoms of life. Mammals require a source of THF in the diet but plants and most microbes make THF de novo. Although many variations in the THF biosynthesis pathway have recently been discovered (de Crécy-Lagard, 2014), most organisms synthesize THF via the classical pathway summarized in Figure 1 (Cossins and Chen, 1997; Green and Matthews, 2007; Hanson and Gregory, 2011).

<a id='130ba77d-bd09-4359-baa6-409b8c2b58d7'></a>

The structure of folates, with a reduced pterin moiety linked to p-aminobenzoate (pABA) by the C9–N10 bond, makes them inherently unstable. Folates are sensitive at physiological pH to oxidative or photooxidative scission to release the pterin and p-aminobenzoylglutamate (pABA-Glu) moieties (Gregory, 1989; Suh et al., 2001; Hanson and Gregory, 2011). The tetrahydropterin ring can also be oxidized to form dihydrofolate (DHF), which can undergo further oxidation to produce scission products. This chemical damage occurs _in vitro_ and _in vivo_. Other common sources of damage occur at the level of the pterin

<a id='e2d8a579-0500-42c5-8f42-54916317865b'></a>

<::transcription of the content: flowchart::>GTP is converted to 7,8-Dihydroneopterin (H2-neopterin) by the enzyme FolB. 7,8-Dihydroneopterin, which has a dihydropterin ring with a dihydroxypropyl side chain, is then converted by the enzyme FolK to a molecule named H2-HMPt, which has a dihydropterin ring with a hydroxymethyl side chain. H2-HMPt is further converted to 2-Amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate (H2-HMPt-PP), which has the same dihydropterin ring but with a diphosphate group attached to the hydroxymethyl. There is a recycling pathway indicated by a dotted arrow from H2-HMPt-PP back to H2-HMPt, labeled "recycling".

Following the main pathway, H2-HMPt-PP reacts with p-ABA (para-aminobenzoate) to form H2-Pteroate, a reaction catalyzed by the enzyme FolP. This step is inhibited by sulfathiazole. H2-Pteroate then reacts with Glutamate to form DHF (Dihydrofolate). DHF is converted to THF (Tetrahydrofolate) by the enzyme FolA. This step is inhibited by trimethoprim.

THF is in equilibrium with CH2-THF (5,10-methylenetetrahydrofolate) through the enzyme GlyA. The structure of CH2-THF is shown, consisting of a tetrahydrofolate core with a methylene bridge. From CH2-THF, a hypothetical folate-cleaving side-reaction is proposed. This involves the cleavage of bonds, indicated by an arrow pointing to the bonds, as part of a "damage hypothesis". This cleavage leads to the formation of H4-HMPt and p-ABA + glutamate, mediated by the enzyme PanB.

FIGURE 1 | The classical THF synthesis pathway and a hypothetical folate-cleaving side-reaction mediated by PanB.<::>

<a id='a28291cc-5299-4cd1-af30-a35c5f565ca1'></a>

precursors of THF, 7,8-dihydroneopterin (H2-Neopterin), or 6-
hydroxymethyldihydropterin (H2-HMPterin), whose side chains
are oxidatively labile _in vitro_ (Davis et al., 1988; Dántola et al.,
2008). This cleavage also occurs _in vivo_ as cleavage products such
as xanthopterin or 2-amino-4-hydroxypteridine (pterin) have
been detected in various bacteria and are sometimes secreted in
large amounts (Goto et al., 1965; Forrest and Van Baalen, 1970).

<a id='2f6eae12-40a1-4625-a7e8-fd4d5d116d8c'></a>

While chemical damage is well-established, the nature and extent of enzymatic damage to THF and other folates are less clear. Bacteria, plants, and mammals have enzymes that can cleave the amide bond in folates, forming glutamate and pteroate moieties, but these hydrolases have wide specificities and evidence that they act on folates _in vivo_ is lacking (McCullough et al., 1971; Oe et al., 1983; Bozzo et al., 2008).
It is known that mammalian ferritin enhances folate cleavage _in vitro_ and _in vivo_ (Suh et al., 2000), and an enzyme that cleaves the folate C9–N10 bond has been found in the slime mold _Dictyostelium_ (De Wit et al., 1983). Furthermore, the high rates of folate breakdown reported in plants may not be accounted for by chemical instability alone (Orsomando et al., 2006; Hanson and Gregory, 2011). It is conceivable that 6-pyruvoyl-tetrahydropterin synthase-type enzymes, which seem to have wide substrate specificities (Phillips et al., 2012; Seo et al., 2014), can cleave folates. However, another—and unconventional—possibility has not been explored: that enzymes that use folates as C₁-donors or in other types of chemistry (Waller et al., 2010) mediate folate-cleaving side-reactions.

<a id='3480228b-86ae-4b20-9b8b-fd461a07a70c'></a>

Although the drain on folate pools from oxidative damage is known to be countered by recycling strategies for the pABA and pterin moieties, these have not been fully elucidated (Quinlivan et al., 2000; Carter et al., 2007; Noiriel et al., 2007a,b; Bozzo et al., 2008; Hanson and Gregory, 2011). Nor is it known how folate biosynthesis responds to folate depletion, although it has been shown that treatment with antifolates causes rapid accumulation of the alarmone ZTP or its precursor ZMP (Bochner and Ames, 1982; Kim et al., 2015).

<a id='327e5eda-0363-41a2-b2f9-30684783a357'></a>

We present here comparative genomic, genetic, and metabolic modeling evidence that (i) the pantothenate (vitamin B5) biosynthesis enzyme ketopantoate hydroxymethyltransferase (PanB) cleaves 5,10-methylenetetrahydrofolate (CH2-THF) as a side-reaction, (ii) that cells repair this damage via the folate biosynthesis enzyme 6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase (FolK), and (iii) that folate biosynthesis is upregulated in response to PanB-inflicted damage.

<a id='1fc0e52c-bea7-48f3-b281-6b7f36b06a77'></a>

# MATERIALS AND METHODS

## Bioinformatic Analyses

The BLAST tools (Altschul et al., 1997) and resources at NCBI (http://www.ncbi.nlm.nih.gov/) were routinely used. Sequences were aligned using Clustal Omega (Li et al., 2015) or Multalin (Corpet, 1988). Sequence logos were generated using WebLogo3 (http://weblogo.threeplusone.com/) (Crooks et al., 2004) or with the logo comparison tool at http://www.twosamplelogo.org/ (Vacic et al., 2006). Phylogenetic distribution was analyzed in the SEED database (Overbeek et al., 2005). Results are available in the "Folate_biosynthesis" subsystem on the SEED

<a id='64fa0269-f3cb-4bd6-87a5-a777fc1ef933'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='94ea7e49-5d6c-4ba4-a1cf-2072f797bd66'></a>

2

<a id='37b465a7-707f-4b5f-9cea-ee1152d03039'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='6233af9d-0fde-4b04-945a-9f1a406fafa9'></a>

Thiaville et al.

<a id='ae28e8ae-3c3f-411a-9af9-101209b9373c'></a>

Folate Cleavage by PanB

<a id='b7cebf55-2453-42ed-8c96-8b14d1b855ae'></a>

server
(http://pubseed.theseed.org/SubsysEditor.cgi?page=
ShowSubsystem&subsystem=Folate_Biosynthesis). Physical
clustering was analyzed with the SEED subsystem coloring tool
or the SeedViewer Compare Regions tool (Overbeek et al., 2014).
A subset of FolK sequences from ~1000 representative genomes
was extracted from SEED via a perl API query (Disz et al.,
2010). An alignment was done using Muscle (http://www.drive5.
com/muscle/) (Edgar, 2004) on the command line with default
settings. The trees were made with MEGA6 (Tamura et al., 2013)
using Maximum Likelihood, Neighbor Joining, and UPGMA
methods. The trees were visualized with the ETE2 python
package (Huerta-Cepas et al., 2010). The physical clustering
information was added to the tree after writing a python code
that extracted if folK was within 10 coding sequences of the
folB gene, the panB gene or both in a given genome. PDB
(www.rcsb.org) (Berman et al., 2000) was used to visualize
structures and ligand binding sites.

<a id='a282503a-13a4-4a02-a13a-c7d85549cba0'></a>

# Strains and Media
Bacteria were grown at 37C on Luria Bertani (LB) medium (BD Diagnostics Systems) or on M9 minimal medium (Sambrook et al., 1989) supplemented with 0.4% glucose (w/v). Growth media were solidified with 15 g/l agar (BD Diagnostics Systems) for the preparation of plates. Transformations were performed following standard procedures (Sambrook et al., 1989). Chloramphenicol (Cm, 30g/ml), kanamycin (Kan, 50 g/ml), ampicillin (Amp, 100 g/ml), thymidine (dT, 80 g/ml), and pantothenate (1 M) were used as appropriate. E. coli strains used in this study included MG1655 (Coli Genetic Stock Center), BW25113 (Baba et al., 2006), and C600folK::tet (Jonsson and Swedberg, 2005). The BW25113 panB::kan mutant was obtained from the Keio collection (Baba et al., 2006) and confirmed to be auxotrophic for pantothenate. E. coli GC10 (GeneChoice) was routinely used for cloning.

<a id='fc3df62b-17ec-4550-8e01-a2fda8779c4f'></a>

# Antifolate Sensitivity
E. coli strains MG1655 and BW25113 were each transformed with pCA24N::panB and pBAD33. The panB overexpression plasmid (pCA24N::panB) was obtained from the ASKA collection of E. coli clones (Kitagawa et al., 2005) and was confirmed to complement the pantothenate auxotrophy of the BW25113 ΔpanB::kan strain. pBAD33 encoding chloramphenicol resistance was used as an empty vector control (Guzman et al., 1995). Transformants were selected on LB with Cm. Three colony-purified isolates from each transformation were selected for further analysis. The isolates were tested for sensitivity to folate inhibitors by the Kirby-Bauer Method (Bauer et al., 1966). Cultures were grown in 5 ml M9-glucose medium with chloramphenicol overnight at 37°C with shaking. The following day, the strains were diluted 1:500 in fresh M9-glucose medium and 5 ml of each culture was poured onto M9-glucose agar with added chloramphenicol and IPTG (0.1 mM). The liquid was evenly distributed across the plate and the unabsorbed liquid was removed by pipette. Filter disks were placed on top of the agar, and 20 µl of either 50 or 100 µg/ml of trimethoprim, or 50 or 100 µg/ml of sulfathiazole antibiotics were spotted onto

<a id='bc3b00c1-6e9c-45eb-8bb5-1688abbdb86f'></a>

each disk. The plates were incubated for 18 h at 37&#176;C and the
diameters of the resulting zones of inhibition were measured.

<a id='18399344-5d21-42f3-8a21-2a624a0917b7'></a>

Sensitivity to antifolates was also measured by dilution drops onto various concentrations of antibiotic. Cultures were grown in 5 ml M9-glucose medium with chloramphenicol overnight at 37°C with shaking. The following day, the strains were diluted 1:20 in fresh M9-glucose medium and grown at 37°C with shaking until the cultures reached approximately A600 1.0. The cultures were normalized to an A600 1.0 and serially diluted in 10-fold increments. Ten microliter of each dilution was spotted onto M9-glucose agar plates with added chloramphenicol and IPTG (0.1 mM) with sulfathiazole (0–1 µg/ml) or trimethoprim (0–1.5 µg/ml). Plates were incubated at 37°C overnight. To test the effect of ΔpanB on sensitivity to folate inhibitors, the same assay was performed with wild-type BW25113 and BW25113 ΔpanB::kan with the exception that chloramphenicol was not added to the media and all minimal media contained 1 µM pantothenate.

<a id='217f77a2-e11d-47cc-ba67-f151b4719e3a'></a>

# Folate Gene Expression Analysis
Expression levels of _folB_, _folE_, _folK_, and _panB_ were analyzed in MG1655 harboring either empty vector pBAD33 or the _panB_ overexpression plasmid pCA24N::_panB_. Three biological replicates of each were grown overnight in M9-glucose medium with chloramphenicol at 37°C with shaking. The following day the cultures were diluted 1:100 in fresh M9-glucose medium with chloramphenicol and grown at 37°C with shaking. IPTG was added to 0.2 mM when the culture was at A600 0.2 and the induced cultures were harvested at A600 1.0. RNA was extracted from each culture with the QIAGEN RNeasy Protect Bacteria Mini Kit, the concentration was determined by NanoDrop spectrophotometer, and RNA was stored at -80°C. cDNA was synthesized from 300 ng RNA using the iScript Select cDNA synthesis kit (Bio-Rad) using the provided random primer mix. Quantitative PCR was performed using the MyiQ2 Real Time PCR Detection System (Bio-Rad) using iTaq Universal SYBR Green Supermix (Bio-Rad). Amplification parameters were 95°C for 3 min followed by 40 cycles of 95°C for 10 s, 59°C for 30 s with fluorescence measurement, followed by the establishment of a melting curve. Data were analyzed with the IQ5 software (Bio-Rad) and the Bio-Rad Expression Macro. Expression was normalized against two reference genes: _rssA_ (b1234) and _rpoA_ (b3295). All primers used for the RT-PCR are listed in Table S1.

<a id='9f2a1789-f1c2-49a6-9dd1-066dc75f8ba2'></a>

**Cloning of *folK1* and *folK2* and Complementation of Δ*folK***
ACIAD3062 (*folK1*) and ACIAD2407 (*folK2*) were PCR-amplified with primers ACIAD3062-xbaI-5 (5'-CTACTCTAG AATGAGCATAACCACСТАТATCG-3') and ACIAD3062-SalI-3 (5'-CATTGTCGACCGCGTTATTTTTCAACCCAG-3') and ACIAD2407-xbaI-5 (5'-CATTTCTAGATTGAACGCCAA CGCCACAATTTTTG-3') and ACIAD2407-SalI-3 (5'-CAATGTCGACGAATTATGATGAAGAAATCAC-3'), respectively. *Acinetobacter baylyi* ADP1 genomic DNA was used as the template for PCR. PCR products were digested with *XbaI* and *SalI*, purified with the Zymo Clean and Concentrator-5 kit, and ligated into *XbaI*/*SalI*-digested pBAD24. The ligation

<a id='730cdae8-14db-4106-8818-8db1d90d4a9f'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='efa02d42-10f3-4081-8f68-a78aaceb4afd'></a>

3

<a id='61f71506-9dfa-4fb6-b4a2-cfa8adfa14e5'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='89626ed4-2e41-40c5-a2a6-06553b1d6aa4'></a>

Thiaville et al.

<a id='7917acc1-289b-4f66-83c8-df5a46c9bd3a'></a>

Folate Cleavage by PanB

<a id='583fad30-7c60-417b-a22e-df94dd4e7b20'></a>

mixtures were used to transform _E. coli_ GC10 and transformants were selected on LB with ampicillin. pBAD24::_folK1_ and pBAD24::_folK2_ were confirmed by sequencing and the plasmids were renamed pJJT115 and pJJT107, respectively.

<a id='9967087c-8124-4ccd-a40c-2e83db7caa48'></a>

**Complementation of *E. coli* Δ*folK***
pJJT115, pJJT107, or pBAD24 were transformed via electroporation into *E. coli* C600 Δ*folK*::tet. The cells were recovered in 1 ml of LB plus dT for 1 h at 37°C. After recovery, the cells were washed once with 1 ml LB without dT to remove dT, and suspended in 1 ml LB. One hundred microliter of the transformation reaction was spread onto LB with ampicillin containing either 0.2% arabinose (w/v) or dT. If the *folK* gene on the plasmid complements the Δ*folK*, the colonies appear after overnight growth at 37°C on LB with ampicillin and arabinose without dT.

<a id='ff9b3d9f-adbe-4f21-b82a-8ce4ac672d38'></a>

## Pterin and Folate Analyses
For pterin and folate analysis experiments, a *panB* expression plasmid was constructed as follows. The *panB* gene was amplified from genomic DNA of strain W3110 by PCR using primers EcPanBp19Fwd (5'-CTAGAAGCTTATGACAGGAAACAG CTATGAAACCGACCACCATCTC-3') and EcPanBp19Rev (5'-GATCGAATTCTTAATGGAAAC-TGTGTTCTTCG-3'), and cloned into the *Hind*III and *Eco*RI sites of pUC19 (Yanisch-Perron et al., 1985) to give pUC19::*panB*, which was verified by sequencing. To validate the functionality of the expressed gene of the pUC19::*panB* plasmid, the BW25113 Δ*panB*::kan mutant, which is auxotrophic for pantothenate, was transformed with pUC19::*panB* plasmid. Transformants were able to grow on minimal medium in absence of pantothenate, restoring the growth of the mutant. For pterin analysis of the Δ*panB*::kan mutant, three independent colonies of each strain (BW25113 wild type and Δ*panB*::kan mutant) were grown on M9 glucose (0.4%) and 10 μM pantothenate. Cells were harvested when A600 reached 1.0. For *panB* overexpression analyses, the strains (wild type MG1655 harboring the vector pUC19 or containing *panB*) were grown on M9 glucose (0.4%) with added Amp. IPTG (0.5 mM) was added at A600 of 0.3. Three independent colonies for each were cultivated. Only the cultures overexpressing *panB* had filaments (cell lysis) after adding IPTG (repeated twice independently). Cells were harvested when A600 reached 1.0. Protein contents of harvested bacterial cells were determined using the Pierce bicinchoninic acid (BCA) assay kit. Pterins were extracted, converted to their oxidized forms, and analyzed by HPLC with fluorometric detection as described (Pribat et al., 2010). Folates were extracted and analyzed by HPLC with electrochemical detection as described (Pribat et al., 2010; Srivastava et al., 2011).

<a id='aba42985-4626-4601-8bb8-9227f60e6591'></a>

**Modeling**
A kinetic model of the THF biosynthesis pathway was constructed manually in the Copasi Biochemical System Simulator software (Hoops et al., 2006). Reaction stoichiometry was obtained from KEGG (Kanehisa and Goto, 2000) and kinetic parameters were obtained from BRENDA (Chang et al., 2015).

<a id='fd4db22b-24c3-42be-baa4-444186370aa5'></a>

Thermodynamic parameters were computed for all reactions using the group contribution method (Jankowski et al., 2008). Kinetic and thermodynamic parameters were used to evaluate whether each model reaction was reversible or irreversible, and saturated or unsaturated; they were not used directly as they did not replicate the experimentally observed metabolite concentrations and fluxes. The actual kinetic parameters in the model were selected to fit experimentally measured fluxes and metabolite concentrations. In addition to the last four steps of THF biosynthesis, the main CH2-THF synthesizing reaction (GlyA), and the proposed PanB side reaction, the model included exchange reactions that simulate the production of H2-HMPt and pABA by reactions outside the selected scope of the model. Similarly, exchange reactions were added to simulate the continuous dilution of THF and CH2-THF that occurs during cell growth (see Figure S4). The H2-HMPt and pABA exchange reactions produce these compounds at a fixed rate of 1.66e-7 mmol ml⁻¹ cytoplasm s⁻¹, which is equal to the total THF synthesis rate required to counter growth-associated dilution computed in wild-type cells based on measured growth rates. The exchange reactions for consumption of THF and CH2-THF were modeled as saturating irreversible enzymatic reactions, with Vmax and Km values selected to ensure that steady state concentrations for THF and CH2-THF match experimentally measured values. THF consumption fluxes cannot be fixed like the H2-HMPt and pABA production fluxes, as this results in an overly constrained model. The model did not include folate polyglutamylation because this is peripheral to the chemistry of the reactions of interest. Nor did it explicitly include hydrolysis of PABA-Glu to PABA and glutamate (Carter et al., 2007), which is also peripheral. Additionally, the reactions included in our model involved seven metabolites that are prevalent in numerous metabolic pathways: ATP, AMP, ADP, phosphate, serine, glycine, and pyrophosphate. We held the concentrations of these metabolites in our model at fixed physiological levels taken from the literature (Kukko and Heinonen, 1982; Kukko-Kalske et al., 1989; Rao et al., 1993; Amin and Peterkofsky, 1995; Bennett et al., 2009), as we expect other pathways that fall outside the scope of our model to be responsible for maintaining these metabolites at their physiological concentrations. All data and parameters relating to model compounds and reactions are available in Tables S2 and S3, respectively. We also provide the model data in Copasi format for the three variations of the model that were applied in this work: (i) wild-type (Additional File 1); (ii) PanB overexpression (Additional File 2); and (iii) PanB overexpression and THF regulation (Additional File 3). Finally, all three models were deposited in BioModels (Chelliah et al., 2015) and assigned the identifiers MODEL1602280001, MODEL1602280002, and MODEL1602280003, respectively.

<a id='2d668a25-599e-4bae-861e-74915738d708'></a>

**Model Parameter Sensitivity Analysis**
A sensitivity analysis was performed on the kinetic model to identify which parameters were most significant in governing model behavior. We altered model parameters around their currently defined values, rerunning the model after each alteration, and identifying the changes in predicted steady-state

<a id='ba2a8e1c-5449-4308-985d-0e0ec17ba72d'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='67768e76-e586-4405-a90b-f887a19f68f5'></a>

4

<a id='2f91b6c0-e674-4d38-a8ca-63c83a0b4b41'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='da61b657-af82-44b8-9f45-330df42c5ea9'></a>

Thiaville et al.

<a id='248d725e-aaf5-4de7-8b1e-08d1ec53801a'></a>

Folate Cleavage by PanB

<a id='5d91fbd5-6dc3-4809-a88c-4fa5df7d1c09'></a>

fluxes and concentrations. Many parameters in the model had little impact on overall model behavior. These included the kinetic constants for the FolK, FolP, FolC, and FolA reactions, and nearly all of the fixed metabolite concentrations (see previous section). Increasing the kinetic constant in the mass-action kinetic equation will increase the instantaneous flux of the associated reaction, but then the substrates of the reaction are consumed faster than they are produced, causing a decline in substrate concentration, and restoring flux to its original steady-state value. In this case, the steady-state flux through the Fol[KPCA] reactions will be the flux entering the pathway via the H₂-HMPt production reaction, which we call vnet, plus the flux recycled by the proposed PanB reaction, which we call vPanB. Similarly, increasing an intermediate concentration will temporarily boost the flux of the reaction consuming the metabolite, but then flux will relax to the same steady state value as the metabolite is consumed faster than it is produced.

<a id='c9071e16-509e-4b6d-836d-8b3ca543b7f3'></a>

The model was also insensitive to the saturation state of the Folk, FolP, FolC, FolA, and PanB reactions. All of these reactions were modeled as completely unsaturated reactions, essentially following mass action kinetics. We chose mass action kinetics for these reactions, as opposed to unsaturated Monod kinetics, because this reduces the number of parameters, simplifies the model, and produces equivalent behavior when the enzyme is in a completely unsaturated state. However, we did determine that modeling these reactions as saturated enzymatic reactions results in similar behavior and steady states so long as the v_max values exceed the net steady-state flux that these reactions must achieve (v_net + v_PanB).

<a id='a82cde6d-5167-49c3-9fce-875f79740c14'></a>

In contrast, the kinetic parameters on the GlyA reaction exercised a large degree of control over the ratio of steady-state concentrations for THF and CH2-THF. The ratio and magnitude of these rate constants dictated how close this reaction was to equilibrium, as well as what the equilibrium ratio of THF and CH2-THF would be. The total steady-state concentration of THF and CH2-THF was controlled by the value of *Vnet* and the kinetic parameters on the drain reactions for THF and CH2-THF. The THF and CH2-THF drain reactions represent the consumption of these compounds during cell growth and dilution. Because the value of *Vnet* was fixed, the only adjustable parameters governing the total THF and CH2-THF concentration were the kinetic parameters on the drain reactions. These parameters were adjusted to ensure that the total concentration of THF and CH2-THF predicted by the model matched experimental data under all conditions studied. Given these constraints, these kinetic parameters were not flexible. Rather, only a single set of values could be found to produce the optimal fit to the experimental data.

<a id='555b832c-57c7-48e6-9466-aeffe0798788'></a>

The other key parameters in the model are the kinetic
constants on the PanB reaction, which control the steady state
concentration of H2-HMPt, as well as the magnitude of the
recycle flux back to H2-HMPt. This flux controls the dynamic
response of the folate pathway intermediates, including the initial
dip that occurs in the H2-HMPt concentration immediately
following the induction of the PanB enzyme, which we have

<a id='20bafd64-4c84-4bc6-a5e2-306b06ec0fd5'></a>

proposed as the cause of the overall induction of the folate
pathway. We tuned the kinetic parameters on the PanB reaction
in our model to fit the experimentally measured concentrations
for H2-HMPt. We currently model this reaction as unsaturated
following irreversible mass action kinetics, but behavior would
be similar if the reaction followed saturated Monod kinetics.

<a id='53191212-57de-431c-88a2-7b6851157e8a'></a>

## RESULTS
### Comparative Genomics Predicts a Functional Association between _panB_ and _folK_ Genes

Inspection of the current "Folate biosynthesis" subsystem in the SEED database (Overbeek et al., 2005) revealed that 14% of the ~11,400 genomes analyzed contain two copies of the gene encoding 6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase (_folK_). This observation had already been made when the subsystem was first constructed with far fewer genomes (de Crécy-Lagard et al., 2007), but no explanation for the role of the second copy of the _folK_ gene was proposed at that time.

<a id='44b18fc0-f638-4089-84b1-bea27733861b'></a>

Physical clustering analysis showed that in ~70% of the genomes with two copies of *folK*, each *folK* gene occurs in a particular genomic context. One copy clusters with *folB*, which encodes the preceding step in folate synthesis (**Figure 1**), and the other clusters with a pantothenate biosynthesis gene, *panB*, as seen in *Acinetobacter baylyi* ADP1 (**Figure 2A**). These clusters also reflect the gene organization in genomes that have only one *folK* gene. Thus, 25% of the organisms in SEED harbor a single *folK* gene that clusters with *folB* (e.g., *Salmonella enterica*) and 18% harbor a single *folK* gene that clusters with *panB* (e.g., *Bacillus subtilis*) (**Figure 2A**). Furthermore in certain genomes (e.g., *Desulforudis audaxviator*) a single *folK* gene clusters with both *panB* and *folB* (**Figure 2A**). To eliminate any bias introduced by overrepresentation of certain species, the analysis was repeated on a set of 981 organisms chosen for their diversity (Niehaus et al., 2015). Very similar results were obtained: 7% of the genomes contained two *folK* genes with one next to *panB* and the other next to *folB*; 20% of the genomes had a unique *folK* next to *folB*; and 11% had a unique *folK* next to *panB*. Consistent with the functional link between the *folK* and *panB* genes implied by their clustering in bacteria, the FolK and PanB enzymes localize to the same subcellular compartment (the mitochondrial matrix) in plants and yeast (Güldener et al., 2004; Ottenhof et al., 2004; Perocchi et al., 2006; Gerdes et al., 2012). To explore structural, and potential functional, differences between the products of *folK* genes clustered with *panB* or *folB* genes, we aligned ~270 FolK sequences that were chosen from a diverse set of prokaryotes that included organisms with *folK* duplications. In order to produce a higher quality alignment, proteins were kept only if their lengths were within 0.25 standard deviations of the average length of the set, or if there was another FolK encoded in the same genome. Sequence logo comparisons showed differences in enrichments for specific amino acids at given positions between the FolK proteins whose genes physically cluster with

<a id='2fc7247c-243c-4903-802c-b1baa798b892'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='31e48a5a-9ea1-4a72-8121-302c077d8965'></a>

5

<a id='52488672-087e-432f-a1d0-ad4f9522225c'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='85519e7e-c358-4fef-9b29-23aa4f9a3813'></a>

Thiaville et al.

<a id='aa377442-31d5-452d-86c2-76099be6f778'></a>

Folate Cleavage by PanB

<a id='bd31396a-790e-43f1-a73b-7f11e0a0abb1'></a>

A
B
<::Figure A: Gene cluster diagrams showing physical clustering of folK homologs with panB or folB in specific genomes.::>
panB-clustered folK
Acinetobacter baylii ADP1
<::Diagram: Gene cluster for Acinetobacter baylii ADP1 (panB-clustered folK). From left to right: a black gene, a light green gene labeled "panC", a dark green gene labeled "panB", a red gene labeled "folK1", a light blue gene labeled "pcnB", and two black genes.::>
Salmonella enterica subsp. enterica serovar Typhimurium str. LT2
<::Diagram: Gene cluster for Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 (panB-clustered folK). From left to right: a black gene, a light green gene labeled "panG", a dark green gene labeled "panC", a red gene labeled "panB", a light blue gene labeled "folK", a cyan gene labeled "pcnB", and a black gene.::>
folB-clustered folK
Acinetobacter baylii ADP1
<::Diagram: Gene cluster for Acinetobacter baylii ADP1 (folB-clustered folK). From left to right: a black gene, a light blue gene labeled "DUF2799", a red gene labeled "folK2", a dark blue gene labeled "folB", a yellow gene labeled "ABC1 domain", and an orange gene labeled "moeB".::>
Bacillus subtilis subsp. subtilis str. 168
<::Diagram: Gene cluster for Bacillus subtilis subsp. subtilis str. 168 (folB-clustered folK). From left to right: a black gene, a purple gene labeled "pabA", a dark blue gene labeled "pabB", a light blue gene labeled "pabC", a light purple gene labeled "folP", a dark blue gene labeled "folB", a red gene labeled "folK", and a black gene.::>
panB and folB-clustered folK
Desulforudis audaxviator MP104C
<::Diagram: Gene cluster for Desulforudis audaxviator MP104C (panB and folB-clustered folK). From left to right: a light purple gene labeled "folP", a dark blue gene labeled "folB", a red gene labeled "folK", an orange gene labeled "cobB", a light green gene labeled "panG", a dark green gene labeled "panB", a light blue gene labeled "panC", and a dark blue gene labeled "panD folD".::>
<::Figure B: A circular phylogenetic tree of FolK homologs. The tree branches are colored according to their clustering type: FolB-clustered FolK (red), PanB-clustered FolK (blue), and Both FolB and PanB-clustered FolK (green). The labels for the species are arranged radially around the tree.::>

FIGURE 2 | Clustering and phylogeny of folK. (A) Physical clustering of folK homologs with panB or folB in specific genomes. (B) A phylogenetic tree of
FolB-clustered FolK (red), PanB-clustered FolK (blue), and FolB and PanB-clustered FolK (green). The sequences were aligned with MUSCLE and the tree was
calculated with MEGA6 using the maximum likelihood method.

<a id='5f805e8a-901d-4fed-a2bd-47833fb0056b'></a>

panB genes and those that cluster with folB (Figure S1).
These amino acid differences between the two groups were
confirmed by phylogenetic analyses on the same set of sequences
as that for the majority of FolK proteins; the phylogenetic
clustering broadly matched the physical clustering (Figure 2B).
The separation is not perfect, however, so these signatures do not
necessarily point to a functional divergence between the two FolK
groups.

<a id='877fc100-62a9-428b-b36c-6d01d438daea'></a>

In order to test whether, from genomes with two copies of _folK_, both have 6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase activity _in vivo_, the _folK1_ and _folK2_ genes of _A. baylyi_ ADP1 were tested for the capacity to complement the dT auxotrophy a △_folK_ strain of _E. coli_. The _folK_ homolog found next to _panB_ (_folK1_, ACIAD3062) robustly complemented the dT auxotrophy, whereas the one next to _folB_ (_folK2_, ACIAD2407) did not (Figure S2A). This fits with gene essentiality data for _A. baylyi_ showing that _folK1_ is essential and that _folK2_ is not (de Berardinis et al., 2008). The _folK_ genes that cluster with _panB_ may thus be taken to be functional. We were surprised by these results as many organisms have just one _folK_ that clusters with _folB_ and must therefore be active. Analysis of the FolK multiple alignments revealed that two critical residues that interact with Mg2+, ATP, and substrates (R92, F123 in _E. coli_ FolK numbering Blaszczyk et al., 2000) are not conserved in the _A. baylyi_ FolK that clusters with _folB_ (Figure S2B). This was an exception of the _Acinetobacter_ clade because in most organisms with duplicated FolKs, all catalytic residues were conserved in both copies (data not shown).

<a id='6cb46a35-3eb4-452a-9052-9a2b12b0c8dd'></a>

## A Hypothesis Linking the _panB-folK_
Association to Folate Damage and Its
Repair
The _panB_ gene encodes the CH2-THF-dependent enzyme
ketopantoate hydroxymethyltransferase (EC 2.1.2.11). This
suggested an explanation for the observed association between
_panB_ and _folK_ based on the proposed reaction mechanism of
PanB. Powers, Snell, and coworkers first purified this enzyme
and showed that it is a class II aldolase (i.e., metal requiring)
(Powers and Snell, 1976; Teller et al., 1976). In the proposed
mechanism, PanB initiates the normal reaction sequence by
forming an adduct between α-ketoisovalerate and CH2-THF;
the adduct is then resolved by hydrolytic attack to generate
THF and the product 2-dehydropantoate. We hypothesized
a damage side-reaction in which the adduct first undergoes
hydrolytic attack to liberate the pABA-Glu moiety (Figure 1),
with concomitant formation of a hydroxymethyl group on
the pterin/α-ketoisovalerate adduct (Figure 3). This adduct
then undergoes a second hydrolytic attack, with two possible
outcomes, both involving production of 2-amino-4-hydroxy-6-
hydroxymethyl-7,8-tetrahydropteridine (H4-HMPterin). In path
A, the other reaction product is 2-dehydropantoate; in path
B, α-ketoisovalerate is regenerated along with an unstable bis-
hydroxymethylpterin, which spontaneously loses formaldehyde
to give H4-HMPterin. The H4-HMPterin formed by either path
could re-enter the folate pathway via FolK after spontaneous
oxidation to the dihydro form (Figure 1), or possibly directly. We
therefore made genetic tests of the hypothesis that PanB damages

<a id='3f9cfdda-7cc3-4957-b445-545ad76e5a96'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='6103334c-f0a0-4387-ae60-0fcccbc8820c'></a>

6

<a id='fd6c898b-7a5e-4c8e-8b47-4be59b8e46dc'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='61d08930-d6bd-42ba-bb94-24b7a48c1f2b'></a>

Thiaville et al.

<a id='68f54c87-91d5-4833-adbd-862749d7a690'></a>

Folate Cleavage by PanB

<a id='3423c0ba-d520-488b-9ab3-ab4ad639a52b'></a>

<::Chemical reaction scheme: The top reaction shows the formation of a 'damaged intermediate'. The starting molecule is a complex pterin derivative, which reacts in the presence of 'PanB'. An intermediate structure is shown where a water molecule is involved, with a base ':B' abstracting a proton and an acid 'H-A' donating a proton. This leads to the 'damaged intermediate', which is a 7,8-dihydropterin-6-ylmethyl-OH derivative with a side chain of CH2-C(CH3)2-C(=O)O-Mg+2.The bottom part of the scheme shows two repair pathways, 'path A' and 'path B', starting from the damaged intermediate (or a similar structure showing the attack of water, where 'B:' abstracts a proton from H-O-H).Path A: In the presence of 'PanB', the damaged intermediate is cleaved into two products: HOCH2-C(CH3)2-C(=O)O-Mg+2 and H4-HMPt (a 7,8-dihydropterin-6-ylmethyl-OH derivative), which is indicated to go 'to repair'.Path B: In the presence of 'PanB', the damaged intermediate undergoes a reaction involving water (B: abstracting a proton from H-O-H). This leads to an unstable intermediate shown in brackets, which then cleaves to form H2CO (formaldehyde) and 'regenerated α-ketoisovalerate' (O=C(CH3)2-C(=O)O-Mg+2). The remaining pterin derivative is H4-HMPt (7,8-dihydropterin-6-ylmethyl-OH), which is also indicated to go 'to repair'. :chemical reaction scheme::>

<a id='7f86ce6a-ee01-4dc1-ad14-a50910e2e4fc'></a>

FIGURE 3 | Proposed side activity of PanB. PanB initiates normal carbon transfer to α-ketoisovalerate to form the initial adduct which then subsequently undergoes aberrant hydrolytic attack to cleave the glutaminyl-p-ABA group from the pterin system. The resulting adduct can cleave by path A which generates 2-dehydropantoate and H₄-HMPterin. In path B, hydrolytic cleavage releases unchanged α-ketoisovalerate and produces the bis-hydroxymethyl intermediate that spontaneously decomposes to formaldehyde and H₄-HMPterin. Subsequent redox steps would convert the H₄-HMPterin to H₂-HMPterin for re-entry into the biosynthetic pathway.

<a id='f0edd0fd-6611-4079-8b38-4ef144585a0c'></a>

CH2-THF and that the resulting pterin moiety is recycled to
folate via FolK.

<a id='c85947d1-9092-402f-8998-bb1563d9aff2'></a>

**Genetic and Metabolic Evidence Favor a Role of PanB in THF Damage**
If a side-reaction of PanB cleaves CH2-THF (Figure 3), then overexpressing *panB* should make wild type *E. coli* more sensitive to antifolate drugs that deplete folate pools, such as sulfathiazole (a pABA analog) and trimethoprim (a dihydrofolate reductase inhibitor).

<a id='7ca5db67-a048-499a-8d4f-2ddac6853ac9'></a>

The effect of overexpressing the _panB_ was tested by transforming either _E. coli_ strain BW25113 or MG1655 with the ASKA clone expressing _panB_ under control of the _lac_ promoter (_ppanB_) or with an empty vector (pBAD33) control. Sensitivity to trimethoprim and sulfathiazole was assessed for each strain by measuring the halos of inhibition of different concentrations of each drug. The strains overexpressing _panB_ were more sensitive to both trimethoprim and sulfathiazole resulting in larger zones of inhibition (Figures 4A,B). _E. coli_ MG1655 showed a greater

<a id='efea9c66-c694-4082-9d15-cfde77f0886d'></a>

increase in sensitivity to sulfathiazole when overexpressing *panB*
than BW25113; conversely, BW25113 overexpressing *panB* had
a greater increase in sensitivity to trimethoprim than MG1655.
To confirm the exacerbated sensitivity, ten-fold serial dilutions
of late log-phase cultures were spotted onto M9-glucose agar
plates containing chloramphenicol, IPTG, and various levels of
trimethoprim or sulfathiazole (Figure 4C). Trimethoprim at 1
µg/ml did not affect growth of the empty-vector control cells but
reduced growth of the BW25113 *panB*-overexpressing cells by a
factor of 10⁵. Similarly, overexpressing *panB* made *E. coli* 10²-
fold more sensitive to 0.1 µg/ml sulfathiazole. As observed with
the inhibition halos, the trimethoprim sensitivity of MG1655
overexpressing *panB* was less drastic than BW25113, however,
the sulfathiazole sensitivity of both *panB*-overexpressing strains
was similar.

<a id='e1159b64-73ee-4fdf-b173-1b0d292b76e4'></a>

To assess whether deleting _panB_ affected sensitivity to antifolates, BW25113 _ΔpanB_ was acquired from the Keio collection (Baba et al., 2006). Ten-fold serial dilutions of wild-type and mutant were spotted onto M9 glucose

<a id='99d0f593-398e-4371-aa3e-ff44964ab1a2'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='8a5d9e70-4670-441e-a09e-d43e1b3ee7a2'></a>

7

<a id='e83d9c76-a79e-4a81-aa9d-82dfb25cd9a1'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='f28633cc-a084-4968-a549-ce4fd2da3607'></a>

Thiaville et al.

<a id='f52cddd3-3d40-4789-956c-b725eead78dc'></a>

Folate Cleavage by PanB

<a id='fedcacaf-d174-465e-b611-cf6163add518'></a>

A
MG1655 (empty) BW25113(empty)
<::Disk diffusion assay plates. Top left: MG1655 (empty) strain showing four wells (1, 2, 3, 4) and a central well (N), each surrounded by a clear zone of inhibition (halo). Top right: BW25113 (empty) strain showing four wells (1, 2, 3, 4) and a central well (N), each surrounded by a clear zone of inhibition (halo).
: disk diffusion assay plates::>
MG1655 (ppanB) BW25113(ppanB)
<::Disk diffusion assay plates. Bottom left: MG1655 (ppanB) strain showing four wells (1, 2, 3, 4) and a central well (N), each surrounded by a clear zone of inhibition (halo). The halos appear smaller than those for MG1655 (empty). Bottom right: BW25113 (ppanB) strain showing four wells (1, 2, 3, 4) and a central well (N), each surrounded by a clear zone of inhibition (halo). The halos appear smaller than those for BW25113 (empty).
: disk diffusion assay plates::>

B
<::Bar chart showing the average halo diameter (mm) for different strains and antibiotic concentrations.
Y-axis: Average halo diameter (mm), ranging from 0 to 35.
X-axis: Antibiotic treatments: Trimethoprim 100 µg/ml, Trimethoprim 50 µg/ml, Sulfathiazole 100 µg/ml, Sulfathiazole 50 µg/ml.
Legend:
- BW25113 (pBAD33) (dark grey)
- BW25113 (ppanB) (light grey)
- MG1655 (pBAD33) (medium grey)
- MG1655 (ppanB) (very light grey)

For Trimethoprim 100 µg/ml, BW25113 (ppanB) and MG1655 (ppanB) show significantly larger halos compared to their respective (pBAD33) controls, indicated by asterisks.
For Sulfathiazole 100 µg/ml, MG1655 (ppanB) shows a significantly larger halo compared to MG1655 (pBAD33), indicated by an asterisk.
For Sulfathiazole 50 µg/ml, MG1655 (ppanB) shows a significantly larger halo compared to MG1655 (pBAD33), indicated by an asterisk.
Error bars are shown for all data points.
: bar chart::>

C
µg/ml Trimethoprim
0 1.0
<::Agar spot plate showing bacterial growth under different conditions.
The plate is divided into two main sections for Trimethoprim (0 and 1.0 µg/ml) and Sulfathiazole (0 and 0.1 µg/ml).

Rows represent different bacterial strains:
- BW25113 (ppanB)
- BW25113 (empty)
- MG1655 (ppanB)
- MG1655 (empty)

Under each antibiotic concentration, there are columns representing bacterial dilutions from 0 to -6. Each spot shows bacterial growth, decreasing with higher dilutions. Visible differences in growth are observed between strains and antibiotic conditions, with some strains showing reduced growth at higher antibiotic concentrations.
: agar spot plate::>
µg/ml Sulfathiazole
0 0.1
<::Agar spot plate showing bacterial growth under different conditions. This section is a continuation of the previous visual content, showing results for Sulfathiazole.

Rows represent different bacterial strains:
- BW25113 (ppanB)
- BW25113 (empty)
- MG1655 (ppanB)
- MG1655 (empty)

Under each antibiotic concentration, there are columns representing bacterial dilutions from 0 to -6. Each spot shows bacterial growth, decreasing with higher dilutions. Visible differences in growth are observed between strains and antibiotic conditions, with some strains showing reduced growth at higher antibiotic concentrations.
: agar spot plate::>
Dilution: 0 -1 -2 -3 -4 -5 -6 0 -1 -2 -3 -4 -5 -6 

<a id='00f38de2-d3a6-4026-97e9-81fc680f2cfe'></a>

FIGURE 4 | Antifolate sensitivity (A) Overnight cultures of E. coli BW25113 and MG1655 carrying pCA24N::panB (ppanB) or pBAD33 (empty) were diluted 100-fold and spread onto M9-glucose agar medium containing chloramphenicol and IPTG (0.1 mM). Twenty microliter of (1) sulfathiazole at 100 µg/ml, (2) sulfathiazole at 50 µg/ml, (3) trimethoprim at 100 µg/ml, (4) trimethoprim at 50 µg/ml, or (N) media with no antibiotic were spotted onto filter disks. (B) Diameter of the halo inhibition were measured for three biological replicates of each and the average and standard deviation of each were calculated.* indicates significant difference from empty vector control (p > 0.05 determined by 2-tailed Student's t-test). (C) Serial dilutions of each strain were spotted onto M9-glucose agar plates with chloramphenicol and IPTG with trimethoprim (0 or 1 µg/ml) or sulfathiazole (0 or 0.1 µg/ml). E. coli overexpressing panB were more sensitive to both folate inhibitors than E. coli with empty vector control.

<a id='58943ba0-9821-4b4f-8849-1ebbdb1bc6a5'></a>

supplemented with pantothenate and various levels of sulfathiazole or trimethoprim. Deletion of _panB_ did not alter the sensitivity to either antifolate (data not shown).

<a id='050b63fb-3e3b-41bd-90e9-895751e6fe16'></a>

Growth phenotypes can be caused by very indirect effects,
as shown in recent studies on mutants affected in vitamin
B6 damage that propagates to CoA and folate metabolism
(Flynn et al., 2013; Downs and Ernst, 2015). Pterin pools
were therefore analyzed in strains overexpressing or lacking
panB to determine whether direct effects could be observed.
According to our hypothesis, overexpressing panB will cause a
buildup in cells or medium of H4-HMPterin and its dihydro
form (which are both analyzed as the oxidized form 6-
hydroxymethylpterin).

<a id='b8825c40-d2aa-4d0f-b8ea-bf63069d4366'></a>

Overexpression of _panB_ (as a pUC19 construct) in _E. coli_ MG1655 indeed led to accumulation of 6-hydroxymethylpterin in both medium (five-fold) and cells (three-fold) (Figure 5A). Also, the total pterin content of the medium doubled in cultures overexpressing _panB_; the total intracellular content remained same as the control (Figure 5A). The ratio of pterin to monapterin was 4.5 in cells overexpressing _panB_ compared to 1.2 in control cells (Figure 5A). Note that tetrahydromonapterin (analyzed as monapterin) is known to be a major _E. coli_ pterin (Pribat et al., 2010) and that pterin is a breakdown product of both tetrahydromonapterin and 6-hydroxymethyldihydropterin (Forrest and Van Baalen, 1970; Davis et al., 1988). The data for overexpression of _panB_ are thus consistent with a damage

<a id='f775826b-ba06-4fc9-9a8a-c61dedadb268'></a>

hypothesis. The deletion of _panB_ had no impact on pterin pools (Figure 5B).

<a id='1e8051d4-a381-4178-90e1-b7542d484c8b'></a>

Folate pools were also analyzed in the strain overexpressing _panB_. As shown in **Figure 6A**, a 46% increase in total folates was observed, contributed by substantial increases in 5-methyltetrahydrofolate and in THF/CH₂-THF (which are both analyzed as THF) that were partially offset by decreases in 5-formyl-THF and 5,10-methenyl-THF/10-formyl-THF (which are analyzed together). The folate pools that increased were largely polyglutamyl forms (**Figure 6B**), which are generally more metabolically active than monoglutamyl forms (Suh et al., 2001; Green and Matthews, 2007). The increase in total folate content appeared counter-intuitive as a folate-cleaving reaction of PanB might be expected to deplete folates.

<a id='8f8fdba3-a1ba-4711-a33e-ab133b649b1c'></a>

The observed increase in folate pools upon overexpression of *panB* suggested a potential regulation of the folate genes, particularly those involved in pterin synthesis. Gene expression of *folK*, *folB*, *folE*, and *panB* was analyzed by quantitative PCR in *E. coli* MG1655 overexpressing *panB* (as the pCA24N construct). Upon IPTG induction, the expression of *panB* increased over *E. coli* MG1655 harboring empty vector by up to 6000-fold. When *panB* induction was 6000-fold, the expression of *folK*, *folB*, and *folE* increased by about 10-fold (Figure S3). With the level of *panB* induction achieved was lower (500-fold), however, the expression of all three folate genes was essentially unaffected (not shown). Variation in induction of *panB* presumably reflects

<a id='9fe0c77e-b902-4fe2-9ab6-173a03f2cd71'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='847e83e9-a128-423c-8a00-7311057d9833'></a>

8

<a id='5bb97cde-284b-4c4f-b53a-91e096f8b698'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='2021e0ec-cdd6-41bc-a358-712b0da0a26f'></a>

Thiaville et al.

<a id='875f6ceb-a4d3-41a0-afe7-2ab9d54b99ec'></a>

Folate Cleavage by PanB

<a id='c3a19497-7d79-478d-a173-ca88a91ea022'></a>

<::Figure 5: Quantification of pterin pools in *E. coli* cells over- or underexpressing PanB. The figure consists of two main panels, (A) and (B), each containing multiple bar charts. A 1000-fold difference in scale is noted between the two leftmost frames of panel A (reporting 6-hydroxymethylpterin levels in pmol mg⁻¹ protein) and the two rightmost frames of panel A (reporting all pterin levels in nmol mg⁻¹ protein). Asterisks indicate significant differences: *P* < 0.05 (*), *P* < 0.01 (**), or *P* < 0.001 (***). (A) Quantification of intra- and extracellular pterins extracted from *E. coli* wild type MG1665 harboring pUC19 (vector) or overexpressing *panB* (PanB). Four bar charts are presented, comparing 'vector' (dark gray bars) and 'PanB' (light gray bars). All charts include error bars representing standard errors from three biological replicates. Top left chart: Extracellular 6-OHPt (6-hydroxymethylpterin) levels. Y-axis: 6-OHPt, pmol mg⁻¹ protein, ranging from 0 to 200. X-axis labels: vector, PanB. Top middle-left chart: Intracellular 6-OHPt levels. Y-axis: 6-OHPt, pmol mg⁻¹ protein, ranging from 0 to 8. X-axis labels: vector, PanB. Top middle-right chart: Extracellular pterins (Mpt, 6-OHPt, Pt, Total). Y-axis: nmol mg⁻¹ protein, ranging from 0 to 12. X-axis labels: Mpt (monapterin), 6-OHPt, Pt (pterin), Total. Significant differences are marked: Mpt (vector vs PanB) shows **; 6-OHPt (vector vs PanB) shows ***; Pt (vector vs PanB) shows **; Total (vector vs PanB) shows **. Top right chart: Intracellular pterins (Mpt, 6-OHPt, Pt, Total). Y-axis: nmol mg⁻¹ protein, ranging from 0 to 0.4. X-axis labels: Mpt, 6-OHPt, Pt, Total. Significant differences are marked: Mpt (vector vs PanB) shows *; Pt (vector vs PanB) shows *. (B) Quantification of intra- and extracellular pterins extracted from *E. coli* wild type BW25113 and Δ*panB*::kan mutant. Four bar charts are presented, comparing 'WT' (dark gray bars) and 'Δ*panB*' (light gray bars). All charts include error bars. Bottom left chart: Extracellular pterins (Mpt, 6-OHPt, Pt, Total). Y-axis: nmol mg⁻¹ protein, ranging from 0 to 6. X-axis labels: Mpt, 6-OHPt, Pt, Total. Bottom middle-left chart: Intracellular pterins (Mpt, 6-OHPt, Pt, Total). Y-axis: nmol mg⁻¹ protein, ranging from 0 to 0.8. X-axis labels: Mpt, 6-OHPt, Pt, Total.::>FIGURE 5 | Quantification of pterin pools in *E. coli* cells over- or underexpressing PanB. (A) Quantification of intra- and extracellular pterins extracted from *E. coli* wild type MG1665 harboring pUC19 (vector) or overexpressing *panB* (PanB). Strains were grown in liquid M9 medium plus 0.4% glucose to an A600 of 1.0. Cultures were induced by the addition of 0.5 mM IPTG at an A600 of 0.3. Cell extracts and media were oxidized before analysis by HPLC to convert di- and tetrahydropterins to their fluorescent aromatic forms. Pterin contents of both extracts and media are expressed per unit of protein in the cells from which they came. Data are means and standard errors from three biological replicates, and were subjected to a *t*-test. Differences in pterin content between vector control and the *panB* overexpressing strains that are significant at *P* < 0.05, < 0.01, or < 0.001 are respectively marked by one, two, or three asteriskS. Mpt, monapterin; Pt, pterin; 6-OHPt, 6-hydroxymethylpterin. Note the 1000-fold differenCe in scale between the tWo frames on the left (which report only 6-hydroxymethylpterin levels) and the two frames on the right (which report the levels of all pterins measured). (B) Quantification of intra- and extracellular pterins extracted from *E. coli* wild type BW25113 and Δ*panB*::kan mutant. Strains were grown in liquid M9 medium plus 0.4% glucose and 10 μM pantothenate to an A600 of 1.0. Samples were treated and analyzed as in (A).

<a id='f5ae3b94-475d-4c36-b6c3-921cfdd11f66'></a>

the stochastic nature of induction, as documented for the _lac_
promoter both experimentally and through modeling (Novick
and Weiner, 1957; Elowitz et al., 2002; Stamatakis and Mantzaris,
2009).

<a id='276dc88f-d8b1-409c-a86c-b224aa9659df'></a>

Metabolic Modeling Reconciles the
Experimental Evidence with the PanB
Damage Model
A kinetic model (Figure S4) of the folate synthesis pathway was
constructed to explore potential mechanistic explanations for the
increase in folate pools observed when PanB is overexpressed.
The model includes the last four steps of THF synthesis, the GlyA
reaction, which generates CH2-THF, and the proposed folate-
cleaving side-reaction of PanB. The GlyA reaction is modeled
to operate near equilibrium, while the four preceding reactions
are all modeled as irreversible and unsaturated (meaning
reaction rates are proportional to reactant concentrations).
This is consistent with the kinetic and thermodynamic data
available for these reactions (Jankowski et al., 2008; Chang

<a id='65e4b164-f59a-4999-a27b-9d456618af39'></a>

et al., 2015). The proposed PanB side reaction is also modeled as irreversible and unsaturated. A sensitivity analysis of the model (see Methods) reveals that model results are not impacted greatly by assumptions regarding the saturation states of the included enzymes. However, the near-equilibrium state of the GlyA reaction was found to be very important for controlling the steady state ratio of THF and CH2-THF predicted by the model.

<a id='f5accd2e-e366-41c7-ad9a-7a7a3c082160'></a>

Kinetic parameters and metabolite concentrations were selected for the model to fit physiological conditions and replicate the wild-type concentrations measured for H2-HMPt and THF (Figure S4). The model also replicated the net production rates predicted for THF compounds in wild-type cells based on measured growth rates (1.66e-7 mmol ml⁻¹ cytoplasm s⁻¹). While measured values are not available for many of the metabolite concentrations and kinetic parameters in the model, these parameters are restricted by the need to replicate experimental observations. Once complete, we simulated the model under wild-type conditions, demonstrating that the steady-state predicted by the model was consistent with all the experimental observations.

<a id='c7736924-57cb-4a31-8784-532ab2ff16a5'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='ee9fcdb3-a38d-45a6-bc90-9ba551839f0b'></a>

9

<a id='dbb13301-866d-4bae-b89a-c7722ac34249'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='83d81f1e-474f-4c59-a1f8-1dd747d9b3e2'></a>

Thiaville et al.

<a id='e1759198-8a5b-44bc-ba1d-4c340d0a1bc2'></a>

Folate Cleavage by PanB

<a id='fb6e0bbd-923e-4ba6-b3f1-a2252cc47616'></a>

<::chart:FIGURE 6 | Effect of PanB overexpression on folate levels in E. coli cells. Wild type E. coli cells overexpressing panB or harboring empty vector (control) were grown as in Figure 5A. (A) Total folates observed. The total folate level in cells overexpressing PanB was significantly different (*p < 0.05) from that in the vector control. (B) Total folates observed in mono- and polyglutamyl form. Abbreviations: 5,10-CH₂-THF, 5,10-methylenetetrahydrofolate; 5-CH₃-THF, 5-methyltetrahydrofolate; 5,10-CH=THF, 5,10-methenyltetrahydrofolate; 10-CHO-THF, 10-formyltetrahydrofolate; 5-CHO-THF, 5-formyltetrahydrofolate. Small amounts of 10-formyldihydrofolate (which forms during extraction from 10-formyltetrahydrofolate) were added to the 10-formyltetrahydrofolate pool. (A) Bar chart showing total folates in E. coli cells. The y-axis is 'Folates (pmol mg⁻¹ protein)' ranging from 0 to 1800. The x-axis shows two conditions: 'vector' and 'panB'. Each condition has a stacked bar representing different folate forms. Legend for folate forms: white square for THF + 5,10-CH₂-THF, light gray square for 5-CH₃-THF, dark gray square for 5,10-CH=THF + 10-CHO-THF, and very light gray square for 5-CHO-THF. For 'vector', the total folate is around 1100 pmol mg⁻¹ protein. The stack shows: THF + 5,10-CH₂-THF at ~220, 5-CH₃-THF at ~180, 5,10-CH=THF + 10-CHO-THF at ~550, and 5-CHO-THF at ~150. For 'panB', the total folate is around 1600 pmol mg⁻¹ protein. The stack shows: THF + 5,10-CH₂-THF at ~670 (*), 5-CH₃-THF at ~600 (*), 5,10-CH=THF + 10-CHO-THF at ~200, and 5-CHO-THF at ~130. Error bars are shown for each segment and total. (B) Bar chart showing total folates observed in mono- and polyglutamyl form. The y-axis is 'Folates (pmol mg⁻¹ protein)' ranging from 0 to 800. The x-axis shows four groups of folate forms: 'THF + 5,10-CH₂-THF', '5-CH₃-THF', '5,10-CH=THF + 10-CHO-THF', and '5-CHO-THF'. Each group has two bars: 'vector' and 'panB'. Each bar is stacked, representing 'Monoglutamyl' (dark gray) and 'Polyglutamyl' (light gray). Legend: dark gray square for Monoglutamyl, light gray square for Polyglutamyl. For 'THF + 5,10-CH₂-THF': 'vector' has ~240 total (Monoglutamyl ~60, Polyglutamyl ~180), 'panB' has ~700 total (*), (Monoglutamyl ~100, Polyglutamyl ~600). For '5-CH₃-THF': 'vector' has ~180 total (Monoglutamyl ~70, Polyglutamyl ~110), 'panB' has ~600 total (*), (Monoglutamyl ~180, Polyglutamyl ~420). For '5,10-CH=THF + 10-CHO-THF': 'vector' has ~520 total (Monoglutamyl ~290, Polyglutamyl ~230), 'panB' has ~250 total (*), (Monoglutamyl ~180, Polyglutamyl ~70). For '5-CHO-THF': 'vector' has ~170 total (Monoglutamyl ~120, Polyglutamyl ~50), 'panB' has ~70 total (*), (Monoglutamyl ~40, Polyglutamyl ~30). Error bars are shown for each segment and total.::>

<a id='9641a2fd-0730-460e-95ef-7167ae04cbba'></a>

Next, we simulated the overexpression of PanB by increasing only the kinetic constant of the mass-action kinetic equation for the PanB folate-cleaving reaction (which integrates the enzyme concentration of PanB), leaving all other model parameters the same. In this simulation, all metabolite concentrations started at the steady-state values predicted from the wild-type model (Figure 7A). Immediately, the CH2-THF (and THF) concentration began to drop due to the larger flux through the PanB side reaction. This led to a rise in the concentrations of H2-HMPt (and its pyrophosphate, the PanK reaction product), which in turn led to a rise in the flux through the THF synthesis pathway, leading to the slow recovery of the THF concentration back to—but not exceeding—the wild-type values. Thus, this simulation successfully replicates the rise in H2-HMPt concentration that accompanied the overexpression of PanB in our experiments, but it fails to replicate the rise in THF concentrations, meaning the overexpression of PanB alone cannot explain all experimental observations.

<a id='f380a077-28a3-4d33-af27-64d6c09f93c5'></a>

<::chart: FIGURE 7 | Model-predicted changes in the concentrations of folates and their precursors in response to overexpression of PanB. (A) The response when only the Vmax of the PanB folate-cleaving reaction is increased, leaving other model parameters the same. The chart displays two subplots, A and B, both showing Concentration (mmol/ml) on the y-axis against Time since PanB overexpression (sec) on the x-axis. In subplot A, the x-axis ranges from 0 to 10000 seconds. The y-axis is split, with the upper range from 0 to 0.00018 and the lower range from 4.00E-06 to 2.80E-05. Several lines represent different compounds: Tetrahydrofolate (blue, increasing to ~0.00016), 5,10-methylenetetrahydrofolate (red, increasing to ~0.00008), Dihydropteroate (orange, stable at ~2.7E-05), Dihydrofolate (purple, stable at ~2.4E-05), pABA (light green, stable at ~1.9E-05), 6-hydroxymethyldihydropterin pyrophosphate (dark red, stable at ~1.4E-05), and 6-hydroxymethyldihydropterin (light blue, stable at ~8E-06). (B) The response when both the PanB Vmax and the external flux into 6-hydroxymethyldihydropterin are increased at the same time. In subplot B, the x-axis ranges from 0 to 100000 seconds. The y-axis is split, with the upper range from 0 to 0.0006 and the lower range from 4.00E-06 to 3.40E-05. Similar compounds are plotted: Tetrahydrofolate (blue, increasing to ~0.0005), 5,10-methylenetetrahydrofolate (red, increasing to ~0.00028), Dihydropteroate (orange, stable at ~3.0E-05), Dihydrofolate (purple, stable at ~2.7E-05), pABA (light green, stable at ~2.1E-05), 6-hydroxymethyldihydropterin pyrophosphate (dark red, stable at ~1.5E-05), and 6-hydroxymethyldihydropterin (light blue, stable at ~8E-06).::>

<a id='f8af2d05-5bf5-4b21-b513-dc44fb960a77'></a>

We therefore hypothesized that the initial drop in THF concentration predicted when PanB is overexpressed triggers induction of the enzymes leading into the THF synthesis pathway, thereby increasing the flux to folates and more rapidly restoring folate concentration. We tested this hypothesis by repeating the previous simulations, but this time increasing the external flux into H2-HMPt and pABA at the same time as we increase the kinetic constant of the mass-action kinetic equation for PanB kinetic constant. In this scenario, we still see an initial dip in THF concentrations, which accompanies the rise in H2-HMPt, but this time, the THF concentrations recover more rapidly and ultimately rise beyond the wild-type levels and reach new steady-state values that closely resemble those observed in the PanB overexpression experiments (Figure 7B). The analysis of expression levels the folEBK by quantitative PCR (Figure S3) indicate that an increase in H2-HMPt biosynthesis can indeed occur when panB is highly overexpressed.

<a id='f44eb484-f755-431a-aaf0-5a3596056918'></a>

A remaining issue is whether our experimental observations can be reproduced by a kinetic model that lacks a PanB-mediated folate cleavage reaction. If one models the FolK reaction to be in a saturated state with appropriately tuned kinetic parameters, the observed changes in metabolite concentration can be replicated to co-occur with a rise in flux through the folate pathway. However, this scenario does not explain

<a id='9309e5fc-70e7-43cc-bd51-1f55d98ac73f'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='f7f86a0b-a521-4e99-9972-5338d147e71c'></a>

10

<a id='7793905c-0702-4b0f-95a5-d52798f9a9f2'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='b310ec76-5fee-4dd3-b956-57bbb2f666e8'></a>

Thiaville et al.

<a id='b16c1849-2300-4df3-89b1-24d564f6ae1e'></a>

Folate Cleavage by PanB

<a id='0c022856-75bb-4d26-8891-97d1bf915965'></a>

why the folate pathway flux rises with the induction of PanB, nor does it explain the direct link between the THF and H2-HMPt concentrations implied by the experimental data. A model that includes the PanB folate-cleaving reaction thus accounts more fully for the observations than one that does not.

<a id='4273a90e-d67c-4dfd-9f06-74907fba6b17'></a>

## DISCUSSION

This work illustrates the power of comparative genomics approaches to uncover novel damage reactions and repair mechanisms (Linster et al., 2013). Physical clustering combined with gene duplication clues in association with analysis of the biochemical literature led us to infer that PanB damages the THF molecule as a side reaction. In the course of normal activity, PanB catalyzes formation of an adduct between α-ketoisovalerate and CH₂-THF (Figure 3). In order to release pABA-Glu from the complex, we hypothesize that PanB provides a suitably disposed general acid to deliver a proton to the pABA nitrogen, simultaneous with general base catalyzed attack of water at the methylene carbon to release pABA and generate the 6-hydroxymethyl group.

<a id='74af2bd9-1a6b-47d1-9b9b-c020a99be48e'></a>

Possible path A of the side reaction involves an attack of water to release 2-dehydropantoate and directly produce H4-HMPterin. Possible path B involves hydrolytic attack on the bridging methylene carbon between the pterin ring and the α-ketoisovalerate adduct. This displacement reaction by water is reasonable given the stabilization of the enolate leaving group as the Mg2+ complex, and possible general base catalysis to assist the attack of water. The resulting N5 hydroxymethyl group is a hemiaminal and should equilibrate to liberate free H4-HMPterin and formaldehyde. One question remains open, however, as the product of this side reaction is H4-HMPterin, but the dihydro form is the normal FolK substrate. Thus, either there is an oxidation step, most likely spontaneous (Davis et al., 1988) before FolK acts, or FolK (and the subsequent folate pathway enzymes FolP and FolC) can act on the tetrahydro forms of their substrates instead of the dihydro forms—in which case DHFR/FolA would be dispensable for this salvage reaction. Analysis of the structures of FolK, FolP, and FolC with substrates (PDB codes 1Q0N, 2DZB, 1W78, and Figure S5) suggests that these three enzymes would not discriminate between the di- and tetrahydro forms of their substrates and that H4-HMPterin could be recycled.

<a id='a9fd92ab-668f-4ce2-b284-c50c9cb3f606'></a>

Overexpression of PanB caused expected and unexpected effects. Expectedly, levels of 6-hydroxymethylpterin and total pterins increased. Unexpectedly, so did folate levels. However, as kinetic modeling showed, the folate increase can be accounted for by a very reasonable assumption, viz. that depletion of certain folates (or conceivably the buildup of folate damage products) leads to upregulation of the folate pathway. he observed increase in folate production appears to be the only case so far reported of a folate pathway regulatory response to a physiological perturbation (Tran and Nichols, 1991; Green and Matthews, 2007). The scale of the upregulation of the pterin branch of the folate pathway—a doubling (Figure 5A)—is

<a id='dce346e7-c127-4dea-b3e3-c560b0f64e32'></a>

particularly striking, as is the loss to the medium of most of the extra pterin production. It should be noted that some cell lysis was observed in cells overexpressing *panB*, which could account for a portion of the observed increase in extracellular pterins. However, it was previously observed that, in wild type *E. coli*, folate synthesis accounts for <20% of the pterin moieties produced, most of which are exported to the medium (Pribat et al., 2010). Our present data agree with this observation (Figures 5A, 6A), and further show that the increase in total folate production elicited by PanB overexpression (0.5 nmol mg⁻¹ protein) was almost ten-fold less than the increase in pterin production (4.7 nmol mg⁻¹ protein), all of it found in the medium. Thus, an increase in intracellular folate cleavage triggers a doubling of pterin production, most of which flows not to folate synthesis but out into the medium.

<a id='ae212bbf-7aa2-416b-a5b6-7b644cf89271'></a>

The expanded folate pool in E. coli cells overexpressing panB raises the question of how this observation can be reconciled with the antifolate sensitivity phenotypes of these cells (Figure 4B).
One possibility is that pABA-Glu recycling is inefficient, so that an increased flux to folates depletes the pABA pool, which increases sulfathiazole sensitivity. This scenario is supported by the findings that pterin overproduction in tomato fruit increased the flux to folates but caused pABA depletion (Díaz de la Garza et al., 2004), and that pABA supplementation increased folate production in Lactococcus lactis (Sybesma et al., 2003).
Another possibility is that accumulated pterins competitively inhibit dihydrofolate reductase, and hence potentiate the action of trimethoprim. In support of this possibility, bacterial and mammalian dihydrofolate reductases are known to bind (and inefficiently reduce) certain dihydropterins (Armarego et al., 1980; Matsuura and Sugimoto, 1981).

<a id='aa1e030b-b034-43ae-90ad-f10e2b78d764'></a>

A role for PanB in THF damage could explain several long-standing observations. First, it has been shown that PanB is a limiting step in pantothenate synthesis (Rubio and Downs, 2002); PanB levels could have been kept low to avoid damage. Second, there is evidence that folate and pantothenate pathways cross-connect. In *Bacterium linens* str. 456, pABA was able to substitute for the pantothenate requirement and vice versa (Purko et al., 1953). Each compound was shown to enable the synthesis of the other (the pABA analysis in this study involved an acid hydrolysis step and bioassay of pABA, so that folate was probably the main source of pABA). The pABA (folate) requirement for pantothenate synthesis was subsequently explained by the discovery of the folate-dependent ketopantoate hydroxymethyltransferase PanB. The pantothenate requirement for "pABA" synthesis appears never to have been explained. This pantothenate requirement cannot be explained by a CoA-dependent step in chorismate or pABA synthesis. A simple possibility is that *B. linens* str. 456 has a PanB defect that is rescued by a high folate concentration, and that supplying pABA boosts folate content and hence pantothenate synthesis, i.e., there is no defect in folate synthesis. A more complex possibility is that *B. linens* str. 456 has a FolP defect that can be corrected by supplementary pABA, that FolP and FolK are coupled, and that in the absence of supplemental pABA,

<a id='3d6d8f3e-dc3d-4b1b-9284-6db55778869e'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='dbbec43b-b962-42a9-918c-1e8a7ba2b474'></a>

11

<a id='631e9c08-c536-40a6-8199-92a787e2a7df'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='d0d02a65-2e60-4d35-8c74-daad9e154737'></a>

Thiaville et al.

<a id='91daf93d-0e05-4441-b93c-2e7215edb6b0'></a>

Folate Cleavage by PanB

<a id='8b5665e6-204d-4ec1-acb3-1fbe69224226'></a>

6-hydroxymethyldihydropterin pyrophosphate accumulates and negatively regulates (Mouillon et al., 2002) the FolK reaction so that 6-hydroxymethyldihydropterin accumulates, favoring spontaneous loss of the side-chain and so further compromises folate synthesis and hence PanB activity.

<a id='5d5812b0-a0e8-483b-8f89-70c711ad6aae'></a>

It would obviously be of interest to test PanB for a folate-cleaving side activity *in vitro*. There are, however, major difficulties with this type of experiment. First, THF and CH₂-THF are highly labile folates and readily undergo C9-N10 bond cleavage in physiological conditions (Wilson and Horne, 1983), so that the background cleavage rate against which to detect a minor activity of PanB would be high. The half-life of free THF, for example, is only about 40 min at physiological pH (Suh et al., 2001). Reduced folates are greatly stabilized against spontaneous cleavage *in vivo* by binding to enzymes and other folate-binding proteins (Suh et al., 2001), but attempting such stabilization *in vitro* would necessarily sequester folates away from PanB. Second, CH₂-THF is in spontaneous equilibrium with THF and formaldehyde (Blakley, 1959) so that its use as a substrate entails the presence of at least a low level of formaldehyde, which reacts readily with proteins, blocking reactive residues (Metz et al., 2004). Finally, there is the concern that, like some other side-reactions (Downs and Ernst, 2015), the folate-cleaving reaction could depend so much the cellular context that it can only be investigated in a complex system.

<a id='c551269e-5312-49b5-a09b-ca4b044658e5'></a>

## REFERENCES

Altschul, S. F., Madden, T. L., Schäffer, A. A., Zhang, J., Zhang, Z., Miller, W., et al.
(1997). Gapped BLAST and PSI-BLAST: a new generation of protein database
search programs. Nucleic Acids Res. 25, 3389–3402.
Amin, N., and Peterkofsky, A. (1995). A dual mechanism for regulating cAMP
levels in Escherichia coli. J. Biol. Chem. 270, 11803–11805.
Armarego, W. L. F., Waring, P., and Williams, J. W. (1980). Absolute configuration
of 6-methyl-5,6,7,8-tetrahydropterin produced by enzymic reduction
(dihydrofolate reductase and NADPH) of 6-methyl-7,8-dihydropterin. J.
Chem. Soc. Chem. Commun. 334–336. doi: 10.1039/c39800000334
Baba, T., Ara, T., Hasegawa, M., Takai, Y., Okumura, Y., Baba, M., et al. (2006).
Construction of Escherichia coli K-12 in-frame, single-gene knockout mutants:
the Keio collection. Mol. Syst. Biol. 2:2006.0008. doi: 10.1038/msb4100050
Bauer, A. W., Kirby, W. M., Sherris, J. C., and Turck, M. (1966). Antibiotic
susceptibility testing by a standardized single disk method. Am. J. Clin. Pathol.
45, 493–496.
Bennett, B. D., Kimball, E. H., Gao, M., Osterhout, R., Van Dien, S. J., and
Rabinowitz, J. D. (2009). Absolute metabolite concentrations and implied
enzyme active site occupancy in Escherichia coli. Nat. Chem. Biol. 5, 593–599.
doi: 10.1038/nchembio.186
Berman, H. M., Westbrook, J., Feng, Z., Gilliland, G., Bhat, T. N., Weissig, H.,
et al. (2000). The Protein Data Bank. Nucleic Acids Res. 28, 235–242. doi:
10.1093/nar/28.1.235
Blakley, R. L. (1959). The reaction of tetrahydropteroylglutamic acid and related
hydropteridines with formaldehyde. Biochem. J. 72, 707–715.
Blaszczyk, J., Shi, G., Yan, H., and Ji, X. (2000). Catalytic center assembly of HPPK
as revealed by the crystal structure of a ternary complex at 1.25 Å resolution.
Structure 8, 1049–1058. doi: 10.1016/S0969-2126(00)00502-5
Bochner, B. R., and Ames, B. N. (1982). ZTP (5-amino 4-imidazole carboxamide
riboside 5'-triphosphate): a proposed alarmone for 10-formyl-tetrahydrofolate
deficiency. Cell 29, 929–937.
Bozzo, G. G., Basset, G. J., Naponelli, V., Noiriel, A., Gregory, J. F. III.
and Hanson, A. D. (2008). Characterization of the folate salvage enzyme

<a id='e3702301-1d32-4314-9c4d-15f91a53d070'></a>

**AUTHOR CONTRIBUTIONS**

VC and AH designed the study and supervised the experimental studies, CH and AH created and analyzed the kinetic model, VC performed the bioinformatic analysis with the help of KH. JT and GH did the molecular biology and genetics experiments, OF conducted the pterin analyses. RD and CG conducted the folate analyses. NH proposed the biochemical mechanisms. VC, AH, NH and CH wrote the manuscript and all authors edited it.

<a id='74ebcae6-6b73-4631-a2f7-ef3daf9f6dae'></a>

## FUND

This work was funded by US National Science Foundation (NSF) grants MCB-1153413.

<a id='976d3e48-79a4-4e62-856d-99a25ec38a6c'></a>

# ACKNOWLEDGMENTS

We thank S. Shanker and the staff at UF ICBR for Sanger DNA sequencing.

<a id='304cc6cf-1a4f-4167-a192-1f0e61897699'></a>

**SUPPLEMENTARY MATERIAL**
The Supplementary Material for this article can be found online at: http://journal.frontiersin.org/article/10.3389/fmicb. 2016.00431

<a id='282571a7-c210-4c76-9d8d-0843671fb572'></a>

p-aminobenzoylglutamate hydrolase in plants. Phytochemistry 69, 29-37. doi:
10.1016/j.phytochem.2007.06.031
Carter, E. L., Jager, L., Gardner, L., Hall, C. C., Willis, S., and Green, J. M. (2007).
Escherichia coli abg genes enable uptake and cleavage of the folate catabolite p-
aminobenzoyl-glutamate. J. Bacteriol. 189, 3329-3334. doi: 10.1128/JB.01940-
06
Chang, A., Schomburg, I., Placzek, S., Jeske, L., Ulbrich, M., Xiao, M., et al. (2015).
BRENDA in 2015: exciting developments in its 25th year of existence. Nucleic
Acids Res. 43, D439-D446. doi: 10.1093/nar/gku1068
Chelliah, V., Juty, N., Ajmera, I., Ali, R., Dumousseau, M., Glont, M., et al.
(2015). BioModels: ten-year anniversary. Nucleic Acids Res. 43, D542-D548.
doi: 10.1093/nar/gku1181
Corpet, F. (1988). Multiple sequence alignment with hierarchical clustering.
Nucleic Aids Res. 16, 10881-10890.
Cossins, E. A., and Chen, L. (1997). Folates and one-carbon metabolism in plants
and fungi. Phytochemistry 45, 437-452.
Crooks, G. E., Hon, G., Chandonia, J. M., and Brenner, S. E. (2004). WebLogo: a
sequence logo generator. Genome Res. 14, 1188-1190. doi: 10.1101/gr.849004
Dántola, M. L., Vignoni, M., Capparelli, A. L., Lorente, C., and Thomas, A. Η.
(2008). Stability of 7,8-dihydropterins in air-equilibrated aqueous solutions.
Helv. Chim. Acta 91, 411-425. doi: 10.1002/hlca.200890046
Davis, M. D., Kaufman, S., and Milstien, S. (1988). The auto-oxidation of
tetrahydrobiopterin. Eur. J. Biochem. 173, 345-351.
de Berardinis, V., Vallenet, D., Castelli, V., Besnard, M., Pinet, A., Cruaud, C., et al.
(2008). A complete collection of single-gene deletion mutants of Acinetobacter
baylyi ADP1. Mol. Syst. Biol. 4, 174. doi: 10.1038/msb.2008.10
de Crécy-Lagard, V., El Yacoubi, B., de la Garza, R., Noiriel, A., and Hanson,
A. (2007). Comparative genomics of bacterial and plant folate synthesis and
salvage: predictions and validations. BMC Genomics 8:245. doi: 10.1186/1471-
2164-8-245
de Crécy-Lagard, V. (2014). Variations in metabolic pathways create
challenges for automated metabolic reconstructions: examples from the
tetrahydrofolate synthesis pathway. Comput. Struct. Biotechnol. J. 10, 41-50.
doi: 10.1016/j.csbj.2014.05.008

<a id='55d54192-41df-419d-a893-b850114b8b29'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='474e0a63-e093-45f4-b77f-0d6bc49f3370'></a>

12

<a id='1b31b14b-742b-49b2-8a5b-81d78e6c2976'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='c68dfa62-44d0-486b-a66b-3ba908bb55b6'></a>

Thiaville et al.

<a id='9121860e-cd78-4cd2-99ed-07955746a435'></a>

Folate Cleavage by PanB

<a id='f2c116de-c2cf-4867-b742-8c75959d7e11'></a>

De Wit, R. J., van der Velden, R. J., and Konijn, T. M. (1983). Characterization of the folic acid C9-N10-cleaving enzyme of Dictyostelium minutum V3. J. Bacteriol. 154, 859-863.Diaz de la Garza, R., Quinlivan, E. P., Klaus, S. M., Basset, G. J., Gregory, J. F. III, and Hanson, A. D. (2004). Folate biofortification in tomatoes by engineering the pteridine branch of folate synthesis. Proc. Natl. Acad. Sci. U.S.A. 101, 13720-13725. doi: 10.1073/pnas.0404208101Disz, T., Akhter, S., Cuevas, D., Olson, R., Overbeek, R., Vonstein, V., et al. (2010). Accessing the SEED genome databases via Web services API: tools for programmers. BMC Bioinformatics 11:319. doi: 10.1186/1471-2105-11-319Downs, D. M., and Ernst, D. C. (2015). From microbiology to cancer biology: the Rid protein family prevents cellular damage caused by endogenously generated reactive nitrogen species. Mol. Microbiol. 96, 211-219. doi: 10.1111/mmi.12945Edgar, R. C. (2004). MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic Acids Res. 32, 1792-1797. doi: 10.1093/nar/gkh340Elowitz, M. B., Levine, A. J., Siggia, E. D., and Swain, P. S. (2002). Stochastic gene expression in a single cell. Science 297, 1183-1186. doi: 10.1126/science.1070919Flynn, J. M., Christopherson, M. R., and Downs, D. M. (2013). Decreased coenzyme A levels in ridA mutant strains of Salmonella enterica result from inactivated serine hydroxymethyltransferase. Mol. Microbiol. 89, 751-759. doi: 10.1111/mmi.12313Forrest, H. S., and Van Baalen, C. (1970). Microbiology of unconjugated pteridines. Annu. Rev. Microbiol. 24, 91-108. doi: 10.1146/annurev.mi.24.100170.000515Gerdes, S., Lerma-Ortiz, C., Frelin, O., Seaver, S. M., Henry, C. S., de Crecy-Lagard, V., et al. (2012). Plant B vitamin pathways and their compartmentation: a guide for the perplexed. J. Exp. Bot. 63, 5379-5395. doi: 10.1093/jxb/ers208Goto, M., Forrest, H. S., Dickerman, L. H., and Urushibara, T. (1965). Isolation of a new naturally occurring pteridine from bacteria, and its relation to folic acid biosynthesis. Arch. Biochem. Biophys. 111, 8-14.Green, J. M., and Matthews, R. G. (2007). Folate Biosynthesis, reduction, and polyglutamylation and the interconversion of folate derivatives. Ecosal Plus 2. doi: 10.1128/ecosalplus.3.6.3.6Gregory, J. F. III. (1989). Chemical and nutritional aspects of folate research: analytical procedures, methods of folate synthesis, stability, and bioavailability of dietary folates. Adv. Food Nutr. Res. 33, 1-101.Guldener, U., Koehler, G. J., Haussmann, C., Bacher, A., Kricke, J., Becher, D., et al. (2004). Characterization of the Saccharomyces cerevisiae Foll protein: starvation for C1 carrier induces pseudohyphal growth. Mol. Biol. Cell 15, 3811-3828. doi: 10.1091/mbc.E03-09-0680Guzman, L. M., Belin, D., Carson, M. J., and Beckwith, J. (1995). Tight regulation, modulation, and high-level expression by vectors containing the arabinose PBAD promoter. J. Bacteriol. 177, 4121-4130.Hanson, A. D., and Gregory, J. F. III. (2011). Folate biosynthesis, turnover, and transport in plants. Annu. Rev. Plant Biol. 62, 105-125. doi: 10.1146/annurev-arplant-042110-103819Hoops, S., Sahle, S., Gauges, R., Lee, C., Pahle, J., Simus, N., et al. (2006). COPASI-a Complex PAthway SImulator. Bioinformatics 22, 3067-3074. doi: 10.1093/bioinformatics/btl485Huerta-Cepas, J., Dopazo, J., and Gabaldon, T. (2010). ETE: a python environment for tree exploration. BMC Bioinformatics 11:24. doi: 10.1186/1471-2105-11-24Jankowski, M. D., Henry, C. S., Broadbelt, L. J., and Hatzimanikatis, V. (2008). Group contribution method for thermodynamic analysis of complex metabolic networks. Biophys. J. 95, 1487-1499. doi: 10.1529/biophysj.107.124784Jonsson, M., and Swedberg, G. (2005). Hydroxymethyldihydropterin pyrophosphokinase from Plasmodium falciparum complements a folk-knockout mutant in E. coli when expressed as a separate polypeptide detached from dihydropteroate synthase. Mol. Biochem. Parasitol. 140, 123-125. doi: 10.1016/j.molbiopara.2004.11.016Kanehisa, M., and Goto, S. (2000). KEGG: kyoto encyclopedia of genes and genomes. Nucleic Acids Res. 28, 27-30. doi: 10.1093/nar/28.1.27Kim, P. B., Nelson, J. W., and Breaker, R. R. (2015). An ancient riboswitch class in bacteria regulates purine biosynthesis and one-carbon metabolism. Mol. Cell 57, 317-328. doi: 10.1016/j.molcel.2015.01.001Kitagawa, M., Ara, T., Arifuzzaman, M., Ioka-Nakamichi, T., Inamoto, E., Toyonaga, H., et al. (2005). Complete set of ORF clones of Escherichia coli

<a id='b33824bf-b5e6-4345-b15b-185f292ad052'></a>

ASKA library (A complete set of E. coli K-12 ORF archive): unique resources for biological research. DNA Res. 12, 291-299. doi: 10.1093/dnares/dsi012
Kukko, E., and Heinonen, J. (1982). The intracellular concentration of pyrophosphate in the batch culture of Escherichia coli. Eur. J. Biochem. 127, 347-349.
Kukko-Kalske, E., Lintunen, M., Inen, M. K., Lahti, R., and Heinonen, J. (1989). Intracellular PPi concentration is not directly dependent on amount of inorganic pyrophosphatase in Escherichia coli K-12 cells. J. Bacteriol. 171, 4498-4500.
Li, W., Cowley, A., Uludag, M., Gur, T., McWilliam, H., Squizzato, S., et al. (2015). The EMBL-EBI bioinformatics web and programmatic tools framework. Nucleic Acids Res. 43, W580-W584. doi: 10.1093/nar/gkv279
Linster, C. L., Van Schaftingen, E., and Hanson, A. D. (2013). Metabolite damage and its repair or pre-emption. Nat. Chem. Biol. 9, 72-80. doi: 10.1038/nchembio.1141
Matsuura, S., and Sugimoto, T. (1981). Studies on biologically active pteridines. VII. Absolute configuration of (-)-6-methyltetrahydropterin produced by enzymic reduction. Bull. Chem. Soc. Jpn. 54, 2543-2544.
McCullough, J. L., Chabner, B. A., and Bertino, J. R. (1971). Purification and properties of carboxypeptidase G 1. J. Biol. Chem. 246, 7207-7213.
Metz, B., Kersten, G. F., Hoogerhout, P., Brugghe, H. F., Timmermans, H. A., de Jong, A., et al. (2004). Identification of formaldehyde-induced modifications in proteins: reactions with model peptides. J. Biol. Chem. 279, 6235-6243. doi: 10.1074/jbc.M310752200
Mouillon, J. M., Ravanel, S., Douce, R., and Rébeillé, F. (2002). Folate synthesis in higher-plant mitochondria: coupling between the dihydropterin pyrophosphokinase and the dihydropteroate synthase activities. Biochem. J. 363, 313-319.
Niehaus, T. D., Gerdes, S., Hodge-Hanson, K., Zhukov, A., Cooper, A. J., ElBadawi-Sidhu, M., et al. (2015). Genomic and experimental evidence for multiple metabolic functions in the RidA/YjgF/YER057c/UK114 (Rid) protein family. BMC Genomics 16:382. doi: 10.1186/s12864-015-1584-3
Noiriel, A., Naponelli, V., Bozzo, G. G., Gregory, J. F. III, and Hanson, A. D. (2007a). Folate salvage in plants: pterin aldehyde reduction is mediated by multiple non-specific aldehyde reductases. Plant J. 51, 378-389. doi: 10.1111/j.1365-313X.2007.03143.x
Noiriel, A., Naponelli, V., Gregory, J. F. III, and Hanson, A. D. (2007b). Pterin and folate salvage. Plants and Escherichia coli lack capacity to reduce oxidized pterins. Plant Physiol. 143, 1101-1109. doi: 10.1104/pp.106.093633
Novick, A., and Weiner, M. (1957). Enzyme induction as an all-or-none phenomenon. Proc. Natl. Acad. Sci. U.S.A. 43, 553-566.
Oe, H., Kohashi, M., and Iwai, K. (1983). Radioassay of the folate-hydrolyzing enzyme activity, and the distribution of the enzyme in biological cells and tissues. J. Nutr. Sci. Vitaminol. 29, 523-531.
Orsomando, G., Bozzo, G. G., de la Garza, R. D., Basset, G. J., Quinlivan, E. P., Naponelli, V., et al. (2006). Evidence for folate-salvage reactions in plants. Plant J. 46, 426-435. doi: 10.1111/j.1365-313X.2006.02685.x
Ottenhof, H. H., Ashurst, J. L., Whitney, H. M., Saldanha, S. A., Schmitzberger, F., Gweon, H. S., et al. (2004). Organisation of the pantothenate (vitamin B5) biosynthesis pathway in higher plants. Plant J. 37, 61-72. doi: 10.1046/j.1365-313Χ.2003.01940.x
Overbeek, R., Begley, T., Butler, R. M., Choudhuri, J. V., Chuang, H. Y., Cohoon, M., et al. (2005). The subsystems approach to genome annotation and its use in the project to annotate 1000 genomes. Nucleic Acids Res. 33, 5691-5702. doi: 10.1093/nar/gki866
Overbeek, R., Olson, R., Pusch, G. D., Olsen, G. J., Davis, J. J., Disz, T., et al. (2014). The SEED and the Rapid Annotation of microbial genomes using Subsystems Technology (RAST). Nucleic Acids Res. 42, D206-D214. doi: 10.1093/nar/gkt1226
Perocchi, F., Jensen, L. J., Gagneur, J., Ahting, U., von Mering, C., Bork, P., et al. (2006). Assessing systems properties of yeast mitochondria through an interaction map of the organelle. PLoS Genet. 2:e170. doi: 10.1371/journal.pgen.0020170
Phillips, G., Grochowski, L. L., Bonnett, S., Xu, H., Bailly, M., Blaby-Haas, C., et al. (2012). Functional Promiscuity of the COG0720 Family. ACS Chem. Biol. 7, 197-209. doi: 10.1021/cb200329f
Powers, S. G., and Snell, E. E. (1976). Ketopantoate hydroxymethyltransferase. II. Physical, catalytic, and regulatory properties. J. Biol. Chem. 251, 3786-3793.

<a id='69d430c3-028e-40a7-9c85-a4d1c2b71d65'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='f7857035-ac22-4fca-bff8-8fd1046665a2'></a>

13

<a id='4073fa5c-f028-4a1c-a050-de46573da40c'></a>

March 2016 | Volume 7 | Article 431

<!-- PAGE BREAK -->

<a id='354abab0-67a5-4645-8f3b-2783a19f66a3'></a>

Thiaville et al.

<a id='08bb733f-1c90-49a7-922a-ca3df00b8dbe'></a>

Folate Cleavage by PanB

<a id='95942520-730e-4775-a5e4-d178adeb487c'></a>

Pribat, A., Blaby, I. K., Lara-Núñez, A., Gregory, J. F. III, de Crécy-Lagard, V., and Hanson, A. D. (2010). FolX and FolM are essential for tetrahydromonapterin synthesis in Escherichia coli and Pseudomonas aeruginosa. J. Bacteriol. 192, 475-482. doi: 10.1128/JB.01198-09
Purko, M., Nelson, W. O., and Wood, W. A. (1953). The nutritional equivalence of pantothenate and p-aminobenzoate for the growth of Bacterium linens. J. Bacteriol. 66, 561-567.
Quinlivan, E. P., McPartlin, J., Weir, D. G., and Scott, J. (2000). Mechanism of the antimicrobial drug trimethoprim revisited. FASEB J. 14, 2519-2524. doi: 10.1096/fj.99-1037com
Rao, N. N., Roberts, M. F., Torriani, A., and Yashphe, J. (1993). Effect of glpT and glpD mutations on expression of the phoA gene in Escherichia coli. J. Bacteriol. 175, 74-79.
Rubio, A., and Downs, D. M. (2002). Elevated levels of ketopantoate hydroxymethyltransferase (PanB) lead to a physiologically significant coenzyme A elevation in Salmonella enterica serovar Typhimurium. J. Bacteriol. 184, 2827-2832. doi: 10.1128/JB.184.10.2827-2832.2002
Sambrook, J. E., Fritsch, F., and Maniatis, T. (1989). Molecular Cloning: A Laboratory Manual, 2nd Edn. New York, NY: Cold Spring Harbor Laboratory Press.
Seo, K. H., Zhuang, N., Park, Y. S., Park, K. H., and Lee, K. H. (2014). Structural basis of a novel activity of bacterial 6-pyruvoyltetrahydropterin synthase homologues distinct from mammalian 6-pyruvoyltetrahydropterin synthase activity. Acta Crystallogr. D Biol. Crystallogr. 70, 1212-1223. doi: 10.1107/S1399004714002016
Srivastava, A. C., Ramos-Parra, P. A., Bedair, M., Robledo-Hernández, A. L., Tang, Y., Sumner, L. W., et al. (2011). The folylpolyglutamate synthetase plastidial isoform is required for postembryonic root development in Arabidopsis. Plant Physiol. 155, 1237-1251. doi: 10.1104/pp.110.168278
Stamatakis, M., and Mantzaris, N. V. (2009). Comparison of deterministic and stochastic models of the lac operon genetic network. Biophys. J. 96, 887-906. doi: 10.1016/j.bpj.2008.10.028
Suh, J. R., Herbig, A. K., and Stover, P. J. (2001). New perspectives on folate catabolism. Annu. Rev. Nutr. 21, 255-282. doi: 10.1146/annurev.nutr.21.1.255
Suh, J. R., Oppenheim, E. W., Girgis, S., and Stover, P. J. (2000). Purification and properties of a folate-catabolizing enzyme. J. Biol. Chem. 275, 35646-35655. doi: 10.1074/jbc.M005864200

<a id='483c77b2-6037-4614-bdf8-57a44f23465a'></a>

Sybesma, W., Starrenburg, M., Tijsseling, L., Hoefnagel, M. H., and Hugenholtz, J. (2003). Effects of cultivation conditions on folate production by lactic acid bacteria. Appl. Environ. Microbiol. 69, 4542-4548. doi: 10.1128/AEM.69.8.4542-4548.2003
Tamura, K., Stecher, G., Peterson, D., Filipski, A., and Kumar, S. (2013). MEGA6: Molecular evolutionary genetics analysis version 6.0. Mol. Biol. Evol. 30, 2725-2729. doi: 10.1093/molbev/mst197
Teller, J. H., Powers, S. G., and Snell, E. E. (1976). Ketopantoate hydroxymethyltransferase. I. Purification and role in pantothenate biosynthesis. J. Biol. Chem. 251, 3780-3785.
Tran, P. V., and Nichols, B. P. (1991). Expression of Escherichia coli pabA. J. Bacteriol. 173, 3680-3687.
Vacic, V., Iakoucheva, L. M., and Radivojac, P. (2006). Two Sample Logo: a graphical representation of the differences between two sets of sequence alignments. Bioinformatics 22, 1536-1537. doi: 10.1093/bioinformatics/btl151
Waller, J. C., Alvarez, S., Naponelli, V., Lara-Nuñez, A., Blaby, I. K., Da Silva, V., et al. (2010). A role for tetrahydrofolates in the metabolism of iron-sulfur clusters in all domains of life. Proc. Natl. Acad. Sci. U.SA. 107, 10412-10417. doi: 10.1073/pnas.0911586107
Wilson, S. D., and Horne, D. W. (1983). Evaluation of ascorbic acid in protecting labile folic acid derivatives. Proc. Natl. Acad. Sci. U.S.A. 80, 6500-6504.
Yanisch-Perron, C., Vieira, J., and Messing, J. (1985). Improved M13 phage cloning vectors and host strains: nucleotide sequences of the M13mp18 and pUC19 vectors. Gene 33, 103-119.

<a id='ce286b36-2950-452c-adc4-545986253682'></a>

**Conflict of Interest Statement:** The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

<a id='25a3c22f-cbdc-487f-a6c4-1657a9e06268'></a>

Copyright  2016 Thiaville, Frelin, García-Salinas, Harrison, Hasnain, Horenstein, Díaz de la Garza, Henry, Hanson and de Crécy-Lagard. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

<a id='7b7cac5a-41b3-4a95-ad8d-7b0470393995'></a>

Frontiers in Microbiology | www.frontiersin.org

<a id='47efed8b-0658-4685-a6df-7c0ceba7283e'></a>

14

<a id='f6f2f41e-fb85-4eca-b55b-2980acf8bebf'></a>

March 2016 | Volume 7 | Article 431