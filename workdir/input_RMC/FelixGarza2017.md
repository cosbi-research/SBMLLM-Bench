<a id='f6fd7c50-01b9-4bd1-86fd-9c5dbb7c9ea6'></a>

<::logo: [Frontiers] [frontiers in Physiology] [The logo features a colorful, abstract cube-like graphic to the left of the text.]::>

<a id='194fc365-7090-4ef0-a20d-085b0a311661'></a>

ORIGINAL RESEARCH published: 26 January 2017 doi: 10.3389/fphys.2017.00028

<a id='d43b67ee-6b22-44d9-80d4-d6c7eaeae68b'></a>

<::logo: [Unknown] Check for updates A grey square button with a circular icon containing a stylized upward-pointing arrow or flag symbol, with text "Check for updates" below it.::>

<a id='76bc05d6-9b8c-49a1-9b9d-f68e40b36a29'></a>

## A Dynamic Model for Prediction of Psoriasis Management by Blue Light Irradiation

Zacher S. Fille. Orser-1* [illegible] Mathius Do [illegible] Retes A. Ull [illegible]

<a id='e7adbce4-508b-440d-bd95-e9c4870c72e0'></a>

Zandra C. Félix Garza¹*, Joerg Liebmann², Matthias Born², Peter A. J. Hilbers¹ and
Natal A. W. van Riel¹

<a id='99bf2b1f-5f29-4ef5-bb2e-a777fbf82e0f'></a>

1 Department of Biomedical Engineering, Eindhoven University of Technology, Eindhoven, Netherlands, 2 Philips Technologie
GmbH, Innovative Technologies, Aachen, Germany

<a id='ac0aacb5-9092-4f1a-a7f3-5894e39f28a8'></a>

Clinical investigations prove that blue light irradiation reduces the severity of psoriasis vulgaris. Nevertheless, the mechanisms involved in the management of this condition remain poorly defined. Despite the encouraging results of the clinical studies, no clear guidelines are specified in the literature for the irradiation scheme regime of blue light-based therapy for psoriasis. We investigated the underlying mechanism of blue light irradiation of psoriatic skin, and tested the hypothesis that regulation of proliferation is a key process. We implemented a mechanistic model of cellular epidermal dynamics to analyze whether a temporary decrease of keratinocytes hyper-proliferation can explain the outcome of phototherapy with blue light. Our results suggest that the main effect of blue light on keratinocytes impacts the proliferative cells. They show that the decrease in the keratinocytes proliferative capacity is sufficient to induce a transient decrease in the severity of psoriasis. To study the impact of the therapeutic regime on the efficacy of psoriasis treatment, we performed simulations for different combinations of the treatment parameters, i.e., length of treatment, fluence (also referred to as dose), and intensity. These simulations indicate that high efficacy is achieved by regimes with long duration and high fluence levels, regardless of the chosen intensity. Our modeling approach constitutes a framework for testing diverse hypotheses on the underlying mechanism of blue light-based phototherapy, and for designing effective strategies for the treatment of psoriasis.

<a id='a94a499d-2da0-4b3c-bafe-075b5c7a6fb5'></a>

Keywords: inflammatory skin conditions, epidermis, keratinocytes, computational model, phototherapy, visible light

<a id='74763409-058d-40c3-b89f-d867a36427f4'></a>

# INTRODUCTION

Blue light (BL) at 453 nm is non-toxic (Awakowicz et al., 2009; Kleinpenning et al., 2010) and decreases the symptoms of psoriasis vulgaris (Pv) (Weinstabl et al., 2011; Pfaff et al., 2015), a chronic, inflammatory skin condition that affects 2–3% of the world's population (Parisi et al., 2013). Psoriasis vulgaris is characterized by hyper proliferation and lowered differentiation of skin

<a id='d20c556c-0c1c-4cae-902d-ead8decc203f'></a>

**Abbreviations:** BL, Blue Light; Pv, Psoriasis vulgaris; F, Fluence; UV, Ultraviolet light; BLISS, Computational model for Blue Light Irradiation of Psoriatic Skin; Psc, Stem Cells; Pta, Transit Amplifying cells; Pga, Growth Arrested cells; Psp, Spinous cells; Pgc, Granular Cells; Pcc, Corneocytes; Iav, Average power density; CW, Continuous Wave mode; PW, Pulsed Wave mode; Ip, Peak power density; PASI, Psoriasis Area and Severity Index; LPSI, Local Psoriasis Severity Index; MPSA, Multiple parameter sensitivity analysis; LPSA, Local sensitivity analysis; LI, Low Intensity; HI, High Intensity.

<a id='0d6d2ea1-f070-4135-bb95-9b88dd26b1fb'></a>

OPEN ACCESS

*Edited by:*
Matteo Barberis,
University of Amsterdam, Netherlands

<a id='b57d3bea-7ff6-4095-8bcd-bec497ae7ffa'></a>

**Reviewed by:**
*Marcel Schilling,*
*German Cancer Research Center,*
*Germany*
*Tianhui Niu,*
*The General Hospital of Air Force,*
*China*

<a id='69e99e55-e3f6-4ec4-a193-e5e439e19f5b'></a>

**Correspondence:**
*Zandra C. Félix Garza*
*z.c.felix.garza@tue.nl*

<a id='ee0cad41-7db5-4c3b-846b-9fe9bf363f4a'></a>

**Specialty section:**
This article was submitted to
*Systems Biology,*
a section of the journal
*Frontiers in Physiology*

<a id='95a7b84d-bd88-497a-af06-656d9ca24b9f'></a>

**Received**: 27 October 2016

**Accepted**: 11 January 2017

**Published**: 26 January 2017

<a id='a31b35ae-7e45-42da-bbe8-0c0cd69cd5ea'></a>

**Citation:**
Félix Garza ZC, Liebmann J, Born M,
Hilbers PAJ and van Riel NAW (2017)
A Dynamic Model for Prediction of
Psoriasis Management by Blue Light
Irradiation. Front. Physiol. 8:28.
doi: 10.3389/fphys.2017.00028

<a id='49da6e51-d070-47e0-93bb-3a10291806b2'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='4c737e99-6bb5-497e-b80d-32b36ccac270'></a>

1

<a id='a1addeee-5b72-4ab5-94a5-34f4def465a6'></a>

January 2017 | Volume 8 | Article 28

<a id='24abd49c-175c-4b80-9742-37f31f7fddae'></a>

nt

<!-- PAGE BREAK -->

<a id='5e453abc-cb91-4f1c-bf6d-8a9ae780fdfa'></a>

Félix Garza et al.

<a id='e4edb9a7-ed20-431d-acec-410dd06d3c3e'></a>

Dynamic Model of Blue Light Treatment

<a id='b2e4d866-3bbd-4b53-9835-b66931d948da'></a>

keratinocytes (Weinstein et al., 1985), evident in lesional areas
of thick skin (Perera et al., 2012). These areas also exhibit
sustained inflammation caused by immune cells such as T cells
and dendritic cells (Perera et al., 2012). Blue light minimizes the
proliferation of keratinocytes and induces their differentiation in
a wavelength and fluence dependent manner (Liebmann et al.,
2010). Additionally, blue light irradiation suppresses dendritic
cell activation (Fischer et al., 2013). These effects of blue light
on keratinocytes and immune cells may explain the reduced
inflammation and diminished epidermal thickness of lesional
psoriatic skin after the treatment. Nevertheless, the underlying
mechanism of this therapeutic approach is not fully understood.
It is not clear how the cellular processes of proliferation and
differentiation are modified in the cells after irradiation with
blue light. Further, it is uncertain whether blue light affects only
proliferative cells or both proliferative and non-proliferative cells.
It is hypothesized that BL improves psoriatic skin by decreasing
the proliferative capacity of keratinocytes.

<a id='45151dca-a0b3-4f04-bcb8-f6258482381b'></a>

Large variations are observed in the results from the available clinical investigations (Maari et al., 2003; Weinstabl et al., 2011; Kleinpenning et al., 2012; Pfaff et al., 2015). These discrepancies in the reported outcome may be due to differences in the main treatment parameters, i.e. length of treatment (days), fluence F (Jcm-2) also referred to as dose, and power density (mWcm-2) also denoted as intensity. Additionally, a BL treatment session may occur one or more times per week for a certain number of weeks (Maari et al., 2003; Weinstabl et al., 2011). Despite all the potential combinations of treatment parameters and their impact on the effectiveness of the treatment, the effect of variations in the irradiation parameters of BL on the dynamics of keratinocytes is unknown. Additionally, no clear guidelines have been defined in the literature for BL treatment of psoriasis. The current treatments for psoriasis include phototherapy with ultraviolet (UV) light (Schneider et al., 2008). UV phototherapy is effective but only indicated for severely affected patients due to the risk of skin cancer (Pathak, 1991) caused by DNA damage. In contrast with UV, blue light is not toxic to skin cells (Awakowicz et al., 2009). The difference in the therapeutic effects of both spectral ranges is the result of the interactions between these spectral ranges and their molecular photoacceptors. UV is absorbed by DNA (Markovitsi, 2016) and yields DNA damage (Lee et al., 2013), cell death, and remission of psoriasis. Blue light is accepted by flavins (Eichler et al., 2005) and porphyrins (Dai et al., 2012), resulting in a decreased proliferative capacity and management of psoriasis. The non-toxicity and beneficial effects of blue light make it an attractive alternative to UV phototherapy. Emphasizing the need for establishing clear treatment recommendations that lead to an effective therapeutic regime using blue light.

<a id='120a5c11-726b-46e0-88f6-c8f96f166970'></a>

Considering that the details of the mechanism of blue light-
based therapy for psoriasis are still not fully elucidated, it
seems suitable to use computational methods for their analysis.
Computational models have previously been used to predict
cellular behaviors (Savill, 2003; Gandolfi et al., 2011) and the
effects of ultraviolet irradiation on the skin (Weatherhead et al.,
2011; Zhang et al., 2015). This approach may contribute to the
investigation of processes occurring in the epidermis after blue

<a id='1fb7669f-f47d-4d04-8ae2-18342516a628'></a>

light irradiation, and extend our knowledge on the principles of regulatory effects induced by this spectral range on the keratinocytes dynamics.

<a id='7c4032c2-a0f5-435d-968c-7e7a61e44732'></a>

Here, we study the blue light treatment of psoriasis using an
in silico approach. We first used the model to explore whether
a temporary decrease of keratinocytes hyper-proliferation can
explain the outcome of phototherapy with blue light. The
model accurately described the response to blue light therapy.
The simulations suggested that the observed decrease in the
keratinocytes proliferation rate is sufficient to reduce the
epidermal thickness and severity of psoriasis. However, it was
not sufficient to allow psoriatic epidermis to completely remodel
back to a healthy phenotype, regardless the treatment scheme.
Then, we analyzed the effect of length of treatment, fluence,
and intensity on the management of this inflammatory skin
condition. The model predicted that high efficacy is achieved by
treatment schemes with long duration and high fluence levels.

<a id='73df8339-0bf2-47ca-94f0-19c4ae5a8e43'></a>

## MATERIALS AND METHODS

To describe the management of psoriasis by blue light, we implemented a computational model for BL irradiation of psoriatic skin (BLISS; Figure 1). This model is defined by a set of 12 ordinary differential equations (ODEs) describing the time evolution of keratinocytes as they move vertically through the layers of the epidermis while blue light is shined upon them. BLISS was developed based on the phenomenological observations of decreased proliferation and increased differentiation of keratinocytes due to blue light, particularly at a wavelength of 453 nm. In this section we describe the general structure of the model, its implementation, and analysis.

<a id='3d5732d2-e0d5-45a6-b246-4a857c9021e4'></a>

# Computational Model
In contrast with UV, BL does not lead to cell death below fluences of 500 Jcm-2 (Awakowicz et al., 2009). Instead, it affects the proliferation and differentiation of the keratinocytes, which are key processes in the model we propose. The general structure and assumptions considered in the model regarding the kinetics of keratinocytes in psoriasis are based on the work of Zhang et al. (2015) for UV phototherapy of psoriasis. However, the main difference with their model is the implementation of the underlying mechanism by which the kinetics of the keratinocytes are affected upon BL irradiation.

<a id='c28d6200-08a7-426c-abf5-aac6884d202b'></a>

In the model (Figure 1), we represent psoriasis as a bi-stable system and assume that keratinocytes show either a healthy or diseased phenotype. We consider that both populations coexist and interact within the epidermis. This assumption allows the description of the effects induced by blue light therapy. The set of ODEs describing the interactions between healthy and diseased keratinocytes under the influence of blue light are presented by Equations (1-12). This set of equations describes the kinetics of keratinocytes at six stages of differentiation in both their healthy (Equations 1-6) and diseased (Equations 7-12) state, i.e., stem cells (Psch,d), transit amplifying cells (Pah,d), growth arrested cells (Pgah,d), spinous cells (Psph,d), granular cells (Pgch,d), corneocytes (Pcch,d). Stem cells and transit amplifying

<a id='3a631a34-ae90-4131-aee5-12b5ead0c82b'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='ebd1454b-1593-45ce-b50f-51911df64a17'></a>

2

<a id='3c1f42a4-54b8-4a1d-a604-25ab9034c81d'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='a9b4f43e-405d-4c4f-b4d3-26c3942c4408'></a>

Félix Garza et al.

<a id='bf38920d-f63f-4029-8e45-11cb45bd4f36'></a>

Dynamic Model of Blue Light Treatment

<a id='d61a0daf-c163-4e58-8824-e665c08a3cb8'></a>

