<a id='e9180e6a-e293-4a9c-8073-d8bbff20f604'></a>

Journal of Theoretical Biology 330 (2013) 75-87

<a id='c87c3619-08d7-47cc-afb3-789c0f5aee51'></a>

<::logo: Elsevier
NON SOLLUS
A detailed illustration of a tree with a figure on either side, one reaching for fruit, above the word "ELSEVIER" in orange capital letters.::>

<a id='de9e5a8a-3e6e-4b00-8c4f-8a623ec35e54'></a>

Contents lists available at SciVerse ScienceDirect

<a id='7a0fb92f-e6cb-45f7-9563-d3f97f51f053'></a>

Journal of Theoretical Biology

<a id='43f30a1e-4d9b-45ba-9b93-127751c37c58'></a>

journal homepage: www.elsevier.com/locate/yjtbi

<a id='aab2b1f4-1938-4eba-874c-bc2955ff284d'></a>

<::Cover of the "Journal of Theoretical Biology". The background is a marbled pattern in shades of green and cream. In the upper left corner, there is a small emblem with text that is not clearly legible. The title "Journal of Theoretical Biology" is prominently displayed in red serif font, with "Theoretical Biology" being larger than "Journal of".
: journal cover::>

<a id='ba071a82-7ffe-478a-a3f6-7325bdfaa807'></a>

A mathematical model representing cellular immune development
and response to *Salmonella* of chicken intestinal tissue

<a id='1507a481-b178-4d75-8bf6-97c2149453f2'></a>

<::logo: CrossMark
CrossMark
This logo features a red bookmark icon within a blue circle, with the brand name "CrossMark" written next to it in black text.::>

<a id='5ecbb6ea-3d00-4af8-a25f-57023236f82e'></a>

**D. Schokker** a*, **A. Bannink** b, **M.A. Smits** a,c,
**J.M.J. Rebel** c

a *Genetics and Genomics, Wageningen UR Livestock Research, Wageningen UR, PO Box 65, 6500 AB Lelystad, The Netherlands*
b *Animal Nutrition, Wageningen UR Livestock Research, Wageningen UR, PO Box 65, 6500 AB Lelystad, The Netherlands*
c *Central Veterinary Institute, Wageningen UR, PO Box 65, 8200 Lelystad, The Netherlands*

<a id='9f38bb49-082c-493c-b522-e2cc91254902'></a>

HIGHLIGHTS
---
* We examined early development of chicken with an immature immune system.
* We modelled both non-infected and infected chicks.
* _Salmonella_ is used as a challenge model.
* Model is line specific, other chicken lines can be modelled by changing parameters.
* Relationship between _Salmonella_ and chicken intestinal immune system is described.

<a id='3fca22d2-af81-4162-b97f-fac6a7842df9'></a>

## ARTICLE INFO
---
Article history:
Received 1 October 2012
Received in revised form
5 April 2013
Accepted 9 April 2013
Available online 18 April 2013
---
Keywords:
Dynamic modelling
Gastrointestinal tract
Immune response
Salmonella infection
Birds

<a id='10981ce1-f387-4bf4-abd9-99294f87ff3d'></a>

ABSTRACT

The aim of this study was to create a dynamic mathematical model of the development of the cellular branch of the intestinal immune system of poultry during the first 42 days of life and of its response towards an oral infection with *Salmonella enterica* serovar Enteritidis. The system elements were grouped in five important classes consisting of intra- and extracellular *S. Enteritidis* bacteria, macrophages, CD4$^+$, and CD8$^+$ cells. Twelve model variables were described by ordinary differential equations, including 50 parameters. Parameter values were estimated from literature or from own immunohistochemistry data. The model described the immune development in non-infected birds with an average R$^2$ of 0.87. The model showed less accuracy in reproducing the immune response to *S. Enteritidis* infection, with an average R$^2$ of 0.51, although model response did follow observed trends in time. Evaluation of the model against independent data derived from several infection trials showed strong/significant deviations from observed values. Nevertheless, it was shown that the model could be used to simulate the effect of varying input parameters on system elements response, such as the number of immune cells at hatch. Model simulations allowed one to study the sensitivity of the model outcome for varying model inputs. The initial number of immune cells at hatch was shown to have a profound impact on the predicted development in the number of systemic *S. Enteritidis* bacteria after infection. The theoretical contribution of this work is the identification of responses in system elements of the developing intestinal immune system of poultry obtaining a mathematical representation which allows one to explore the relationships between these elements under contrasting environmental conditions during different stages of intestinal development.

© 2013 Elsevier Ltd. All rights reserved.

<a id='c86e2f33-a53e-4d2c-b705-3a4a20c53e0d'></a>

1. Introduction

Maintaining intestinal health in chicken is crucial for sustainable poultry production. In this respect, it is important that the gut-associated immune system of young birds develops in a timely and appropriate manner. This development depends on a variety of genetic, nutritional, environmental, and management related factors.

<a id='e561504e-d778-4bff-bc44-d253efd4511f'></a>

Abbreviations: _Mr_, resting macrophages; _Ma_, activated macrophages; _Mi_, infected macrophages; _Se_, extracellular _Salmonella_; _Si_, intracellular _Salmonella_.
* Corresponding author. Tel.: +31 320 238 401; fax: +31 320 238 050.
E-mail addresses: dirkjan.schokker@wur.nl,
d.schokker@gmail.com (D. Schokker).

<a id='50d128c1-3c98-44e5-b2eb-d980db86b37e'></a>

0022-5193/$- see front matter  2013 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.jtbi.2013.04.005

<a id='feceaa08-2390-4bcc-9345-07ae86cfd6a4'></a>

Studies that investigate the effects of these factors on development of the immune system usually consider the various factors independently from each other to prevent confounding (Kelly and Coutts, 2000; Lewis et al., 2012; Cole et al., 2012). For a full understanding of the system, all these factors have to be considered together in an integrated manner. However, no methods are available yet for analyzing the combined impact of these factors on immune development. Thus, developing a mathematical model that represents the major aspects of immunological development and immune response, and that accommodates the most critical factors impacting on the system, would contribute to theory development and testing.

<a id='ae63930b-ff1e-44f2-8155-6fef8fefd9e1'></a>

After hatch, the chickens' intestinal tissue develops fast, accompanied by rapid morphological, functional and immunological

<!-- PAGE BREAK -->

<a id='6384a879-c666-4a6d-a38a-c296632f21d3'></a>

76

<a id='63b22299-6ac0-4af9-906f-3c5d86f8a63b'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75–87

<a id='dcfbcdb3-b68f-426e-bdda-21709998cbcd'></a>

changes (Schokker et al., 2009; Sklan, 2001; Uni et al., 2000).
Appropriate and timely development of the Gut Associated Lym-
phoid Tissue (GALT) is an important event in chicken, because, unlike
mammals, they lack lymph nodes which are a rich source of immune
cells. The avian intestinal immune system harbors a variety of
immune cells, including macrophages and dendritic cells (Janeway
and Medzhitov, 2002; Medzhitov and Janeway, 2000), plasma and
(memory-) B cells (Vaughan et al., 2011), and an array of subpopula-
tions of T cells, such as helper T cells (TH cells), cytotoxic T
lymphocytes (CTLs), regulatory T cells, natural killer T cells and
memory T cells (Romagnani, 2006). In addition, intraepithelial
lymphocytes, which monitor the luminal content of the gut and
eliminate distressed epithelial cells (Kunisawa et al., 2007), are
abundantly dispersed in the mucosal layer. Furthermore, lamina
propria lymphocytes are present which are classified as differen-
tiated effector lymphocytes and have a phenotype of activated
memory T cells (Cheroutre et al., 2011; James, 1991; Zeitz et al., 1990).

<a id='df4fb41e-48a9-47f0-9612-cd6da104814e'></a>

Specific components of microorganisms residing in the gut are monitored by Pathogen Recognition Receptors of the intestinal immune system, and when harmful microorganisms are detected, the innate part of the immune system is activated in order to neutralize the intruder (Iwasaki and Medzhitov, 2010). The process of immune activation in poultry has been the subject of numerous investigations, with gram-negative *Salmonella* species being frequently used as the immune response inducing agent (Kaiser et al., 2006; van Hemert et al., 2006, 2007; Withanage et al., 2005; Zhou and Lamont, 2007). These studies identified and characterized a variety of immunological components and defense mechanisms involved in the response against *S. Enteritidis*, and they defined the specific roles of immunological cells, signaling molecules, effector molecules, (signaling) pathways, and the products of a number of genes (proteins) (Ghebremicael et al., 2008; Kramer et al., 2003).

<a id='d2ee8f6b-0ff9-4175-940e-27fd74f231ea'></a>

It appears that the development and the activity of the intestinal immune response depend on numerous components and a complex interaction between these components, and between components and foreign antigens. Although detailed information has been gath-ered with respect to the dynamics and activity of individual compo-nents, it remains difficult to understand their interaction and how they are co-regulated to mount a protective immune response. Mathematical modeling of the intestinal immune system could assist in developing an improved understanding of the dynamics of this complex biological system. Such a model should represent the major components of the system and attempt to represent their interaction in a quantitative manner. The objective of this study was to construct a dynamic mechanistic model of the development of the cellular branch of the intestinal innate and adaptive immune system in chicken. The model focuses on the dynamics of early immunological development and the response to an infection with S. Enteritidis strain immediately after hatch. The theoretical contribution of this modeling effort is the mathematical representation of the most relevant system elements of the developing intestinal immune system of poultry, to be used to explore their mutual relationships and the overall immune response under contrasting environmental conditions (normal development versus development during S. Enteritidis infection). To our knowledge, a mathematical representation of both the development of the immune system and the immune response in young developing birds has not been reported before.

<a id='b0ec2b80-2538-4c1b-b70a-b1258f9277bd'></a>

## 2. Model development

### 2.1. Model description

A mathematical model was constructed to represent the events related to early cellular immune development in the intestine of chicken, and how it is affected during infection with S. Enteritidis

<a id='ff54c667-b0ce-49dc-9681-7a3b655b0251'></a>

immediately after hatch. The model represents processes taking place in jejunal tissue which harbors different immune cells, including intraepithelial lymphocytes and lamina propria lymphocytes. The focus of this model was the representation of CD4+ and CD8+ T cells,

<a id='fc8b46d7-f42e-4165-b97d-45cb6d9ae622'></a>

A<::Diagram of interconnected boxes and arrows, representing a biological process or system. The diagram shows several components, some highlighted with bold outlines and others faded. The connections indicate flows, reactions, or dependencies. The main components are CD4, CD8, Mr (bold), and Se, Mi, Si, Ma, CD4rec, Mrrec (faded).: chart::>

<a id='fa6f3af2-1474-4a8f-bffe-a2b1f4d76f97'></a>

<::chart::>Fig. 1. Schematic representation of variables and their fluxes. In non-infected developing chicken (A), resting macrophages (Mr), CD4+ cells (CD4+) and CD8+ cells (CD8+) increase over time by different mechanisms. The *Salmonella*-affected fluxes and variables are shown in grey, and they are not operative. For these cells a fixed source (s) and death rate (dr) per time was assumed. Moreover, the process of growth boost (gb) was described to account for the major changes in developing chicken. In *S. Enteritidis*

CD4rec box:
  - Input: CD4rec, Se (dashed arrow) -> rec
  - Output: rec (dashed arrow) -> CD4

CD4 box:
  - Inputs:
    - s (solid arrow)
    - gb (dashed arrow) <- CD4
    - rec (dashed arrow) <- CD4rec, Se
    - k (dashed arrow) <- CD4n <- Se, CD4
  - Outputs:
    - dr (dashed arrow) -> CD4
    - k (dashed arrow) -> Se, CD4

CD8 box:
  - Inputs:
    - s (solid arrow)
    - gb + comp (dashed arrow) <- CD8, CD4, Se
  - Outputs:
    - dr (dashed arrow) -> CD8

Se box:
  - Inputs:
    - k (dashed arrow) <- Ma, Se
    - k (dashed arrow) <- Mr, Se
    - k (dashed arrow) <- CD4, Se
    - b (solid arrow) <- Si, Mi
  - Outputs:
    - dr (dashed arrow) -> Se
    - p (dashed arrow) -> Se
    - i (dashed arrow) -> Mr, Se (to Mr)
    - i (dashed arrow) -> Mr, Se (to Mi)

Mr box:
  - Inputs:
    - s (solid arrow)
    - gb (dashed arrow) <- Mr
    - rec (dashed arrow) <- Mrrec, Se
    - k (dashed arrow) <- Se, Mr
    - da (dashed arrow) <- CD4, Ma
  - Outputs:
    - dr (dashed arrow) -> Mr
    - a (dashed arrow) -> Se, Mr (to Ma)
    - i (dashed arrow) -> Mr, Se (to Se)
    - i (dashed arrow) -> Mr, Se (to Mi)

Mi box:
  - Inputs:
    - i (dashed arrow) <- Mr, Se (from Mr)
    - i (dashed arrow) <- Mr, Se (from Se)
    - p (solid arrow) <- Mi, CD4, CD8, Si
  - Outputs:
    - dr (dashed arrow) -> Mi

