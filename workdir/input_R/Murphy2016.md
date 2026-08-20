<a id='f8cd0729-13d9-482f-ac80-a80a449d054d'></a>

Murphy et al. BMC Cancer (2016) 16:163 DOI 10.1186/s12885-016-2164-x

<a id='e8f40999-010d-4d14-9f88-4825be8f4869'></a>

<::logo: BMC Cancer
BMC
Cancer
The logo features the text "BMC Cancer" with a teal-colored arc above the letters "BMC"::>

<a id='fd0bb9ee-acfc-40ee-b42f-5675e5320235'></a>

RESEARCH ARTICLE                                                    Open Access

<a id='daebd186-39d2-47e6-8d37-9fb4c7d0bcfb'></a>

Differences in predictions of ODE models
of tumor growth: a cautionary example

<a id='37012715-3bd9-4616-b7ae-8c7d60731504'></a>

<::logo: CrossMark
CrossMark
A red bookmark-like symbol is centered within a blue and grey circular emblem, positioned to the left of the brand name "CrossMark".::>

<a id='38307ab7-5bff-4068-aeea-dd8fbfa9d3cf'></a>

Hope Murphy¹, Hana Jaafari² and Hana M. Dobrovolny²*

<a id='527d0f5c-ba4b-442e-9eaa-d3e30c79a771'></a>

**Abstract**

**Background:** While mathematical models are often used to predict progression of cancer and treatment outcomes, there is still uncertainty over how to best model tumor growth. Seven ordinary differential equation (ODE) models of tumor growth (exponential, Mendelsohn, logistic, linear, surface, Gompertz, and Bertalanffy) have been proposed, but there is no clear guidance on how to choose the most appropriate model for a particular cancer.

**Methods:** We examined all seven of the previously proposed ODE models in the presence and absence of chemotherapy. We derived equations for the maximum tumor size, doubling time, and the minimum amount of chemotherapy needed to suppress the tumor and used a sample data set to compare how these quantities differ based on choice of growth model.

**Results:** We find that there is a 12-fold difference in predicting doubling times and a 6-fold difference in the predicted amount of chemotherapy needed for suppression depending on which growth model was used.

**Conclusion:** Our results highlight the need for careful consideration of model assumptions when developing mathematical models for use in cancer treatment planning.

**Keywords:** Tumor growth, Mathematical model, Ordinary differential equation, Cancer, Chemotherapy

<a id='ea50a090-45a8-400b-88f6-5e1204f59374'></a>

## Background
Cancer is a leading cause of death and places a heavy burden on the health care system due to the chronic nature of the disease and the side effects caused by many of the treatments [1–3]. Much research effort is spent improving the efficacy of current treatments [4] and on developing new treatment modalitites [5–9]. As cancer treatment moves towards personalized treatment, mathematical models will be important component of this research, helping to predict the time course of the tumor and optimizing treatment regimens [10, 11].

<a id='c06c2c40-f54b-4b61-a206-78bfd38ac42c'></a>

Mathematical models are used in a number of ways
to help understand and treat cancer. Models are used to
understand how cancer develops [12] and grows [13-16].
They are used to optimize [17, 18] or even personalize [11,
19, 20] current treatment regimens; predict the efficacy
of new treatments [21] or combinations of different ther-
apies [22-24]; and give insight into the development of

<a id='918949f0-39f8-45a7-988c-10875547467c'></a>

*Correspondence: h.dobrovolny@tcu.edu
2Department of Physics & Astronomy, Texas Christian University, 2800 S.
University Drive, 76129, Fort Worth, TX, USA
Full list of author information is available at the end of the article

<a id='d50990ec-582a-4e86-a746-45df5e489848'></a>

resistance to treatment [25, 26]. While models have great potential to improve development and implementation of cancer treatment, they will only realize this potential if they provide accurate predictions.

<a id='32f90824-581f-4fc4-84f4-1f2ae6fd93af'></a>

The basis of any mathematical model used to study
treatment of cancer is a model of tumor growth. This
paper focuses on ordinary differential equation (ODE)
models of tumor growth. A number of ODE models have
been proposed to represent tumor growth [27, 28] and are
regularly used to make predictions about the efficacy of
cancer treatments [29]. Unfortunately, choice of a growth
model is often driven by ease of mathematical analysis
rather than whether it provides the best model for growth
of a tumor [27].

<a id='617f9ff4-7ce1-4d38-a018-8d4296ac53eb'></a>

Some researchers have attempted to find the "best" ODE growth model by fitting various models to a small number of experimental data sets of tumor growth [30–33]. Taken altogether, the results are rather inconclusive, with results suggesting that choice of growth model depends at least in part on the type of tumor [31, 32]. This leaves modelers with little guidance in choosing a tumor growth model.

<a id='b2dfe39a-4eb8-4417-8845-253b616db148'></a>

<::logo: BioMed Central
BioMed Central
The logo features a stylized incomplete circle in blue and green, followed by the company name in a sans-serif font, with "BioMed" in blue and "Central" in dark gray-green::>

<a id='b5a79a87-e7eb-4e6d-9be8-7fcd7fee6739'></a>

&copy; 2016 Murphy et al. **Open Access** This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.

<!-- PAGE BREAK -->

<a id='a617d55b-8acb-4bc2-8ec7-b7f939342d17'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='0be4ba3c-d659-41aa-8f16-36eebe1b636a'></a>

Page 2 of 10

<a id='102b7e19-4feb-411f-be38-8dd928ec70c1'></a>

Many researchers realize that improper choice of growth model is problematic [27] and can lead to differences in predictions of treatment outcomes [28, 29]. However, there has not yet been a study that compares and quantifies differences in predictions of the various models and how these differences affect predictions of treatment outcomes. This paper presents results of analysis of the various ODE growth models highlighting their predictions of tumor growth in the presence and absence of chemotherapy. We also fit the models to sample experimental tumor growth data sets and find a wide range of predicted outcomes based on the choice of growth model.

<a id='ba850e3a-d9e3-4f69-b907-c39798743bd1'></a>

Methods
Mathematical models
Early studies of tumor growth were concerned with
finding equations to describe the growth of cancer cells
[13-16] and many of the models examined here were pro-
posed at that time. The models predict the growth of a
tumor by describing the change in tumor volume, V, over
time. The model equations used in this analysis are pre-
sented in Table 1 and the models are described below.
a, b, and c are parameters that can be adjusted to describe
a particular data set.

<a id='89841fc8-08d5-4183-aa18-4c1db5256178'></a>

**Exponential:** In the early stages of tumor growth, cells divide regularly, creating two daughter cells each time. A natural description of the early stages of cancer growth is thus the exponential model [34], where growth is pro-portional to the population. The proportionality constant _a_ is the growth rate of the tumor. This model was often used in early analysis of tumor growth curves [13–16] and appears to work quite well at predicting early growth. It is known to fail, however, at later stages when angiogenesis and nutrient depletion begin to play a role [27, 32].

