<a id='33bfc81b-eca5-44a6-a8fb-b719a5a69d3b'></a>

Jurnal
Teknologi

<a id='eea116aa-3aa3-4ede-9c8d-f1737e006f6b'></a>

Full Paper

<a id='58a9a441-a020-4b04-9477-65e138a417e4'></a>

MODELLING TUMOR GROWTH WITH IMMUNE
RESPONSE AND DRUG USING ORDINARY
DIFFERENTIAL EQUATIONS

<a id='86b9d574-1945-49ab-9004-7d696544767c'></a>

**Article history**
Received
*18 October 2016*
Received in revised form
*8 May 2017*
Accepted
*31 May 2017*

<a id='f37738d5-6b34-429d-8d5b-86a2423990f1'></a>

Mohd Rashid Admon, Normah Maan*

<a id='dcd38dfc-bd77-4ab5-830f-ae4946a847c3'></a>

Department of Mathematical Sciences, Faculty of Sciences,
81310, UTM Johor Bahru, Malaysia

<a id='47355114-e8d5-41e7-be94-4c1a1f2c9390'></a>

*Corresponding author
normahmaan@utm.my

<a id='8bc19838-bcea-47ea-8790-e00415807fae'></a>

Graphical abstract <::A diagram illustrating the cell cycle. The cell cycle is represented as a circular flow, with an outer orange ring and an inner segmented ring. The inner ring is divided into phases: G1 (light blue), S (red), G2 (dark green), and M (purple). An additional 'M' phase (yellow) is shown at the top, outside the main cycle. Below the G1 phase, there is an 'I' segment (light blue) that appears to be part of the G1 phase. Arrows indicate the progression of the cycle in a clockwise direction. From the G1 phase, an arrow points outwards to a G0 phase, indicating a resting state. At the top of the cycle, near the yellow M phase, a syringe is depicted injecting into the cycle, with the text "Drug was Injected" next to it. From this point, two small circular cells with purple nuclei are shown emerging, indicating cell division.: diagram::>

<a id='1a8e0b28-ca6f-4253-9fcb-e6141fafb626'></a>

Abstract
This is a mathematical study about tumor growth from a different perspective, with the aim of predicting and/or controlling the disease. The focus is on the effect and interaction of tumor cell with immune and drug. This paper presents a mathematical model of immune response and a cycle phase specific drug using a system of ordinary differential equations. Stability analysis is used to produce stability regions for various values of certain parameters during mitosis. The stability region of the graph shows that the curve splits the tumor decay and growth regions in the absence of immune response. However, when immune response is present, the tumor growth region is decreased. When drugs are considered in the system, the stability region remains unchanged as the system with the presence of immune response but the population of tumor cells at interphase and metaphase is reduced with percentage differences of 1.27 and 1.53 respectively. The combination of immunity and drug to fight cancer provides a better method to reduce tumor population compared to immunity alone.

<a id='2af9cfb8-f3ff-4338-8abc-e837a4dd4375'></a>

Keywords: Tumor growth, immune response, cycle phase specific drug, cell cycle, stability region

<a id='6e751b8b-9e22-4f98-8792-1f688cca870a'></a>

## Abstrak
Kajian ini adalah berkenaan dengan pertumbuhan tumor daripada sudut perspektif yang berbeza, bertujuan untuk meramal atau mengawal penyakit tersebut. Fokus perspektif tersebut adalah kesan dan interaksi antara sel tumor dengan sistem imunisasi dan ubat. Kajian ini menerangkan sistem persamaan terbitan yang melibatkan pertumbuhan tumor bersama tindak balas imunisasi dan ubat yang bertindak mengikut fasa spesifik dalam kitaran sel. Kaedah analisis kestabilan digunakan untuk menghasilkan kawasan kestabilan bagi nilai-nilai parameter tertentu dalam fasa mitosis. Kawasan kestabilan untuk ketidakhadiran tindak balas imunisasi menunjukkan kawasan pertumbuhan tumor dan kawasan pereputan tumor dipisahkan oleh garis lengkuk. Dengan kehadiran tindak balas imunisasi, kawasan pertumbuhan tumor didapati berkurang. Apabila ubat untuk kitaran spesifik diambil kira dalam sistem, kawasan kestabilan tidak mengalami sebarang perubahan tetapi pertumbuhan sel-sel tumor pada kedua-dua fasa berkurang dengan perbezaan peratus masing-masing 1.27 dan 1.53. Ini menunjukkan bahawan gabungan antara imunisasi dan ubat adalah cara yang lebih baik untuk mengurangkan populasi sel tumor berbanding dengan hanya bergantung pada tindak balas imunisasi sahaja.

<a id='c2ef1689-803f-4917-89b1-f36fd3b1639c'></a>

Kata kunci: Pertumbuhan tumor, tindak balas imunisasi, ubat untuk kitaran fasa spesifik, kitaran sel, kawasan kestabilan

<a id='6c2712a0-2f77-477a-9051-d0b63cc8ec15'></a>

© 2017 Penerbit UTM Press. All rights reserved

<a id='b9121bac-8ee8-46fd-ab0b-d14ad55da67b'></a>

79:5 (2017) 49–56 | www.jurnalteknologi.utm.my | eISSN 2180–3722 |

<!-- PAGE BREAK -->

<a id='d47fb597-b765-4be5-bbe4-be36adcf9d25'></a>

50

<a id='44b55594-980c-42f4-a7c1-976bb934f2d6'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='8817b7c1-bc2d-4072-a231-271b5c1e7077'></a>

## 1.0 INTRODUCTION

Every year more than 8.2 million people die from cancer worldwide [1]. World Health organization [2] reports that the majority of death caused by cancer occurs in countries that are economically well developed. This scenario forces scientists all over the world to develop theory and practical strategies to address the threat from cancer. On the whole, most researchers focused on particular issues since the interaction between tumor cells and other type of cells are very complex. Immune system plays an important role in human body to fight tumor. However there are limits for ability of immune system due to unpredictable tumor behaviour [3]. In medical treatment, chemotherapy offers a powerful mechanism among other tools to kill cancer cell, but it also kill the normal cells [4, 5, 6].

<a id='6bd42b53-5054-4315-b568-05b2816ee918'></a>

