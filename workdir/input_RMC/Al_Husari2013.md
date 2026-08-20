<a id='b64e61cf-60e1-4e95-931b-3cf51660cba7'></a>

Journal of Theoretical Biology 322 (2013) 58–71

<a id='f4d4d124-64bb-4fbc-9448-e0dec42bfa4c'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a tree with a figure standing beside it, featuring the word "ELSEVIER" in orange text below.::>

<a id='e145c25f-1ab3-46cb-ad5a-677e09a234e7'></a>

Contents lists available at SciVerse ScienceDirect

<a id='7f806a2b-6202-46e8-897a-7da21ab4e17f'></a>

Journal of Theoretical Biology

<a id='6a6b92c7-0513-4279-b383-c3396b2efa29'></a>

journal homepage: www.elsevier.com/locate/yjtbi

<a id='ec571a06-fd3d-4b15-89fe-8dd80bab1afd'></a>

<::Cover of "Journal of Theoretical Biology". The background is a marbled green and white pattern. In the top left corner, there is a small logo, possibly an abstract representation of a plant or organism, with the letters "JB" or similar. The title "Journal of" is in a smaller font, and "Theoretical Biology" is in a larger, bold, red font below it.: figure::>

<a id='84de0969-51ac-4887-9ea9-c7e10e4c3325'></a>

Regulation of tumour intracellular pH: A mathematical model examining the interplay between H⁺ and lactate

<a id='93bf9607-6f91-4bc3-a530-63cb8911848b'></a>

Maymona Al-Husari a, Steven D. Webb b,*
a Department of Mathematics and Statistics, University of Strathclyde, Glasgow G1 1XH, UK
b MRC Centre for Drug Safety Science, Department of Molecular and Clinical Pharmacology, Institute of Translational Medicine, Sherrington Building, Ashton Street, The University of Liverpool, Liverpool L69 3GE, UK

<a id='3d44d0bd-eb4f-41d3-b35d-5894594c4dae'></a>

HIGHLIGHTS

* We develop a model for cellular ion transporter activity in tumour pH regulation.
* We focus on the interplay between lactate and H+ ions.
* We examine the role of the lactate/H+ symporter in pH gradient reversal.

<a id='9eaaa56c-1795-4e01-a1e7-ef9d9e095332'></a>

# ARTICLE INFO

Article history:
Received 11 June 2012
Received in revised form
31 October 2012
Accepted 3 January 2013
Available online 20 January 2013

Keywords:
Tumour microenvironment
Modelling
pH gradient
Na+/H+ antiporter
Lactate/H+ symporter

<a id='6ca9becc-dfac-4211-b7bc-450077adcc8f'></a>

A B S T R A C T

Non-invasive measurements of pH have shown that both tumour and normal cells have intracellular pH
(pHᵢ) that lies on the alkaline side of neutrality (7.1–7.2). However, extracellular pH (pHₑ) is reported to
be more acidic in some tumours compared to normal tissues. Many cellular processes and therapeutic
agents are known to be tightly pH dependent which makes the study of intracellular pH regulation of
paramount importance. We develop a mathematical model that examines the role of various
membrane-based ion transporters in tumour pH regulation, in particular, with a focus on the interplay
between lactate and H⁺ ions and whether the lactate/H⁺ symporter activity is sufficient to give rise to
the observed reversed pH gradient that is seen is some tumours. Using linear stability analysis and
numerical methods, we are able to gain a clear understanding of the relationship between lactate and
H⁺ ions. We extend this analysis using perturbation techniques to specifically examine a rapid change
in H⁺-ion concentrations relative to variations in lactate. We then perform a parameter sensitivity
analysis to explore solution robustness to parameter variations. An important result from our study is
that a reversed pH gradient is possible in our system but for unrealistic parameter estimates—pointing
to the possible involvement of other mechanisms in cellular pH gradient reversal, for example acidic
vesicles, lysosomes, golgi and endosomes.

© 2013 Elsevier Ltd. All rights reserved.

<a id='31ecab6d-d418-4002-908a-c98c9692c348'></a>

## 1. Introduction
The microenvironment of tumours can trigger various signals which promote invasion (Martinez-Zaguilan et al., 1996; Nyberg et al., 2008) and reduce tumour response to therapies (Brown, 2002; Henning et al., 2004). Some tumours are characterised by regions of acidity and hypoxia which are thought to confer a survival advantage to the tumour (Pouysségur et al., 2006; Raghunand et al., 2003). This is evident from studies where tumours exposed to long term extracellular acidity showed invasive behaviour (Martinez-Zaguilan

<a id='9497a799-4ff6-47f4-8dd7-36c05337567d'></a>

* Corresponding author. Tel.: +44 151 795 5460; fax: +44 151 794 5540.E-mail address: steven.webb@liverpool.ac.uk (S.D. Webb).

<a id='00200152-9be0-4181-9627-e0c77470d464'></a>

0022-5193/$- see front matter © 2013 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.jtbi.2013.01.007

<a id='b5b8fe20-9d2e-4225-9def-41722a509714'></a>

et al., 1996; Rofstad et al., 2006), and resistance to chemotherapeutics (Wachsberger et al., 1997).

<a id='22251a4d-23a8-479d-8dc5-bfcfeb3e0c0c'></a>

More than 80 years ago, Warburg et al. (1926) observed that
tumour cells exhibit an altered metabolism, marked by increased
glucose uptake and elevated glycolysis. In the absence of oxygen,
pyruvate is converted into two molecules of lactic acid which
dissociates rapidly into lactate and H+ ions (Berg et al., 2003).
Warburg's pioneering work also showed that even in the presence
of an ample supply of oxygen, tumour cells still undergo anaero-
bic glycolysis yielding only two ATP molecules (Warburg et al.,
1926). This type of energy metabolism is inefficient compared to
aerobic metabolism and, for a vastly growing tumour to maintain
sufficient production of ATP, the tumour cells must up-regulate
their glycolytic pathway. As a result, more lactic acid is produced
and the tumour can become very acidic (Warburg et al., 1926). In

<!-- PAGE BREAK -->

<a id='e4b0ff91-d698-4329-bef6-87ac2fb91727'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='e288cde2-d265-4bd9-a3c9-5e641312813f'></a>

59

<a id='4ccdf853-eed9-4885-a7d9-22fa609c2f73'></a>

fact, tumours were initially thought to have an acidic intracellular
pH. But, the invention of non-invasive measurements of pHᵢ by
magnetic resonance spectroscopy (MRS) has shown that tumour
pHᵢ can actually be alkaline (Griffiths, 1991).

<a id='75d0bba8-e17c-4bfd-800d-db104f4772f9'></a>

The metabolically produced hydrogen ions must be extruded to ensure a physiological pHᵢ and cell viability. This is because many cellular processes such as those associated with metabolism (Romero, 2004), the cell cycle (Fitzgerald et al., 1997; Humez et al., 2003) and cell proliferation (Boron, 1985; Mackenzie et al., 1961) are all pH sensitive. Furthermore, most mammalian cells in tissue culture will not proliferate at a pH less than 6.6 (Boron, 1985). Cells, therefore, have evolved several short and long term mechanisms to maintain their pHᵢ within the normal physiological range (pH 7.2-7.4). Short term homoeostasis, for example, involves a rapid defence mechanism that minimises changes in pH as a result of acid or alkali load (Boron, 1985). This includes physicochemical buffering, H⁺-consuming metabolic buffering and organelle sequestration or release of hydrogen ions.

<a id='7c0c9ccc-114f-43c6-af71-d9ccb9767b55'></a>

In addition, cells employ another strategy to maintain their pH through several membrane-based transport systems. The univer-sal membrane protein, Na+/H+ antiporter exports one H+ ion outside the cell in return of one Na+ ion (Aronson, 1985). This antiporter plays an essential physiological role in the regulation of cytoplasmic pH, and a change in its activity can have a drastic effect on cell metabolism and viability (Aronson, 1985). The Na+/H+ antiporter is freely reversible depending on both the Na+ and H+ gradients. However, most mammalian cells maintain an inward Na+ gradient which stimulates H+ ion efflux. This process is tightly mediated by pH and the antiporter's activity changes by more than three orders of magnitude between pH 7 and 8 (recall that pH = -log[H+]), and is totally down-regulated below pH 6.5 (Aronson, 1985).

<a id='20d38834-14e1-4e6c-8217-d7bed4ef5290'></a>

Amongst the other cellular pH transmembrane exchangers is the lactate/H⁺ symporter (also known as MCT—Monocarboxylate Transporter) (Walenta et al., 2000). This symporter works by transporting lactate and hydrogen ions together in the same direction. Depending on the gradient of each ion, this process is freely reversible with equilibrium being attained when [lactateᵢ]/[lactateₑ]=[H⁺]ₑ/[H⁺]ᵢ. There is a growing evidence suggesting that elevated tissue lactate levels are associated with a high risk of metastasis (Schwickert et al., 1995; Walenta et al., 2000) and a reduced response to radiotherapy (Quennet et al., 2006). Moreover, reports by Cardone et al. (2005) claim that the lactate/H⁺ symporter and the Na⁺/H⁺ antiporter cause tumour acidity which in turn stimulates metastasis.

<a id='8a06520d-a603-4f67-9db1-878d96b3cdb0'></a>

The contributions of mathematical modelling to the under-
standing of tumour growth and development dates back at least
60 years. Models mainly explore particular aspects of tumour
growth and dynamics such as immunotherapy (e.g. see
Bunimovich-Mendrazitsky et al., 2008), angiogenesis (e.g. see
Chaplain et al., 2006) and invasion (e.g. see Gerisch and
Chaplain, 2008; Smallbone et al., 2005). However, there are only
relatively few mathematical models that consider tumour acidity.
Amongst these are the work of Smallbone et al. (2005), Gatenby
and Gawlinski (1996), Neville (2003), Webb et al. (1999a, 1999b).
Gatenby and Gawlinski (1996) derive an acid-mediated tumour
invasion model which provides a simple mechanism linking
altered glucose metabolism with the ability of tumour cells to
form invasive cancers. The modelling of Webb et al. (1999a,
1999b) includes descriptions of intracellular and extracellular
pH and their effects on invasion. However, the various cell-
membrane transporters are represented in a rather simple fash-
ion. Moreover, they do not include lactate as a variable, but
instead include the lactate/H+ symporter as a function depending
wholly on extracellular H+ and the degree of functioning vascu-
lature. The role of sequestration of H+-ions into lysosomes is also

<a id='73a71f1b-fffa-4361-a26d-b6e9b7ba85d5'></a>

considered in Webb et al. (1999b). The modelling of Neville
(2003) considers the evolution of intracellular and extracellular
glucose as well as hydrogen ions.

<a id='2bc801b7-3478-43c1-ac5a-28a0029c1e3b'></a>

In this study, we present a new model for pH regulation that explicitly focuses on the interplay between H+-ions and lactate. We develop the mathematical model in Section 2. Numerical simulations show that the pH solutions initially change very rapidly relative to lactate. Detailed analysis of this behaviour in Section 3 shows that the initial concentration of intra and extracellular lactate play a crucial role in the sharp transient. More importantly, our model has the potential to reproduce the well-documented reversed pH gradient but unfortunately for values outside the physiological pH range (6.9-7.4)-suggesting, instead, that other cellular mechanisms may play an important role in this behaviour.

<a id='2b3e5526-af5d-4e46-93d2-6df95e798990'></a>

## 2. Model development

Our model framework is that of a single cell with two compartments—intracellular and extracellular—and we focus on the regulation of lactate and H$^+$ between these two compartments. Our model considers the temporal evolution of H$^+$ which we denote by H$\sigma$, $\sigma \in \{I,E\}$ where $I, E$ denotes intracellular and extracellular concentrations, and lactate ($L\sigma$) where $\sigma \in \{I,E\}$. We assume that the cell is growing in *in vivo* which is supported by a vascular bed. The vasculature density is represented via a parameter $V$ which we take to vary between zero and one to denote hypoxic and aerobic regions, respectively, and, in line with Webb et al. (1999a, 1999b), we assume that extracellular ions are removed from the interstitial space at a rate directly proportional to $V$. The cells studied in this model can be tumour or normal depending on parameter choices and whether $V$ is bigger or smaller than a chosen threshold degree of vasculature ($V^*$) which we use to control whether the cell undergoes glycolysis (for $V < V^*$) or aerobic metabolism (for $V > V^*$).

<a id='b97db8a0-8865-424a-b7e9-bff5e44f2c63'></a>

Our model differs from previous studies in that we explicitly include lactate. This allows a better representation of the MCT (i.e., the lactate/H+ symporter) and its role in pH regulation and, in particular, whether the action of the MCT's are able to reproduce a reversed pH gradient which is characteristic of some tumours (Griffiths, 1991). We study the model using both analytical and numerical methods in an attempt to understand the role of the various membrane-based ion transporters in tumour pH regulation. The full model equations read as follows:

<a id='fb5a4066-f3f7-4eca-a22e-c0677386c91e'></a>

$\frac{dH_I}{dt} = \underbrace{l_H(H_E-H_I)}_{H^+ \text{ leakage}} - \underbrace{f_1H(H_I-H_E)(H_I-H_E)}_{Na^+ / H^+ \text{ antiporter}} - \underbrace{k_3(H_IL_I-H_EL_E)}_{MCT}$