<a id='c4bbbea4-5238-48ec-b03a-d387543bc81f'></a>

**Mendelsohn**: A generalization of the exponential growth model was introduced by Mendelsohn [35]. In this model, growth is proportional to some power, *b*, of the population.

<a id='6d85f16f-aa3f-4bb8-83b9-fa638819bf33'></a>

Table 1 ODE models of tumor growth
<table><thead><tr><th>Model</th><th>Equation</th></tr></thead><tbody><tr><td>Exponential</td><td>V&#775; = aV</td></tr><tr><td>Mendelsohn</td><td>V&#775; = aV<sup>b</sup></td></tr><tr><td>Logistic</td><td>V&#775; = aV (1 - V/b)</td></tr><tr><td>Linear</td><td>V&#775; = aV / (V+b)</td></tr><tr><td>Surface</td><td>V&#775; = aV / (V+b)<sup>3</sup></td></tr><tr><td>Gompertz</td><td>V&#775; = aV ln (b / (V+c))</td></tr><tr><td>Bertalanffy</td><td>V&#775; = aV<sup>2&#8260;3</sup> - bV</td></tr></tbody></table>

<a id='9ef4c0b6-0d25-4979-b235-766ecc3f5255'></a>

**Logistic:** The logistic (or Pearl-Verhulst) equation was created by Pierre Francois Verhulst in 1838 [36]. This model describes the growth of a population that is limited by a carrying capacity of *b*. The logistic equation assumes that the growth rate decreases linearly with size until it equals zero at the carrying capacity.

<a id='78e59efc-f03f-4ee2-86df-11bf7472ff30'></a>

**Linear:** The linear model assumes initial exponential growth that changes to growth that is constant over time. In our formulation of the model, the initial exponential growth rate is given by a/b and the later constant growth is a. The model was used in early research to analyze growth of cancer cell colonies [16].

<a id='64f4230e-3565-4235-9ed0-a79d04a66841'></a>

**Surface:** The surface model assumes only a thin layer of cells at the surface of the tumor are dividing while the cells inside the solid tumors do not reproduce; they are mitotically inactive [37]. Our formulation again assumes exponential growth at early times with the surface growth taking over at longer times.

<a id='9ffbd12e-953e-49f1-9077-ba4c18ff6990'></a>

**Bertalanffy**: The Bertalanffy equation was created by Ludwig Bertalanffy as a model for organism growth [38]. This model assumes that growth occurs proportional to surface area, but that there is also a decrease of tumor volume due to cell death. This model was shown to provide the best description of human tumor growth [30].

<a id='6ddeaa45-9ca8-41e4-a7be-47c4e47f2a1e'></a>

**Gompertz:** Benjamin Gompertz originally created the Gompertz model in 1825 in order to explain human mortality curves [39]. The model is a generalization of the logistic model with a sigmoidal curve that is asymmetrical with the point of inflection. The curve was eventually applied to model growth in size of entire organisms [40] and more recently, was shown to provide the best fits for breast and lung cancer growth [32].

<a id='abd68822-2eac-4d3b-87cd-5f328628a5ad'></a>

## Dynamical analysis
Our goal is to assess differences in model predictions. While we are often concerned with prediction of time points in the near future, it is also informative to study the long-term predictions of a mathematical model. To this end, we find the fixed points of each equation which will tell us the long-term predictions of each of the models.
Stability analysis [41] is used to determine the boundary between growth and decay of the tumor.
We also determine the doubling time,

<a id='7b040b46-f9bf-41cb-a1ec-673021985003'></a>

DT = ln2
-----
  λ

(1)

where λ is the initial growth rate of the tumor. The doubling time is often used as a measure of how fast the tumor grows [42]. We use a Taylor expansion of the equations in Table 1 about V = 0 to determine the initial growth

<!-- PAGE BREAK -->

<a id='503cde0c-47a1-4342-8c49-71077fb917f8'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='a76c040b-b1f8-4478-9177-0a5674c4f2a8'></a>

Page 3 of 10

<a id='7581090d-ce98-4270-a873-59830137f757'></a>

rate. While this means that the calculated doubling time is an approximation and only valid during the early por-tion of the growth phase, many experimental data sets only follow the growth for a short period of time so this is representative of what might be calculated in actual experiments.

<a id='f8b3bc2a-e393-470d-9aab-90061be0b1cb'></a>

### Chemotherapy
In addition to assessing the predictions of the growth models alone, we examined how predictions differed when chemotherapy was added to the models. This is particularly important since growth models are often used as a basis for predicting the efficacy of cancer therapies.

<a id='7aebce8f-0b0e-403c-8683-335bf644a63f'></a>

Since this is just illustrative, we choose a simple implementation of chemotherapy. We assume that there is a constant supply of drug C0 acting on the tumor. We simply subtract the term C0V from each equation [29] and again use stability analysis to determine the conditions that lead to eradication of the tumor.

<a id='b74649b2-a23f-4065-8c35-2c5d48505d6c'></a>

**Data fitting**
Data from Worschech et al. [43] of a GI-101A xenograft in
nude mice (Figure 1A of [43], control data) was extracted
using WebPlotDigitizer, an online data extraction tool. Fit-
ting was performed by minimizing the sum of squared
residuals (SSR),

<a id='10863fe4-3358-4506-9e2f-d1774093dacf'></a>

SSR = \sum_i (x_i - m_i)^2,

(2)

<a id='7e49e9a2-be70-4c39-9d19-8115a1249df0'></a>

where $x_i$ are the experimental data points, and $m_i$ are the predicted model values at the same times. The lowest SSR was found using the Python Scipy fmin_tnc function, which uses a truncated Newton algorithm.

<a id='04611325-0ee6-4578-b51a-6c806ec77d8b'></a>

Since the models have a different number of free param-
eters, comparison using only the SSR is not always fair
since models with more free parameters have more free-
dom to to fit the data. To correct for this bias, we
use Aikaike's information criterion (AICc), corrected for
small sample size, which penalizes models with more
parameters if there is not enough improvement in the SSR.
The AICc is given by

<a id='2198457d-e3c9-4240-89e6-7e03e1443389'></a>

AIC_C = nln (SSR/n) + (2(K + 1)n) / (n - K - 2) ,

(3)

<a id='395b19cd-c63d-4e04-b9db-63e6d117f4b6'></a>

where _n_ is the number of data points and _K_ is the number of parameters [44]. The model with the lowest AIC_C is considered to be the better model given the experimental data it is approximating.

<a id='3013748e-0741-46cd-983b-afa1e176d402'></a>

## Results
### Tumor growth in the absence of chemotherapy
A simple analysis of the different models shows that they have very different predictions of the long-term dynamics

<a id='a40fe166-255a-4f4a-ac10-0e328bff1e2e'></a>