The problem of modelling tumor growth is a vast study by researchers, with each focussing on different aspects on cancer development [7]. This includes the importance of the immune systems in fighting tumor that has been summarized by Adam and Bellomo [8]. Kuznetsov et al. [9] proposed an ordinary differential equation model of the cytotoxic T lymphocyte (CTL) response with population of tumor cells. They found that CTL and tumor cells competed like "predator-prey" interaction in which CTL in the role of predator while tumor cell act as prey. Adam [10] then formulated the cell populations of a solid tumor and reactive lymphocyte and found that if the immune system is stimulated, the survival chance for tumor increases. In addition, whether growth rate and death rate increase or decrease, this condition will probably lead to an uncontrolled tumor growth. De Pillis et al. [11] proceeded to develop and analyze a mathematical model in order to understand the dynamics between tumor and immune system. The model concluded out that the combination effect of natural killer (NK) and CD8+ T cells could eliminate larger tumors compared to the effect of individual immune cell. This is due to the depletion of NK cells having different impact to CD8+ T cells.

<a id='f943527d-ecc3-49de-8167-c3e251da50a5'></a>

Chemotherapy is usually the first treatment for cancer [4, 5, 6, 12, 13]. Pastorino et al. [14] reported that chemotherapy treatments are in the process of improvement for better distribution mechanism that will reduce the toxicity of anticancer drugs. Besides, most of the drug used are cycle phase specific drugs such as vincristine and paclitaxel which interfere with certain phases in cell cycle [15]. It may prevent the cell from continuing the cycle, causing the proliferation to be stopped. Immune system then target and kill the cancerous cell by their natural mechanism. By taking this advantage, it will minimized the loss of normal cells. The use of cycle phase specific drugs have been included in the model proposed by Villasana M. and Radunskaya [16]. However, they did not present results of analysis and numerical computation had not been shwn in their paper.
A different approach was adopted by Villasana M. and Radunskaya [16]. They presented a system of

<a id='b65fad81-a373-472a-adb0-88cbcc9f7f6c'></a>

differential equations without considering any delay terms. Numerical results were done as a contribution to investigate the stability of the presented model. The model takes the form of ordinary differential equation (ODE) which includes tumor cell population during interphase, tumor population during metaphase, immune response and cycle phase with specific drugs. Three different systems were discussed by analysing its stability and numerical examples using Fourth Order Runge Kutta Method.

<a id='1c1ac79a-c8ca-4447-b1a9-422dec5e8ab2'></a>

## 2.0 METHODOLOGY
The tumor growth model considered in this paper is a system of first order differential equations with nᵗʰ dimensional system.

<a id='5c36f558-8ad6-4dce-ad71-18e078a8cc66'></a>

dx1 / dt = f1(x1, x2, ..., xn)
dx2 / dt = f2(x1, x2, ..., xn)
...
dxn / dt = fn(x1, x2, ..., xn) (1)

<a id='45de623c-60fa-4a40-b809-00538768b31a'></a>

where x1, x2,..., xn are the variables, f1, f2,..., fn can be linear or nonlinear functions and the right hand side of the ODEs may depend only on the independent variable t [17]. The first step is to find the steady state solution of the system

<a id='0c36c650-62fd-4023-8f3f-6358485c2c5b'></a>

## 2.1 Steady State Solution

A steady state or equilibrium point, $\bar{X} = (\bar{x}_1,\bar{x}_2, ..., \bar{x}_n)$ is a situation in which the system does not appear to undergo any change [18]. To find the steady state of a system, set the derivatives equal to zero:

$$ \frac{dx_1}{dt} = 0 $$
$$ \frac{dx_2}{dt} = 0 $$
$$ \vdots $$
$$ \frac{dx_n}{dt} = 0 $$ (2)

<a id='38c600d7-d10f-4ce5-b726-d463860edd6c'></a>

There may exist one or several steady state points.

<a id='5a8ff4d6-4d68-4e6c-993f-b5e09b1defdf'></a>

## 2.2 Stability of Steady State

The stability of steady state can be investigated by using Routh-Hurwitz condition/criteria [18, 19, 20]. System (1) is linearized using Jacobian Matrix

```
          (∂f₁   ...   ∂f₁  )
          |∂x₁         ∂xₙ  |
          |∵    ∴    ∵  |
J(ē₁, ē₂, ..., ēₙ) = |∂fₙ   ...   ∂fₙ  |  (3)
          |∂x₁         ∂xₙ  |
          (                 )
```

<a id='57ab0852-a74e-43fd-b556-29d2616b86a1'></a>

The next step is to find the eigenvalues, \lambda satisfying

<!-- PAGE BREAK -->

<a id='9cd1eb08-355e-4d34-b28f-9cdeb8dc7245'></a>

51

<a id='49bb7673-6f18-4bb5-9d23-10a086e07a3c'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='be2844d7-686a-42a9-af07-86822f27731c'></a>

det(J − ̸̸I) = ̸̸

(4)

<a id='9c8a73e5-bb3f-43f3-958b-d4195cfc031a'></a>

This will yield a characteristic equation of the form

$\lambda^n + p_1\lambda^{n-1} + p_2\lambda^{n-2} + \ldots + p_n = 0\quad(5)$

<a id='72c47e08-553f-4502-bf15-be2d46ef4769'></a>

where pi's will be functions of the elements of the n x
n matrix.

<a id='5fd2801c-10e5-439d-b91a-f55df504c7f2'></a>

The Hurwitz matrix is defined as follows:

<a id='ace931bf-f77a-4f29-8871-5a59b34ac712'></a>

H_1 = (p_1),
H_2 = \begin{pmatrix} p_1 & 1 \\ p_3 & p_2 \end{pmatrix},
H_3 = \begin{pmatrix} p_1 & 1 & 0 \\ p_3 & p_2 & p_1 \\ p_5 & p_4 & p_3 \end{pmatrix} ...

H_j = \begin{pmatrix} p_1 & 1 & 0 & \dots & 0 \\ p_3 & p_2 & p_1 & \dots & 0 \\ p_5 & p_4 & p_3 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ p_{2j-1} & p_{2j-2} & p_{2j-3} & \dots & p_j \end{pmatrix} ... (6)

H_n = \begin{pmatrix} p_1 & 1 & 0 & \dots & 0 \\ p_3 & p_2 & p_1 & \dots & 0 \\ p_5 & p_4 & p_3 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & p_n \end{pmatrix}