<::Figure: A. Diagram illustrating the structure of the epidermis and the impact of blue light. The epidermis is divided into: Stratum Corneum (topmost, red), Stratum Granulosum (orange), Stratum Spinosum (green), and Stratum Basale (bottom, light blue). The Stratum Corneum, Granulosum, and Spinosum form the Non-Proliferative Compartment, while the Stratum Basale forms the Proliferative Compartment, which rests on the Dermis. Blue light is shown as arrows impacting the Stratum Corneum. On the right, a legend depicts cell types for both Healthy keratinocytes and Diseased keratinocytes: - Corneocyte (red oval) - Granular cell (orange oval) - Spinous cell (green oval) - Growth arrested cell (light blue oval) - Transit amplifying cell (dark blue oval) - Stem cell (darkest blue oval). B. Two flowcharts illustrating cell dynamics, one for healthy and one for diseased conditions. Each flowchart shows a progression of cell states from bottom to top: Stem cell (darkest blue oval), Transit amplifying cell (dark blue oval), Growth arrested cell (light blue oval), Spinous cell (green oval), Granular cell (orange oval), and Corneocyte (red oval). Various rates govern transitions between states: - From Stem cell to Transit amplifying cell: γ₁BLh (proliferation) and k₋₁h, k₁a,sh (back conversion/asymmetric division) for healthy; γ₁BLd and k₋₁d, k₁a,sd for diseased. - From Transit amplifying cell to Growth arrested cell: γ₂BLh (proliferation) and k₋₂h, k₂a,sh (back conversion/asymmetric division) for healthy; γ₂BLd and k₋₂d, k₂a,sd for diseased. - From Growth arrested cell to Spinous cell: k₃h for healthy; k₃d for diseased. - From Spinous cell to Granular cell: k₄h for healthy; k₄d for diseased. - From Granular cell to Corneocyte: k₅h for healthy; k₅d for diseased. - From Corneocyte, cells are removed by desquamation (αh for healthy, αd for diseased). - Apoptosis rates (βnh) are shown exiting each cell type from Growth arrested cell to Corneocyte for healthy; (βnd) for diseased. A legend on the right defines the parameters: - γ₁: Proliferation rate - kᵢs: Symmetric division rate - kᵢa: Asymmetric division rate - k₋ᵢ: Back conversion rate (With 1 ≤ i ≤ 2) - kⱼ: Differentiation rate (With 3 ≤ j ≤ 5) - βn: Apoptosis rate (With 1 ≤ n ≤ 5) - α: Desquamation rate - h = healthy - d = diseased - BL = Blue light phototherapy::>

<a id='6f83fd55-cd30-4540-926d-3d392ff3e21e'></a>

FIGURE 1 | Schematic description of the mechanistic model for blue light treatment of psoriasis. (A) The model considers the 4 sub-layers of the epidermis, the 6 stages of differentiation for keratinocytes across the sub-layers. (B) BLISS accounts for the cellular processes of proliferation (y), differentiation (k), apoptosis (β), and desquamation (α).

<a id='1a3438e2-ef7e-4b61-aaf7-c14a0229ff49'></a>

cells form the proliferative compartment of the epidermis, and corneocytes are the end point of the differentiation process. The ODEs account for the cellular processes of proliferation (Yh,d), differentiation (kh,d), apoptosis (ẞh,d), and desquamation (ah,d). The cells in the proliferative compartment may divide in one of three modes, i.e., produce to daughter cells equal to the progenitor [self-proliferation (yh,d)], generate two daughter cells where one corresponds to the next stage of differentiation [asymmetric division (kah,d)], or induce two daughter cells where both correspond to the next stage of differentiation [symmetric division (ksh,d)]. The description of each parameter considered in these equations is presented in Table 1. These parameters were derived from one of three sources, i.e., the literature, calculated from other model parameters as specified in Table 1, or estimated by fitting the model to experimental data of Liebmann et al. (2010).

<a id='6f4847c4-d12e-4631-b9fd-e7fd2fc1345f'></a>

dP_sch / dt = [ γ_1h θ_BLy (1 - (P_sch + P_scd / λ) / P_sc^max ) - k_1sh θ_BLk - β_1h ] / (P_sch + k_-1h P_tah) (1)

<a id='5f02ccd2-dbf4-48f5-9b1c-95bedacf39c1'></a>

$$\frac{dP_{tah}}{dt} = (\gamma_{2h}\theta_{BLy} - k_{2sh}\theta_{BLk} - \beta_{2h} - k_{-1h})P_{tah} - (k_{1ah} + 2k_{1sh})\theta_{BLk}P_{sch} + k_{-2h}P_{gah}\quad(2)$$

$$\frac{dP_{gah}}{dt} = (k_{2ah} + k_{2sh})\theta_{BLk}P_{tah} - (k_{-2h} + k_{3h}\theta_{BLk} + \beta_{3h})P_{gah}\quad(3)$$

$$\frac{dP_{sph}}{dt} = k_{3h}\theta_{BLk}P_{gah} - (k_{4h}\theta_{BLk} + \beta_{4h})P_{sph}\quad(4)$$

$$\frac{dP_{gch}}{dt} = k_{4h}\theta_{BLk}P_{sph} - (k_{5h}\theta_{BLk} + \beta_{5h})P_{gch}\quad(5)$$

$$\frac{dP_{cch}}{dt} = k_{5h}\theta_{BLk}P_{gch} - a_h P_{cch}\quad(6)$$

$$\frac{dP_{scd}}{dt} = \left[\gamma_{1d}\theta_{BLy}\left(1 - \frac{P_{sch} + P_{scd}}{\lambda P_{sc}^{max}}\right) - k_{1sd}\theta_{BLk} - \beta_{1d}\right]P_{scd} - \frac{K_p P_{scd}^2}{K_a^2 + P_{scd}^2} + k_{-1d}P_{tad}\quad(7)$$

<a id='89121178-f8a9-4582-94ce-c7052079c98c'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='6cd9e9c1-1e4f-4eee-8b09-342753508dab'></a>

3

<a id='dbb83121-dc0e-4ca3-9887-bc63466e4cea'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='6b313c7c-fe7d-47a0-9aeb-1e2760c5e12a'></a>

Félix Garza et al.

<a id='6efc2976-5f6a-4859-9ae7-54d76c4ed4e8'></a>

Dynamic Model of Blue Light Treatment

<a id='e3fc0661-8f90-4157-9950-a5fb9ec6078a'></a>

TABLE 1 | BLISS model parameterization.
<table id="3-1">
<tr><td id="3-2">Parameter</td><td id="3-3">Description</td><td id="3-4">Value</td><td id="3-5">Source</td></tr>
<tr><td id="3-6">Pmax SC</td><td id="3-7">Growth capacity of stem cells</td><td id="3-8">4.5 x 103 mm-2</td><td id="3-9">Zhang et al., 2015</td></tr>
<tr><td id="3-a">Y1hom</td><td id="3-b">Minimal stem cell self-proliferation rate constant</td><td id="3-c">3.30 x 10-3 d-1</td><td id="3-d">Zhang et al., 2015</td></tr>
<tr><td id="3-e">K1shom</td><td id="3-f">Minimal symmetric healthy stem cell division rate constant</td><td id="3-g">1.64 x 10-3 d-1</td><td id="3-h">Clayton et al., 2007; Zhang et al., 2015</td></tr>
<tr><td id="3-i">K1ahom</td><td id="3-j">Minimal asymmetric healthy stem cell division rate constant</td><td id="3-k">1.31 x 10-2 d-1</td><td id="3-l">Clayton et al., 2007; Zhang et al., 2015</td></tr>
<tr><td id="3-m">\gamma_{2h}</td><td id="3-n">Healthy transit amplifying cells self-proliferation rate constant</td><td id="3-o">1.40\times10^{-2}d^{-1}</td><td id="3-p">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-q">k_{2sh}</td><td id="3-r">Healthy transit amplifying cells symmetric division rate constant</td><td id="3-s">1.73\times10^{-2}d^{-1}</td><td id="3-t">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-u">k_{2ah}</td><td id="3-v">Healthy transit amplifying cells asymmetric division rate constant</td><td id="3-w">1.38\times10^{-1}d^{-1}</td><td id="3-x">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-y">K_{3h}</td><td id="3-z">Healthy growth arrested to spinous cells differentiation rate constant</td><td id="3-A">2.16\times10^{-1}d^{-1}</td><td id="3-B">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-C">k_{4h}</td><td id="3-D">Healthy spinous to granular cells differentiation rate constant</td><td id="3-E">5.56\times10^{-2}d^{-1}</td><td id="3-F">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-G">Kih</td><td id="3-H">Healthy granular cells to corneocytes differentiation rate constant</td><td id="3-I">1.11 x 10-1 d-1</td><td id="3-J">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-K">K-1h</td><td id="3-L">Back conversion rate constant of healthy cells (transit amplifying to stem cells)</td><td id="3-M">1.00 x 10-6 d-1</td><td id="3-N">Zhang et al., 2015</td></tr>
<tr><td id="3-O">K-2h</td><td id="3-P">Back conversion rate constant of healthy cells (growth arrested to transit amplifying cells)</td><td id="3-Q">1.00 x 10-6 d-1</td><td id="3-R">Zhang et al., 2015</td></tr>
<tr><td id="3-S">w</td><td id="3-T">Maximum fold increase of stem cells proliferation rate</td><td id="3-U">100</td><td id="3-V">Heenen et al., 1998; Zhang et al., 2015</td></tr>
<tr><td id="3-W">n</td><td id="3-X">Stem cells proliferation rate regulation by transit amplifying cells</td><td id="3-Y">3</td><td id="3-Z">Zhang et al., 2015</td></tr>
<tr><td id="3-10">Alh</td><td id="3-11">Epidermal apoptosis index for healthy skin</td><td id="3-12">0.12%</td><td id="3-13">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-14">β1h</td><td id="3-15">Apoptosis rate of healthy epidermal stem cells</td><td id="3-16">1.97 x 10-6 d-1</td><td id="3-17">Calculated as described by Equation 16</td></tr>
<tr><td id="3-18">β2h</td><td id="3-19">Apoptosis rate of healthy transit amplifying cells</td><td id="3-1a">2.08 x 10-5 d-1</td><td id="3-1b">Calculated as described by Equation 16</td></tr>
<tr><td id="3-1c">β3h</td><td id="3-1d">Apoptosis rate of healthy growth arrested cells</td><td id="3-1e">2.60 x 10-4 d-1</td><td id="3-1f">Calculated as described by Equation 16</td></tr>
<tr><td id="3-1g">β4h</td><td id="3-1h">Apoptosis rate of healthy spinous cells</td><td id="3-1i">6.68 x 10-5 d-1</td><td id="3-1j">Calculated as described by equation 16</td></tr>
<tr><td id="3-1k">β5h</td><td id="3-1l">Apoptosis rate of healthy granular cells</td><td id="3-1m">1.33 x 10-4 d-1</td><td id="3-1n">Calculated as described by Equation 16</td></tr>
<tr><td id="3-1o">αh</td><td id="3-1p">Healthy corneocytes desquamation rate constant</td><td id="3-1q">7.14 x 10-2 d-1</td><td id="3-1r">Weinstein et al., 1985; Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-1s">ρsc</td><td id="3-1t">Fold change of stem cells proliferation in psoriasis</td><td id="3-1u">4</td><td id="3-1v">Weinstein et al., 1985; Zhang et al., 2015</td></tr>
<tr><td id="3-1w">ρta</td><td id="3-1x">Fold change of transit amplifying cells proliferation in psoriasis</td><td id="3-1y">4</td><td id="3-1z">Weinstein et al., 1985; Zhang et al., 2015</td></tr>
<tr><td id="3-1A">ρtr</td><td id="3-1B">Fold change of psoriatic cells transit rate</td><td id="3-1C">5</td><td id="3-1D">Weatherhead et al., 2011; Zhang et al., 2015</td></tr>
<tr><td id="3-1E">Pde</td><td id="3-1F">Fold change of psoriatic corneocytes desquamation</td><td id="3-1G">4</td><td id="3-1H">Weinstein and Van Scott, 1965; Zhang et al., 2015</td></tr>
<tr><td id="3-1I">\lambda</td><td id="3-1J">Fold change of stem cells growth capacity in psoriasis</td><td id="3-1K">3.5</td><td id="3-1L">Heenen et al., 1987; Simonart et al., 2010; Zhang et al., 2015</td></tr>
<tr><td id="3-1M">Kp</td><td id="3-1N">Maximum immune response rate</td><td id="3-1O">6</td><td id="3-1P">Zhang et al., 2015</td></tr>
<tr><td id="3-1Q">Ka</td><td id="3-1R">Half-activation of immune system by psoriatic stem cells density</td><td id="3-1S">380</td><td id="3-1T">Zhang et al., 2015</td></tr>
<tr><td id="3-1U">\gamma1d</td><td id="3-1V">Diseased stem cell self-proliferation rate constant</td><td id="3-1W">1.16 x 10^-2 d^-1</td><td id="3-1X">Calculated as the product f\gamma_{1hom} and \rho_{sc}</td></tr>
<tr><td id="3-1Y">K1sd</td><td id="3-1Z">Symmetric diseased stem cell division rate constant</td><td id="3-20">5.70 x 10-3d-1</td><td id="3-21">Calculated as the product of Kishom and pesc</td></tr>
<tr><td id="3-22">K1ad</td><td id="3-23">Asymmetric diseased stem cell division rate constant</td><td id="3-24">4.59 x 10-2 d-1</td><td id="3-25">Calculated as the product of Kishom and Pesc</td></tr>
<tr><td id="3-26">Y2d</td><td id="3-27">Diseased transit amplifying cells self-proliferation rate constant</td><td id="3-28">4.90 x 10-2</td><td id="3-29">Calculated as the product of y2h and Pta</td></tr>
<tr><td id="3-2a">K2sd</td><td id="3-2b">Diseased transit amplifying cels symmetric division rate constant</td><td id="3-2c">6.06 x 10-2 d-1</td><td id="3-2d">Calculated as the product of k2sh and pta</td></tr>
<tr><td id="3-2e">K2ad</td><td id="3-2f">Diseased transit amplifying cells asymmetric division rate constant</td><td id="3-2g">4.83 x 10-1 1</td><td id="3-2h">Calculated as the product of k2ah and Pta</td></tr>
<tr><td id="3-2i">K3d</td><td id="3-2j">Diseased growth arrested to spinous cells differentiation rate constant</td><td id="3-2k">9.72 x 10-1 d-1</td><td id="3-2l">Calculated as the product of kah and ptr</td></tr>
<tr><td id="3-2m">K4d</td><td id="3-2n">Diseased spinous to granular cells differentiation rate constant</td><td id="3-2o">2.50 x 10-1 d-1</td><td id="3-2p">Calculated as the product of kah and ptr</td></tr>
<tr><td id="3-2q">K5d</td><td id="3-2r">Diseased granular cells to corneocytes differentiation rate constant</td><td id="3-2s">3.89 x 10-1 d-1</td><td id="3-2t">Calculated as the product of ksh and ptr</td></tr>
<tr><td id="3-2u">Ald</td><td id="3-2v">Epidermal apoptosis index for psoriatic skin</td><td id="3-2w">0.035%</td><td id="3-2x">Bauer et al., 2001; Hoath and Leahy, 2003; Zhang et al., 2015</td></tr>
<tr><td id="3-2y">Bid</td><td id="3-2z">Apoptosis rate of diseased epidermal stem cells</td><td id="3-2A">2.01 x 10-6d-1</td><td id="3-2B">Calculated as described by Equation 17</td></tr>
<tr><td id="3-2C">β2d</td><td id="3-2D">Apoptosis rate of diseased transit amplifying cells</td><td id="3-2E">2.12 x 10⁻⁵ d⁻¹</td><td id="3-2F">Calculated as described by Equation 17</td></tr>
</table>