of tumor growth. The fixed points, doubling time and con-
dition for growth of the tumor are presented in Table 2.
All models have two fixed points, one of which is zero.
The remaining fixed point represents the maximum pos-
sible tumor size predicted by the model. In a real system,
the maximum possible tumor size, or carrying capacity,
is a function of the tumor's environment and its access
to resources [45] and can change as the tumor grows,
particularly in the case of extracapsular extension when
it extends beyond the bounds of its original organ. Four
of the models (exponential, Mendelsohn, linear, and sur-
face) predict that tumors will continue growing without
bound, a biologically unrealistic scenario. The remaining
three models (logistic, Gompertz, and Bertalanffy) predict
that tumors will grow to some maximum size and reach a
stable equilibrium at that point.

<a id='59e75a6f-a752-4535-98bf-b47c87f90f95'></a>

The growth criteria listed in Table 2 gives the condition for growth or decay of the tumor if a few cancer cells appear in the system. While the criteria all have slightly different forms, they essentially tell us that the initial growth rate once tumor cells appear must be positive. All the models agree that if the initial growth rate is positive, the tumor will continue to grow until it reaches its maximum size; the disease-free equilibrium is unstable. The doubling time for each model gives an indication of how quickly the tumor will reach this maximum size. Unfortunately, comparing the formulas does not really give much insight into differences in model predictions without having some estimate of the parameter values. In a later section, we give a quantitative assessment of differences in model predictions using sample tumor growth data.

<a id='edc044b8-08af-41a5-bb42-f07e2b88d7b5'></a>

**Tumor growth in the presence of chemotherapy**
As described in Methods, we assess how chemotherapy alters the dynamics of each of the growth models using the simplifying assumption of constant drug concentration. We again use stability analysis to assess the long-term

<a id='3ea93f1d-f38b-4c6b-ab2f-fca0a392a286'></a>

**Table 2** Model predictions in the absence of chemotherapy
<table id="2-1">
<tr><td id="2-2">Model</td><td id="2-3">Maximum size</td><td id="2-4">Doubling time</td><td id="2-5">Growth condition</td></tr>
<tr><td id="2-6">Exponential</td><td id="2-7">∞</td><td id="2-8">ln 2 / a</td><td id="2-9">a &gt; 0</td></tr>
<tr><td id="2-a">Mendelsohn</td><td id="2-b">∞</td><td id="2-c">ln 2 / a</td><td id="2-d">a &gt; 0</td></tr>
<tr><td id="2-e">Logistic</td><td id="2-f">b</td><td id="2-g">ln 2 / a</td><td id="2-h">a &gt; 0</td></tr>
<tr><td id="2-i">Linear</td><td id="2-j">∞</td><td id="2-k">b ln 2 / a</td><td id="2-l">a/b &gt; 0</td></tr>
<tr><td id="2-m">Surface</td><td id="2-n">∞</td><td id="2-o">b³ ln 2 / a</td><td id="2-p">a/b³ &gt; 0</td></tr>
<tr><td id="2-q">Gompertz</td><td id="2-r">b-c</td><td id="2-s">ln 2 / a ln(b/c)</td><td id="2-t">a ln(b/c) &gt; 0</td></tr>
<tr><td id="2-u">Bertalanffy</td><td id="2-v">(a/b)³</td><td id="2-w">ln 2 / a-b</td><td id="2-x">a-b &gt; 0</td></tr>
</table>

<!-- PAGE BREAK -->

<a id='d7f37391-f23b-4a97-993f-1dbf129358fc'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='572322f6-0c1c-417e-9159-fe08d0f68d8a'></a>

Page 4 of 10

<a id='661d52d7-73ae-4597-a02a-165176650987'></a>

predictions made by each of the models. Each of the
models again predicts that there are two possible fixed
points, one of which is zero. The other fixed point repre-
sents the maximum possible tumor size in the presence
of chemotherapy and is presented in Table 3. In this case,
only one model (exponential) predicts that the tumor
will continue to grow indefinitely even in the presence
of chemotherapy. The remaining models all predict that
the chemotherapy will hold the tumor to some maximum
size. Unfortunately, it is again difficult to assess the rela-
tive sizes of the predicted maximum size without having
values for parameters.

<a id='30032ee8-1c0f-4b5f-8d48-eea9ebd63f77'></a>

We can again determine the boundary condition that delineates growth of the tumor from decay of the tumor. In this case, this represents the minimum amount of chemotherapy needed to cause eradication of the tumor. Essentially, the minimum amount of chemotherapy needed is the amount that results in a kill rate equal to the initial growth rate of the tumor.

<a id='b6845a10-d0c5-44a7-a466-168bccfdd3ae'></a>

## Quantitative example
In the previous sections, we derived equations for maximum tumor size and conditions for growth of the tumor in the presence and absence of chemotherapy for each of the ODE growth models. However, it is difficult to assess just how large differences between model predictions are without having values for model parameters. In this section, we use sample tumor growth data extracted from the literature to quantitatively assess differences in model predictions.

<a id='f7e950c4-60e7-4a7e-ab6b-e2cb1bcfe40a'></a>

We use data from Worschech et al. [43] which consists
of measurements of growth of GI-101A cells injected sub-
cutaneously into nude mice. This is an unusually long data
set consisting of 14 time points spanning 114 days. In
addition to assessing differences in model predictions, we
will use this data set to examine whether model predic-
tions can be improved with the collection of more data.
We will initially use only the first half of the time series,

<a id='90f30602-307b-4f47-8c2a-87ef05a8ceef'></a>

Table 3 Model predictions in the presence of chemotherapy
<table id="3-1">
<tr><td id="3-2">Model</td><td id="3-3">Maximum size</td><td id="3-4">Minimum concentration needed to cure</td></tr>
<tr><td id="3-5">Exponential</td><td id="3-6">∞</td><td id="3-7">C_{0}=a</td></tr>
<tr><td id="3-8">Mendelsohn</td><td id="3-9">(\frac{C_{0}}{a})^{\frac{1}{b-1}}</td><td id="3-a">C_{0}=a</td></tr>
<tr><td id="3-b">Logistic</td><td id="3-c">\frac{b(a-C_{0})}{a}</td><td id="3-d">C_{0}=a</td></tr>
<tr><td id="3-e">Linear</td><td id="3-f">\frac{a}{C_{0}}-b</td><td id="3-g">C_{0}=\frac{a}{b}</td></tr>
<tr><td id="3-h">Surface</td><td id="3-i">a³/C₀ - b</td><td id="3-j">C₀ = a/b³</td></tr>
<tr><td id="3-k">Gompertz</td><td id="3-l">b/e^(C₀) - c</td><td id="3-m">C₀ = a ln(b/c)</td></tr>
<tr><td id="3-n">Bertalanffy</td><td id="3-o">(a / (b + C₀))³</td><td id="3-p">C₀ = a - b</td></tr>
</table>

<a id='b035a29a-395d-426b-82df-0cf3e171a866'></a>

seven points spanning 65 days. Note that many tumor
growth data sets contain fewer than ten points and often
span only a week or two [31], so this truncated data set is
quite representative of much of the data available in the
literature.