<a id='d3132cd6-e47b-48ce-81f0-66f5c58b683a'></a>

where the (l, m) element in the matrix H_j is

p_2l-m for 0 < 2l - m < k
1 for 2l = m
2 for 2l < m or 2l > k + m

<a id='2ffb182d-62ee-4199-91e1-0ae16428a3fc'></a>

Hence, all eigenvalues have negative real parts
(steady state stable) if and only if the determinants of
the Hurwitz matrix are positive:

<a id='221ff1a6-3c14-4387-bb0c-3fbf9737e74e'></a>

det(**H**_j) > 0, (j = 1,2,...,k) (7)

<a id='b16a972e-4422-4280-8841-0f435ff213ab'></a>

## 2.3 Numerical Method
Runge Kutta (RK4) method is applied to present several graphical results using MATLAB software. Tay _et al._ [21] considered an initial value problem of the first order differential equation given below:

<a id='d2f37d06-5712-412d-b6eb-cccb313c814a'></a>

$$\frac{dx}{dt} = F(t, x, y)$$
$$\frac{dy}{dt} = G(t, x, y) \quad (8)$$

<a id='3a35ed16-e50e-4cd5-a397-381c4b341379'></a>

with x(t_0) = x_0, y(t_0) = y_0 and t_0 ≤ t ≤ t_n. This problem
is a system of ODEs, which consists of a single pair of
ordinary differential equations. The solution domain is
discretized such that t_0, t_1 = t_0 + h, t_n = t_0 + nh, where
h is the step size of t. The solution that is obtained by
the RK4 method is given as

<a id='83771d59-2e50-4a69-b390-b0f57bad96cb'></a>

x_{i+1} = x_i + \frac{1}{6}(f_1 + 2f_2 + 2f_3 + f_4),
y_{i+1} = y_i + \frac{1}{6}(g_1 + 2g_2 + 2g_3 + g_4), (9)

<a id='fb3b1750-c75d-404f-92d4-7a81ab64364c'></a>

where

<a id='fe574b24-b78a-4007-bc83-0357d9553801'></a>

f₁ = hf (tᵢ, xᵢ, yᵢ)
f₂ = hf (tᵢ + h/2, xᵢ + f₁/2, yᵢ + g₁/2)
f₃ = hf (tᵢ + h/2, xᵢ + f₂/2, yᵢ + g₂/2)
f₄ = hf(tᵢ + h, xᵢ + f₃, yᵢ + g₃)
g₁ = hg(tᵢ, xᵢ, yᵢ)
g₂ = hg (tᵢ + h/2, xᵢ + f₁/2, yᵢ + g₁/2)
g₃ = hg (tᵢ + h/2, xᵢ + f₂/2, yᵢ + g₂/2)
g₄ = hg(tᵢ + h, xᵢ + f₃, yᵢ + g₃)

<a id='d030b24b-cabb-4eac-be05-10fea3537b89'></a>

## 3.0 RESULTS AND DISCUSSION

The system considers three population which are population of tumor cells during interphase (G₁ + S + G₂) denoted by T₁, population of tumor cells during mitosis denoted by T_M and population of immune response denoted by I. In this research, Cytotoxic T Lymphocytes (CTL) is assume to be main representative of the immune system in fight cancer. A certain amount of cycle phase specific drug is included to analyze the effect on the system. The model takes form

<a id='cd649b45-51f9-4b56-afa6-0ee738f75c8d'></a>

$$\frac{dT_I}{dt} = 2a_4T_M - (c_1I + d_2)T_I - a_1T_I$$$$\frac{dT_M}{dt} = a_1T_I - d_3T_M - a_4T_M - c_3T_MI - k_1(-e^{-k_2u})T_M$$$$\frac{dI}{dt} = k + \frac{\rho I(T_I + T_M)^n}{\alpha + (T_I + T_M)^n} - c_2IT_I - c_4T_MI - d_1I - k_3(1-e^{-k_4u})I \quad (10)$$$$\frac{du}{dt} = -\gamma u$$

<a id='ef3810ab-1202-4771-ab72-ab31edd9bba2'></a>

where parameter a₁ and a₄ represent the rates of cell cycle and rates of cell reproduction respectively. Besides, the proportion for cell deaths are represent by the term d₂Tᵢ, d₃Tₘ and d₁I. Note that the term 2a₄Tₘ present in the equation because in fact, one parent cell will split into two new daughter cells during mitosis. The parameter cᵢ then represent the losses of immune cell or tumor cell during the event of an encounter for both cell. Due to the presence of tumor, the growth for immune population is assumed to be nonlinear which indicated by the term ρI(Tᵢ+Tₘ)ⁿ / α+(Tᵢ+Tₘ)ⁿ. Another

<a id='864b65d2-9496-4ea4-8988-cda004ed4f3e'></a>

parameter which are p, a, and n in the equations are
influence by the type of tumor itself together with the
healthiness of patient's immune system.

<a id='3069446b-bfaa-4ec2-9b44-734ff7065aeb'></a>

The impact of drug towards tumor population in
mitosis and immune are modeled by the killing terms

<!-- PAGE BREAK -->

<a id='e6613d6e-c3c9-4c8d-9ee5-3e8ffea0f458'></a>

52

<a id='461f22e6-f22b-4162-a054-629d88ad1024'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='517228f7-140b-4806-9b3d-3b23f7a15f0c'></a>

k_1(1 - e^{-k_2 u})T_M and k_3(1 - e^{-k_4 u})I respectively. Since the drug is decay over time, it assumed to be exponential while parameter \gamma acts as both elimination and absorption effects. This paper highlights only an application of single drug dose treatment, otherwise it is beyond the scope of this paper.

<a id='b89fb1c8-f9d4-4b78-82c9-878ff8ee604b'></a>

It is important to know that the parameter values are vary for any model presented since patients have different types of tumor. Thus, it is allowed to vary the parameter values in order to understand better of tumor problem. This research will used the non dimensionalized parameter that have been set by Villasana and Ochoa [21].

<a id='ce6009f0-e0b2-41df-9bf2-378da0c7078b'></a>

a₁ = 0.98; a₄ = 0.8; d₁ = 0.29; d₂ = 0.11; d₃ = 0.4
c₁ = c₃ = 0.9; c₂ = c₄ = 0.085; k = 0.029
k₁ = 0.47; k₂ = 0.57; k₃ = 0.49; k₄ = 0.061
α = 0.2; ρ = 0.1; n = 3; γ = 0.85