<a id='ce817f44-f5e6-4593-ad1a-66e7f62540e2'></a>

(Continued)

<a id='4348d51a-1534-4d05-b18d-f256530088b9'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='b8f11b60-d8e6-4754-9e53-035245034522'></a>

4

<a id='1b01cf6d-d693-4271-a19d-7e6242c3f228'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='be62bb1a-7787-4cde-b368-fc265cf59116'></a>

Félix Garza et al.

<a id='ace3f53e-6001-499b-8514-c3351355765f'></a>

Dynamic Model of Blue Light Treatment

<a id='cadf174f-1422-4759-b1ee-6f44f781fdad'></a>

TABLE 1 | Continued
<table id="4-1">
<tr><td id="4-2">Parameter</td><td id="4-3">Description</td><td id="4-4">Value</td><td id="4-5">Source</td></tr>
<tr><td id="4-6">β3d</td><td id="4-7">Apoptosis rate of diseased growth arrested cells</td><td id="4-8">3.40 x 10-4 d-1</td><td id="4-9">Calculated as described by Equation 17</td></tr>
<tr><td id="4-a">β4d</td><td id="4-b">Apoptosis rate of diseased spinous cells</td><td id="4-c">8.76 x 10-5 d-1</td><td id="4-d">Calculated as described by Equation 17</td></tr>
<tr><td id="4-e">β5d</td><td id="4-f">Apoptosis rate of diseased granular cells</td><td id="4-g">1.36 x 10-4 d-1</td><td id="4-h">Calculated as described by Equation 17</td></tr>
<tr><td id="4-i">αd</td><td id="4-j">Diseased corneocytes desquamation rate constant</td><td id="4-k">2.50 x 10-1 d-1</td><td id="4-l">Calculated as the product of αh and ρde</td></tr>
<tr><td id="4-m">ay</td><td id="4-n">Blue light coefficient for proliferation factor</td><td id="4-o">1</td><td id="4-p">Estimated from Liebmann et al., 2010</td></tr>
<tr><td id="4-q">by</td><td id="4-r">Blue light coefficient for proliferation factor</td><td id="4-s">-3.40 x 10-3</td><td id="4-t">Estimated from Liebmann et al., 2010</td></tr>
<tr><td id="4-u">ak</td><td id="4-v">Blue light coefficient for differentiation factor</td><td id="4-w">2.46</td><td id="4-x">Estimated from Liebmann et al., 2010</td></tr>
<tr><td id="4-y">bk</td><td id="4-z">Blue light coefficient for differentiation factor</td><td id="4-A">1.94 x 10-2</td><td id="4-B">Estimated from Liebmann et al., 2010</td></tr>
<tr><td id="4-C">ck</td><td id="4-D">Blue light coefficient for differentiation factor</td><td id="4-E">3.46</td><td id="4-F">Estimated from Liebmann et al., 2010</td></tr>
<tr><td id="4-G">BBL β500-750</td><td id="4-H">Blue light factor increasing the apoptosis rate at fluences higher than 500 Jcm-2 and lower than 750 Jcm-2</td><td id="4-I">3.9 x 10-2</td><td id="4-J">Awakowicz et al., 2009</td></tr>
<tr><td id="4-K">θBL β&gt;750</td><td id="4-L">Blue light factor increasing the apoptosis rate at fluences higher than 750 Jcm-2</td><td id="4-M">5 x 10-2</td><td id="4-N">Awakowicz et al., 2009</td></tr>
<tr><td id="4-O">ξabs</td><td id="4-P">Energy absorbance of the epidermis for a low perfused Caucasian skin</td><td id="4-Q">57.9%</td><td id="4-R">Calculated from optical model</td></tr>
</table>

<a id='44403194-4d73-4423-b076-5b782f3de9e5'></a>

$$\frac{dP_{tad}}{dt} = (\gamma_{2d}\theta_{BL}\gamma - k_{2sd}\theta_{BLk} - \beta_{2d} - k_{-1d}) P_{tad} \\ \quad - (k_{1ad} + 2k_{1sd}) \theta_{BLk}P_{scd} + k_{-2d}P_{gad} \quad (8)$$

$$\frac{dP_{gad}}{dt} = (k_{2ad} + k_{2sd}) \theta_{BLk}P_{tad} \\ \quad - (k_{-2d} + k_{3d}\theta_{BLk} + \beta_{3d}) P_{gad} \quad (9)$$

$$\frac{dP_{spd}}{dt} = k_{3d}\theta_{BLk}P_{gad} - (k_{4h}\theta_{BLk} + \beta_{4d}) P_{spd} \quad (10)$$

$$\frac{dP_{gcd}}{dt} = 0 \quad (11)$$

$$\frac{dP_{ccd}}{dt} = k_{5d}\theta_{BLk}P_{gcd} - a_{d}P_{ccd} \quad (12)$$

<a id='7f88d688-3173-48fa-9c7e-554a61ea7fe4'></a>

Where

$\frac{\gamma_{1h}}{\gamma_{1,hom}} = \frac{k_{1ah}}{k_{1a,hom}} = \frac{k_{1sh}}{k_{1s,hom}} = \frac{\omega}{1 + (\omega - 1)\left(\frac{P_{tah} + P_{tad}}{P_{ta,hom}}\right)^n}$ (13)

<a id='a212f3c9-c625-4c96-891d-541032dd3b84'></a>

In psoriasis, the increased number of keratinocytes is the result of a hyper-proliferative population of basal cells and a sustained activation of the immune system. In the model, the hyper-proliferative population is represented by the diseased stem cells and transit amplifying cells proliferating at a rate $\gamma_d$, which is faster than the proliferative rate of their healthy counterparts. It is assumed that there are a maximum number of stem cells $P_{sc}^{max}$ available in the epidermis, which limits the numbers of healthy and diseased stem cells $P_{sch,d}$. The diseased stem cells have a larger growth capacity defined by fold increase $\lambda$. The sustained activation of the immune system is considered through the removal of diseased stem cells in Equation (7). The sustained immune system response is regulated by the density of diseased stem cells and defined by the maximum killing rate $K_p$ and the half activation of the immune system $K_a$ due to psoriatic stem cells. The immune response is ample when the cell density of diseased cells exceeds the threshold defined by $K_a$.

<a id='732322b1-fb1b-4708-b73d-6e0869d87032'></a>

In Equation (13), γ₁,_hom_, k₁a,_hom_, k₁s,_hom_ are the homeostatic rate constants for each division process, and P_ta,_hom_ is the homeostatic density of transit amplifying cells (Zhang et al., 2015). The density of the total transit amplifying cells population is the sum of the healthy and diseased groups of transit amplifying cells. The maximum increase in the growth fraction and decrease in the cell cycle time of fast proliferating stem cells is indicated by ω. n represents the steepness of the stem cells proliferation rate regulated by the transit amplifying cells population. When the number of healthy transit amplifying cells is low, the proliferation and division rates of the healthy stem cells increase. Alternatively, the healthy stem cell parameter rates are at their minimum values when the population of healthy transit amplifying cells equals its homeostatic population. It is assumed that psoriatic stem cells are not regulated by the population of transit amplifying cells. Thus, they proliferate with rates ρ_sc_ fold higher than the healthy stem cells rate constants in homeostasis. The proliferation and differentiation rates of diseased transit amplifying cells (γ₂_d_, k₂_sd_, and k₂_ad_) are ρ_ta_ fold changes higher than the rates of healthy transit amplifying cells. Similarly the diseased cells in the non-proliferative compartment, i.e., P_gad_ and P_spd_, differentiate ρ_tr_ times faster than their healthy counterparts. The desquamation (α_d_) of psoriatic corneocytes is affected by ρ_de_. Note that Equation (11) equals to zero, given that granular cells are lost in psoriasis due to abnormal differentiation.

<a id='c9a11cf3-f9db-4514-b886-5d47d9df578d'></a>

Irradiation with blue light exponentially decreases the proliferation rate of all healthy and diseased proliferative keratinocytes by a fluence dependent factor $\theta_{BLY}$ with a value between 0 and 1 (Equation 14).

<a id='e62e357e-f133-4435-b324-76808d3a5300'></a>

$\theta_{BL\gamma} = a_\gamma e^{(b_\gamma F)}$ with $a_\gamma > 0$ and $b_\gamma < 0$ (14)

<a id='4620c50e-9d40-4b57-b2df-5d4fd8650952'></a>

Based on the keratinocytes behavior experimentally observed
(Liebmann et al., 2010), blue light might also directly affect
the differentiation rate of the keratinocytes in an exponential
manner by a fluence dependent factor $\theta_{BLK}$ with a value between
0 and 1 (Equation 15). Parameters related to the decrease of the

<a id='cb36e7a5-b5bc-4132-9bd1-b8a612726e9e'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='2b7aea9d-cbc1-4bf6-b239-eb69c2e8bd5a'></a>

5

<a id='d74c2475-65ad-44fb-84f8-1c0ecfc7a443'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='c3b7d112-e847-4b79-ba9d-cb725d0e71c7'></a>

Félix Garza et al.

<a id='03edf686-f307-4a8e-b9ea-dcd62ba225f4'></a>

Dynamic Model of Blue Light Treatment

<a id='86dfe23a-41d5-47b3-9cc1-00eeaec08f0e'></a>

proliferation and increase of differentiation rates were initially estimated by fitting _in vitro_ data from Liebmann et al. (2010).

<a id='174daf20-20a2-4bb8-b3de-2c71c7c5e186'></a>

$\theta_{BLk} = c_k - a_k e^{(b_k F)}$ with $a_k, b_k$ and $c_k > 0$ (15)

<a id='efcce460-9957-46f4-8b8e-6e4f358870bb'></a>

Blue light phototherapy is divided into sessions with a certain fluence _F_, defined by the product of the irradiation time and the average intensity _Iav_ at which light is shined on the skin. The treatment sessions can occur one time per day in a daily or spread out basis. In the model we consider that each day of treatment affects the proliferation of the keratinocytes, based on _F_ > 0. In days where no treatment is provided _F_ = 0 and _θBLy_ = _θBLK_ = 1.

<a id='5b52ffb9-1fe0-4d5e-8063-6513319efb23'></a>

The apoptosis rates of the healthy keratinocytes βh (Equation
16) are determined by the differentiation rate of each population
(k1sh, k2sh, k3h, k4h, k5h) and the probability of a cell undergoing
apoptosis (apoptotic index AIh). The apoptotic index is a
common measurement for quantifying the extent of apoptosis
for a given cell population. It is defined as the ratio of apoptosis
rate to the total out flux. At fluences higher than 500 Jcm⁻² BL
increases the apoptosis of keratinocytes by factor θBLβ. Thus,
accounting for the cytotoxicity observed only at high fluences of
blue light (Awakowicz et al., 2009). Below 500 Jcm⁻², θBLβ has a
value of 0, for F between 500 and 750 Jcm⁻² its value is 0.039, and
0.05 above 750 Jcm⁻².

<a id='fb4d0243-dffe-475c-a127-a0f817cc25bb'></a>

$\beta_h = \frac{AI_h k_j}{1 - AI_h} + \theta_{BL\beta}$ j $\in$ {1$_{sh}$, 2$_{sh}$, 3$_h$, 4$_h$, 5$_h$} (16)

<a id='7911de66-9677-46cd-a015-9eca91ebea3e'></a>

The diseased keratinocytes have an apoptosis rate defined by the apoptotic index of psoriatic cells *AI*<sub>d</sub>, the differentiation rate of each population (*k*<sub>1sd</sub>, *k*<sub>2sd</sub>, *k*<sub>3d</sub>, *k*<sub>4d</sub>, *k*<sub>5d</sub>) and *q*<sub>BLβ</sub>. (Equation 17).

<a id='97a9dce6-7fa6-41f3-a935-626604a32798'></a>

$\beta_d = \frac{AI_d k_j}{1 - AI_d} + \theta_{BL}\beta$

j $\in$ {$1_{sd}$, $2_{sd}$, $3_d$, $4_d$, $5_d$} (17)

<a id='3ea315e0-9ce5-4919-b6c1-7ddb97232791'></a>

The skin has specific wavelength dependent optical properties that must be considered in the model, i.e., refractive index, absorption coefficient, scattering coefficient, and anisotropy factor (van Gemert et al., 1989). These properties vary per skin layer and skin type (Zonios et al., 2001). BLISS accounts for a low perfused type 1-3 skin with an epidermal energy absorbance level of 57.9%. This value was computed using an unpublished five- layered optical model developed in LightTools (Synopsis). The energy absorbance value defines the amount of BL energy that is absorbed by the epidermis. Skin types 4-6 have a higher energy absorbance, however are not considered in the model.

<a id='32b9adfd-e337-4ad9-b0b4-0f5ba67e27bc'></a>

## Model Implementation and Analysis
The model was implemented in Matlab (The Mathworks Inc.).
The ODE system was solved with ode-solver ode15s. The inputs
of the model were the BL irradiation parameters (Table 2) and
the initial cell density of the 12 keratinocyte populations (Table 3)
representing an psoriatic epidermis (Simonart et al., 2010; Zhang
et al., 2015). The total keratinocytes cell density in the simulated
epidermis at t = 0 was of 217,556 cells per mm², which is 2
times higher than that of healthy skin (~100,000 cells per mm²;
Hoath and Leahy, 2003). BLISS is available at GitHub¹ and

<a id='d78a3b6a-30f4-48cb-9b95-659a58222879'></a>

¹ https://github.com/ZFelixGarza/BLISS

<a id='14b60382-682b-4a2c-ad7e-8af6eccd24e3'></a>

TABLE 2 | Blue light irradiation parameters.
<table><thead><tr><th>Parameter</th><th>Value</th></tr></thead><tbody><tr><td>Fluence</td><td>90 Jcm-2</td></tr><tr><td>Irradiation mode</td><td>Continuous or pulsed</td></tr><tr><td>Irradiation time</td><td>1800 s (30 min)</td></tr><tr><td>Duration of treatment</td><td>84 days</td></tr></tbody></table>

<a id='0911a5ea-cd1e-49e8-9673-2bc5f2c9694e'></a>