<a id='60d08fda-e8de-4be1-a008-8d6fb5feabce'></a>

Model fits to this truncated data, along with the best fit parameter estimates are presented in Fig. 1. All the models provide reasonable fits to the data, with the exponential model producing the worst SSR since it only has one free parameter. The model with the lowest SSR is the Bertalanffy model in this case. However, the AICc indicates that the exponential model actually provides the best explanation for the data since the improvement in SSR did not offset the inherent improvement in fit with the addition of the extra parameter. A close inspection of the fits shows that they largely agree on the growth trajectory while there are experimental data points to guide the time course, but they appear to diverge beyond the last experimentally collected time point. This is particularly problematic since mathematical models are often used for extrapolation, suggesting that proper choice of growth model is extremely important for correctly predicting the future growth of tumors as well as for assessing how treatment might affect growth of the tumor.

<a id='d0dafe94-9de1-44e5-a323-69c3cf66ba65'></a>

As a test of the accuracy of each model, we can use the best fit parameter estimates from the truncated data to predict the remaining seven time points of the full data set. As a measure of the accuracy of the predictions, we can calculate the SSR for each model prediction. The model predictions, along with the SSRs, are presented in Fig. 2. While the model that provided the best fit to the data was the Bertalanffy model and the model that provided the best explanation for the data was the exponential model, the model that actually provides the best estimate of the future growth of the tumor is the surface model. This is likely because the experimental data are measurements of a xenograft which grows as an approximately spherical tumor where only the cells near the surface are dividing. With the exception of the exponential model, the models underestimate the actual growth of the tumor. In the case of the Bertalanffy, Gompertz, and logistic models, this is because the truncated data set did not provide enough information to correctly estimate the maximum tumor size. Unfortunately, these three models are particularly popular choices for modeling tumor growth [27, 29] because they include a biologically realistic slowing of the growth rate as the tumor increases. Yet it is precisely this feature that results in the poor predictive value of the models.

<a id='9c48d980-381d-4281-992f-16641375830a'></a>

In practice, mathematical models are often not used to
predict full time series, but are used to calculate quanti-
ties of interest to clinicians. Using the formulas derived in
sections "Tumor growth in the absence of chemotherapy"
and "Tumor growth in the presence of chemotherapy", we

<!-- PAGE BREAK -->

<a id='f02d5c32-ade3-4234-872f-b06f2e6a7b44'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='161fffb4-cc4e-4255-bd17-1dbac3dfba13'></a>

Page 5 of 10

<a id='5e94b4a1-4250-4e35-91d4-819866efa041'></a>

<::chart: Plot showing tumor size (mm³) versus Time (d). The y-axis ranges from 0 to 1600. The x-axis ranges from 0 to 60. Eight different colored lines represent different tumor growth models: Exponential (black), Mendelsohn (blue), Logistic (yellow), Linear (cyan), Surface (red), Gompertz (magenta), and Bertalanffy (green). Black square markers represent 'Data' points, which are approximately at (5, 250), (10, 300), (20, 580), (35, 680), (45, 850), (55, 1050), and (65, 1200). The model lines generally follow the trend of the data points. Below the chart is a table titled 'Model fits to data. Best fits of the ODE tumor growth models to the first half of the data from Worschech et al. [43]. Parameter estimates are given in the table below the graph'. The table has columns: Model, a, b, c, SSR, AICc. The rows are: | Model | a | b | c | SSR | AICc | |---|---|---|---|---|---| | Exponential | 0.0262 /d | | | 54900 | 69.8 | | Mendelsohn | 0.286 /d | 0.616 | | 35100 | 73.6 | | Logistic | 0.0370 /d | 2000 mm³ | | 39800 | 74.5 | | Linear | 58.7 mm³/d | 1690 mm³ | | 41200 | 74.8 | | Surface | 0.265 mm/d | 506 mm³ | | 44000 | 75.2 | | Gompertz | 0.279 /d | 13900 mm³ | 12000 mm³ | 40100 | 88.6 | | Bertalanffy | 0.306 mm/d | 0.0119 /d | | 33700 | 73.3 |::>

<a id='7d1d0b63-a7c8-4e87-9aba-300af1f9468e'></a>

can use our parameter estimates to calculate maximum tumor size, doubling time, and minimum concentration of chemotherapy needed for suppression of the tumor. These quantities are presented in Fig. 4 (top row) for the truncated Worschech data. Four of the models (exponen- tial, Mendelsohn, linear, and surface) predict indefinite growth of the tumor. The remaining three models pre- dict finite tumor sizes, but the predicted maximum size varies by almost an order of magnitude, with the Gom- pertz and logistic models estimating a maximum tumor volume of ~ 2000mm3 while the Bertalanffy model esti- mates a maximum tumor volume of ~ 16000mm3. The doubling time estimated by the different models also shows a good deal of variation, ranging from ~ 2 d for the Mendelsohn and Bertalanffy models to ~ 26 d for the exponential model. The assumption of exponential

<a id='6d62df87-4d28-4b21-a26b-0253dd990a0d'></a>

growth underlies many calculations of the tumor growth rate or doubling time [42, 46] and the exponential model is also the model of choice for this data, so it is concerning that the exponential model provides one of the extreme estimates of doubling time. Of particular concern is the variation in predictions of the minimum amount of chemotherapy needed to suppress a tumor. The Bertalanffy and Mendelsohn models predictions are about six times larger than the predictions of the remaining models. If we use one of these models to decide on treatment plans, we could be treating patients with far more drug than is actually necessary. The extreme values predicted by the Bertalanffy model are especially concerning since the Bertalanffy model provided the lowest SSR and might be a choice for some modelers in predicting the future growth of this particular tumor.

<!-- PAGE BREAK -->

<a id='f8c749df-8e8b-4409-ae03-fe73327f2b12'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='da960203-04e0-4047-84e3-8f0c8db50a9f'></a>

Page 6 of 10

<a id='9204a3c0-f2bf-44e6-8668-c35ad957db8b'></a>

<::chart and table::>Fig. 2 ODE models' predicted time course of tumor growth. Each model was fit to the first seven time points and parameter estimates were used to extrapolate the remaining seven time points. The SSR for each prediction is given in the table below the graph. The chart displays Tumor volume (mm³) on the y-axis, ranging from 0 to 4000, and Time (d) on the x-axis, ranging from 0 to 120. Multiple curves represent different models: Data (black squares), Exponential (black line), Mendelsohn (blue line), Logistic (light brown line), Linear (cyan line), Surface (red line), Gompertz (magenta line), and Bertalanffy (green line). The Data points show an increasing trend, and the models are fitted to these points, with some extrapolating beyond the initial data. Below the chart, a table provides the SSR (Sum of Squared Residuals) for each model:
| | Exp. | Mend. | Log. | Lin. | Surf. | Gomp. | Bert. |
|---|---|---|---|---|---|---|---|
| SSR | 1.85×10^6 | 2.08×10^6 | 6.90×10^6 | 1.57×10^6 | 4.30×10^5 | 8.20×10^6 | 3.63×10^6 |
<::>


