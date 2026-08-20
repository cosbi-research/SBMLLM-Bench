<a id='deacd9ce-4c48-4407-8f69-7ca0840d031d'></a>

Adv Physiol Educ 30: 67–72, 2006; doi:10.1152/advan.00072.2005.

<a id='59669bc1-7da0-4e8f-88d0-fc4db1bcef36'></a>

Teaching With Classic Papers

<a id='f1c3494b-196d-45b5-a1b5-393bc57db359'></a>

Teaching from classic papers: Hill's model of muscle contraction

<a id='f9822090-474f-4ee1-a50c-ced07db6dabe'></a>

**Jeffrey W. Holmes**
*Department of Biomedical Engineering, Columbia University, New York, New York*
Submitted 20 October 2005; accepted in final form 5 February 2006

<a id='7d5c5cd5-7506-4b5b-ba56-32feced513bd'></a>

Holmes, Jeffrey W. Teaching from classic papers: Hill's model of muscle contraction. _Adv Physiol Educ_ 30: 67–72, 2006; doi:10.1152/ advan.00072.2005.—A. V. Hill's 1938 paper "The heat of shortening and the dynamic constants of muscle" is an enduring classic, present- ing detailed methods, meticulous experiments, and the model of muscle contraction that now bears Hill's name. Pairing a simulation based on Hill's model with a reading of his paper allows students to follow his thought process to discover key principles of muscle physiology and gain insight into how to develop quantitative models of physiological processes. In this article, the experience of the author using this approach in a graduate biomedical engineering course is outlined, along with suggestions for adapting this approach to other audiences.

<a id='169acdba-84d0-4dd6-a6b2-a62b2f04ea93'></a>

striated muscle; energetics; heat production; force-velocity; educa-
tion; modeling; simulation; MATLAB

<a id='a73c7029-6376-4217-b870-b88e4a38d8e5'></a>

ALL GRADUATE STUDENTS in our department are required to take Advanced Quantitative Physiology, a team-taught collection of month-long modules on mathematical modeling of various cellular and organ systems. As part of this course, I decided to teach a module on basic muscle physiology using two classic papers as readings: A. V. Hill's "The heat of shortening and the dynamic constants of muscle" (1) and A. F. Huxley's "Muscle structure and theories of contraction" (2). The objectives of this module are to 1) review the basic physiology of striated muscle contraction; 2) utilize two elegant, classic papers as examples of the thought processes involved in developing a model from physiological data; and 3) contrast the Hill and Huxley models as examples of more phenomenological and more mechanistic models, respectively, of the same physiological process.

<a id='1a77965f-71af-45cd-8feb-844b63b97c85'></a>

Taking a discovery learning approach, I ask students to use a simple simulation to conduct the experiments Hill described in his paper and then fit Hill's and Huxley's models to their simulated data. While fitting of Huxley's model to experimental data requires a reasonably strong background in mathematics, a simulation-based approach to understanding Hill's thought process and model could be employed in teaching physiology to a range of audiences. This article therefore presents my simple simulation and illustrates how this simulation can be used together with Hill's classic paper to help students with varying levels of mathematical expertise develop an inquiry-based understanding of Hill-type muscle models and related concepts in muscle physiology.

<a id='3d99eb4e-980e-4af2-92fb-fc674c0a6cad'></a>

_Approach_

This section outlines how I presented Hill's paper and related material in our Advanced Quantitative Physiology course, to give the reader some context. The specifics unavoidably depend heavily on the background of students in the

<a id='76f3bfe8-7ccb-4dff-963b-34847fb87790'></a>

--- 
Address for reprint requests and other correspondence: J. W. Holmes, Dept. 
of Biomedical Engineering, ET 351, Columbia Univ., MC 8904, 1210 Am- 
sterdam Ave., New York, NY 10027 (e-mail: jh553@columbia.edu).

<a id='c4406220-b1d3-4d6c-853d-c3283d91870f'></a>

course. Therefore, in *Teaching Points*, I tried to abstract more general advice for adapting this approach to undergraduate, graduate, and medical student audiences.

<a id='b4f0e930-ee6f-4788-a999-cfd6a2d2821f'></a>

Lectures. The muscle physiology module of our course includes one 3-h lecture each week for 3 wk. Although the biomedical engineering graduate students taking this course come from a variety of undergraduate majors, they are required to have taken an introductory physiology course or to take our own undergraduate physiology course concurrently. Our course therefore focuses more on modeling than on teaching the details of the physiology. I use the 3 h of lecture in the first week to review the basics of striated muscle physiology: structure and organization, excitation-contraction coupling, twitch and tetanic responses, definitions of preload and after-load, force-length and force-velocity relationships, energetics of contraction, and basic differences between cardiac and skeletal muscle. Students are assigned to read Hill's paper before the second 3-h session, which focuses on Hill's paper (1) and particularly on his model of muscle contraction. The third week is devoted to Huxley's 1957 paper (2), which will not be discussed further here for the reasons explained above.

<a id='7dfefd21-bbc7-4a93-8d6b-f45db9b3c8c3'></a>