TABLE 3 | Initial cell density distribution (cells per mm²).
<table id="5-1">
<tr><td id="5-2">Keratinocytes population</td><td id="5-3">Healthy</td><td id="5-4">Psoriatic</td></tr>
<tr><td id="5-5">Corneocytes</td><td id="5-6">185</td><td id="5-7">77,633</td></tr>
<tr><td id="5-8">Granular cells</td><td id="5-9">119</td><td id="5-a">0</td></tr>
<tr><td id="5-b">Spinous cells</td><td id="5-c">238</td><td id="5-d">79,788</td></tr>
<tr><td id="5-e">Growth arrested cells</td><td id="5-f">61</td><td id="5-g">20,536</td></tr>
<tr><td id="5-h">Transit amplifying cells</td><td id="5-i">77</td><td id="5-j">32,098</td></tr>
<tr><td id="5-k">Stem cells</td><td id="5-l">362</td><td id="5-m">6459</td></tr>
<tr><td id="5-n">Total</td><td id="5-o" colspan="2">1042 + 216514 = 217,556</td></tr>
</table>

<a id='c59357cb-226d-44e7-9d15-0742228d31ec'></a>

the BioModels Database² (Chelliah et al., 2015) with identifier
MODEL1701090001.

<a id='3d6c4b05-9140-42b3-b643-f5d089e2bebc'></a>

A full treatment of blue light was simulated by modifying the proliferation, differentiation, and apoptotic rates on the day of a BL session during the whole treatment. For example, if the treatment sessions occurred three times per week for 8 weeks, the rates were only varying on those specific days during the 8 weeks of treatment. During a treatment session, light can be shined in a continuous (CW) or pulsed (PW) mode. In CW the fluence of blue light, defined as power density I multiplied by time t, is provided at a constant peak power density Ip, which is equal to the average power density Iav. In PW, the epidermis is irradiated in short pulses at an Ip higher than Iav. The model allows for the simulation of both modes based on a given duty cycle, fluence, and treatment time. These inputs are used to compute the Ip and duration of each peak and define the instants in which the proliferation rates are decreased during the treatment time.

<a id='0eb429a5-9249-46e8-b6d0-0adea7b46136'></a>

BLISS calculates the cell densities over time, during and after blue light phototherapy for each healthy and diseased keratinocyte population. The model's results can be directly compared to *in vitro* data. However, in psoriasis most clinical data is given in terms of the psoriasis area and severity index (PASI), or its local form, i.e., the local psoriasis severity index (LPSI; Maari et al., 2003; Weinstabl et al., 2011; Pfaff et al., 2015). PASI is a quantitative rating score for measuring the severity of a psoriatic lesion based on the degree of erythema, scaling and induration per anatomic area, i.e., head, trunk, upper, and lower limbs. Each of the three characteristics is graded on a scale from 0 to 4, giving a maximum score of 12 per area based on the percentage of coverage. The maximum PASI is 72, mild psoriasis which is the target of blue light treatment corresponds to a PASI of 0–10. Induration is related to the thickness of the epidermis, and scaliness is related to the status of the Stratum Corneum.

<a id='8c6a3392-0888-4471-82fd-314430f3e258'></a>

2http://www.ebi.ac.uk/biomodels-main/

<a id='e7b512b1-2d6d-48ff-9fb3-d8560da383a8'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='9c386b19-fd10-4661-9321-a8b70c3a7fba'></a>

6

<a id='835be979-97f9-4caf-90c2-22e18164a383'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='f6c28a8d-4746-418c-8e56-d50aa54979ad'></a>

Félix Garza et al.

<a id='0d9b34ff-d957-427c-9b5f-21a449607937'></a>

Dynamic Model of Blue Light Treatment

<a id='d8bda0e8-b34f-4dd5-9ff3-418130df3353'></a>

Both features are comprised within the model. Thus, assuming an initial LPSI value and a positive correlation between thickness and scaliness with the cell density of keratinocytes, the LPSI is derived from the relative change in the total cell density of keratinocytes as indicated by Equation (18). A similar approach has been previously described in the literature (Ng et al., 2005; Zhou et al., 2010).

<a id='c4977eca-2085-4652-ba72-bc78b3a0171f'></a>

LPSI_i = LPSI_0 - LPSI_0 ( (P_{Tot_i} - P_{Tot_0}) / P_{Tot_0} ) where i >= 1 (18)

<a id='dd653585-8498-4752-91a8-48d58dc102a7'></a>

Data from the clinical investigation of Pfaff et al. (2015) was used
to verify the adequate description of BL treatment of psoriasis by
the model.

<a id='3f8cf40d-53fc-498d-b9d8-a014a4f6e01d'></a>

## Multiple Parameter Sensitivity Analysis
A multiple parameter sensitivity analysis (MPSA) was performed to understand how the system may be affected by uncertainty in the model's parameters. An initial simulation for blue light treatment was executed with the nominal model parameters _θ_ref presented in **Table 1**. From this first simulation the reference output response _y_ref(_k_) was computed, where _k_ represents the cell density of each keratinocyte cell densities derived by the model. 500,000 random parameter value sets were generated with the _lhsdesign_ MATLAB function. The parameter sets _θ_(_i_) were used as input to the model and simulations were implemented. The cost function _v_(_i_) for the simulation results obtained with each parameter set was calculated as the sum of squared errors between the perturbed _y_sim and reference output _y_ref (Equation 19).

<a id='70081351-4088-40ed-a0cf-c99bfad1ba44'></a>

$$v(i) = \sum_{k=1}^{N} (y_{ref}(k) - y_{sim}(k, \theta(i)))^2 \quad (19)$$


<a id='8d36a954-2349-4b05-9b9e-8b7c66136156'></a>

The parameter sets were then classified as acceptable or unacceptable and the cumulative frequency functions were computed for the acceptable and unacceptable values of each parameter. Then, the Kolmogorov–Smirnov statistic was calculated as the separation between S_a(\theta) and S_u(\theta) (Equation 20).

<a id='17448f29-00ff-47dd-86b0-0bd0160a9bcf'></a>

D = max |Sa(θ) - Sq(θ)|                                         (20)

<a id='3e7fd4cb-884c-4699-b14a-24c569f868f5'></a>

Finally, this value was used to derive the sensitivity of each
parameter on the cell density of all keratinocyte populations
at each of the six differentiation states and the local psoriasis
severity index. Additionally, a local sensitivity analysis (LPSA;
Marino et al., 2008) was performed for the parameters
identified by the MPSA for further understanding of how small
perturbations in these parameters reflect on the output of the
model.

<a id='ff0a6b62-6744-405c-b46e-d1cb607155c3'></a>

## RESULTS
**The Regulation of the Keratinocytes
Proliferation Is Key in the Mechanism of
Blue Light Irradiation**
Given the phenomenological observations reported in the
literature and the flexibility offered by the model to describe

<a id='9b4d9a7f-7c00-4172-98a9-2423b7e2da07'></a>

them, we first analyzed all the possible _in silico_ representations of the changes induced on the proliferation and differentiation of the keratinocytes. **Table 4** presents a summary of all potential cases.

<a id='6ac1cf69-afe7-4dad-84dd-5e62d40d242b'></a>

The general set of ODEs used in this analysis is presented by (Equations 1–17). Note that for cases where only θ_BLY is considered, θ_BLK is equal to 1. Similarly when only θ_BLK is considered, θ_BLY equals 1. For cases where only the stem cells and transit amplifying cells are affected, θ_BLK for the differentiation rates of growth arrested, spinous, and granular cells equals 1. For each case, the time evolution of proliferation and differentiation parameters, the net proliferative and differentiation capacity of the keratinocytes, and the regulatory capacity of the immune system is computed (Figure 2). From this analysis, it is clear that shifting only parameters related to the symmetric and asymmetric division of proliferative keratinocytes does not yield a decrease on the proliferative compartment (Figures 2B,D,E). Further, changing the division parameters causes a marked increase in the differentiation rates (Figures 2B–D,F, H–M), which is reflected in an increased cell density of the transit amplifying cells in the proliferative compartment and all cells in the non-proliferative compartment. Modifying the self-proliferation rate of the proliferative keratinocytes leads to a decrease on the proliferation and increase on the differentiation of the cells in the proliferative compartment, without unrealistic surge of the keratinocytes differentiation capacity (Figure 2A). Thus, we conclude that the effect of blue light is best described in silico when θ_BLY is lower than 1 and θ_BLK is equal to 1. The simulations and results presented in the following sections of this work are based on this conclusion.

<a id='7aa5e194-954e-4daa-86c9-f47b0926044d'></a>

# A Transient Decrease in the Proliferative Capacity of Keratinocytes Lowers the Severity of Psoriatic Lesions
The results from Section The Regulation of the Keratinocytes Proliferation is Key in the Mechanism of Blue Light Irradiation suggested that the experimental observations for keratinocytes (Liebmann et al., 2010) are best described by the model when the self-proliferation rate of all stem cells and transit amplifying cells decreases during blue light irradiation. Simulations performed for the same conditions of that in vitro study show a similar reduction in the relative cell number achieved after BL irradiation at fluence of 33, 66, and 100 Jcm-2 (Figure 3A). To verify that the model was also able to describe the reduced severity achieved by blue light treatment of psoriatic skin, simulations (Figure 3B) were performed and compared to data from the clinical investigation of Pfaff et al. (2015). Their clinical study measured the LPSI of psoriatic patients after irradiating the skin with 90 Jcm-2 of pulsed blue light for 12 weeks at either a low (LI), 100 mWcm-2, or high (HI), 200 mWcm-2, peak intensities. During the first 4 weeks the patients were treated every day, the next 8 weeks the therapy occurred three times per week. In the simulations, the initial LPSI values are equal to those of the clinical investigation (Pfaff et al., 2015; i.e., 5.52 for LI and 5.17 for HI). The model achieved an accurate representation of the applied treatments at low and high peak

<a id='3dd721e2-5443-422d-9a91-bf7536ca0205'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='1f18e7c6-19fc-44bf-8424-349974db0bac'></a>

7

<a id='c22bae82-0e8a-4057-a67a-853fce850a27'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='d1f23010-e480-4190-9aa5-09563c586791'></a>

Félix Garza et al.

<a id='3ab13eb3-e468-40ee-914b-ef53648b1a2b'></a>

Dynamic Model of Blue Light Treatment

<a id='4f94cc83-9367-4a71-b213-599a20ddc071'></a>

TABLE 4 | Possible cases describing the blue light effects on the cellular processes of keratinocytes.
<table id="7-1">
<tr><td id="7-2">Case</td><td id="7-3">Rate modified</td><td id="7-4">Value of blue light factors θBLγ and θBLK</td><td id="7-5">Population affected</td></tr>
<tr><td id="7-6">1</td><td id="7-7">Self-proliferation rates y₁ and y₂ are decreased.</td><td id="7-8">θBLγ &lt; 1 and θBLK = 1 for proliferative cells</td><td id="7-9">Proliferative cells, i.e. stem cells and</td></tr>
<tr><td id="7-a">2</td><td id="7-b">Asymmetric (k₁a and k₂a) and symmetric (k₁s and k₂s) division rates of proliferative cells are increased.</td><td id="7-c">θBLγ = 1 and θBLK &gt; 1 for proliferative cells</td><td id="7-d">transit amplifying cells.</td></tr>
<tr><td id="7-e">3</td><td id="7-f">The self-proliferation rates (y₁ and y₂) are decreased and the asymmetric and symmetric division rates (k₁a, k₂a, k₁s, and k₂s) are increased.</td><td id="7-g">θBLγ &lt; 1 and θBLK &gt; 1 for proliferative cells</td><td id="7-h"></td></tr>
<tr><td id="7-i">4</td><td id="7-j">Asymmetric (k₁a and k₂a) division rates are increased.</td><td id="7-k">θBLγ = 1 and θBLK &gt; 1 (for the asymmetric division rates of proliferative cells)</td><td id="7-l"></td></tr>
<tr><td id="7-m">5</td><td id="7-n">Symmetric (k1s and k2s) division rates are increased.</td><td id="7-o">θBLY = 1 and θBLK &gt; 1 (for the symmetric division rates of proliferative cells)</td><td id="7-p"></td></tr>
<tr><td id="7-q">6</td><td id="7-r">The self-proliferation rates (γ1 and γ2) are decreased and the asymmetric division rates (k1a and k2a) are increased.</td><td id="7-s">θBLY &lt; 1 and θBLK &gt; 1 (for the asymmetric division rates of proliferative cells)</td><td id="7-t"></td></tr>
<tr><td id="7-u">7</td><td id="7-v">The self-proliferation rates (γ1 and γ2) are decreased and the symmetric division rates (k1s and k2s) are increased.</td><td id="7-w">θBLY &lt; 1 and θBLK &gt; 1 (for the symmetric division rates of proliferative cells)</td><td id="7-x"></td></tr>
<tr><td id="7-y">8</td><td id="7-z">Differentiation rates (k3, k4, and k5) of non-proliferative cells are increased.</td><td id="7-A">θBLY = 1 and θBLK &gt; 1 (for division rates of non-proliferative cells)</td><td id="7-B">Non-proliferative cells, i.e. growth arrested cells, spinous cells, and granular cells.</td></tr>
<tr><td id="7-C">9</td><td id="7-D">Differentiation rates (K1a, Kis, K2a, k2s, K3, K4, and k5) of all cells are increased.</td><td id="7-E">θBLY = 1 and θBLK &gt; 1 (for division rates of all cells)</td><td id="7-F">Proliferative cells, i.e. stem cells and transit amplifying cells. Non-proliferative</td></tr>
<tr><td id="7-G">10</td><td id="7-H">The self-proliferation rates (y1 and y2) are decreased and the differentiation rates (k3, k4, and k5) of non-proliferative cells are increased.</td><td id="7-I">OBLy &lt;1 and @BLK &gt; 1 (for division rates of non-proliferative cells)</td><td id="7-J">cells, i.e. growth arrested cells, spinous cells, and granular cells.</td></tr>
<tr><td id="7-K">11</td><td id="7-L">The asymmetric division and differentiation rates (k1a, k2a, k3, k4, and k5) are increased.</td><td id="7-M">@BLY =1 and @BLk &gt; 1 (for the asymmetric division rates of proliferative cells and the division rates of non-proliferative cells)</td><td id="7-N"></td></tr>
<tr><td id="7-O">12</td><td id="7-P">The symmetric division and differentiation rates (k1s, k2s, k3, k4, and k5) are increased.</td><td id="7-Q">OBLy 1 and @BLk &gt; 1 (for the symmetric division rates of proliferative cells and the division rates of non-proliferative cells)</td><td id="7-R"></td></tr>
<tr><td id="7-S">13</td><td id="7-T">The self-proliferation rates (y₁ and y2) are decreased and the division and differentiation rates (k1a, k1s, K2a: K2s k3, k4, and k5) are increased.</td><td id="7-U">@BLy &gt; 1 and @BLk &gt; 1 (for division rates of all cells)</td><td id="7-V"></td></tr>
</table>

<a id='4e226429-55cb-4001-9f01-3733f79b35ef'></a>