$+ \underbrace{\frac{2\phi_GH(V^*-V)}{H_I+b}}_{\text{Excess } H^+ \text{ via glycolysis}} + \underbrace{d_1}_{\text{Other sources of } H^+} \quad (1)$

<a id='a60c9919-09e4-455a-8bb8-9e078ea7175d'></a>

where H(.) denotes a Heaviside function,

$${\frac{dH_E}{dt} = -l_H(H_E-H_I) + f_1H(H_I-H_E)(H_I-H_E)}\tag{2}$$

$$\underbrace{\text{H}^+\text{ leakage}}_{} \underbrace{\text{Na}^+/\text{H}^+\text{ antiporter}}_{}$$

$$+ \underbrace{k_3(H_IL_I-H_EL_E)}_{\text{MCT}} - \underbrace{R_1(V)H_E}_{\text{Removal by vasculature}},$$

$${\frac{dL_I}{dt} = \frac{2\Phi_GH(V^*-V)}{H_I+b} + d_4}\tag{3}$$

$$\underbrace{\text{Production from glycolysis}}_{} \underbrace{\text{Other sources of lactate}}_{}$$

$$- \underbrace{\alpha_4L_I}_{\text{Lactate degradation}} - \underbrace{k_3(H_IL_I-H_EL_E)}_{\text{MCT}},$$

<!-- PAGE BREAK -->

<a id='edbca6c5-1c60-4db5-9eca-84c4d3a0607a'></a>

60

<a id='d722ad81-148a-41c3-9acd-ec971badbce8'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58–71

<a id='fe8a0e92-ff98-4769-82e3-ddd368b4b25d'></a>

$$\frac{d L_E}{d t} = \underbrace{k_3(H_I L_I - H_E L_E)}_{MCT} - \underbrace{R_2(V) L_E.}_{\text{Removal by vasculature}}$$ (4)

<a id='06ddd457-0919-4769-971b-8a49640dbe48'></a>

We take as initial conditions: H_I = H_I^0 mol/l, H_E = H_E^0 mol/l,
L_I = L_I^0 mol/l, L_E = L_E^0 mol/l.
We now clarify each of the model expressions in turn:

<a id='6c0e8e61-5f61-4c90-8cdc-14e99f90548b'></a>

1. Iₕ(Hₑ-Hᵢ). This term describes the rate at which H⁺ ions enter the cell due to the internally negative potential of the cell membrane. It is assumed to be directly proportional to the difference in the hydrogen ion concentration across the cell membrane. The permeability of the cell membrane to H⁺ ions is approximately 10⁻¹⁴ m/s (Lawrence, 1989). Dividing this by the typical width of the bilayer (~10 nm) (Lawrence, 1989) gives an estimation for Iₕ as 10⁻⁶ s⁻¹.
2. f₁H(Hᵢ-Hₑ)(Hᵢ-Hₑ). This term models the rate at which H⁺ ions are exported outside the cell via the Na⁺/H⁺ exchanger (NHE for short) and we assume that the rate of H⁺ efflux is directly proportional to the H⁺ gradient across the cell mem- brane, i.e. Hᵢ-Hₑ. For simplicity, we assume that the outward Na⁺ gradient is always positive. Therefore, this term is taken to be proportional to the hydrogen ion gradient only. The Heavi- side is used to prevent any H⁺ influx which is typically not observed via this transporter. The constant f₁ is a parameter which denotes the rate of H⁺ flux, and carries the units of s⁻¹.
3. k₃(HᵢLᵢ-HₑLₑ). This term represents the rate at which hydro- gen ions are extruded along with lactate ions. These ions are transported via a Monocarboxylate Transporter (MCT) located at the plasma membrane. A study by McDermott and Bonen (1993) showed that lactate transport is saturable with respect to increasing concentrations of lactate and hydrogen ions, but for simplicity we assume a linear relationship—a full deriva- tion of this term is given in Appendix A. The constant k₃ (mol⁻¹l⁻¹s) describes the rate at which hydrogen ions and lactate are exported or imported.
4. d₁. This term implicitly accounts for other sources of H⁺ ions in the cell. For example, this could include the catalysed hydration of CO₂ into H⁺ and HCO₃⁻ by Carbonic Anhydrase (Swietach et al., 2007).
5. 2ΦG H(V\*-V)/(Hᵢ+b). This term models the net production of H⁺ ions via the process of glycolysis. Glycolysis is a metabolic pathway involving a complex chain of chemical reactions that produces energy rich molecules (ATP) (Lawrence, 1989). Stu- dies by Kaminskas (1978) showed that glucose transport and consumption in cultured Ehrlich ascites-tumour cells are pH dependent. Decreasing pHᵢ is found to decrease the rate of glucose consumption (Boron, 1985; Casciari et al., 1992). In particular, the key glycolytic enzyme phosphofructokinase is found to be critically pH sensitive (Berg et al., 2003). As mentioned above, in our model, we assume a threshold degree of vasculature (V\*), above which a cell will undergo aerobic metabolism, and below which anaerobic glycolysis will pre- vail. In the presence of an oxygen supply (V > V\*), there is no net production of H⁺ ions as aerobic metabolism is shown not to produce any net H⁺-ions (Hochachka and Mommsen, 1983). However, in low oxygen concentrations (V <V\*), two H⁺-ions are produced from the dissociation of lactic acid (Hochachka and Mommsen, 1983). We assume glucose to be plentiful, which is reasonable given the observed large diffu- sion distance of glucose (Vaupel et al., 1989). The constant ΦG represents the maximal rate of glycolysis and b corresponds to the concentration of H⁺ ions needed to achieve one half of the maximum rate of glycolysis. We use the results of Casciari et al. (1992) for EMT6/R0 mouse mammary tumour cells to

<a id='82e886fe-74ea-4893-ae71-d6430d5b199b'></a>

estimate $\Phi_G$ and $b$. In this study, it is noted that glucose is consumed at a rate of $2 \times 10^{-14}$ g/cell/s at a pH of 7.2. One mol of glucose has a relative molecular mass of 180 g and one cell has a volume of roughly $10^{-15}$ m$^3$ (Lodish et al., 2008). This corresponds to a glucose consumption rate of $1.1 \times 10^{-4}$ mol/m$^3$/s. If we choose $b=10^{-7}$ mol/l then $\Phi_G = 10^{-14}$ (mol/l)$^2$/s. We assume that $b$ does not change between normal and tumour cells. However, tumours are known to have a higher glycolytic rate than normal cells and we represent this excess by an increase in $\Phi_G$.

6. $R_\sigma(V)$, $\sigma = 1,2$ for H$^+$-ions and lactate, respectively. These terms represent the rate at which hydrogen and lactate ions are removed from the interstitial space. We assume that once H$^+$ ions and lactate are extruded, they are removed linearly by the supporting vasculature, that is, $R_\sigma(V) = \rho_\sigma V$, where $\sigma = 1,2$. However, the vasculature of tumour is believed to be highly disordered and compromised (Raghunand et al., 2003; Vaupel et al., 1989), which results in uneven perfusion and a poor clearance rate. This allows us to take $V$ to be much lower in tumours than in normal tissue.

7. $d_4$. Even under aerobic conditions, there is evidence to suggest that there is some degree of lactate production (Brooks, 1986). Lactate is known to be only produced via the breakdown of pyruvate which is made from either glucose or some aminoacids (Sauer et al., 1982). Therefore, since our model assumes no production of lactate from glucose under aerobic conditions, $d_4$ may still account for a minor production from glucose. On the other hand, under anaerobic conditions, $d_4$ may account for lactate production from some aminoacids. In non-stressed or non-shocked animals, significant lactate is produced to maintain a concentration of 0.7 mM (Schumer, 1978). It has been estimated (Schumer, 1978) that lactate is produced in the resting man at the following rates (mM/h/kg): skeletal mass, 3.13; brain, 0.14; red cell mass, 0.18; and 0.11 for blood elements, renal medulla, intestinal mucosa and skin. Total lactate production in a 70-kg man is approximately 1300 mM/day (Schumer, 1978).

8. $\alpha_{4L_1}$. This term implicitly describes the rate at which lactate is converted back to pyruvate. That is, if we assume a linear conversion from pyruvate to acetyl-coA and steady state efflux conditions then one can estimate a linear relationship between pyruvate and lactate concentrations and then obtain a linear loss term for lactate, namely $\alpha_{4L_1}$. A similar approach has been adopted in Bertuzzi et al (2010). We currently have no available data to approximate this value and so we vary it in our analysis.

<a id='b3fbb721-bff8-455c-87c1-8cb10fd0197f'></a>

3. Analysis of the model

3.1. Parameter rescaling

We perform a numerical study of this system to explore the system behaviours. To facilitate this, we rescale the system according to the following rescalings: H̃_I = H_I/b, H̃_E = H_E/b, L̃_I = α_4L_I/d_4, L̃_E = α_4L_E/d_4, t̃ = α_4t, where the tildes represent rescaled variables with which the model equations become

dH̃_I / dt = l̃_H(H̃_E − H̃_I) − f̃_1H(H̃_I − H̃_E)(H̃_I − H̃_E)
− k̃_3ψ(H̃_I L̃_I − H̃_E L̃_E) + (2Φ̃_GψH(V* − V)) / (H̃_I + 1) + d̃_1, (5)

dH̃_E / dt = −l̃_H(H̃_E − H̃_I) + f̃_1H(H̃_I − H̃_E)(H̃_I − H̃_E)
+ k̃_3ψ(H̃_I L̃_I − H̃_E L̃_E) − R̃_1(V)H̃_E, (6)

<!-- PAGE BREAK -->

<a id='505df1c7-d232-434f-a5d2-fce9101470e5'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='92b04889-b360-49c6-8e0e-6b19f5f7a3ae'></a>

61

<a id='a6f4fd7a-0476-4cca-9da4-3a2297f9a10e'></a>

$$\frac{d\tilde{L}_I}{dt} = \frac{2\tilde{\Phi}_G H(\tilde{V}^* - \tilde{V})}{\tilde{H}_I + 1} + 1 - \tilde{L}_I - \tilde{k}_3 (\tilde{H}_I \tilde{L}_I - \tilde{H}_E \tilde{L}_E),$$

<a id='312e74e3-7c67-49eb-abe1-725261b8bc0e'></a>

<::dŁ_E/dt = ķ_3(Ĥ_IŁ_I - Ĥ_EŁ_E) - Ř_2(V)Ł_E::>

<a id='362e3bfb-c185-41d1-ba3b-aa22f468645d'></a>

where
$\tilde{l}_H = \frac{l_H}{\alpha_4}$, $\tilde{f}_1 = \frac{f_1}{\alpha_4}$, $\tilde{k}_3 = \frac{k_3 b}{\alpha_4}$, $\tilde{\Phi}_G = \frac{\Phi_G}{bd_4}$

<a id='0f1a57ec-9101-433d-a62d-e6fd2ef6f61d'></a>

Table 1
Dimensionless values of the model parameters.
Full details of the parameter estimation are given
in Appendix B.

<table id="3-1">
<tr><td id="3-2">Parameter</td><td id="3-3">Value</td></tr>
<tr><td id="3-4">ĩ H</td><td id="3-5">1.7174 × 10-2</td></tr>
<tr><td id="3-6">f̃ 1</td><td id="3-7">1.7174 × 104</td></tr>
<tr><td id="3-8">k̃ 3</td><td id="3-9">5.4316</td></tr>
<tr><td id="3-a">d̃ 1</td><td id="3-b">7.9996 × 103</td></tr>
<tr><td id="3-c">p̂₁</td><td id="3-d">2.0095 × 10⁴</td></tr>
<tr><td id="3-e">p̂₂</td><td id="3-f">0.2857</td></tr>
<tr><td id="3-g">φ̂G</td><td id="3-h">0.2823</td></tr>
<tr><td id="3-i">ψ</td><td id="3-j">1.4 × 10⁴</td></tr>
<tr><td id="3-k">V*</td><td id="3-l">0.5</td></tr>
</table>

<a id='1779e142-ecd6-4b5d-9283-a91d405c50d4'></a>

<::Figure a: Two line graphs. The top graph shows pH versus time. The y-axis ranges from 7 to 7.5. The x-axis ranges from 0 to 10. A solid line starts at pH 7.4 and remains constant. A dashed line starts around pH 7.3, drops rapidly to about 7.2, then gradually stabilizes around 7.2. The bottom graph shows lactate (mol/l) x 10^-3 versus time. The y-axis ranges from 1 to 1.6. The x-axis ranges from 0 to 10. A solid line starts around 1.25, increases to about 1.4, and then stabilizes. A dashed line starts around 1.25, decreases rapidly to 1.0, and then stabilizes.: chart::>

<a id='2d39ffe7-33ee-4bd1-b052-4015e08d1a09'></a>

$\tilde{d}_1 = \frac{d_1}{b\chi_4}$, $\psi = \frac{d_4}{b\chi_4}$, $\tilde{p}_1 = \frac{\rho_1}{\alpha_4}$, $\tilde{p}_2 = \frac{\rho_2}{\alpha_4}$.

We will henceforth drop the tildes for notational convenience.
Estimates for the non-dimensional parameters are given in
Appendix B and summarised in Table 1.