Hill's paper. A. V. Hill's paper "The heat of shortening and the dynamic constants of muscle" (1) is a wonderful classic from a bygone era, 60 pages of detailed methods, experiments, and modeling representing years of work. In the first of three sections, Hill outlines the design and construction of his experimental system, with detailed circuit diagrams, the complete equations for a Wheatstone bridge amplifier, instructions on how to build a thermopile, and more. (For many students, it may be appropriate to skip or skim this section, but for an engineering audience, this is elegant and historically interesting work.) The second section presents the results of a series of experiments on mechanics and heat production in frog skeletal muscle. The final section presents the classic two-component Hill model with a contractile and an elastic element in series, develops the appropriate equations, and shows that this model explains many of the key experimental observations presented earlier in the paper. The only caution with regard to this paper is its length: while it is not too much to ask of students in a graduate course, for undergraduates or medical students selected excerpts will probably be more appropriate.

<a id='5806bb8e-8695-4162-86ce-df638341b10c'></a>

Simulation. My simple MATLAB simulation is provided in the APPENDIX.¹ This is by no means a research-grade simulation; it correctly solves for the forces predicted by Hill's model assuming length is prescribed as an input and a tetanizing stimulus is applied beginning at the start of the simulation, but does not simulate other situations in which Hill's model might be of interest, such as contractions against a constant afterload.

<a id='df6acde8-c6b6-4864-8537-9ee4237fe3a9'></a>

¹ Three MATLAB files containing the simulation, demonstrations of its use,
and graphical interface for creating length inputs are available from the
*Advances in Physiology* website or from the author's website at http://
www.columbia.edu/~jh553/protocols/programs.html.

<a id='05eb70f9-bb5f-4831-b248-4772538bd6f1'></a>

1043-4046/06 $8.00 Copyright © 2006 The American Physiological Society

<a id='08965389-5870-4eaf-993c-21687991a9fd'></a>

67

<a id='25455623-6977-45c1-9a7b-1065c183a95e'></a>

Downloaded from journals.physiology.org/journal/advances (087.121.037.170) on December 22, 2025.

<!-- PAGE BREAK -->

<a id='361d1505-8015-4445-b892-688b48e00628'></a>

Teaching With Classic Papers

<a id='c6fb6ef9-47ef-4eff-9d83-7ced02167329'></a>

68

<a id='cae13de4-ab49-41c1-a7fa-913d94370eaf'></a>

By choosing an arbitrary but reasonable rate of baseline heat liberation, it also produces heat tracings consistent with Hill's figures from the 1938 paper. It is written so that with minor modifications it could be transferred to any programming language: rather than using MATLAB's built-in equation solvers, this simulation solves Hill's model by simply stepping through the length and time inputs and using the calculated rate of force rise at each step to project the force at the next. Many of our students have never written a program like this to directly solve a simple set of equations; for them, one of the secondary goals of this module is to write their own version of my simulation. For a general audience, the only important point is that this method only works well for a sufficiently large number of steps. All of the results shown here were obtained by breaking a period of 5 s into 1,000 steps (Table 1).

<a id='890b5fc4-93b5-41cb-81a5-0a839462df54'></a>

In lectures, I introduce the model by demonstrating how to use the simulation to predict the response of Hill's model to isometric tetanus (Table 1 and Fig. 1A) and a step change in length (Fig. 1B). We graph and discuss the results as a way of exploring the implications of two features of Hill's model: 1) force is the same in the contractile and elastic elements because they are in series and 2) force in the elastic element is proportional to stretch. In equations,

<a id='34108e03-983c-4b81-aa18-ad2f9505214a'></a>

L = Lce + Lse                                 (1A)
P = Pce + Pse = α[Lse - Lse(0)]               (1B)

<a id='6af4ea38-f94e-4da7-9893-57e5d28cb4d8'></a>

where L is muscle length, L_ce and L_se are the lengths of the
contractile and series elastic elements, P is muscle force, and α
is the spring constant for the series elastic element. During
isometric contraction, total length remains constant and the
contractile element can only shorten by stretching the elastic
element; to stretch the elastic element further and further, the
contractile element must generate more and more force (in Fig.
1A, as L_ce decreases and L_se increases, P rises).
If the activated model is then subjected to a sudden change
in length, the time derivatives of Eq. 1, A and B, are of interest:

<a id='69d995dd-71be-4974-97b9-16850242d433'></a>

dL/dt = dL_ce/dt + dL_se/dt = v_ce + dL_se/dt (2A)
dP/dt = \alpha dL_se/dt (2B)

<a id='e74ac657-7a50-4fd9-837b-275a6a552331'></a>

where _v_ce is the shortening velocity of the contractile element.
For a sudden step decrease in length (_dL_/_dt_ < 0), the fact that

<a id='a72e7163-116b-4071-a350-c40b9bfda4a6'></a>