<a id='6a05d83c-e56b-4bab-a558-ef8590b228e6'></a>

Given that the short time series led to a large varia-tion in predicted outcomes, we examined whether the collection of extra time points might lead the models to more closely agree on predicted outcomes. We fit the full Worschech time series with each of the ODE growth models, as shown in Fig. 3. Many of the estimated param-eter values change somewhat from the estimates deter-mined by the fits to the first half of the time series. The most notable of these is the second parameter (b) of the Bertalanffy model which drops to essentially zero, sug-gesting that the best description of the data by this model neglects death within the core of the tumor. The model with the best fit in this case is the logistic model, which has both the lowest SSR and lowest AICC, so the addi-tion of extra information can alter the choice of growth model. Again, however, we see that the models all pro-vide reasonably good fits to the experimental data, but start to diverge beyond the last data point. It is unclear if this divergence will lead to large variations in clinical parameters.

<a id='c5569207-9eee-4b48-a76a-df69564f55ed'></a>

The maximum tumor size, doubling time and mini-
mum amount of chemotherapy needed for suppression
predicted by each model based on parameter estimates
from the full Worschech time series are shown in Fig. 4
(center row). As before, four of the models predict unfet-
tered growth of the tumor, but they are now joined by
the Bertalanffy model in predicting unrealistically large
tumors. Since there is now essentially no death of tumor
cells in the Bertalanffy model, the tumor continues to

<a id='40e7032b-c237-4a3c-a195-90db6ad6f857'></a>

grow indefinitely. The maximum tumor sizes predicted by the Gompertz and logistic models have increased slightly to ~ 5000 mm³ and ~ 7000 mm³, respectively. This is because the new data clearly shows that the tumor does not stop growing at 2000 mm³. The doubling times predicted by the Mendelsohn and Bertalanffy models are still quite a bit smaller than those predicted by the remaining models, although these estimates have increased. Finally, the predicted amount of chemotherapy needed to sup-press the tumor by the Mendelsohn model drops, coming noticeably closer to the values predicted by all but the Bertalanffy model.

<a id='8119ec77-0605-434f-ba39-c99661bae829'></a>

To quantify the changes we see with the addition of extra time points, we calculate the percent difference in each prediction between estimates based on the truncated time series and estimates based on the full time series (Fig. 4, bottom row). Of those models that predict a finite tumor size, we see that all have increased the predicted size of the tumor. The predicted doubling time has also increased for all of the models. This suggests that all of the models were underestimating the true doubling time of the tumor. Similarly, the percent differences suggest that the models all overestimated the amount of chemotherapy needed to suppress the tumor. The Mendelsohn and Bertalanffy models, which predicted particularly small doubling times and large amount of chemotherapy, show the largest percent changes in both estimates with the addition of extra time points. The surface model, which most accurately predicted the full time course based on estimates from

<!-- PAGE BREAK -->

<a id='f0fa8d15-17a6-4f4c-8d22-aa5b37b4a485'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='cfcd7cb9-7e33-4ca1-9f90-e90e381cd11a'></a>

Page 7 of 10

<a id='eb763c75-22e1-44f3-a1d8-6493b70085a6'></a>

<::Figure 3: A combined plot and table illustrating model fits to tumor growth data.

**Plot:**
- **Type:** Line chart with scatter plot data points.
- **X-axis:** Time (d), ranging from 0 to 100.
- **Y-axis:** Tumor size (mm³), ranging from 0 to 3500.
- **Legend:**
    - Exponential (black line)
    - Mendelsohn (blue line)
    - Logistic (cyan line)
    - Linear (yellow line)
    - Surface (red line)
    - Gompertz (magenta line)
    - Bertalanffy (green line)
    - Data (black squares)
- **Content:** Several growth curves representing different mathematical models are plotted, along with experimental data points (black squares) that these models are fitted to.

**Table:**
| Model | a | b | c | SSR | AIC_C |
| :---------- | :---------- | :---------- | :---------- | :---------- | :---------- |
| Exponential | 0.0246 /d | | | 4.31×10⁵ | 150 |
| Mendelsohn | 0.105 /d | 0.785 | | 1.82×10⁵ | 141 |
| Logistic | 0.0295 /d | 6920 mm³ | | 1.67×10⁵ | 139 |
| Linear | 132 mm³/d | 4300 mm³ | | 1.76×10⁵ | 140 |
| Surface | 0.291 mm/d | 708 mm³ | | 1.77×10⁵ | 140 |
| Gompertz | 0.0919 /d | 15500 mm³ | 10700 mm³ | 3.94×10⁵ | 155 |
| Bertalanffy | 0.234 mm/d | 3.46 × 10⁻¹⁹ /d | | 2.54×10⁵ | 145 |

Fig. 3 Model fits to data. Best fits of the ODE tumor growth models to the data from Worschech et al. [43]. Parameter estimates are given in the table below the graph
: chart and table::>

<a id='e00366a1-6c4a-409e-b909-e0dc100519bb'></a>

the first half, shows the smallest percent change with the addition of extra time points.

<a id='ee98f8fa-c24b-4f9e-b3fa-bc3fa777aedd'></a>

# Discussion
This paper examines several commonly used ODE models of tumor growth and quantitatively assesses the differences in their predictions of clinically relevant quantities. We first derived equations for the maximum tumor size, doubling time, and the condition for growth of all the models. We then derived equations for the maximum tumor size in the presence of chemotherapy and the minimum amount of chemotherapy needed to suppress a tumor. Finally, we used experimental tumor growth data along with these equations to compare predicted values of maximum tumor size, doubling time, and minimum amount of chemotherapy needed for suppression for each of the ODE models. We find that there is a six-fold difference in the minimum concentration of chemotherapy required for suppression of the tumor and a 12-fold

<a id='e643e758-a4c7-497a-95f4-b813df1f845a'></a>

difference in estimates of the doubling time. While the exact amount of variation in predictions between different models will differ for other data sets, we expect that there will be disagreement in model predictions for all data sets. In fact, this data set was particularly long, so the models were constrained to agree for a longer time period than with most other data sets. This, along with our finding that increasing the duration of the data set reduced the variability in model predictions suggests that differences in model predictions might be even larger for most other data sets. These findings suggest that modelers and clinicians must carefully consider their choice of growth model and how different growth assumptions might alter model predictions of the efficacy of treatment.

<a id='d7941cbc-4738-4716-a3ba-9e18731157b9'></a>

While our findings could be dismissed because they are based on a single example or because the models and the implementation of chemotherapy are highly simplified, we believe they highlight a significant problem. While many mathematical models used for clinical assessment

<!-- PAGE BREAK -->

<a id='f90d1cbf-cab5-4993-b452-56bd5cc63248'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='8af21d89-076f-4edb-b8c3-0346263b3387'></a>

Page 8 of 10