<a id='6af9f47a-eb4e-4203-a7c2-23e7236f24f6'></a>

3.2. Numerical solution

We construct numerical solutions to the system (5)-(8) in MATLAB using the parameter values in Table 1. Using those parameters, a linearisation of our system yields real and negative eigenvalues of varying order of magnitudes. Hence, we use a stiff multistep ODE solver, ode15s, based on backward numerical differentiation formulas. A typical solution is shown in Fig. 1, (a) for V > V* and (b) for V <V*.

Note that for the full model, we assume a resting pHᵢ = 7.2, pHₑ = 7.4, for V > V* (normoxia) and pHᵢ = 6.50, pHₑ = 6.58, for V <V* (hypoxia) (Mellergard et al., 1994; Stubbs et al., 1994). We hard-wire the final steady state solutions into this simulation, but it is interesting to note the differences in how pH and lactate attain these steady state values. We observe that the solutions of pHᵢ and pHₑ initially change very rapidly, whilst Lᵢ and Lₑ vary over a longer timescale (see Fig. 1). We use singular perturbation techniques in Section 3.4 to analyse this behaviour in more detail. Before we do this, given the uncertainty in some of the parameter estimates, we perform a parameter sensitivity analysis to identify the key rate parameters in the system.

<a id='d0889a4e-be87-4be1-9c21-2d587bd92baf'></a>

<::Figure b: Two plots are shown. The top plot displays pH versus time. The y-axis ranges from 6.2 to 7.0, labeled "pH". The x-axis ranges from 0 to 10, labeled "time". Four lines are plotted with the following legend:
- dotted line: I, simple model (section 4.2)
- dash-dot line: E, simple model
- dashed line: I, full model (equations (16)-(19))
- solid line: E, full model
The bottom plot displays lactate (mol/l) versus time. The y-axis ranges from 1.2 to 2.6 x 10^-3, labeled "lactate (mol/l)". The x-axis ranges from 0 to 10, labeled "time". Five lines are plotted, showing increasing lactate concentration over time.::>

<a id='94d4300d-b52f-4684-bfb8-1dc3ba98eebd'></a>