Table 1. Input and output arrays for simulation
of isometric tetanus
<table id="1-1">
<tr><td id="1-2"></td><td id="1-3" colspan="2">Inputs</td><td id="1-4" colspan="4">Outputs</td></tr>
<tr><td id="1-5">Row</td><td id="1-6">L</td><td id="1-7">t</td><td id="1-8">P</td><td id="1-9">H</td><td id="1-a">Lse</td><td id="1-b">Lce</td></tr>
<tr><td id="1-c">1</td><td id="1-d">1.000</td><td id="1-e">0.000</td><td id="1-f">-0.99</td><td id="1-g">0.13</td><td id="1-h">0.300</td><td id="1-i">0.700</td></tr>
<tr><td id="1-j">2</td><td id="1-k">1.000</td><td id="1-l">0.005</td><td id="1-m">8.93</td><td id="1-n">0.16</td><td id="1-o">0.306</td><td id="1-p">0.694</td></tr>
<tr><td id="1-q">3</td><td id="1-r">1.000</td><td id="1-s">0.010</td><td id="1-t">14.89</td><td id="1-u">0.46</td><td id="1-v">0.311</td><td id="1-w">0.689</td></tr>
<tr><td id="1-x">4</td><td id="1-y">1.000</td><td id="1-z">0.015</td><td id="1-A">21.62</td><td id="1-B">0.58</td><td id="1-C">0.315</td><td id="1-D">0.685</td></tr>
<tr><td id="1-E">5</td><td id="1-F">1.000</td><td id="1-G">0.020</td><td id="1-H">27.75</td><td id="1-I">0.83</td><td id="1-J">0.318</td><td id="1-K">0.682</td></tr>
<tr><td id="1-L">6</td><td id="1-M">1.000</td><td id="1-N">0.025</td><td id="1-O">30.73</td><td id="1-P">0.91</td><td id="1-Q">0.321</td><td id="1-R">0.679</td></tr>
<tr><td id="1-S">7</td><td id="1-T">1.000</td><td id="1-U">0.030</td><td id="1-V">34.25</td><td id="1-W">0.93</td><td id="1-X">0.324</td><td id="1-Y">0.676</td></tr>
<tr><td id="1-Z">1,000</td><td id="1-10">1.000</td><td id="1-11">5.000</td><td id="1-12">145.99</td><td id="1-13">11.31</td><td id="1-14">0.400</td><td id="1-15">0.600</td></tr>
</table>
L, length (fraction of muscle length); t, time (in ms); P, force (in mN/mm²);
H, heat/volume (in mN/mm²); Lce and Lse, lengths of the contractile and series
elastic elements, respectively.

<a id='92ea00fc-c966-4339-a073-a89230fa5712'></a>

<::Figure 1: Two line charts showing force (P) and length (L) responses of the Hill model from a MATLAB simulation. The x-axis for both charts is 'Time (s)' from 0 to 5. The left y-axis for both charts is 'Length (muscle length)' from 0.0 to 1.0. The right y-axis for both charts is 'Force (mN/mm²)' from 0 to 200. The charts display four lines: L (length), P (force), Lce (contractile element length), and Lse (series elastic element length). A: Simulation of isometric tetanus. The 'L' line (muscle length) is constant at 1.0. The 'P' line (force) starts at 0 and gradually increases to approximately 150 mN/mm² by 1.5 seconds, then remains relatively constant. The 'Lce' line (contractile element length) starts around 0.68 and gradually decreases to approximately 0.61. The 'Lse' line (series elastic element length) starts at 0 and gradually increases to approximately 0.39. B: Simulation of a step decrease in length imposed on a tetanized muscle. The 'L' line (muscle length) is constant at 1.0 until 2 seconds, then drops sharply to approximately 0.9 and remains constant. The 'P' line (force) starts at 0, gradually increases to approximately 150 mN/mm² by 2 seconds, then sharply drops to approximately 75 mN/mm² at 2 seconds, and then gradually increases back to approximately 150 mN/mm². The 'Lce' line (contractile element length) starts around 0.68, gradually decreases to approximately 0.61 by 2 seconds, then sharply drops to approximately 0.58, and then gradually decreases further to approximately 0.55. The 'Lse' line (series elastic element length) starts at 0, gradually increases to approximately 0.39 by 2 seconds, then sharply drops to approximately 0.33, and then gradually increases back to approximately 0.39.: chart::>Fig. 1. Force (P) and length (L) responses of the Hill model as reflected in the output of the MATLAB simulation presented in the APPENDIX. A: simulation of isometric tetanus. When length is held constant, force rises gradually as the contractile element shortens (where Lce is the contractile element length) and stretches the series elastic element (where Lse is the series elastic element length). B: simulation of a step decrease in length imposed on a tetanized muscle. The series elastic element absorbs the initial drop in length, and then force recovers as the series element is gradually restretched by the contractile element.

<a id='da45da62-a826-424e-8220-09c816cdf6be'></a>

# DISCOVERY LEARNING QUESTIONS

1. Draw the expected length-vs.-time curves for the contractile and series elastic elements in Hill's model during the development of an isometric tetanus. Use the simulation to obtain the actual responses and comment on the agreement or disagreement with your prediction.
2. Repeat the cycle of prediction, simulation, and comparison for a step release from isometric tetanus and for a constant-velocity release from isometric tetanus.

<a id='73173184-b63e-402e-82c1-4a840d7f01bd'></a>