intensities, particularly during the first 4 weeks. In the next 8 weeks, the _in silico_ results are less pronounced compared to the clinical study. The final values predicted by the model are within the error margins of the experimental results. Based on the results of the simulations performed for the experimental and clinical studies, it is evident that the transient decrease in proliferation has a pivotal role in the underlying mechanism of blue light treatment.

<a id='c32b4b15-566a-4e10-a15e-c512fde912da'></a>

To assess the impact of changes in the proliferation rate and other model parameters on the outcome of the treatment, a multiple parameter sensitivity analysis was implemented. Figure 4 presents the results of this analysis for all model parameters in relation to the keratinocyte cell densities (Figure 4A) and the LPSI (Figure 4B). According to Figure 4A, the model output is mainly affected by 12 parameters related to the proliferation of stem cells and transit amplifying cells. However, not all keratinocyte populations are evenly altered by variations in these parameters, some affect only the healthy populations while others have an impact on the diseased populations. The cell density of psoriatic keratinocytes is mainly affected by the proliferation rate of healthy and diseased transit amplifying cells. Conversely, the proliferation rate of psoriatic stem cells only impacts the healthy populations and the psoriatic stem cells. The LPSA performed for these 12 sensitive parameters

<a id='8913d8b0-1384-467a-b059-1c4be195c589'></a>

indicated that diseased transit amplifying cells are most sensitive to small perturbations on the proliferation rate of healthy transit amplifying cells. This parameter as well as the proliferation rate of diseased stem cells and transit amplifying cells are directly related to the fluence, intensity and irradiation time used by the implemented treatment. From the 12 parameters identified in the MPSA for keratinocytes cell density, only seven have a strong impact on the local severity of psoriasis at the end of treatment (Figure 4B). These seven parameters correspond to those affecting the cell densities of diseased keratinocyte populations. The impact of these parameters on the LPSI is consistent with the effect on the cell density of diseased keratinocytes, but lower in comparison to the latter.

<a id='c77a39c9-589e-4d63-b9ce-52184e4b1a3a'></a>

Based on the sensitivity analysis, it was confirmed that the decreased proliferation capacity induced by blue light irradiation directly impacts all keratinocytes populations. Despite the insightful information this analysis provided, it was yet unclear how each keratinocyte population varied before, during, and after shining blue light on the skin. Thus, a simulation (Figure 5) was executed for the blue light treatment of a lesional skin area of 1 mm&#178; for 84 days, using a fluence of 90 Jcm&#8315;&#178;. The simulated scheme was divided into two sections, the first one with everyday treatment, and the second one with three times per week irradiations. The time evolution of both healthy and

<a id='099ccd7c-a6a9-4ded-9ae4-0a0038b1af2b'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='8bb843b5-6f93-4b31-a5de-ea5d8a1004e2'></a>

8

<a id='05a8f877-8e58-4176-80bd-9387940e9947'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='7df84c71-8826-4afd-b52a-a9a25626f2aa'></a>

Félix Garza et al.

<a id='8357e507-09c8-4406-a213-51d00f1bfa18'></a>

Dynamic Model of Blue Light Treatment

<a id='903444f4-b654-448c-bea9-ae4d713880da'></a>

Direct impact of blue light on proliferative compartment parameters
<::Multi-panel chart showing the direct impact of blue light on proliferative compartment parameters. The chart consists of 8 panels (A-H), each labeled "Case 1" through "Case 8". Each panel contains two sub-plots: an upper plot showing "Rate (days⁻¹)" on the y-axis (ranging from 0 to 3) against "Time (days)" on the x-axis (log scale from 10⁰ to 10³), and a lower plot also showing "Rate (days⁻¹)" on the y-axis (ranging from 0 to 100) against "Time (days)" on the x-axis (log scale from 10⁰ to 10³). Various colored lines representing different parameters are plotted in both sub-plots.::>
Direct impact of blue light on non-proliferative compartment parameters
Impact of blue light on parameters from both the proliferative and non-proliferative compartments
<::Multi-panel chart showing the impact of blue light on parameters from both the proliferative and non-proliferative compartments. The chart consists of 5 panels (I-M), each labeled "Case 9" through "Case 13". Each panel contains two sub-plots: an upper plot showing "Rate (days⁻¹)" on the y-axis (ranging from 0 to 3) against "Time (days)" on the x-axis (log scale from 10⁰ to 10³), and a lower plot also showing "Rate (days⁻¹)" on the y-axis (ranging from 0 to 100) against "Time (days)" on the x-axis (log scale from 10⁰ to 10³). Various colored lines representing different parameters are plotted in both sub-plots. This set of panels (I-M) shares a common legend with panels A-H, located below panel M. The legend is as follows:

Proliferation and differentiation rates
- γ₁h (light blue line)
- γ₁d (dark blue line)
- γ₂h (purple line)
- γ₂d (dark purple line)
- K₁sh (light green line)
- K₁sd (dark green line)
- K₁ah (orange line)
- K₁ad (dark orange line)
- K₂sh (light red line)
- K₂sd (dark red line)
- K₂ah (yellow line)
- K₂ad (dark yellow line)
- K₃h (pink line)
- K₃d (dark pink line)
- K₄ah (brown line)
- K₄d (dark brown line)
- K₅h (gray line)

--- General Rates Legend ---
- Proliferation (green line)
- Differentiation (blue line)
- Cytotoxicity (red line)
::>


<a id='b1741d12-b2d7-4864-b18d-219bf0e1761c'></a>

FIGURE 2 | Representing in silico the blue light effect by decreasing the proliferation rate of keratinocytes yields the behavior observed experimentally. The panels show the changes on the proliferation and differentiation of healthy and diseased keratinocytes due to different approaches of blue light in silico representation. Thirteen different cases are depicted in this figure. A detailed description of each case can be found in Table 4. These cases are grouped according to the parameters affected by blue light. Panels (A–G) show cases where only the proliferation and division parameters from the proliferative compartment are modified during blue light irradiation. Panel (H) presents the case where only the differentiation parameters from the non-proliferative compartment are affected. Panels (I–M) described the cases where blue light irradiation impacts both compartments. The upper plots of each panel show the impact of the blue light factor on the proliferation and differentiation rates of all keratinocyte populations as a consequence of the parameters affected by blue light. The lower panels display the impact of each potential representation on the proliferative (green), differentiation (blue), and immune system-cytotoxic (red) capacities.

<a id='84c86a2b-bf39-41b9-9e70-22807e7a3a2b'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='24309ede-956f-43da-8ad2-13db9367f2ff'></a>

9

<a id='2824192b-2751-4637-9428-ebaf8f9768a6'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='d3870900-bcba-4235-acc0-4b6b39a3b13a'></a>

Félix Garza et al.

<a id='c9d2ac34-5a80-4a25-9703-2c1a5f40471e'></a>

Dynamic Model of Blue Light Treatment

<a id='9cd1f62e-e416-4531-80fc-02cc3ded9efc'></a>

<::chart: A two-panel figure showing BLISS model data compared to in vitro and in vivo experimental data. FIGURE 3 | BLISS accurately describes in vitro and in vivo data. (A) The relative keratinocyte density is computed (solid black line) for irradiation schemes with fluences between 0 and 100 Jcm⁻² and compared to the experimental data (Liebmann et al., 2010) of keratinocytes irradiated with three fluences of continuous wave blue light (gray dot). The chart shows 'Dose (Jcm⁻²)' on the x-axis from 0 to 100 and 'Relative cell number' on the y-axis from 0 to 1. A legend indicates 'In vitro data' with gray dots and 'In silico data' with a solid black line. The black line shows a decreasing trend from 1 at 0 Jcm⁻² to approximately 0.45 at 100 Jcm⁻², with gray dots and error bars plotted near the line. (B) The changes in the severity of a psoriasis lesion during (blue bar) and after treatment (black bar) are predicted (solid lines) for a pulsed wave treatment at high (red) and low (blue) intensities. These changes in the severity of the disease are shown in terms of the local psoriasis severity index (LPSI). The in silico results are compared to the clinical data (dots) of Pfaff et al. (2015). The chart shows 'Time (weeks)' on the x-axis from 0 to 16 and 'Local Psoriasis Severity Index (LPSI)' on the y-axis from 0 to 10. A legend indicates 'Low peak intensity in vivo' (blue dots), 'Low peak intensity in silico' (solid blue line), 'High peak intensity in vivo' (red dots), and 'High peak intensity in silico' (solid red line). Both sets of data show a decrease in LPSI over the 'Blue light treatment' period (0-12 weeks, marked by a blue bar below the x-axis), followed by a slight increase during the 'After treatment' period (12-16 weeks, marked by a black bar below the x-axis). A vertical dashed line is present at 12 weeks.::>

<a id='d34f8966-3b15-4569-aa91-b1bed0fd448c'></a>

diseased keratinocytes is depicted in Figures 5A,B respectively.
The model predicted that the cell density of all keratinocyte
populations decreases due to the repetitive irradiation with
blue light. However, the cell density of diseased keratinocytes
remained considerably high after the treatment compared to
the cell density of healthy keratinocytes. Thus, no shift to a
healthy phenotype was achieved by this therapeutic approach.
The model suggested that a lesional state may prevail after the
treatment, but some improvements might be observed within
the period of phototherapy. Additionally, it predicted that a less
pronounced decrease in the cell density of all keratinocytes is
achieved when the treatment occurs every other day compared
to daily treatment. This observation suggests that the longer the
period of daily treatment the lower the final LPSI value.

<a id='040cf951-6bb5-4e38-8011-c8d6619cee96'></a>

## Blue Light Treatment Schemes with Long Duration and High Fluence Yield High Efficacy in the Management of Psoriasis
Hitherto, the model predicted that regulating the hyper-proliferative populations of keratinocytes induces a transient management of psoriasis. However, it also showed that the treatment scheme used in the simulations has a direct impact in the predicted outcome. This observation agrees with the large variations perceived in the results from the available clinical investigations (Maari et al., 2003; Weinstabl et al., 2011; Kleinpenning et al., 2012; Pfaff et al., 2015). Therefore, we studied the impact of each treatment parameter on the efficacy of the therapeutic approach. Figure 5B shows a prominent decrease in the cell densities of diseased keratinocytes when the blue light is constantly shinned upon the skin compared to when the irradiation is less frequent. To further analyze this observation, simulations were executed for therapy schemes with a total duration of 4–28 weeks, using either a daily or every other day treatment (Figure 6A). The results showed that the longer

<a id='70e1bfbf-3104-465b-a1cd-f4b5ed791266'></a>

the period of daily treatment the lower the final LPSI value.
Nevertheless, the relative change in the LPSI value decreased for
treatment periods longer than 20 weeks. Further, BLISS predicted
that for a blue light phototherapy scheme where both daily and
every other day treatment sessions are used, higher efficacy is
achieved with an increasing number of daily treatment sessions.

<a id='18afd8b0-1e04-46c6-8e29-048db0380902'></a>

Given that repeated treatment sessions seemed to yield higher efficacy, we then tested whether the same trend applied to the irradiation mode of treatment scheme. As previously mentioned a given fluence of blue light can be shinned on the skin in either a continuous or pulsed mode. Both cases comprise the same average intensity, however the peak intensity differs. Pfaff et al. studied in vivo the impact of low and high peak intensities in the pulsed irradiation of psoriatic skin (Pfaff et al., 2015). They observed minor differences between low and high peak intensity groups; however this trend was not seen in silico (Figure 3B solid lines vs. dots). In the model, both low and high intensity pulsed treatment led to the same trend. These results led to questioning whether the model could predict a different outcome for treatment strategies with pulsed and continuous irradiation. Thus, simulations were implemented for low and high power densities in pulsed and continuous modes (Figures 6B-D), considering a 12 weeks treatment and 4 weeks follow-up with an average fluence of 90 Jcm-2 and an average intensity of 50 mWcm-2 for both irradiation modes. Figure 6B compares the efficacy of pulsed and continuous mode in terms of the local psoriasis severity index. In the simulations for the pulsed mode, low (100 mWcm-2) and high (200mWcm-2) peak intensities were used. No differences were observed between both modes, or between low and high peak power densities. Hence, the model suggested that duration rather than intensity determines the efficacy of the treatment. This prediction was further tested by simulating the treatment of a psoriatic epidermis using power

<a id='1f961720-4197-40dd-babb-1a22a87d08ef'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='edceef5c-862d-4437-b183-5b36bf90c33c'></a>

10

<a id='b6143701-1852-448c-be49-57a5c11237b2'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='ea3457e3-6613-46c5-b8e6-3bde8caab28b'></a>

Félix Garza et al.

<a id='cc8d150f-3fed-4ff5-aca5-e1ad63a81e42'></a>

Dynamic Model of Blue Light Treatment

<a id='834cc40e-2c34-485f-873c-f7595180e2df'></a>

A<::Figure A: Heatmap showing sensitivity analysis of different parameters across keratinocyte populations in healthy and diseased states.Y-axis: Parameter (P_scmax, γ_1hom, γ_2h, K_3h, β_2h, P_schom, P_tahom, λ, ρ_ta, K_4d, γ_1d, γ_2d).X-axis: Keratinocyte population.Sub-X-axis (Healthy): Stem cell, Transit amplifying cell, Growth arrested cell, Spinous cell, Granular cell, Corneocyte cell.Sub-X-axis (Diseased): Stem cell, Transit amplifying cell, Growth arrested cell, Spinous cell, Granular cell, Corneocyte cell.Color bar: 0 (blue) to 1 (red), indicating sensitivity values.: heatmap::>B<::Figure B: Bar chart showing the sensitivity of Local Psoriasis Severity Index (LPSI) to various parameters.Y-axis: Sensitivity of Local Psoriasis Severity Index (LPSI) (0 to 1).X-axis: Parameter (γ_2h, K_3h, β_2h, P_tahom, ρ_TA, K_4d, γ_2d).: bar chart::>

<a id='8df08258-2bd2-4127-96fd-d7875eee7935'></a>

FIGURE 4 | Multiple parameter sensitivity shows that variations in the proliferation parameters have a high impact on the final keratinocyte cell densities and the local severity of psoriasis at the end of treatment. (A) The sensitivity of healthy and diseased keratinocytes (x axis) to variations in the 58 model parameters (y axis) is depicted in the heat map. Only those with a Kolmogorov–Smirnov statistic value higher than 0.3 are shown in the y axis. (B) The sensitivity of the treatment outcome to changes in the same model parameters of Panel (A) are shown in the bar plot in terms of the local psoriasis severity index. Only those parameters with a Kolmogorov–Smirnov statistic value higher than 0.3 are shown in the x axis.