Fig. 1. A typical numerical solution for (a) V > V* and (b) V < V* for the full (Eqs. (5)-(8) and simplified model (Section 3.4) showing the sharp initial transient in the H+-ions solution relative to lactate. (—, extracellular, full model), (——, intracellular, full model), (......, intracellular, simple model), (–. –., extracellular, simple model). The parameter values used are shown in Table 1—we refer to this as the 'base' set of parameter values. We note from (b) that by removing the H₁ +1 factor from the glycolysis term (giving the simple model) the qualitative behaviour of the model is unchanged for the range of parameters considered.

<a id='1aa9a989-add0-4e36-9b2d-6897d75931f3'></a>

(7)

<a id='c9fb4412-dc42-408f-b1d2-edbf00e52ada'></a>

(8)

<!-- PAGE BREAK -->

<a id='bedf06f2-bfcc-4c72-bc8e-8bc569c32b9e'></a>

62

<a id='baedb285-90b7-47a0-8f07-4ebf9f66363b'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='8d7449ce-ad75-4e7d-9830-821a197ef957'></a>

<::transcription of the content: figure::>
Fig. 2. Sensitivity analysis of the full model. For each parameter, the percentage change in its value from the base case is plotted on the x-axis, and the corresponding percentage change in the steady state solution is plotted on the y-axis. We only show the results for V < V* as they are qualitatively similar to V > V*.

The figure displays a grid of 24 bar charts, arranged in 6 rows and 4 columns, illustrating the sensitivity analysis for various parameters and their impact on different steady-state solutions. Each column represents a different solution output, and each row represents a different input parameter being varied.

The x-axis for all 24 charts is labeled "% change in parameter", ranging from -50 to 100.

**Row 1: Parameter `f_1`**
- **Column 1 (a)**: Y-axis range approximately -8 to 0. Bars show a negative correlation, increasing from -8 to 0 as `f_1` changes from -50 to 100.
- **Column 2 (b)**: Y-axis range approximately 0 to 100. Bars show a strong positive value at -50% change in `f_1`, rapidly decreasing towards 0 as `f_1` changes to 100%.
- **Column 3 (c)**: Y-axis range approximately 0 to 100. Similar to (b), with a high positive value at -50% change in `f_1`, decreasing towards 0.
- **Column 4 (d)**: Y-axis range approximately 0 to 10. Bars show a negative correlation, starting around 10 and decreasing to 0 as `f_1` changes from -50 to 100.

**Row 2: Parameter `k_3`**
- **Column 1**: Y-axis range approximately -8 to 0 (scaled by 10^-3). Bars show a negative correlation, increasing from -8 to 0 as `k_3` changes from -50 to 100.
- **Column 2**: Y-axis range approximately 0 to 0.05. Bars show a strong positive value at -50% change in `k_3`, rapidly decreasing towards 0 as `k_3` changes to 100%.
- **Column 3**: Y-axis range approximately -3 to 0. Bars show a negative correlation, increasing from -3 to 0 as `k_3` changes from -50 to 100.
- **Column 4**: Y-axis range approximately 0 to 0.2. Bars show a strong positive value at -50% change in `k_3`, rapidly decreasing towards 0 as `k_3` changes to 100%.

**Row 3: Parameter `ρ_1`**
- **Column 1**: Y-axis labeled "% change in H_E solution", range approximately 0 to 600. Bars show a strong positive value at -50% change in `ρ_1`, rapidly decreasing towards 0 as `ρ_1` changes to 100%.
- **Column 2**: Y-axis labeled "% change in H_I solution", range approximately 0 to 600. Bars show a strong positive value at -50% change in `ρ_1`, rapidly decreasing towards 0 as `ρ_1` changes to 100%.
- **Column 3**: Y-axis labeled "% change in L_E solution", range approximately -20 to 20. Bars show a positive correlation, increasing from -20 to 20 as `ρ_1` changes from -50 to 100.
- **Column 4**: Y-axis labeled "% change in L_I solution", range approximately -8 to 2. Bars show a positive correlation, increasing from -8 to 2 as `ρ_1` changes from -50 to 100.

**Row 4: Parameter `ρ_2`**
- **Column 1**: Y-axis labeled "% change", range approximately -0.2 to 0.2. Bars show a positive correlation, increasing from -0.2 to 0.2 as `ρ_2` changes from -50 to 100.
- **Column 2**: Y-axis labeled "% change", range approximately -1 to 1. Bars show a positive correlation, increasing from -1 to 1 as `ρ_2` changes from -50 to 100.
- **Column 3**: Y-axis labeled "% change", range approximately -5 to 5. Bars show a positive correlation, increasing from -5 to 5 as `ρ_2` changes from -50 to 100.
- **Column 4**: Y-axis labeled "% change", range approximately -5 to 5. Bars show a positive correlation, increasing from -5 to 5 as `ρ_2` changes from -50 to 100.

**Row 5: Parameter `d_1`**
- **Column 1**: Y-axis range approximately -50 to 50. Bars show a positive correlation, increasing from -50 to 50 as `d_1` changes from -50 to 100.
- **Column 2**: Y-axis range approximately -50 to 50. Bars show a positive correlation, increasing from -50 to 50 as `d_1` changes from -50 to 100.
- **Column 3**: Y-axis range approximately -2 to 6. Bars show a negative correlation, decreasing from 6 to -2 as `d_1` changes from -50 to 100.
- **Column 4**: Y-axis range approximately -4 to 8. Bars show a negative correlation, decreasing from 8 to -4 as `d_1` changes from -50 to 100.

**Row 6: Parameter `V`**
- **Column 1**: Y-axis range approximately 0 to 600. Bars show a strong positive value at -50% change in `V`, rapidly decreasing towards 0 as `V` changes to 100%.
- **Column 2**: Y-axis range approximately 0 to 600. Bars show a strong positive value at -50% change in `V`, rapidly decreasing towards 0 as `V` changes to 100%.
- **Column 3**: Y-axis range approximately -15 to 5. Bars show a positive correlation, increasing from -15 to 5 as `V` changes from -50 to 100.
- **Column 4**: Y-axis range approximately -4 to 0. Bars show a curve, starting around -1 at -50%, decreasing to -4 around 0% change, and then increasing back to -1 at 100% change in `V`.
<::/transcription of the content: figure::>

<a id='bc91e92b-266f-4a9b-bc29-3faebd722573'></a>

3.3. _Sensitivity analysis_
In this section, we vary individual parameters in turn and note their effects on the steady state solutions of the model.

<a id='ef9c270a-96e4-4ca5-979e-628fe9c77bb9'></a>

We illustrate the sensitivity of the model behaviour for the V < V*
case in Fig. 2 as a percentage change in each of the chosen
parameter values from their base value. The parameters that we

<!-- PAGE BREAK -->

<a id='63c5e7b6-95a0-43e5-ae31-080b24280f35'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='5dedf08e-77e1-4af2-9b47-38772cf0c08e'></a>

63

<a id='bd8a946c-6605-4ef1-af2f-3590d641ba0f'></a>

<::chart: The image displays Figure 3, titled "Inner solution for the normoxic case in terms of increasing order of ε." It consists of four line plots arranged in a 2x2 grid, comparing numerical solutions with analytic approximations obtained via perturbation analysis for various orders of ε. All x-axes are labeled "time" and scaled by "x 10^-4".The top-left plot shows HT versus time. The y-axis ranges from 0.8 to 2.0. It displays six curves: "numerical" (solid line), "up to O(ε)" (circles), "up to O(ε^2)" (triangles), "up to O(ε^3)" (dashed line), "up to O(ε^4)" (dash-dotted line), and "up to O(ε^5)" (dotted line). All curves show a general decrease over time, with higher-order approximations tracking the numerical solution more closely.The top-right plot shows HD versus time. The y-axis ranges from 0 to 0.18. It displays the same six types of curves as the top-left plot. The curves generally increase rapidly and then flatten out, with the numerical solution and higher-order approximations converging to a stable value around 0.16.The bottom-left plot shows LT versus time. The y-axis ranges from 1.8 to 1.8. It displays three curves: "numerical" (solid line), "up to O(ε^4)" (circles), and "up to O(ε^6)" (triangles). The "up to O(ε^4)" curve shows a slight increase, while the "up to O(ε^6)" curve shows a slight decrease. An inset magnifies a section of the plot, showing values around 1.8.The bottom-right plot shows LD versus time. The y-axis ranges from -16 to 2 x 10^-5. It displays six curves: "numerical" (solid line), "up to O(ε)" (circles), "up to O(ε^3)" (triangles), "up to O(ε^5)" (dashed line), "up to O(ε^7)" (dash-dotted line), and "up to O(ε^8)" (dotted line). The curves generally show a decrease over time, becoming more negative. An inset magnifies a section of the plot, showing values around -7.2 x 10^-5.Fig. 3. Inner solution for the normoxic case in terms of increasing order of ε. Using perturbation analysis, we obtain an analytic approximation (shown in Eqs. (C1)–(C19)) to the solution of the simpler system and compare them with the numerical solution. These solutions capture the interesting sharp transition in the pH solution that is observed in the full model for t ∈ [0, ε⁴], where here we take ε = 0.1.::>

<a id='ef214ebf-d52d-46c4-9a4a-4f9e3eaf4a1a'></a>

illustrate are those that show the most variation in the solutions—these are, f₁,k₃,ρ₁,ρ₂,d₁ and V, which, respectively, represent the rate of activity of the NHE; and that of MCT; the rate of removal of H⁺-ions; and that of lactate; background produc- tion of H⁺-ions; and finally the degree of vasculature. The sensitivity of the model behaviour for the V > V* is qualitatively similar to that shown in Fig. 2, except that Hₑ* is insensitive to any parameter variations except for d₁, ρ₁ and V. Also, variations in d₁, ρ₁ and V result in qualitatively different lactate behaviour for the V≤V* cases. More specifically, increasing ρ₁ above its 'base' value (see Table 1) results in low steady state levels of intracellular lactate under normoxic conditions, whilst a high value of intra- cellular lactate is attained under hypoxia. This means that a purely glycolytic tumour will still have high levels of intracellular lactate despite increased H⁺-ions removal rate. Numerical simu- lations indicate that increasing H⁺-ions removal rate under hypoxic conditions results in a high NHE activity, which leaves less intracellular H⁺-ions to bind with lactate for extrusion via the MCT. Moreover, increasing d₁ results in a large Lₑ* under normoxic conditions, whilst the opposite is true under hypoxic conditions. This implies that the MCT extrudes H⁺ ions (along with lactate) more rapidly under normoxic conditions compared to hypoxic. Our sensitivity analysis also predicts that increasing the blood perfusion for an already highly glycolytic tumour, whilst keeping perfusion below the hypoxic threshold, results in low intra and extracellular H⁺-ions and intracellular lactate, but

<a id='3ef56a3f-b433-4166-8c41-f576dd6d057c'></a>

an unexpectedly high extracellular lactate levels. This is because
as extracellular H+-ions and lactate are cleared, intracellular
lactate and H+-ions continue to be produced glycolytically, and
hence the activity of the MCT becomes much higher which gives
rise to the observed higher extracellular lactate. Given the
similarity between the V≤V* cases, we only show the V < V*
case for brevity.

<a id='875ec248-ac4b-4bdd-b159-20c7379b55e0'></a>

## 3.4. Singular perturbation analysis of a simplified model

We note from the numerical simulations in Fig. 1 that there is an initial sharp transient in the pH solution profile relative to the slower change in the lactate solutions. We now analyse this behaviour in more detail. To facilitate the analysis, we remove the factor 1/(H_I+1) from the glycolysis term. We note that by doing so the qualitative behaviour of the solutions is not affected for the range of parameters considered (compare dotted and dash-dotted solutions in Fig. 1(b)). Also, it turns out to be more convenient to work with the following variables for total H$^+$ and lactate and the difference between intracellular and extracellular concentrations, namely: H_T = H_I + H_E, L_T = L_I + L_E, H_D = H_I - H_E, L_D = L_I - L_E. The model contains a number of large and small parameters (see Table 1) and we exploit this by introducing a small parameter $\epsilon \ll 1$ and rescale the parameters as follows
$\hat{l}_H = \hat{l}_H\epsilon^2$, $f_1 = \hat{f}_1/\epsilon^4$, $\psi = \hat{\psi}/\epsilon^4$, $\Phi_G = \hat{\Phi}_G\epsilon$, $d_1 = \hat{d}_1/\epsilon^3$, $\rho_1 = \hat{\rho}_1/\epsilon^4$, $\rho_2 = \hat{\rho}_2\epsilon$, $V = \hat{V}\epsilon$, where the parameters represented by 'hats' are

<!-- PAGE BREAK -->

<a id='3fe8daa2-fcee-429d-b5df-92e4987c3bfc'></a>

64

<a id='df1d9d85-acba-4d04-8cdf-38e2997bf771'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='8dffefb6-ce53-466a-9946-c3c66504fa79'></a>

all of $O(1)$ and $\epsilon = 0.1$. Upon substitution into (5)–(8), and representing the equations in terms of $H_T, H_D, L_T$ and $L_D$ we obtain

$\epsilon^3 \frac{dH_T}{dt} = 2\hat{\Phi}_G \psi H(\hat{V}^* - \hat{V}) + \hat{d}_1 - \frac{\hat{\rho}_1 \hat{V}}{2}(H_T - H_D)$, (9)

$\epsilon^4 \frac{dH_D}{dt} = 2\hat{\Phi}_G \psi \epsilon H(\hat{V}^* - \hat{V}) + \hat{d}_1 \epsilon + \frac{\hat{\rho}_1 \hat{V}}{2}\epsilon(H_T - H_D) - 2H_D(\hat{I}_H \epsilon^6 + f_1) - k_3 \psi (H_T L_D + H_D L_T)$, (10)

<a id='af47af08-97bc-4b9f-a58f-9db8193adc03'></a>

dLT/dt = 2Φ̂_GεH(V̂*-V̂) + 1 - 1/2(LT+LD) - ρ̂₂V̂/2 ε²(LT-LD), (11)
dLD/dt = 2Φ̂_GεH(V̂*-V̂) + 1 - 1/2(LT+LD) + ρ̂₂V̂/2 ε²(LT-LD)
-k₃(HTLD + HDLT). (12)

<a id='98d67626-94ae-483f-9d1b-c39c81220347'></a>

The problem is clearly singular since the small parameter _ε_ multiplies the derivative terms in the _H_<sub>T</sub> and _H_<sub>D</sub> equations. This means that the dependent variables, _H_<sub>T</sub> and _H_<sub>D</sub>, undergo rapid changes over very small timescale (as we indeed observe in Fig. 1). These rapid changes cannot be handled by slow time scales, but can be tackled using a stretched time scale. Specifically, we look for solutions in the form of an asymptotic expansion such as

_u_<sub>_σ_</sub>(_t_; _ε_) = _u_<sub>_σ_</sub><sup>0</sup>(_t_) + _εu_<sub>_σ_</sub><sup>1</sup>(_t_) + _ε_<sup>2</sup>_u_<sub>_σ_</sub><sup>2</sup>(_t_) + _ε_<sup>3</sup>_u_<sub>_σ_</sub><sup>3</sup>(_t_) + ..., (13)

<a id='dc4a3f66-fedb-40b4-b3f2-bba3a88129a4'></a>

where _u_=_H_, _L_ and _σ_ =_T_,_D_ and we first rescale time using _t_ = _e_<sup>_α_</sup>_t_,
_α_ > 0. See Appendix C for details on the inner solution.

<a id='9d384be8-8bf8-4ff6-ba50-432cfd3b5fa2'></a>

3.4.1. Outer solution
Putting $\epsilon = 0$ in Eqs. (9)-(12) yields the following set of differential algebraic equations:

$2\hat{\Phi}_G\hat{\psi} + \hat{d}_1 - \frac{\hat{\rho}_1\hat{V}(H_T^0 - H_D^0)}{2} = 0$, (14)

$-2\hat{f}_1 H_D^0 - k_3\hat{\psi} (H_T^0 L_D^0 + H_D^0 L_T^0) = 0$, (15)

$\frac{dL_T^0}{dt} = 1 - \frac{(L_T^0 + L_D^0)}{2}$, (16)

$\frac{dL_D^0}{dt} = 1 - \frac{(L_T^0 + L_D^0)}{2} - k_3(H_T^0 L_D^0 + H_D^0 L_T^0)$. (17)

Eliminating $H_T^0$ from Eqs. (14) and (15) gives

$H_D^0 = \frac{-2k_3\hat{\psi} L_D^0 (2\hat{\Phi}_G\hat{\psi} + \hat{d}_1)}{\hat{\rho}_1\hat{V}(2\hat{f}_1 + k_3\hat{\psi}(L_T^0 + L_D^0))}$ (18)

Noting that $(L_T^0 + L_D^0) = 2L_T^0 > 0$ in (18) we notice that, to leading order,

<a id='793c53a2-97b9-419b-8e8d-1bd7986e94a3'></a>

1. H₀ᴴ > 0 if L₀ᴴ < 0, i.e. we have H₀ᴹ < H₀₁ if L₀₁ < L₀ᴹ.
2. H₀ᴴ < 0 if L₀ᴴ > 0, i.e. we have H₀ᴹ > H₀₁ if L₀₁ > L₀ᴹ.

<a id='ea5e1eb2-7aeb-4fc3-aaa0-76f03049af7e'></a>

<::Line chart with an inset. The y-axis is labeled H_T and ranges from 1.8 to 3.2. The x-axis is labeled time and ranges from 0 to 1, multiplied by 10^-4. The legend shows three lines: "numerical" (solid line), "up to O(ε)" (line with circles), and "up to O(ε²)" (line with triangles). An inset magnifies a section of the chart, showing values 2.894, 2.892, and 2.89, with an H label to the right, indicating a closer look at the convergence of the lines.: chart::>

<a id='80f85b2e-b9be-4509-a3d7-e30505b1b7e6'></a>

<::A line graph titled 'D' on the y-axis and 'time x 10^-4' on the x-axis. The y-axis ranges from 0 to 0.14, and the x-axis ranges from 0 to 1. Three lines are plotted: 'numerical' (solid line), 'up to O(ε)' (line with circles), and 'up to O(ε²)' (line with triangles). The graph shows all three lines starting at 0, rapidly increasing, and then leveling off. An inset magnifies a section of the graph around x = 0.8 and y between 0.124 and 0.126, showing the 'up to O(ε²)' line slightly above the 'numerical' line, which is slightly above the 'up to O(ε)' line.::>

<a id='258766d2-dfc8-4f96-b643-b292558857b2'></a>

<::chart: A line chart showing 'L_T' on the y-axis and 'time x 10^-4' on the x-axis. The y-axis ranges from approximately 1.8 to 1.8001. The x-axis ranges from 0 to 1. The chart displays four series: 'numerical' (solid line), 'up to O(ε^4)' (line with circle markers), 'up to O(ε^5)' (line with triangle markers), and 'up to O(ε^6)' (dashed line). The 'up to O(ε^4)' series shows a gradual increase, while the other three series show a steeper, nearly linear increase, staying very close to each other. An inset box magnifies a section of the graph, highlighting two closely spaced lines (solid and dashed) around the y-value of 1.8.::>Fig. 4. Same caption to Fig. 3 but, here, v

<a id='058ba1e0-8e76-4d74-9120-022bee817fbb'></a>

<::line chart::>  The chart shows data points plotted against time. The y-axis ranges from -5 to 1, with values scaled by 10⁻⁵. The x-axis is labeled "time" and ranges from 0 to 1, with values scaled by 10⁻⁴.  There are four data series:  - "numerical" (represented by a solid line)  - "up to O(ε⁴)" (represented by a line with circles)  - "up to O(ε⁵)" (represented by a line with triangles)  - "up to O(ε⁶)" (represented by a dashed-dotted line)  The series "numerical", "up to O(ε⁵)", and "up to O(ε⁶)" largely overlap, showing a decreasing trend from 0 to approximately -4 x 10⁻⁵. The series "up to O(ε⁴)" shows an increasing trend from 0 to approximately 1 x 10⁻⁵.  An inset box magnifies a section of the graph, showing the numerical and up to O(ε⁶) lines, with y-axis labels -1.86 and -1.88, also scaled by 10⁻⁵.  <::/line chart::>  how the hypoxic case (V < V*).

<!-- PAGE BREAK -->

<a id='1fcabbb2-be4a-447e-a54e-1a1bd7e499d9'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='d7726866-27f1-400d-b071-173f3456060c'></a>

65

<a id='187b8c60-95b1-44d5-983b-3d91d923b79b'></a>

<::chart: Fig. 5. This figure presents two plots, (a) and (b), illustrating the effect of increasing the dimensionless initial concentration of intracellular lactate, Lᵢ⁰, on intracellular H⁺-ions and pH under hypoxic conditions. The initial extracellular lactate concentration, Lₑ⁰, is 0.9. The simulation shows results for Lᵢ⁰ increasing from 0.9 (solid black line) to 80 (solid circled line), with intermediate values represented by dotted and dashed lines. An arrow labeled "increasing Lᵢ⁰" indicates the trend. Insets show shallower profiles when Lᵢ⁰ as well as Lₑ⁰ are increased. Plot (a) shows the intracellular H⁺-ions profile (Hᵢ) over time. The y-axis ranges from 0 to 7, and the x-axis (time) ranges from 0 to 10. For Lᵢ⁰ = 0.9 (solid black line), Hᵢ starts at approximately 0.5, rises to about 4.7, and then stabilizes around 4.8. As Lᵢ⁰ increases, the curves show a steeper rise to higher peaks and then a gradual decrease, with the Lᵢ⁰ = 80 (solid circled line) peaking at over 6. The inset for plot (a) is titled "Lᵢ⁰=800 Lₑ⁰=200" and shows Hᵢ on the y-axis (0 to 30) against time on the x-axis (0 to 10). The curve in the inset rises to a peak around time 5 and then declines. Plot (b) shows the corresponding intracellular pH (pHᵢ) over time. The y-axis ranges from 6.2 to 8.2, and the x-axis (time) ranges from 0 to 10. For Lᵢ⁰ = 0.9 (solid black line), pHᵢ starts at approximately 6.3, decreases slightly, and then stabilizes around 6.3. As Lᵢ⁰ increases, the curves show a sharper drop to lower pH values, followed by a gradual increase, with the Lᵢ⁰ = 80 (solid circled line) starting around 8, dropping to a minimum below 6.2, and then stabilizing around 6.2. The inset for plot (b) is titled "Lᵢ⁰=800 Lₑ⁰=200" and shows pHᵢ on the y-axis (5.5 to 7) against time on the x-axis (0 to 10). The curve in the inset decreases to a minimum around time 5 and then increases.::>

<a id='7400692b-981d-4026-b5c7-b367010a03c4'></a>

Although this conclusion is to leading order, experiments carried out by Stubbs et al. (1994) to determine whether lactate distribution across the cell membrane reflect the transmembrane pH in Hepatoma 9618a found that: pHᵢ = 7.10 > pHₑ = 6.79 and Lᵢ = 8.36 mM > Lₑ = 3.39 mM, which is in line with our prediction that Hₑ⁰ > Hᵢ⁰ if Lᵢ⁰ > Lₑ⁰. We find later in this section that where a reversed pH gradient is attained, the steady state levels of intracellular lactate are always higher than the extracellular (see Fig. 7).

<a id='83942acd-3e02-463c-a792-aab5fa7e7454'></a>

The outer solutions evolve to the steady state solution which,
in terms of the simple non-dimensional model, are

<a id='4da0dd90-42bb-4ebc-a79d-7fa38f1a971b'></a>

$$H_E^* = \begin{cases} \frac{d_1}{\rho_1 V'}, & V > V^* \\ \frac{d_1 + 2\Phi_G \psi}{\rho_1 V}, & V < V^* \end{cases} \quad (19)$$

<a id='f05a61b3-1d1d-48bd-9215-ac8ced5efcc4'></a>

We note that, compared with the full model solution in Section
3.2, H*E here does not depend on H*i for the V < V* case. We also
have, from (14)-(17)

<a id='b5aa4540-318b-4b33-9f12-917728302f69'></a>

$$L_i^* = \begin{cases}1 - \rho_2 VL_E^*, & V > V^* \\2\Phi_G + 1 - \rho_2 VL_E^*, & V < V^*\end{cases}\quad (20)$$

<a id='d75931f9-502c-4b4a-8aec-86e438d5e282'></a>

and

L*_E = {
k_3 ρ_1 V H*_i / (k_3 ρ_1 ρ_2 V^2 H*_i + d_1 k_3 + ρ_1 ρ_2 V^2),       V > V*,
k_3 ρ_1 V (1 + 2 Φ_G) H*_i / (ρ_1 ρ_2 V^2 k_3 H*_i + 2 k_3 Φ_G ψ + d_1 k_3 + ρ_1 ρ_2 V^2),       V < V*.
}
(21)

Finally, substituting (19)-(21) into (6) yields a lengthy expression for H*_i in terms of the model parameters. We show the variation of this H*_i solution in Fig. 6, for variations in (a) (f_1,V) and (b) (k_3,V); and in Fig. 7, (a) (d_1, Φ_G) and (b) (d_1,k_3).

<a id='31b6c9b4-b6b7-4e0e-8940-f5ebdbc19a96'></a>

Fig. 6 clearly shows that across a range of *f₁*,*k₃* and *V* values, with better vascularisation, a tumour will have a higher pHᵢ and pHₑ and lower lactateᵢ and lactateₑ levels. This is supported by studies carried out by Gillies et al. (1994) and Tozer et al. (1990) which shows that the intracellular pH of tumours depends on blood flow and an acute decline in blood flow results in a significant reduction in pHᵢ (Tozer et al., 1990). Fig. 6(a) further indicates that an increase in *f₁* raises pHᵢ because more *Hᵢ*'s are extruded. As a result, less intracellular hydrogen ions are available to bind with intracellular lactate for MCT to function and, hence, we observe that intracellular lactate builds up and extracellular lactate decreases. This observation is more apparent in the hypoxic case (*V* < *V*\*). There seems to be no effect on pHₑ with increasing *f₁*, which is not surprising. In Fig. 6(b), we see that varying *k₃* has little effect on pHᵢ, pHₑ and *Lᵢ* but a more significant effect on *Lₑ*\*, which is more apparent in the *V* > *V*\* region. Numerical simulations showing the activity of the NHEs and MCTs indicate that increasing *k₃* results in a lower H⁺-ion gradient and a lower MCT activity (the extent of the decrease is very small in the hypoxic case).

<a id='f0fc6e0a-dd34-4a4e-affc-6b446973af46'></a>

We show in Fig. 7(a) the effect of varying ΦG (rate of glycolysis) and d₁ (background production of H⁺-ions) on the steady state solution of pH and lactate under hypoxic conditions. The pH gradient is reversed for relatively small ΦG and d₁ which we find, from our numerical simulations, to be due to the increased activity of the MCTs. This is because a low source of intracellular H⁺-ions and rate of glycolysis directly impacts the NHEs by lowering its activity. Clearly, the reversed pH gradient is above pH 8—outside the physiologically reasonable range. Fig. 7(b) shows the effect of varying k₃ (rate of MCT activity) and d₁ (background production of H⁺-ions) on the steady state solution of pH and lactate under normoxic conditions. Note that varying k₃ and d₁ under hypoxic conditions does not result in a negative pH gradient (not shown). This is because our model predicts that the impact of the MCT on the regulation of pHᵢ is small in hypoxic regions compared to normoxic (in line with findings by Webb et al., 1999b). Fig. 7 predicts that decreasing d₁ shifts the steady state solution of Hᵢ into the region where Hₑ* > Hᵢ*. This appears to be due to the increased activity of the MCTs which is evident from the decreased Lᵢ* and increased Lₑ*. Biologically, this implies that lowering sources of intracellular H⁺-ions other than those resulting from glycolysis can give rise to highly alkaline reversed pH gradient. For example, lowering the Carbonic Anhydrase (CA) catalysed hydration of CO₂ into HCO₃⁻ and H⁺-ions can enhance the efficacy of chemotherapeutics by alkalising the intra and extracellular pH. This is supported by an in vitro study by Parkkila et al. (2000) which found that a potent CA inhibitor suppresses the relative invasion rate of renal carcinoma cell lines by 18–74%.

<!-- PAGE BREAK -->

<a id='69eac06d-0289-49ad-a81d-169089e8ba3f'></a>

66

<a id='ea9c7c24-f962-4813-bba7-f3478aaa2ed3'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='a817ef8b-cbfc-4c7a-a175-87bbd39d4995'></a>

<::figure: contour plots::>Fig. 6. We illustrate the effect of varying key parameters (a) f₁ (NHE rate activity) versus V (vasculature); and (b) k₃ (MCT rate activity) versus V on the steady state solution of pH and lactate. In both simulations, vasculature spans from poorly formed blood vessels (V < V* = 0.5) to very efficient ones (V > V* = 0.5). The figure is composed of two main panels, (a) and (b), each containing four contour plots. (a) This panel shows the effect of varying f₁ (NHE rate activity) and V (vasculature). The y-axis for all subplots in this panel is f₁ (x 10⁴) and the x-axis is V. The four subplots are: 1. A contour plot for pHᵢ with contour lines labeled 6.0, 6.4, 6.6, 6.8, 7.0, 7.2. 2. A contour plot for pHₑ with contour lines labeled 5.8, 6.2, 6.4, 6.6, 6.8, 7.2, 7.3. 3. A contour plot for Lᵢ with contour lines labeled 0.001, 0.0011, 0.0018, 0.002, 0.0021. 4. A contour plot for Lₑ with contour lines labeled 0.0013, 0.0015, 0.0017, 0.0024, 0.0025, 0.005. (b) This panel shows the effect of varying k₃ (MCT rate activity) and V (vasculature). The y-axis for all subplots in this panel is k₃ and the x-axis is V. The four subplots are: 1. A contour plot for pHᵢ with contour lines labeled 5.9, 6.1, 6.3, 6.5, 6.9, 7.1, 7.2. 2. A contour plot for pHₑ with contour lines labeled 5.8, 6.2, 6.4, 6.6, 6.8, 7.2, 7.3. 3. A contour plot for Lᵢ with contour lines labeled 0.001, 0.0011, 0.0012, 0.0018, 0.002, 0.0021. 4. A contour plot for Lₑ with contour lines labeled 0.001, 0.0013, 0.0015, 0.0024, 0.0025.<::>

<a id='09012c47-e0db-493b-be0a-cf5c0d02c7c0'></a>

## 4. Discussion

Some tumours are reported to have an acidic extracellular environment, which is often thought to give them a greater survival advantage (Gatenby et al., 2007). It is believed that this is caused by elevated glycolysis which results in the up-regulation of certain cellular transporters. In this paper, we have described a mathematical model that focuses on the interplay between H⁺-

<a id='598f669e-1e6e-4928-8929-16ac5e59c5c9'></a>

ions and lactate in tumours. The main differences between normal and tumour cells in the model are: tumour cells rely heavily on the inefficient glycolytic pathway for energy produc- tion and also their clearance rate of extracellular ions is assumed to be poor. Analysis of the model shows that tumour cells have higher levels of lactate and lower pH, which is in line with experimental observations (Gatenby et al., 2007). Further analysis of the steady state solutions shows that, the more vascularised

<!-- PAGE BREAK -->

<a id='27fb8313-17fa-447b-acdd-7519fed7349e'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='c29dad74-40d2-4801-85a0-493c915459d9'></a>

67

<a id='f58ffbb2-c04b-4c2c-bf5d-c042c47e035d'></a>

<::figure: contour plot::>Fig. 7. (a) This panel displays four contour plots showing the effect of varying φG (rate of glycolysis) on the x-axis (from 10^-2 to 10^1) and d₁ (background production of H⁺-ions) on the y-axis (from 10^2 to 10^4) on the steady state solution of pH and lactate under hypoxic conditions. The regions below the black thick line represent a reversed pH gradient, while above is otherwise. Values for the 'base' case parameter set are represented by a black filled circle.

Top left: Contour plot of intracellular pH (pH_i). Contour lines are labeled 6.4, 6.8, 7.2, 7.4, 8.0. The black filled circle is at pH_i 6.4.
Top right: Contour plot of extracellular pH (pH_e). Contour lines are labeled 6.4, 6.8, 7.2. The black filled circle is at pH_e 6.4.
Bottom left: Contour plot of intracellular lactate (L_i). Contour lines are labeled 0.0013, 0.0014, 0.0016, 0.0018, 0.0022. The black filled circle is at L_i 0.0022.
Bottom right: Contour plot of extracellular lactate (L_e). Contour lines are labeled 0.0017, 0.002, 0.0028. The black filled circle is at L_e 0.0028.

(b) This panel displays four contour plots showing the effect of varying k₃ (rate of MCT activity) on the x-axis (from 10^-2 to 10^1) and d₁ (background production of H⁺-ions) on the y-axis (from 10^2 to 10^4) on the steady state solution of pH and lactate under normoxic conditions. The black filled circle represents the 'base' case parameter set.

Top left: Contour plot of intracellular pH (pH_i). Contour lines are labeled 7.1, 7.5, 7.9, 8.3, 8.7, 9.1, 9.5. The black filled circle is at pH_i 7.1.
Top right: Contour plot of extracellular pH (pH_e). Contour lines are labeled 7.5, 7.9, 8.3, 8.7. The black filled circle is at pH_e 7.5.
Bottom left: Contour plot of intracellular lactate (L_i). Contour lines are labeled 0.001, 0.0011, 0.0012, 0.0013, 0.00135, 0.00139. The black filled circle is at L_i 0.001.
Bottom right: Contour plot of extracellular lactate (L_e). Contour lines are labeled 5.3e-5, 3.5e-4, 6.4e-4, 9.3e-4, 1.3e-3, 1.5e-3. The black filled circle is at L_e 1.5e-3.

Regions below the black thick line represent a reversed pH gradient whilst above is otherwise. Values of pH and lactate for the 'base' case parameter set are represented by a black filled circle. Clearly the reversed pH gradient is above pH 8—outside the physiologically reasonable range. Note that varying k₃ and d₁ does not result in a negative pH gradient under hypoxic conditions.<::figure::>

<a id='c035f093-4eae-4479-9c64-f664434ffd89'></a>

the cell, the higher the intra and extracellular pH and the lower
the lactate levels. This is supported by studies carried out by
Gillies et al. (1994) and Tozer et al. (1990) which shows that
the intracellular pH of tumours depend on blood flow and
an acute decline in blood flow results in a significant reduction
in pH, (Tozer et al., 1990). Our analysis also shows that

<a id='6bbd13af-1032-4df2-8c6d-1de2548a42f6'></a>

decreasing the quantity of hydrogen ions produced from sources other than metabolism can cause the pH cellular gradient to be reversed.

<a id='c713d3e9-e7e1-4d14-850d-064cbcc555b8'></a>

Numerical simulations show that, after an initial transient, the
intra and extracellular pH sharply attain their steady state value.
To study this behaviour in more detail, we have considered a

<!-- PAGE BREAK -->

<a id='649393df-df49-4c1c-b3d4-63b129e3e9ea'></a>

68

<a id='f7071a42-7b9a-4f94-b1f7-6af20a6baa46'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='b79efbb7-1d4e-4496-bff5-ea83aaa1c1cf'></a>

simplified model, in which we neglect the inhibitory effect of low intracellular pH on glycolysis. Investigation of this model using singular perturbation analysis has given considerable insight into the behaviour of the solution, and has provided a good analytical approximation to the solutions of the system. These solutions compare very well with the numerical simulations, and capture the interesting transition in the pH solution that is observed in the full model. We find that the initial concentrations of intra and extracellular lactate play a key role in this sharp transient. Numerical simulations show that a high initial value of intracellular lactate results in a sharp increase in the activity of the MCTs which gives rise to a transiently reversed pH gradient and as a result a suspended NHE activity. This seems to explain the shallow profile obtained when the initial concentration of intracellular lactate is increased, which is more shallow when the extracellular is also increased. Therefore, we conclude that the activity of the Na+/H+ exchanger plays a key role in the sharp initial transient in the pH solution relative to lactate.

<a id='f526c597-1c1e-4566-8cfd-5097d3883813'></a>

We then move on to examine the effect of varying multiple parameters on the model solutions. We show that the lactate/H+ symporter is less active under hypoxic conditions than aerobic and that the Na+/H+ antiporter is more active under hypoxic conditions than aerobic. It would be interesting to validate this experimentally. Analysis of the model shows that, with the inclusion of lactate explicitly in the model, a reversed pH gradient is attainable under aerobic conditions when other sources of hydrogen ions are decreased and MCT activity is increased-but we find the pH conditions that this reversed gradient is found to be too alkaline to be viable and therefore is unrealistic. This indicates that another mechanism could be contributing to support a physiologically reasonable reversed pH gradient and we suggest, in agreement with Neville (2003) and Webb et al. (1999b) that the transfer of H+ ions into acidic vesicles such as lysosomes, could be the major contributor to the reversed pH gradient seen in some tumours, although investigating this effect is subject to our future work. Nevertheless, a recent study by Colen et al. (2011) indicates that glioma invasion is markedly impaired when lactate efflux is inhibited. More specifically, it was found to cause complete necrosis in some cases. A more recent study by Sonveaux et al. (2012) shows that blocking lactate influx through MCT1 can lead to anti-angiogenic and anti-metabolic effects. Our study suggests that, for some values of background production of H+-ions, decreasing the MCT activity will diminish the reversed pH gradient which is known to be implicated in tumour invasiveness (Webb et al., 2011).

<a id='8dfc9f36-dbc6-4604-b836-d4dd3352b430'></a>

One of the most well studied proton pumps is the V-ATPase
that is involved in pumping protons into the extracellular environment or into intracellular vesicles. The highly acidic organelles
may then be released into the extracellular space where they are
thought to activate various proteolytic enzymes involved in
invasion and metastasis (Webb et al., 1999a). A possible extension
of this work would be to account for such acidic vesicles in the
model and also incorporate more realism into the model, such as
CO₂ as another source of acidity. Experiments carried out on
glycolytic deficient Chinese hamster lung fibroblasts report that
the extracellular environment in vivo is acidic despite very little
production of lactate, which suggests that CO₂ maybe another
source of acidity (Newell et al., 1993). The over expressed enzyme
in aggressive cancers, Carbonic Anhydrase 9 (CA 9), catalyses the
hydration of extracellular CO₂ into H⁺ and HCO₃⁻, which is
thought to further acidify the extracellular environment. Studies
by Swietach et al. (2008) show that CA 9 reduces pHᵢ in cultured
spheroids but not in isolated cells. However, our current model
assumes no spatial heterogeneity and so one next step forward
would be to develop a spatial model to investigate the role of
Carbonic Anhydrase in the regulation of pH and to test the results

<a id='bd68115a-c59a-4fe7-acdd-2d0582aedc47'></a>

of for example Provent et al. (2007). That is, Provent et al. (2007)
shows that increased lactate levels show no spatial correlation
with low pHe. In addition, there is a growing evidence suggesting
that the expression of the Na+/H+ antiporter is up-regulated at
the leading edge of migrating cancer cells (Cardone et al., 2005;
Stock and Schwab, 2009). Therefore, our model could also be
extended to investigate the effect of pH on invasion and metas-
tasis and, in particular, whether the Na+/H+ and lactate/H+
transporters have a role in these processes.

<a id='918a58e7-3edf-4a5f-879d-356dc9612118'></a>

Another useful extension to our model would be to include the dynamics of pyruvate as presented in Bertuzzi et al (2010) in order to accurately describe the behaviour of lactate production and degradation in our model.

<a id='7126f56d-f32c-4b5a-8527-6cf205755ec1'></a>

## Acknowledgements
M.A. was supported by a studentship from the Engineering and Physical Sciences Research Council.

<a id='c265793e-93a5-41ae-bf1f-bc00e67d3a99'></a>

**Appendix A. Derivation of the lactate/H⁺ term**

Consider the following closed system which describes the transport of H⁺-ions and lactate across the cell membrane from the intracellular to the extracellular space via the MCT transporter:

<a id='2c45b46e-9c81-4167-a684-b308756ff3a1'></a>

[L_I] + [H_I]  k_1 / k_-1  <->  [L_I H_I]  k_2([L_I H_I] - [L_E H_E]) <->  [L_E H_E]  k_-1 / k_1  <->  [L_E] + [H_E],

(A.1)

<a id='452c75f4-001c-458e-b8c1-1782193dcaff'></a>

where [.] denotes concentration and $L_\sigma H_\sigma$ represents intracellular and extracellular lactic acid, for $\sigma = I,E$, respectively. The $k_2$ term denotes the rate of activity of the lactate/H$^+$ symporter and we assume that this activity is directly proportional to the concentration difference of lactic acid across the cell membrane. The rate at which lactic acid dissociates into lactate and H$^+$-ions is denoted by $k_{-1}$ and the rate of the reversible reaction is denoted by $k_1$.

<a id='b1ed0ef4-c375-48e3-95d1-6dc2000260dd'></a>

We then use the law of mass action to derive the following equations from the reactions shown in (A.1), namely:

$\frac{d[H_I]}{dt} = -k_1[L_I][H_I] + k_{-1}[L_IH_I]$ (A.2)

$\frac{d[L_I]}{dt} = -k_1[L_I][H_I] + k_{-1}[L_IH_I]$ (A.3)

$\frac{d[L_IH_I]}{dt} = k_1[L_I][H_I] - k_{-1}[L_IH_I] - k_2([L_IH_I] - [L_EH_E])$ (A.4)

$\frac{d[H_E]}{dt} = k_{-1}[L_EH_E] - k_1[H_E][L_E]$ (A.5)

$\frac{d[L_E]}{dt} = k_{-1}[L_EH_E] - k_1[H_E][L_E]$ (A.6)

$\frac{d[L_EH_E]}{dt} = -k_{-1}[L_EH_E] + k_1[H_E][L_E] + k_2([L_IH_I] - [L_EH_E])$ (A.7)

<a id='7f5dbb88-1fdd-4b25-80bc-2709f1277b63'></a>

Assuming that k_1 and k_-1 are large, that is, lactic acid dissociates freely to form lactate and H⁺-ions. This allows us to assume that [L_iH_i] and [L_eH_e] are quasi-steady. Hence, adding Eqs. (A.4) and (A.7) and solving algebraically for [L_1H_1] we get

<a id='631eb0cb-6740-4cf9-9c4d-7400d26db6c6'></a>

[L_I H_I] = k_1 / k_-1 ( [L_I][H_I] + [L_E][H_E] ) - [L_E H_E],

<a id='3873e2a3-58a5-4f83-b88b-c0a274d274a2'></a>

where

$[L_E H_E] = \frac{k_1 k_2}{k_{-1}(2k_2 + k_{-1})} ([L_I][H_I] + [L_E][H_E] (1 + \frac{k_{-1}}{k_2}))$.

<!-- PAGE BREAK -->

<a id='1add4e46-d1da-44b6-941c-27d2758cc043'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='8537bd36-d930-4ebc-874e-26dd78ac92fc'></a>

69

<a id='a5db342e-6ba9-44a6-9610-d5d5038e8e2c'></a>

So that the lactate/H⁺ efflux term after a little algebra,
k₁[LᵢHᵢ] - k₋₁[LᵢHᵢ], becomes
k₃([Hᵢ][Lᵢ] - [Hₑ][Lₑ]),

<a id='a2f16868-51f6-49b9-9708-2d31009ad4c1'></a>

where k₃ = k₁k₂/(2k₂ + k₋₁) and we will use this expression for lactate/H⁺ efflux via the MCT in our full model.

<a id='75132dd4-64af-4a97-824a-337593218802'></a>

Note that the above derivation for the MCT transporter denotes activity in the linear regime of the standard Michaelis-Menten kinetics obtained for this transporter by Vinnakota and Beard (2011).

<a id='95c44a0f-75bb-4242-9b9b-37943247452a'></a>

Appendix B. Parametrisation

Given the large number of parameters posed in the model, it has proved difficult to obtain concrete values for all our parameters. However, we were able to obtain values for some of the parameters using literature data, see Section 2 for details. The remaining parameters are determined by pre-assuming normoxic and hypoxic steady state values for pH_e, pH_i, L_I and L_E. Ball park estimates for these values are readily available in the literature. For instance, assuming that for a normal tissue in a normoxic environment: pH*_e = 7.4 (H*_e = 10^-7.4 mol/l), pH*_i = 7.2 (H*_i = 10^-7.2 mol/l), L*_I = 1 × 10^-3 mol/l, L*_E = 1.4 × 10^-3 mol/l (Stubbs et al., 1994) and we take V=1 to denote normoxia. Now, with b=10^-7 mol/l we have H̃*_I = 0.6310, H̃*_E = 0.3981, and now taking L̃*_E = 1 we have d_4/α_4 ~ O(10^-3) = 1.4 × 10^-3 and L̃*_I = 0.7143. Adding Eqs. (7) and (8) at steady state gives 1−L̃*_I −ρ̃_2VL*_E = 0 and substituting for L̃*_I, L̃*_E and V we then have ρ̃_2 = 0.2857. Then substituting for H̃*_E, H̃*_I, L̃*_I, L̃*_E and ρ̃_2 in Eq. (8) at steady state we have that k̃_3 = 5.4316. Now adding Eqs. (5) and (6) at steady state we get d̃_1 = ρ̃_1H̃*_E and substituting for H̃*_E we have that d̃_1 = 0.3981ρ̃_1. Assuming that the activity of Na^+/H^+ exchanger is of similar order to that of the MCT, i.e. (H̃*_I −H̃*_E)f̃_1 ≈ (H̃*_I L̃*_I −H̃*_E L̃*_E)k̃_3, we get f̃_1 = 1.7174 × 10^4. Using estimates for I_H from Lawrence (1989) and assuming that I_H = 10^-6f̃_1, we obtain from Eq. (5) at steady state d̃_1 = 7.9978 × 10^3.

<a id='33617982-4715-4b65-b59b-3abbc7936406'></a>

Now, for V < V* we would expect pH*e = 6.8 and pH*i = 6.58, respectively (Mellergard et al., 1994). Adding Eqs. (5) and (6) at steady state we get d̃₁ = p̃₁VH*e−2Φ̃Gψ/H̃I+1, from which we obtain Φ̃G = 0.2823. A summary of all the non-dimensional parameters is given in Table 1—we refer to this set of parameters as the 'base' set.

<a id='b99129c7-3dd7-4898-abe6-0cc3b2b00e7b'></a>

## Appendix C. Inner solution

We look for the inner solution of (9)-(12) valid near $t=0$, with the objective of understanding in more detail the sharp initial transient in the intra and extracellular pH solutions. We rescale time by letting $t = \epsilon^{\alpha}\tau$ and after substituting into (9)-(12) we find that the distinguished limit is reached when $\alpha = 4$. Now, with $t = \epsilon^4\tau$, putting $\epsilon = 0$ in the resulting equations we have

$L_D^0 = 0, L_T^0 = L_T^0(0), H_D^0 = 0 \text{ and } H_T^0 = H_T^0(0),$ (C.1)

where $H_T^0(0)$ and $L_T^0(0)$ correspond to the initial values of $H_T^0$ and $L_T^0$, respectively.

Equating $O(\epsilon)$ terms for $H_T$ and solving gives

$H_T^1 = (2\hat{\Phi}_G\hat{\Psi}H(\hat{V}^*-\hat{V})+\hat{d}_1-\hat{p}_1\hat{V}\hat{H}_T^0)\tau.$ (C.2)

Equating $O(\epsilon)$ terms for $H_D$ gives

$\frac{dH_D^1}{d\tau} = 2\hat{\Phi}_G\hat{\Psi}H(\hat{V}^*-\hat{V})+\hat{d}_1+\frac{\hat{p}_1\hat{V}}{2}\hat{H}_T^0-(k_3\hat{\Psi}\hat{L}_T^0+2\hat{f}_1)H_D^1.$ (C.3)

<a id='1bdbb6e7-f538-4d45-a714-1d4c1c3bc632'></a>

Solving for $H_D^1$ with $H_D^1(0) = 0$, we then get

$H_D^1 = \frac{(\hat{\rho}_1 \hat{V} H_T^0 + 4\hat{\Phi}_G \hat{\psi} H(\hat{V}^* - \hat{V}) + 2\hat{d}_1)(1-e^{-(k_3 \hat{\psi} L_T^0 + 2\hat{f}_1)\tau})}{2(2\hat{f}_1 + k_3 \hat{\psi} L_T^0)}$ (C.4)

where $H_T^0$ and $L_T^0$ are given in (C.1).
Equating $O(\epsilon)$ terms for $L_T$ and $L_D$ gives $L_T^1 = L_D^1 = 0$. Now,
equating $O(\epsilon^2)$ terms for $H_T$ gives

$\frac{dH_T^2}{d\tau} = -\frac{\hat{\rho}_1 \hat{V}(H_T^1 - H_D^1)}{2}$ (C.5)

<a id='43f932fe-c03d-4319-9960-652892a356c7'></a>

subject to $H^2_T(0) = 0$. Substituting for $H^1_D$, $H^1_T$ and solving for $H^2_T$ we then get

$H^2_T = \frac{\hat{\rho}_1 \hat{V}}{8(k_3 \psi \hat{L}^0_T + 2\hat{f}_1)^2} (k_3 \psi \hat{L}^0_T \tau (\hat{\rho}_1 k_3 \hat{\psi} \hat{V} H^0_T \hat{L}^0_T + 4\hat{\rho}_1 \hat{f}_1 \hat{V} H^0_T \tau + 2\hat{\rho}_1 \hat{V} H^0_T$
$+ 8\hat{\phi}_G \psi H(\hat{V}-\hat{V}^*) + 4\hat{d}_1 - 4k_3 \hat{\phi}_G \psi^2 H(\hat{V}-\hat{V}^*) \hat{L}^0_T \tau - 8\hat{d}_1 \hat{f}_1 \tau^2 - 8\hat{d}_1 \hat{f}_1$
$- 2\hat{d}_1 k_3 \hat{\phi}_G \psi H(\hat{V}-\hat{V}^*) \tau) + 8\hat{d}_1 \hat{f}_1 \tau + 4\hat{\rho}_1 \hat{f}_1^2 \hat{V} H^0_T \tau^2 - 4\hat{d}_1 - 2\hat{\rho}_1 \hat{V} H^0_T$
$+ (2\hat{\rho}_1 \hat{V} H^0_T + 8\hat{\phi}_G \psi H(\hat{V}-\hat{V}^*) + 4\hat{d}_1)e^{-(k_3 \psi \hat{L}^0_T + 2\hat{f}_1)} + 4\hat{\rho}_1 \hat{f}_1 \hat{V} H^0_T \tau$
$- 16\hat{f}_1 \hat{\phi}_G \psi H(\hat{V}-\hat{V}^*) (\psi k_3 \hat{L}^0_T \tau^2 + \tau^2 - 1) - 8\hat{\phi}_G \psi H(\hat{V}-\hat{V}^*))$.

<a id='d3589380-3abc-4a61-9a4d-8d692e57f982'></a>

Equating O(ε²) terms for H_D gives

$\frac{dH_D^2}{d\tau} = \frac{\hat{\rho}_1 \hat{V} (H_T^1 - H_D^1)}{2} - (2\hat{f}_1 + k_3 \hat{\psi} L_T^0)H_D^2$, (C.7)

which, on solving subject to $H_D^2(0) = 0$, we get

$H_D^2 = \frac{\hat{\rho}_1 \hat{V}}{4(k_3 \hat{\psi} L_T^0 + 2\hat{f}_1)^2} ((8\hat{\phi}_G \hat{\psi} H(\hat{V}^* - \hat{V}) + 4\hat{d}_1)(e^{-(k_3 \hat{\psi} L_T^0 + 2\hat{f}_1)\tau} - 1)

+ (4k_3 \hat{\phi}_G \hat{\psi}^2 H(\hat{V}^* - \hat{V}) L_T^0 \tau + 2\hat{d}_1 k_3 \hat{\psi} L_T^0 \tau + 8\hat{f}_1 \hat{\phi}_G \hat{\psi} H(\hat{V}^* - \hat{V}) \tau

- 8\hat{\phi}_G \hat{\psi} H(\hat{V}^* - \hat{V}) - 2\hat{\rho}_1 \hat{f}_1 \hat{V} H_T^0 \tau - \hat{\rho}_1 \hat{V} k_3 \hat{\psi} H_T^0 L_T^0 \tau + 4\hat{d}_1 \hat{f}_1 \tau

- 4\hat{d}_1)(e^{-(k_3 \hat{\psi} L_T^0 + 2\hat{f}_1)\tau} + 1)).$ (C.8)

Equating O(ε²) terms for $L_T$ and $L_D$ then gives $L_T^2 = 0, L_D^2 = 0$.
Equating O(ε³) terms in the $H_T$ equation gives

$\frac{dH_T^3}{d\tau} = -\frac{\hat{\rho}_1 \hat{V} (H_T^2 - H_D^2)}{2}.$ (C.9)

<a id='2aa56f26-3984-4da9-a100-358f01ae6f1c'></a>

Substituting for $H_D^2, H_T^2$ and solving for $H_T^3$ subject to $H_T^3(0) = 0$, we get

$H_T^3 = - \frac{\hat{\rho}_1^2 \hat{V}^2}{48(k_3 \hat{\psi} L_T^0 + 2\hat{f}_1)^3}((24k_3 \hat{\Phi}_G \hat{\psi}^2 L_T^0 \tau$

$+ 6k_3 \hat{\rho}_1 \hat{V} \hat{\psi} H_T^0 L_T^0 \tau + 24\hat{d}_1 (\hat{f}_1 \tau + 1)$

$+ 48\hat{\Phi}_G \hat{\psi} (1 + \hat{f}_1 \tau) + 12k_3 \hat{d}_1 \hat{\psi} L_T^0 \tau + 12\hat{f}_1 \hat{\rho}_1 \hat{V} H_T^0 \tau)e^{-(k_3 \hat{\psi} L_T^0 + 2\hat{f}_1)\tau}$

$+ 24\hat{d}_1 \hat{f}_1 \tau + 24k_3 \hat{\Phi}_G \hat{\psi}^2 L_T^0 \tau + 12\hat{d}_1 k_3 \hat{\psi} L_T^0 \tau - 12\hat{f}_1 \hat{\rho}_1 \hat{V} H_T^0 \tau$

$+ 24\hat{f}_1^2 \hat{\rho}_1 \hat{V} H_T^0 \tau^2 - 16\hat{f}_1^3 \hat{d}_1 \tau^3 + 8\hat{f}_1^3 \hat{\rho}_1 \hat{V} H_T^0 \tau^3 - 4k_3 \hat{\Phi}_G \hat{\psi}^4 L_T^0 3\tau^3$

$- 2\hat{d}_1 k_3^3 \hat{\psi}^3 L_T^0 3\tau^3 - 24\hat{f}_1 k_3^2 \hat{\Phi}_G \hat{\psi}^3 L_T^0 2\tau^3 - 12k_3^2 \hat{f}_1 \hat{d}_1 \hat{\psi}^2 L_T^0 2\tau^3$

$- 48\hat{f}_1^2 k_3 \hat{\Phi}_G \hat{\psi}^2 L_T^0 \tau^3 - 24\hat{d}_1 \hat{f}_1^2 k_3 \hat{\psi} L_T^0 \tau^3 - 32\hat{f}_1^3 \hat{\Phi}_G \hat{\psi} \tau^3 + 48\hat{f}_1 \hat{\Phi}_G \hat{\psi} \tau$

$+ k_3 \hat{\rho}_1 \hat{V} \hat{\psi} H_T^0 L_T^0 (6k_3 \hat{\psi} L_T^0 \tau^2 + 24\hat{f}_1 \tau^2 + 6\hat{f}_1 k_3 \hat{\psi} L_T^0 + k_3^2 \hat{\psi}^2 L_T^0 2\tau^3$

$+ 12\hat{f}_1^2 \tau^3 - 6) - 24\hat{d}_1 - 48\hat{\Phi}_G \hat{\psi})$.

(C.10)

<a id='e3d321dc-d65a-44fd-8f01-1f3f5253d501'></a>

Equating O(ε³) terms in the H_D equation gives

$\frac{dH_D^3}{d\tau} = \frac{\hat{\rho}_1 \hat{V}(H_T^2 - H_D^2)}{2} - (2\hat{f}_1 + k_3\hat{\psi} L_T^0)H_D^3$

(C.11)

<a id='98893e6b-54b6-4962-a9d9-c1c914ba8738'></a>

subject to $H_D^3(0) = 0$. This can be readily solved after substituting for $H_D^2$ and $H_T^2$ from above (solution not shown for brevity).

<!-- PAGE BREAK -->

<a id='2b23370b-7245-4e97-87fe-2b886f1c3676'></a>

70

<a id='0bbc9c40-c600-4230-8179-d0a99cecfc47'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58-71

<a id='6e6be521-0142-4862-8794-5ea526ae0d29'></a>

Equating O(€³) terms in the L_T and L_D equations gives
L_T³ = 0, L_D³ = 0. Equating O(€⁴) terms in the H_T equation then gives

$\frac{dH_T^4}{d\tau} = -\frac{\hat{\rho}_1\hat{V}(H_T^3 - H_D^3)}{2}$
(C.12)

<a id='c30bd0ec-78f4-46a6-9cf3-2d52ce6e06c4'></a>

Again, after substituting for $H_D^3, H_T^3$, (C.12) can be easily solved subject to $H_T^4(0) = 0$ (solution not shown for brevity).
Equating $O(\epsilon^4)$ in the $H_D$ equation gives

<a id='e6ab4858-fccf-48c6-ab44-7e49f8179d90'></a>

$$\frac{d H_D^4}{d \tau} = \frac{\hat{\rho}_1 \hat{V}(H_T^3 - H_D^3)}{2} - (2\hat{f}_1 + k_3 \hat{\psi} L_T^0) H_D^4 - k_3 \hat{\psi} H_T^0 L_D^4, \quad (C.13)$$

<a id='14d8bf1d-5883-46f3-ad6d-de6dcc1440fc'></a>

subject to $H_D^4(0)=0$. Here, $L_T^4$ and $L_D^4$, respectively, satisfy
$\frac{dL_T^4}{d\tau} = 1 - \frac{L_T^0}{2}$ and $\frac{dL_D^4}{d\tau} = 1 - \frac{L_D^0}{2}$, subject to $L_T^4(0) = 0$ and $L_D^4(0) = 0$
respectively, which in solving gives

<a id='9d56e970-a59f-4678-aa95-e339e652d9ea'></a>

$L_T^4 = \left(1 - \frac{L_T^0}{2}\right) \tau \quad \text{and} \quad L_D^4 = \left(1 - \frac{L_T^0}{2}\right) \tau$. (C.14)

<a id='edf3032b-74b3-4e24-bc07-fdd7d4cd6108'></a>

Eq. (C.13) can then be readily solved after substituting for $H_D^3, H_T^3$ and $L_D^4$ (solution not shown for brevity).
Now, equating $O(\epsilon^5)$ terms for $L_T$ gives

$\frac{dL_T^5}{d\tau} = 2\hat{\phi}_G H(\hat{V}^* - \hat{V})$, (C.15)

<a id='b25b0bf9-ee6a-478e-b684-17d1db26f77c'></a>

subject to $L_T^5(0) = 0$, which on solving gives $L_T^5 = 2\hat{\phi}_G H(\hat{V}^* - \hat{V})\tau$.
Equating $O(\epsilon^5)$ terms for $L_D^5$ then gives

$\frac{dL_D^5}{d\tau} = 2\hat{\phi}_G - k_3 L_T^0 H_D^1$, (C.16)

<a id='81c19968-c8ec-41be-a87f-4c0f3c1bf352'></a>

subject to $L_D^5(0) = 0$, which upon solving gives

<a id='de580ec3-5b20-4486-b939-44c3e5dbf36c'></a>

L_D^5 = \frac{-1}{2(k_3\hat{\psi}L_T^0+2\hat{f}_1)^2} ((k_3\hat{\rho}_1\hat{V}H_T^0+4k_3\hat{\Phi}_G\hat{\psi}+2\hat{d}_1k_3)L_T^0e^{-(k_3\hat{\psi}L_T^0+2\hat{f}_1)\tau}
+(k_3^2\hat{\rho}_1\hat{\psi}L_T^0H_T^0+2\hat{f}_1k_3\hat{\rho}_1\hat{V}H_T^0\tau
-8\hat{f}_1k_3\hat{\Phi}_G\hat{\psi}\tau+2\hat{d}_1k_3^2\hat{\psi}L_T^0\tau+4\hat{d}_1\hat{f}_1k_3\tau
-k_3\hat{\rho}_1\hat{V}H_T^0L_T^0-4k_3\hat{\Phi}_G\hat{\psi}-2\hat{d}_1k_3)L_T^0-16\hat{f}_1^2\hat{\Phi}_G\tau).
(C.17)

<a id='436411bc-e0b3-4a05-945e-3979da83175e'></a>

We equate O(ϵ^5) terms for the H_T and H_D equations and show
the resulting solution in Fig. 3.
Equating O(ϵ^6) terms for L_D gives

$\frac{dL_D^6}{d\tau} = L_T^0 \left( \frac{\hat{\rho}_2 \hat{V}}{2} - k_3 H_D^2 \right)$ (C.18)

<a id='ecd25e2f-11c2-45e1-8a3b-3eb7e9121634'></a>

subject to $L_D^6(0) = 0$, which can be easily solved upon substitution for $H_D^2$.

<a id='33716a75-92fd-435e-ac33-b7cc3433a6d3'></a>

Equating O(ε⁶) terms for L_T gives dL_T⁶/dτ = -ρ₂V̂L_T⁰, which subject to L_T⁶(0) = 0, solves to

<a id='a1b3f436-243b-489d-bf34-5a2cc73bd0d4'></a>

$$L_T^6 = \frac{-\hat{\rho}_2\hat{V}L_T^0\tau}{2}.$$ (C.19)

<a id='7bcd613f-b994-4703-9299-65755d2e213f'></a>

We equate O(ε⁷) and O(ε⁸) terms in the L_D equation and present the solutions in Fig. 3.

<a id='84742816-5683-406d-8f45-10208a8f37d0'></a>

The approximations for L_T and L_D, inclusive of all terms up to
O(ϵ^6), compare very well with the numerical solutions for t ∈ [0,ϵ^4]
as shown in Fig. 3 for V > V* and Fig. 4 for V < V*.

<a id='7e9ed4d2-3147-43f8-b708-b105a4669baa'></a>

With H_I(t,€) = (H_T(t,€)+H_D(t,€))/2, numerical inspections through variations in the magnitudes of the parameters that constitute H_I(t,€) shows that, amongst other parameters, L_T^0 in particular plays a crucial role in the sharp transient in the H+-ions profile. Recall that L_T^0 denotes the combined initial concentration of intra and extracellular lactate. With the initial levels of extracellular lactate kept fixed, L_E^0, numerical simulations show that increasing the initial intracellular lactate levels, L_I^0, results in a shallow profile of H+-ions (see Fig. 5(a)), which is much shallower when L_E^0 is increased (see inset of Fig. 5(a)).

<a id='aebb5d6b-765f-460f-939d-97be8567e18f'></a>

Numerical simulations illustrating the activity of the NHEs and MCTs reveal that, when L$_i^0$ and L$_E^0$ is low, the activity of the NHEs is much more rapid than the MCTs and that a sharp transient exists in the H$^+$-ions solution. On the other hand, a high L$_i^0$ and L$_E^0$ results in a much higher activity of the MCT (for a short time) and consequently a reversed pH gradient (for that period of time). Then, as extracellular H$^+$-ions and lactate build up, the MCTs import H$^+$-ions and lactate and hence provide intracellular H$^+$-ions for the NHEs to function again. Our results, therefore, suggest that the activity of the NHE indirectly controls the steepness of the initial transient of the pH solution.

<a id='b5b8affb-30ae-4942-9fd2-862a73a0c2d2'></a>

## References

Aronson, P.S., 1985. Kinetic properties of the plasma membrane Na+-H+ exchanger. Annu. Rev. Physiol. 47, 545-560.

Berg, J.M., Tymoczko, J.L., Stryer, L., 2003. Biochemistry, 5th ed. W. H. Freeman, New York.

Bertuzzi, A., Fasano, A., Gandolfi, A., Sinisgalli, C., 2010. Necrotic core in EMT6/Ro tumor spheroids: Is it caused by an ATP deficit?. J. Theor. Biol. 262, 142-150.

Boron, W.F., 1985. Intracellular pH-regulating mechanisms for the squid axons: relation between the external Na+ and HCO3- dependences. J. Gen. Physiol. 85 (3), 325-345.

Brooks, G.A., 1986. Lactate production under fully aerobic conditions: the lactate shuttle during rest and exercise. Fed. Proc. 45 (13).

Brown, J.M., 2002. Tumor microenvironment and the response to anticancer therapy (review). Cancer Biol. Ther. 1 (15), 453-458.

Bunimovich-Mendrazitsky, S., Byrne, H., Stone, K., 2008. Mathematical model of pulsed immunotherapy for superficial bladder cancer. Bull. Math. Biol. 70 (7), 2055-2076.

Cardone, R.A., Casavola, V., Reshkin, S.J., 2005. The role of distributed pH dynamics and the Na+/H+ exchanger in metastasis. Nat. Rev. Cancer 5, 786-795.

Casciari, J.J., Sotirchos, S.V., Sutherland, R.M., 1992. Variations in tumour cell growth rates and metabolism with oxygen concentrations, glucose concentra-tion, and extracellular pH. J. Cell. Physiol. 151 (2), 386-394.

Chaplain, M.A.J., McDougall, S.R., Anderson, A.R.A., 2006. Mathematical modeling of tumour-induced angiogenesis. Annu. Rev. Biomed. Eng. 8, 233-257.

Colen, C.B., Shen, Y., Ghoddoussi, F., Yu, P., Francis, T.B., Koch, B.J., Monterey, M.D., Galloway, M.P., Sloan, A.E., Mathupala, S.P., 2011. Metabolic targeting of lactate efflux by malignant glioma inhibits invasiveness and induces necrosis: an in vivo study1. Neoplasia 13 (7), 620-632.

Fitzgerald, R.C., Omary, M.B., Triadafilopoulos, G., 1997. Acid modulation of HT29 cell growth and differentiation. J. Cell Sci. 110 (5), 663-671.

Gatenby, R.A., Gawlinski, E.T., 1996. A reaction diffusion model of cancer invasion. Cancer Res. 56, 5745-5753.

Gatenby, R.A., Smallbone, K., Maini, P.K., Rose, F., Averill, J., Nagle, R.B., Worrall, L., Gillies, R.J., 2007. Cellular adaptations to hypoxia and acidosis during somatic evolution of breast cancer. Br. J. Cancer 97, 646-653.

Gerisch, A., Chaplain, M.A.J., 2008. Mathematical modelling of cancer cell invasion of tissue: local and non-local models and the effect of adhesion. J. Theor. Biol. 250, 684-704.

Gillies, R.J., Liu, Z., Bhujwalla, Z., 1994. 31P-MRS measurements of extracellular pH of tumors using 3-aminopropylphosphonate. Am. J. Physiol. 267 (1), C195-C203.

Griffiths, J.R., 1991. Are cancer cells acidic? Br. J. Cancer 3 (64), 425-427.

Henning, T., Krausb, M., Brischweina, M., Ottoa, A.M., Wolfa, B., 2004. Relevance of tumor microenvironment for progression, therapy and drug development (review). AntiCancer Drugs 15, 7-14.

Hochachka, P.W., Mommsen, T.P., 1983. Protons and anaerobiosis. Science 219, 1391-1397.

Humez, S., Monet, M., Coppenolle, F.V., Delcourt, P., Prevarskaya, N., 2003. The role of intracellular pH in cell growth arrest induced by ATP. Am. J. Physiol. Cell Physiol. 287, C1733-C1746.

Kaminskas, E., 1978. The pH-dependence of sugar-transport and glycolysis in cultured ehrlich ascites-tumour cells. Biochem. J. 174 (2), 453-459.

Lawrence, E., 1989. A Guide to Modern Biology: Genetics, Cells and Systems. Addison-Wesley Longman Ltd.

Lodish, H., Berk, A., Zipursky, S.L., Matsudaira, P., Baltimore, D., Darnell, J.E., 2008. Molecular Cell Biology, 4th ed. W.H. freeman, New York.

Mackenzie, C.G., Mackenzie, J.B., Beck, P., 1961. The effect of pH on growth, protein synthesis, and lipid-rich particles of cultured mammalian cells. J. Biophys. Biochem. Cytol. 9 (1), 141-156.

Martinez-Zaguilan, R., Seftor, E.A., Seftor, R.E., Chu, Y.W., Gillies, R.J., Hendrix, M.J., 1996. Acidic pH enhances the invasive behaviour of human melanoma cells. Clin. Exp. Metastas. 14 (2), 176-186.

McDermott, J.C., Bonen, A., 1993. Lactate transport by skeletal muscle sarcolemmal vesicles. Mol. Cell. Biochem. 122 (2), 113-121.

Mellergard, P., Ou-Yang, Y., Siesjo, B.K., 1994. Relationship between intra- and extracellular pH in primary cultures of rat astrocytes. Am. J. Physiol. Cell Physiol. 267 (2), C581-C589.

<!-- PAGE BREAK -->

<a id='0030b57d-9747-4c5e-a011-2da6e22a4e58'></a>

M. Al-Husari, S.D. Webb / Journal of Theoretical Biology 322 (2013) 58–71

<a id='be0d572a-e31d-4f3c-91c2-099c568dca2a'></a>

71

<a id='b0233338-7b0b-498a-82d7-51eb68639b48'></a>

Neville, A.A., 2003. Biomedical Modelling Incorporating Growth. Ph.D. Thesis, University of Nottingham.
Newell, K., Franchi, A., Pouysségur, J., Tannock, I., 1993. Studies with glycolysis-deficient cells suggest that production of lactic acid is not the only cause of tumor acidity. Proc. Natl. Acad. Sci. 90 (3), 1127-1131.
Nyberg, P., Salo, T., Kalluri, R., 2008. Tumor microenvironment and angiogenesis. Front Biosci. 1 (13), 6537-6553.
Parkkila, S., Rajaniemi, H., Parkkila, A., Kivelä, J., Waheed, A., Pastoreková, S., Pastorek, J., Sly, W.S., 2000. Carbonic anhydrase inhibitor suppresses invasion of renal cancer cells in vitro. Proc. Natl. Acad. Sci. USA 97 (5), 2220-2224.
Pouysségur, J., Dayan, F., Mazure, N., 2006. Hypoxia signalling in cancer and approaches to enforce tumour regression. Nature 441 (13), 437-443.
Provent, P., Benito, M., Hiba, B., Farion, R., López-Larrubia, P., Ballesteros, P., Rémy, C., Segebarth, C., Cerdán, S., Coles, J.A., García-Martín, M.L., 2007. Serial In vivo spectroscopic nuclear magnetic resonance imaging of lactate and extracellular pH in rat gilomas shows redistribution of protons away from sites of glycolysis. Cancer Res. 67 (16), 7638-7645.
Quennet, V., Yaromina, A., Zips, D., Rosner, A., Walenta, S., Baumann, M., Mueller-Kliesera, W., 2006. Tumor lactate content predicts for response to fractionated irradiation of human squamous cell carcinomas in nude mice. Radiother. Oncol. 81 (2), 130-135.
Raghunand, N., Gatenby, R.A., Gillies, R.J., 2003. Microenvironmental and cellular consequences of altered blood flow in tumours. Br. J. Radiol. 76, S11-S22.
Rofstad, E.K., Mathiesen, B., Kindem, K., Galappathi, K., 2006. Acidic extracellular pH promotes experimental metastasis of human melanoma cells in athymic nude mice. Cancer Res. 66 (13), 6699-6707.
Romero, M.F., 2004. In the beginning, there was the cell: cellular homeostasis. Adv. Physiol. Educ. 28, 135-138.
Sauer, L.A., Stayman, J.W., Dauchy, R.T., 1982. Amino acid, glucose, and lactic acid utilization in vivo by rat tumors. Cancer Res. 42, 4090-4097.
Schumer, W., 1978. Cell metabolism and lactate. In: Bossart, H., Perret, C. (Eds.), Lactate in Acute Conditions International Symposium. Basel, pp. 1-9.
Schwickert, G., Walenta, S., Sundfør, K., Rofstad, E.K., Mueller-Kliesera, W., 1995. Correlation of high lactate levels in human cervical cancer with incidence of metastasis. Cancer Res. 55, 4757-4759.
Smallbone, K., Gavaghan, D.J., Gatenby, R.A., Maini, P.K., 2005. The role of acidity in solid tumour growth and invasion. J. Theor. Biol. 235, 476-484.
Sonveaux, P., Copetti, T., Saedeleer, C.J.D., Vegran, F., Verrax, J., Kennedy, K.M., Moon, E.J., Dhup, S., Danhier, P., Frerart, F., Gallez, B., Ribeiro, A., Michiels, C.,

<a id='2b5a3e53-be5d-4822-a86f-2a3800fc70c0'></a>

Dewhirst, O., Feron, O., 2012. Targeting the lactate transporter MCT1 in endothelial cells inhibits lactate-induced HIF-1 activation and tumor angio-genesis. PLOS one 7 (3), e33418.
Stock, C., Schwab, A., 2009. Protons make tumor cells move like clockwork. Pflugers Arch. 458 (5), 981-992.
Stubbs, M., Rodrigues, L., Howe, F.A., Wang, J., Jeong, K.-S., Veech, R.L., Griffiths, J.R., 1994. Metabolic consequences of a reversed pH gradient in rat tumors. Cancer Res. 54, 4011-4016.
Swietach, P., Vaughan-Jones, R.D., Harris, A.L., 2007. Regulation of tumor pH and the role of carbonic anhydrase 9. Cancer Metast. Rev. 26, 299-310.
Swietach, P., Wigfield, S., Cobden, P., Supuran, C.T., Harris, A.L., Vaughan-Jones, R.D., 2008. Tumour-associated carbonic anhydrase 9 spatially co-ordinates intracellular pH in three-dimensional multicellular growths. J. Biol. Chem. 283 (29), 20473-20483.
Tozer, G.M., Maxwell, R.J., Griffiths, J.R., Pham, P., 1990. Modification of the 31P magnetic resonance spectra of a rat tumour using vasodilators and its relationship to hypotension. Br. J. Cancer 62 (4), 553-560.
Vaupel, P., Kallinowski, F., Okunieff, P., 1989. Blood flow, oxygen and nutrient supply, and metabolic microenvironment of human tumors. Cancer Res. 49 (23), 6449-6465.
Vinnakota, K.C., Beard, D.A., 2011. Kinetic analysis and design of experiments to identify the catalytic mechanism of the monocarboxylate transporter isoforms 4 and 1. Biophys. J. 100, 369-380.
Wachsberger, P.R., Landry, J., Storck, C., 1997. Mammalian cells adapted to growth at pH 6.7 have elevated HSP27 levels and are resistant to cisplatin. Int. J. Hyperther. 13, 251-255.
Walenta, S., Wetterling, M., Lehrke, M., Schwickert, G., Sundfør, K., Rofstad, E.K., Mueller-Kliesera, W., 2000. High lactate levels predict likelihood of metastasis, tumor recurrence, and restricted patient survival in human cervical cancers. Cancer Res. 16 (4), 916-921.
Warburg, O., Wind, F., Negelein, E., 1926. The metabolism of tumours in the body. J. Gen. Physiol. 8 (6), 519-530.
Webb, S.D., Sherratt, J.A., Fish, R.G., 1999a. Alterations in proteolytic activity at low pH and its association with invasion: a theoretical model. Clin. Exp. Metastas. 17, 397-407.
Webb, S.D., Sherratt, J.A., Fish, R.G., 1999b. Mathematical modelling of tumour acidity: regulation of intracellular pH. J. Theor. Biol. 196, 237-250.
Webb, B.A., Chimenti, M., Jacobson, M.P., Barber, D.L., 2011. Dysregulated pH a perfect storm for cancer progression. Nat. Rev. Cancer 11 (9), 671-700.