the contractile element has a limited maximal shortening ve-
locity means that the drop is absorbed primarily by the elastic
element, with a resulting immediate drop in force; force then
recovers as the contractile element restretches the elastic ele-
ment (Fig. 1B).

<a id='34187575-c95a-40c8-8412-a3a1b3b65eaf'></a>

The remainder of the student work with the simulation is
discovery learning, where students work with the simulation to
discover for themselves some of the basic principles identified
by Hill that motivated his model. The students work through a
homework assignment that asks them to follow in Hill's

<a id='a6f00149-68cd-4988-a867-6631720ee76d'></a>

*Advances in Physiology Education* • VOL 30 • JUNE 2006

<a id='61972a59-c4d7-46a4-90a8-5295a9257f0f'></a>

Downloaded from journals.physiology.org/journal/advances (087.121.037.170) on December 22, 2025.

<!-- PAGE BREAK -->

<a id='5d60d9e8-e7f5-41b3-921d-a1ec6b3a9bd0'></a>

Teaching With Classic Papers

<a id='920dcaba-77a4-460f-a669-9a9948d08191'></a>

69

<a id='06b6a73e-93da-49fd-b856-a2e39e949a07'></a>

footsteps to perform simulated versions of his experiments and
determine the Hill constants _a_ and _b_ as well as the spring
constant for the series elastic element _α_, the maximum velocity
of unloaded shortening _v_max, and the maximal isometric tetanic
force P₀. Some aspects of this homework are described below;
the entire homework and solution set are available from the
author on request.

<a id='e030184c-984c-4569-b79f-67d0b9e75c93'></a>

Homework problems. First, I ask the students to simulate releases of different rates and durations from an initial fully developed tetanus and explore how the rate and amount of heat liberation depend on the rate and distance of shortening. Through simulations with an appropriate choice of length inputs, students can easily verify Hill's critical finding: that the amount of excess heat liberated as a result of shortening depends only on the amount shortened, not on the rate [Fig. 2, compare with Fig. 7B in Hill's paper (1)].

<a id='a33986ba-7e84-456f-adb5-02f483ab2c5d'></a>

