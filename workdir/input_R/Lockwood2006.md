<a id='53e92aca-45d1-4570-a125-b741ec87edf0'></a>

Pharmaceutical Research, Vol. 23, No. 9, September 2006 (© 2006) DOI: 10.1007/s11095-006-9048-8

<a id='fae9f59f-86d7-4a98-b6da-b612e6ea1c80'></a>

*Research Paper*

<a id='772b4335-c717-41dd-833d-8423859c0474'></a>

Application of Clinical Trial Simulation to Compare Proof-of-Concept
Study Designs for Drugs with a Slow Onset of Effect; An Example
in Alzheimer's Disease

<a id='102b026d-926f-42e1-b9f2-179fddf18099'></a>

Peter Lockwood,¹⁴ Wayne Ewy,¹ David Hermann,² and Nick Holford³

<a id='e904df33-3426-4163-9a88-bc604fb8b7ef'></a>

Received February 1, 2006; accepted May 2, 2006; published online August 12, 2006

**Objective.** Clinical trial simulation (CTS) was used to select a robust design to test the hypothesis that a new treatment was effective for Alzheimer's disease (AD). Typically, a parallel group, placebo controlled, 12-week trial in 200–400 AD patients would be used to establish drug effect relative to placebo (i.e., Ho: Drug Effect = 0). We evaluated if a crossover design would allow smaller and shorter duration trials.

**Materials and Methods.** A family of plausible drug and disease models describing the time course of the AD assessment scale (ADAS-Cog) was developed based on Phase I data and literature reports of other treatments for AD. The models included pharmacokinetic, pharmacodynamic, disease progression, and placebo components. Eight alternative trial designs were explored via simulation. One hundred replicates of each combination of drug and disease model and trial design were simulated. A 'positive trial' reflecting drug activity was declared considering both a dose trend test (_p_ < 0.05) and pair-wise comparisons to placebo (_p_ < 0.025).

**Results.** A 4 × 4 Latin Square design was predicted to have at least 80% power to detect activity across a range of drug and disease models. The trial design was subsequently implemented and the trial was completed. Based on the results of the actual trial, a conclusive decision about further development was taken. The crossover design provided enhanced power over a parallel group design due to the lower residual variability.

**Conclusion.** CTS aided the decision to use a more efficient proof of concept trial design, leading to savings of up to US$4M in direct costs and a firm decision 8–12 months earlier than a 12-week parallel group trial.

**KEY WORDS:** Alzheimer's disease; clinical trial simulation; pharmacokinetic pharmacodynamic model; trial design.

<a id='c1da3209-320e-47e2-ade1-8cb39022dcc1'></a>

# INTRODUCTION

Clinical trial simulation (CTS) may be used to assess how different design and drug factors may affect trial performance. These factors may be controllable trial design properties, e.g., the doses studied, the duration of treatment, or uncontrollable drug characteristics, such as its pharmaco- kinetic or pharmacodynamic models and parameters. Other influencing factors may include the progression of disease over time or subject specific characteristics that may be re- lated to disease progression or treatment response. Provided there are specific decision rules for determining that a particular trial was positive, or for judging an estimate to be sufficiently accurate, CTS can provide a rational basis for

<a id='e27336fb-552b-420b-b448-fa3ccea7ec96'></a>

1 Pfizer Global Research and Development, Ann Arbor, Michigan,
USA.
2 deCODE genetics, Brighton, Michigan, USA.
3 Department of Pharmacology and Clinical Pharmacology, School of
Medicine, University of Auckland, Auckland, New Zealand.
4 To whom correspondence should be addressed. (e-mail: peter.
lockwood@pfizer.com)

<a id='0eb0be46-a915-4aa9-a1b1-a980651515fc'></a>

making decisions about the trial design and quantitating how effectively the design can answer the study objectives (1,2).
Clinical trial simulation can be viewed as an extension of conventional statistical design evaluation. Data derived models are utilized, based on the relationship between dose, exposure, the time course of disease progression, placebo effect, and the outcome measure, providing an alternative approach to that described in the statistics literature (3).

<a id='df5b34c1-9e92-48eb-919c-ff82bee2286d'></a>

A CTS study is presented which guided the design of a proof of concept (POC) trial for an M1 muscarinic agonist (CI-1017) being developed for the symptomatic treatment of Alzheimer's disease (AD) (4). M1 receptors are abundant in the hippocampus and cortex playing an important role in learning and memory and are an attractive target for cognitive enhancement in AD (5,6). Direct acting muscarinic agonists may also be effective in modulating tissue levels of the amyloid ̓ peptide, which in its aggregated form is highly toxic to neurons and is a major constituent of senile plaques characteristic of the neuropathological diagnosis of AD (7).

<a id='7ff6c8ba-55ae-4f2c-9d25-f5dc73704030'></a>

Because the mechanism of action of CI-1017 was
untested clinically, the principle objective of the clinical
study was to ascertain whether CI-1017 improved cognitive

<a id='ba0f582a-52ec-4932-9ba9-e01e8e22dfa6'></a>

0724-8741/06/0900-2050/0 © 2006 Springer Science + Business Media, Inc.

<a id='618a416d-9557-4b37-b907-a137d95265ab'></a>

2050

<!-- PAGE BREAK -->

<a id='0f0ddd1b-1024-4f77-b174-c889006b40b5'></a>

Clinical Trial Simulation to Compare Proof-of-Concept Trial Designs

<a id='1fab367b-052d-4bdf-a8de-4c32dc8e67e3'></a>

2051

<a id='72a1441b-0de5-49b5-8299-11cf79b45353'></a>

performance at least as fast and as well as tacrine—a
commercially available product for this indication. This
would be considered proof-of-concept (POC). At this stage
of development, while it was not essential to obtain accurate
estimates of the magnitude of drug effect, it was necessary to
obtain information that would enable an early decision about
whether to continue investing resources in the development
of the compound. This distinction in key objectives and
awareness that the POC study design was for internal
decision making, prompted considerations of study designs
that otherwise might not be considered suitable were it a
pivotal registration study.

<a id='05e74df2-a6fc-4f1f-88cd-fd0157a89afd'></a>

Preclinical pharmacological studies in rats and mice which were deficient in performing spatial memory tasks (i.e., the ability to find a hidden platform in a water maze (8)) as a consequence of genetic modification or lesioning of the nucleus basalis, responded to treatment with CI-1017 but demonstrated a U-shaped dose-response (DR) relationship. As doses were increased, the latency time to find a hidden platform decreased, but at higher doses the latency time increased. A similar outcome was observed in another study that investigated reversal of scopolamine-induced impair- ment of vigilance in rhesus monkeys, as measured by a continuous performance task. This U-shaped phenomenon has also been described in a clinical setting by Soncrantt et al., who reported that the cholinergic agonist arecoline (an alkaloid of the betel nut with agonist activity at M1 and M2 receptors) improved the ability to remember verbally pre- sented words, in a small group of subjects with probable or possible Alzheimer's disease (9). When the results were averaged across patients a U-shaped DR curve was observed. Based on these preclinical and clinical data, it was considered plausible that CI-1017 might also have a U-shaped DR profile and therefore a secondary trial objective was to characterize the dose-response.

<a id='bc7fae2d-5c02-4a97-95bd-501a328a0e59'></a>

Typically, effectiveness trials in AD are based on a parallel group design with two to four treatment groups plus a placebo group powered to detect a three-point improvement in the Alzheimer's Disease Assessment Scale-Cognitive sub-scale (ADAS-Cog) score after a minimum of 12 weeks of treatment (10–12). The ADAS-Cog is an objective test that evaluates memory, attention, reasoning, language, orientation and praxis (maximum score, 70); a decrease in score indicates improvement (13). Assuming a three-point treatment effect size from placebo with a standard deviation of 5.7, a parallel group design requires approximately 80 subjects per dose group to have 90% power (based on a two sided test and 5% significance level). It has also been consistently demonstrated that cholinesterase inhibitors may take up to 12 weeks to fully reflect the response to a given (14,15) dose and therefore studies designed to demonstrate the effectiveness of a pharmacological agent are at least of this duration.

<a id='5165bc76-00d3-4209-8ef5-b334f4601b70'></a>

Non-human toxicology studies for CI-1017 permitted up to 12 weeks of treatment and a POC study of this duration was proposed for CI-1017. Human pharmacokinetic and safety data from the Phase 1 single and multiple dose studies indicated that 25 mg TID was the maximum dose with tolerable adverse events in healthy elderly patients. Other doses available for study were 2, 5, 10 and 15 mg.