<a id='ee52a555-3418-4134-919c-02e4b246fd16'></a>

<::bar chart: Fig. 4 Estimates of clinically important measurements. Model predictions of the maximum tumor volume (left), doubling time (center), and minimum concentration of chemotherapy needed for eradication (right) based on parameter estimates from the half (top row) or the full (center row) Worschech data set. The bottom row shows the percent change in each of the predictions when the full data set is used rather than the truncated data set.The figure contains a 3x3 grid of bar charts. The x-axis for all charts is labeled with categories: Exp., Mendel., Logistic, Linear, Surface, Gomp., Bert. The rows represent data sets, and columns represent measurements. Top Row (Half Worschech data set):Chart 1 (Top Left): Y-axis: Max. tumor volume (mm³) x10⁴. Bars show values for each category.Chart 2 (Top Center): Y-axis: Doubling time (d). Bars show values for each category.Chart 3 (Top Right): Y-axis: Min. conc. of chemotherapy (/d). Bars show values for each category.Center Row (Full Worschech data set):Chart 4 (Middle Left): Y-axis: Max. tumor volume (mm³) x10⁴. Bars show values for each category.Chart 5 (Middle Center): Y-axis: Doubling time (d). Bars show values for each category.Chart 6 (Middle Right): Y-axis: Min. conc. of chemotherapy (/d). Bars show values for each category.Bottom Row (Percent change):Chart 7 (Bottom Left): Y-axis: % change in max. tumor volume. Bars show values for each category.Chart 8 (Bottom Center): Y-axis: % change in doubling time. Bars show values for each category.Chart 9 (Bottom Right): Y-axis: % change in min. chemo. conc. Bars show values for each category.::>

<a id='138a9f11-0076-4be5-ba7d-96d8b2f9f99e'></a>

of patients and development of radiation or chemother-
apy plans are more complex than those presented here
[47], they must all make some assumption of how the
tumor will grow. Due to the complexity of these models,
however, it is difficult to trace the effect of the choice of
growth model and determine how this choice might alter
the model's predictions. In fact, while model predictions
are often assessed for sensitivity to errors in estimates of
the parameters [48, 49], the effect of model assumptions
is often neglected. Our findings, however, indicate that
these assumptions could have a profound effect on model
predictions since our simple models show that different
choices of growth model result in large variations in model
predictions. The results of these inaccuracies could have
significant impacts on patient outcomes since we might
either provide too much treatment, causing more severe
side effects, or too little treatment, possibly resulting in
continued growth of the tumor. In fact, a recent analysis
of patients receiving radiation therapy suggests that tumor
size relative to its maximum possible size is a stronger

<a id='1e8ad7d6-bbf2-4b00-a482-aff5b2fd2927'></a>

indicator of response to treatment than simply the tumor size [50]. This is because the radiosensitivity of tumor cells is dependent on their growth and tumors closer to their maximum size are growing more slowly than tumors that still have room to grow. This simply highlights the need to accurately determine how tumors are growing when planning for dose and fractionation schedule.

<a id='3b32a1f8-b034-48a3-832c-fdcb7f250729'></a>

While some research has attempted to find the best
ODE model to describe tumor growth [30–33], the results
seem to suggest that there are no broad guidelines; the
most appropriate model seems to be dependent on the
details of the experiment. These papers used least-square
minimization, or minimization of information criterion
to determine the "best" model [44]. In our example, use
of minimum SSR would lead us to choose the Berta-
lanffy model as the "best" model, while use of AIC<sub>C</sub> would
lead us to choose the exponential model to fit the trun-
cated Worschech data set. However, further investigation
suggests that either of these models would actually be a
poor choice of model. The Bertalanffy did a poor job of

<!-- PAGE BREAK -->

<a id='83faa9f0-b470-455d-b06a-593ff61b1fb9'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='1cee3b97-6e28-458d-9299-9c8d58911e17'></a>

Page 9 of 10

<a id='e0dc830f-ce25-4f23-9b43-edda858f5114'></a>

predicting the future growth of the tumor (Fig. 2), and gave an extremely low estimate of the doubling time and a high estimate for the amount of chemotherapy needed to suppress the tumor. The exponential model overestimated the growth rate of the tumor and does not allow for slower growth of the tumor as resources are depleted.

<a id='f8ee4a90-da70-4aae-810d-9f14eadab2cc'></a>

While some modelers would perhaps fit several different growth models to a data set, current model selection techniques were not designed for the type of model selection problem faced by cancer modelers. Statistical measures such as the SSR, AICc, Mallow's Cp [51], Schwarz Bayesian information criterion [52], among others, all measure how well the model explains experimental data that has already been collected. A model selected as the best model using one of these measures should work reasonably well to make predictions if future behavior is similar to past behavior. Unfortunately, we know that this is often not the case when modeling tumor growth. Most experimental data sets capture the early growth of the tumor [31]. Modelers, however, would like to predict future growth where space and resource limitations hamper growth and structural changes such as a necrotic core, extracapsular extension, and angiogenesis will also affect growth dynamics [53–55], so the data used to select the model does not necessarily reflect the dynamics at the time when the predictions are made. In addition, it is well-known that experimental results in many pre-clinical systems do not translate well to human clinical studies [56–59]. A model chosen based on goodness-of-fit criteria to data from a pre-clinical experiment might not provide the most accurate predictions of future growth and treatment outcomes in humans. Our example suggests that more robust testing of model assumptions is needed before settling on a particular formulation. Minimization of SSR or information criterion does not guarantee selection of the best model for predicting future behavior.

<a id='73f51d9d-4a22-4c9f-b154-09a03dfc8e1d'></a>

## Conclusions
Our results show that choice of tumor growth model can lead to as much as a 12-fold change in predicted outcomes and that the model that best fits experimental data might not be the model that best predicts future growth. It is our hope that the findings presented here will spur more investigation into the effect of choice of cancer growth model on predicted treatment outcomes and that researchers will consider more than just best fit when selecting a growth model.

<a id='e4d93636-9f65-4d93-8560-070f8bc5267d'></a>

## Abbreviations
ODE: ordinary differential equation; SSR: sum of squared residuals; AICc: aikaike's information criterion.

<a id='120efa0a-0e3d-4812-a0a2-7ee2bfa6ea76'></a>

**Competing interests**
The authors declare that they have no competing interests.

<a id='41e4e620-dcba-406b-9b1b-a571bd36372a'></a>

**Authors' contributions**
HEM carried out the mathematical analysis and drafted the manuscript. HKJ
extracted the data and fit it to the models. HMD conceived and coordinated
the study and drafted the manuscript. All authors read and approved the final
manuscript.

<a id='491282ec-8820-440b-b3b6-1e8da82dd8f9'></a>

**Acknowledgements**
This research was supported by the NSF grant PHY-1358770.

<a id='231337d3-1cda-4d37-81e2-5d3e15a1d243'></a>

**Author details**