Next, I ask students to design and conduct appropriate
experiments to determine the constants Hill termed a and b in
his paper. Hill defined constant a as the slope of the relation-
ship between the amount of shortening x and the amount of
associated excess heat (Hill's Fig. 10E):

<a id='f7fff6f4-0d0c-4389-ba77-b3d2eeafa93e'></a>

Shortening heat = ax (3)

<a id='0d427c90-bf35-42e9-bfd4-87bcb803fdba'></a>

Students can easily repeat his approach to obtain a value for _a_ (Fig. 3). Next, Hill considered the excess energy released during shortening. The mechanical work performed is force times distance; the additional energy released beyond that of an isometric contraction is therefore the mechanical work plus the extra heat liberated:

<a id='7ecac315-6264-48d4-b5cc-db619544425e'></a>

Excess energy liberated = Px + ax = (P + a)x (4)

<a id='fd0b2e07-4686-42a6-9cce-78b1e4500862'></a>

Hill found experimentally that if he plotted the rate of excess
energy liberation for muscles shortening at a constant load (P
and a constant) against the amount of load, he obtained a
straight line; he defined constant b as the slope of the relation-
ship between the excess energy rate and steady-state force P
(Hill's Fig. 11):

<a id='1ccd1833-4e07-4418-bf64-f66b345bf9f9'></a>

Excess energy rate = (P + a)dx/dt = (P + a)v
= -bP + c (5)

<a id='028300a0-5898-47dc-a63f-1aafbd4f0614'></a>

With the use of data from the same set of simulations they used to obtain a, students can repeat this part of his analysis as well (Fig. 3C). Equation 5 contains an extra constant, c, which represents the y-intercept of the plot of (P + a)v against P (Fig. 3C). Because the excess heat of shortening must be zero when there is no shortening (during an isometric contraction), c must equal bP0, where P0 is the force generated by an isometric contraction. Incorporating this fact and rearranging the equations yields the famous Hill equation, presented as Eqs. 1 and 2 in his paper:

<a id='e02ad62a-46c3-44d0-ad8e-c9595e1dfe02'></a>

(P + a)v = -b(P - Po) or
(P + a)(v + b) = (Po + a) = constant (6)

<a id='336045c0-567c-4667-96c7-c4dc06402210'></a>

This last equation describes the classic hyperbolic force-veloc-
ity relationship of muscle, but was discovered as described
here based on considerations of energy liberation.

<a id='081f5503-20d1-4709-aa0a-4dfb358aef26'></a>

To conduct these simulations, students must wrestle with
some of the same experimental design issues that would face

<a id='80161286-ddf7-4e7b-8fd6-120b2abe2335'></a>

<::Fig. 2. Heat responses of the Hill model as reflected in the output of the MATLAB simulation presented in the APPENDIX.

A: A line graph with 'Time (s)' on the x-axis (0 to 5) and 'Length (muscle lengths)' on the y-axis (0.0 to 1.2). A horizontal black line is at Length 1.0 from Time 0 to 2. At Time 2, five lines descend from Length 1.0 with varying slopes, representing different velocities of shortening. These lines then flatten out at different lengths, with the lowest reaching Length 0.5. A gray horizontal line is labeled 'isometric' at Length 1.0.

B: A line graph with 'Time (s)' on the x-axis (0 to 5) and 'Heat/Volume (mN/mm²)' on the y-axis (0 to 35). Several curves show heat release over time. All curves start near 0 at Time 0 and gradually increase until Time 2. At Time 2, five black curves show a sharp increase in heat, then level off at different maximum values, ranging from approximately 15 to 30 mN/mm². A gray curve, labeled 'isometric', shows a continuous gradual increase in heat, reaching about 10 mN/mm² at Time 5.

A: length inputs to the model impose a series of releases from isometric tetanus with the same amount of shortening but different velocities. B: amount of heat released in excess of that for an isometric tetanus depends on the distance shortened but not on shortening velocity v [compare with Hill's Fig. 7B (1)].: chart::>
DISCOVERY LEARNING QUESTIONS
1. Simulate releases of different rates and durations from an initial fully developed tetanus and explore how the rate and amount of heat liberation depend on the rate and distance of shortening. Read part II, section a (p. 157–161), of Dr. Hill's paper (1) and compare your findings with his conclusions.

<a id='4ebaff1d-5a6b-4b2f-96c3-c7d64f50bd1f'></a>

them if it were possible to have them perform these experi-
ments in the laboratory. For example, to obtain the most
accurate value for constant _b_, it is best to obtain data at the
widest possible range of shortening velocities and associated
forces. However, very rapid shortening velocities can only be
maintained briefly before the muscle length reaches unreason-
able values and the simulation breaks down, and over such
short times the force may not reach a true steady-state value
associated with the imposed velocity. In addition, the simula-
tion as written adds some Gaussian noise to the computed force
and heat outputs, so that students must average multiple trials
or come up with other strategies to handle the presence of
noise.

<a id='4fdb5329-fec4-4b5a-9779-ed98fdf25ae0'></a>

Advances in Physiology Education • VOL 30 • JUNE 2006
Downloaded from journals.physiology.org/journal/advances (087.121.037.170) on December 22, 2025.

<!-- PAGE BREAK -->

<a id='8576cdf8-e8bf-4745-bdff-2f144c7b7d32'></a>

Teaching With Classic Papers

<a id='3c5ba629-2e71-4a2a-bc44-1b44db63bdec'></a>

70
<::chart: Fig. 3. Fitting Hill's model to simulated data. A: by simulating releases of varying distances and velocities from isometric tetanus, a range of length-excess heat and force-velocity pairs can be generated for analysis. The chart shows Heat/Volume (mN/mm²) on the y-axis and Time (s) on the x-axis. Multiple curves rise over time, indicating heat production.::>
<::chart: B: excess heat is linearly related to the distance shortened, with slope equal to Hill constant a. The chart shows Excess Heat/Volume (mN/mm²) on the y-axis and Distance (muscle lengths) on the x-axis. Data points form a straight line with an upward slope. An annotation reads "a = 37.35".::>
<::chart: C: the energy rate, (P + a)v, is linearly related to steady-state force P with a negative slope equal to Hill constant b. The chart shows Energy rate/Volume (mN/mm².s) on the y-axis and Force (mN/mm²) on the x-axis. Data points form a straight line with a downward slope. An annotation reads "b = 0.316".::>
<::chart: D: very similar values of Hill constants may also be obtained by directly fitting force-velocity data as shown. k is a constant. The chart shows Force (mN/mm²) on the y-axis and Velocity (length/sec) on the x-axis. Data points form a hyperbolic curve with a downward trend. Annotations read "a = 37.49", "b = 0.317", "k = 47.14".::>
DISCOVERY LEARNING QUESTIONS

<a id='abb35623-3834-4c98-b7ff-e599c288cbfa'></a>

1. With the use of the simulation provided, perform appropriate releases from isometric tetanus and determine Hill constant a as the slope of the relationship between the amount of shortening and the associated excess heat, as in Hill's Fig. 10E (1).
2. Next, use the same data to determine Hill constant b from the slope of the relationship between steady-state force P and the energy rate, (P + a)v, as in Hill's Fig. 11 (1).
3. Next, try an alternate approach to determine the Hill constants by performing a series of constant velocity releases from tetanus and fitting the resulting force-velocity data to an appropriate equation.
4. Compare the values for the constants you obtained using the two methods outlined above. Propose an explanation for any differences.

<a id='eea31817-f680-40cc-bc37-4e886385a794'></a>

While there is teaching value in having students repeat Hill's thought process and derive the Hill constants as he originally described, Hill constants are rarely obtained in this way today. It is much more common to simply fit force-velocity data to obtain these constants. Therefore, I also ask students to simulate constant-velocity releases at a number of different velocities, find the steady-state force associated with each velocity, and fit the force-velocity data to the equation (P + a)(v + b) = k, where k is a constant (Fig. 3D). Because most simple graphing programs do not have this equation as a built-in feature, this provides an opportunity to discuss curve fitting approaches. In this case, three or more force-velocity data pairs can be used to construct a system of equations that is linear in the constants a, b, and (k – a × b), easily converted to matrix form and solved in MATLAB.

<a id='8db942b9-6246-4e8d-945e-3feb7d1a1dc4'></a>

For the remainder of the homework, students write and work with their own implementation of Hill's equations. Because of this, for the earlier parts of the homework, they do not have access to my original MATLAB program but only to an executable version created with the MATLAB command "pcode." This has the added advantage that the Hill constants in the model are unknowns from the students' point of view. I can vary them from year to year and compare the values determined by the students with the true values in the simula-

<a id='cd6a4d49-07c8-477f-986e-34c97f58df1a'></a>

tion to help me assess their work. Once students write their own simulations using constants from Hill's paper and verify that their simulations give appropriate responses for the devel-opment of an isometric tetanus, recovery from a step decrease in length, and constant-velocity shortening, I ask them to modify Hill's model and their implementation to improve agreement with some experimental data that is not well ex-plained by Hill's original model. There are several possible challenges of this nature that can be assigned. For example, Jewell and Wilkie (3) showed that force recovery after a step decrease in length follows a different time course than pre-dicted by Hill's model, and students can adjust the model to improve the fit by modeling the series elastic element as nonlinear rather than linear.

<a id='317780ce-eab4-4d15-87c6-1d093693f03e'></a>

_Teaching Points_

The approach outlined in the previous section was developed for a graduate biomedical engineering course and may not be appropriate for courses with a different target audience. On the basis of my experience teaching physiology to undergraduate biology students, graduate biomedical engineering students, and medical students, I have tried to suggest ideas that may be more appropriate for each of these audiences in the text below

<a id='d8bcfc07-8e16-4f76-bb59-2ab9de2463f8'></a>

_Advances in Physiology Education_ • VOL 30 • JUNE 2006

<a id='fb27456e-d632-423a-968c-3595e5ccc443'></a>

Downloaded from journals.physiology.org/journal/advances (087.121.037.170) on December 22, 2025.

<!-- PAGE BREAK -->

<a id='26b603af-8223-4869-9cf7-2c2421bba5eb'></a>

Teaching With Classic Papers

<a id='c29d5ec3-0a04-4dbe-880d-7f68c4b4bf3c'></a>

71

<a id='78ae5e40-4cf1-4b27-aa25-868a6b9a5670'></a>

and in the DISCOVERY LEARNING QUESTIONS that accompany each
figure. The degree of difficulty of these exercises increases
from Fig. 1 to Fig. 3, and the figures themselves serve as the
instructor "answer key" for the questions.

<a id='09ea8568-102e-4c2e-b2eb-6e4674f93fd7'></a>

Medical physiology courses. Of the properties explored by Hill in his paper, medical students are typically interested primarily in the force-velocity relationship. The simulation introduced here could be used as an exploratory tool for students to simulate releases from tetanus at different velocities, plot the resulting steady-state forces against the prescribed release velocities, and thereby "discover" the force-velocity relationship. However, Hill's model in itself does not provide insight into the mechanisms that underlie the force-velocity relationship; this relationship is specified for the contractile element in his model, based on his empirical finding that the energy rate (P + a)v is linearly related to force P. Because the density of medical school physiology courses also generally discourages reference to primary sources, the approach outlined here will probably be of least interest to those teaching medical physiology.

<a id='55e47ce9-e405-434e-a123-0e3ead3c5904'></a>

Undergraduate and graduate physiology courses. Once a physiology course begins to consider energetics and heat produc- tion in muscle in addition to force-length and force-velocity relationships, Hill's model and paper are of much more impor- tance and interest. In this case, the interaction between the con- tractile and series elastic elements in Hill's model must be under- stood, as must the concept that there are two types of work performed by the contractile element during variously loaded contractions: external work (Px) of the type familiar from physics and internal work (ax), which appears as excess heat production.

<a id='73a81664-6869-4c95-a821-5a710ca17a87'></a>

In these situations, a number of uses of the simulation
presented here may be appropriate. Before ever reading Hill's
paper or learning about his model, students might be asked to
prescribe a range of inputs to the simulation, explore the force
and heat responses, and propose possible explanations for the
results they see. Students may well articulate that the force
response to a step decrease in length has an immediate com-
ponent and a slower recovery component or discover on their
own that shortening produces an extra amount of heat that
depends only on the distance shortened. Each of these insights
and the effort to explain them will help prepare students to
better understand Hill's model once it is introduced.

<a id='e4bbad5f-2333-45c9-b4f8-e79957560fc2'></a>

After Hill's model has been introduced, a series of simulations focusing on helping students understand the series interaction between the elements may be appropriate. Suggested exercises are provided under the heading DISCOVERY LEARNING QUESTIONS in Fig. 1. Asking students to first predict the response of the elastic and contractile elements for the cases of isometric force development, a step decrease in muscle length, and constant velocity shortening and then simulate these cases and compare the outputs Lce and Lse to their predictions will force them to think carefully about how the two elements interact. Students usually find the concept that the contractile element stretches the series element during isometric contraction relatively easy to grasp. However, they often guess that the two elements will absorb a step change in length equally, not anticipating the fact that the maximal shortening velocity of the contractile element limits its response. During various shortening protocols, they often predict changes in force and series elastic element length that do not correspond, but one or two failures of this type can be used to remind them of the behavior of simple

<a id='e3a081e6-7a20-453c-abf7-2898e45f76e1'></a>

springs (familiar from physics) and cement the concept that force
and elastic element length must change in parallel.

<a id='a0289b8e-b115-4305-bf98-f0412ac6e7e7'></a>

Both undergraduate and graduate students can easily dis-cover for themselves Hill's critical observations that the amount of excess heat associated with shortening depends only on the distance shortened (see suggested DISCOVERY LEARNING QUESTIONS in Fig. 2) and that the rate of excess energy liberation is linearly proportional to force (Fig. 3C). Depending on the intended degree of difficulty, these exercises can be combined with a derivation of Hill's equation in lecture or with reading of the derivation in Hill's paper (as outlined in Homework problems) to recreate Hill's thought process in originally dis-covering this equation.

<a id='e71b4dee-3339-4d6f-9b59-a0660a262243'></a>

Finally, at the graduate level, I consider the additional effort to repeat Hill's procedure for fitting his model to data (see suggested DISCOVERY LEARNING QUESTIONS in Fig. 3) very valuable. Fitting a model to data is a critical skill for all science and engineering graduate students, and they should be aware of the range of methods available to them for doing so, from simple linear regression to more complicated nonlinear fits. Because the simulation as written adds random (Gaussian) noise to the heat and force outputs, students will find that their values for a and b will not match the "true" values incorporated in the simulation. They can be asked to generate and test several ideas for reducing the impact of noise on their estimates. Typically, in a first attempt, they will have used data from just three or four simulated releases, and they will have determined the "excess heat" by comparing individual heat values at a single time point (e.g., the final heat value at 5 s). Many of them realize that multiple trials are usual in experimentation and may propose to overcome the effects of noise by rerunning the same simulation several times and averaging the values they obtain for a and b. They may not realize that simulating more different releases (as shown in Fig. 3) rather than repetitions of the same releases may be a more efficient approach. In actual experiments, time, expense, or other practical limits may restrict the number of trials that can be performed, making it essential to extract the best possible information from each trial. However, students almost never propose linear fits to the individual heat tracings to reduce noise in the estimate of excess shortening heat for each release; this, in fact, was the approach Hill used (see Fig. 10 in Hill's paper).

<a id='d143fd62-6144-455c-90c9-5911cdf08896'></a>

There are two aspects of the approach described here that may appear particularly daunting to physiology students and instructors. First, particularly in undergraduate courses, students may be discouraged by the effort required to become familiar enough with MATLAB to construct appropriate inputs to my simulation and graph the outputs. We want our engineering students to become proficient with MATLAB and modules such as this provide opportunities for practice. Understanding that this may be an unwanted distraction in a physiology course, I have written a simple graphical interface that allows students to choose from three example length inputs (isometric, step change in length, or constant velocity release) or to outline their own length inputs by simply clicking with the mouse on a length-time plot. The selected length input is then passed to my simulation, and the results are graphed automatically. Students can use the MATLAB Array Editor window to view the resulting input or output arrays and copy values for graphing or further analysis. Instructors who choose to use this option should be able get students up and running

<a id='0e3b5b80-b0f1-4f18-b091-af85fcc54f8d'></a>

_Advances in Physiology Education_ • VOL 30 • JUNE 2006

<a id='e3b5a41d-d0dc-4bc4-a24f-ddf3ab88e264'></a>

Downloaded from journals.physiology.org/journal/advances (087.121.037.170) on December 22, 2025.

<!-- PAGE BREAK -->

<a id='b354d2ca-3fcf-48f3-a25f-8868a9b1fc13'></a>

Teaching With Classic Papers

<a id='1f63cf72-e63b-4550-9268-6426ffabceef'></a>

72

<a id='1f162328-e8f5-4ba0-bc29-060fb37e7dcc'></a>

with the simulation after a 10- to 15-min introduction to the MATLAB environment and the graphical interface.

<a id='845186ce-cc08-4077-9099-bbfbc4b4bd93'></a>

The second potentially intimidating aspect of the exercise as employed in our course is asking students to implement Hill's model themselves. It is tempting to dismiss this as too difficult for students who do not have strong math backgrounds, and I did not focus on this aspect in outlining teaching points here. However, I contend that it is exactly these students who most need to overcome their fear of generating and using models as needed. A number of software packages (including Simulink, available as a package with MATLAB) now allow students to construct a model simply by connecting elements such as a differentiator or an integrator graphically, and this exercise can be liberating for students who believed themselves incapable of implementing models involving differential equations. In fact, even writing a program to solve a simple differential equation is often easier than integrating that equation analytically, as Hill does in his paper, and learning how to solve simple equations computationally could provide graduate physiology students with a new and very powerful tool.

<a id='46347e55-19fc-469c-98e3-7286ab8b7f6d'></a>

Undergraduate and graduate engineering/mathematics courses. The approach outlined in this article is by design most appropriate for engineering audiences. Undergraduates should be comfortable using simulations to explore features of a model as outlined above and implementing a simple model such as this graphically. Graduate students should be facile with a range of implementation options, with fitting models to data and with modifying simple models to improve agreement with data as discussed previously.

<a id='1634841b-a6cb-4ecd-8e6f-7b03d3e556af'></a>

Conclusions

A. V. Hill's classic paper "The heat of shortening and the
dynamic constants of muscle" (1) is a wonderful example not
only of careful experimentation but also of the thought process
required to generate a model from experimental observations.
I attempted to engage students in thinking about and under-
standing relevant aspects of muscle physiology through a
simple simulation that allows them to reproduce his observa-
tions and parts of his thought process. This approach is out-
lined here in the hope that it will be of use to others who teach
muscle physiology to a range of audiences.

<a id='82bb8c9a-578d-453b-bcc5-3900a764e468'></a>

APPENDIX: SIMULATED RESPONSE OF HILL MODEL TO PRESCRIBED LENGTH INPUT

<a id='f987844b-2fa9-4a97-884b-8303e808148c'></a>

function [P,H,Lse,Lce] = hill(L,t)
% Function hill accepts length & time inputs L(n), t(n) and
% computes following outputs assuming tetanizing
% impulse starts at first time point:
% P(n) - force
% H(n) - heat

<a id='f13b790c-0489-462a-b88b-16d3c6e06aeb'></a>

% Lse(n) - series elastic element length
% Lce(n) - contractile element length
% Inputs and outputs are column vectors that must all
% have same length n.

<a id='5c115b21-f063-4f77-b381-a3693c69b13c'></a>

% Establish constants (Hill 1938 p.174, mean data at
% 0C: a = 399*0.098, b = 0.331)
% Note that because Hill reports force with units of
% force/unit area and lengths in unitless fractions of
% muscle length, force, and heat all have units of
% force/area.

<a id='de937944-4443-4546-9e9d-3629bad2ea1a'></a>

a = (380* .098);
b = 0.325;
P0 = a/0.257;
vm = P0*b/a;
alpha = P0/0.1;
Lse0 = 0.3;
k = a/25;
% units mN/mm2
% units lengths/sec
% units mN/mm2
% units lengths/sec
% units mN/mm2
% assume Lse initially 30% of length
% set arbitrary baseline heat rate

<a id='360a3369-161b-4d86-a524-c95dc400c07b'></a>

% Initialize arrays
Lse = [repmat(Lse0,length(t),1)];
Lce = [repmat((1-Lse0),length(t),1)];
H = [repmat(0,length(t),1)];
P = [repmat(0,length(t),1)];

<a id='ed3074b5-d96d-41dc-af96-8b6a2bef8fc8'></a>

% General solver for prescribed length input to Hill model
for j = 1:(length(t) - 1)
Lse(j) = Lse0 + P(j)/alpha; Lce(j) = L(j)-Lse(j);
dt = (t(j + 1)-t(j));
dL = (L(j + 1)-L(j));
dP = alpha*((dL/dt) + b*((P0-P(j))/(a + P(j))))*dt;
P(j + 1) = P(j) + dP;
H(j + 1) = H(j) + (k + a*b*((P0-P(j))/(a + P(j))))*dt;
end
Lse(j + 1) = Lse0 + P(j + 1)/alpha;
Lce(j + 1) = L(j + 1)-Lse(j + 1);

<a id='6c72f21b-75a7-460c-970a-4c35a45cd5f5'></a>

% Add some noise if desired for more realistic output
H = H + (k/10)*(randn(1000,1)-0.5);
P = P + (P0/100)*(randn(1000,1)-0.5);

<a id='8dc63b2f-9b73-42fa-8986-8c8170e933c1'></a>

## ACKNOWLEDGMENTS
The author acknowledges past mentors and teachers of cardiac physiology for inspiration and students from the Advanced Quantitative Physiology course at Columbia University for feedback to the continuing development of this module. The original publisher, the Royal Society, has graciously granted permission to post Dr. Hill's article in the APS Archive of Teaching Resources as a supplement to this article. Dr. Hill's paper is also available through JSTOR (http://www.jstor.org/), a subscription service available at many institutions.

<a id='6223930c-cce1-4254-9403-a43a460e43cc'></a>

## REFERENCES

1. Hill AV. The heat of shortening and the dynamic constants of muscle. *Proc R Soc London B Biol Sci* 126: 136–195, 1938.
2. Huxley AF. Muscle structure and theories of contraction. *Prog Biophys Biophys Chem* 7: 255–318, 1957.
3. Jewell BR and Wilkie DR. An analysis of the mechanical components in frog's striated muscle. *J Physiol* 143: 515–540, 1958.

<a id='a3a247dd-20e6-44c6-a428-28ecc9882210'></a>

Advances in Physiology Education • VOL 30 • JUNE 2006

<a id='c2cebe88-c6db-4fda-a5ae-0c6c416bb3c8'></a>

Downloaded from journals.physiology.org/journal/advances (087.121.037.170) on December 22, 2025.