<a id='13603cf1-a674-42a0-92f7-21da31869448'></a>

A population pharmacokinetic pharmacodynamic anal-
ysis of tacrine clinical studies estimated a 3-unit improvement

<a id='45c32816-641b-4cc1-b376-deafb28299ad'></a>

on the ADAS-Cog at 80 mg with the time to reach 50% of this drug effect (equilibration half-time) of about 2 weeks (14). This implied that the full drug effect (i.e., effect at pharmacodynamic equilibrium) would be apparent by 12 weeks of treatment. As it was not a requirement that the full drug effect be measured to demonstrate that the treatment was superior to placebo, designs that studied the change in ADAS-Cog after treating Alzheimer's patients for less than 12 weeks were considered. Subsequently, a clinical trial simulation study was undertaken to compare how well different designs of approximately equal cost, could meet the POC objectives for a range of drug candidates that differed in their pharmacodynamic properties.

<a id='402671f3-03ef-4b77-99d6-37c45c6822f4'></a>

### Simulation Study Objectives
The primary objectives of the simulation study were to compare the power of the different study designs to detect a treatment effect of a specified size and to compare design performance to differentiate a DR pattern that was monotonic, from one that was U-shaped. A secondary objective was to evaluate the bias in the drug effect size estimate relative to that assumed at pharmcodynamic equilibrium.

<a id='a299c240-93cc-4745-a18f-c4bed591e7be'></a>

As the true underlying effect for this novel treatment was not known, four theoretical DR curves were considered, each reflected by a unique dose-response model of the drug effect. The curves had either a monotonic (linear, hyperbolic, or sigmoidal) or U-shaped DR relationship and an effect size of 3-unit at the best dose in the range up to 25 mg. Alternatives were also considered for the time to reach the pharmacodynamic equilibrium state, being either "fast" (50% of the full drug effect by 3 days) or "slow" (similar to tacrine and with 50% of the full drug effect reached at 2 weeks). Based on the pharmacokinetic convention that five half-lives approximate a steady state, these drugs would reach the pharmacodynamic equilibrium state at about 2 and 10 weeks, respectively. A target sample size was set at 60 based on a preliminary power analysis for a Latin Square design and budget considerations.

<a id='d2b49b68-2fd3-4121-982b-6fef25930d70'></a>

## MATERIALS AND METHODS

### The Simulation Model

*Population Pharmacodynamic Model*

A population pharmacodynamic model, relating plasma concentrations to ADAS-Cog scores was used to simulate realistic patient responses (14,16). Drug effect was assumed to be symptomatic rather than disease modifying (17). The model and its parameters were based on 5,263 ADAS-Cog measurements obtained from 909 patients recruited in French and American tarcrine studies (14). The ADAS-Cog score at any time during the study (i.e., *S(t)*), was a function of a linear combination of sub-models (Eq. (1)) that included a baseline value (*S*₀), a linear time course for untreated disease progression (*α·t*), a placebo effect (*PD(C*ep*)*) and drug effect (*PD(C*eA*)*). The residual error (*ε*) was assumed to be normally distributed with variance *σ*².

*S(t) = S*₀* + α·t + PD(C*ep*)* + *PD(C*eA*)* + *ε* (1)

<!-- PAGE BREAK -->

<a id='7176188c-2371-4ac7-937f-ae3a55df5288'></a>

2052

<a id='296c9921-ef22-44f4-bb0d-93bed1ce182c'></a>

Lockwood et al.

<a id='631b4072-7a1b-4a30-aed5-34223e4c70d6'></a>

The delay in reaching a pharmacodynamic equilibrium state was characterized using the effect compartment model which assumes the drug effect is dependent on the effect site concentrations which differ from systemic concentrations prior to the attainment of pharmacokinetic equilibrium (18). Accumulation of drug at the effect site was dependent on the plasma concentration that was predicted by the CI-1017 pharmacokinetic model, and the effect compartment equilibration half-time (t1/2eq).

<a id='01e08116-6d71-4e56-be99-9418346a5ffa'></a>

Placebo Response Model ($PD(C_{ep})$)

Patients entering an Alzheimer's trial may demonstrate a placebo response. Therefore, a placebo component was included in the simulation model. Based on the placebo model described by Holford and Peace (16), a placebo response ($ADAS-Cog_p(t)$) was assumed, that would develop over the early days of treatment and subsequently fade to zero after about 6 weeks. Mathematically, the time course of placebo response can be described by Eq. (2) with parameters

<a id='1ad002a3-998e-4b7b-a206-12f2e4109086'></a>

effect (days); Kelp, the rate constant defining the onset rate of the placebo effect (days⁻¹), and βp, a scaling parameter defining the size of the placebo effect. The time in days after the initiation of treatment is represented by the independent variable t.

$ADAS - Cog_p(t) = \frac{\beta_p \cdot Keq_p}{(Keq_p - Kel_p)} \cdot (e^{-Kel_p \cdot t} - e^{-Keq_p \cdot t})$ (2)

<a id='c52bcf52-3623-4bef-83fc-d9fe30ba7855'></a>

The onset half-life of the placebo effect is related to
$Keq_P$ by Eq. (3).

<a id='91c45b77-270c-4ea5-ba73-8d16d9eaf3dc'></a>

t_1/2eqm = ln(2) / Keq_p (3)

<a id='935ab100-205b-4ccd-9720-eafb3d99ea2e'></a>

The offset half-life of the placebo effect is related to
$Kel_p$ in a similar fashion.

<a id='cbca58a3-03b1-4973-b23c-c3de1cda580a'></a>

<::Figure: Linear dose response model graph. The primary y-axis is 'change in ADAS-cog score' ranging from 0 to -4. The top x-axis is 'CI-1017 tid dose (mg)' ranging from 0 to 36. The bottom x-axis is 'CI-1017 average steady state plasma concentration (ng/mL)' ranging from 0 to 90. A downward sloping line is plotted across the graph. Annotations on the graph include: Effect size at 25mg = -3, Effect/dose slope = -0.12, Effect/conc slope = -0.047. Vertical and horizontal lines intersect at approximately 25mg on the top x-axis (and roughly 62.5 ng/mL on the bottom x-axis) and -3 on the y-axis, indicating the effect size.::>

<a id='1e3c4528-6231-4509-98cf-dc75889664ab'></a>

<::Graph showing a Hyperbolic (Emax) dose response model. The y-axis represents the "change in ADAS-cog score" ranging from 0 to -4. There are two x-axes: the top x-axis shows "CI-1017 tid dose (mg)" ranging from 0 to 36, and the bottom x-axis shows "CI-1017 average steady state plasma concentration (ng/mL)" ranging from 0 to 90. A curve is plotted, starting at (0, 0) and decreasing. Annotations on the graph include: ED50 ~ 8.5 mg, EC50 ~ 21 ng/mL, 1/2 maximal effect = -2, and Effect size at 25 mg tid = -3 = 75% Emax.::>

<a id='bf8da6d1-553b-4236-bce0-0da2052c4d0b'></a>

<::Sigmoidal (Smax) dose response model chart: The chart displays a sigmoidal dose-response curve.The top x-axis is labeled "CI-1017 tid dose (mg)" with tick marks and labels from 0 to 36, incrementing by 2.The left y-axis is labeled "change in ADAS-cog score" with tick marks and labels from 0 down to -4, incrementing by -1.The bottom x-axis is labeled "CI-1017 average steady state plasma concentration (ng/mL)" with tick marks and labels from 0 to 90, incrementing by 3.A sigmoidal curve descends from the top left (near 0,0) towards the bottom right (approaching -3).Vertical and horizontal grid lines are present.Annotations on the graph include:"ED50 ~ 8 mg""EC50 ~ 21 ng/mL""Hill coefficient = 4""Effect size at 25 mg = 100% Emax = -3"::>

<a id='1dd55105-7b30-481e-9e09-63dcadb783fa'></a>

<::U shaped dose response model chart:CI-1017 tid dose (mg) is plotted on the top x-axis, ranging from 0 to 36. The bottom x-axis represents CI-1017 average steady state plasma concentration (ng/mL), ranging from 0 to 90. The y-axis shows change in ADAS-cog score, ranging from 0 to -6.The chart displays three curves:1. Combined agonist-antagonist dose/response (solid line).2. Agonist (Emax) dose/response (dotted line).3. Antagonist (Imax) dose/response (dashed line).A horizontal line at y = -3 is labeled "Overall effect size at 10mg tid = -3".A vertical line at x = 10 mg (corresponding to approx 25 ng/mL) is shown.Another vertical line at x = 15 mg (corresponding to approx 37.5 ng/mL) is shown.Text labels on the chart include:"ED50 Emax ~ 7 mg" (near the dotted line at y=-5)."ED50 Imax ~ 15 mg" (near the dashed line at y=-5).::>