¹Department of Physics, Utica College, Utica, NY, USA. ²Department of Physics & Astronomy, Texas Christian University, 2800 S. University Drive, 76129, Fort Worth, TX, USA.

<a id='1bba6195-18ed-417e-94e6-b353b83e60a0'></a>

Received: 21 August 2015 Accepted: 14 February 2016
Published online: 26 February 2016

<a id='3082c5f5-5008-4de7-be5b-c6367caac495'></a>

References
1. Hanly P, Pearce A, Sharp L. The cost of premature cancer-related mortality: a review and assessment of the evidence. Exp Rev Pharmacoecon Outcomes Res. 2014;14(3):355–77. doi:10.1586/14737167.2014.909287.
2. Schmitz KH, DiSipio T, Gordon LG, Hayes SC. Adverse breast cancer treatment effects: the economic case for making rehabilitative programs standard of care. Support Care Cancer. 2015;23(6):1807–17. doi:10.1007/s00520-014-2539-y.
3. Carlotto A, Hogsett VL, Maiorini EM, Razulis JG, Sonis ST. The economic burden of toxicities associated with cancer treatment: Review of the literature and analysis of nausea and vomiting, diarrhoea, oral mucositis and fatigue. Pharmacoecon. 2013;31(9):753–66. doi:10.1007/s40273-013-0081-2.
4. Glynn R, Chin JZ, Kerin MJ, Sweeney KJ. Representation of cancer in the medical literature - a bibliometric analysis. PLOS One. 2010;5(11):13902. doi:10.1371/journal.pone.0013902.
5. Babu A, Templeton AK, Munshi A, Ramesh R. Nanodrug delivery systems: A promising technology for detection, diagnosis, and treatment of cancer. AAPS Pharmscitech. 2014;15(3):709–21. doi:10.1208/s12249-014-0089-8.
6. Pol J, Bloy N, Obrist F, Eggermont A, Galon J, Cremer I, Erbs P, Limacher JM, Preville X, Zitvogel L. Trial watch oncolytic viruses for cancer therapy. Oncoimmunology. 2014;3:28694. doi:10.4161/onci.28694.
7. Ceresa C, Bravin A, Cavaletti G, Pellei M, Santini C. The combined therapeutical effect of metal-based drugs and radiation therapy: The present status of research. Curr Med Chem. 2014;21(20):2237–65. doi:10.2174/0929867321666140216125721.
8. Bakhshinejad B, Karimi M, Sadeghizadeh M. Bacteriophages and medical oncology: targeted gene therapy of cancer. Med Oncol. 2014;31(8):110. doi:10.1007/s12032-014-0110-9.
9. Kuroki M, Shirasu N. Novel treatment strategies for cancer and their tumor-targeting approaches using antibodies against tumor-associated antigens. Anticancer Res. 2014;34(8):4481–8.
10. Agur Z, Vuk-Pavlovic S. Mathematical modeling in immunotherapy of cancer: Personalizing clinical trials. Mol Ther. 2012;20(1):1–2. doi:10.1038/mt.2011.272.
11. Agur Z, Elishmereni M, Kheifetz Y. Personalizing oncology treatments by predicting drug efficacy, side-effects, and improved therapy: mathematics, statistics, and their integration. Wiley Interdiscip Rev Syst Biol Med. 2014;6(3):239–53. doi:10.1002/wsbm.1263.
12. Elias J, Dimitrio L, Clairambault J, Natalini R. The p53 protein and its molecular network: Modelling a missing link between dna damage and cell fate. Biochim Biophys Acta, Proteins Proteomics. 2014;1844(1):232–47. doi:10.1016/j.bbapap.2013.09.019.
13. Laird AK. Dynamics of tumor growth. Br J Cancer. 1965;19(2):278–91.
14. Laird AK. Dynamics of tumor growth. Br J Cancer. 1964;13:490–502.
15. Summers W. Dynamics of tumor growth — a mathematical model. Growth. 1966;30(3):333.
16. Dethlefsen LA, Prewitt JMS, Mendelsohn ML. Analysis of tumor growth curves. J Nat Cancer Inst. 1968;40(2):389–405.
17. Brodin NP, Vogelius IR, Bjork-Eriksson T, af Rosenschold PM, Maraldo MV, Aznar MC, Specht L, Bentzen SM. Optimizing the radiation therapy dose prescription for pediatric medulloblastoma: Minimizing the life years lost

<!-- PAGE BREAK -->

<a id='2810347e-99cb-428b-bf7c-cc91a3d75216'></a>

Murphy et al. BMC Cancer (2016) 16:163

<a id='983d648d-b208-45ce-b4b5-2da90f8a2dd1'></a>

Page 10 of 10

<a id='595538a6-c4f3-451a-b74a-fdb6e42012ba'></a>