Si box:
  - Inputs:
    - p (solid arrow) <- Mi, CD4, CD8, Si
  - Outputs:
    - dr (dashed arrow) -> Si
    - b (solid arrow) -> Si, Mi (to Se)

Mrrec box:
  - Input: Mrrec, Se (dashed arrow) -> rec
  - Output: rec (dashed arrow) -> Mr

Ma box:
  - Inputs:
    - a (dashed arrow) <- Se, Mr (from Mr)
  - Outputs:
    - dr (dashed arrow) -> Ma
    - k (dashed arrow) -> Se, Ma (to Se)
<::chart::>

<a id='11b7e816-9121-459a-b69b-175e635ab5f9'></a>

death rate (_dr_) per time was assumed. Moreover, the process of growth boost (_gb_) was described to account for the major changes in developing chicken. In _S. Enteritidis_ infected developing chicken (B), the same components as in the non-infected chicken were present, but due to the _S. Enteritidis_ infection, recruitment (_rec_) of CD4+ occurred from a pool outside the intestine (CD4rec). Furthermore, infection (_i_) of _Mr_ by extracellular _Salmonella_ (_Se_) occurred which consequently become infected macrophages (_Mi_) harboring intracellular _Salmonella_ (_Si_). These _Mi_ can burst (_b_) or undergo lysis (_l_), which, respectively, contribute to the amount of _Se_ or clearance of _Se_. Due to the _S. Enteritidis_ infection _Mr_ is activated (_a_) and become activated macrophages (_Ma_), and vice versa where _Ma_ will be deactivated (_da_) and become _Mr_. Together _Ma_ and _Mr_ will actively kill (_k_) _Se_, as well as (naïve) CD4+ (CD4n). The _Se_ and _Si_ have a proliferation (_p_) and death rate (_dr_). Furthermore, due to the _S. Enteritidis_ infection the increase of CD8+ is negatively affected by CD4+, competition effect (_comp_). Solid lines indicate fluxes, whereas dashed lines indicate which variables have an influence on that specific flux.

<!-- PAGE BREAK -->

<a id='870641b0-5019-40e5-860a-7a8fe9e07326'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='b484a2da-2f9d-4fc2-81cc-72ff68ab6740'></a>

77

<a id='d70679df-c722-426b-907c-3c2a9151c1f0'></a>

in addition to macrophages and S. Enteritidis cells. It is known that
γδ⁺ cells are involved in the response against _Salmonella_ (Hara et al.,
1992) and that there is an increase in the number of CD8a⁺ γδ⁺ cells
in the intestine due to the _Salmonella_ infection in chickens (Berndt
and Methner, 2001; Berndt et al., 2007). However, the CD8α⁻ γδ⁺
T cells hardly respond to the _Salmonella_ infection (Pieper et al., 2011).
In order to generate a relatively simple model the CD8⁺ population
also contains the CD8α⁺ γδ⁺ T cell population. Different cell types
interact via intercellular communication. A schematic overview of
the state variables in the model and associated flows, and their
influence on other cells via intercellular communication, is given in
Fig. 1A and B for non-infected and S. Enteritidis infected chickens,
respectively. The change of state variables in time is represented by
ordinary differential equations (Eqs. (1)–(12)). Parameter names and
abbreviations are explained in Table 1. Interactions between cell
types, which can be characterized by a saturating process or by an
active process that follows the law of enzyme kinetics, are repre-
sented by a Henri-Michaelis-Menten (HMM) function. To represent
allosteric effects on such enzyme kinetics (stimulation or inhibition),
a Hill equation was used, which includes an additional exponent
parameter.

<a id='a4ba2a6e-59ef-4eae-9c67-63b0300970e9'></a>

dMr/dt = + sMr + gbMr \times Mr \times (1 - Mr / (ccMr - ccMr \times p1))
+ Mrrec \times (vrecMr \times Se) / (Se + kmrecMr)
+ daMa \times Ma \times CD4 / (CD4 + cdaMa)
- iMr \times Mr \times Se / (Se + cSeMri)
- aMr \times Mr \times Se / (Se + cSeMr)
- kSeMr \times Mr \times Se - drMr \times Mr
(1)

<a id='e3cedaa1-8d20-4fd0-b9fa-aa1885972aeb'></a>

dCD4/dt = sCD4 + gbCD4 × CD4 × (1 - CD4/cc1CD4)
× (CD4^ngbCD4 / (CD4^ngbCD4 + k2CD4^ngbCD4))
+ CD4rec × (vrecCD4 × Se / (Se + kmrecCD4)) - kSeCD4 × CD4 × Se
- CD4n × CD4 × (Se^ndCD4 / (Se^ndCD4 + Se^ndCD4)) - drCD4 × CD4 (2)

<a id='82966864-32f6-4c46-af7e-68c60781d14f'></a>

dCD8 / dt = + sCD8 + gbCD8 × CD8 × (1 - CD8 / cc1CD8)
× CD8 / (CD8 + k2CD8) - compCD8 × CD8 × (Se / (Se + w1))
× (CD4^ncompcd8 / (CD4^ncompcd8 + kcompCD4^ncompcd8)) - drCD8 × CD8 (3)

<a id='9c7010d4-310b-4ce1-bdf3-15e7fe2368cf'></a>

Table 1
General abbreviation for variables and model parameters.
<table id="2-1">
<tr><td id="2-2">Parameter name</td><td id="2-3">Short</td></tr>
<tr><td id="2-4">Death rate</td><td id="2-5">dr</td></tr>
<tr><td id="2-6">Source</td><td id="2-7">s</td></tr>
<tr><td id="2-8">Growth boost</td><td id="2-9">gb</td></tr>
<tr><td id="2-a">Competition</td><td id="2-b">comp</td></tr>
<tr><td id="2-c">Pool for recruitment</td><td id="2-d">rec</td></tr>
<tr><td id="2-e">Killing</td><td id="2-f">k</td></tr>
<tr><td id="2-g">Activation</td><td id="2-h">a</td></tr>
<tr><td id="2-i">Deactivation</td><td id="2-j">da</td></tr>
<tr><td id="2-k">Infection</td><td id="2-l">i</td></tr>
<tr><td id="2-m">Lysis</td><td id="2-n">l</td></tr>
<tr><td id="2-o">Bursting</td><td id="2-p">b</td></tr>
<tr><td id="2-q">Proliferation</td><td id="2-r">p</td></tr>
<tr><td id="2-s">Carrying capacity</td><td id="2-t">cc</td></tr>
</table>

<a id='3b6cd55f-c7f0-485b-b013-845985fa2f0a'></a>

dMa / dt = + aMr × Mr × Se / (Se + cSeMr) - daMa × Ma × CD4 / (CD4 + cdaMA) - kSeMa × Ma × Se - drMa × Ma (4)

dMi / dt = + iMr × Mr × Se / (Se + cSeMri) - bMi × Mi × Si^mMi / (Si^mMi + (N × Mi)^mMi) - lMi × (CD4 + CD8/Mi) / ((CD4 + CD8/Mi) + cCD4CD8) × (1 - apop × Si / (Si + N + Mi)) - drMi × Mi (5)

dSe / dt = + pSe × Se × (1 - Se / ccSe) + bMi × Mi × Si^mMi / (Si^mMi + (N × Mi)^mMi) - iMr × Mr × Se / (Se + cSeMri) - kSeCD4 × CD4 × Se - kSeMr × Mr × Se - kSeMa × Ma × Se - drSe × Se (6)

dSi / dt = + pSi × Si × (1 - Si / (Si + N × Mi)) + iMr × Mr × Se / (Se + cSeMr) - bMi × Mi × Si^mMi / (Si^mMi + (N × Mi)^mMi) - lMi × (CD4 + CD8/Mi) / ((CD4 + CD8/Mi) + cCD4CD8) - drSi × Si (7)

dCD4rec / dt = -CD4rec × vrecCD4 × Se / (Se + kmrecCD4) (8)

dMrrec / dt = -Mrrec × vrecMr × Se / (Se + kmrecMr) (9)

dTotalM / dt = dMr / dt + dMa / dt + dMi / dt (10)

dTotalT / dt = dCD4 / dt + dCD8 / dt (11)

dTotalS / dt = dSe / dt + dSi / dt (12)

<a id='5aaa66a0-ef16-4aee-9992-d208cd15ebeb'></a>