<a id='50d1f2d9-d676-4510-b806-fb064722a402'></a>

The analysis is divide into three cases which are tumor system without immune response, tumor system with the presence of immune response and tumor system with single drug. The behavior of these system are depended on fixed point and its stability. Numerical examples for certain chosen parameters in stability region are then computed using Fourth Order Runge Kutta Method.

<a id='b0822f46-7f50-4bf2-a79a-b8ac449cf430'></a>

## 3.1 Tumor System without Immune Response
Consider a system of ordinary differential equations:

<a id='7bd3ebf9-1030-4055-a253-bb5a851e8f0b'></a>

dT_I / dt = 2a_4 T_M - (d_2 + a_1)T_I
dT_M / dt = a_1 T_I - d_3 T_M - a_4 T_M (11)

<a id='70c6633c-4f6e-439e-9239-157eaa86a11d'></a>

The auxiliary equation at tumor free point ($T_I, T_M$) = (0,0) is

<a id='a3b15d37-b198-4891-9105-cb4fba17df67'></a>

λ² + (a₁ + d + d₂)λ + d(a₁ + d₂) - 2a₁a₄ = 0 (12)

  λ² + p₁λ + p₂ = 0 (13)

<a id='1773c870-21c0-4682-b8a9-7c93cd4724a6'></a>

where

<a id='3e85887d-60b5-433d-87cb-8a4917bdf9ac'></a>

∴ p₁ = a₁ + d + d₂ (14)
p₂ = d(a₁ + d₂) - 2a₁a₄ (15)

<a id='6d045771-c9f2-4b14-9f9d-05da27944396'></a>

The value of p₁ from Eq. (14) is always positive [15, 16,
22]. The value of p₂ can be negative or positive.
According to the Routh-Hurwitz stability criteria, the
tumor free point will be stable if p₁ > 0 and p₂ > 0.
Thus, the necessary condition for the tumor growth is
given by Eq. (16).

<a id='08c3c6d6-f2b6-4843-baca-cc49cde8595b'></a>

d < (2a1a4) / (a1 + d2) (16)

<a id='55d4904b-6cef-4220-b8e4-3900df4cf77a'></a>

<::chart: 2D plot showing a stability region. The x-axis is labeled "$a_1$" and ranges from 0 to 1. The y-axis is labeled "$d$" and ranges from 0 to 2. A blue curve starts at (0,0) and increases, dividing the plot into two regions. Region I is below the curve. Region II is above the curve. Figure 1 Stability region for the case without immune response when $a_4 = 0.8$ and $d_2 = 0.11$::>

<a id='238a5bfc-d620-4779-b2a8-a9dbb043ec3d'></a>

<::chart: A line graph titled "Figure 2 Numerical example for stable fixed point (0,0) when $a_1 = 1$ and $d = 1.9$ with initial condition $T_I(0) = 1.3$ and $T_M(0) = 1.2$". The x-axis is labeled "t" and ranges from 0 to 60. The y-axis is labeled "Ti and Tm" and ranges from 0 to 1.4. There are two lines plotted: a blue line labeled "Ti" and a red line labeled "Tm". Both lines start high on the y-axis (Ti around 1.4 and Tm around 1.2) and decrease exponentially, approaching 0 as t increases.:;>

<a id='c92a9831-26dc-41d8-9515-bc7f2a9319f4'></a>

<::line chart showing two exponentially increasing curves. The y-axis is labeled "Ti and Tm" and ranges from 0 to 160. The x-axis is labeled "t" and ranges from 0 to 15. A legend indicates a blue line as "Ti" and a red line as "Tm". Both curves start near the origin and diverge as 't' increases, with the "Ti" curve consistently above the "Tm" curve. Figure 3 Numerical example for unstable fixed point (0,0) when a₁ = 1 and d = 0.8 with initial condition Tᵢ(0) = 1.3 and T_M(0) = 1.2: chart::>

<!-- PAGE BREAK -->

<a id='37188502-6885-4821-8394-2e9eec35dabe'></a>

53

<a id='b0ff12ab-7ec3-4814-ae7f-01e97d9c9fab'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='8160345c-ff76-4b7f-9981-b63a0a7b2a1d'></a>

From Figure 1, the region for tumor growth where (0,0)
unstable is given by I and the region for tumor decay
where (0,0) stable is given by the complement II. The
values were chosen from different regions to observe
the solution of the system as presented in Figure 2 and
Figure 3.

<a id='a530d09e-b2e5-414d-8268-fe4f55e6eecd'></a>

**3.2 Tumor System with the presence of Immune Response**

In this case, the effect of immune response is added to the model. The system of equations now becomes

<a id='fd970a09-aa12-4d42-946f-d730f24d3096'></a>

$$\frac{dT_I}{dt} = 2a_4 T_M - (c_1 I + d_2)T_I - a_1 T_I$$

$$\frac{dT_M}{dt} = a_1 T_I - d_3 T_M - a_4 T_M - c_3 T_M I \quad (17)$$

$$\frac{dI}{dt} = k + \frac{\rho I(T_I + T_M)^n}{\alpha + (T_I + T_M)^n} - c_2 I T_I - c_4 T_M I - d_1 I$$

<a id='27cbdb9f-3618-4a1b-af60-2b424a7f46a1'></a>

One of the tumor free point is ($T_I, T_M, I$) = ($0,0, \frac{k}{d_1}$) with zero tumor population. This is our starting point since it represents a tumor free condition. The factorization form of the auxiliary equation at this steady state yields Eq. (18).

<a id='89d3b2e5-7022-4b31-add6-ddf4b2a95f84'></a>

(-d₁ - λ)[(-c₁d̄₁ - d₂ - a₁ - λ)(-d - c₃d̄₁ - λ) - 2a₁a₄] = 0 (18)

<a id='5987edef-d6f2-489c-8c48-5079fb5c99c4'></a>

where d̄₁ = k/d₁. Clearly, one of the eigenvalue is λ = -d₁. The remaining eigenvalues are given as the solution to the auxiliary equation

<a id='6e156961-52c2-40e9-9e52-941a79a2d195'></a>

λ² + [a₁ + d₂ + (c₁ + c₃)d̄₁ + d]λ
+ (a₁ + d₂ + c₁d̄₁)(d + c₃d̄₁) - 2a₁a₄ = 0 (19)
λ² + p₁*λ + p₂* = 0 (20)