<a id='0093b0be-8dea-41ba-8ac0-fffdcbf369b1'></a>

Fig. 1. Drug effect models considered in simulations study. Parameters characterizing the model are displayed in the individual panels.

<a id='9c9a8595-bcfe-42cf-b3a2-6e22a8afc23d'></a>

Keqp, the rate constant defining the onset rate of the placebo
-ff-t (\\...-1\\. \\ \\ ... \\ ... \\ ... \\ .ff...

<!-- PAGE BREAK -->

<a id='a9e5c552-c510-4879-be87-3ef866828710'></a>

Clinical Trial Simulation to Compare Proof-of-Concept Trial Designs

<a id='9aeea464-fcd0-4912-834d-65f397614daf'></a>

2053

<a id='b95e56b2-84cd-43f9-a6fc-137917626ad9'></a>

Table I. Parametric Form of Models Describing Active or Inactive Drug Effect. Model Parameters are Described in Table II

<a id='3b5cb383-d730-486a-a794-60d0d047564c'></a>

<table id="3-1">
<tr><td id="3-2">Model Type</td><td id="3-3">Description</td><td id="3-4">Parametric Form</td></tr>
<tr><td id="3-5">Inactive Active</td><td id="3-6">No effect Linear Emax (hyperbolic) Smax (sigmoidal)</td><td id="3-7">PDinactive (CeA) = 0·CeA PDEmax (CeA) = βA·CeA PDEmax (CeA) = Emax · CeA / (ECCeA50 + CeA) PDSmax (CeA) = Emax · CeAⁿ / (ECCeA50ⁿ + CeAⁿ)</td></tr>
<tr><td id="3-8"></td><td id="3-9">U-shaped A, B</td><td id="3-a">PDUshape (CeA) = Emax U · (CeAUⁿ / (ECCeAU50ⁿ + CeAUⁿ) - ICeAUⁿ / (ICeAU50ⁿ + ICeAUⁿ))</td></tr>
</table>
A The U-shaped dose-response pattern was modeled as the difference of two Emax functions with the same Emax and Hill coefficient
(agonist–antagonist model).
B CeA, CI-1017 drug concentration at effect site for monotonic concentration response relationship.
CeaU, CI-1017 drug concentration at effect site mediating pure agonist effect.
ICeaU, CI-1017 drug concentration at effect site mediating antagonist (inhibitory) effect.

<a id='26e07643-665e-4ac8-bb02-07ec39e6ec7b'></a>

Drug Response Model ($PD(C_{eA}))$)

Five different drug response models were used. One model characterized the drug as inactive (no effect) while the other four described a linear, hyperbolic, sigmoidal or U-shape. Mean parameter values for the active concentration response relationships were calculated based on lowering the mean ADAS-Cog score by three points at the best dose in the testable range. This was at 25 mg for monotonic patterns and 10 mg for the U-shape pattern. Figures and parametric

<a id='c09e548b-387e-4cc6-b7d6-4f1e4dc3b3f9'></a>