2.1.1. Macrophage-related processes
The model for non-infected chickens included resting macrophages (Mr, #/ml) (Table 2). The following processes involving macrophages were represented: a source, death and a growth boost of Mr (Eq. (1)). Source is an influx of Mr from outside the intestinal system, which is estimated to be close to a daily flow of 1% the initial number of macrophages present (Eq. (1), sMr; 300,000 #Mr/(ml d)). The death rate of Mr (Eq. (1), drMr; 0.011 d⁻¹) is assumed to be in the same range as the death rate of macrophages in healthy adult mice or humans (Monack et al., 1996; Van Furth et al., 1973). In addition, we used a growth boost for Mr, based on a law of population growth, with growth rate gbMr (Eq. (1); 1.2 d⁻¹) and carrying capacity ccMr (Eq. (1); 2.5E+7 #Mr/ml).

<a id='e2c08e73-b5bc-4089-92bb-ca1697d18350'></a>

In infected chickens, S. Enteritidis breaches the intestinal
barrier and Mr encounter and phagocytize extracellular S. Enter-
itidis (Se). Subsequently, infection of macrophages (Mi, #/ml)
or activation of macrophages (Ma, #/ml) occurs, the infection
reaction (Mr to Mi) is expressed by a HMM equation for Se
(Eqs. (1) and (5), iMr, 0.1 d¯¹ (Oh et al., 1996)). The half-
saturation of Se on infection of Mr (cSeMri) is set to 600,000
#Se/ml. Similarly, the activation rate of macrophages, Mr to Ma
(aMa, 100 d¯¹), was described by an HMM equation (Eq. (4)), with

<!-- PAGE BREAK -->

<a id='1628939a-6639-4029-bdb1-47d4e916d18f'></a>

78

<a id='05f7cf94-f8dc-4ec7-894b-47f76f806ac0'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='dc3f81ff-b51d-43cd-ab69-ecab5e7ad18c'></a>

a half saturation *Se* on activation *Mr* (*cSeMra*) of 1 #*Se*/ml. The *Se*
bacteria are actively cleared by *Mr* and *Ma* in order to decrease the
severity of infection. This clearance rate was defined by separate
equations for *Mr* (Eqs. (1) and (6), *kSeMr*; 5e-8 ml/(#*Mr*•d) (Flesch
and Kaufmann, 1990; Wigginton and Kirschner, 2001)) and *Ma*
(Eqs. (4) and (6), *kMa*; 2.5e-7 ml/(#*Ma*•d) (Flesch and Kaufmann,
1990; Wigginton and Kirschner, 2001)) and their interaction with
*Se* (Wigginton and Kirschner, 2001). The rapid influx of macro-
phages, which is different from the growth boost, is represented
by a pool of macrophages (*Mrrec*) from outside the intestine. The
corresponding reaction is expressed by a HMM equation with
maximum velocity of *vrecMr* (Eqs. (1) and (9); 1 #*Se*/(ml• d•#*Mr*))
and Michaelis-Menten constant of *kmrecMr* (Eqs. (1) and (9); 1000
#*Mr*/ml). It was demonstrated that *S. Enteritidis* can survive within
macrophages and is able to spread systemically in the host
(Richter-Dahlfors et al., 1997). The representation of intracellular
growth of *S. Enteritidis* is described in Section 2.1.4. The *Mi* are

<a id='e2c5c87c-fae3-4ef4-b148-d04f56a0d856'></a>

Table 2
Initial values of model variables.
<table id="3-1">
<tr><td id="3-2">Variable name</td><td id="3-3">Eq.a</td><td id="3-4">Common name</td><td id="3-5">Non-infected (#/ml)</td><td id="3-6">Infected (#/ml)</td></tr>
<tr><td id="3-7">CD4+</td><td id="3-8">1</td><td id="3-9">CD4+ cells</td><td id="3-a">9e+06</td><td id="3-b">9e+06</td></tr>
<tr><td id="3-c">CD8+</td><td id="3-d">2</td><td id="3-e">CD8+ cells</td><td id="3-f">7e+06</td><td id="3-g">7e+06</td></tr>
<tr><td id="3-h">Mr</td><td id="3-i">3</td><td id="3-j">Resting macrophages</td><td id="3-k">9e+06</td><td id="3-l">9e+06</td></tr>
<tr><td id="3-m">Ma</td><td id="3-n">4</td><td id="3-o">Activated macrophages</td><td id="3-p">0</td><td id="3-q">0</td></tr>
<tr><td id="3-r">Mi</td><td id="3-s">5</td><td id="3-t">Infected macrophages</td><td id="3-u">0</td><td id="3-v">0</td></tr>
<tr><td id="3-w">Se</td><td id="3-x">6</td><td id="3-y">Extracellular Salmonella</td><td id="3-z">0</td><td id="3-A">200</td></tr>
<tr><td id="3-B">Si</td><td id="3-C">7</td><td id="3-D">Intracellular Salmonella</td><td id="3-E">0</td><td id="3-F">0</td></tr>
<tr><td id="3-G">CD4rec</td><td id="3-H">8</td><td id="3-I">Pool for recruitment CD4+</td><td id="3-J">2.7e+07</td><td id="3-K">2.7e+07</td></tr>
<tr><td id="3-L">Mrrec</td><td id="3-M">9</td><td id="3-N">Pool for recruitment Mr</td><td id="3-O">2e+07</td><td id="3-P">2e+07</td></tr>
<tr><td id="3-Q">TotalM</td><td id="3-R">10</td><td id="3-S">Sum of Mr, Ma and Mi</td><td id="3-T">9e+06</td><td id="3-U">9e+06</td></tr>
<tr><td id="3-V">TotalT</td><td id="3-W">11</td><td id="3-X">Sum of CD4+ and CD8+</td><td id="3-Y">1.6e+07</td><td id="3-Z">1.6e+07</td></tr>
<tr><td id="3-10">TotalS</td><td id="3-11">12</td><td id="3-12">Sum of Se and Si</td><td id="3-13">0</td><td id="3-14">200</td></tr>
</table>
ᵃ Eq. = equations.

<a id='f09769ec-ab10-49f0-81b4-7984b2a65070'></a>

-1
targets for lysis by the immune system, and Mi are eliminated via
apoptosis by CD4+ cells at a maximal rate of IMi (Eq. (5); 0.8 d^-1
(Lewinsohn et al., 1998)). Furthermore, both CD4+ (CD4, #/ml) and
CD8+ cells (CD8, #/ml) account for the cytotoxic effects, and this
effect depends on the ratio of total T cells (CD4+CD8) and Mi, which
was half maximal when the ratio is equal to the parameter cCD4CD8
(Eq. (5); 10 (CD4+CD8)/Mi) (Wigginton and Kirschner, 2001)). Also,
we assume that Se is capable of opposing death of its host cell, which
is denoted by 1-apop\u2022(Si/(Si+N\u2022Mi)), where apop (Eq. (5), A.6, and
A.7; 0.7 (scalar) (Balcewicz-Sablinska et al., 1999)) stands for the
maximal per cent effect of intracellular S. Enteritidis (Si). The Si are
able to proliferate and if this proliferation is uncontrolled, the limit of
the capacity N (Eq. (5), A.6, and A.7; 30 Si/Mi (Brown et al., 2006;
Lindgren et al., 1996)) of the Mi to sustain bacteria will be reached, i.e.
the maximum multiplicity of infection (MOI). When this threshold is
exceeded the macrophage will die and bacteria will be released in
the extracellular matrix. This process is represented by a HMM
equation and growth occurs at rate bMi (Eq. (5), A.6, and A.7; 0.4 d^-1
(Rojas et al., 1997). When the infection is less severe, Ma will be
inactivated by CD4+ which is programmed by a HMM equation with
maximum conversion rate daMa (Eq. (1) and A.4; 40 d^-1) and
Michaelis-Menten constant cdaMa (Eq. (1) and A.4; 3E+07 #CD4/
ml). An overview of all parameters regarding Mr, Ma and Mi is given
in Tables 3\u20135, respectively.

<a id='b9a25f85-1363-4fa9-b00b-20e69282547d'></a>

2.1.2. CD4+ cells related processes
The model for infected chickens includes a representation of the number of CD4+ cells because this influences the deactivation of activated macrophages and stimulates lysis of Mi. In normal development (non-infected chickens) CD4+ cells die at rate drCD4 (Eq. (2); 0.016 d⁻¹ (Sprent, 1973; Sprent and Basten, 1973)) and their renewal occurs at rate sCD4 (Eq. (2); 490,000 #CD4/(ml d)). Like for Mr, a growth boost was assumed for CD4+ too to describe a rapid development of the intestinal immune system in time. Again an equation based on the law of population growth was used, with maximum growth rate gbCD4 (Eq. (2); 0.19 d⁻¹) and carrying capacity cc1CD4 (Eq. (2); 8.2E+7 #CD4/ml). Furthermore, a Hill-like equation was programmed to create a sigmoidal relation with

<a id='8f508f0f-a8af-473d-9415-0bef4c555a8b'></a>

Table 3
Definitions and values of model parameters related to resting macrophages.

<a id='395097ba-dc35-47f1-89bf-ce2cd7c3e447'></a>

<table id="3-15">
<tr><td id="3-16">Parameter name</td><td id="3-17">Short</td><td id="3-18">Eq.ª</td><td id="3-19">Range</td><td id="3-1a">Value</td><td id="3-1b">Unit</td></tr>
<tr><td id="3-1c">Source Mr</td><td id="3-1d">sMr</td><td id="3-1e">1</td><td id="3-1f">300,000</td><td id="3-1g">300,000</td><td id="3-1h">#Mr/(ml d)</td></tr>
<tr><td id="3-1i">Death rate Mr</td><td id="3-1j">drMr</td><td id="3-1k">1</td><td id="3-1l">0.011–0.03</td><td id="3-1m">0.011</td><td id="3-1n">d⁻¹</td></tr>
<tr><td id="3-1o">Activation rate Mr</td><td id="3-1p">aMr</td><td id="3-1q">1,4</td><td id="3-1r">100</td><td id="3-1s">100</td><td id="3-1t">d⁻¹</td></tr>
<tr><td id="3-1u">Half-saturation Se on activation Mr</td><td id="3-1v">cSeMr</td><td id="3-1w">1,4</td><td id="3-1x">1</td><td id="3-1y">1</td><td id="3-1z">#Se/ml</td></tr>
<tr><td id="3-1A">Infection rate Mr</td><td id="3-1B">iMr</td><td id="3-1C">1,5,6</td><td id="3-1D">0.1-0.9</td><td id="3-1E">0.1</td><td id="3-1F">d⁻¹</td></tr>
<tr><td id="3-1G">Half-saturation Se on infection Mr</td><td id="3-1H">cSeMri</td><td id="3-1I">1,5,6</td><td id="3-1J">600,000</td><td id="3-1K">600,000</td><td id="3-1L">#Se/ml</td></tr>
<tr><td id="3-1M">Killing Se by Mr</td><td id="3-1N">kSeMr</td><td id="3-1O">1,6</td><td id="3-1P">5E-08</td><td id="3-1Q">5E-08</td><td id="3-1R">ml/(#•d)</td></tr>
<tr><td id="3-1S">Growth boost Mr</td><td id="3-1T">gbMr</td><td id="3-1U">1</td><td id="3-1V">1.2</td><td id="3-1W">1.2</td><td id="3-1X">d⁻¹</td></tr>
<tr><td id="3-1Y">Growth boost carrying capacity Mr</td><td id="3-1Z">ccMr</td><td id="3-20">1</td><td id="3-21">2.5E+07</td><td id="3-22">2.5E+07</td><td id="3-23">#Mr/ml</td></tr>
<tr><td id="3-24">Growth boost Mr p1</td><td id="3-25">p1</td><td id="3-26">1</td><td id="3-27">0.65</td><td id="3-28">0.65</td><td id="3-29">scalar</td></tr>
<tr><td id="3-2a">Recruitment Mr v</td><td id="3-2b">vrecMr</td><td id="3-2c">1,9</td><td id="3-2d">1</td><td id="3-2e">1</td><td id="3-2f">#Se/(ml d•#Mr)</td></tr>
<tr><td id="3-2g">Recruitment Mr km</td><td id="3-2h">kmrecMr</td><td id="3-2i">1,9</td><td id="3-2j">1000</td><td id="3-2k">1000</td><td id="3-2l">#Mr/ml</td></tr>
</table>
a Eq. = equations.

<a id='ccf0187c-fed1-473d-8004-777ec3404482'></a>

Table 4
Definitions and values of model parameters related to activated macrophages.
<table id="3-2m">
<tr><td id="3-2n">Parameter name</td><td id="3-2o">Short</td><td id="3-2p">Eq.ª</td><td id="3-2q">Range</td><td id="3-2r">Value</td><td id="3-2s">Unit</td></tr>
<tr><td id="3-2t">Death rate Ma</td><td id="3-2u">drMa</td><td id="3-2v">4</td><td id="3-2w">0.011-0.08</td><td id="3-2x">0.08</td><td id="3-2y">d⁻¹</td></tr>
<tr><td id="3-2z">Killing Se by Ma</td><td id="3-2A">kSeMa</td><td id="3-2B">4,6</td><td id="3-2C">2.6E-07</td><td id="3-2D">2.6E-07</td><td id="3-2E">ml/(#Ma•d)</td></tr>
<tr><td id="3-2F">Deactivation rate Ma</td><td id="3-2G">daMa</td><td id="3-2H">1,4</td><td id="3-2I">40</td><td id="3-2J">40</td><td id="3-2K">d⁻¹</td></tr>
<tr><td id="3-2L">Half-saturation CD4+ on deactivation Ma</td><td id="3-2M">cdaMa</td><td id="3-2N">1,4</td><td id="3-2O">3E+07</td><td id="3-2P">3E+07</td><td id="3-2Q">#CD4⁺/ml</td></tr>
</table>

<a id='2c237123-4070-4796-b289-ac722e2a4557'></a>

a Eq. = equations.

<!-- PAGE BREAK -->

<a id='1e46092d-56fd-4d07-9102-7cb01a22f2f1'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='023de566-c628-4fc4-9eb6-708426627e6a'></a>

79

<a id='fdd102aa-1b7a-446c-a8e2-402fa4402242'></a>

Table 5
Definitions and values of model parameters related to infected macrophages.

<table id="4-1">
<tr><td id="4-2">Parameter name</td><td id="4-3">Short</td><td id="4-4">Eq.a</td><td id="4-5">Range</td><td id="4-6">Value</td><td id="4-7">Unit</td></tr>
<tr><td id="4-8">Carrying capacity of Mi</td><td id="4-9">N</td><td id="4-a">5, 6, 7</td><td id="4-b">7-30</td><td id="4-c">30</td><td id="4-d">#Si/#Mi</td></tr>
<tr><td id="4-e">Bursting rate Mi</td><td id="4-f">bMi</td><td id="4-g">5, 6, 7</td><td id="4-h">0.05-0.5</td><td id="4-i">0.4</td><td id="4-j">d⁻¹</td></tr>
<tr><td id="4-k">HMM constant Mi</td><td id="4-l">mMi</td><td id="4-m">5, 6, 7</td><td id="4-n">2</td><td id="4-o">2</td><td id="4-p">Scalar</td></tr>
<tr><td id="4-q">Lysis rate Mi</td><td id="4-r">IMi</td><td id="4-s">5, 7</td><td id="4-t">0.4-0.8</td><td id="4-u">0.8</td><td id="4-v">d⁻¹</td></tr>
<tr><td id="4-w">Half saturation (CD4++CD8+)/Mi ratio on lysis Mi</td><td id="4-x">CCD4CD8</td><td id="4-y">5,7</td><td id="4-z">5-20</td><td id="4-A">10</td><td id="4-B">(#CD4++#CD8*)|#Mi</td></tr>
<tr><td id="4-C">Max percentage inhibition of apoptosis</td><td id="4-D">apop</td><td id="4-E">5,7</td><td id="4-F">0.7</td><td id="4-G">0.7</td><td id="4-H">Scalar</td></tr>
<tr><td id="4-I">Death rate Mi</td><td id="4-J">drMi</td><td id="4-K">5</td><td id="4-L">0.011-0.03</td><td id="4-M">0.011</td><td id="4-N">d⁻¹</td></tr>
</table>
ª Eq. = equations.

<a id='acb0fd3f-094e-48c0-b025-66752ef823f6'></a>

Table 6
Definitions and values of model parameters related to CD4+ cells.
<table id="4-O">
<tr><td id="4-P">Parameter name</td><td id="4-Q">Short</td><td id="4-R">Eq.ª</td><td id="4-S">Range</td><td id="4-T">Value</td><td id="4-U">Unit</td></tr>
<tr><td id="4-V">Source CD4+</td><td id="4-W">sCD4</td><td id="4-X">2</td><td id="4-Y">490,000</td><td id="4-Z">490,000</td><td id="4-10"># CD4+/(ml d)</td></tr>
<tr><td id="4-11">Death rate CD4+</td><td id="4-12">drCD4</td><td id="4-13">2</td><td id="4-14">0.01-0.33</td><td id="4-15">0.016</td><td id="4-16">d⁻¹</td></tr>
<tr><td id="4-17">Growth boost CD4+ rate</td><td id="4-18">gbCD4</td><td id="4-19">2</td><td id="4-1a">0.19</td><td id="4-1b">0.19</td><td id="4-1c">d⁻¹</td></tr>
<tr><td id="4-1d">Growth boost CD4+ carrying capacity</td><td id="4-1e">cc1CD4</td><td id="4-1f">2</td><td id="4-1g">8.2E+07</td><td id="4-1h">8.2E+07</td><td id="4-1i"># CD4+/ml</td></tr>
<tr><td id="4-1j">Growth boost CD4+ n</td><td id="4-1k">ngbCD4</td><td id="4-1l">2</td><td id="4-1m">2</td><td id="4-1n">2</td><td id="4-1o">Scalar</td></tr>
<tr><td id="4-1p">Growth boost CD4+ kCD4</td><td id="4-1q">k2CD4</td><td id="4-1r">2</td><td id="4-1s">8.7E+06</td><td id="4-1t">8.7E+06</td><td id="4-1u"># CD4*/ml</td></tr>
<tr><td id="4-1v">Recruitment CD4+ from CD4recr km</td><td id="4-1w">kmrecCD4</td><td id="4-1x">2,8</td><td id="4-1y">1</td><td id="4-1z">1</td><td id="4-1A"># CD4*/ml</td></tr>
<tr><td id="4-1B">Recruitment CD4+ from CD4recr v</td><td id="4-1C">vrecCD4</td><td id="4-1D">2.8</td><td id="4-1E">100</td><td id="4-1F">100</td><td id="4-1G">#Se/(ml d.# CD4*)</td></tr>
<tr><td id="4-1H">Interaction (naive) CD4&quot; with Se n</td><td id="4-1I">CD4n</td><td id="4-1J">2</td><td id="4-1K">04</td><td id="4-1L">04</td><td id="4-1M">d⁻¹</td></tr>
<tr><td id="4-1N">Interaction (naïve) CD4+ with Se b</td><td id="4-1O">ndCD4</td><td id="4-1P">2</td><td id="4-1Q">8</td><td id="4-1R">8</td><td id="4-1S">Scalar</td></tr>
<tr><td id="4-1T">Interaction (naïve) CD4+ with Se kSe</td><td id="4-1U">kSedCD4</td><td id="4-1V">2</td><td id="4-1W">4200</td><td id="4-1X">4200</td><td id="4-1Y">ml/(d•# CD4+)</td></tr>
<tr><td id="4-1Z">Killing Se by CD4* k4</td><td id="4-20">kSeCD4</td><td id="4-21">2,6</td><td id="4-22">1e-9</td><td id="4-23">1e-9</td><td id="4-24">ml/(# CD4+ •d)</td></tr>
</table>
ª Eq. = equations.

<a id='6b274ba0-3b72-4917-86cf-844fc82ccd19'></a>

an initial gradual increase followed by a rapid increase in velocity of CD4+, by the use of the Hill coefficient *ngbCD4* (Eq. (2); 2 (scalar)) and ligand concentration producing half occupation of k2CD4 (Eq. (2); 8.7E+6 #CD4/ml).

<a id='275ab6c4-7e07-4e36-a16f-29cddea35db9'></a>

In S. Enteritidis infected chickens, an influx of CD4+ is observed at 1 day post-infection. Therefore, we assumed that (naïve) CD4+ also participate in the response against S. Enteritidis, as was observed for S. Typhimurium infections in mice (Caramalho et al., 2003). This participation is embodied in an equation where CD4+ cells kill Se at rate kSeCD4 (Eq. (2); 1e-9 ml/(#CD4·d)), and a Hill-like equation is included to create a sigmoidal relation for the interaction between naïve CD4+ and Se. A Hill equation was programmed wherein the initial increase is slow followed by rapid increase, with Hill coefficient ndCD4 (Eq. (2); 8 (scalar)), ligand concentration producing half occupation of kSedCD4 (Eq. (2); 4200 ml/(d·#CD4)), and maximum rate of CD4n (Eq. (2); 0.4 d¯¹). The rapid influx of CD4+, which is different from the growth boost, is represented by a pool of CD4+ (CD4rec) from outside the intestine. The corresponding reaction is expressed by a HMM equation, with a maximum rate of vrecCD4 (Eq. (2); 100 #Se/ (ml d•#CD4)) and Michaelis-Menten constant kmrecCD4 (Eq. (2); 1 #CD4/ml). An overview of all parameters regarding CD4+ is presented in Table 6.

<a id='38ba8cf7-a18d-4244-84ff-6cebf3d357be'></a>

2.1.3. CD8+ cells related processes
The model includes CD8+ because 90% of the intraepithelial lymphocytes are T-cells and 80% of those are CD8+. It is known that CD8+ are involved in clearing of *Salmonella* (Li et al., 2012).
In normal development (non-infected chickens), CD8+ die at rate *drCD8* (Eq. (2); 0.001 d⁻¹ (Sprent, 1973; Sprent and Basten, 1973)) and renew from source at rate *sCD8* (Eq. (2); 430,000 #CD8/ (ml d)). Comparable to *Mr* and CD4+, also for CD8+ a growth boost was presumed due to the rapidly developing intestine, represented by population growth law with maximum growth rate *gbCD8* (Eq. (3); 1.44 d⁻¹) and carrying capacity *cc1CD8* (Eq. (3);

<a id='12a0ea27-db16-4a03-9aa5-1351b59f0a87'></a>

1.3E+7 #CD8/ml). Furthermore, a Hill-like equation was introduced to create a sigmoidal relationship, with k2CD8 (Eq. (3); 4.7E+7 #CD8/ml) as ligand concentration producing half occupation. Although CD8+ have a minor role in this model, they do affect the lysis of Mi (Eq. (5), A.6 and A.7). Moreover, in the immunohistochemistry data, a down-regulation of CD8+ was observed when comparing infected chickens with non-infected chickens, which could be an indirect effect of S. Enteritidis. This competitive effect is represented by inhibition of the growth boost of CD8+ by CD4+, which is described with a Hill function with ncompCD4 as the Hill coefficient (Eq. (3); 0.5 (scalar)) and kcompCD4 (Eq. (3); 3.4E+7 #CD4/ml) for the ligand concentration producing half occupation, compCD8 (Eq. (3); 0.85 #CD8/ml) for the maximum rate of competition by CD4+. To ensure that the competitive effect will only occur when S. Enteritidis is present, the function Se/(Se+w1) was programmed, where w1 is 1e-25 (scalar) (Eq. (3)). An overview of all parameters regarding CD8+ is given in Table 7.

<a id='42af61f9-2851-4342-a132-93851868a248'></a>

2.1.4. *S. Enteritidis* related processes

*S. Enteritidis* stays either extracellular (*Se*, # *Se* cells/ml) or intracellular (*Si*, # *Si* cells/ml). The *Se* will proliferate within the intestinal tissue matrix at rate *pSe* (Eq. (6); 35 d⁻¹ (Brown et al., 2006)) and *Si* inside macrophages at rate *pSi* (Eq. (6); 4.1 d⁻¹ (Abshire and Neidhardt, 1993; Lowrie et al., 1979)). The carrying capacity (*ccSe*) for *Se* is set at 500,000 #*Se*/ml. Both *Si* and *Se* have death rates, *drSi* (Eq. (7); 0.05 d⁻¹) and *drSe* (Eq. (6); 28 d⁻¹, respectively (Garcia-del Portillo, 2001; Hormaeche, 1980)). An overview of all parameters regarding *Se* and *Si* is given in Table 8.

<a id='ddc43c11-648d-4a25-8eb9-2e9d451957b6'></a>

## 2.2. Model simulation software

The model was programmed in Complex Pathway Simulator (COPASI v4.6.33) (Hoops et al., 2006). Infections were simulated for 42 days and model output was generated with an interval of 0.01 day. The LSODA method (Hoops et al., 2006) was used to solve

<!-- PAGE BREAK -->

<a id='16379e6c-b505-4ab5-bb4b-be9263b1da0c'></a>

80

<a id='cf624ccc-a7ac-46b2-a630-636436bbf158'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='9236689d-69fe-458e-8cec-d43a8d0ae1c5'></a>

Table 7
Definitions and values of model parameters related to CD8+ cells.
<table id="5-1">
<tr><td id="5-2">Parameter name</td><td id="5-3">Short</td><td id="5-4">Eq.ᵃ</td><td id="5-5">Range</td><td id="5-6">Value</td><td id="5-7">Unit</td></tr>
<tr><td id="5-8">Death rate CD8⁺</td><td id="5-9">drCD8</td><td id="5-a">3</td><td id="5-b">0.001-0.33</td><td id="5-c">0.001</td><td id="5-d">d⁻¹</td></tr>
<tr><td id="5-e">Source CD8⁺</td><td id="5-f">sCD8</td><td id="5-g">3</td><td id="5-h">430,000</td><td id="5-i">430,000</td><td id="5-j"># CD8⁺/(ml d)</td></tr>
<tr><td id="5-k">Growth boost+competition CD8⁺ a8</td><td id="5-l">gbCD8</td><td id="5-m">3</td><td id="5-n">1.44</td><td id="5-o">1.44</td><td id="5-p">d⁻¹</td></tr>
<tr><td id="5-q">Growth boost+competition CD8⁺ cc1CD8</td><td id="5-r">cc1CD8</td><td id="5-s">3</td><td id="5-t">1.3E+07</td><td id="5-u">1.3E+07</td><td id="5-v"># CD8⁺/ml</td></tr>
<tr><td id="5-w">Growth boost+competition CD8+ K2CD8</td><td id="5-x">K2CD8</td><td id="5-y">3</td><td id="5-z">4.7E+07</td><td id="5-A">4.7E+07</td><td id="5-B"># CD8+/ml</td></tr>
<tr><td id="5-C">Growth boost+competition mCD4 ncompCD4</td><td id="5-D">ncompCD4</td><td id="5-E">3</td><td id="5-F">0.5</td><td id="5-G">0.5</td><td id="5-H">Scalar</td></tr>
<tr><td id="5-I">Growth boost+competition CD8+ kcompCD4</td><td id="5-J">kcompCD4</td><td id="5-K">3</td><td id="5-L">3.4E+07</td><td id="5-M">3.4E+07</td><td id="5-N"># CD4+/ml</td></tr>
<tr><td id="5-O">Growth boost+competition CD8+ compCD8</td><td id="5-P">compCD8</td><td id="5-Q">3</td><td id="5-R">0.85</td><td id="5-S">0.85</td><td id="5-T"># CD8+/ml</td></tr>
<tr><td id="5-U">Growth boost+competition CD8* w1</td><td id="5-V">w1</td><td id="5-W">3</td><td id="5-X">1e-25</td><td id="5-Y">1e-25</td><td id="5-Z">scalar</td></tr>
</table>
ª Eq. = equations.

<a id='8d5bc9a4-d301-4ac0-a65e-5b901603353c'></a>

Table 8
Definitions and values of model parameters related to extracellular and intracel-
lular Salmonella.

<table id="5-10">
<tr><td id="5-11">Parameter name</td><td id="5-12">Short</td><td id="5-13">Eq.a</td><td id="5-14">Range</td><td id="5-15">Value</td><td id="5-16">Unit</td></tr>
<tr><td id="5-17">Death rate Se</td><td id="5-18">drSe</td><td id="5-19">6</td><td id="5-1a">25-35</td><td id="5-1b">27.8</td><td id="5-1c">d⁻¹</td></tr>
<tr><td id="5-1d">Proliferation rate Se b</td><td id="5-1e">pSe</td><td id="5-1f">6</td><td id="5-1g">25-35</td><td id="5-1h">35</td><td id="5-1i">d⁻¹</td></tr>
<tr><td id="5-1j">Carrying capacity Se</td><td id="5-1k">ccSe</td><td id="5-1l">6</td><td id="5-1m">500,000</td><td id="5-1n">500,000</td><td id="5-1o">#Se/ml</td></tr>
<tr><td id="5-1p">Death rate Si</td><td id="5-1q">drSi</td><td id="5-1r">7</td><td id="5-1s">0.05</td><td id="5-1t">0.05</td><td id="5-1u">d⁻¹</td></tr>
<tr><td id="5-1v">Proliferation rate Si</td><td id="5-1w">pSi</td><td id="5-1x">7</td><td id="5-1y">4.08-7.92</td><td id="5-1z">4.1</td><td id="5-1A">d⁻¹</td></tr>
</table>
a Eq. = equations.
b Proliferation rate is estimated by the following formula: growth rate con-
stant=ln(2)/'doubling time', e.g. Salmonella doubling time is 30 min or, 1/48=0.021
per day, thus growth rate is approximately 33 per day.

<a id='7e8c288a-cd7b-407c-88bb-e7b4bdfe0311'></a>

the set ordinary differential equations (ODEs) which defines the change of the state variables in time (Appendix A) with a dense or banded Jacobian when the problem is stiff. The routine starts applying the non-stiff routine and automatically evaluates the simulation data to select between a non-stiff (Adams) and a stiff (Backward Differ- entiation Formulae) numerical routine. The parameter settings for the LSODA were as follows, 'integrate reduced model' was zero, which instructs COPASI to integrate all ODEs. A 'relative tolerance' value of 1e-6 was used to indicate the relative level of accuracy of the numerical integration of the ODEs, likewise, an 'absolute tolerance' value of 1e-12 was used for the absolute level of accuracy of numerical integration. The maximum number of iterative calculation steps was set to 10,000 for every integration step. Because we lack day 0 immunohistochemistry measurements, realistic initial values of all state variables had to be estimated for this time point (Table 2). Furthermore, a sensitivity analysis was performed within the COPASI environment. By numerical differentiation using finite differences, the generalized sensitivities of parameter values of the model were calculated, with generally a two-dimensional matrix (parameters values vs. state variables) as outcome. The following settings were used: subtask was set to 'time series', function to 'all variables of the model', variable to 'all parameter values'. The delta factor and delta minimum were the default values of 0.001 and 1e-12, respectively. The delta factor is used to determine the delta value for the finite difference numerical differentiation. The product of the current absolute value of the variable and the delta factor is the delta. If the resulting value is smaller than the 'delta minimum' it is discarded and instead the 'delta minimum' is used. Because the program calculates the 'generalized' sensitivity only at the end of a simulation run, multiple end-points were taken for sensitivity analysis (e.g. 1, 2, 4, 8, 12, 21, and 42 days).

<a id='89618a78-ca5e-4e6e-b727-4c686366000a'></a>

2.3. _Model calibration data_

Published data on chicken line A were used to calibrate the model (Schokker et al., 2009, 2010). In short, one-day-old chickens

<a id='84626503-f6a8-443b-8f1c-f0c91c7510b3'></a>

Intestinal tissue<::A microscopic image of intestinal tissue with villi structures. A black rectangular box highlights a small section within the tissue. An arrow points from this highlighted section to a purple three-dimensional cube labeled "Simulation" above it and "1 mL" below it. Fig. 2. Model assumptions. The biological system that was modeled involves a cross section of non-infected jejunal tissue (colored purple) four days post hatch including macrophages (colored brown). Data used for the present modeling study were derived from a jejunal tissue preparation of approximately 1 mL. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.): figure::>

<a id='210b20a4-62c9-4949-89ba-402c2d4de6a0'></a>

(Line A) were inoculated orally with 1 x 10⁵ Salmonella enterica serovar Enteritidis in 0.2 ml Phosphate Buffered Saline (PBS) (van Zijderveld et al., 1992) or with 0.2 ml PBS at day 0. Intestinal samples were taken at 8 h, and at 1, 2, 4, 8, 12, and 21 days post hatch for uninfected or infected chickens. For each time point ten chickens of each group were used. The bacteriological data used in the model are the colony forming units of S. Enteritidis bacteria per ml liver.

<a id='a5b4b950-2b79-4479-b997-191d67402893'></a>

For immunohistochemical examination, the intestinal samples were snap frozen in liquid nitrogen and used to make cryosections. Similar to the procedure described in (Schokker et al., 2010), slides (8 µm) were incubated with monoclonal antibodies against chicken CD4+ cells (1:200 diluted; CT-4, Southern Biotech), or macrophages (1:50 diluted; KUL-01, Southern Biotech), or CD8+ cell (CT-8, 1:200, Southern Biotech). The amount of cells in 1 ml tissue (Fig. 2) was calculated as follows: counting the number of positive stained cells per mm² for each slide using Image-Pro Plus (version 6.2, Media Cybernetics), multiplying this number by 125 to get the number of cells per mm², multiplying this number by 1000 to convert to number of cells per mm³; and finally, calculat-ing an average for each time point and cell type. To minimize the technical variation of the immunohistochemical measurements, we analyzed intestinal slides for a maximum of ten individual chickens per time point, averaging the counts from three areas per slide.

<!-- PAGE BREAK -->

<a id='630d5891-703f-4d42-a39d-e115a0a45280'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='f2533f5f-7093-4d68-89f2-5895bc5d79e6'></a>

81

<a id='0078b6c9-12bc-449d-9698-164a97e6dbe5'></a>

## 2.4. Model evaluation
Model predictions in non-infected chickens were evaluated on six data sets which were independent of the data sets used in model development and calibration. These datasets were obtained from different chicken lines from different studies: (1) a fast growing (van Hemert et al., 2007) and (2) and a slow growing chicken line (van Hemert et al., 2007); (3) chicken line B (Schokker et al., 2012); (4) chicken line C (Schokker et al., 2012); (5) chicken line A (Cornelissen et al., 2009); (6) chicken line D (unpublished work Swinkels and Rebel). Four out of these six studies, two by van Hemert et al. (2007) and two by Schokker et al. (2012) also delivered data that could be used to evaluate the model under the condition of infection with S. Enteritidis for time points post infection.

<a id='1741a9c0-28a7-48bd-8e0a-ecb5776b20ba'></a>

3. Model evaluation and simulation runs

3.1. Model behavior

Figs. 3 and 4 represent the results of simulation runs from hatch (day 0) to day 42. The lines in Fig. 3 show the predicted

<::transcription of the content
: chart::>

Fig. 3. Comparison of model prediction with data of non-infected chickens. In all graphs, the horizontal axis depicts time in days post infection and the vertical axis the number of cells per milliliter in intestinal tissue. Grey curves depict the model prediction after calibration with the immunohistochemical data of line A chicken, whereas black symbols indicate the average of the observed values (max. 10 chicken, 3 observations per chicken). Panel A, Total macrophages (TotalM); panel B, CD4+ cells; and panel C, CD8+ cells.

<a id='d19192eb-1b22-4bb8-9408-5d6bbeae18a4'></a>

model outputs together with the immunohistochemical data (square symbols) of non-infected chickens after calibration with the immunohistochemical data of line A chickens. The lines in Fig. 4 show the predicted model output together with the immunohistochemical data of infected chickens (square symbols). Model predictions in non-infected chickens corresponded with observed values of CD4⁺, CD8⁺ and TotalM. Therefore, the selected cell types in our model and the representation of their interrela- tionships were able to portray the biology of the development, at least in cellular quantitative terms, of the intestinal immune system of chickens in early life. Also for S. Enteritidis infected chickens, predicted values of CD4⁺ and TotalS corresponded with observed values. However, predicted CD8⁺ and TotalM were less reflective of observed values. The observed rapid change in CD8⁺ was not captured by the model. Similar to the experimental conditions, the number of macrophages peaked at 4 days post- infection and subsequently dropped to a stable level, whereas the model predicted a too high peak in TotalM and a too slow return towards homeostatic values (Fig. 4). To assess the extent to which the model reproduced observed values, the R² values were calculated for each observed state variable (Table 9). For non- infected chickens, the R² values for CD4⁺, CD8⁺ and TotalM were all above 0.83, meaning that only 17% of the experimental observa- tions remained unexplained by the model. For the S. Enteritidis infected chickens, CD4⁺ had the highest R² of 0.84, followed by a R² of 0.49 and 0.43 for TotalS and CD8⁺, respectively. The score for TotalM was only 0.26, due to the fact that the model could only reproduce the initial time course of the development of TotalM at 8 h and 1 day post hatch (Fig. 4).

<a id='d418b49c-657e-43a4-a9b6-86688db956b1'></a>

A sensitivity analysis was performed; (1) to investigate how robust the model is in relation to perturbation of parameter values and (2) to identify parameters that the system is more sensitive to, in order to understand the biology of the immunological processes after S. Enteritidis infection. Understanding how the system changes with respect to changes in parameter values could also provide new insights into the biology of immune responses. Several parameters have a relatively high influence on the system in all sampled time-points, namely parameters involved in killing the *Salmonella* bacteria (*kSeMa*, *kSeMr*, and *kSeCD4*; see Suppl. Figs. S1–S3, respectively). This is logical given the fact that when *S. Enteritidis* is present in the system, the killing rates of these bacteria by immune cells will determine the change over time in the bacterial count. Furthermore, it can be concluded that perturbations of these ‘killing’ parameter values have a higher impact in early life (0–8 days) compared to 8–42 days. An example of a parameter value that is robust during the sensitivity analysis is parameter cSeMri, the half-saturation of *Se* on infection of *Mr*, which means that the system will react similarly when more or fewer *Se* were in the system and *Mr* and CD4+ continue to be recruited to eliminate the invading *S. Enteritidis*. This sensitivity analysis shows sensitivity to changes of parameters involved in clearing the *S. Enteritidis* infection, which means that controlling an infection with *S. Enteritidis* is a variable process dependent on multiple variables.

<a id='6ab1cd70-ade2-47be-9c4f-cc740e427507'></a>

3.2. Model evaluation

The model was evaluated against cellular immune data independent studies that were not used to calibrate or parameterize the model. We investigated the robustness of the model and the impact of genetic background of the chicken line on prediction accuracy for intestinal immune development and response to S. Enteritidis infection. The results show chicken-line or chicken-experiment specificity (Fig. 5). In an early stage of intestinal development, observed values compared to model predictions (Fig. 6) for all data sets. However, at a later stage (day 4–21) model

<!-- PAGE BREAK -->

<a id='d1d1a462-0b02-45aa-910c-93d4070e318b'></a>

82

<a id='4bf916fb-2aa0-4117-998c-40a69656b2d2'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='c398fce8-156e-46bb-bb8f-34cef10df587'></a>

A<::Figure: A line graph titled "TotalM". The y-axis is labeled "# / ml" and ranges from 0.00E+00 to 4.50E+07. The x-axis is labeled "days" and ranges from 0 to 40. The graph displays several data points represented by black squares and a light grey curved line. The data points are approximately: (0, 1.00E+07), (0.5, 2.30E+07), (1.5, 2.90E+07), (2.5, 3.90E+07), (6, 2.20E+07), (11, 2.40E+07), (20, 2.80E+07). The grey line shows a trend that increases rapidly, peaks around 3.50E+07 at approximately 5 days, and then slowly decreases and stabilizes around 3.00E+07.: chart::>J

<a id='1447a6ba-7672-41eb-b1ad-b03c821f2456'></a>

B<::line graph titled "CD4+ cells". The y-axis is labeled "# / ml" and ranges from 0.00E+00 to 9.00E+07. The x-axis is labeled "days" and ranges from 0 to 40. Data points are marked with black squares and connected by a smoothed light grey line, showing an initial dip followed by a steady increase and then leveling off.::>

<a id='5f4d1cf6-4ca9-45a4-b344-b79d2098c727'></a>

C<::line graph titled "CD8+ cells". The x-axis is labeled "days" and ranges from 0 to 40 in increments of 10. The y-axis is labeled "# / ml" and ranges from 0.00E+00 to 3.00E+07 in increments of 5.00E+06. Black square data points are plotted, with a light grey curve fitted to them. The approximate data points are: (0, 4.00E+06), (1, 9.00E+06), (2, 1.40E+07), (4, 1.60E+07), (8, 1.00E+07), (12, 2.30E+07), and (20, 2.00E+07). The curve shows an initial increase, peaks around day 12-15 at approximately 2.40E+07, and then gradually decreases to around 2.10E+07 by day 40.: chart::>

<a id='5c11606f-db66-4350-bbe8-8fc85f50da91'></a>

<::D. Line graph titled "Salmonella". The y-axis is labeled "#/ml" and ranges from 0.00E+00 to 1.20E+04. The x-axis is labeled "days" and ranges from 0 to 40. The graph shows a gray curve peaking around day 2-3 and then decreasing, with black square data points plotted at approximately: (0, 0), (1, 6.20E+03), (2, 4.20E+03), (5, 5.20E+03), (8, 1.80E+03), (12, 0), (21, 0).: chart::>

<a id='5de27f9a-322c-4ee1-8ae0-9150edf4138a'></a>

Fig. 4. Comparison of model prediction with data of infected chicken. In all graphs the horizontal axis depicts time in days post infection and the vertical axis the number of cells per cm³ (ml) in intestinal tissue. Grey curves indicate the model prediction, the black symbols indicate the average of the immunohistochemistry data (max. 10 chicken, 3 observation per chicken). (A) Total macrophages (TotalM); (B) CD4+ cells; (C) CD8+ cells, and (D) Salmonella.

<a id='f03c3b3a-db95-4eaa-a280-c082772ec151'></a>

predictions started to deviate increasingly from observed values
(Fig. 5). For 21 to 42 days post hatch no data were available. When
plotting the average observed values for each cell type in time,

<a id='d87b21c2-b894-485a-b441-9fffbfc5ec6e'></a>

Table 9
R² values of predicted versus observed data (Figs. 3 and 4).
<table id="7-1">
<tr><td id="7-2">Cell type</td><td id="7-3">Non-infected</td><td id="7-4">Infected</td></tr>
<tr><td id="7-5">Total macrophages</td><td id="7-6">0.83</td><td id="7-7">0.26</td></tr>
<tr><td id="7-8">CD4+ cells</td><td id="7-9">0.90</td><td id="7-a">0.84</td></tr>
<tr><td id="7-b">CD8+ cells</td><td id="7-c">0.88</td><td id="7-d">0.49</td></tr>
<tr><td id="7-e">Total S. Enteritidis</td><td id="7-f">NA</td><td id="7-g">0.43</td></tr>
</table>
NA, not available.

<a id='49e045d1-a155-4970-819b-b9fe0ce8900e'></a>

a high variation in the number of immune cells between experiments and between chicken lines was observed (Fig. 7), which differs from the present parameterization of the model and hence the model could not reproduce the number of cells at these late time-points (21–42 days post hatch).

<a id='d70c656a-7ef5-4d0d-89dc-96893d4edb4a'></a>

## 4. Discussion
The dynamics of intestinal immune development at the gene expression level have previously been investigated for both non-infected (Schokker et al., 2009) and S. Enteritidis infected chickens (Schokker et al., 2010; Withanage et al., 2004). These studies concluded that the well-orchestrated spatiotemporal pattern of immune development in non-infected chickens is considerably disturbed after an oral infection with S. Enteritidis. The dynamics of cellular immunity was however not covered by these studies. Furthermore, immuno-histochemical measurements, e.g. immune cell counts, do not provide enough information on the interactions in time between cellular components of the intestinal immune system and the response dynamics against invading pathogens. Therefore, a dynamic model was constructed that represents the development of the cellular branch of the intestinal innate and adaptive immune system of chickens from 0 to 42 days after hatch. Such a mathematical model delivers a more quantitative understanding of the interactions between the individual cellular components of the immune system and may help explain the observed behavior of the immune system in response to external stimuli. The model provides the opportunity to run simulations to identify and test how different conditions (chan-ging model inputs and some parameter estimates) affect the response in intestinal immune system development and immune response to infection in the chicken. In this manner, the model can be a valuable tool to direct the setup of animal experimentation in order to formulate and test new hypotheses.

<a id='ed7b46a4-8fab-46e0-b551-fd55ea401172'></a>

4.1. Modeling development without infection

A growth boost for Mr, CD4+ and CD8+ was introduced in the model. The growth boost equations represent the rapid development of the intestine, including the intestinal immune system, after hatch (Geyra et al., 2001; Sklan, 2001; Uni et al., 2000). Furthermore, it was assumed that the small areas of the jejunum, which were sampled here for immunohistochemical analysis, are representative of the whole tissue. Although the chickens were selected based on similar weight and numbers of caecal secreted Salmonella, variation in the number of cells per ml of tissue between chickens remained high (Fig. 7). Repeated measurements within the same individual chicken in time could have helped reduce the variation; however, this was not an option because of the need to sacrifice the chicken to obtain immunohistochemical data. Moreover, the variation between chickens is probably inflated by converting the two dimensional data to three dimensional (from square centimeters to cubical centimeters). The deviance between predicted and observed data may hence have a methodological cause as well. This conversion of mm² to mm³

<!-- PAGE BREAK -->

<a id='70a9d307-a944-4347-bb5e-0712f85dbfba'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='7d065d85-75a6-47dc-93ee-96ce9ccbf867'></a>

83

<a id='749ada34-f3eb-4f96-9935-242b8b52b409'></a>

<::Figure: A multi-panel figure displaying six line graphs (A-F) showing cell counts over time, with two main conditions (Non-infected and Infected) and three cell types (TotalM, CD4+, CD8+). The x-axis for all panels is "Time (dpi)" ranging from 0 to 40. The y-axis for all panels is "# / ml". Each panel includes a solid black line representing the "model" and various data points represented by different symbols. A legend at the bottom defines the symbols: "model" (solid line), "Fast" (triangle), "Slow" (X), "Line B" (asterisk), "Line C" (circle), "Line A" (plus sign), and "Line D" (square).::>

<::Panel A: TotalM, Non-infected::>

<::Panel A shows TotalM cell counts in non-infected conditions. The y-axis ranges from 0.00E+00 to 1.00E+08. Data points are scattered, generally around or below 5.00E+07. The model line is relatively flat, hovering around 2.50E+07.::>

<::Panel B: TotalM, Infected::>

<::Panel B shows TotalM cell counts in infected conditions. The y-axis ranges from 0.00E+00 to 6.00E+07. Data points show an initial rise then scatter. The model line increases to a peak around 3.50E+07 at approximately 5 dpi, then gradually decreases and stabilizes around 2.50E+07.::>

<::Panel C: CD4+, Non-infected::>

<::Panel C shows CD4+ cell counts in non-infected conditions. The y-axis ranges from 0.00E+00 to 9.00E+07. Data points are scattered. The model line shows a gradual increase from approximately 1.00E+07 to 8.00E+07 over the 40 dpi period.::>

<::Panel D: CD4+, Infected::>

<::Panel D shows CD4+ cell counts in infected conditions. The y-axis ranges from 0.00E+00 to 9.00E+07. Data points show an initial drop followed by some recovery or scatter. The model line shows a sharp initial drop from approximately 1.00E+07 to below 1.00E+07, followed by a sharp increase to approximately 8.00E+07.::>

<::Panel E: CD8+, Non-infected::>

<::Panel E shows CD8+ cell counts in non-infected conditions. The y-axis ranges from 0.00E+00 to 1.00E+08. Data points are scattered. The model line shows an initial increase from approximately 5.00E+06 to 5.00E+07, then remains flat.::>

<::Panel F: CD8+, Infected::>

<::Panel F shows CD8+ cell counts in infected conditions. The y-axis ranges from 0.00E+00 to 4.00E+07. Data points show an initial increase then scatter. The model line shows an initial increase from approximately 5.00E+06 to a peak around 2.50E+07 at approximately 15 dpi, then gradually decreases and stabilizes around 2.00E+07.::>

<a id='6d02f82c-8053-42d0-8254-826711272283'></a>

Fig. 5. Model evaluation against observed values for macrophages, CD4+ cells and CD8+ cells in both non-infected and infected jejunum of chicken. For all experiments the number of cells per cm³ (ml) intestinal tissue is plotted against time in days post infection. Total macrophages (TotalM): (A) non-infected; and (B) infected chicken, CD4+ cells; (C) non-infected; and (D) infected chicken, and CD8+ cells: (E), non-infected; and (F), infected chicken. Datasets of the following lines and/or studies are included for non-infected chicken: (1) fast growing (van Hemert et al., 2007) and (2) slow growing chicken lines (van Hemert et al., 2007); (3) chicken line B (Schokker et al., 2012) and (4) chicken line C (Schokker et al., 2012); (5) chicken line A (Cornelissen et al., 2009); and (6) chicken line D an unpublished study. Whereas for S. Enteritidis infected chicken only four out of these six studies were available, including the two datasets of van Hemert et al. (2007)) and the two datasets of Schokker et al. (2012).

<a id='cb7b7c4a-d4b0-438e-bb5a-5181ac3b34ea'></a>

was necessary to ensure that both the bacteriological and immunohistochemistry data were expressed in the same unit of tissue volume. To investigate whether the predicted values for the model variables and the predicted interactions between them were plausible, predictions were plotted against the average values of the immunohistochemical observations of non-infected chickens and R&sup2; values were calculated (Fig. 3 and Table 9). Using these averaged results, the selected state variables and their relationships seemed to be represented accurately in the model.

<a id='877b90e3-e047-444f-a82b-474308871a6f'></a>

4.2. Modeling development with S. Enteritidis infection

S. Enteritidis colonizes the intestine and (trans)migrates to the spleen, liver and other tissues. We assumed that the same

<a id='bd571315-7136-4897-849e-99904919224e'></a>

percentage of the pathogen inoculum crosses the intestinal barrier
in young chicken as observed in adult mice (Collins and Carter,
1974), which is approximately 0.25% at 6 h after administration of
the inoculum (Carter and Collins, 1974). However, even a (very)
small number of *Salmonella* bacteria reaching the bloodstream
already can trigger a systemic infection (Collins and Carter, 1974).
In the present study we assumed that approximately 200 bacteria
will enter the system at day zero. Furthermore, we assumed that
the number of colony forming units (CFUs) in the liver (Schokker
et al., 2010) is representative of the amount of extracellular
*S. Enteritidis* present in the entire intestinal tissue. The host evokes
an immune response against the intracellular and extracellular
*S. Enteritidis* in the intestinal tissue. Extracellular *S. Enteritidis* will
be phagocytized by macrophages, but can survive within them

<!-- PAGE BREAK -->

<a id='0d690c98-9f71-4240-be8e-2cedfc112c30'></a>

84

<a id='de821883-54a8-4bb5-9df9-3f2b5831ff6d'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='891c6e6d-09e7-42fe-ac60-e73c69e9e193'></a>

<::chart: Fig. 6. Biological variation between chicken in number of macrophages in chicken intestine after hatching. Variation in immunohistochemistry data (this paper) of total macrophages (TotalM) in both non-infected (panel A) and S. Enteritidis infected chicken (panel B). On the vertical axis the number of TotalM per cm³ (ml) intestinal tissue is depicted and on the horizontal axis the time in days post infection. Observations for individual measurements are depicted by a grey asteriks, whereas the average per time point is depicted by a black square.  

**Panel A: Non-infected**
- **Type:** Scatter plot with connected average points.
- **Y-axis:** # M / ml (Number of TotalM per cm³ (ml) intestinal tissue), ranging from 0.00E+00 to 6.00E+07.
- **X-axis:** Time (days), ranging from 0 to 25.
- **Legend:** 
  - individual measurement: [x] (grey asterisk)
  - avg timepoint: [x] (black square)
- **Data points:** Individual measurements are scattered at time points 0, ~2, ~4, ~7, ~11, ~12, ~21 days. Average time points are connected by a line.

**Panel B: Salmonella infected**
- **Type:** Scatter plot with connected average points.
- **Y-axis:** # M / ml (Number of TotalM per cm³ (ml) intestinal tissue), ranging from 0.00E+00 to 1.00E+08.
- **X-axis:** Time (days), ranging from 0 to 25.
- **Legend:** 
  - individual measurement: [x] (grey asterisk)
  - avg timepoint: [x] (black square)
- **Data points:** Individual measurements are scattered at time points 0, ~2, ~4, ~7, ~11, ~12, ~21 days. Average time points are connected by a line.::>

<a id='b84c39ef-2d6b-4411-aadf-9c76d73517d5'></a>

<::chart: Line graph titled "Fig. 7. Prediction of the effect of an increase in initial number of macrophages on number of Salmonella in chicken intesine after hatching." The x-axis is labeled "Time (days)" and ranges from 0 to 25. The y-axis is labeled "number of Salmonella / ml" and ranges from 0 to 12000. The chart displays two predicted dynamics curves and experimental data points for two chicken lines. A legend indicates: "Model" (grey dashed line), "Simulation (higher initial Mr)" (black solid line), "Line A" (grey diamond), and "Line C" (black triangle).The "Model" (grey dashed line) shows a sharp increase in Salmonella from 0 to a peak of approximately 10,800 at around 1.5 days, then a gradual decrease to near 0 by day 15-20.The "Simulation (higher initial Mr)" (black solid line) shows a sharp increase from 0 to a peak of approximately 1,100 at around 1.5 days, then a gradual decrease to near 0 by day 5-7.Experimental data points for "Line A" (grey diamond) are: (1, 6200), (2, 4000), (4, 5300), (8, 2000), (12, 100), (21, 50).Experimental data points for "Line C" (black triangle) are: (1, 300), (2, 1000), (4, 100), (8, 2000), (12, 100), (21, 50).The x-axis depicts time after infection in days, whereas the y-axis depicts the number of Salmonella per cm³ (ml) intestinal tissue. The curves depict predicted (grey, dashed) dynamics of the number of Salmonella in time by the model, and predicted dynamics when starting with a a higher number of total macrophages (TotalM) at hatch (black, solid). In addition, experimental data are plotted for two genetically different chicken lines: line A on which the model was calibrated (grey diamond); and line C (Schokker et al., 2012) which represents the case study which had an increased initial number of TotalM (black triangle).::>

<a id='f9691ca3-c64f-4dfc-b809-5ef37f04046f'></a>

(Lindgren et al., 1996). Phagocytosis and migration of macrophages results in a systemic spread of Salmonella in the host. The severity of a systemic infection depends on a variety of factors such as the immune response, barrier functions, genetic background of the host, and the genetic background of the Salmonella (Schokker et al., 2012). Clearance of an infection is dependent on the immune system, where time and efficacy of the immune response are of importance. Active recruitment of macrophages and the involvement of CD8$^{+}$ in the immune response against S. typhimurium (Lo et al., 1999) suggests a T helper 1 response, and we expect a similar response to S. Enteritidis. Previous studies showed that the ability to transfer protective immunity to virulent S. typhimurium is impaired by exhaustion of either CD8$^{+}$ or CD4$^{+}$ (Guilloteau et al., 1993; Mastroeni et al., 1992, 1993) meaning that both cell types are of importance in host response against Salmonella. Therefore, the focus in the current study was primarily on macrophages, CD4$^{+}$ and CD8$^{+}$ as elements of the immune response, and not on B cells because they are of little or no importance for clearance of the pathogen (Beal et al., 2006).

<a id='e4cbb1f8-ff21-4d61-b7c8-854b0b660e2a'></a>

To investigate the extent to which our model representation of the response to infected status was realistic, R² values were calculated for the comparison of predicted against observed TotalM, CD4⁺, CD8⁺, and TotalS. Predicted TotalM did not accurately describe observed numbers, which suggests that some processes in the immune system or some external influencing factors were misrepresented or neglected. The model predicts the number of immune cells in the system, however, the activity of these immune cells is not taken into account, which could be a reason for the misfit. Cytokines are good candidates of such an improperly represented factor, because they have important functions in the regulation of the cellular immune response. It could be that the addition of cytokines as a state variable to the model representa- tion will improve the explanation of predicted macrophage dynamics. Cytokines are involved in regulating the activity of immune cells, as well as effector mechanisms such as production of antimicrobial peptides, oxygen radicals and lysozomes (Izcue et al., 2009), and are hence good candidates for implementation in the model. Most of the variation in CD4⁺ was captured by the model, as indicated by the high R² of 0.84. The observed number of CD8⁺ showed rapid fluctuations in time, which could not be captured. Its R² was only 0.49, but the model was able to generate a similar trend to that in observed data. The model predicted that Salmonella was cleared at approximately 6 days post infection, whereas the observations show clearance only at 12 days post infection (Fig. 4; R² of 0.43, Table 9). This difference between the model and the experimental data indicates that the representation of the interactions between macrophages and S. Enteritidis, and their relationships with other influencing factors has to be improved.

<a id='f929cdd4-ebe2-46c4-8694-2d48a3c11d7d'></a>

4.3. Model application and future model development

The present mathematical model can be used to simulate the course of a S. Enteritidis infection in the chicken intestine (jejunum) during the development of the gastrointestinal tract and chick growth. Model inputs such as the initial number of immunological cells can be varied, or parameter values for recruitment rate, proliferation rate, or death rate can be based on more specific information on genetic background or physiological (experimental) condition of the chicken. The present model was calibrated with chicken line A, and model simulations clearly showed that it has to be adapted to be able to reproduce the observations obtained for genetically different chicken lines. By simply changing the initial number of Mr it was possible to reproduce the observed differences for a genetically different chicken line C, which has a higher number of macrophages at

<!-- PAGE BREAK -->

<a id='f966d8e0-fc1c-48ea-930f-83d5d1b77e5f'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='a0055347-5b95-43ee-a729-28085c3905f6'></a>

85

<a id='db72c44c-6657-4769-95b8-7c4d6b88c6fa'></a>

hatch. When doubling the initial number of Mr at hatch, the severity of a systemic infection decreases by approximately an order of magnitude (Fig. 7), which is in line with the experimental data for line C. This example shows how the model can be used to test the effect of the different state variables on the severity of infection. Multiple scenarios can be run, but it seems the model will become specific enough for accurate prediction only after parameterization for different chicken lines, different Salmonella strains, or different experimental or physiological conditions. The evaluation of the model outcome aids in setting up new animal trials and to formulate and test new hypothesis on observed variation in intestinal immune response and the impact of infection on chicken performance after hatching. In further model development it would be necessary to include the separation between CD8+ and γδ T cells, the effect of epithelial cells and cytokines. Because γδ T cells are important for the course of Salmonella Typhimurium infection in young chicks (Berndt and Methner, 2001; Berndt et al., 2007; Li et al., 2012; Pieper et al., 2011), it can be helpful to model this subpopulation of T cells separately. In doing so, additional dynamical aspects can be incorporated which relate to more specific aspects of the underlying biology of intestinal immune response. It is known that epithelial cells are able to contribute to the clearance of Salmonella by secretion of cytokines, and by the subsequent mobilization and modulation of the activity of immune cells. For example, the recruitment and activation of macrophages was shown to be influenced by the local concentrations of IL8 (Hobbie et al., 1997), IFNG, IL4, and IL13 (Gordon, 2003). Another example of improving the model would be the use of Single Nucleotide Polymorphisms (SNPs). Chicken lines differ in their susceptibility to Salmonella and/or in the underlying phenotypes (Schokker et al., 2012). Genetic association studies have already identified quantitative trait loci involved in determining the susceptibility of chicken to Salmonella (Fife et al., 2010). Knowledge of the causal SNPs and affected gene functions may allow to extend the model with parameters related to genetic diversity and its consequences for the intestinal immune system response.

<a id='5ae09357-2f56-4ae5-aaa7-ce7809f97926'></a>

## 4.4. Infection models

Several models for a variety of bacterial infections in humans and mice have been described already in literature. Examples are infection with *Helicobacter pylori* (Blaser and Kirschner, 1999, 2007; Joseph and Kirschner, 2004; Kirschner and Blaser, 1995), *Vibrio cholerae* (Spagnuolo et al., 2011), *Mycobacterium tuberculosis* (Gammack et al., 2004; Pieters and Gatfield, 2002; Raman et al., 2010; Wigginton and Kirschner, 2001), or Necrotizing enterocolitis (*Pseudomonas aeruginosa*) (Upperman et al., 2007). In contrast to these models, all of which deal with a matured intestinal immune system, the model described in the present study aims to represent the developing intestinal immune system. In the *Helicobacter pylori* model described by Kirschner and Blaser (1995) four state variables were defined: bacteria in mucus layer, bacteria adherent to epithelial layer, nutrients and effectors. A small number of state variables was used because the survival method of *Helicobacter pylori* was not known. The model contained an auto regulatory network in which inflammation triggers nutrient release for the bacteria. A subsequent model also included the host-pathogen interaction by adding another state variable (Blaser and Kirschner, 1999). Although details of the working mechanisms of the host response were not known, they included innate and adaptive immunity as well as iron-sequestration. This work showed the importance of mathematical modelling as a tool to improve the understanding of the (immune) response against invading *Helicobacter pylori* in the stomach.

<a id='8014191e-ceb0-4edb-803d-2ab021e1e4a3'></a>

The objective of the model of an infection with _Vibrio cholera_
(Spagnuolo et al., 2011) was to investigate both host and bacterial
factors that contribute to colonization and lead to either infection
or clearance. Contrary to the present model, which only categor-
ized the bacteria as either intra- or extracellular, the model of
Spagnuolo et al. (2011) defined three different sub-populations of
bacterial cells; luminal, mucosal, and epithelium (adherent) popu-
lations. Their approach of subdividing the bacterial populations
could be a useful extension to the present model.

<a id='7c339565-45cb-4e0d-b255-033a9d46ee48'></a>

Gammack et al. (2005) showed various *M. tuberculosis* models which represent different biological scales, including the scale of cellular dynamics similar to the approach described in the present study. Furthermore, they clearly show that the mathematical framework needed depends on the research questions posed. The model described by Wigginton and Kirschner (2001) represents the temporal dynamics of immune cells during the *M. tuberculosis* infection in lung tissue. Another model includes partial differential equations to take into account the structure of the granulomas and spatial distribution. exclusively describing the initial innate response of macrophages (Gammack et al., 2004). These *M. tuberculosis* models are comparable to the present *Salmonella* infection model because in both infections the bacteria also evade the immune system.

<a id='d61220e9-5cda-47e4-bfb8-013eb527029f'></a>

Necrotizing enterocolitis (NEC) could be caused by the bacteria Pseudomonas aeruginosa. The model developed by Upperman et al. (2007) describes the dynamics of the infection response and it considers two physical compartments: tissue and blood. Multiple cell types are represented including macrophages, neutrophils, dendritic cells and helper T cells (Th1 and Th2), and pathogens. It is known that NEC exhibits spatial characteristics and therefore an extended model version was needed which was described by Barber et al. (2013). They developed a model incorporating such spatial characteristics by developing a three-dimensional representation of this intestinal infection. It was demonstrated that changing the initial shape of the infection significantly affects overall model outcome and predicted infection response. The present study only considered intestinal tissue as single physical compartment. With future efforts spatial aspects of the infection response may be added.

<a id='dad1e6d7-a1cc-41b3-bd9e-f16db2ab8a81'></a>

To conclude, although several models have already been developed which address the immune response of invading bacteria in the intestinal environment, they differ on several aspects depending on the research questions posed and in their specific modelling aim. So far, none of these models dealt with the development of the immune response in reaction to an infection as described in the present study.

<a id='992ced63-b9a7-46cc-b59e-ff4de99ed168'></a>

5. Conclusions

As a conceptual approach to quantify and integrate current knowledge on the intestinal immune system in the chick, a dynamic mechanistic model was constructed which represents the dynamics of major phenomena of cellular immune develop-ment of both the innate and the adaptive immune system in young non-infected chickens and in chickens infected with S. Enteritidis. Observed data regarding the quantity of immune cells were accurately reproduced by the model for non-infected animals but to a lesser extent for infected animals. Although the model was shown to be specific for the specific chicken line it was calibrated for, it seems relatively easy to simulate the cellular immune development in genetically different chicken lines by changing some specific parameter values. Initial model simula-tions already show the potential of the model to contribute to theory on how important input and parameters affect the simu-lated immune response. Improvements to be made to the model

<!-- PAGE BREAK -->

<a id='a8ccfa2e-496f-428a-b6a0-42eb19b86cbc'></a>

86

<a id='6f610dcb-461d-48d4-a0f3-4057138ba3a7'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='2c550b13-5dfa-434b-baeb-bdd2a4ea1f31'></a>

are thought to be the inclusion of cytokines, data on SNP or
quantitative measurements, or a representation of theory on
factors that influence the activity of cells (e.g. macrophages).

<a id='fa26fb0d-8443-4018-a03d-abee20825368'></a>

## Acknowledgements

We wish to thank Jaap Molenaar and Apri Mochamed for fruitful discussions regarding the mathematical model and Henk Parmentier for critical assessment of the immunological interactions. These results are obtained through the EC-funded FP6 Integrated Project SABRE—Cutting Edge Genomics for Farm Animal Breeding (contract no. FOOD-CT-2006-016250), EADGENE a network of excellence (contract no. FOOD-CT-2004-506416), and IP/OP—Systems Biology which was financially supported by the Ministry of Agriculture, Nature and Food Quality (BAS no. 4434660800). The text represents the authors' views and does not necessarily represent a position of the Commission who will not be liable for the use made of such information.

<a id='3b53db46-8ae3-4831-83ec-582d751fa4ac'></a>

## Appendix A. Supporting information
Supplementary data associated with this article can be found in the online version at http://dx.doi.org/10.1016/j.jtbi.2013.04.005.

<a id='76d2a7bf-de5d-44b2-b0c5-7f987106f726'></a>

## References

Abshire, K.Z., Neidhardt, F.C., 1993. Growth rate paradox of *Salmonella typhimurium* within host macrophages. J. Bacteriol. 175, 3744-3748.
Balcewicz-Sablinska, M.K., Gan, H., Remold, H.G., 1999. Interleukin 10 produced by macrophages inoculated with *Mycobacterium avium* attenuates mycobacteria-induced apoptosis by reduction of TNF-alpha activity. J. Infect. Dis. 180, 1230-1237.
Barber, J., Tronzo, M., Horvat, C., Clermont, G., Upperman, J., Vodovotz, Y., Yotov, I., 2013. A three-dimensional mathematical and computational model of necrotizing enterocolitis. J. Theor. Biol. 322, 17-32, http://dx.doi.org/10.1016/j.jtbi.2012.11.018.
Beal, R.K., Powers, C., Davison, T.F., Barrow, P.A., Smith, A.L., 2006. Clearance of enteric *Salmonella enterica* serovar Typhimurium in chickens is independent of B-cell function. Infect. Immun. 74, 1442-1444.
Berndt, A., Methner, U., 2001. Gamma/delta T cell response of chickens after oral administration of attenuated and non-attenuated *Salmonella typhimurium* strains. Vet. Immunol. Immunopathol. 78, 143-161.
Berndt, A., Wilhelm, A., Jugert, C., Pieper, J., Sachse, K., Methner, U., 2007. Chicken cecum immune response to *Salmonella enterica* serovars of different levels of invasiveness. Infect. Immun. 75, 5993-6007.
Blaser, M.J., Kirschner, D., 1999. Dynamics of *Helicobacter pylori* colonization in relation to the host response. Proc. Nat. Acad. Sci. U.S.A. 96, 8359-8364.
Blaser, M.J., Kirschner, D., 2007. The equilibria that allow bacterial persistence in human hosts. Nature 449, 843-849.
Brown, S.P., Cornell, S.J., Sheppard, M., Grant, A.J., Maskell, D.J., Grenfell, B.T., Mastroeni, P., 2006. Intracellular demography and the dynamics of *Salmonella enterica* infections. PLoS Biol. 4, e349.
Caramalho, I., Lopes-Carvalho, T., Ostler, D., Zelenay, S., Haury, M., Demengeot, J., 2003. Regulatory T cells selectively express toll-like receptors and are activated by lipopolysaccharide. J. Exp. Med. 197, 403-411.
Carter, P.B., Collins, F.M., 1974. The route of enteric infection in normal mice. J. Exp. Med. 139, 1189-1203.
Cheroutre, H., Lambolez, F., Mucida, D., 2011. The light and dark sides of intestinal intraepithelial lymphocytes. Nat. Rev. Immunol. 11, 445-456.
Cole, S.W., Conti, G., Arevalo, J.M., Ruggiero, A.M., Heckman, J.J., Suomi, S.J., 2012. Transcriptional modulation of the developing immune system by early life social adversity. Proc. Nat. Acad. Sci. U.S.A. 109, 20578-20583.
Collins, F.M., Carter, P.B., 1974. Cellular immunity in enteric disease. Am. J. Clin. Nutr. 27, 1424-1433.
Cornelissen, J.B., Swinkels, W.J., Boersma, W.A., Rebel, J.M., 2009. Host response to simultaneous infections with *Eimeria acervulina, maxima* and *tenella*: a cumulation of single responses. Vet. Parasitol. 162, 58-66.
Fife, M.S., Howell, J.S., Salmon, N., Hocking, P.M., van Diemen, P.M., Jones, M.A., Stevens, M.P., Kaiser, P., 2010. Genome-wide SNP analysis identifies major QTL for *Salmonella* colonization in the chicken. Anim. Genet..
Flesch, I.E., Kaufmann, S.H., 1990. Activation of tuberculostatic macrophage functions by gamma interferon, interleukin-4, and tumor necrosis factor. Infect. Immun. 58, 2675-2677.

<a id='f25b3796-98b4-4bcd-97e7-f2e0bfe2b5e0'></a>

Gammack, D., Doering, C.R., Kirschner, D.E., 2004. Macrophage response to Mycobacterium tuberculosis infection. J. Math. Biol. 48, 218-242.
Gammack, D., Ganguli, S., Marino, S., Segovia-Juarez, J., Kirschner, D.E., 2005. Understanding the immune response in tuberculosis using different mathema- tical models and biological scales. Multiscale Model. Simul. 3, 312-345.
Garcia-del Portillo, F., 2001. Salmonella intracellular proliferation: where, when and how? Microb. Infect. 3, 1305-1311.
Geyra, A., Uni, Z., Sklan, D., 2001. Enterocyte dynamics and mucosal development in the posthatch chick. Poult. Sci. 80, 776-782.
Ghebremicael, S.B., Hasenstein, J.R., Lamont, S.J., 2008. Association of interleukin-10 cluster genes and Salmonella response in the chicken. Poult. Sci. 87, 22-26.
Gordon, S., 2003. Alternative activation of macrophages. Nat. Rev. Immunol. 3, 23-35.
Guilloteau, L., Buzoni-Gatel, D., Bernard, F., Lantier, I., Lantier, F., 1993. Salmonella abortusovis infection in susceptible BALB/cby mice: importance of Lyt-2+ and L3T4+ T cells in acquired immunity and granuloma formation. Microb. Pathog. 14, 45-55.
Hara, T., Mizuno, Y., Takaki, K., Takada, H., Akeda, H., Aoki, T., Nagata, M., Ueda, K., Matsuzaki, G., Yoshikai, Y., et al., 1992. Predominant activation and expansion of V gamma 9-bearing gamma delta T cells in vivo as well as in vitro in Salmonella infection. J. Clin. Invest. 90, 204-210.
Hobbie, S., Chen, L.M., Davis, R.J., Galan, J.E., 1997. Involvement of mitogen-activated protein kinase pathways in the nuclear responses and cytokine production induced by Salmonella typhimurium in cultured intestinal epithelial cells. J. Immunol. 159, 5550-5559.
Hoops, S., Sahle, S., Gauges, R., Lee, C., Pahle, J., Simus, N., Singhal, M., Xu, L., Mendes, P., Kummer, U., 2006. COPASI-a Complex PAthway Simulator. Bioinformatics 22, 3067-3074.
Hormaeche, C.E., 1980. The in vivo division and death rates of Salmonella typhimurium in the spleens of naturally resistant and susceptible mice measured by the superinfecting phage technique of Meynell. Immunology 41, 973-979.
Iwasaki, A., Medzhitov, R., 2010. Regulation of adaptive immunity by the innate immune system. Science 327, 291-295.
Izcue, A., Coombes, J.L., Powrie, F., 2009. Regulatory lymphocytes and intestinal inflammation. Annu. Rev. Immunol. 27, 313-338.
James, S.P., 1991. Mucosal T-cell function. Gastroenterol. Clin. North Am. 20, 597-612.
Janeway Jr., C.A., Medzhitov, R., 2002. Innate immune recognition. Annu. Rev. Immunol. 20, 197-216.
Joseph, I.M., Kirschner, D., 2004. A model for the study of Helicobacter pylori interaction with human gastric acid secretion. J. Theor. Biol. 228, 55-80.
Kaiser, M.G., Cheeseman, J.H., Kaiser, P., Lamont, S.J., 2006. Cytokine expression in chicken peripheral blood mononuclear cells after in vitro exposure to Salmo- nella enterica serovar Enteritidis. Poult. Sci. 85, 1907-1911.
Kelly, D., Coutts, A.G., 2000. Early nutrition and the development of immune function in the neonate. Proc. Nutr. Soc. 59, 177-185.
Kirschner, D.E., Blaser, M.J., 1995. The dynamics of Helicobacter pylori infection of the human stomach. J. Theor. Biol. 176, 281-290.
Kramer, J., Malek, M., Lamont, S.J., 2003. Association of twelve candidate gene polymorphisms and response to challenge with Salmonella enteritidis in poultry. Anim. Genet. 34, 339-348.
Kunisawa, J., Takahashi, I., Kiyono, H., 2007. Intraepithelial lymphocytes: their shared and divergent immunological behaviors in the small and large intestine. Immunol. Rev. 215, 136-153.
Lewinsohn, D.M., Bement, T.T., Xu, J., Lynch, D.H., Grabstein, K.H., Reed, S.G., Alderson, M.R., 1998. Human purified protein derivative-specific CD4+ T cells use both CD95-dependent and CD95-independent cytolytic mechanisms. J. Immunol. 160, 2374-2379.
Lewis, M.C., Inman, C.F., Patel, D., Schmidt, B., Mulder, I., Miller, B., Gill, B.P., Pluske, J., Kelly, D., Stokes, C.R., Bailey, M., 2012. Direct experimental evidence that early-life farm environment influences regulation of immune responses. Pediatr. Allergy Immunol. 23, 265-269.
Li, Z., Zhang, C., Zhou, Z., Zhang, J., Tian, Z., 2012. Small intestinal intraepithelial lymphocytes expressing CD8 and T cell receptor gammadelta are involved in bacterial clearance during Salmonella enterica serovar Typhimurium infection. Infect. Immun. 80, 565-574.
Lindgren, S.W., Stojiljkovic, I., Heffron, F., 1996. Macrophage killing is an essential virulence mechanism of Salmonella typhimurium. Proc. Nat. Acad. Sci. U.S.A. 93, 4197-4201.
Lo, W.F., Ong, H., Metcalf, E.S., Soloski, M.J., 1999. T cell responses to Gram-negative intracellular bacterial pathogens: a role for CD8+ T cells in immunity to Salmonella infection and the involvement of MHC class Ib molecules. J. Immunol. 162, 5398-5406.
Lowrie, D.B., Aber, V.R., Carrol, M.E., 1979. Division and death rates of Salmonella typhimurium inside macrophages: use of penicillin as a probe. J. Gen. Microbiol. 110, 409-419.
Mastroeni, P., Villarreal-Ramos, B., Hormaeche, C.E., 1992. Role of T cells, TNF alpha and IFN gamma in recall of immunity to oral challenge with virulent salmonellae in mice vaccinated with live attenuated aro- Salmonella vaccines. Microb. Pathog. 13, 477-491.
Mastroeni, P., Villarreal-Ramos, B., Hormaeche, C.E., 1993. Adoptive transfer of immunity to oral challenge with virulent salmonellae in innately susceptible BALB/c mice requires both immune serum and T cells. Infect. Immun. 61, 3981-3984.
Medzhitov, R., Janeway Jr., C., 2000. Innate immunity. N. Engl. J. Med. 343, 338-344.

<!-- PAGE BREAK -->

<a id='c0d6eea7-2fe9-45f1-a82f-ec5c84df80b9'></a>

D. Schokker et al. / Journal of Theoretical Biology 330 (2013) 75-87

<a id='a618b239-c02c-40fd-b24d-c33a96f63f13'></a>

87

<a id='dedbbb18-b212-4025-8d99-de87f73f789a'></a>

Monack, D.M., Raupach, B., Hromockyj, A.E., Falkow, S., 1996. Salmonella typhimur-
ium invasion induces apoptosis in infected macrophages. Proc. Nat. Acad. Sci. U.
S.A. 93, 9833–9838.
Oh, Y.K., Alpuche-Aranda, C., Berthiaume, E., Jinks, T., Miller, S.I., Swanson, J.A., 1996.
Rapid and complete fusion of macrophage lysosomes with phagosomes con-
taining Salmonella typhimurium. Infect. Immun. 64, 3877–3883.
Pieper, J., Methner, U., Berndt, A., 2011. Characterization of avian gammadelta T-cell
subsets after Salmonella enterica serovar Typhimurium infection of chicks.
Infect. Immun. 79, 822–829.
Pieters, J., Gatfield, J., 2002. Hijacking the host: survival of pathogenic mycobacteria
inside macrophages. Trends Microbiol. 10, 142–146.
Raman, K., Bhat, A.G., Chandra, N., 2010. A systems perspective of host-pathogen
interactions: predicting disease outcome in tuberculosis. Mol. Biosyst. 6,
516–530.
Richter-Dahlfors, A., Buchan, A.M., Finlay, B.B., 1997. Murine salmonellosis studied
by confocal microscopy: Salmonella typhimurium resides intracellularly inside
macrophages and exerts a cytotoxic effect on phagocytes in vivo. J. Exp. Med.
186, 569–580.
Rojas, M., Barrera, L.F., Puzo, G., Garcia, L.F., 1997. Differential induction of apoptosis
by virulent Mycobacterium tuberculosis in resistant and susceptible murine
macrophages: role of nitric oxide and mycobacterial products. J. Immunol. 159,
1352–1361.
Romagnani, S., 2006. Regulation of the T cell response. Clin. Exp. Allergy 36,
1357–1366.
Schokker, D., Hoekman, A.J., Smits, M.A., Rebel, J.M., 2009. Gene expression patterns
associated with chicken jejunal development. Dev. Comp. Immunol. 33,
1156–1164.
Schokker, D., Smits, M.A., Hoekman, A.J., Parmentier, H.K., Rebel, J.M., 2010. Effects
of Salmonella on spatial-temporal processes of jejunal development in chickens.
Dev. Comp. Immunol. 34, 1090–1100.
Schokker, D., Peters, T.H., Hoekman, A.J., Rebel, J.M., Smits, M.A., 2012. Differences
in the early response of hatchlings of different chicken breeding lines to
Salmonella enterica serovar Enteritidis infection. Poult. Sci. 91, 346–353.
Sklan, D., 2001. Development of the digestive tract of poultry. World's Poult. Sci. J.
57, 415–458.
Spagnuolo, A.M., Dirita, V., Kirschner, D., 2011. A model for Vibrio cholerae
colonization of the human intestine. J. Theor. Biol. 289, 247–258.
Sprent, J., 1973. Circulating T and B Lymphocytes of Mouse. 1. Migratory properties.
Cell. Immunol. 7, 10–39.
Sprent, J., Basten, A., 1973. Circulating T and B Lymphocytes of Mouse. 2. Lifespan.
Cell. Immunol. 7, 40–59.

<a id='0229308c-f8e7-4804-bea6-93effee6eac4'></a>

Uni, Z., Geyra, A., Ben-Hur, H., Sklan, D., 2000. Small intestinal development in the young chick: crypt formation and enterocyte proliferation and migration. Br. Poult. Sci. 41, 544-551.

Upperman, J.S., Camerini, V., Lugo, B., Yotov, I., Sullivan, J., Rubin, J., Clermont, G., Zamora, R., Ermentrout, G.B., Ford, H.R., Vodovotz, Y., 2007. Mathematical modeling in necrotizing enterocolitis—a new look at an ongoing problem. J. Pediatr. Surg. 42, 445-453.

Van Furth, R., Diesselhoff-den Dulk, M.C., Mattie, H., 1973. Quantitative study on the production and kinetics of mononuclear phagocytes during an acute inflammatory reaction. J. Exp. Med. 138, 1314-1330.

van Hemert, S., Hoekman, A.J., Smits, M.A., Rebel, J.M., 2006. Gene expression responses to a Salmonella infection in the chicken intestine differ between lines. Vet. Immunol. Immunopathol. 114, 247-258.

van Hemert, S., Hoekman, A.J., Smits, M.A., Rebel, J.M., 2007. Immunological and gene expression responses to a Salmonella infection in the chicken intestine. Vet. Res. 38, 51-63.

van Zijderveld, F.G., van Zijderveld-van Bemmel, A.M., Anakotta, J., 1992. Comparison of four different enzyme-linked immunosorbent assays for serological diagnosis of Salmonella enteritidis infections in experimentally infected chickens. J. Clin. Microbiol. 30, 2560-2566.

Vaughan, A.T., Roghanian, A., Cragg, M.S., 2011. B cells—masters of the immunoverse. Int. J. Biochem. Cell. Biol. 43, 280-285.

Wigginton, J.E., Kirschner, D., 2001. A model to predict cell-mediated immune regulatory mechanisms during human infection with Mycobacterium tuberculosis. J. Immunol. 166, 1951-1967.

Withanage, G.S., Kaiser, P., Wigley, P., Powers, C., Mastroeni, P., Brooks, H., Barrow, P., Smith, A., Maskell, D., McConnell, I., 2004. Rapid expression of chemokines and proinflammatory cytokines in newly hatched chickens infected with Salmonella enterica serovar typhimurium. Infect. Immun. 72, 2152-2159.

Withanage, G.S., Wigley, P., Kaiser, P., Mastroeni, P., Brooks, H., Powers, C., Beal, R., Barrow, P., Maskell, D., McConnell, I., 2005. Cytokine and chemokine responses associated with clearance of a primary Salmonella enterica serovar Typhimurium infection in the chicken and in protective immunity to rechallenge. Infect. Immun. 73, 5173-5182.

Zeitz, M., Schieferdecker, H.L., James, S.P., Riecken, E.O., 1990. Special functional features of T-lymphocyte subpopulations in the effector compartment of the intestinal mucosa and their relation to mucosal transformation. Digestion 46 (Suppl 2), 280-289.

Zhou, H., Lamont, S.J., 2007. Global gene expression profile after Salmonella enterica Serovar enteritidis challenge in two F8 advanced intercross chicken lines. Cytogenet. Genome Res. 117, 131-138.