<a id='8bf778b9-d209-4410-89fa-cb1e46c38459'></a>

where

<a id='4c708638-04e4-4ae3-9afa-523b117f8b87'></a>

∴ p₁* = a₁ + d₂ + (c₁ + c₃)d̄₁ + d (21)
p₂* = (a₁ + d₂ + c₁d₁)(d + c₃d̄₁) - 2a₁a₄ (22)

<a id='4c942eb2-7a5b-4893-b2a4-b3aeb4671c5b'></a>

The value of p₁* is always positive [15, 16, 22]. The value
of p₂* can be negative or positive. According to the
Routh-Hurwitz stability criteria the fixed point (0,0, k/d)

<a id='65021c64-89a9-4cab-8be4-d406a79b0bf5'></a>

will stable if p₁* > 0 and p₂* > 0. Thus, the necessary condition for the tumor growth is given by Eq. (23).

<a id='ce513c47-88e1-4da8-92b8-ee8fe33f3bbe'></a>

$$d < \frac{-(c_1 + c_3)\bar{d}_1 + 2a_1a_4}{d_2 + a_1} \quad (23)$$

<a id='b4eb9c78-de5d-4259-9e83-3c424e7780a9'></a>

<::A 2D line chart titled "Stability region for the case with the presence of immune response when a_4 = 0.8, c_1 = c_3 = 0.9, d_2 = 0.11 and d_1 = 0.1241". The x-axis is labeled "a1" and ranges from 0 to 1.0 in increments of 0.1. The y-axis is labeled "a" and ranges from 0 to 2.0 in increments of 0.2. A red curve starts near (0.1, 0) and curves upwards and to the right, ending near (1.0, 1.2). The area above the curve and to the left is labeled "IV", and the area below the curve and to the right is labeled "III". Figure 4 Stability region for the case with the presence of immune response when $a_4 = 0.8, c_1 = c_3 = 0.9, d_2 = 0.11$ and $\bar{d_1} = 0.1241$ : chart::>

<a id='772c584f-3440-449e-80c3-57d1759f77d2'></a>

<::transcription of the content: chart::>
Figure 5 Stability region for both cases. The chart shows a 2D plot with 'a1' on the x-axis ranging from 0 to 1, and 'd' on the y-axis ranging from 0 to 2. There are two curves. The upper blue curve is labeled "curve limits tumor growth region with no immune suppression". The lower red curve is labeled "curve limits tumor growth region with immune suppression".
<::>

<a id='00e5d604-ca29-4aea-a0cc-06f176256653'></a>

<::chart: A line graph titled "Figure 6 Numerical example for stable fixed point (0,0,k/d1) when a1 = 1 and d = 1.3 with initial condition TI = 1.3, TM = 1.2 and I = 0.9". The x-axis is labeled 't' and ranges from 0 to 60. The y-axis is labeled 'TI, TM and I' and ranges from 0 to 1.5. There are three lines plotted: a blue line labeled 'Ti', a green line labeled 'Tm', and a black line labeled 'I'. All three lines start at values above 1.0 on the y-axis at t=0, then decrease rapidly before leveling off to a stable value around 0.1 to 0.2 on the y-axis as t approaches 60. The black line (I) appears to stabilize at the highest value, followed by the blue line (Ti), and then the green line (Tm) at the lowest stable value.::>

<!-- PAGE BREAK -->

<a id='93e15ca4-c5f1-403e-b23b-bbb55ed0afc5'></a>

54

<a id='f68e3fa2-ef1e-4440-9f71-acc3dbde5133'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='5fe6ae49-09c7-4159-b302-40297bf97d61'></a>

<::chart
: Type: Line chart
: Title: (No title)
: X-axis: t, ranging from 0 to 60
: Y-axis: Ti, Tm and I, ranging from 0 to 1.5
: Legend:
: - Ti (blue line)
: - Tm (green line)
: - I (black line)
: Data points/trends:
: - The Ti line (blue) starts high, decreases to a minimum around t=10-15, then increases steadily.
: - The Tm line (green) starts high, decreases to a minimum around t=10-15, then increases steadily, staying below the Ti line.
: - The I line (black) starts high, decreases sharply to a low value around t=10-15, and then remains relatively flat at a low value.
Figure 7 Numerical example for unstable fixed point $(0,0,\frac{k}{d_1})$ when $a_1 = 1$ and $d = 1.15$ with initial condition $T_I = 1.3, T_M = 1.2$ and $I = 0.9$::>

<a id='2ffa15c8-a814-4d2b-bb7e-a3699a2b327e'></a>

From Figure 4, the region for tumor growth, where
(0,0, k/d1) is unstable is given by III and the region for
tumor decay where (0,0, k/d1) is stable is given by the

<a id='ced784c7-9172-471b-bbdc-a946c030fca2'></a>

complement IV. It can be seen in Figure 5 that the region of tumor growth without immune response for system (11) is larger than the region of tumor growth with the presence of immune response for system (17). Thus, system (17) is more stable compared to system (11). Various values were chosen from different regions to observe the solution of the system as presented in Figure 6 and Figure 7.

<a id='1e4d1fb5-da70-47ec-815b-8101cdbdd3f4'></a>

3.3 Tumor System with Single Drug
Now, consider the effect of single drug to the system

<a id='72a83957-2a33-4143-a3de-c4ee5e598ea0'></a>

dTI/dt = 2a4TM - (c1I + d2)TI - a1TI
dTM/dt = a1TI - d3TM - a4TM - c3TMI
          - k1(1 - e^(-k2u))TM
dI/dt = k + ρI(TI + TM)^n / (α + (TI + TM)^n) - c2ITI - c4TMI - d1I (24)
        - k3(1 - e^(-k4u))I
du/dt = -γu

<a id='d492d35c-961b-495d-b7af-1fb40195e297'></a>

One of the tumor free point for this system is
$(T_I, T_M, I, u) = (0,0, \frac{k}{d_1}, 0)$ with zero tumor and drug level.
This represents a tumor and drug free condition and
serves as the base for reference. The factorization form
of the auxiliary equation at this steady state yields Eq.
(24)

<a id='c62dce26-e0c3-46db-990a-bd59c0600e83'></a>