forms of the drug effect models are displayed in Fig. 1 and Table I, respectively. The parameters characterizing drug potency for the linear and non-linear models (i.e., slope or ED 50 [the dose at which 50% of the maximum drug effect was achieved] were converted to an average steady state concentration in a 65-year old non-smoking population.

<a id='e5908cec-e142-439f-a68a-fd004cda6f3d'></a>

To reflect between-patient random variation, the base-
line ADAS-Cog score (S₀), rate of score change (α), onset
half-life of placebo effect (t₁/₂eqp), offset half-life of placebo
effect (t₁/₂elp), placebo effect magnitude (βp), and active drug

<a id='5235f142-3cb3-49c9-b428-f6453758fde3'></a>

Table II. Parameter Values Characterizing Disease Progression, Placebo Effect, and Drug Effect Components used in Simulation Model
<table id="3-b">
<tr><td id="3-c">Parameter</td><td id="3-d">Description</td><td id="3-e">Units</td><td id="3-f">Population Estimate</td><td id="3-g">Percentage CV</td></tr>
<tr><td id="3-h">S₀</td><td id="3-i">Baseline ADAS-Cog score</td><td id="3-j">ADAS-Cog units</td><td id="3-k">30</td><td id="3-l">30</td></tr>
<tr><td id="3-m">α</td><td id="3-n">Rate of change of ADAS-Cog score, due to disease progression</td><td id="3-o">U/day</td><td id="3-p">0.0164</td><td id="3-q">30</td></tr>
<tr><td id="3-r">t₁/₂eqp</td><td id="3-s">Placebo effect onset half-life mediator</td><td id="3-t">Days</td><td id="3-u">6</td><td id="3-v">30</td></tr>
<tr><td id="3-w">t₁/₂elp</td><td id="3-x">Placebo effect offset half-life</td><td id="3-y">Days</td><td id="3-z">7</td><td id="3-A">30</td></tr>
<tr><td id="3-B">βp</td><td id="3-C">Magnitude of placebo effect</td><td id="3-D">ADAS-Cog</td><td id="3-E">-3</td><td id="3-F">30</td></tr>
<tr><td id="3-G">t1/2eqa</td><td id="3-H">Equilibration half-life (slow)</td><td id="3-I">Days</td><td id="3-J">16</td><td id="3-K">30</td></tr>
<tr><td id="3-L"></td><td id="3-M">Equilibration half-life (fast)</td><td id="3-N"></td><td id="3-O">2.8</td><td id="3-P">30</td></tr>
<tr><td id="3-Q">βA</td><td id="3-R">Potency of active drug (linear model)</td><td id="3-S">ADAS-Cog*ml/ng</td><td id="3-T">-0.047</td><td id="3-U">30</td></tr>
<tr><td id="3-V">Emax</td><td id="3-W">Maximum drug effect (hyperbolic model)</td><td id="3-X">ADAS-Cog units</td><td id="3-Y">-4</td><td id="3-Z">NA</td></tr>
<tr><td id="3-10"></td><td id="3-11">Maximum drug effect, (sigmoidal model)</td><td id="3-12">ADAS-Cog units</td><td id="3-13">-3</td><td id="3-14">NA</td></tr>
<tr><td id="3-15"></td><td id="3-16">Maximum drug effect for U-shaped model</td><td id="3-17">ADAS-Cog units</td><td id="3-18">-6</td><td id="3-19">NA</td></tr>
<tr><td id="3-1a">ECeA50</td><td id="3-1b">effect compartment concentration producing 50% of Emax</td><td id="3-1c">ng/ml</td><td id="3-1d">21</td><td id="3-1e">30</td></tr>
<tr><td id="3-1f">ECeAU50</td><td id="3-1g">Effect compartment concentration producing 50% of Emax for agonist component of U-shape model</td><td id="3-1h">ng/ml</td><td id="3-1i">18</td><td id="3-1j">30</td></tr>
<tr><td id="3-1k">ICeAnU50</td><td id="3-1l">Effect compartment concentration producing 50% inhibition of Emax for inhibitory component (antagonist) of U shape model</td><td id="3-1m">ng/ml</td><td id="3-1n">38</td><td id="3-1o">30</td></tr>
<tr><td id="3-1p">N</td><td id="3-1q">Hill coefficient (sigmoidal model) Hill coefficient (U shape model)</td><td id="3-1r">Unitless Unitless</td><td id="3-1s">4 3</td><td id="3-1t">30 30</td></tr>
<tr><td id="3-1u">σ</td><td id="3-1v">Residual error standard deviation</td><td id="3-1w">ADAS-Cog units</td><td id="3-1x">4</td><td id="3-1y">NA</td></tr>
</table>

<a id='25d3a311-ebb2-4d4a-9b42-2c81d54e5913'></a>

NA = Not assigned.

<!-- PAGE BREAK -->

<a id='f5535e1e-514a-4840-a2be-4eb4b83a4090'></a>

2054

<a id='463e910d-8f1e-470b-849c-d6b3e1a7b26c'></a>

Lockwood et al.

<a id='b689270f-afe7-476a-b5d4-5e91cd3d3757'></a>

Table III. CI-1017 Population Pharmacokinetic Parameter Estimates
<table id="4-1">
<tr><td id="4-2">Parameter</td><td id="4-3">Units</td><td id="4-4">Value</td><td id="4-5">Population Predicted Variance</td><td id="4-6">FBOV</td></tr>
<tr><td id="4-7">Clearance</td><td id="4-8">l/h</td><td id="4-9">94.5</td><td id="4-a">32</td><td id="4-b">11</td></tr>
<tr><td id="4-c">Central volume</td><td id="4-d">1</td><td id="4-e">172</td><td id="4-f">45</td><td id="4-g">21</td></tr>
<tr><td id="4-h">Inter compartmental clearance</td><td id="4-i">l/h</td><td id="4-j">31.8</td><td id="4-k">75</td><td id="4-l">43</td></tr>
<tr><td id="4-m">Peripheral volume</td><td id="4-n">1</td><td id="4-o">222</td><td id="4-p">71</td><td id="4-q">41</td></tr>
<tr><td id="4-r">Absorption rate constant</td><td id="4-s">h⁻¹</td><td id="4-t">4.81</td><td id="4-u">103</td><td id="4-v">ND</td></tr>
<tr><td id="4-w">Lag time</td><td id="4-x">h</td><td id="4-y">0.322</td><td id="4-z">27</td><td id="4-A">ND</td></tr>
</table>
*FBOV = Fraction of population variance attributable to between
occasion variability.

<a id='21069036-4047-446d-baf7-df2ccb8b5a03'></a>

equilibration half-life (t1/2eqa), were simulated from univari- ate independent log-normal distributions. The coefficient of variation (CV) for these distributions is shown as percentage CV in Table II.

<a id='5d5c5ddc-13d9-43fa-8dce-e7264baf7dcf'></a>

Disease progression, placebo response, and drug effect parameter values are displayed in Table II. Population variability parameters were arbitrarily set to 30% based on discussions with consultants and values reported by Holford and Peace (14). The drug effect equilibration half-time and placebo response reported were associated with the different study populations and the parameter estimates selected for these components in this simulation study reflected an American population (14).

<a id='1e950af9-8ccf-4bdb-aae0-cbe851ce90d7'></a>

_Pharmacokinetic Model_

Single doses ranging from 0.25 to 150 mg and multiple
doses of 2, 10, 25, and 50 mg q6h were rapidly absorbed. The
time of maximal plasma concentrations (tmax) occurred
approximately 1 h after oral administration. With multiple-
dose administration of CI-1017, maximum plasma drug
concentrations (Cmax) and total exposures (AUC) increased
in greater proportion relative to the increase in dose over a
dose range of 2 to 50 mg. Multiple doses of 2, 10, and 25 mg
administered q6h were generally well-tolerated.

<a id='c33cb968-dc6a-4e87-84a7-9d5bbdf29cab'></a>

Population pharmacokinetic parameters and estimates
of their variability were derived from fitting the Phase 1 data
using NONMEM and are displayed in Table III (19). Plasma

<a id='2ee6ceac-06c5-40df-96d9-c6abfa1ed0d0'></a>

concentrations of CI-1017 were described by a two-compartment model with first order input and a lag-time. The relative bioavailability of each dose was estimated in comparison to the nominal standard dose of 25 mg. Clearance (CL/F) was dependent on age (years) and smoking status (Eq. 4).

<a id='3a7deac4-60dd-46b6-9088-d42f4b68e196'></a>

CL = 94.5 \cdot e^{-0.0135 \cdot (age-40)} \cdot smk (4)

<a id='4cd56489-e8f2-4863-86df-d18537a6865b'></a>

If the subject was a smoker, the variable smk was equal to 1.5, otherwise 1. The between-subject random effects for some pharmacokinetic parameters (clearance, central volume, inter-compartmental clearance, and peripheral volume) were correlated. The correlation was incorporated into the simulation model by using a multivariate normal distribution from the estimated variance–covariance matrix obtained from NONMEM. The estimated between occasion variability (BOV) in pharmacokinetics was also incorporated into the simulation model (20). At each 7-day occasion, random normal distributions with mean 0 and variance σ²<sub>BOV</sub> were used to generate new subject specific random effects values for BOV, which were then added to the subject's pharmacokinetic parameters.

<a id='5fbff4c7-e712-4335-b815-f7da24e54944'></a>

**Drop Out Model**
A 1% weekly dropout rate was assumed based on an informal review of past experience in these types of trials. This was implemented in the simulation model as a survival model where the expected percentage of patients remaining in the trial at time = t days, S_v(t), is described by Eq. (5).

S_v(t) = e^-0.00145 * t (5)

<a id='b20faf14-6ef7-4bb3-8439-9a866974a5ca'></a>

## Trial Designs

Eight trial designs were evaluated, including Latin Square, incomplete block, and parallel group, as well as two composite designs that included both crossover and parallel group arms. Each design had approximately equal sample size (60 total), as a surrogate for trial cost. No patient received non-placebo treatment for more than 12 weeks—the total trial length was 12 weeks for all designs except for number 8, which was 16 weeks. The key characteristics of these designs are shown in Table IV. Table V shows the

<a id='f2589b12-f149-4f61-acf2-cb7225eafdf1'></a>

Table IV. Trial Designs Evaluated in Simulation Study
<table id="4-B">
<tr><td id="4-C">Design Number</td><td id="4-D">Design Description</td><td id="4-E">Number of Sequences</td><td id="4-F">Subjects per Sequence</td><td id="4-G">Number of Treatments Periods</td><td id="4-H">Period Length (weeks)</td><td id="4-I">Measurements per Period</td></tr>
<tr><td id="4-J">1</td><td id="4-K">6 × 6 Latin Square</td><td id="4-L">6</td><td id="4-M">10</td><td id="4-N">6</td><td id="4-O">2</td><td id="4-P">1</td></tr>
<tr><td id="4-Q">2</td><td id="4-R">6 × 3 Incomplete block</td><td id="4-S">6</td><td id="4-T">10</td><td id="4-U">3</td><td id="4-V">4</td><td id="4-W">2</td></tr>
<tr><td id="4-X">3</td><td id="4-Y">Parallel group</td><td id="4-Z">6</td><td id="4-10">10</td><td id="4-11">1</td><td id="4-12">12</td><td id="4-13">6</td></tr>
<tr><td id="4-14">4</td><td id="4-15">6 x 4 Incomplete block</td><td id="4-16">6</td><td id="4-17">10</td><td id="4-18">4</td><td id="4-19">3</td><td id="4-1a">1</td></tr>
<tr><td id="4-1b">5</td><td id="4-1c">6 × 3 Incomplete block with two parallel groups</td><td id="4-1d"></td><td id="4-1e"></td><td id="4-1f">Seq 1-6: 3</td><td id="4-1g">Seq 1-6: 4</td><td id="4-1h">2</td></tr>
<tr><td id="4-1i"></td><td id="4-1j"></td><td id="4-1k">8</td><td id="4-1l">8</td><td id="4-1m">Seq 7-8: 1</td><td id="4-1n">Seq 7-8:12</td><td id="4-1o">6</td></tr>
<tr><td id="4-1p">6</td><td id="4-1q">4 × 4 Latin Square</td><td id="4-1r">4</td><td id="4-1s">15</td><td id="4-1t">4</td><td id="4-1u">3</td><td id="4-1v">1</td></tr>
<tr><td id="4-1w">7</td><td id="4-1x">4 x 4 Latin Square with two parallel groups</td><td id="4-1y"></td><td id="4-1z"></td><td id="4-1A">Seq 1-4: 4</td><td id="4-1B">3</td><td id="4-1C">1</td></tr>
<tr><td id="4-1D"></td><td id="4-1E"></td><td id="4-1F">6</td><td id="4-1G">10</td><td id="4-1H">Seq 5-6: 1</td><td id="4-1I">12</td><td id="4-1J">6</td></tr>
<tr><td id="4-1K">8</td><td id="4-1L">4 x 4 Latin Square</td><td id="4-1M">4</td><td id="4-1N">15</td><td id="4-1O">4</td><td id="4-1P">4</td><td id="4-1Q">2</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='d7658a44-b3d8-44bd-8446-128f9c9ac523'></a>

Clinical Trial Simulation to Compare Proof-of-Concept Trial Designs

<a id='30d05b2c-d32f-4a7c-9ddb-d5f1f05af68a'></a>

2055

<a id='8b1959dd-1b9f-4db7-affb-73d524c014e5'></a>

Table V. Dosing Sequences in Design Number 1
<table id="5-1">
<tr><td id="5-2" colspan="3">Design Number 1: 6 x 6 Latin Square;</td><td id="5-3" colspan="3">TID Dose (mg)</td><td id="5-4"></td></tr>
<tr><td id="5-5">Sequence number 1</td><td id="5-6">P</td><td id="5-7">25</td><td id="5-8">2</td><td id="5-9">15</td><td id="5-a">5</td><td id="5-b">10</td></tr>
<tr><td id="5-c">Sequence number 2</td><td id="5-d">2</td><td id="5-e">P</td><td id="5-f">5</td><td id="5-g">25</td><td id="5-h">10</td><td id="5-i">15</td></tr>
<tr><td id="5-j">Sequence number 3</td><td id="5-k">5</td><td id="5-l">2</td><td id="5-m">10</td><td id="5-n">P</td><td id="5-o">15</td><td id="5-p">25</td></tr>
<tr><td id="5-q">Sequence number 4</td><td id="5-r">10</td><td id="5-s">5</td><td id="5-t">15</td><td id="5-u">2</td><td id="5-v">25</td><td id="5-w">P</td></tr>
<tr><td id="5-x">Sequence number 5</td><td id="5-y">15</td><td id="5-z">10</td><td id="5-A">25</td><td id="5-B">5</td><td id="5-C">P</td><td id="5-D">2</td></tr>
<tr><td id="5-E">Sequence number 6</td><td id="5-F">25</td><td id="5-G">15</td><td id="5-H">P</td><td id="5-I">10</td><td id="5-J">2</td><td id="5-K">5</td></tr>
</table>

<a id='b1261112-1f5b-4a79-ab16-cdf83ba2ef30'></a>

dosing sequences for the six groups in design number 1, a six period, six-sequence group Latin Square that is balanced for pair-wise treatment sequence—a William's design (21).
Design number 6–8 were based on a similarly defined 4 × 4 Latin Square, using 2, 10, and 25 mg doses and placebo. The lower doses (2, 10 mg) were selected to approximate the ED10 and ED50 while the 25 mg dose was selected to achieve a 3-unit change in the ADAS-Cog for the assumed population average monotonic dose-response relationships. For the U-shaped dose-response relationship, 10 mg defined the population average peak effect, while the bordering doses of 2 and 25 mg doses mediated a small effect (less than 25% of Emax for the agonist–antagonist model).

<a id='0777447d-ebaa-45f3-aaf7-8b1bfa20bdd4'></a>

### Data Evaluation Methods

An analysis of variance (AOV) model appropriate to each design was used to analyze the simulated data. For each trial objective, a decision rule was defined to translate a trial's analysis results into an outcome from which the percentage correct was calculated (over the 100 replicate trials). The analysis methods employed for each of the trial objectives are detailed more explicitly as follows.

<a id='a5c9042e-c6e1-4be8-ba42-950fa398fb84'></a>

Primary Objective A: Does the drug work?
The AOV was used to test the null hypothesis of no drug effect on ADAS-Cog. Rejection of the null hypothesis constituted a "positive study" finding, which would be judged as "correct" for all data models except the no effect model, for which "not positive" was correct. The specific AOV model depended upon the design, but the decision rule for declaring a "positive study" was based on a 2 degrees of freedom (linear and quadratic) dose trend test at the two-tailed 5% significance level together with at least one dose declared statistically better than placebo (p < 0.025, one tail).

<a id='dc0a777f-260d-4749-a453-fd654c6e3bc0'></a>

Primary Objective B: Is the shape monotonic or U-shaped?
After exploring various parametric and non-parametric approaches, a simple but robust criterion was adopted for deciding whether a trial's data supported a monotonic or U-shaped pattern (within the tested dose range). A two-stage approach was used, initiated with a test for activity that was identical to the procedure used in primary objective A, except for using a higher type 1 error setting (0.1 one tail rather than 0.025 one tail). As this was not a pivotal registration study and was to be used for internal decision-making, relaxing of the critical value for rejecting the null hypothesis and increasing the Type I error to 0.1 for the shape classification algorithm was considered justified. For a non-positive trial (by this relaxed standard), the response

<a id='ea4e761a-c951-4dcb-b0e5-37da7da21b38'></a>

Table VI. Estimated Power for Detecting Activity (%), Averaged
over the Four Dose-response Patterns
<table id="5-L">
<tr><td id="5-M">Design Number</td><td id="5-N">1</td><td id="5-O">2</td><td id="5-P">3</td><td id="5-Q">4</td><td id="5-R">5</td><td id="5-S">6</td><td id="5-T">7</td><td id="5-U">8</td></tr>
<tr><td id="5-V">Fast</td><td id="5-W">95</td><td id="5-X">64</td><td id="5-Y">41</td><td id="5-Z">56</td><td id="5-10">64</td><td id="5-11">86</td><td id="5-12">80</td><td id="5-13">96</td></tr>
<tr><td id="5-14">Slow</td><td id="5-15">48</td><td id="5-16">40</td><td id="5-17">30</td><td id="5-18">31</td><td id="5-19">41</td><td id="5-1a">63</td><td id="5-1b">54</td><td id="5-1c">81</td></tr>
</table>

<a id='964a93d7-2ffe-467f-a876-603af7babb24'></a>

pattern was classified as 'flat' (i.e., essentially as 'no
information regarding shape'); otherwise an inference was
made between monotonic and U-shaped based on the pattern
of the estimated dose group means from the AOV. For the
four-dose group designs, monotonicity was declared if the
highest dose group had the best mean outcome; otherwise a
U-Shaped pattern was declared. For the six-group designs,
monotonicity was declared if either of the two highest dose
groups had the best mean.

<a id='c4b78ddd-e685-4315-8ca2-a99787b70bc4'></a>

_Secondary Objective: What is the Accuracy of the Pharmacodynamic Equilibrium Effect Estimate?_
An effect size estimate within one point (33%) of the true steady state effect size was considered "correct" for the purposes of the simulation study. The simulated estimate at the 25 mg dose was used for the monotonic DR patterns (regardless of the outcome for objective number 2), or the 10 mg dose when the true pattern was U-shaped.

<a id='130b20af-fee6-4ac0-811d-04aea3c45317'></a>

# Simulation Methods

One hundred trial replications were simulated using Pharsight Trial Simulator (22) for the different study designs listed in Table IV, for each of the dose-response patterns and for both the *slow* and *fast* drug types. The residual error, the effect size at the best dose, and the number of subjects were held constant, while the period length, number of doses, and number of measurements per period were varied. The data from each trial were analyzed to obtain and score the conclusions for each trial objective. The percentages of correct trials were tabulated for review, leading to the design recommendations described below.

<a id='d88f6f45-cc74-4251-8484-b5ef56b0435c'></a>

The Clinical Study

Based on the results of the simulations, the recommended design was carried out in an an Alzheimer's population. Both the 2- and 4-week measurements within each dose were

<a id='d4272110-070c-41de-8d4c-555aed29ba8e'></a>

Table **VII**. Percent of 100 Trials (power) that Detected a Drug
Effect for Slow Acting Drug for Design Number 6, 7 and 8
<table id="5-1d">
<tr><td id="5-1e">Design Number</td><td id="5-1f">8</td><td id="5-1g">7</td><td id="5-1h">6</td></tr>
<tr><td id="5-1i">Dose-response shape</td><td id="5-1j"></td><td id="5-1k"></td><td id="5-1l"></td></tr>
<tr><td id="5-1m">Linear</td><td id="5-1n">84</td><td id="5-1o">41</td><td id="5-1p">51</td></tr>
<tr><td id="5-1q">Emax</td><td id="5-1r">88</td><td id="5-1s">58</td><td id="5-1t">67</td></tr>
<tr><td id="5-1u">Smax</td><td id="5-1v">96</td><td id="5-1w">75</td><td id="5-1x">85</td></tr>
<tr><td id="5-1y">U-shape</td><td id="5-1z">57</td><td id="5-1A">40</td><td id="5-1B">49</td></tr>
<tr><td id="5-1C">Average</td><td id="5-1D">81</td><td id="5-1E">54</td><td id="5-1F">63</td></tr>
</table>
Design number 6: 4 × 4 Latin Square, 3 weeks per treatment.
Design number 7: 4 × 4 Latin Square with two parallel groups.
Design number 8, 4 × 4 Latin Square, 4 weeks per treatment.

<!-- PAGE BREAK -->

<a id='1509d25d-82ac-4fc1-9970-b5da12431d38'></a>

2056

<a id='5c0a7878-12cc-461a-b8fc-d41210bb33fe'></a>

Lockwood et al.

<a id='05788208-7eef-4af2-acdb-4f6b5745404c'></a>

Table VIII. Percent of 100 Trials (power) that Correctly Identified
Dose-response Shape for Slow Acting Drug for Design Number 6, 7
<table id="6-1">
<tr><td id="6-2"></td><td id="6-3">and 8</td><td id="6-4"></td><td id="6-5"></td></tr>
<tr><td id="6-6">Design Number</td><td id="6-7">8</td><td id="6-8">7</td><td id="6-9">6</td></tr>
<tr><td id="6-a">Dose-response shape</td><td id="6-b"></td><td id="6-c"></td><td id="6-d"></td></tr>
<tr><td id="6-e">Linear</td><td id="6-f">96</td><td id="6-g">69</td><td id="6-h">72</td></tr>
<tr><td id="6-i">Emax</td><td id="6-j">84</td><td id="6-k">62</td><td id="6-l">74</td></tr>
<tr><td id="6-m">Smax</td><td id="6-n">96</td><td id="6-o">83</td><td id="6-p">89</td></tr>
<tr><td id="6-q">U-shape</td><td id="6-r">45</td><td id="6-s">34</td><td id="6-t">39</td></tr>
<tr><td id="6-u">Average</td><td id="6-v">80</td><td id="6-w">62</td><td id="6-x">69</td></tr>
</table>

<a id='aaca132b-954c-4ee1-9eaa-dbbcae4e603e'></a>

used in the analysis of the ADAS-Cog subscale. The changes from baseline in total score on the ADAS-Cog were analyzed using a mixed-model analysis of variance that was similar to the method used in the simulation. The model contained fixed effect terms for treatment sequence, period, carryover effect, baseline value, and dose. Random effects were included to model the correlation between measurements within a patient, and to model the correlation between the 2-and 4-week measurements within each dose. A two-degree of freedom linear-quadratic trend test was performed to investigate dose-response (5%, two-tail). The study was to be considered positive if both the trend test (5%, two-tail) and the improvement of ADAS-Cog relative to placebo, at one or more active doses (2.5%, one-tail) were significant.

<a id='85e3c7c8-47d2-4715-bfd6-c4d915c1957f'></a>

## RESULTS

### Simulation Study Results

For detecting drug activity, all designs correctly declared the no effect drug candidate as "not positive" with an error rate of about 2.5% (observed rates based on 100 simulated trials ranging from 1% to 4%). For each design, the percentage of positive trials averaged over the four dose-response patterns is displayed in Table VI, for the slow and fast acting drug types.

<a id='2b8a6a42-2ba0-4a1e-8c63-0e5e328525ff'></a>

For each drug type, the best designs were 1, 6, 7, and 8, with design number 8 (4 × 4 Latin Square, 4-week treatment periods) being the best for both drug types. The parallel group design (number 3) was the poorest performer for both drug types. Only design 8 reached the 80% power level on average over the four dose-response patterns with the sample sizes used. Across designs, the estimated power was always higher for the fast acting drug. Therefore in order to simplify

<a id='af270986-d44e-47cd-9b43-7d327e288b66'></a>

Table IX. Percent of 100 Trials (Power) that Estimated the Effect
Size for the Slow Acting Drug at 25 mg (monotonic) or 10 mg
(U-shape) to be within +/- 33% of the True Effect
<table id="6-y">
<tr><td id="6-z">Design Number</td><td id="6-A">8</td><td id="6-B">7</td><td id="6-C">6</td></tr>
<tr><td id="6-D">Dose-response shape</td><td id="6-E"></td><td id="6-F"></td><td id="6-G"></td></tr>
<tr><td id="6-H">Linear</td><td id="6-I">42</td><td id="6-J">41</td><td id="6-K">42</td></tr>
<tr><td id="6-L">Emax</td><td id="6-M">47</td><td id="6-N">51</td><td id="6-O">55</td></tr>
<tr><td id="6-P">Smax</td><td id="6-Q">75</td><td id="6-R">68</td><td id="6-S">65</td></tr>
<tr><td id="6-T">U-shape</td><td id="6-U">14</td><td id="6-V">28</td><td id="6-W">34</td></tr>
<tr><td id="6-X">Average</td><td id="6-Y">45</td><td id="6-Z">47</td><td id="6-10">49</td></tr>
</table>

<a id='8420ed5a-03fd-43a7-8d6d-ccc6629614ea'></a>

Table X. Analysis of ADAS Cognitive Results (Intent-to-Treat)
from a 16-week, Randomized, Double-blind, Placebo-Controlled,
Crossover, Multi-Center Study of CI-1017 in Patients with Mild to
Moderate Alzheimer's Disease
<table id="6-11">
<tr><td id="6-12">TID Dose (mg)</td><td id="6-13">Difference from Placebo (95% CI)</td></tr>
<tr><td id="6-14">2</td><td id="6-15">-0.46 (-1.14-0.23)</td></tr>
<tr><td id="6-16">10</td><td id="6-17">-0.06 (-0.75-0.62)</td></tr>
<tr><td id="6-18">25</td><td id="6-19">-0.68 (-1.37-0.01)</td></tr>
</table>

<a id='2da1c918-a8fc-4ed5-b5f4-4906d5544ffa'></a>

the description of further results the design performance for
the slow acting drug only is reported, as this will characterize
trial performance for the least optimistic scenario. Table VII
partitions the average power to detect a drug effect into the
results for each of the active drug profiles. Table VIII
displays the estimated power to correctly identify the dose-
response shape. For all shapes, design 8 performed as well or
better than designs 6 and 7.

<a id='d31e158c-b545-4f52-bd67-fbcb5ebfe747'></a>

Table IX displays the power to correctly estimate the true effect size (to within +/- 33% of the true effect). As expected the overall level of performance is low. Averaged over the four DR models, designs 6, 7 and 8 are similar. For all the objectives, the power of any design was always lower for the U-shaped drug type compared to the drug type with monotonic dose-response characteristics.

<a id='d40adebf-e583-491c-bc84-fc071422f2cc'></a>

Based on these results, design 8 was selected for the actual clinical trial. Seventy patients were randomized to one of four assigned treatment sequences. Each treatment sequence consisted of three dose levels of CI-1017 (2, 10, and 25 mg) taken three times a day (TID) and matching placebo with each dose level administered sequentially. The sequence of administration was randomly assigned. All patients were intended to receive 4-week treatment with each of the dose levels of CI-1017 and placebo.

<a id='8f36873f-933b-472f-a69d-ea9b66b376cd'></a>

**Clinical Study Results**

The results of the clinical study are displayed in Table X. The study was not considered positive since the linear-quadratic trend test of ADAS-Cog scale was not significant and none of the three doses of CI-1017 were significantly better than placebo. The root mean square error (RMSE) derived from the mixed-model analysis of variance was 2.47 ADAS-Cog units.

<a id='f13ff8a8-65a6-4f4d-8fe7-e4118a2ee6f7'></a>

## DISCUSSION

It is often thought that the most convincing studies that demonstrate the benefit of therapy are parallel group designs with long treatment phases, in part because the drug effect at the time an equilibrium state has been reached is considered to be the critical endpoint. Crossover designs on the other hand are considered to harbor methodological problems and confound estimates of the treatment effect under various conditions, particularly when carry-over is present (3). This paper describes a clinical trial simulation study that provided a quantitative comparison of the potential performance of different study designs in Alzheimer's disease for fast and slow acting drug types and ultimately supported the implementation of a cross-over design for a POC study. While this example is

<!-- PAGE BREAK -->

<a id='2aa7f2d8-653a-42d4-8e7f-f1b35c4aadb7'></a>

Clinical Trial Simulation to Compare Proof-of-Concept Trial Designs

<a id='8187e0dc-e205-41ef-8829-dcd92570b908'></a>

2057

<a id='66c71495-d905-4249-bc65-3b26949d58b0'></a>

limited to a POC trial in Alzheimer's disease, the concepts
discussed are not limited to that therapeutic area and would be
applicable to many Phase 2 and 3 clinical trial settings.

<a id='fe35c408-4208-401b-9921-f125062ef0b3'></a>

The simulation model was characterized by parametric descriptions of the drug pharmacokinetics and pharmacodynamics, the natural progression of the disease, and the placebo effect. Estimates of the residual error and within subject variability for the different parameters were also included in the model. The simulated data were analyzed using a polynomial-based approach for dose-trend testing. This analysis method satisfied a basic requirement that the test be appropriate in the presence of non-monotonicity of response with dose, a requirement that excluded any trend test for which the validity depends upon monotonicity. Pragmatic considerations and time constraints were also factors in the choice of the analysis method for the simulations. It was recognized that the analysis method could have some effect on the relative estimates of design performance, however it was decided not compare the performance of different dose trend tests. This would have added another dimension to what was already a complex project, potentially compromising the timely delivery of the simulation results to the development team. Holford reports between-subject variability of 208% for disease progression and approximately 100% for placebo and drug potency parameters (14) and did not estimate random effects for any other parameters. In this simulation study, parameters accounting for the between-subject variability were assigned to all fixed effect parameters with the exception of Emax and this partitioning was considered to result in an overall between-subject variability that approximated that reported by Holford. However, as the primary consideration was to understand the performance of a trial design using this set of assumptions, the impact of the size of the random effects was not explored. The residual variability matched that described in the literature.

<a id='f72e6d2b-0d90-46f9-bdaa-ef627e898c27'></a>

Because the model and model parameters were based on data analyzed almost 15 years ago (14,16), the possibility of a change in the time course of the disease and placebo response between former and latter patient populations merits comment. In a study of 331 patients receiving a placebo treatment reported by Feldman et al. in 2005 (23), the mean 12-month decline in ADAS-Cog was 5.6 U/year (95% CI: 4.8–6.4). Stern et al. (1994), reported a decline of 4.9 points that falls within this confidence interval (24), while a number of placebo-controlled studies (25–29) have shown that the annual decline in cognition is 5–8 points with a 2-year decline of seven points reported by Sano et al. in 1997 (28). Nevertheless, even if disease progression rate was slower than that used in this simulation study, the impact would be minimal because the effect would be equal for all treatment groups and the duration of the study was short. With regard to the placebo response, it is difficult to make assertions as to whether this profile has changed over time because inves- tigators do not usually differentiate the placebo response from the underlying disease progression.

<a id='a87196d9-fd30-4893-8c3f-1d29d9fd3dd3'></a>

As the principle goal of this Phase 2a study was to
answer the key questions as to whether the drug had any
effect at all given the target sample size, as quickly as
possible, it was not considered necessary to measure the
steady state treatment effect. Additionally, even though the

<a id='58caa03d-14bf-43fc-85c8-dc3f73031b4d'></a>

trial was considered a tool for internal decision-making and would not satisfy the regulatory requirements for a confirmatory study, it was believed that a positive outcome would provide suitable supportive data for registration. The 4 x 4 crossover design was demonstrated to be the best design among those considered for detecting activity. For the fast acting design, which produces a larger effect size sooner than the slower one, the power for detecting the effect was higher regardless of design. Therefore the design evaluation focused on the performance assuming administration of the drug type that was slower acting. The lower power that was consistently observed for the drug type with U shape characteristics reflects the fact that the mean effect size at any of the dose options was less than 3, even though the population model defined a three-point effect at 10 mg. Due to the variability in ECeAU50 and ICeAnU50 parameters specified in the agonist-antagonist simulation model, an individual's "best dose" would not necessarily be at any of the doses included in the simulation study. Consequently this would lead to an average effect size of less that three points at any one of the doses studied. This simulation approach reflects inter-subject variability to drug potency, which was considered a realistic pharmacological concept. Other methods were not considered pharmacologically realistic e.g., an agonist antagonist model that excluded inter-subject variability and only described residual variability.

<a id='59d4e419-1b52-4bb3-8798-ea86a68d0737'></a>

While there were significant advantages to the implementation of the cross-over design in this instance, the design and analysis strategy (ANOVA) itself does have limitations, and these should be addressed when considering this type of study. For example, the design and analysis is unsuitable for evaluating beneficial or adverse treatment effects that are apparent only after 4 weeks of therapy because the observed effects would be assigned to the wrong treatment. Further, this design would be inefficient for evaluating effects that persist unchanged into subsequent periods; the effect estimates become increasingly biased as carry-over increases. Alternatively, a pharmacologically based model analysis would explicitly account for carryover in a mechanistic way.

<a id='73e9ed01-4b65-492c-9fd4-495f94103ab2'></a>

Further development of CI-1017 was terminated based on the results of the clinical study. The residual error standard deviation of 2.47 estimated from the actual POC study was 60% of the value observed in parallel group tacrine trials and 60% of the value used in the trial simulations (four ADAS-Cog units). This implied that the study was better powered to detect a signal than the power associated with a similar sized parallel group trial and the outcome appeared consistent with results for another drug in this class. Veroff et al., reported a mean treatment difference of -1.26 (p = 0.22), based on an intent-to-treat (ITT) analysis in patients administered 75 mg TID of xanomoline (an M1/M4 selective muscarinic agonist), for 24 weeks. Visual inspection of a figure depicting the change in mean ADAS-Cog score at 4, 8, 12 and 24 weeks that was based on the ITT population, suggests no difference between the placebo and drug treated groups at 4 weeks and that the maximal drug effect is exerted between 8 and 12 weeks (30).

<a id='5c155a75-4b24-43d8-8ac3-d7f32a3f0fc0'></a>

The implementation of the crossover design resulted in substantial time and cost savings relative to a traditional parallel group study. The minimum direct costs associated with a conventional 12 week, 300 patient Alzheimer's POC

<!-- PAGE BREAK -->

<a id='b79b9d02-3695-45e3-abe5-c2f95b3ee272'></a>

2058

<a id='011989b9-37c2-4755-8b76-8a014779bced'></a>

Lockwood et al.

<a id='4a7b29fb-a7e0-4ce9-b995-4818c1cf8558'></a>

study in 25–30 centers was estimated to be about US$4M (2001) and to extend over 24-month duration, from the time of enrollment of the first subject until the reporting of the results. In this example, because fewer patients and recruitment centers were required, the study was executed for one quarter of the cost (approximately US$1M) and the time from enrollment of the first patient to reporting of results was reduced to 7 months. These time-savings enabled resources to be reallocated to other development projects and the additional value of this "indirect saving" is considerable and should not be overlooked. The approach of initially determining whether the drug has any activity over a short time period, in place of estimating the drug effect after long-term treatment enables an earlier termination of a development program if a drug effect is not detected. Such an approach is consistent with the theme of developing new tools and practices to improve the critical path or product development process as described in the FDA's recent document that addresses how to get fundamentally better answers about the safety and effectiveness of new medical products (31).

<a id='2ae249df-947a-4740-a61c-2c52b6414bd7'></a>

The use of placebo controls in Alzheimer's disease has been the center of debate and is considered an unethical practice by some, especially if the treatment is long term. Use of the crossover design as described herein, may offer a solution to this dilemma in POC studies of acute symptom-atic treatments because patients are assigned a placebo treatment for much shorter periods (32,33). Another benefit of the shorter placebo period might be reduced drop out due to lack of effectiveness and enhanced recruitment as all patients will receive study drug during the trial.

<a id='e3340d04-b5a2-4b6f-9b7b-608f757457b1'></a>

This simulation study reflects a changing attitude in drug development. Firstly, the primary objective was to obtain sufficient evidence to determine if further development of the compound was justifiable by focusing on whether any activity could be detected after 4 weeks, as opposed to estimates of the drug effect after 12 weeks. Estimating the drug effect following 12 weeks of treatment was considered the goal of a of Phase IIB dose-response study. Secondly, a semi-mechanistic PKPD approach was used for simulating realistic patient level data as a function of drug exposure and time, and this enabled a quantitative comparison of the performance of different study designs under the different scenarios. This quantitative comparison eventually convinced skeptics to move forward with an atypical design. Because the study provides a "yes or no answer" to the fundamental question "does the drug work," it can be described as a confirming type study. Sheiner has previously discussed the distinction between learning and confirming studies (34). Had the study yielded a positive outcome, analysis of the data in a stand alone mode or coupled with prior information, may have then provided the answers to more quantitative questions such as "what is the expected steady state effect size at each dose"—a "learning" type study.

<a id='244abad4-be45-4963-a6b3-ee459fb1f34a'></a>

In summary, these clinical trial simulation results helped the development team better understand and compare the operating characteristics of eight plausible POC trial designs. In the end the chosen design proved to be more efficient than a traditional clinical development approach leading to considerable savings in time to decision and trial costs. The results of this CTS support the continued application of modeling and simulation to aid the design of clinical studies.

<a id='257e4160-00c5-4237-823d-0da7341090ae'></a>

# REFERENCES

1. P. L. Bonate. Clinical trial simulation in drug development. Pharm. Res. 17:3252-3256 (2000).
2. N. H. G. Holford, H. C. Kimko, J. P. R. Monteleone, and C. C. Peck. Simulation of clinical trials. Ann. Rev. Pharmacol. Toxicol. 40:209-234 (2000).
3. M. E. Putt and B. Ravina. Randomized, placebo controlled, parallel group versus crossover study designs for the study of dementia in Parkinson's disease. Control. Clin. Trials 23:111-126 (2002).
4. G. McKhann, D. Drachman, M. Folstein, R. Katzman, D. Price, and E. M. Stadlam et al., Clinical diagnosis of Alzheimer's disease: report of the NINCDS-ADRDA work group under the auspices of department of health and human services task force of Alzheimer's disease. Neurology 34:939-944 (1984).
5. A. I. Levey. Muscarinic acetylcholine receptor expression in memory circuits: implication for treatment of Alzheimer disease. Proc. Natl. Acad. Sci. USA. 93:13541-13546 (1996).
6. M. R. Emmerling, R. D. Schwarz, K. Spiegel, and M. J. Callahan. New perspectives on developing muscarinic agoists for Alzheimer's disease. Alzheimers Dis. 2:187-194 (1997).
7. D. J. Selkoe. Alzheimer's disease: a central role for amyloid. J. Neuropathol. Exp. Neurol. 43:438-447 (1994).
8. R. G. M. Morris. Development of a water maze procedure for studying spatial learning in the rat. J. Neurosci. Methods 11:47-60 (1984).
9. T. T. Soncrant, K. C. Raffaele, S. Asthana, A. Berardi, P. P. Morris, and J. V. Haxby. Memory improvement without toxicity during chronic low dose intravenous arecoline in Alzheimer's disease. Psychopharmacology 112:421-427 (1993).
10. N. Qizibash, A. Whitehead, J. Higgans, G. Wilcock, L. Schneider, and M. Farlow. Cholinesterase inhibition for Alzheimer disease. A meta-analysis of the tacrine trials. JAMA 280:1777-1782 (1998).
11. A. Whitehead, C. Perdomo, R. D. Pratt, J. Birks, G. K. Wilcock, and J. G. Evans. Donepezil for the symptomatic treatment of patients with mild to moderate Alzheimer's disease: a meta-analysis of individual patient data from randomized controlled trials. Int. J. Geriatr. Psychiatry 19:624-633 (2004).
12. N. Trinh, J. Hoblyn, S. Mohanty, and K. Yaffe. Efficacy of cholinesterase inhibitors in the treatment of neuropsychiatric symptoms and functional impairment in Alzheimer disease. A meta-analysis. JAMA 289:210-216 (2003).
13. W. G. Rosen, R. C. Mohs, and K. Davis. A new rating scale for Alzheimer's disease. Am. J. Psychiatry 141:1356-1364 (1984).
14. N. H. G. Holford and K. E. Peace. Results and validation of a population pharmacodynamic model for cognitive effects in Alzheimers patients treated with tacrine. Proc. Natl. Acad. Sci. 89:11471-11475 (1992).
15. A. Burns, M. Rossor, J. Hecker, S. Gauthier, H. Petit, H. J. Moller, S. L. Rogers, and L. T. Freidhoff and the International Donepezil Study Group The effects of Donepezil in Alzheimer's disease results from a multinational trial. Dement. Geriatr. Cogn. Disord. 10:237-244 (1999).
16. N. H. G. Holford and K. E. Peace. Methodologic aspects of a population pharmacodynamic model for cognitive effects in Alzheimers patients treated with tacrine. Proc. Natl. Acad. Sci. 89:11466-11470 (1992).
17. P. L. Chan and N. H. G. Holford. Drug treatment effects on disease progress. Ann. Rev. Pharmacol. Toxicol. 41:625-659 (2001).
18. N. H. G. Holford and L. B. Sheiner. Understanding the dose-effect relationship: clinical application of pharmacokinetic and pharmacodynamic models. Clin. Pharmacokinet. 6:429-453 (1981).
19. L. S. Beal and L. B. Sheiner. NONMEM Users Guides, part I-VIII, University of California, San Francisco, 1996.
20. M. O. Karlsson and L. B. Sheiner. The importance of modeling inter-occasion variability in population pharmacokinetic analyses. J. Pharmacokinet. Biopharm. 21:735-750 (1993).
21. B. Jones and M. G. Kenward. Design and Analysis of Cross-Over Trials, Chapman & Hall, London, 1994.
22. Pharsight Trial Simulator Version 2.1. 2000. Pharsight Corporation Mountain View California, USA.

<!-- PAGE BREAK -->

<a id='33c25790-706d-4d96-b130-6ad6336fec91'></a>

Clinical Trial Simulation to Compare Proof-of-Concept Trial Designs

<a id='d4b41e36-0340-4a84-b246-6dcdf1fd462a'></a>

2059

<a id='ddcdd052-c019-425b-a1ac-adf80c134acf'></a>

23. H. Feldman, B. Van Baelen, S. M. Kavanagh, and E. L. Koen. Torfs, MSc§ Cognition, function, and caregiving time patterns in patients with mild-to-moderate Alzheimer disease—a 12-month analysis. Alzheimer Dis. Assoc. Disord. 19:29-36 (2005).
24. R. G. Stern, R. C. Mohs, and M. Davidson. A longitudinal study of Alzheimer's disease: measurement, rate, and predictors of cognitive deterioration. Am. J. Psychiatry 151: 390-396 (1994).
25. P. S. Aisen, K. L Davis, J. D. Berg, K. Schafer, K. Campbell, R. G. Thomas, M. F. Weiner, M. R. Farlow, M. Sano, M. Grundman, and L. J. Thal. A randomized controlled trial of prednisone in Alzheimer's disease. Alzheimer's disease cooperative study. Neurology 54:588-593 (2000).
26. P. S. Aisen, K. A. Schafer, M. Grundman, E. Pfeiffer, M. Sano, K. L. Davis, M. R. Farlow, S. Jin, R. G. Thomas, and L. J. Thal. Effects of rofecoxib or naproxen vs placebo on Alzheimer disease progression: a randomized controlled trial. JAMA 289:2819-2826 (2003).
27. S. A. Reines, G. A. Block, J. C. Morris, G. Liu, M. L. Nessly, C. R. Lines, B. A. Norman, and C. C. Baranak. Rofecoxib: no effect on Alzheimer's disease in a 1-year, randomized, blinded, controlled study. Neurology 62:66-71 (2004).
28. M. Sano, C. Ernesto, R. G. Thomas, M. R. Klauber, K. Schafer, M. Grundman, P. Woodbury, J. Growdon, C. W. Cotman, E.

<a id='1b57f7a3-02f6-4518-85f2-c4a142f663ea'></a>

Pfeiffer, L. S. Schneider, and L. J. Thal. A controlled trial of selegiline, alpha-tocopherol, or both as treatment for Alzheimer's disease. The Alzheimer's disease cooperative study. N. Engl. J. Med. **336**:1216-1222 (1997).
29. L. J. Thal, M. Calvani, A. Amato, and A. Carta. A 1-year controlled trial of acetyl-1-carnitine in early-onset AD. Neurology **55**:805-810 (2000).
30. A. E. Veroff, N. C. Bodick, W. W. Offen, J. J. Sramek, and N. R. Cutler. Efficacy of xanomeline in Alzheimer's disease: cognitive improvement measured using the computerized neuropsychological test battery (CNTB). Alzheimer Dis. Assoc. Disord. **12**:304-312 (1998).
31. US Department of Health and Human Services, Food and Drug Administration. Challenge and opportunity on the critical path to new medical products (2004). http://www.fda.gov/oc/initiatives/criticalpath/whitepaper.html.
32. P. J. Whithouse, R. Arizaga, H. Brodaty, and S. Gauthier. Placebo in clinical trials in Alzheimer disease: an international discussion. Alzheimer Dis. Assoc. Disord. **13**:121-123 (1999).
33. D. Knopman, J. Kahn, and S. Miles. Clinical research designs for emerging treatments for Alzheimer's disease. Moving beyond placebo controlled trials. Arch. Neurol. **55**:1425-1429 (1998).
34. L. B. Sheiner. Learning versus confirming in clinical drug development. Clin. Pharmacol. Ther. **6**:275-291 (1997).