<a id='1e3abe95-8e67-4819-8831-9040052c32db'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='6c163888-5a87-46ca-a2b9-9cf51b4d9298'></a>

11

<a id='cdb29bb7-482e-4088-892a-47cc508a7118'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='ff9d8650-183a-4e39-8e16-85a9f95e358b'></a>

Félix Garza et al.

<a id='84dfac41-be0f-4727-8b3c-90b44139b06d'></a>

Dynamic Model of Blue Light Treatment

<a id='7b24e369-58c6-4080-a876-7fd3e3cbfe76'></a>

<::chart: FIGURE 5 | Blue light induces a temporary reduction of all keratinocyte populations during the length of the treatment. (A) The time evolution of the healthy keratinocyte cell densities (dashed lines) comprised in a psoriatic epidermis are described during (blue bar) and after (black bar) blue light-based therapy. (B) Similarly, the time evolution of the diseased keratinocytes (continuous lines) is shown during and after treatment. Note the difference in scales of the y-axes between panels (A) and (B). In this simulation, the treatment periods divided into two sections. The first one consists of 28 days, with irradiation sessions occurring every day. The second section comprises 56 days, with treatment sessions happening three times per week. On each session a fluence of 90 Jcm⁻² is applied for 30 min. Chart (A) shows the cell density (mm⁻²) scaled by x10² over Time (days) for healthy keratinocytes. The legend includes: Corneocyte, Granular cell, Spinous cell, Growth arrested cell, Transit amplifying cell, and Stem cell, all represented by dashed lines. The x-axis timeline is marked with 'Blue light treatment' (blue bar) and 'After treatment' (black bar). Chart (B) shows the cell density (mm⁻²) scaled by x10⁴ over Time (days) for diseased keratinocytes. The legend includes: Corneocyte, Granular cell, Spinous cell, Growth arrested cell, Transit amplifying cell, and Stem cell, all represented by continuous lines. The x-axis timeline is marked with 'Blue light treatment' (blue bar) and 'After treatment' (black bar).::>

<a id='c89d1677-a1f0-47eb-914f-edf82224dc37'></a>

densities of 100, 200, and 600 mWcm-2 in the continuous mode (Figures 6C,D).

<a id='36ddadeb-d7c5-46d4-ace6-8a42aa2c1937'></a>

In addition to time and intensity, fluence is another important parameter of the treatment scheme. Simulations performed for fluences between 0 and 750 Jcm⁻², considering a treatment of 12 weeks (Figure 7A) predicted that fluence levels as low as 45 Jcm⁻² lead to a decrease in the LPSI value. Moreover, at fluence levels between 200 and 500 Jcm⁻² a saturation point was observed. At fluences equal or higher than 500 Jcm⁻² the decrease in the LPSI value was considerably larger due to the cytotoxicity induced by BL at these levels. According to these results, low fluences would lead to a minor decrease in the LPSI compared to higher fluences. This observation is better understood when analyzing the relation between the fluence, the blue light factor θBL_Y, and the consequent proliferation rate derived by the model (Figure 7B). Here, we show only the analysis for the proliferation rate of diseased transit amplifying cells, but the trends are consistent for the other proliferative populations. A clear exponential decrease is seen on both the blue light factor and the proliferation rate with increasing fluences. However, the impact of fluence on the proliferation rate is steeper and faster compared to the effect on the blue light factor. Further, for fluences below 500 Jcm⁻² both the blue light factor and the proliferation rate are reduce in an almost linear manner. But it is less abrupt at fluences above 200 Jcm⁻². The fluence effect translates into a linear reduction of the proliferation in relation to the blue light factor, which yields a lower cell density and

<a id='b04fec20-ca3c-4121-b351-ef7e5c41c7cc'></a>

the consequent improvement on the psoriatic skin. The model was designed to allow bi-stability at either a diseased or healthy phenotype. The healthy state can only be reached when the total cell density at the end of treatment is dominated by healthy keratinocyte populations. To achieve the switch in the ruling type of population, the number of diseased cells must be considerably lowered during the treatment. Our results showed that this shift in phenotypes could not be acquired with blue light fluences where no cytotoxicity was induced (Figures 7C,D). Figure 7C presents the relation between healthy and diseased stem cells with increasing fluence levels. From this figure is clear that only fluences above 500 Jcm-2 achieve a majority of healthy stem cells. Fluences below that level reduce the cell densities but remain within the diseased state due to a high predominance of diseased keratinocytes (Figure 7D).

<a id='f3968bd7-2d82-48cb-95c5-d9dbb3d933fa'></a>

# DISCUSSION

Blue light at 420 and 453 nm is highly effective in the management of psoriasis (Weinstabl et al., 2011; Pfaff et al., 2015) without any adverse effects (Awakowicz et al., 2009; Kleinpenning et al., 2010). We have explored the underlying mechanism of this therapeutic method and the impact of the treatment scheme on the efficacy of the treatment using an *in silico* approach. BLISS suggests that the decrease in the keratinocytes proliferative capacity is sufficient to induce a transient decrease in the severity of psoriasis. Further,

<a id='e611e327-3080-4026-ab43-9a423bccd8cb'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='bdf05118-d248-41f6-8cea-808fb35dbb24'></a>

12

<a id='3bcad537-4266-48e6-9554-6a9e525e5490'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='d44f19fd-bb5f-4973-9b60-30af396d0fb8'></a>

Félix Garza et al.

<a id='cdaa0ef6-8541-4f87-b340-9110796fd69e'></a>

Dynamic Model of Blue Light Treatment

<a id='2f5851f1-06b1-4f88-b894-536ec2eff1d1'></a>

FIGURE 6 | The length of treatment is a key factor to achieve high treatment efficacy. (A) The LPSI at the end of treatment is predicted for treatment protocols with a total duration of 4–28 weeks. The treatment sessions in the simulated protocols occur either on a daily (blue dots) or every other day (green dots) basis. The plot shows Local Psoriasis Severity Index (LPSI) on the y-axis ranging from 0 to 10, and Time (weeks) on the x-axis ranging from 0 to 28. A legend indicates 'Treatment scheme: 3 sessions/week' represented by green dots and '7 sessions/week' by blue dots. Both show a decrease in LPSI over time, with 7 sessions/week generally yielding lower LPSI values. (B) A 12 weeks treatment with fluence of 90 Jcm⁻² is simulated for continuous (black) and pulsed irradiation with low (blue) and high (red) peak intensities. This bar chart displays Local Psoriasis Severity Index (LPSI) on the y-axis (0-10) and Time (weeks) on the x-axis (0-16). The x-axis is segmented into 'Blue light treatment' (0-12 weeks) and 'After treatment' (from 12 weeks onwards, marked by a dashed vertical line). The legend shows 'Low peak intensity' (blue bars), 'High peak intensity' (red bars), and 'Continuous irradiation' (black bars). LPSI values are shown at weeks 0, 2, 4, 8, 12, and 16. (C) The variation in the LPSI value is predicted for irradiation schemes with low and high intensities of continuous wave blue light. This bar chart shows Local Psoriasis Severity Index (LPSI) on the y-axis (0-10) and Time (weeks) on the x-axis (0-12), labeled 'Blue light treatment'. The legend indicates different intensities: '100 mWcm⁻²' (black bars), '200 mWcm⁻²' (gray bars), and '600 mWcm⁻²' (white bars with black outline). LPSI values are shown at weeks 0, 2, 4, 8, and 12 for each intensity. (D) The evolution of the total keratinocyte cell densities during (blue bar) and after (black bar) treatment are derived using the same low and high intensities of continuous wave blue light presented in panel (C). This line graph shows Cell density (mm⁻²) x10⁴ on the y-axis (0-8) and Time (days) on the x-axis (0-800). The x-axis is marked with a 'Blue light treatment' bar (approx. 0-100 days) and an 'After treatment' bar (approx. 100-800 days), separated by a dashed vertical line. A comprehensive legend at the bottom details the cell types (Stem Cell, Transit Amplifying Cell, Growth Arrested Cell, Spinous Cell, Granular Cell, Corneocyte) and their corresponding line styles for each of the three intensities (100 mWcm⁻², 200 mWcm⁻², 600 mWcm⁻²). For instance, Growth Arrested Cell is represented by solid lines (blue for 100 mWcm⁻², green for 200 mWcm⁻², red for 600 mWcm⁻²). The plot shows the density of various cell types changing over time, with some decreasing during treatment and then recovering or stabilizing afterwards.

<a id='75c20fdc-7f52-43b6-ae99-b529b1d882cb'></a>

it predicts that treatment schemes with long duration and
high fluence yield the most optimal outcome. The model
constitutes a fast and flexible tool that considers not only
the properties of the irradiated epidermis but also the
interactions between the structural cells within it. Our *in*
*silico* method provides a framework for further insight on the
underlying mechanism of this blue light-based phototherapy
and the optimal treatment of psoriasis. To the extent of our
knowledge, this is the first model that studies the changes
induced by blue light irradiation on the cell dynamics of
keratinocytes. The general concepts of epidermal kinetics used
here have been applied to UV phototherapy (Grabe and Neuber,
2007; Weatherhead et al., 2011; Zhang et al., 2015) before.
Nevertheless, the differences on the underlying mechanism
make the previous models and ours two utterly different
applications.

<a id='ba3ab79e-ae9d-4580-9153-e95b8e0f5e28'></a>

On this work, we first addressed how to best represent these phenomenological observations in silico while accounting for the characteristic phenotype of psoriasis (Perera et al., 2012). From experimental studies, it is known that blue light decreases the proliferative capacity of keratinocytes and other cell types (Taoufik et al., 2008; Wataha et al., 2008), and that it reduces their proliferation by inducing their differentiation (Liebmann et al., 2010). However, it is not clear how exactly these changes are exerted on the cellular processes of keratinocytes. BLISS accounts for the three main theories of cell division (Clayton et al., 2007; Klein et al., 2011; Watt, 2014), i.e., self-proliferation, asymmetric, and symmetric division. Self-proliferation refers to the ability of a cell dividing into two daughter cells of the same kind. Asymmetric division considers that one proliferative cell divides intro one daughter cell of the same kind and one of the next differentiation stage. Finally,

<a id='dcb2931b-bbe0-422e-a39d-260a8fb9cb78'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='aea4bc24-b0a0-49b3-b4ae-1efbe35d5a08'></a>

13

<a id='7d701b09-cc9e-4ec5-af14-939c70fe1316'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='43b784d0-5053-4eb7-804a-feb01fb35af7'></a>

Félix Garza et al.

<a id='3acde976-ddae-464b-847b-94ef512a4031'></a>

Dynamic Model of Blue Light Treatment

<a id='58689066-0446-4136-b055-363de16679c0'></a>

<::figure: FIGURE 7 | High fluences of blue light yield higher management of psoriasis than low fluences. (A) Bar chart titled "Blue light treatment" showing Local Psoriasis Severity Index (LPSI) on the y-axis (from 0 to 10) against Time (weeks) on the x-axis (0, 2, 4, 8, 12). The bars represent different fluences in Jcm⁻²: 0, 45, 90, 250, 300, 350, 400, 450, 500, 650, 750, 800. The LPSI generally decreases over time with blue light treatment, especially at higher fluences. (B) A 3D plot showing Blue light factor θ_BLγ on the y-axis (from 0 to 1), Proliferation rate (days⁻¹) on one x-axis (from 0.05 to 0.01), and Fluence (Jcm⁻²) on the other x-axis (from 0 to 1000). A curved surface illustrates the relationship between these three variables. (C) A log-log plot evaluating the bi-stability of the model. The y-axis is log₁₀ (Healthy stem cells) and the x-axis is log₁₀ (Diseased stem cells). Multiple colored lines represent different fluences (0, 100, 200, 300, 400, 500, 600, 700, 800 Jcm⁻²). The plot shows two distinct regions labeled "Healthy state" and "Diseased state", with a "starting point" indicated in the diseased state. Curves for higher fluences show a shift towards the healthy state. (D) A zoomed-in log-log plot focusing on the "Diseased state" region. The y-axis is log₁₀ (Healthy stem cells) (from 10^2.52 to 10^2.56) and the x-axis is log₁₀ (Diseased stem cells) (from 10^3.7 to 10^3.8). Multiple colored lines represent different fluences (0, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450 Jcm⁻²). All curves in this plot remain within the "Diseased state" region, starting from a "starting point". (A) The LPSI over time is computed for a 12 weeks continuous wave treatment with an initial LPSI of 5.17 (Pfaff et al., 2015) using 11 fluences. (B) The behavior of the blue light factor θBLγ and the proliferation rate are visualized as functions of the fluence. (C) The bi-stability of the model is evaluated in the logarithmic scale for a wide range of fluences in a phase diagram of healthy and diseased keratinocytes. Only fluences above 500 Jcm⁻² yield a shift the dominant keratinocyte population and the phenotype of the skin. (D) Fluences below this level remain in the disease state.::>

<a id='3eb49980-41c8-4093-a322-833903ed080d'></a>

symmetric division comprises the division of a proliferative cell into two cells of the next differentiation stage. In the model the proliferation and differentiation of keratinocytes in the proliferative compartment is represented by their self-proliferation, symmetric, and asymmetric division parameters. The keen reader could think that in order to best describe the effect of blue light on proliferation and differentiation, increasing the rates of asymmetric and symmetric division should be enough to achieve similar observations as those reported in vitro. Alternatively, the direct increase on the division rates of proliferative cells should be coupled to the decrease of the self-proliferation rate of all keratinocytes in the proliferative compartment. Thus, capturing the increase in differentiation and the decrease in proliferation of the irradiated keratinocytes. Our analysis (Figure 2) showed that modifying the division rates alone does not appropriately reflect on the proliferative capacity of the cells. Additionally, it translates into high peaks in the cell density of transit amplifying and non-proliferative cells, which are biologically unlikely. However, decreasing only the proliferation rate does yield the effect on the differentiation and proliferative capacity of keratinocytes observed experimentally. The outcome of this approach is a transient decline in the proliferative rates of the cells and consequent higher differentiation, translated into a temporary drop local severity of the disease. BLISS comprises a fine tuning

<a id='dd541c32-0081-4043-b16f-0e9a83eb557c'></a>

between the proliferation and division rates of all keratinocytes, particularly of healthy stem cells. It considers a strong connection between the proliferation and division rates of healthy stem cells and their regulation by the total population of healthy and diseased transit amplifying cells. This fact might explain the outcome of our analysis. From the sensitivity analysis (Figure 4), it was clear that proliferation-related parameters had the highest influence on the final cell densities and the improvement of psoriasis due to blue light treatment. The most sensitive parameters were directly related to the treatment scheme. Their impact was reflected on the cell density of diseased keratinocyte populations and local psoriasis severity index. These observations may explain the large variations observed among clinical investigations of BL treatment (Maari et al., 2003; Weinstabl et al., 2011; Pfaff et al., 2015).