$$(- \gamma - \lambda)(-d_1 - \lambda)[(-c_1 \overline{d_1} - d_2 - a_1 - \lambda)(-d - c_3 \overline{d_1} - \lambda) - 2a_1 a_4] = 0 \quad (25)$$

<a id='9d62a9e8-4d58-4c81-b9fe-b3652cfc5af3'></a>

where $\overline{d_1} = \frac{k}{d_1}$. Clearly, two of the eigenvalues are $\lambda = -\gamma$ and $\lambda = -d_1$. The other eigenvalues are given as the solutions to the auxiliary equation

$\lambda^2 + [a_1 + d_2 + (c_1 + c_3)\overline{d_1} + d]\lambda$

$+ (a_1 + d_2 + c_1\overline{d_1})(d + c_3\overline{d_1}) - 2a_1a_4 = 0$ (26)

$\lambda^2 + p_1^{**}\lambda + p_2^{**} = 0$ (27)

where

<a id='87191907-af58-45eb-a48d-76a3cb8f037d'></a>

∴ p₁** = a₁ + d₂ + (c₁ + c₃)d₁ + d (28)
p₂** = (a₁ + d₂ + c₁d₁)(d + c₃d₁) - 2a₁a₄ (29)

<a id='f8b40bd8-8087-40b4-af3d-0029631253e7'></a>

The value of p₁** is always positive [15, 16, 22]. The value of p₂** can be negative or positive. According to the Routh-Hurwitz stability criteria the fixed point (0,0, k/d₁, 0) will be stable if p₁** > 0 and p₂** > 0. Thus the necessary condition for the tumor growth is given by Eq. (30)

<a id='7206c93f-158a-4892-8026-63a2a2be254e'></a>

d < -(c_1 + c_3)\bar{d}_1 + 2a_1a_4 / d_2 + a_1 (30)

<a id='97158870-a5b7-4a4f-b91f-a6911b487878'></a>

Notice that Eq. (30) is the same as Eq. (23). Hence, it has the same stability region as the previous system. It can be concluded that this system has the same stability characteristics as the tumor system without the application of drug.

<a id='f3e87769-b56d-468c-be66-f2367a9f1927'></a>

To observe the effect of the drug towards the
tumor population, numerical calculations were
carried out, with results plotted using three different
amounts of drug or initial value, u₀ which are u₀ =
0.05, u₀ = 0.1, and u₀ = 0.15. These values are chosen
from the range 0 ≤ u₀ ≤ 0.15 founded in [23].

<a id='bb6a67d8-4820-40bf-97fd-45c75dc584f6'></a>

<::chart: Line graph titled 'Numerical example for tumor system with the presence of immune response and drug'. The x-axis is labeled 't' and ranges from 0 to 60. The y-axis is labeled 'Ti, Tm, I, u' and ranges from 0 to 1.6. The graph displays four lines: Ti (blue), Tm (green), I (black), and u (red). The Ti line starts at approximately 1.3, decreases to a minimum around 0.2, and then increases to about 0.7. The Tm line starts at approximately 1.2, decreases to a minimum around 0.15, and then increases to about 0.5. The I line starts at approximately 0.9, decreases to about 0.1, and then remains relatively constant. The u line starts at approximately 0.05, decreases to near 0, and then remains near 0. Figure 8 Numerical example for tumor system with the presence of immune response and drug when a₁ = 1 and d = 1.15 with initial condition Tᵢ = 1.3, Tₘ = 1.2, I = 0.9 and u = 0.05::>

<!-- PAGE BREAK -->

<a id='b063b193-4cd5-48ca-8cf8-6af2879ae30f'></a>

55

<a id='02c042cc-33e9-4e9f-a399-23514ceb50a0'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='81ad3e4b-f391-4246-8e65-e260bdbde0f7'></a>

<::Line chart: The chart shows the numerical example for a tumor system with the presence of immune response and drug when a₁ = 1 and d = 1.15. The x-axis is labeled 't' and ranges from 0 to 60. The y-axis is labeled 'Ti, Tm, I, u' and ranges from 0 to 1.6. Four lines are plotted: a blue line for 'Ti', a green line for 'Tm', a black line for 'I', and a red line for 'u'. Initial conditions are T₁ = 1.3, T_M = 1.2, I = 0.9, and u = 0.1. All lines (Ti, Tm, I) start high and decrease rapidly before changing trajectory. The 'u' line starts low and decreases to near zero.::>

<a id='7e8ab819-55ff-4999-93b2-843a028d31ce'></a>

<::chart: A line chart titled "Numerical example for tumor system with the presence of immune response and drug when a₁ = 1 and d = 1.15 with initial condition Tᵢ = 1.3, Tₘ = 1.2, I = 0.9 and u = 0.15". The x-axis is labeled 't' and ranges from 0 to 60. The y-axis is labeled 'Ti, Tm, I, u' and ranges from 0 to 1.6. The chart shows four lines representing Ti, Tm, I, and u.
- The blue line represents 'Ti', starting at approximately 1.3, decreasing to a minimum around t=10-15, and then increasing to about 0.65 at t=60.
- The green line represents 'Tm', starting at approximately 1.2, decreasing to a minimum around t=10-15, and then increasing to about 0.5 at t=60.
- The black line represents 'I', starting at approximately 0.9, decreasing to a minimum around t=10-15, and then remaining relatively constant at about 0.15-0.2.
- The red line represents 'u', starting at approximately 0.15, quickly decreasing to near 0 by t=5, and remaining near 0 for the rest of the duration.
Figure 10 Numerical example for tumor system with the presence of immune response and drug when a₁ = 1 and d = 1.15 with initial condition Tᵢ = 1.3, Tₘ = 1.2, I = 0.9 and u = 0.15::>

<a id='d8bff1c2-6794-413c-9c94-9cd601446dd4'></a>

In Figure 8, the graph of the solution shows that the tumor population is growing when the amount of drug is u₀ = 0.05. Next, the initial amount of drug is increased to u₀ = 0.1, and the graph of the solution is shown in Figure 9.

<a id='121f7f31-83b8-4fb7-8304-bff140dcf541'></a>

From Figure 9, the tumor population is still growing
even when the amount of drug have been increased.
According to [23], the upper limit of reasonable drug
is 0.15. By taking this highest amount of drug as a final
selection, the graph of solution is then produced in
Figure 10 to see whether the population of tumor grow
or decay as time progresses.