attributable to failure to control the disease and late complication risk. Acta Oncologica. 2014;53(4):462-70. doi:10.3109/0284186X.2013.858824.
18. Batmani Y, Khaloozadeh H. Optimal drug regimens in cancer chemotherapy: A multi-objective approach. Comput Biol Med. 2013;43: 2089-95. doi:10.1016/j.compbiomed.2013.09.026.
19. Huang X, Ning J, Wahed AS. Optimization of individualized dynamic treatment regimes for recurrent diseases. Stat Med. 2014;33(14):2363-78. doi:10.1002/sim.6104.
20. Moodie EEM, Richardson TS, Stephens DA. Demystifying optimal dynamic treatment regimes. Biom. 2014;63(2):447-55. doi:10.1111/j.1541-0420.2006.00686.x.
21. Wang Z, Deisboeck TS. Mathematical modeling in cancer drug discovery. Drug Discov Today. 2014;19(2):145-50. doi:10.1016/j.drudis.2013.06.015.
22. Panetta JC. A mathematical model of drug resistance: Heterogeneous tumors. Math Biosci. 1998;147:41-61. doi:0025-5564/98.
23. Sakode CM, Padhi R, Kapoor S, Rallabandi VPS, Roy PK. Multimodal therapy for complete regression of malignant melanoma using constrained nonlinear optimal dynamic inversion. Biomed Signal Process Control. 2014;13:198-211. doi:10.1016/j.bspc.2014.04.010.
24. de Pillis LG, Gu W, Radunskaya AE. Mixed immunotherapy and chemotherapy of tumors: modeling, applications and biological interpretations. J Theo Biol. 2006;238(4):841-62. doi:10.1016/j.jtbi.2005.06.037.
25. Panetta JC. A logistic model of periodic chemotherapy with drug resistance. Appl Math Lett. 1997;10(1):123-7. doi:0893-9659/97.
26. Foo J, Michor F. Evolution of acquired resistance to anti-cancer therapy. J Theor Biol. 2014;355:10-20. doi:10.1016/j.jtbi.2014.02.025.
27. Gerlee P. The model muddle: In search of tumor growth laws. Cancer Res. 2013;73(8):2407-11. doi:10.1158/0008-5472.CAN-12-4355.
28. Wodarz D, Komarova N. Towards predictive computational models of oncolytic virus therapy: Basis for experimental validation and model selection. PLoS One. 2009;4(1):4271. doi:10.1371/journal.pone.0004271.
29. Usher JR. Some mathematical models for cancer chemotherapy. Comput Math Applic. 1994;28(9):73-80. doi:0898-1221 (94)00179-0.
30. Vaidya VG, Alexandro FJ. Evaluation of some mathematical models for tumor growth. Int J Bio-Med Comput. 1982;13(1):19-35.
31. Sarapata EA, de Pillis LG. A comparison and catalog of intrinsic tumor growth models. Bull Math Biol. 2014;76(8):2010-24. doi:10.1007/s11538-014-9986-y.
32. Benzekry S, Lamont C, Beheshti A, Tracz A, Ebos JML, Hlatky L, Hahnfeldt P. Classical mathematical models for description and prediction of experimental tumor growth. Plos Comp Biol. 2014;10(8): 1003800. doi:10.1371/journal.pcbi.1003800.
33. Hartung N, Mollard S, Barbolosi D, Benabdallah A, Chapuisat G, Henry G, Giacometti S, Iliadis A, Ciccolini J, Faivre C, Hubert F. Mathematical modeling of tumor growth and metastatic spreading: Validation in tumor-bearing mice. Cancer Res. 2014;74(22):6397-407. doi:10.1158/0008-5472.CAN-14-0721.
34. Collins VP, Loeffler RK, Tivey H. Observations on growth rates of human tumors. Am J Roentgenol Radium Ther Nuc Med. 1956;78(5):988-1000.
35. Mendelsohn ML. Cell proliferation and tumor growth. In: Lamberton LF, Fry RJM, editors. Cell Proliferation. Oxford: Blackwell Scientific Publications; 1963. p. 190-210.
36. Verhulst PF. Notice sur la loi que la population poursuit dans son accroissement. Correspondance mathématique et physique. 1838;10: 113-21.
37. Patt HM, Blackford ME. Quantitative studies of the growth response of the Krebs ascites tumor. Cancer Res. 1954;14(5):391-6.
38. von Bertalanffy L. Problems of organic growth. Nature. 1949;163(4135): 156-8. doi:10.1038/163156a0.
39. Gompertz B. On the nature of the function expressive of the law of human mortality, and on a new method of determining the value of life contingencies. Phil Trans Roy Soc. 1825;27:513-85.
40. Winsor CP. The gompertz curve as a growth curve. Proc Nat Acad Sci USA. 1932;18(1):1-8. doi:10.1073/pnas.18.1.1.
41. Strogatz SH. Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering. Cambridge, MA: Perseus Books; 1994.
42. Mehrara E, Forssell-Aronsson E, Johanson V, Kö6lby L, Hultborn R, Bernhardt P. A new method to estimate parameters of the growth model

<a id='ab475caa-8259-4f6f-967f-1d19487d3824'></a>

for metastatic tumours. Theor Biol Med Modell. 2013;10:31–43. doi:10.1186/1742-4682-10-31.
43. Worschech A, Chen N, Yu YA, Zhang Q, Pos Z, Weibel S, Raab V, Sabatino M, Monaco A, Liu H, Monsurró V, Buller RM, Stroncek DF, Wang E, Szalay AA, Marincola FM. Systemic treatment of xenografts with vaccinia virus GLV-1h68 reveals the immunologic facet of oncolytic therapy. BMC Genomics. 2009;10:301. doi:10.1186/1471-2164-10-301.
44. Burnham KP, Anderson DR. Model Selection and Multimodel Inference: A Practical Information-Theoretic Approach, 2nd. New York, USA: Springer; 2002.
45. Folkman J, Hochberg M. Self-regulation of growth in 3 dimensions. J Exp Med. 1973;139(4):745–53. doi:10.1084/jem.138.4.745.
46. Brenner MW, Holsti LR, Perttala Y. The study by graphical analysis of the growth of human tumours and metastases of the lung. Brit J Cancer. 1967;21(1):1–13.
47. Marcu LG, Harriss-Phillips WM. In silico modelling of treatment-induced tumour cell kill: Developments and advances. Comp Math Meth Med. 2012:2012:960256. doi:10.1155/2012/960256.
48. Hoffmann A, Scherrer A, Kufer KH. Analyzing the quality robustness of chemotherapy plans with respect to model uncertainties. Math Biosci. 2015;259:55–61. doi:10.1016/j.mbs.2014.11.003.
49. Krause M, Scherrer A, Thieke C. On the role of modeling parameters in IMRT plan optimization. Phys Med Biol. 2008;53(18):4907–26. doi:10.1088/0031-9155/53/18/004.
50. Prokopiou S, Moros EG, Poleszczuk J, Caudell J, Torres-Roca JF, Latifi K, Lee JK, Myerson R, Harrison LB, Enderling H. A proliferation saturation index to predict radiation response and personalize radiotherapy fractionation. Radiat Oncol. 2015;10:159. doi:10.1186/s13014-015-0465-x.
51. Mallows C. Some comments on c~p~. Technometrics. 1973;15(4):661–75. doi:10.2307/1267380.
52. Schwarz G. Estimating the dimension of a model. Ann Stat. 1978;6(2):461–4. doi:10.1214/aos/1176344136.
53. Kolobov AV, Kuznetsov MB. Investigation of the influence of angiogenesis on tumor growth with the use of a mathematical model. Biofizika. 2015;60(3):555–63.
54. Cooper MD, Tanaka ML, Puri IK. Coupled mathematical model of tumorigenesis and angiogenesis in vascular tumours. Cell Proliferation. 2010;43(6):542–52. doi:10.1111/j.1365-2184.2010.00703.x.
55. Emerick KS, Leavitt ER, Michaelson JS, Diephuis B, Clark JR, Deschler DG. Initial clinical findings of a mathematical model to predict survival of head and neck cancer. Otolaryngol Head Neck Surg. 2013;149(4):572–8. doi:10.1177/0194599813495178.
56. Elias KM, Emori MM, Papp E, MacDuffie E, Konecny GE, Velculescu VE, Drapkin R. Beyond genomics: Critical evaluation of cell line utility for ovarian cancer research. Gynocol Oncol. 2015;139(1):97–103. doi:10.1016/j.ygyno.2015.08.017.
57. Ruggeri BA, Camp F, Miknyoczki S. Animal models of disease: Pre-clinical animal models of cancer and their applications and utility in drug discovery. Biochem Pharmacol. 2014;87(1):150–61. doi:10.1016/j.bcp.2013.06.020.
58. Westwood J, Darcy PK, Kershaw MH. The potential impact of mouse model selection in preclinical evaluation of cancer immunotherapy. Oncoimmunol. 2014;3(7):946361. doi:10.4161/21624011.2014.946361.
59. McGonigle P, Ruggeri B. Animal models of human disease: Challenges in enabling translation. Biochem Pharmacol. 2014;87(1):162–71. doi:10.1016/j.bcp.2013.08.006.