<a id='c69ea40d-cda8-4e5e-89aa-cd14933fc169'></a>

Previous models of phototherapy, particularly UV-based approaches represented the therapeutic effect by inducing strong apoptosis on the keratinocytes (Weatherhead et al., 2013; Zhang et al., 2015). This temporal increase in the apoptotic rate leads to a remission phase, characterized by a lower total cell density after the treatment compared to the initial one. In our model, apoptosis is only affected at fluences above 500 Jcm-2, instead the proliferation and differentiation capacity of keratinocytes are altered during the treatment sessions. The key difference in the approaches of representing UV and BL phototherapy in silico

<a id='6974d5f4-71e8-4eaa-9793-d0d7b1c616d5'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='62326f00-36f4-4484-bf01-65fb5fb64145'></a>

14

<a id='9eca2823-f504-4cbe-8456-a641177834d9'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='98a3318b-06aa-4620-91eb-25afe220a418'></a>

Félix Garza et al.

<a id='0035be28-b250-4f0c-86a1-f7181c7e1790'></a>

Dynamic Model of Blue Light Treatment

<a id='ac630ddc-b083-442e-aee6-f5d23eed52ad'></a>

is defined by the difference in the underlying mechanisms of both therapeutic approaches. Despite both methods affecting the cells behavior by absorption of light at a certain wavelength, the photo-acceptors and consequent events differ. UV is mainly absorbed by the cell's DNA (Benedix et al., 2005), consequently inducing direct DNA damage, apoptosis (Weatherhead et al., 2011), and a decrease in the total cell density of the lesional skin. Blue light irradiation does not induce DNA damage (Awakowicz et al., 2009), it is absorbed by other photo-acceptors in the cell, e.g., flavins (Sadeghian et al., 2008) and cryptochromes (Bouly et al., 2007). The consequent effect is the release of nitric oxide (Opländer et al., 2013) and reactive oxygen species (Yoshida et al., 2013), which alter the cell's proliferation and differentiation rates.

<a id='748096b9-b859-4b13-8567-eef06b4cc57d'></a>

Clinically, this transient effect on the keratinocytes
proliferation and differentiation is observed as the improvement
of a psoriatic lesion (Weinstabl et al., 2011; Kleinpenning et al.,
2012). The model is bi-stable, thus it can reproduce steady
states for both healthy and diseased skin phenotypes. In our
simulations, we account for mild psoriasis through a specific
set of initial cell densities and show that although the plaque
is controlled during the treatment the underlying state is still
diseased. After the treatment, the model eventually goes back
to the initial diseased state. In the UV phototherapy model of
Zhang et al. (2015), they demonstrate that UV treatment with
consecutive episodes can theoretically control the disease and
achieve a remission of the psoriatic phenotype. In our model,
we do not observed this remission phase for mild psoriasis
considered with fluences below 500 Jcm-2.The lack of remission
phase in our simulations for blue light treatment in contrast with
UV phototherapy may be due to the underlying mechanism.
Increasing the apoptosis of keratinocytes yields a lower cell
density regardless of their proliferation and differentiation
rate. This effect results in a shift of the stem cell density from
the disease state to the healthy state (Figure 7C). Altering
the proliferation and differentiation rates of the proliferative
keratinocytes due to blue light irradiation only impacts their
apoptosis rates at high fluence levels. Thus, the effect of blue
light is mild compared to that of UV (Weatherhead et al., 2013).
Nevertheless, it is possible that other factors are involved in the
underlying mechanism of blue light management of psoriasis.
The inclusion of these factors in the model could potentially
yield to the shift in phenotypes and full remission of psoriatic
skin. In our method, the immune system regulates the dynamics
of the keratinocytes through the removal of disease stem cells
at a rate defined by the maximum immune killing rate and the
half activation of the immune system (Equation 7). Blue light
also induces apoptosis of T-cells (Liebmann et al., 2010; Oh
et al., 2016), alter the immune response (Fischer et al., 2013)
and decrease inflammation (Shnitkind et al., 2006). However,
the impact of BL on the immune system is not considered in
the current model. The inclusion of blue light related effects
on the immune system might result in lower keratinocyte
cell densities and the consequent shift in the phenotype. The
available clinical investigations have not assessed yet the impact
of blue light on the immune system in the context of psoriasis.
Data from skin biopsies, experimental, and clinical studies on
blue light irradiation is needed to determine which aspects

<a id='016251b6-27af-4fae-9d6c-5b9895fbba69'></a>

could be involved and how they should be included in the model.

<a id='8d2970dd-e6b8-457e-9209-b63c6d47523a'></a>

BLISS explicitly includes relevant treatment parameters, i.e., fluence, time, intensity, and mode of irradiation. This feature of the model allows us to investigate the influence of these parameters on the management of psoriasis. Recent experimental studies have explored the effect of various wavelengths on the blue range of the electromagnetic spectrum (Liebmann et al., 2010; Opländer et al., 2013), and fluence on various cell types (Awakowicz et al., 2009; Liebmann et al., 2010; Sparsa et al., 2010; Monfrecola et al., 2014). Clinically, the limited number of available studies focuses on the assessment of treatment efficacy with a specific combination of parameters. Only two studies implements a wavelength comparison (Weinstabl et al., 2011; Kleinpenning et al., 2012), and another evaluates high and low pulsed intensities (Pfaff et al., 2015). Nevertheless, no global guidelines for treatment have been defined. Furthermore, the impact on the kinetics of the main cells involved in psoriasis and their role on the management of the disease are yet to be resolved.
One of the objectives of this study was to study the impact of treatment parameters on the blue light mediated regulation of keratinocytes in psoriasis and the consequent control of the lesion. Our results suggested that therapy length and the applied fluence rather than intensity of irradiation may potentially determine the efficacy of the treatment. Simulations for various treatment lengths (Figure 6A) showed that algorithms with a long treatment period and consecutive episodes may be the most effective for psoriasis. This observation could partially explain the higher improvement of Pv symptoms achieved by Pfaff et al. (2015) (12 weeks) in contrast with prior investigations (4 weeks; Maari et al., 2003; Weinstabl et al., 2011). Another reason could be the different fluences used in these studies [10 Jcm-2 (Maari et al., 2003) and 90 Jcm-2 (Weinstabl et al., 2011; Pfaff et al., 2015)], given the fluence dependency associated with blue light irradiation (Liebmann et al., 2010; Dai et al., 2012). Simulations implemented for a wide range of fluences (Figure 7) show a negative correlation between fluence and final LPSI value. However, no threshold value has yet been defined. To define this value additional in vitro and in vivo data are needed. Research on light therapy for different applications has indicated that pulsed light is more effective than continuous light, while others report no effect, or a worsening effect of pulsed irradiation compared to no treatment (Lapchak et al., 2007; Hashmi et al., 2010). In Psoriasis, only one clinical investigation has used a pulsed irradiation mode (Pfaff et al., 2015), while the others employed the continuous mode (Maari et al., 2003; Weinstabl et al., 2011; Kleinpenning et al., 2012). Simulations performed with the model (Figure 6B) indicated that pulsed light is as effective as continuous light in the treatment of psoriasis.

<a id='57e728dd-4820-4fea-8ef0-3eb889db1cfd'></a>

The current model has some addressable limitations: (i)
it does not explicitly comprise the photo-activated processes
leading to the cellular regulation and management of psoriasis.
(ii) We neglected the additional cytotoxicity induced on the
keratinocytes at wavelengths shorter than 453 nm (Liebmann
et al., 2010). The model was built assuming irradiation at
453 nm, which is the most common wavelength used for
psoriasis (Weinstabl et al., 2011; Pfaff et al., 2015). Despite

<a id='a7e6c555-7d11-4679-ae4e-829f6281d7f1'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='fb8bd509-8128-401d-b3c8-8282788f1e51'></a>

15

<a id='0a0ccfd3-22ef-48ea-a0a1-75fb1702b546'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='746a5f91-3c83-4791-900b-dd89e41d30cd'></a>

Félix Garza et al.

<a id='0a619b11-ae6c-439e-94f2-a4b2e963149f'></a>

Dynamic Model of Blue Light Treatment

<a id='0fbc524a-ac1c-4c75-a2e9-20b15b21ac37'></a>

the minimum differences in treatment efficacy reported in the
literature (Kleinpenning et al., 2010; Weinstabl et al., 2011),
inclusion of this effect could be worth a thorough analysis.
However, additional data is needed on the optical parameters and
the skin before this feature can be included in the model.

<a id='3250a21d-1753-4b2c-94c9-82425e8c82cb'></a>

One definite experimental test of our model should aim at simultaneously tracing psoriasis and healthy proliferative and non-proliferative keratinocytes to verify whether blue light equally affects healthy and diseased proliferative cells. One potential approach to test this hypothesis could be isolating keratinocytes from psoriatic skin (Aasen and Belmonte, 2010) after shinning blue light on it. In this work, we provide general insights and recommendations based on the model results. In the future, more precise recommendations could be derived from the model by implementing an optimization analysis for the treatment (Kessel et al., 2013). Our results showed that length of treatment is vital in decreasing the severity of a psoriasis lesion, however there is little information reported in the literature on the direct effect of irradiation length and cumulative exposure of cells to blue light. Future studies should explore this theory experimentally to define the boundaries of the cellular response and the most optimal outcome. Also, they should assess the long term management of psoriasis and the recurrence of the lesions.

<a id='ecfa1ac9-b91a-4389-938c-24f03c2b7b3e'></a>

# CONCLUSIONS
Overall, this study demonstrates that regulation of the proliferative capacity of keratinocytes is a crucial process in

<a id='ed84d929-8a38-4084-a5fc-4300776532d3'></a>

## REFERENCES
Aasen, T., and Belmonte, J. C. I. (2010). Isolation and cultivation of human
keratinocytes from skin or plucked hair for the generation of induced
pluripotent stem cells. Nat. Protoc. 5, 371-382. doi: 10.1038/nprot.2009.241
Awakowicz, P., Bibinov, N., Born, M., Busse, B., Gesche, R., Helmke,
A., et al. (2009). Biological stimulation of the human skin applying
healthpromoting light and plasma sources. Contrib. Plasma Phys. 49, 641-647.
doi: 10.1002/ctpp.200910068

<a id='18e31637-46ad-478d-ac3d-828ff29fad2a'></a>

Bauer, J., Bahmer, F. A., Wörl, J., Neuhuber, W., Schuler, G., and Fartasch, M.
(2001). A strikingly constant ratio exists between Langerhans cells and other
epidermal cells in human skin. A stereologic study using the optical disector
method and the confocal laser scanning microscope. J. Invest. Dermatol. 116,
313-318. doi: 10.1046/j.1523-1747.2001.01247.x

<a id='6fcc946f-b9b5-4994-8728-de3eca55b25c'></a>

Benedix, F., Berneburg, M., and Röcken, M. (2005). Phototherapy with
narrowband vs broadband UVB. *Acta Derm. Venereol.* 85, 98–108.
doi: 10.1080/00015550510025579

<a id='70501501-c0ef-4a80-b975-fc6237c4df0b'></a>

Bouly, J.-P., Schleicher, E., Dionisio-Sese, M., Vandenbussche, F., Van Der Straeten,
D., Bakrim, N., et al. (2007). Cryptochrome blue light photoreceptors are
activated through interconversion of flavin redox states. J. Biol. Chem. 282,
9383-9391. doi: 10.1074/jbc.M609842200

<a id='ed6ff176-ecc3-43c6-8ddb-a35d171d1ca4'></a>

Chelliah, V., Juty, N., Ajmera, I., Ali, R., Dumousseau, M., Glont, M., et al.
(2015). BioModels: ten-year anniversary. Nucleic Acids Res. 43, D542-D548.
doi: 10.1093/nar/gku1181

<a id='4738f38c-125f-4193-9cc3-6e7f13a2770a'></a>

Clayton, E., Doupé, D. P., Klein, A. M., Winton, D. J., Simons, B. D., and Jones, P.
H. (2007). A single type of progenitor cell maintains normal epidermis. Nature
446, 185–189. doi: 10.1038/nature05574

<a id='29fdb7c7-cb9b-4023-88e2-67063dc300c6'></a>

Dai, T., Gupta, A., Murray, C. K., Vrahas, M. S., Tegos, G. P., and Hamblin, M. R. (2012). Blue light for infectious diseases: propionibacterium acnes, *Helicobacter pylori*, and beyond? *Drug Resist. Updat*. 15, 223–236. doi: 10.1016/j.drup.2012.07.001

<a id='cb11a6e5-68f0-41ad-889f-bddced5cc464'></a>

the blue light induced management of psoriasis. Considering the uprising interest in blue light as treatment for inflammatory skin conditions, the availability of irradiation guidelines becomes of great relevance. Our model constitutes a flexible tool for studying the underlying mechanism, formulating valuable recommendations, and designing effective therapeutic regimes with BL in a constraint-free environment.

<a id='89842b88-4f68-42e0-8693-4c6202bc4746'></a>

## AUTHOR CONTRIBUTIONS
Wrote the paper: ZCFG. Conceived and designed the computational framework: ZCFG, JL, MB, PAJH, NAWvR. Developed the model: ZCFG. Performed the computational analysis: ZCFG. Revised the paper: JL, MB, PAJH, NAWvR. Supervised the study: JL, MB, PAJH, NAWvR.

<a id='739f18e1-5abe-481a-97d6-69f7d2a68ef8'></a>

FUNDING

This project was funded under the public-private partnership between Philips and the Eindhoven University of Technology.

<a id='038c6fc4-1785-46b4-a938-0fdbd276a222'></a>

# ACKNOWLEDGMENTS

We are grateful to Elvira Paulussen for her contribution to the inclusion of optical parameters in the model. The model described here was deposited in the online repository BioModels Database (Chelliah et al., 2015) with identifier MODEL1701090001.

<a id='67096746-81ef-4266-aca9-c69d395e8902'></a>