<a id='bf16c07a-65b2-4b3a-939a-6cdcfc427b5b'></a>

It is obvious that the population of tumor still does not display any change with time. It can be concluded that the system maintains stability even though the maximum amount of drug have been delivered. However, the numerical values explain the differences between these figures.

<a id='1c3c0dc6-4291-40da-a509-5364e735bf17'></a>

These values were presented in the Table 1 while another comparison of numerical values between tumor system with immune response and drug system with u_0 = 0.15 have been tabulated in Table 2.

<a id='78f7bfd0-c422-40ae-97ed-da850e5d4660'></a>

Table 1 Comparison of numerical values for tumor on each
phase with respect to different amount of drug
<table id="6-1">
<tr><td id="6-2" rowspan="2">t</td><td id="6-3" colspan="2">u_0 = 0.05</td><td id="6-4" colspan="2">u_0 = 0.1</td><td id="6-5" colspan="2">u_0 = 0.15</td></tr>
<tr><td id="6-6">T₁</td><td id="6-7">Tₘ</td><td id="6-8">T₁</td><td id="6-9">Tₘ</td><td id="6-a">T_I</td><td id="6-b">T_M</td></tr>
<tr><td id="6-c">10</td><td id="6-d">0.2185</td><td id="6-e">0.1700</td><td id="6-f">0.2173</td><td id="6-g">0.1691</td><td id="6-h">0.2162</td><td id="6-i">0.1683</td></tr>
<tr><td id="6-j">20</td><td id="6-k">0.2562</td><td id="6-l">0.1994</td><td id="6-m">0.2550</td><td id="6-n">0.1984</td><td id="6-o">0.2539</td><td id="6-p">0.1976</td></tr>
<tr><td id="6-q">30</td><td id="6-r">0.3282</td><td id="6-s">0.2554</td><td id="6-t">0.3269</td><td id="6-u">0.2543</td><td id="6-v">0.3255</td><td id="6-w">0.2533</td></tr>
<tr><td id="6-x">40</td><td id="6-y">0.4131</td><td id="6-z">0.3214</td><td id="6-A">0.4115</td><td id="6-B">0.3202</td><td id="6-C">0.4100</td><td id="6-D">0.3190</td></tr>
<tr><td id="6-E">50</td><td id="6-F">0.5147</td><td id="6-G">0.4005</td><td id="6-H">0.5127</td><td id="6-I">0.3990</td><td id="6-J">0.5108</td><td id="6-K">0.3975</td></tr>
<tr><td id="6-L">60</td><td id="6-M">0.6511</td><td id="6-N">0.5067</td><td id="6-O">0.6483</td><td id="6-P">0.5045</td><td id="6-Q">0.6456</td><td id="6-R">0.5024</td></tr>
</table>
Table 2 Comparison of numerical values for tumor on each
phase for tumor system in the presence of immune response
and tumor system with the presence of immune response
and drug

<a id='0e959fbd-666a-4595-ba4e-b3ad018ebab9'></a>

<table id="6-S">
<tr><td id="6-T" rowspan="2">t</td><td id="6-U" colspan="2">without drug, immune is present</td><td id="6-V" colspan="2">with drug u₀ = 0.15, immune is present</td></tr>
<tr><td id="6-W">T_I</td><td id="6-X">T_M</td><td id="6-Y">T_I</td><td id="6-Z">T_M</td></tr>
<tr><td id="6-10">10</td><td id="6-11">0.2197</td><td id="6-12">0.1710</td><td id="6-13">0.2162</td><td id="6-14">0.1683</td></tr>
<tr><td id="6-15">20</td><td id="6-16">0.2574</td><td id="6-17">0.2003</td><td id="6-18">0.2539</td><td id="6-19">0.1976</td></tr>
<tr><td id="6-1a">30</td><td id="6-1b">0.3296</td><td id="6-1c">0.2565</td><td id="6-1d">0.3255</td><td id="6-1e">0.2533</td></tr>
<tr><td id="6-1f">40</td><td id="6-1g">0.4147</td><td id="6-1h">0.3277</td><td id="6-1i">0.4100</td><td id="6-1j">0.3190</td></tr>
<tr><td id="6-1k">50</td><td id="6-1l">0.5168</td><td id="6-1m">0.4021</td><td id="6-1n">0.5108</td><td id="6-1o">0.3975</td></tr>
<tr><td id="6-1p">60</td><td id="6-1q">0.6541</td><td id="6-1r">0.5090</td><td id="6-1s">0.6456</td><td id="6-1t">0.5024</td></tr>
</table>

<a id='6dfa539b-7053-4af7-aa49-30dd95f49695'></a>

From Table 2 above, the population of tumor cells at interphase and metaphase decrease at 1.27% and 1.53% respectively. This shows that the system with implementation of drug provide a better way for treatment in patients.

<a id='335cd0b7-02fd-4ec9-aebf-3974d4edaa17'></a>

## 4.0 CONCLUSION

This research considers three cases which are tumor system without immune response, tumor system with the presence of immune response and tumor system with single drug. Same procedure of stability analysis were done on each cases. For tumor system without immune response, the only steady state obtained is at origin. In this steady state, two regions of stability can be produced by fixing all parameters except for parameter a₁ and d. The regions are tumor growth region and tumor decay region, denoted by I and II respectively. By choosing a specific pair specific pair of value for parameter a1 and d in each region, the system is solved numerically using Fourth Order Runge Kutta Method. The result shows the population of tumor at interphase and metaphase increases when the values of parameter a₁ and d are fixed at the tumor growth region I. While the population of tumor decreases when the value of parameter a1 and d are fixed at the tumor decay region II. This implies that different values of parameter a₁ and d affect the

<!-- PAGE BREAK -->

<a id='17c68c7e-0a36-43f2-ac4b-3179b2ea2fe6'></a>

56

<a id='6c7ded12-51b9-4412-a269-6187dd0c9cfe'></a>

Mohd Rashid Admon & Normah Maan / Jurnal Teknologi (Sciences & Engineering) 79:5 (2017) 49-56

<a id='10474401-eae6-49b1-8d12-17778e6496a2'></a>

stability of the system. It is important to maintain the
value of a₁ and d so the system will maintain at tumor
decay region.

<a id='b5f0fc1c-3f95-45f6-b257-cb2052f8b642'></a>

Previous models were not realistic since the system did not include immune response. By adding the immune response, the model now involves the competition of three populations. This system has more than one steady states. However, this study only analyse the steady state in which tumor populations on both phases are zero. The stability region a₁ and d again is produced and then compared to the previous systems. From the stability region, the curve built in this system shows reduction in the tumor growth region compared to the previous system. It shows that this system is more stable since immune system naturally fights infections, including tumor. With the presence of immune system, numerical examples show that the population of tumor is decreased compared to the previous system. It can also be seen that the immune population maintain at a constant rate as time progresses. However, drug is needed to fight tumor since tumor growth persists even with the presence of immune response.

<a id='90241d2b-d0d2-46bc-9e17-99eda7d1f532'></a>

The drug effect is added into the tumor system with
immune response. There exists another steady states
but this research only looks at the steady state with
zero tumor population and drug with positive immune
level. From the stability analysis, the steady states have
the same stability characteristics as tumor system with
immune response. This means that if a certain amount
of drug is given to the patient, this system will exhibit
the same behaviour as the previous system. However,
the population of tumor is decreased by 1.27% at
interphase and 1.53% at metaphase. This implies that
combination of immune and drug provide a better
way to kill tumor cells.

<a id='e75cbad3-b3d2-4808-91b1-625ca78e76db'></a>

Several recommendations are presented as guides for future study. These include the effect of delay in the cell cycle may improve our findings. It seems more realistic since the tumor are trapped for a certain time in the mitosis for immune cells to kill it after being affected by drug. Besides, including quiescent phase could help us to understand either this phase will contribute or delay the progression of the population of tumor. A more detailed modelling involving immune systems also may provide many ideas. One such possibility is to include more types of immune cells to the model for analysis.

<a id='249ee623-fa10-4c20-8ce5-dd2403fe5ec0'></a>

Acknowledgement

The authors are thankful to Research Management
Centre (UTM) and Ministry of Higher Education
(MOHE), Malaysia for financial support through
research grants of vote 4F797 and vote 4L854.

<a id='aded209f-a118-4813-a85e-fda1b128ac77'></a>

References
[1] C. Garvey, T. McBride, L. Nevin, L. Peiperl, A. Ross, and P. Simpson. 2015. Bringing Access to the Full Spectrum of Cancer Research: A Call for Papers. PloS Med. 12(4): 1-3.
[2] A. Jemal, F. Bray, M. M. Center, J. Ferlay, E. Ward, and D. Forman. 2011. Global Cancer Statistics. Ca: A Cancer Journal for Clinicians. 61:69-90.
[3] N. Rezaei. 2014. Cancer Immunology: A Transitional Medicine Context. London: Springer.
[4] J. Mckay, and T. Schacher. 2009. The Chemotherapy Survival Guide: Everything You Need to Know to get through Treatment. Edisi Ke-3. New Harbinger.
[5] R. A. Lehne. 2013. Pharmacology for Nursing Care. Edisi Ke-5. Elsevier Health Science.
[6] R. K. Noyd, J. A. Krueger, and K. M. Hill. 2013. Biology: Organisms and Adaptations. Cengage Learning.
[7] R. P. Araujo, and D. L. S. McElwain. 2004. A History of the Study of Solid Tumor Growth: The Contribution of Mathematical Modelling. Bulletin of Mathematical Biology. 66: 10391-1091.
[8] J. Adam, and N. Bellomo. 2012. A Survey Models for Tumor-Immune System Dynamics. Springer Science and Business Media.
[9] V. A. Kuznetsov, A. Makalkin, M. A. Taylor, and S. Perelson. 1994. Nonlinear Dynamics of immunogenic Tumors. Bulletin of Mathematical Biology. 56: 295-321.
[10] J. A. Adam. 1996. Effects of Vascularization on Lymphocyte/Tumor Cell Dynamics: Qualitative Features. Mathematical and Computer Modelling. 23: 1-10.
[11] L. G. de Pillis, A. E. Radunskaya, and C. L. Wiseman. 2005. A Validated Mathematical Model of Cell-Mediated Immune Response to Tumor Growth. Cancer Research. 6: 235-252.
[12] R. T. Skeel, and S. N. Khleif. 2011. Handbook of Cancer Chemotherapy. Edisi Ke-8. Lippincott Williams and Wilkins.
[13] F. S. Borges, K. C. Larosz, H. P Ren, A. M. Batista, M. S. Baptista, R. L. Viana, S. R. Lopes, and C. Grebogi. 2014. Model for Tumor Growth with Treatment by Continous and Pulsed Chemotherapy. BioSystems. 116: 43-48.
[14] W. Liu, T. Hillen, and H. I. Freedman. 2007. A Mathematical Model for M-Phase Specific Chemotherapy including the G₀ Phase and Immunoresponse. Mathematical Biosciences and Engineering. 4: 239-259.
[15] M. Villasana, and A. E. Radunskaya. 2003. A Delay Differential Equation of Tumor Growth. Journal of Mathematical Biology. 47(3): 270-294.
[16] M. L. Workman, and L. A. LaCharity. 2015. Understanding Pharmacology: Essentials for Medication Safety. Elsevier Health Sciences.
[17] S. P. Ellner, and J. Guckenheimer, 2006. Dynamic Models in Biology. Princeton N.J. Oxford: Princeton University Press.
[18] L. Eldestein-Keshet. 1988. Mathematical Models in Biology. New York: Random House.
[19] S. P. Otto, and T. Day. 2007. A Biologist's Guide to Mathematical Modeling in Ecology and Evolution. Oxford: Princeton University Press.
[20] D. Gonze, M. Kaufman. 1961. Theory of Nonlinear Dynamical Systems. Biophysical Journal. 3: 1405-1415.
[21] K. G. Tay, S. L. Kek, and R. A. Kahar. 2012. A spreadsheet Solution of a System of Ordinary Differential Equations using the Fourth Order Runge Kutta Method. Spreasheets in Education (eJsiE). 5(2): 1-10
[22] M. Villasana, and G. Ochoa. 2004. Heuristic Design of Cancer Chemotherapy. IEE Transactions on Evolutionary Computation. 8: 513-521.
[23] G. Newbury. 2007. A Numerical Study of a Delay Differential Equation Model for Breast Cancer. M. S Thesis, Department of Mathematics, Virgina Polytechnic Institute and State.