Eichler, M., Lavi, R., Shainberg, A., and Lubart, R. (2005). Flavins are source of visible-light-induced free radical formation in cells. Lasers Surg. Med. 37, 314–319. doi: 10.1002/lsm.20239
Fischer, M. R., Abel, M., Lopez Kostka, S., Rudolph, B., Becker, D., and von Stebut, E. (2013). Blue light irradiation suppresses dendritic cells activation in vitro. Exp. Dermatol. 22, 558–560. doi: 10.1111/exd.12193
Gandolfi, A., Iannelli, M., and Marinoschi, G. (2011). An age-structured model of epidermis growth. J. Math. Biol. 62, 111–141. doi: 10.1007/s00285-010-0330-3
Grabe, N., and Neuber, K. (2007). Simulating psoriasis by altering transit amplifying cells. Bioinformatics 23, 1309–1312. doi: 10.1093/bioinformatics/btm042
Hashmi, J. T., Huang, Y.-Y., Sharma, S. K., Kurup, D. B., De Taboada, L., Carroll, J. D., et al. (2010). Effect of pulsing in low-level light therapy. Lasers Surg. Med. 42, 450–466. doi: 10.1002/lsm.20950
Heenen, M., Galand, P., de Maertelaer, V., and Heenen, P. H. (1987). Psoriasis: hyperproliferation cannot induce characteristic epidermal morphology. Cell Tissue Kinet. 20, 561–570. doi: 10.1111/j.1365-2184.1987.tb01365.x
Heenen, M., Thiriar, S., Noël, J. C., and Galand, P. (1998). Ki-67 immunostaining of normal human epidermis: comparison with 3H-thymidine labelling and PCNA immunostaining. Dermatol. Basel Switz. 197, 123–126. doi: 10.1159/000017982
Hoath, S. B., and Leahy, D. G. (2003). The organization of human epidermis: functional epidermal units and phi proportionality. J. Invest. Dermatol. 121, 1440–1446. doi: 10.1046/j.1523-1747.2003.12606.x
Kessel, K. A., Habermehl, D., Jäger, A., Floca, R. O., Zhang, L., Bendl, R., et al. (2013). Development and validation of automatic tools for interactive recurrence analysis in radiation therapy: optimization of treatment algorithms for locally advanced pancreatic cancer. Radiat. Oncol. Lond. Engl. 8:138. doi: 10.1186/1748-717X-8-138
Klein, A. M., Nikolaidou-Neokosmidou, V., Doupé, D. P., Jones, P. H., and Simons, B. D. (2011). Patterning as a signature of human epidermal stem cell regulation. J. R. Soc. Interface 8, 1815–1824. doi: 10.1098/rsif.2011.0240

<a id='16241f14-dbf5-49b0-9565-9b17245f9c2e'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='d32b3332-7157-4abb-809f-a5713f3526f0'></a>

16

<a id='b6862b1d-29f1-41fd-aecb-fc4ef3a6992e'></a>

January 2017 | Volume 8 | Article 28

<!-- PAGE BREAK -->

<a id='2598da88-3d93-492c-9524-42c2a2b8c6ef'></a>

Félix Garza et al.

<a id='c5cf7a85-d084-405a-90ce-8ce4ac9bdd95'></a>

Dynamic Model of Blue Light Treatment

<a id='39660289-e868-48f1-aa78-7eefe65f9009'></a>

Kleinpenning, M. M., Otero, M. E., van Erp, P. E. J., Gerritsen, M. J. P., and
van de Kerkhof, P. C. M. (2012). Efficacy of blue light vs. red light in the
treatment of psoriasis: a double-blind, randomized comparative study: blue
light versus red light in psoriasis. J. Eur. Acad. Dermatol. Venereol. 26, 219–225.
doi: 10.1111/j.1468-3083.2011.04039.x

<a id='e1d6de4c-b318-4949-93c4-c10334e87b9c'></a>

Kleinpenning, M. M., Smits, T., Frunt, M. H., van Erp, P. E., van de Kerkhof, P., and Gerritsen, R. M. (2010). Clinical and histological effects of blue light on normal skin. Photodermatol. Photoimmunol. Photomed. 26, 16-21. doi: 10.1111/j.1600-0781.2009.00474.x
Lapchak, P. A., Salgado, K. F., Chao, C. H., and Zivin, J. A. (2007). Transcranial near-infrared light therapy improves motor function following embolic strokes in rabbits: an extended therapeutic window study using continuous and pulse frequency delivery modes. Neuroscience 148, 907-914. doi: 10.1016/j.neuroscience.2007.07.002
Lee, C.-H., Wu, S.-B., Hong, C.-H., Yu, H.-S., and Wei, Y.-H. (2013). Molecular mechanisms of UV-induced apoptosis and its effects on skin residential cells: the implication in UV-based phototherapy. Int. J. Mol. Sci. 14, 6414-6435. doi: 10.3390/ijms14036414
Liebmann, J., Born, M., and Kolb-Bachofen, V. (2010). Blue-light irradiation regulates proliferation and differentiation in human skin cells. J. Invest. Dermatol. 130, 259-269. doi: 10.1038/jid.2009.194
Maari, C., Viau, G., and Bissonnette, R. (2003). Repeated exposure to blue light does not improve psoriasis. J. Am. Acad. Dermatol. 49, 55-58. doi: 10.1067/mjd.2003.445
Marino, S., Hogue, I. B., Ray, C. J., and Kirschner, D. E. (2008). A methodology for performing global uncertainty and sensitivity analysis in systems biology. J. Theor. Biol. 254, 178-196. doi: 10.1016/j.jtbi.2008.04.011
Markovitsi, D. (2016). UV-induced DNA damage: the role of electronic excited states. Photochem. Photobiol. 92, 45-51. doi: 10.1111/php.12533
Monfrecola, G., Lembo, S., Cantelli, M., Ciaglia, E., Scarpato, L., Fabbrocini, G., et al. (2014). The effect of visible blue light on the differentiation of dendritic cells in vitro. Biochimie 101, 252-255. doi: 10.1016/j.biochi.2014.02.001
Ng, C. M., Joshi, A., Dedrick, R. L., Garovoy, M. R., and Bauer, R. J. (2005). Pharmacokinetic-pharmacodynamic-efficacy analysis of efalizumab in patients with moderate to severe psoriasis. Pharm. Res. 22, 1088-1100. doi: 10.1007/s11095-005-5642-4
Oh, P.-S., Hwang, H., Jeong, H.-S., Kwon, J., Kim, H.-S., Kim, M., et al. (2016). Blue light emitting diode induces apoptosis in lymphoid cells by stimulating autophagy. Int. J. Biochem. Cell Biol. 70, 13-22. doi: 10.1016/j.biocel.2015.11.004
Opländer, C., Deck, A., Volkmar, C. M., Kirsch, M., Liebmann, J., Born, M., et al. (2013). Mechanism and biological relevance of blue-light (420-453nm)-induced nonenzymatic nitric oxide generation from photolabile nitric oxide derivates in human skin in vitro and in vivo. Free Radic. Biol. Med. 65, 1363-1377. doi: 10.1016/j.freeradbiomed.2013.09.022
Parisi, R., Symmons, D. P., Griffiths, C. E., Ashcroft, D. M., and Identification and Management of Psoriasis and Associated ComorbidiTy (IMPACT) project team (2013). Global epidemiology of psoriasis: a systematic review of incidence and prevalence. J. Invest. Dermatol. 133, 377-385. doi: 10.1038/jid.2012.339
Pathak, M. A. (1991). Ultraviolet radiation and the development of non-melanoma and melanoma skin cancer: clinical and experimental evidence. Skin Pharmacol. 4(Suppl. 1), 85-94.
Perera, G. K., Di Meglio, P., and Nestle, F. O. (2012). Psoriasis. Annu. Rev. Pathol. 7, 385-422. doi: 10.1146/annurev-pathol-011811-132448
Pfaff, S., Liebmann, J., Born, M., Merk, H. F., and von Felbert, V. (2015). Prospective randomized long-term study on the efficacy and safety of uv-free blue light for treating mild Psoriasis Vulgaris. Dermatology 231, 24-34. doi: 10.1159/000430495
Sadeghian, K., Bocola, M., and Schütz, M. (2008). A conclusive mechanism of the photoinduced reaction cascade in blue light using flavin photoreceptors. J. Am. Chem. Soc. 130, 12501-12513. doi: 10.1021/ja803726a

<a id='d8f6a2a9-748d-4d65-83c9-5c47067d1249'></a>

Savill, N. J. (2003). Mathematical models of hierarchically structured cell populations under equilibrium with application to the epidermis. _Cell Prolif._ 36, 1–26. doi: 10.1046/j.1365-2184.2003.00257.x

<a id='40b032c0-10bf-4f32-b075-6aa9e5773000'></a>

Schneider, L. A., Hinrichs, R., and Scharffetter-Kochanek, K. (2008).
Phototherapy and photochemotherapy. Clin. Dermatol. 26, 464-476.
doi: 10.1016/j.clindermatol.2007.11.004

<a id='f904fce5-b399-45a3-a802-efedd043da61'></a>

Shnitkind, E., Yaping, E., Geen, S., Shalita, A. R., and Lee, W.-L. (2006). Anti-inflammatory properties of narrow-band blue light. J. Drugs Dermatol. 5, 605–610.

<a id='34422e54-1285-4a42-8877-e56225461412'></a>

Simonart, T., Heenen, M., and Lejeune, O. (2010). Epidermal kinetic alterations required to generate the psoriatic phenotype: a reappraisal: kinetic alterations in psoriasis. Cell Prolif. 43, 321-325. doi: 10.1111/j.1365-2184.2010.00672.x

<a id='c4124eb0-cbbb-4407-87c2-1461c59689e5'></a>

Sparsa, A., Faucher, K., Sol, V., Durox, H., Boulinguez, S., Doffoel-Hantz, V.,
et al. (2010). Blue light is phototoxic for B16F10 murine melanoma and bovine
endothelial cell lines by direct cytocidal effect. Anticancer Res. 30, 143-147.

<a id='5b4ff49c-901a-4fb6-8a0c-91fc100b250c'></a>

Taoufik, K., Mavrogonatou, E., Eliades, T., Papagiannoulis, L., Eliades, G., and Kletsas, D. (2008). Effect of blue light on the proliferation of human gingival fibroblasts. *Dent. Mater.* 24, 895–900. doi: 10.1016/j.dental.2007.10.006

<a id='e95c3d6e-af43-4bbd-904c-594ff16bd377'></a>

van Gemert, M. J., Jacques, S. L., Sterenborg, H. J., and Star, W. M. (1989). Skin optics. _IEEE Trans. Biomed. Eng._ 36, 1146-1154. doi: 10.1109/10.42108

<a id='ef2e8a9c-0099-4de5-a755-16a28080c61e'></a>

Wataha, J. C., Lewis, J. B., Lockwood, P. E., Noda, M., Messer, R. L., and Hsu, S.
(2008). Response of THP-1 monocytes to blue light from dental curing lights. J.
Oral Rehabil. 35, 105-110. doi: 10.1111/j.1365-2842.2007.01806.x

<a id='b0a6ad81-ada0-48b1-a0be-08f621de237b'></a>

Watt, F. M. (2014). Mammalian skin cell biology: at the interface between laboratory and clinic. Science 346, 937-940. doi: 10.1126/science.1253734

<a id='5679b2b3-c252-4b24-aa65-8f84d7ceb95d'></a>

Weatherhead, S. C., Farr, P. M., Jamieson, D., Hallinan, J. S., Lloyd, J. J., Wipat,
A., et al. (2011). Keratinocyte apoptosis in epidermal remodeling and clearance
of psoriasis induced by UV radiation. J. Invest. Dermatol. 131, 1916–1926.
doi: 10.1038/jid.2011.134

<a id='f960af39-5359-4870-93b9-2635928190e8'></a>

Weatherhead, S. C., Farr, P. M., and Reynolds, N. J. (2013). Spectral effects of UV
on psoriasis. *Photochem. Photobiol. Sci.* 12, 47-53. doi: 10.1039/C2PP25116G

<a id='ee748743-8203-449c-a07c-092b4bc0bd33'></a>

Weinstabl, A., Hoff-Lesch, S., Merk, H. F., and von Felbert, V. (2011). Prospective randomized study on the efficacy of blue light in the treatment of psoriasis vulgaris. *Dermatology* 223, 251-259. doi: 10.1159/000333364

<a id='98456aad-277a-4425-80ad-d6eb7432689c'></a>

Weinstein, G. D., McCullough, J. L., and Ross, P. A. (1985). Cell kinetic
basis for pathophysiology of psoriasis. J. Invest. Dermatol. 85, 579–583.
doi: 10.1111/1523-1747.ep12283594

<a id='ad74b5ec-325d-4ff8-ba99-71952c198da7'></a>

Weinstein, G. D., and Van Scott, E. J. (1965). Autoradiographic analysis of turnover times of normal and psoriatic epidermis. _J. Invest. Dermatol._ 45, 257-262. doi: 10.1038/jid.1965.126

<a id='632f21a8-8344-4274-aa4f-7ab6243ccfb6'></a>

Yoshida, A., Yoshino, F., Makita, T., Maehata, Y., Higashi, K., Miyamoto, C., et al.
(2013). Reactive oxygen species production in mitochondria of human gingival
fibroblast induced by blue light irradiation. J. Photochem. Photobiol. B Biol. 129,
1–5. doi: 10.1016/j.jphotobiol.2013.09.003

<a id='2d9b002e-3935-4ced-8fc7-cdc9d46d00e2'></a>

Zhang, H., Hou, W., Henrot, L., Schnebert, S., Dumas, M., Heusèle, C., et al.
(2015). Modelling epidermis homoeostasis and psoriasis pathogenesis. J. R. Soc.
Interface 12. doi: 10.1098/rsif.2014.1071

<a id='710f29bb-8e70-4da8-aee0-1694e17d76cb'></a>

Zhou, H., Hu, C., Zhu, Y., Lu, M., Liao, S., Yeilding, N., et al. (2010).
Population-based exposure-efficacy modeling of ustekinumab in patients
with moderate to severe plaque psoriasis. J. Clin. Pharmacol. 50, 257-267.
doi: 10.1177/0091270009343695

<a id='182bdb52-1f70-4b2a-b1d2-c4115c1600b6'></a>

Zonios, G., Bykowski, J., and Kollias, N. (2001). Skin melanin, hemoglobin,
and light scattering properties can be quantitatively assessed in vivo
using diffuse reflectance spectroscopy. J. Invest. Dermatol. 117, 1452-1457.
doi: 10.1046/j.0022-202x.2001.01577.x

<a id='a543d237-50cc-41d7-a3cd-db953fd09f50'></a>

Conflict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

<a id='f6597895-0cf4-42dd-8793-3654f088fb2b'></a>

Copyright © 2017 Félix Garza, Liebmann, Born, Hilbers and van Riel. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

<a id='73df328c-dbab-496a-bc40-7add5b662e01'></a>

Frontiers in Physiology | www.frontiersin.org

<a id='82cdd88a-d522-40e1-a19e-e7f22d73b7a6'></a>

17

<a id='72b86c46-e5e2-4da0-b247-4714b95dad00'></a>

January 2017 | Volume 8 | Article 28