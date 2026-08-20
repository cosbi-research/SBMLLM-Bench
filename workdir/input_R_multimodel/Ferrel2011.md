<a id='96404e64-e212-4f82-920f-65bcf6bfd750'></a>

<::logo: Cell
Cell
A green rectangle with the word "Cell" in white text centered within it.::>

<a id='cfd513ed-50cf-4a5c-888c-9d61de1167f0'></a>

<::logo: [Leading Edge Primer]Leading Edge Primer
The text "Leading Edge" is in brown, and "Primer" is in a lighter beige, with both words stacked and centered.::>

<a id='a78ae727-9bb1-4e84-8628-adb1e698c8b6'></a>

Modeling the Cell Cycle:
Why Do Certain Circuits Oscillate?

<a id='b060cefb-2851-4ae1-a42f-bb5e85d22d25'></a>

James E. Ferrell, Jr., 1,2,* Tony Yu-Chen Tsai, 1,2 and Qiong Yang¹
1Department of Chemical and Systems Biology
2Department of Biochemistry
Stanford University School of Medicine, Stanford, CA 94305-5174, USA
*Correspondence: james.ferrell@stanford.edu
DOI 10.1016/j.cell.2011.03.006

<a id='b8577e65-8407-4059-a414-448a0c17e6c8'></a>

Computational modeling and the theory of nonlinear dynamical systems allow one to not simply describe the events of the cell cycle, but also to understand why these events occur, just as the theory of gravitation allows one to understand why cannonballs fly in parabolic arcs. The simplest examples of the eukaryotic cell cycle operate like autonomous oscillators. Here, we present the basic theory of oscillatory biochemical circuits in the context of the Xenopus embryonic cell cycle. We examine Boolean models, delay differential equation models, and especially ordinary differential equation (ODE) models. For ODE models, we explore what it takes to get oscillations out of two simple types of circuits (negative feedback loops and coupled positive and negative feedback loops). Finally, we review the procedures of linear stability analysis, which allow one to determine whether a given ODE model and a particular set of kinetic parameters will produce oscillations.

<a id='775e1361-85c7-43ac-af08-d409ce68bcea'></a>

In many eukaryotic cells, the cell cycle proceeds as a sequence of contingent events. A new cell must first grow to a sufficient size before it can begin DNA replication. Then, the cell must complete DNA replication before it can begin mitosis. Finally, the cell must successfully organize a metaphase spindle before it can complete mitosis and begin the cycle again. If cell growth, DNA replication, or spindle assembly is slowed down, the entire cell cycle slows. Thus, this type of cell cycle is like an "assembly line" or "succession of dominoes" (Hartwell and Weinert, 1989; Murray and Kirschner, 1989b).

<a id='f25b9851-c9ca-4f66-a1d5-3f8a7308a004'></a>

However, some cell cycles are qualitatively different in terms
of their dynamics. Most notable of these exceptions is the early
embryonic cell cycle in the amphibian *Xenopus laevis*. DNA repli-
cation is not contingent upon cell growth, probably because the
frog egg is so big to start with. Mitotic entry is not contingent
upon completion of DNA replication, and mitotic exit is not
contingent upon the successful assembly of a metaphase
spindle because the relevant checkpoints are ineffective in the
context of the embryo's high cytoplasm:nucleus ratio (Dasso
and Newport, 1990; Minshull et al., 1994). Lacking these contin-
gencies, the early embryo simply pulses once every 25 min,
irrespective of whether the endpoints of the cell cycle (DNA
replication and mitosis) have been completed (Hara et al.,
1980). Thus, this cell cycle is clock-like (Murray and Kirschner,
1989b); it behaves as if it is being driven by an autonomous
biochemical oscillator.

<a id='0853e63d-7f2d-4c5f-8438-fa55acc60d29'></a>

Although many biological processes seem almost unfathomably complex and incomprehensible, oscillators and clocks are the types of processes that we might have a good chance of not just describing, but also understanding. Accordingly, much effort has gone into understanding how simple cell cycles work in model systems like *Xenopus* embryos and the fungi *S. pombe*

<a id='67a91e5d-7160-450a-afa3-75ea08277122'></a>

and S. cerevisiae. This requires the identification of the proteins and genes needed for the embryonic cell cycle and the elucidation of the regulatory processes that connect these proteins and genes. Over the past three decades, enormous progress has been made toward these ends. In each case, the cell cycle is driven by a protein circuit centered on the cyclin-dependent protein kinase CDK1 and the anaphase-promoting complex (APC) (Figure 1A). The activation of CDK1 drives the cell into mitosis, whereas the activation of APC, which generally lags behind CDK1, drives the cell back out (Figure 1B). There are still some missing components and poorly understood connections, but overall, the cell-cycle network is fairly well mapped out.

<a id='dd747ae6-a43b-455d-9217-6f56ba37e123'></a>

But a satisfying understanding of why the CDK1/APC system oscillates requires more than a description of components and connections; it requires an understanding of why any regulatory circuit would oscillate instead of simply settling down into a stable steady state. What types of biochemical circuits can oscillate, and what is required of the individual components of the circuit to permit oscillations? Such insights are provided by the theory of nonlinear dynamics and by computational modeling.

<a id='9e12213e-e3c7-43c9-aa7b-7780191af9d4'></a>

Indeed, cell-cycle modeling has become a very popular pursuit. Hundreds of models have been published (Table 1), beginning with Kauffman, Wille, and Tyson's prescient proposal that the cell cycle of the yellow slime mold *Physarum polycephalum* is driven by a relaxation oscillator (Kauffman and Wille, 1975; Tyson and Kauffman, 1975). Many of the early models, and a few of the more recent models, were simple, as models in physics typically are. They consisted of a small number of ordinary differential equations relating a few time-dependent variables (e.g., protein concentrations or activities) to each other and to a few time-independent kinetic parameters.

<a id='81883e80-8019-4702-acf7-ae8f4eba0ee2'></a>

874

<a id='dbcba2ae-82c6-4302-bc1c-31d924afdd67'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc.

<!-- PAGE BREAK -->

<a id='4fa463fc-5cf8-4928-a3f4-db7a29318eb2'></a>

Cell

<a id='ca59ccbd-3896-4720-9ca9-ea64b16de8cc'></a>

<::Figure 1. Simplified Depiction of the Embryonic Cell Cycle, High-lighting the Main Regulatory Loops: diagram::>
(A) This diagram illustrates the regulatory loops of the embryonic cell cycle. A central red oval labeled "Cyclin-CDK1" is shown. An arrow labeled "Cyclin" points to Cyclin-CDK1. Arrows originating from Cyclin-CDK1 point downwards, labeled "Mitotic phosphorylations". There are several feedback loops:
- A green oval labeled "APC-Cdc20" receives a curved arrow from Cyclin-CDK1 and sends a curved arrow labeled "Negative feedback" back to Cyclin-CDK1.
- A yellow oval labeled "Wee1" receives a curved arrow from Cyclin-CDK1 and sends a curved arrow labeled "Double-negative feedback" back to Cyclin-CDK1.
- A yellow oval labeled "Cdc25" receives a curved arrow from Cyclin-CDK1 and sends a curved arrow labeled "Positive feedback" back to Cyclin-CDK1.
(B) This graph shows the activity of CDK1 and APC over time. The y-axis is labeled "Activity". The x-axis is labeled "Time (mins)" and ranges from 0 to 50, with a major tick at 25. Two curves are plotted:
- A red curve labeled "CDK1" shows two sharp peaks of activity, centered around 15 and 40 minutes.
- A green curve labeled "APC" shows two peaks of activity that lag slightly behind the CDK1 peaks, also centered around 15 and 40 minutes, but slightly shifted to the right.
Below the graph, a bar represents the "Cell cycle phase". This bar is divided into alternating segments of light gray and dark gray:
- From 0 to approximately 12 minutes: light gray, labeled "S"
- From approximately 12 to 25 minutes: dark gray, labeled "M"
- From 25 to approximately 37 minutes: light gray, labeled "S"
- From approximately 37 to 50 minutes: dark gray, labeled "M"

(A) Cyclin-CDK1 is the master regulator of mitosis. APC-Cdc20 is an E3 ubiquityl ligase, which marks mitotic cyclins for degradation by the proteasome. Wee1 is a protein kinase that inactivates cyclin-CDK1. Cdc25 is a phosphoprotein phosphatase that activates cyclin-CDK1. Not shown here is Plk1, which cooperates with cyclin-CDK1 in the activation of APC-Cdc20.
(B) In the Xenopus embryo, the activation of CDK1 drives the cell into mitosis, whereas the activation of APC, which generally lags behind CDK1, drives the cell back out of mitosis.

<a id='8a01d81b-56ee-4f30-a0d6-f8737ba1c52b'></a>

The purpose of this type of modeling is to understand in simpler,
albeit more abstract, terms how and why the cell cycle works.

<a id='0fbe61dd-bf90-4e48-8c39-53c9ba3a0fee'></a>

Through time, many of the models have become more complicated and more like chemical engineering models, consisting of dozens of variables and regulatory processes. The purpose of this type of modeling is to account for and test our understanding of specific details of the system that, because of the complexity of the system, cannot always be understood through intuition. This type of detailed model has successfully accounted for the phenotypes of dozens of budding yeast mutants (Chen et al., 2004).

<a id='234a532e-1ab2-4bd2-a320-33831ed57f8f'></a>

Both types of modeling have their place in understanding cell-
cycle regulation, and both have their adherents. Modeling
approaches range from simple Boolean modeling to stochastic
modeling and partial differential equation modeling. However,
to date, the majority of effort has focused on ordinary differential
equation (ODE) modeling (Table 1), which gets at the basic
solution phase biochemistry of cell-cycle regulation.

<a id='18ff801a-c47a-46ba-9c3c-e68f06a0c82d'></a>

Here, we address the question of what it takes to make
a simple protein circuit like the CDK1/APC system oscillate.
We will start with Boolean modeling, which provides intuition
into the logic of biochemical oscillators. We then move on to

<a id='6842d3ec-da27-495c-baee-378c3e6753ce'></a>

ODE models, which translate this logic into chemical terms. The basic methods for analyzing ODE models of oscillators are well known in the field of nonlinear dynamics but are not so well known among biologists. We believe that it is high time that they were; after all, we biologists are studying what are prob-ably the world's most interesting nonlinear dynamical systems. We will emphasize the basic concepts of oscillator function and, to the extent possible, keep the algebra to a minimum. For further information, the reader is directed to lucid reviews by Goldbeter (Goldbeter, 2002) and Novák and Tyson (Novák and Tyson, 2008; Tyson et al., 2003), as well as Strogatz's outstanding textbook (Strogatz, 1994).

<a id='00451fe6-3cdd-45af-a4a2-a079679abcd9'></a>

## Boolean Models
We begin by paring the cell cycle down to a simple two-component model in which CDK1 activates APC and APC inactivates CDK1 (Figure 2B). This is the essential negative feedback loop upon which the cell-cycle oscillator is built (Murray et al., 1989). Perhaps the simplest way to think about the dynamics of a system like this is through Boolean or logical analysis (Glass and Kauffman, 1973).

<a id='5c48867b-7d61-4fe8-977d-c21370b80ac9'></a>

Suppose that both CDK1 and APC are perfectly switch-like in their regulation; that is, they are either completely on or completely off. Then, together, the system of CDK1 plus APC has four possible discrete states (APC<sub>on</sub>/CDK1<sub>on</sub>, APC<sub>on</sub>/CDK1<sub>off</sub>, APC<sub>off</sub>/CDK1<sub>on</sub>, and APC<sub>off</sub>/CDK1<sub>off</sub>) (Figure 2E). Now suppose the system starts in an interphase-like state, with APC<sub>off</sub>/CDK1<sub>off</sub>. In the first increment of time, what will happen? If the APC is off, then CDK1 turns on. Thus, we define a rule: state 1, with APC<sub>off</sub>/CDK1<sub>off</sub>, goes to state 2 with APC<sub>off</sub>/CDK1<sub>on</sub>. Next, the active CDK1 activates APC; thus, state 2 goes to 3. The active APC then inactivates CDK1, and state 3 goes to state 4. Finally, in the absence of active CDK1, the APC becomes inactive, and state 4 goes to state 1. This completes the cycle.

<a id='f7edba72-104d-4270-9094-26bca1ffba07'></a>

We can depict the dynamics of this oscillator as a diagram in "state space" (Figure 2E). The model goes through a never-ending cycle, and all of the possible states of the system are visited during each run through the cycle.

<a id='4f7a95e4-ec7f-4980-82b8-9f6691918763'></a>

If we add one more component to the system—for example,
a protein like Polo-like kinase 1 (Plk1), which here we assume
is activated by CDK1 and, in turn, contributes to the activation
of APC (Figure 2C)—then there are eight (2 × 2 × 2) possible
states for the system. If we start with all of the proteins off and
assume six biologically reasonable rules (active CDK1 activates
Plk1, active Plk1 activates APC, active APC inactivates CDK1...),
once again we get a never-ending cycle of states (Figure 2F). But
this time, only some of the possible states (states 1–6 in
Figure 2F) lie on the cycle. The other two states (7 and 8) feed
into the cycle in a manner determined by the rules we assume.
Thus, no matter where the system starts, it will converge to the
cycle sooner or later. The behavior of this Boolean model is
analogous to “limit cycle oscillations,” which we will encounter
again in the next section.

<a id='09958bbf-7c9f-420e-9f55-971c2d44108d'></a>

With Boolean models, it is easy to obtain oscillations. Indeed,
one can even get oscillations from a model with a single species
(CDK1) that flips on when it is off and flips off when it is on
(Figures 2A and 2D), a discrete representation of a protein that
negatively regulates itself.

<a id='10639d1a-5639-42ed-b4e7-69561cf8a1d9'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc. 875

<!-- PAGE BREAK -->

<a id='311caa96-d170-4c76-8f94-aae9701fe348'></a>

<::logo: [Cell]Cell
A green square with the word "Cell" in white in the bottom right corner::>

<a id='22e6c5ce-032a-4c66-a231-498559296517'></a>

<table id="2-1">
<tr><td id="2-2" colspan="4">Table 1. Some Mathematical Models of the Eukaryotic Cell Cycle</td></tr>
<tr><td id="2-3">Year</td><td id="2-4">Organism/Cell Type</td><td id="2-5">Type of Model</td><td id="2-6">Reference</td></tr>
<tr><td id="2-7">1970</td><td id="2-8">No specific organism</td><td id="2-9">ODE</td><td id="2-a">(Sel&#x27;kov, 1970)</td></tr>
<tr><td id="2-b">1974</td><td id="2-c">No specific organism</td><td id="2-d">ODE</td><td id="2-e">(Gilbert, 1974)</td></tr>
<tr><td id="2-f">1975</td><td id="2-g">Physarum polycephalum</td><td id="2-h">ODE</td><td id="2-i">(Kauffman and Wille, 1975)</td></tr>
<tr><td id="2-j">1975</td><td id="2-k">Physarum polycephalum</td><td id="2-l">ODE</td><td id="2-m">(Tyson and Kauffman, 1975)</td></tr>
<tr><td id="2-n">1991</td><td id="2-o">Xenopus laevis embryos</td><td id="2-p">ODE</td><td id="2-q">(Goldbeter, 1991)</td></tr>
<tr><td id="2-r">1991</td><td id="2-s">Xenopus embryos</td><td id="2-t">ODE</td><td id="2-u">(Norel and Agur, 1991)</td></tr>
<tr><td id="2-v">1991</td><td id="2-w">Xenopus embryos, somatic cells</td><td id="2-x">ODE</td><td id="2-y">(Tyson, 1991)</td></tr>
<tr><td id="2-z">1992</td><td id="2-A">Xenopus embryos</td><td id="2-B">ODE</td><td id="2-C">(Obeyesekere et al., 1992)</td></tr>
<tr><td id="2-D">1993</td><td id="2-E">Xenopus embryos</td><td id="2-F">ODE</td><td id="2-G">(Novak and Tyson, 1993a)</td></tr>
<tr><td id="2-H">1993</td><td id="2-I">Xenopus embryos</td><td id="2-J">ODE</td><td id="2-K">(Novak and Tyson, 1993b)</td></tr>
<tr><td id="2-L">1994</td><td id="2-M">Xenopus embryos</td><td id="2-N">ODE, delay differential equations</td><td id="2-O">(Busenberg and Tang, 1994)</td></tr>
<tr><td id="2-P">1996</td><td id="2-Q">Xenopus embryos</td><td id="2-R">ODE</td><td id="2-S">(Goldbeter and Guilmot, 1996)</td></tr>
<tr><td id="2-T">1997</td><td id="2-U">S. pombe</td><td id="2-V">ODE</td><td id="2-W">(Novak and Tyson, 1997)</td></tr>
<tr><td id="2-X">1998</td><td id="2-Y">S. pombe</td><td id="2-Z">ODE</td><td id="2-10">(Novak et al., 1998)</td></tr>
<tr><td id="2-11">1998</td><td id="2-12">Xenopus embryos</td><td id="2-13">ODE</td><td id="2-14">(Borisuk and Tyson, 1998)</td></tr>
<tr><td id="2-15">1999</td><td id="2-16">Mammalian somatic cells</td><td id="2-17">ODE</td><td id="2-18">(Aguda and Tang, 1999)</td></tr>
<tr><td id="2-19">2003</td><td id="2-1a">Xenopus embryos</td><td id="2-1b">ODE</td><td id="2-1c">(Pomerening et al., 2003)</td></tr>
<tr><td id="2-1d">2003</td><td id="2-1e">S. cerevisiae</td><td id="2-1f">ODE</td><td id="2-1g">(Ciliberto et al., 2003)</td></tr>
<tr><td id="2-1h">2004</td><td id="2-1i">S. cerevisiae</td><td id="2-1j">ODE</td><td id="2-1k">(Chen et al., 2004)</td></tr>
<tr><td id="2-1l">2004</td><td id="2-1m">S. cerevisiae</td><td id="2-1n">Boolean</td><td id="2-1o">(Li et al., 2004)</td></tr>
<tr><td id="2-1p">2004</td><td id="2-1q">S. pombe</td><td id="2-1r">Stochastic</td><td id="2-1s">(Steuer, 2004)</td></tr>
<tr><td id="2-1t">2005</td><td id="2-1u">Xenopus embryos</td><td id="2-1v">ODE</td><td id="2-1w">(Pomerening et al., 2005)</td></tr>
<tr><td id="2-1x">2006</td><td id="2-1y">Mammalian somatic cells</td><td id="2-1z">Delay differential equations</td><td id="2-1A">(Srividhya and Gopinathan, 2006)</td></tr>
<tr><td id="2-1B">2006</td><td id="2-1C">S. cerevisiae</td><td id="2-1D">Stochastic</td><td id="2-1E">(Zhang et al., 2006)</td></tr>
<tr><td id="2-1F">2007</td><td id="2-1G">S. cerevisiae</td><td id="2-1H">Stochastic</td><td id="2-1I">(Braunewel and Bornholdt, 2007)</td></tr>
<tr><td id="2-1J">2007</td><td id="2-1K">S. cerevisiae</td><td id="2-1L">Stochastic</td><td id="2-1M">(Okabe and Sasai, 2007)</td></tr>
<tr><td id="2-1N">2007</td><td id="2-1O">S. cerevisiae</td><td id="2-1P">Hybrid</td><td id="2-1Q">(Barberis et al., 2007)</td></tr>
<tr><td id="2-1R">2008</td><td id="2-1S">Xenopus embryos</td><td id="2-1T">ODE</td><td id="2-1U">(Tsai et al., 2008)</td></tr>
<tr><td id="2-1V">2008</td><td id="2-1W">S. cerevisiae</td><td id="2-1X">Stochastic</td><td id="2-1Y">(Ge et al., 2008)</td></tr>
<tr><td id="2-1Z">2008</td><td id="2-20">S. cerevisiae</td><td id="2-21">Stochastic</td><td id="2-22">(Mura and Csikász-Nagy, 2008)</td></tr>
<tr><td id="2-23">2008</td><td id="2-24">S. pombe</td><td id="2-25">Boolean</td><td id="2-26">(Davidich and Bornholdt, 2008)</td></tr>
<tr><td id="2-27">2008</td><td id="2-28">Mammalian somatic cells</td><td id="2-29">ODE</td><td id="2-2a">(Yao et al., 2008)</td></tr>
<tr><td id="2-2b">2009</td><td id="2-2c">Mammalian somatic cells</td><td id="2-2d">ODE</td><td id="2-2e">(Alfieri et al., 2009)</td></tr>
<tr><td id="2-2f">2010</td><td id="2-2g">S. cerevisiae</td><td id="2-2h">ODE</td><td id="2-2i">(Charvin et al., 2010)</td></tr>
<tr><td id="2-2j">2010</td><td id="2-2k">S. cerevisiae, S. pombe</td><td id="2-2l">Boolean</td><td id="2-2m">(Mangla et al., 2010)</td></tr>
<tr><td id="2-2n">2010</td><td id="2-2o">S. pombe</td><td id="2-2p">ODE</td><td id="2-2q">(Li et al., 2010)</td></tr>
</table>

<a id='f39325ca-c521-4a75-932a-6b57f7b0f2a1'></a>

## ODE Models of the CDK1/APC System

Although Boolean analysis is simple and appealing, it is not completely realistic. First, all three Boolean models with negative feedback loops (Figures 2A–2C) yielded oscillations even though we know that real negative feedback loops do not always oscillate. The problem is the simplifying assumptions that underpin Boolean analysis: the discrete activity states and time steps. Even if individual CDK1 and APC molecules actually flip between discrete on/off states, a cell contains a number of CDK1 and APC molecules, and they would not be expected to all flip simultaneously.

<a id='e11ba71f-7e9c-46eb-8124-e49923538a1e'></a>

The framework for describing the dynamics of such a system
is chemical kinetic theory, and, assuming that the numbers of

<a id='187c3555-75dc-47d3-b424-634b3798bb79'></a>

CDK1 and APC molecules are large, the activation and inactiva-
tion of CDK1 and APC can be described by a set of differential
equations. Here, we will build up an ODE model of the system,
starting with a one-ODE model, which fails to produce
oscillations. We then add additional complexity to the ODEs
until the model succeeds in producing sustained, limit cycle
oscillations.

<a id='3d0a2d82-a088-4b32-a05c-260968f64943'></a>

**A One-ODE Model**
By definition, the rate of change of active CDK1 (denoted CDK1*)
is the rate of CDK1 activation minus the rate of CDK1 inactiva-
tion. For simplicity, we will assume that CDK1 is activated
by the rapid, high-affinity binding of cyclin, which is being

<a id='992a25b8-a3b0-4df3-adf3-2528413b6bce'></a>

876 Cell 144, March 18, 2011 ©2011 Elsevier Inc.

<!-- PAGE BREAK -->

<a id='2b370699-4f9a-4a70-aa85-c9c6a7da1670'></a>

Cell

<a id='4cc813ca-c82f-465e-a23a-ccf619b1d91a'></a>

A
B
C
D
E
F
<::A: Diagram showing a red circle labeled "CDK1" with a self-activating feedback loop (an arrow originating from and returning to CDK1).
B: Diagram showing a red circle labeled "CDK1" and a green circle labeled "APC" with mutual activating feedback loops (an arrow from CDK1 to APC and an arrow from APC to CDK1).
C: Diagram showing a green circle labeled "APC", a red circle labeled "CDK1", and a blue circle labeled "Plk1". APC inhibits CDK1 (flat-headed arrow from APC to CDK1) and Plk1 (flat-headed arrow from APC to Plk1). CDK1 activates Plk1 (arrow from CDK1 to Plk1).
D: State transition diagram with two nodes. Node 1 is labeled "Cdk1 off" and node 2 is labeled "Cdk1 on". There are arrows forming a cycle: from node 1 to node 2, and from node 2 to node 1.
E: State transition diagram with four nodes arranged in a square. Node 1 is labeled "APC off Cdk1 off". Node 2 is labeled "APC off Cdk1 on". Node 3 is labeled "APC on Cdk1 on". Node 4 is labeled "APC on Cdk1 off". Arrows form a cycle: 1 to 2, 2 to 3, 3 to 4, and 4 to 1.
F: State transition diagram with eight nodes arranged in a 3D cube-like structure, representing states of APC, Cdk1, and Plk1 (on/off). Each node is numbered and labeled with its state:
- Node 1: APC off, Cdk1 off, Plk1 off
- Node 2: APC off, Cdk1 on, Plk1 off
- Node 3: APC off, Cdk1 on, Plk1 on
- Node 4: APC on, Cdk1 on, Plk1 on
- Node 5: APC on, Cdk1 off, Plk1 on
- Node 6: APC on, Cdk1 off, Plk1 off
- Node 7: APC off, Cdk1 off, Plk1 on
- Node 8: APC on, Cdk1 on, Plk1 off
Solid arrows indicate transitions: 1 to 2, 2 to 3, 3 to 4, 4 to 5, 5 to 6, 6 to 1.
Dashed arrows indicate transitions: 1 to 7, 7 to 3, 3 to 8, 8 to 4, 4 to 3, 3 to 7, 5 to 7, 7 to 5, 2 to 8, 8 to 2, 6 to 5, 5 to 6, 6 to 1, 1 to 6.
: figure::>

<a id='f19d7109-9f25-400a-9cfa-3b78db88a73a'></a>

Figure 2. Boolean Models of CDK1 Regulation
(A–C) Schematic representation of negative feedback loops composed of one (A), two (B), or three (C) species.
(D–F) Trajectories in state space for Boolean models of these three negative feedback systems. Solid lines represent limit cycles; dashed lines (in F) connect the states off the limit cycle to the limit cycle.

<a id='b7257c5e-f6de-4b5b-b199-417f3d27809e'></a>

synthesized at a constant rate of a₁ (Equation 1, blue). For CDK1
inactivation, we will assume mass action kinetics (Equation 1,
pink).

<a id='0a55fc79-bbc8-4c2b-adb3-39fd59d5aafb'></a>

This gives us the first-order differential equation:

<a id='c9829360-15d7-45c6-963a-0d674a2c8324'></a>

dCDK1*/dt = α₁ - β₁CDK1*·APC* [Equation 1]

<a id='eac0889d-2d1d-4d5b-aac2-bd6639a7996f'></a>

There are two time-dependent variables, CDK1* and APC*. To allow the system to be described by an ODE with a single time-dependent variable (Figure 3A), we assume that the activity of APC is regulated rapidly enough by CDK1* so that it can be considered an instantaneous function of CDK1*. What functional form should we use for APC's response function? Here, we will assume that APC's response to CDK1* is ultrasensitive— sigmoidal in shape, like the response of a cooperative enzyme—and that the response is described by a Hill function. This assumption is reasonable because APC activation is a multi-

<a id='cbaf3604-b640-4040-8c63-1e68fc70af4f'></a>

step process; multistep processes often yield ultrasensitive,
sigmoidal responses; and, for our purposes, the Hill equation
with a Hill coefficient (*n*) greater than 1 can be thought of as
a generic sigmoidal function. Substituting a Hill function for
*APC*** in Equation 1, we get a one-ODE model of a negative feed-
back loop:

<a id='3b3c0584-d7ea-4487-b0bf-49f284344f78'></a>

dCDK1*/dt = Α₁ - Β₁CDK1* (CDK1*ⁿ¹ / (K₁ⁿ¹ + CDK1*ⁿ¹))

[Equation 2]

<a id='443ae4fd-76bd-4536-ba42-f3f80bebfda2'></a>

We now choose, somewhat arbitrarily, values for the model's parameters (α₁ = 0.1, β₁ = 1, K₁ = 0.5, n₁ = 8) and initial conditions (CDK1*[0] = 0). We can then numerically integrate Equation 2 over time and see how the concentration of activated CDK1* evolves.

<a id='8f4ae048-746c-4837-a35d-832d5da4a8c3'></a>

As shown in Figure 3C, the system moves monotonically from its initial state toward a steady state; there is no hint of oscillation. This monotonic approach to steady state is observed no matter what we assume for the parameters and initial conditions. Thus,

<a id='ee7679f9-62a0-463b-8f3f-ab9768af27f0'></a>

<::Figure with three panels (A, B, C) illustrating aspects of CDK1 activity. A: A red circle labeled "CDK1" with a curved arrow originating from and pointing back to itself with a blunt end, indicating negative feedback or self-inhibition. B: A one-dimensional phase line diagram for CDK1* ranging from 0.0 to 1.0. A black dot is located at approximately 0.45, with arrows pointing towards it from both the left and right, indicating a stable fixed point. The x-axis is labeled "CDK1*". C: A line graph showing "Activity" on the y-axis (from 0.0 to 1.0) versus "Time" on the x-axis (from 0 to 20). A red curve, labeled "CDK1*", starts at 0 activity at time 0, rises sharply, and then plateaus at an activity level of approximately 0.42.::>

<a id='c387fc54-0555-4e00-ac25-a515c281cc0d'></a>

Figure 3. A Model of CDK1 Regulation with
One Differential Equation
(A) Schematic of the model. The parameters
chosen for the model were ̑₁ = 0.1, ̑₁ = 1, K₁ =
0.5, and n₁ = 8.
(B) Trajectories in one-dimensional phase space,
approaching a stable steady state (designated by
the filled circle) at CDK1* ≈ 0.43.
(C) Time course of the system, starting with
CDK1*[0] = 0 and evolving toward the steady
state.

<a id='27218a90-d099-4451-8d56-431a1ccb96cb'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc. 877

<!-- PAGE BREAK -->

<a id='64dd5f66-9398-4394-80d2-b090ea5a25a8'></a>

<::logo: [Cell]Cell
A green square with the word "Cell" in white text at the bottom right corner.::>

<a id='277c9ae1-238a-42d5-9fa8-3c4e62df9cdd'></a>

A<::A diagram showing a regulatory network. A red circle labeled 'CDK1' and a green circle labeled 'APC' are connected by two curved arrows. An arrow from CDK1 to APC has a flat head, indicating inhibition. An arrow from APC to CDK1 has a pointed head, indicating activation.: diagram::>B<::A plot with 'CDK1*' on the x-axis, ranging from 0.0 to 1.0, and 'APC*' on the y-axis, ranging from 0.0 to 1.0. Two curves are plotted: a red curve labeled 'CDK1' that starts high and decreases as CDK1* increases, and a green curve labeled 'APC' that starts low and increases as CDK1* increases. The curves intersect at approximately (0.4, 0.4). An arrow indicates movement along the green curve towards the intersection point, and then along the red curve towards the intersection point.: chart::>C<::A plot with 'Time' on the x-axis, ranging from 0 to 25, and 'Activity' on the y-axis, ranging from 0.0 to 1.0. Two curves are plotted: a red curve labeled 'CDK1' and a green curve labeled 'APC'. Both curves start at 0, rise to a peak around time 5 (CDK1 peaks slightly higher than APC), then oscillate slightly before settling to a stable activity level of approximately 0.4.: chart::>Red nullcline:<::A diagram showing a red circle labeled 'CDK1' and a green circle labeled 'APC'. A curved arrow from CDK1 points to APC with a flat head, indicating inhibition.: diagram::>Green nullcline:<::A diagram showing a red circle labeled 'CDK1' and a green circle labeled 'APC'. A curved arrow from APC points to CDK1 with a pointed head, indicating activation.: diagram::>

<a id='39a4d137-9957-4aca-9b15-91e2910e6d6b'></a>

Figure 4. A Two-ODE Model of CDK1 and APC Regulation

(A) Schematic of the model. The parameters chosen for the model were a₁ = 0.1, a₂ = 3, β₁ = 3, β₂ = 1, K₁ = 0.5, K₂ = 0.5, n₁ = 8, and n₂ = 8.

(B) Phase space depiction of the system. The red and green curves are the two nullclines of the system, which can be thought of as the steady-state response curves for the two individual legs of the feedback loop. The filled black circle at the intersection of the nullclines (with CDK1*≈0.42 and APC*≈ 0.37) represents a stable steady state. One trajectory is shown, starting at CDK1*[0] = 0, APC[0] = 0, and spiraling in toward the stable steady state.

(C) Time course of the system, showing damped oscillations approaching the steady state.

<a id='108eb682-8d8d-49b6-95ca-bbf5334d901f'></a>

we have not yet built an oscillator model. Even though we were able to produce sustained oscillations with a one-variable Boolean model of a negative feedback loop (Figures 2A and 2D), translating the model into a differential equation eliminated the oscillations.

<a id='42d1c28e-7baa-4cab-ad88-1ccb574283aa'></a>

Another way of representing the system's behavior is through a phase plot, which shows all possible activities of the system. This is similar to the state-space plots that we used for the Boolean analysis, but instead of having a few discrete states, the phase plot displays a continuum, showing how the system's transition between states occurs through a smooth continuum (as we would expect, given that the numerous CDK1 molecules do not all activate simultaneously but "smoothly" turn on.).

<a id='36d0e9c0-1bbe-4ed9-956a-503785eeec43'></a>

The phase plot contains one dimension for each time-depen-dent variable. Therefore, in this one-variable model, the phase plot possesses one axis, representing the concentration of acti-vated CDK1* (Figure 3B). In addition, the system's phase plot shows one stable steady state with CDK1* \u2248 0.43. If the system starts off with CDK1 activity less or greater than 0.43, the system will move along a trajectory back to 0.43. In other words, any initial condition to the left or right of the steady state yields a trajectory moving to the right or left, respectively.

<a id='dbb13a48-798d-4e90-a554-839c49b1489e'></a>

### A Two-ODE Model
Why did the one variable Boolean model produce oscillations (Figures 2A and 2D), whereas the one-ODE model (Equation 2) did not (Figure 3)? The discrete time steps of the Boolean model help to segregate CDK1 activation from inactivation in time. Thus, perhaps adding another ODE (Figure 4A), which acknowledges the fact that APC regulation is not instantaneous, might allow us to generate oscillations.

<a id='18d71a29-1459-4db3-8c7e-134b7df0b573'></a>

First, we write an ODE for the activation and inactivation of
CDK1 (Equation 3). We once again assume that CDK1 is acti-
vated by a constant rate of cyclin synthesis (α₁). We assume
that the multistep process through which APC* inactivates
CDK1* is described by a Hill function. The inactivation rate is
therefore proportional to the concentration of CDK1* (the
substrate being inactivated) times a Hill function of APC*.

<a id='3cc26f9f-4a6c-4475-afd0-3fb38747dccc'></a>

Now for APC (Equation 4), we assume that its rate of its activa-
tion by CDK1* is proportional to the concentration of inactive
APC (which, assuming the total concentration of active and inac-
tive APC to be constant, we take to be 1 – APC*) times a Hill
function of CDK1*, and the rate of inactivation of APC* is
described by simple mass action kinetics. The resulting two-
ODE model is:

<a id='8a1443e5-dcfe-477c-b6cd-14835685b8d4'></a>

dCDK1* / dt = α₁ - β₁CDK1* APC^n1 / (K₁^n1 + APC^n1) [Equation 3]
dAPC* / dt = α₂(1 - APC*) CDK1*^n2 / (K₂^n2 + CDK1*^n2) - β₂APC* [Equation 4]

<a id='f72bdd6f-4ed6-4e43-8e0e-63c94819551a'></a>

Again, we choose kinetic parameters and initial condition (as described in the caption to Figure 4) and integrate the ODEs numerically. The results are shown in Figures 4B and 4C. The CDK1 activity initially rises as the system moves from interphase (low CDK1 activity) toward M phase (high CDK1 activity) (Figure 4C). After a lag, the APC activity begins to rise too. Then, the rate of CDK1 inactivation (driven by APC activation) exceeds the rate of CDK1 activation (driven by cyclin synthesis), and the CDK1 activity starts to fall. After a few wiggles up and down, the system approaches a steady state with intermediate levels of both CDK1 and APC activities. Thus, we have generated damped oscillations, but not sustained oscillations.

<a id='09461ccf-6992-4110-b94f-a55de9ed63f0'></a>

Figure 4B shows the phase space view of these damped oscil-lations. The phase space is now two dimensional because there are two time-dependent variables. There is a stable steady state that sits at the intersection of two curves called the nullclines (green and red curves, Figure 4B). These two nullclines can be thought of as stimulus-response curves for the two individual legs of the CDK1/APC system. The red nullcline (defined by the equation dCDK1*/dt = 0) represents what the steady-state response of CDK1* to constant levels of APC activity would be if there were no feedback from CDK1* to APC* (Figure 4B). The green nullcline (defined by dAPC*/dt = 0) represents what the steady-state response of APC* to CDK1* would be if there were no feedback from APC* to CDK1* (Figure 4B). For the whole

<a id='86f3d40d-ba23-4528-8c2f-164ac0829b26'></a>

878

<a id='f4336fdf-e651-4b1b-b90a-5c15fd58c2ca'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc.

<!-- PAGE BREAK -->

<a id='2edceb25-1f04-4ec8-bb41-8fab6640ab13'></a>

Cell

<a id='20558f53-c79e-40e7-9a71-2771e4896a86'></a>

<::Figure 5. A composite figure with three panels (A, B, C) illustrating a three-ODE model of CDK1, Plk1, and APC regulation.
(A) Schematic of the model: A diagram shows three interacting components. A red circle labeled "CDK1" activates (arrow) a blue circle labeled "Plk1". The blue circle "Plk1" activates (arrow) a green circle labeled "APC". The green circle "APC" inhibits (T-bar) the red circle "CDK1". The parameters chosen for the model were α₁ = 0.1, α₂ = 3, α₃ = 3, β₁ = 3, β₂ = 1, β₃ = 1, K₁ = 0.5, K₂ = 0.5, K₃ = 0.5, n₁ = 8, n₂ = 8, and n₃ = 8.
(B) Phase space depiction of the system: A 3D plot with axes labeled Plk1* (vertical axis), APC* (depth axis), and CDK1* (horizontal axis), all ranging from 0.0 to 1.0. Two light blue colored surfaces represent two of the three null surfaces of the system. An open circle at the intersection of the null surfaces (approximately CDK1* = 0.43, Plk1* = 0.42, and APC* = 0.37) represents an unstable steady state. A black curved arrowed line shows one trajectory, starting at CDK1*[0] = 0, Plk1[0] = 0, APC[0] = 0, and spiraling in toward a limit cycle.
(C) Time course of the system: A 2D line graph with "Time" on the x-axis (from 0 to 25) and "Activity" on the y-axis (from 0.0 to 1.0). Three colored lines show sustained limit cycle oscillations. The red line represents CDK1, the green line represents APC, and the blue line represents Plk1. All three lines oscillate with a similar period, peaking sequentially, showing a rhythmic pattern of activity.: chart::>

<a id='3f8a5093-98ad-4f16-bd1c-1af36af5a5ad'></a>

system to be in steady state, both time derivatives must be zero.
Thus, the steady state for the entire system lies where the two
nullclines intersect. The steady state is stable, and the trajectory
of the system (black curve) spirals in from the initial values of
CDK1* and APC* toward the stable steady state (Figure 4B).

<a id='62977d23-dffa-4a0c-b4ef-286c51420679'></a>

**A Three-ODE model**
Perhaps we can improve the oscillations by adding a third species to the model, which increases the lag between CDK1 activation and APC activation (Figure 4C). Here, we will add *Plk1* back into the model, as we did in the three-component Boolean model (Figure 2C), with *Plk1* assumed to act as an intermediary between CDK1 and APC. We now have three ODEs (Equations 5–7). The equation for the activation and inactivation of CDK1 stays the same (Equation 5). The activation of *Plk1* by *CDK1** is proportional to the concentration of inactive *Plk1* (1 – *Plk1**) times a Hill function of *CDK1**, and the inactivation is proportional to *Plk1** (Equation 6). A similar logic for the activation and inactivation of APC gives Equation 7.

<a id='7b2e3fa7-d606-48fc-8d77-b82650cea6bf'></a>

dCDK1*
---
dt
= α₁ - β₁CDK1* (APC*^n1 / (K₁^n1 + APC*^n1))
[Equation 5]

dPlk1*
---
dt
= α₂(1 - Plk1*) (CDK1*^n2 / (K₂^n2 + CDK1*^n2)) - β₂Plk1*
[Equation 6]

dAPC*
---
dt
= α₃(1 - APC*) (Plk1*^n3 / (K₃^n3 + Plk1*^n3)) - β₃APC*
[Equation 7]

<a id='cd608c7e-3f1f-4b2c-9bff-0fed13f2c2b4'></a>

We arbitrarily choose parameters and initial conditions, and eureka! We now have sustained oscillations (Figures 5B and 5C). Moreover, no matter initial conditions, the system eventually approaches the same pattern of oscillations, with CDK1 activity peaking first, followed by Plk1 activity and then APC activity (Figure 5C). In the phase plane view, this pattern of oscillations is a limit cycle, a closed circle of states that all trajectories spiral in or out toward (black curve, Figure 5B).

<a id='42ddada5-78a7-4682-be38-639e96b9fb62'></a>

With Equations 5-7, we finally have an ODE model of the Xeno-
pus embryonic cell cycle that exhibits sustained limit cycle oscil-
lations. The key features of this model include the presence of
negative feedback, the fact that there are more than two compo-
nents to the negative feedback loop, and the presence of ultrasen-
sitivity in the individual steps of the loop. These last two features

<a id='c31b2e88-bccf-43e0-8d9d-8e5436dc541a'></a>

help to generate a time delay in the negative feedback, which helps to keep the system from settling into a stable steady state.

<a id='479034cd-fe77-491d-a24a-4157ad056b2e'></a>

## Linear Stability Analysis
So far, we have confined ourselves to analyzing ODE models through simulations. This provides an intuitive feel for the behavior of a system, but of course, it is never possible to choose all possible values for the kinetic parameters or all possible initial conditions. Is there a way to explain theoretically, rather than computationally, why the one-ODE model failed to oscillate at all, the two-ODE model at best yielded damped oscillations, and the three-ODE model finally yielded sustained oscillations?

<a id='73386b5e-3847-4fa7-99b8-ff4d0a090641'></a>

The answer is yes, and probably the most straightforward approach is "linear stability analysis." Linear stability analysis is quite remarkable. It assesses the stability of the steady states of the system, and, almost magically, allows the dynamics of the system to be characterized even when the system is far from steady state. To get started with linear stability analysis, we will analyze the steady state of the one-ODE model described in Equation 2.

<a id='e1c17bcb-608d-4714-9daf-36711f51408d'></a>

**Linear Stability Analysis of the One-ODE Model**
For notational simplicity, we will refer to the rate of change of CDK1 (dCDK1*/dt) as f. This function f can be thought of as a function of CDK1*, which in turn is a function of time. In terms of f, Equation 2 becomes:

<a id='e1260b41-45d8-4eb6-8934-08d0a5a28cdf'></a>

f = α₁ - β₁CDK1 * (CDK1ⁿ¹ / (K₁ⁿ¹ + CDK1ⁿ¹)) [Equation 8]

<a id='a9d27748-4266-4337-b256-87b8fdd4f145'></a>

The system will have a steady state when the derivative
_dCDK1*_/dt equals zero (that is, CDK1* is not changing with
respect to time), which means that:

<a id='7d0dc8d2-02df-4daa-8a91-fa3bbd09f5c3'></a>

f=0

[Equation 9]

<a id='5bb17df8-1c88-43f5-aca1-c032ec7e46e2'></a>

We can calculate the value of _CDK1_\* for which Equation 9 is true either numerically or algebraically. For the parameters used in Figure 3, _CDK1_\*\_ss ≈ 0.43. To the left of the steady state, _f_ is positive (Figure 6); thus, if _CDK1_\* is less than its steady-state value, it will increase with time. Similarly, if _CDK1_\* is greater than its steady-state value, it will decrease with time. This immediately shows that the steady state is stable. With linear stability analysis, we can push this further and determine _how_ stable the steady-state is, in quantitative terms.

<a id='9f72e8f1-ec86-434e-a2a8-8fecaf873fd6'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc.

<a id='ad9aca31-90cf-4000-a2f2-00e6fe6303e3'></a>

879

<!-- PAGE BREAK -->

<a id='b8d41163-c484-4ced-aaf4-dacd5a9bf114'></a>

<::logo: Cell
Cell
A green square with the word "Cell" in white text in the bottom right corner.::>

<a id='13ad536e-2f8e-4a24-a2cb-3476bae9b04e'></a>

<::transcription of the content: chart::>Figure 6. Linear Stability Analysis for the One-ODE Model The blue curve represents $f$ as a function of $CDK1^*$. The dashed red line approximates $f$ for small values of $\delta CDK1^*$.Graph titled 'Linear Stability Analysis for the One-ODE Model'. The x-axis is labeled '$CDK1^*$' with an arrow indicating increasing values. A specific point on the x-axis is marked '$CDK1^*_{ss}$'. The y-axis is labeled '$f(CDK1^*)$' with an arrow indicating increasing values. A specific point on the y-axis is marked '0'. A blue curve, labeled '$f(CDK1^*)$', is plotted, showing a decreasing trend. A dashed red line is shown tangent to the blue curve at a point. This point of tangency is marked by a black circle. From this point, a dashed vertical line extends to the x-axis at '$CDK1^*_{ss}$', and a dashed horizontal line extends to the y-axis at '0'. An equation is displayed at the top left: 'slope = $\frac{df}{dCDK1^*} | CDK1^*_{ss}$'. A horizontal brace above the x-axis, starting from the point of tangency and extending to the right, is labeled '$\delta CDK1^*$'. A vertical brace to the right of the y-axis, starting from the point of tangency and extending downwards, is labeled '$f(CDK1^*_{ss} + \delta CDK1^*) \approx slope \bullet \delta CDK1^*$'.<::

<a id='d2c88473-f5df-4e86-ae0b-f957fbd551a8'></a>

Imagine that we perturb the system away from the steady state by some small increment _δCDK1*_. At what rate will _CDK1*_ move back toward _CDK1*ss_ (and _δCDK1*_ move back toward zero)? In other words, how quickly does the system return to equilibrium?

<a id='39b41eaf-4f39-4437-8eef-332c56ab8fe1'></a>

This question can be addressed algebraically with a Taylor
series expansion, but perhaps it is easier to approach graphi-
cally. This is set up in Figure 6. The x axis represents the concen-
tration of active CDK1*; the y axis represents the rate of change
of CDK1*, f; and the blue curve depicts how f varies with CDK1*.
When CDK1*ss ≈ 0.43, the system is at steady state and f = 0. To
the left of the steady state, the value of f is positive, and the blue
curve lies above the x axis. To the right of the steady state, the
value of f is negative, and the blue curve lies below the axis.

<a id='b626727f-daf6-4293-9b5b-226f553fa9f6'></a>

If the system is perturbed from the steady state by _δ_CDK1*, the rate at which it will return toward the steady state is given by the value of _f_ at CDK1*<sub>ss</sub> + _δ_CDK1*. For small values of _δ_CDK1*, we can approximate _f_ (CDK1*<sub>ss</sub> + _δ_CDK1*) by _δ_CDK1* times the slope of the dashed red line (Figure 6), which is the tangent to the blue curve at the steady state. The slope of the dashed red line is defined to be _df_/_d_CDK1* |<sub>CDK1*ss</sub> (the value of _df_/_d_CDK1* at CDK1*<sub>ss</sub>). Therefore, the rate at which CDK1* goes toward the steady state, which equals the rate at which _δ_CDK1* goes toward zero, is given by:

<a id='9cae9eb2-5d5d-4def-b132-17eb95006019'></a>

dδCDK1*
---- = slope • δCDK1* = ( df / dCDK1* | CDK1*ss ) • δCDK1*
dt

[Equation 10]

<a id='48e337e6-68b8-4051-9731-a90a676d4342'></a>

For notational convenience, we will represent this slope by \u03bb.
Thus, Equation 10 becomes:

<a id='d0d92903-4512-4658-8f66-15a9f02961dc'></a>

dδCDK1*
---
dt
= λ•δCDK1*

[Equation 11]

<a id='3018d0bc-2fb3-4c26-8b95-981aa77f03a1'></a>

ODEs like Equation 11 show up over and over again in quantita-
tive biology. And, fortunately, it is a particularly simple ODE,
probably the only one that most biologists will ever need to solve
analytically. Its solution is an exponential function and describes
an exponential approach to steady state:

<a id='7244cf70-f032-44aa-b4cc-a37f8aa3bb9d'></a>

δCDK1*(t) = δCDK1*(0)e^(λt) [Equation 12]

<a id='b0f43bc1-54ab-47ab-80bf-e5bf2685c74b'></a>

Thus, to determine the stability of the steady state, one simply
needs to determine the value of λ by evaluating the derivative
df/dCDK1* at the steady state. If λ is negative, the steady
state is stable and a small perturbation of the system will return
exponentially toward the steady state with a half-time of –ln 2/λ.
The bigger the absolute value of λ, the faster the system
approaches the steady state and, in a sense, the more stable
the steady state is.

<a id='8dd602ec-fc72-4e32-9e51-867aaa8cd82b'></a>

We can now apply linear stability analysis to our one-ODE
model (_Equation 8_). First, we differentiate the right side of the
ODE with respect to _CDK1*_:

<a id='1ced8ff9-c51f-4c77-871c-6af6b9bb529d'></a>

df / dCDK1* = - β₁CDK1^n1 (CDK1^n1 + K₁^n1 (1 + n1)) / (CDK1^n1 + K₁^n1)² [Equation 13]

<a id='ca9296e3-5de9-4489-870c-b98e767e062d'></a>

Next, we evaluate this derivative at CDK1* = CDK*ss. Because all kinetic parameters are positive numbers and CDK1*ss is always nonnegative, this derivative always evaluates to a negative number (because of the leading negative sign) and the steady state is stable. For the particular choice of parameters given in Figure 3, λ ≈ — 1.66.

<a id='92a361b1-7198-4603-b74c-5485cd52512c'></a>

**Stability in the Two-ODE Model and Three-ODE Model**
The logic behind linear stability analysis for a two-ODE model is similar; the algebra, though, is more complicated. We start by rewriting Equations 3 and 4, using the shorthand of f and g to represent the rates of change of CDK1* and APC*, respectively.

<a id='4f21e7b1-654b-446a-ad84-30e5e640559e'></a>

dCDK1* / dt = f = α₁ - β₁CDK1* (APC*ⁿ¹ / (K₁ⁿ¹ + APC1*ⁿ¹)) [Equation 14]

dAPC* / dt = g = α₂(1 - APC*) (CDK1*ⁿ² / (K₂ⁿ² + CDK1*ⁿ²)) - β₂APC*

<a id='10d98131-468f-4148-adea-9988165c2a0b'></a>

[Equation 15]

<a id='c95d3007-165b-40d7-8caa-c0be9c807c09'></a>

Again, we identify the steady states of the system and consider small perturbations of the system from the steady state. At this point, the procedure becomes more complicated. To quantitatively analyze the stability of the system, we cannot simply calculate one scalar value λ at the steady state values (CDK1*ss, APCss*) because the two equations are interdependent. Instead, we need to calculate eigenvalues of the system at the steady state. Eigenvalues are coefficients—real or complex numbers—that yield the same information about stability that we got from the value of λ in the one-dimensional analysis. For present purposes, we will consider them simply as numbers that can be calculated through a straightforward procedure (see Box 1).

<a id='3a225073-d8d0-4a84-96af-0ce283e69fb5'></a>

The eigenvalues for the two-ODE model turn out to be complex numbers (Box 1). What does that mean? Remember that:

<a id='744a7c83-42fb-436d-b1c5-e5b9a1d79788'></a>

e^λt = e^(x+iy)t = e^xt e^iyt = e^xt (cos yt + i sin yt)
[Equation 18]

<a id='48971f1e-2441-49bb-9100-3b46fb9867db'></a>

Thus, the real part of \u03bb (x in Equation 18) determines whether the amplitude of oscillations increases or decreases (i.e.,

<a id='dec0e08a-b8c9-4019-8065-c3a422f94747'></a>

880 Cell 144, March 18, 2011 2011 Elsevier Inc.

<!-- PAGE BREAK -->

<a id='547721ce-3560-43ff-9270-788cccfdee20'></a>

Cell

<a id='eb967ddc-dde3-4026-900d-c236a9967b68'></a>

## Box 1. Obtaining Eigenvalues for the Two-ODE Model

First, we set up the system's Jacobian matrix A, which is a table of the two partial derivatives of _f_ and the two partial derivatives of _g_:

$A = \begin{pmatrix}
\frac{\partial f}{\partial CDK1^*} & \frac{\partial f}{\partial APC^*}\\
\frac{\partial g}{\partial CDK1^*} & \frac{\partial g}{\partial APC^*}
\end{pmatrix}$ [Equation 16]

Next, we evaluate these four partial derivatives at the steady state, yielding a matrix of four numbers, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Finally, we use these four numbers to calculate the eigenvalues. For a two-ODE system, the eigenvalues are given by:

$\lambda_1 = \frac{\tau + \sqrt{\tau^2 - 4\Delta}}{2}$, $\lambda_2 = \frac{\tau - \sqrt{\tau^2 - 4\Delta}}{2}$

where
$\tau = trace(A) = a+d$
$\Delta = det(A) = ad - bc$ [Equation 17]

For our two-ODE model, the eigenvalues turn out to be
$\lambda_{1,2} \approx -0.91 \pm 3.30i$.

<a id='bdfd54b1-36d7-4b9b-91e2-3b4dbbd1997a'></a>

"dampens") over time: if the real part of λ is negative, the amplitude of the oscillations will decrease by an exponential decay; and if the real part of λ is positive, the oscillations will grow exponentially over time. The imaginary part of λ (y in [Equation 18]) makes the perturbation oscillate up and down (as sine and cosine functions do). For the parameters that we have chosen for our two-ODE system, we have damped oscillations (the real parts of the eigenvalues are negative, and the imaginary parts are nonzero). And one can show algebraically that, for any choice of parameters, the real parts of the eigenvalues will be negative, and the oscillations will be damped.

<a id='a7354091-2931-4872-bd4d-dcfed6d69748'></a>

So what about our three-ODE model, which did exhibit sustained oscillations? Again, we carry out a linear stability analysis at the steady state of the system (for details, see Box 2). For the choice of parameters that we made above, the eigenvalues are -5.29, 0.88+3.47i, 0.88-3.47i. Therefore, the steady state is unstable because two of the eigenvalues have positive real parts and the system exhibits sustained limit cycle oscillations (Figures 5B and 5C).

<a id='86fa7ab1-a850-4543-b7cd-e326fbc8e8e5'></a>

Summary: **Oscillations in ODE Models of Simple Negative Feedback Loops**
Using examples motivated by the cell cycle, we have shown that a one-ODE model of a simple negative feedback loop cannot oscillate; a two-ODE model can exhibit damped, but not sustained, oscillations; and a three-ODE model can exhibit sustained limit cycle oscillations. Linear stability analysis of the systems' steady states gave us an explanation for why these behaviors are found.

<a id='efa987c4-cebb-450c-9a92-b41f74d56e19'></a>

From this analysis, we conclude that a simple three-ODE negative feedback model seems like a reasonable starting point for describing oscillations in CDK1 activity like those seen in Xenopus embryos. Indeed, some of the earliest models of the

<a id='d729233d-a2a7-45b9-84fb-88a21fe19075'></a>

## Box 2. Obtaining Eigenvalues for the Three-ODE Model

We write the three ODEs as:

$$\frac{dCDK1^*}{dt} = f = \alpha_1 - \beta_1 CDK1^* \frac{APC^{*n1}}{K_1^{n1} + APC^{*n1}}$$ [Equation 19]

$$\frac{dPlk1^*}{dt} = g = \alpha_2(1 - Plk1^*) \frac{CDK1^{*n2}}{K_2^{n2} + CDK1^{*n2}} - \beta_2 Plk1^*$$ [Equation 20]

$$\frac{dAPC^*}{dt} = h = \alpha_3(1 - APC^*) \frac{Plk1^{*n3}}{K_3^{n3} + Plk1^{*n3}} - \beta_3 APC^*$$ [Equation 21]

Next, we set up the Jacobian matrix and calculate the partial derivatives:

$$A = \begin{pmatrix}
\frac{\partial f}{\partial CDK1^*} & \frac{\partial f}{\partial Plk1^*} & \frac{\partial f}{\partial APC^*}\\
\frac{\partial g}{\partial CDK1^*} & \frac{\partial g}{\partial Plk1^*} & \frac{\partial g}{\partial APC^*}\\
\frac{\partial h}{\partial CDK1^*} & \frac{\partial h}{\partial Plk1^*} & \frac{\partial h}{\partial APC^*}
\end{pmatrix}$$ [Equation 22]

Finally, we calculate the three eigenvalues. For the choice of parameters we made in Figure 5, the eigenvalues are -5.29, 0.88+3.47i, 0.88 – 3.47i.

<a id='869bd483-4eff-44ef-bcba-bcb2119bf635'></a>

cell cycle were simple three-ODE negative feedback loops
(Goldbeter, 1991). The ability of a model like this to generate
sustained oscillations depends upon the length of the negative
feedback loop and the amount of ultrasensitivity assumed for
the regulatory interactions within the loop. The longer the loop
and the more switch-like the interactions, the easier it is to
produce oscillations.

<a id='64946bda-0d5b-4802-95e2-6a9245523d98'></a>

## Negative Feedback with a Time Delay
As mentioned above, the mechanism through which CDK1 activates APC is incompletely understood, but it is probably a multistep mechanism with many intermediate species and ample possibility for the introduction of time delays. The same is true for the inactivation of CDK1 by active APC. Given the vagaries of the exact mechanisms, perhaps a reasonable approach would be to leave the formalism of ODEs and make use instead of delay differential equations, in which an explicit time delay relates the change in activity of APC to an earlier activity of CDK1, and vice versa. Consider our two-ODE model (Equations 3 and 4), modified to include two explicit delays, T₁ and T₂:

<a id='4631a7da-0474-43f7-9f25-739bb035f52e'></a>

dCDK1*[t]
--- = α₁ - β₁CDK1*[t] * APC*[t - τ₁]ⁿ¹
dt                     K₁ⁿ¹ + APC1*[t - τ₁]ⁿ¹

[Equation 23]

<a id='e89b81e5-d32a-415c-bfa9-bf48c53fc3e8'></a>

$$\frac{dAPC^*[t]}{dt} = \alpha_2(1 - APC^*[t]) \frac{CDK1^*[t - \tau_2]^{n_2}}{K_2^{n_2} + CDK1^*[t - \tau_2]^{n_2}} - \beta_2APC^*[t]$$

[Equation 24]

<a id='c33eaa61-33d2-4042-af34-954c1c6c2d7c'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc. 881

<!-- PAGE BREAK -->

<a id='57552c7e-a63b-40bb-8439-1005e7a9f1ea'></a>

Cell

<a id='877b352f-a445-4bd1-b13c-bf84bd46c8e7'></a>

<::Figure A shows a diagram of interactions between CDK1 and APC. A red circle labeled "CDK1" and a green circle labeled "APC" are displayed. An arrow labeled "τ2" points from CDK1 to APC, indicating activation or promotion. An arrow labeled "τ1" points from APC to CDK1, with a perpendicular bar indicating inhibition.
Figure B shows a phase portrait with CDK1* on the x-axis (ranging from 0.0 to 1.0) and APC* on the y-axis (ranging from 0.0 to 1.0). There are three lines plotted: a red line labeled "CDK1", a green line labeled "APC", and a black closed loop with an arrow indicating a cyclic trajectory. A small white circle is present near the center of the loop.
Figure C shows a time series plot of activity versus time. The x-axis is "Time" ranging from 0 to 25. The y-axis is "Activity" ranging from 0.0 to 1.0. Two oscillating curves are plotted: a red curve labeled "CDK1" and a green curve labeled "APC". Both curves show periodic fluctuations, with APC peaking shortly after CDK1 activity begins to decline.: chart::>

<a id='5089eb8a-eb9b-48ec-9d54-317933bd40d4'></a>

Figure 7. A Delay Differential Equation
Model of CDK1 and APC Regulation
(A) Schematic of the model. The parameters
chosen for the model were α₁ = 0.1, α₂ = 3, β₁ = 3,
β₂ = 1, K₁ = 0.5, K₂ = 0.5, n₁ = 8, n₂ = 8, τ₁ = 0.5, and
τ₂ = 0.5.

<a id='e7bc4e01-3199-4b27-9650-3a1dd6c31b50'></a>

(B) Phase space depiction of the system. The red and green lines are the nullclines. One trajectory is shown. The initial history for this trajectory was CDK1*[t ≤ 0] = 0, APC[t ≤ 0] = 0. The trajectory spirals in toward a limit cycle.
(C) Time course of the system, showing sustained limit cycle oscillations.

<a id='318ff5f0-9265-4007-aab7-4b92834f08e6'></a>

Here, the rate of change of CDK1 activity at time _t_ depends on APC activity at time _t_– _τ_₁, and the rate of change of APC activity at time _t_ depends on CDK1 activity at time _t_– _τ_₂.

<a id='d48db19b-2c41-449b-860f-b45f04bd99b6'></a>

This two-equation model now yields sustained limit cycle oscillations (Figure 7) once the time delays exceed a fairly small critical value. Even a model of a negative feedback loop with only one delay differential equation can be made to oscillate. The explicit time delays, like the discrete time steps in the Boolean model (Figure 2), help to keep the activities of CDK1 and APC from settling into a stable steady state.

<a id='e254ac89-5c6a-4967-9503-70957d248370'></a>

Delay differential equation models have been used to rationalize the robust oscillations seen in some synthetic biochemical oscillators based on negative feedback loops (Stricker et al., 2008) and have been proposed to model the embryonic cell cycle in Xenopus as well (Busenberg and Tang, 1994).

<a id='fe5d0d6a-a2c5-46dd-8d79-4aed2d77b3a1'></a>

2001; Gardner et al., 2000; Tyson et al., 2003). The term "bista-
ble" means that the system can be in either of two alternative,
stable steady states, depending upon its history, and the term
"hysteretic" means that, once the system has been switched
from one state to the other, it tends to stay there. Indeed, exper-
imental studies have shown that, in Xenopus egg extracts, the
CDK1/Wee1/Cdc25 system does respond to cyclin in a hysteretic
fashion; it is easier to maintain an extract in M phase than it is to
push an interphase extract into M phase (Pomerening et al., 2003;
Sha et al., 2003). Thus, mitosis is driven by a bistable trigger. How
would a bistable trigger alter our simple model of the cell cycle?

<a id='abfda973-122f-41b2-b361-867a73de54d6'></a>

Let us begin again with our two-ODE model (Equations 3
and 4) but now add an additional positive feedback term (Equa-
tion 25, yellow) to the first equation, accounting for the fact that
active CDK1 promotes the formation of more active CDK1 in
a highly nonlinear way:

<a id='86f93849-05dc-4d17-ae58-73922e4815e2'></a>

$$\frac{dCDK1^*}{dt} = \alpha_1 - \beta_1CDK1^* \frac{APC^{n1}}{K_1^{n1} + APC^{n1}} + \alpha_3(1 - CDK1^*) \frac{CDK1^{n3}}{K_3^{n3} + CDK1^{n3}}$$[Equation 25]

<a id='7093c4c9-b67b-45ba-877a-cac80ae0cf78'></a>

## Adding a Bistable Trigger
To this point, we have ignored an important part of the scheme shown in Figure 1, the positive feedback loop (CDK1 activates Cdc25, which in turn activates CDK1) and the double-negative feedback loop (CDK1 inhibits Wee1, which in turn inhibits CDK1). Nevertheless, this is probably a critical part of the network; every eukaryotic species examined so far has at least one identifiable Wee1 homolog, and all eukaryotic species except higher plants have at least one Cdc25 homolog. In addition, genetic studies in S. pombe identified these genes as critical for cell-cycle oscillations (Russell and Nurse, 1986, 1987), although, surprisingly, they become less important in S. pombe strains engineered to run off a single cyclin/Cdk fusion protein (Coudreuse and Nurse, 2010). Biochemical studies in Xenopus egg extracts and gene disruption studies in human HeLa cells also provide evidence that these feedback loops are important for the cell cycle (Pomerening et al., 2005, 2008). What do these positive and double-negative feedback loops add to the oscillator?

<a id='0387bcff-e241-44b2-b2d8-9c7397a3aa84'></a>

On their own, positive or double-negative feedback loops can accomplish several things. For example, they can amplify the magnitude of a signal and can amplify the system's sensitivity to a change in a signal. However, these feedback loops are probably best known for their potential to function as bistable, hysteretic toggle switches (Ferrell, 2002; Ferrell and Xiong,

<a id='aff46e3e-0258-4675-befc-afe88cdc96f7'></a>

dAPC*/dt = α2(1 - APC*) * (CDK1^n2 / (K2^n2 + CDK1^n2)) - β2APC* [Equation 26]

<a id='241eaeb1-0b71-4f96-99a9-aa9372734fb4'></a>

Moreover, we assume that the basal rate of CDK1 activation,
α₁—essentially the cyclin synthesis rate—is slow compared to
the other activation and inactivation rates.

<a id='f1bee787-a127-4b65-bf64-fcc08658354c'></a>

Now, let us examine the system one leg at a time. First, we look at how the steady state _APC*_ activity would vary with _CDK1*_ activity if there were no feedback from APC to CDK1. This dependency is given by the solution of the equation:

<a id='6d388e58-f553-45c0-ae7c-69e4d14fde21'></a>

α₂(1 − APC*) (CDK1*n² / (K₂n² + CDK1*n²)) − β₂APC* = 0 [Equation 27]

<a id='d4464135-3896-4f4b-9fa1-3f5367703aa0'></a>

Equation 27 defines one of the nullclines for the two-ODE system (shown in green in Figure 8B). This nullcline is a monotonic, sigmoidal curve. When CDK1* is low, APC* is low; when CDK1* is high, APC* is high; and in between, APC is intermediate in activity.

<a id='3fb77166-834e-44f6-8a71-59363e1c1d0b'></a>

However, the other nullcline (shown in red in Figure 8B), which describes how the steady-state activity of CDK1 would vary with APC* in the absence of feedback from CDK1 to APC, is qualitatively different. It is not just sigmoidal, it is S shaped. This means that there are three possible steady-state values of CDK1* for

<a id='c26c7b64-231c-4a1b-8cbb-a03691a56d9d'></a>

882

<a id='609e76f3-2570-41e6-a7ca-a69976ad8226'></a>

Cell 144, March 18, 2011 2011 Elsevier Inc.

<!-- PAGE BREAK -->

<a id='3e8db34a-494a-423e-8524-0a07d1f84f6b'></a>

Cell

<a id='4ab299b8-cbfb-4da1-a787-f7fa241b1b3e'></a>

<::Figure 1: Dynamics of CDK1 and APC.Panel A: A schematic diagram illustrating the interactions between CDK1 and APC. A red circle labeled "CDK1" and a green circle labeled "APC" are shown. An arrow points from CDK1 to APC, indicating activation. A blunt-ended arrow points from APC to CDK1, indicating inhibition. A curved blunt-ended arrow points from CDK1 back to itself, indicating self-inhibition.Panel B: A phase plane plot showing APC* activity versus CDK1* activity. The x-axis is labeled "CDK1*" and ranges from 0.0 to 1.0. The y-axis is labeled "APC*" and ranges from 0.0 to 1.0. Two nullclines are plotted:
  - A red line labeled "CDK1" represents the CDK1 nullcline, which starts low, increases, and then decreases. A pink shaded region is beneath part of this curve.
  - A green line labeled "APC" represents the APC nullcline, which starts low, increases, and then flattens out.
  The nullclines intersect at an unstable fixed point. A black trajectory with arrows shows a limit cycle oscillation around this fixed point.Panel C: A time series plot showing the activity of CDK1 and APC over time. The x-axis is labeled "Time" and ranges from 0 to 25. The y-axis is labeled "Activity" and ranges from 0.0 to 1.0. Two oscillating curves are plotted:
  - A red curve labeled "CDK1" shows periodic peaks and troughs.
  - A green curve labeled "APC" shows periodic peaks and troughs, slightly out of phase with CDK1.Below Panel B are two diagrams illustrating the nullclines:
  - Red nullcline: A diagram with a red circle labeled "CDK1" and a green circle labeled "APC". An arrow points from CDK1 to APC (activation). A curved blunt-ended arrow points from CDK1 back to itself (self-inhibition).
  - Green nullcline: A diagram with a red circle labeled "CDK1" and a green circle labeled "APC". A blunt-ended arrow points from APC to CDK1 (inhibition).: figure::>

<a id='a5d602a4-34a8-48f9-b7ac-0399bad0c1de'></a>

Figure 8. Interlinked Positive and Negative
Feedback Loops in a Two-Component
Model of CDK1 and APC Regulation
(A) Schematic of the model. The parameters
chosen for the model were α₁ = 0.02, α₂ = 3, α₂ = 3,
β₁ = 3, β₂ = 1, K₁ = 0.5, K₂ = 0.5, K₃ = 0.5, n₁ = 8,
n₂ = 8, and n₃ = 8.

<a id='a30c212d-8ff5-4ff7-bf9d-fff89d4d8552'></a>

(B) Phase space depiction of the system. The red and green lines are the nullclines. They intersect at an unstable steady state designated by the open circle. All trajectories spiral in or out toward a stable limit cycle, denoted by the closed black loop.
(C) Time course of the system, showing sustained limit cycle oscillations.

<a id='ff170d1a-f2d9-46a2-a804-2d6d8d7b5ffd'></a>

---to evolve or may have particular perfor-mance advantages that make themespecially suitable for biological applica-tions (Holt et al., 2008; Pomerening et al., 2003; Skotheimet al., 2008; Tsai et al., 2008).

<a id='c188d3dd-c2a1-4058-bc2f-b35635ca594a'></a>

a given APC activity when _APC*_ is within a certain range (_APC*_≈ 0.35 to 0.5, shown by pink shading in Figure 8B). By applying linear stability analysis to this one-dimensional system (or rate balance analysis, which is an easier way to analyze the stability of steady states in one-dimensional systems [Ferrell and Xiong, 2001]), one can show that the left and right steady states are stable, and the middle one is an unstable threshold. Thus, we have chosen parameters such that one leg of the CDK1/APC system functions like a hysteretic, bistable toggle switch. As _APC*_ increases, _CDK1*_ decreases toward the edge of a cliff (at _APC*_≈0.5) and then falls precipitously to a very low level. Then, as _APC*_ decreases, _CDK1*_ rises only slightly until _APC*_≈ 0.35, whereupon it shoots sky-high.

<a id='e728637c-6817-4566-9c7b-0e22d8daaab0'></a>

When this toggle switch is coupled to a negative feedback loop, the result can be stable limit cycle oscillations, and for the parameters chosen here, that is what we get (Figures 8B and 8C). CDK1 activity rises slowly at first and then explodes upward toward high mitotic levels. This is followed closely by a rapid rise in APC*, which changes the rapid rise in CDK1* to a similarly precipitous fall. Once CDK1* has fallen enough to turn APC back off, the system begins to slowly ramp up toward its next spike. The oscillations in CDK1 activity shown in Figure 8C look qualitatively similar to those seen in cycling Xenopus egg extracts (Murray and Kirschner, 1989a; Murray et al., 1989; Pomerening et al., 2003) and in HeLa cells in culture (Gavet and Pines, 2010). Accordingly, models that combine positive and negative feedback loops have dominated the cell-cycle modeling field since its beginning (Novak and Tyson, 1993a; Tyson and Kauffman, 1975).

<a id='8ca62b50-33a7-4f36-b5c1-467840674736'></a>

However, the oscillations shown in Figure 8C are qualitatively quite different from the oscillations that we observed from our ODE models of simple negative feedback loops (Figure 4 and Figure 5). The oscillations for the positive-plus-negative feedback model are spiky, not smooth (Figure 8C), and there are distinct slow and fast phases. This is the type of oscillation that is exhibited by pacemaker cells in a beating heart and by dripping water faucets, and it is termed a "relaxation oscillation."

<a id='bc358410-1ad2-41b3-9252-d2d8964941fc'></a>

Biological oscillator circuits often do include positive feedback
loops, arguing that relaxation oscillators may be particularly easy

<a id='ba0d9a16-e75e-4ddc-8d8c-091886e5cce2'></a>

Why can this two-ODE system oscillate, whereas the straight
negative feedback two-ODE system could not? It is because
positive feedback adds a type of time delay to the system,
making the ODE model behave more like a delay differential
equation model. The typical response of a system without posi-
tive feedback is a gradual, progressively slowing approach to
a steady state. In contrast, a system with positive feedback first
simmers and then explodes. This simmering phase is essentially
a time lag, and it facilitates the generation of oscillations.

<a id='c20e2cc3-2fea-4835-b189-f9c2673cd3da'></a>

Accordingly, we expect that the stable steady state seen in the straight negative feedback two-ODE system (Figure 4) must be destabilized in the positive-plus-negative feedback system (Figure 8). Indeed, this is the case. Linear stability analysis yielded eigenvalues of λ1,2 ≈ 0.91 ± 3.30i for the negative feed-back-only system; now, with positive feedback added, the eigenvalues are 1.12 ± 4.77i. The real part of the eigenvalues is positive, so the steady state is unstable; the imaginary part of the eigenvalues is nonzero, so there are oscillations.

<a id='dad19185-3668-4792-9f9e-b9df5211c683'></a>

At this point, we have an oscillator model composed of two ODEs, representing two interlinked feedback loops. By adding more ODEs, the model can be made more realistic. For example, one could divide the process of CDK1 activation into its two most critical steps: the production of cyclin-CDK1 complexes through the synthesis of cyclin and regulation of the complexes' activity through phosphorylation and dephosphorylation. This additional realism comes at the cost of additional complexity; the more ODEs, the harder it is to understand why the system behaves the way that it does.

<a id='9684a44a-10cf-4666-a688-c6c97c377224'></a>

**Conclusion**
The *Xenopus* embryonic cell cycle is driven by a protein circuit that acts like an autonomous oscillator. In this Primer, we set out to explore how oscillations can arise from a protein circuit. We examined three types of models of simple oscillator circuits based on the CDK1/APC system: Boolean models, ordinary differential equation models, and delay differential equation models. The discrete character of Boolean models and the time lags introduced into

<a id='1bb4ce05-e9e1-4a8b-8e09-dde220997abc'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc. 883

<!-- PAGE BREAK -->

<a id='73a06b6e-c00d-4266-b39d-8365ae8f0611'></a>

<::logo: Cell
Cell
A green square with the word "Cell" in white text at the bottom right corner.::>

<a id='25822617-06a6-4017-be06-e737733bcaa9'></a>

delay differential equation models make it relatively easy to generate oscillations. For ODE models, it is more difficult to keep the model from settling into a stable steady state. With everything else equal, longer negative feedback loops are easier to get oscillating than shorter ones, and switch-like, ultrasensitive response functions within the negative feedback loop promote oscillations, as well. Adding a positive feedback loop to a negative feedback loop tends to promote oscillations, and oscillators with this bistable trigger have distinct characteristics that might make them particularly suitable for biological systems.

<a id='72300d58-525e-4705-8bd5-0d9c76396b29'></a>

Linear stability analysis addresses why one ODE model oscil-
lates and another one does not. Accordingly, we have presented
several examples of stability analysis for simple oscillator
circuits. For one-ODE systems, linear stability analysis is fairly
simple. For two or more ODEs, however, one must make use
of matrix algebra manipulations, calculating the eigenvalues of
the system at the steady state(s). This takes some effort, but
the effort is worth it—it provides us with an understanding of
why a circuit does or does not oscillate.

<a id='46521d98-5f91-43dd-a74c-8a0f134b73d1'></a>

In many eukaryotic cells, the cell cycle is driven by a CDK1/
APC circuit that behaves more like a succession of decisions
or contingent events rather than an autonomous oscillator.
Nevertheless, simple models of the _Xenopus_ oscillator, such as
the ones discussed here, provide insight that informs the under-
standing of more complex cell-cycle circuits. Just as positive
feedback loops can provide an oscillator circuit with robustness,
positive feedback loops can be used to build a succession of reli-
able switches. We suspect that the link between clock-like cell
cycles (like the _Xenopus_ embryonic cycle) and domino-like cell
cycles (like the somatic cell cycle) is that they are both con-
structed out of bistable switches.

<a id='d5cd0288-77fc-41bf-ad40-fd069773cb74'></a>

It is clear that the *Xenopus* embryonic cell cycle can operate in the absence of transcription. Therefore, we have regarded the cell-cycle oscillator as only a protein circuit---proteins regulate other proteins, but not gene expression. Nonetheless, many cell-cycle regulators in many cell types undergo periodic transcription (Spellman et al., 1998). Indeed, in budding yeast, transcriptional oscillations persist in the absence of CDK1 oscillations (Haase and Reed, 1999; Orlando et al., 2008). Transcriptional regulation undoubtedly contributes to the overall functioning of the cell-cycle oscillator, with the protein oscillator acting as a basic core circuit upon which additional controls have been layered.

<a id='57870ea1-d6f1-4859-8c4a-0b3a9659a970'></a>

The same may be true of another well-studied biological oscil-lator, the circadian clock. The slow pace of the circadian clock makes it natural to think of the clock as arising from a transcrip-tional gene circuit. Nevertheless, in cyanobacteria (Nakajima et al., 2005; Rust et al., 2007; Tomita et al., 2005), Ostreococcus (O'Neill et al., 2011), and human red blood cells (O'Neill and Reddy, 2011), circadian oscillations can proceed in the absence of transcription. Perhaps core protein circuits constitute the basic circadian clock, with transcriptional circuits reinforcing and refining the clock's behavior (Zwicker et al., 2010).

<a id='e1f52d2b-3394-45de-a61d-c3c565d3eaf2'></a>

In any case, whether one is interested in gene circuits or
protein circuits, and in cell-cycle oscillations or circadian oscilla-
tions, the basic concepts and tools that we have reviewed here—
negative feedback loops, bistable triggers, time lags, and linear
stability analysis—should prove helpful. Our hope is that the
detailed analysis of particular oscillator circuits, coupled with

<a id='c0ed54e5-bce4-4143-b3f0-7dca2060a9ed'></a>

the comparative analysis of different biological oscillators, will allow us to gain insight into the basic design principles of all of these fascinating clocks.

<a id='713916d7-ba9f-413d-b4d4-6e7ea9c962b2'></a>

## ACKNOWLEDGMENTS

We thank Markus Covert for the idea of starting this tutorial with a Boolean analysis instead of plunging right into ODEs and David Dill for helpful discussions. This work was supported by NIH GM077544.

<a id='37c3ce27-bb53-4927-bf09-6ae16a2bba11'></a>

REFERENCES
Aguda, B.D., and Tang, Y. (1999). The kinetic origins of the restriction point in the mammalian cell cycle. Cell Prolif. 32, 321-335.
Alfieri, R., Barberis, M., Chiaradonna, F., Gaglio, D., Milanesi, L., Vanoni, M., Klipp, E., and Alberghina, L. (2009). Towards a systems biology approach to mammalian cell cycle: modeling the entrance into S phase of quiescent fibroblasts after serum stimulation. BMC Bioinformatics 10 (Suppl 12), S16.
Barberis, M., Klipp, E., Vanoni, M., and Alberghina, L. (2007). Cell size at S phase initiation: an emergent property of the G1/S network. PLoS Comput. Biol. 3, e64.
Borisuk, M.T., and Tyson, J.J. (1998). Bifurcation analysis of a model of mitotic control in frog eggs. J. Theor. Biol. 195, 69-85.
Braunewell, S., and Bornholdt, S. (2007). Superstability of the yeast cell-cycle dynamics: ensuring causality in the presence of biochemical stochasticity. J. Theor. Biol. 245, 638-643.
Busenberg, S., and Tang, B. (1994). Mathematical models of the early embryonic cell cycle: the role of MPF activation and cyclin degradation. J. Math. Biol. 32, 573-596.
Charvin, G., Oikonomou, C., Siggia, E.D., and Cross, F.R. (2010). Origin of irreversibility of cell cycle start in budding yeast. PLoS Biol. 8, e1000284.
Chen, K.C., Calzone, L., Csikasz-Nagy, A., Cross, F.R., Novak, B., and Tyson, J.J. (2004). Integrative analysis of cell cycle control in budding yeast. Mol. Biol. Cell 15, 3841-3862.
Ciliberto, A., Novak, B., and Tyson, J.J. (2003). Mathematical model of the morphogenesis checkpoint in budding yeast. J. Cell Biol. 163, 1243-1254.
Coudreuse, D., and Nurse, P. (2010). Driving the cell cycle with a minimal CDK control network. Nature 468, 1074-1079.
Dasso, M., and Newport, J.W. (1990). Completion of DNA replication is monitored by a feedback system that controls the initiation of mitosis in vitro: studies in Xenopus. Cell 61, 811-823.
Davidich, M.I., and Bornholdt, S. (2008). Boolean network model predicts cell cycle sequence of fission yeast. PLoS One 3, e1672.
Ferrell, J.E., Jr. (2002). Self-perpetuating states in signal transduction: positive feedback, double-negative feedback and bistability. Curr. Opin. Cell Biol. 14, 140-148.
Ferrell, J.E., Jr., and Xiong, W. (2001). Bistability in cell signaling: How to make continuous processes discontinuous, and reversible processes irreversible. Chaos 11, 227-236.
Gardner, T.S., Cantor, C.R., and Collins, J.J. (2000). Construction of a genetic toggle switch in Escherichia coli. Nature 403, 339-342.
Gavet, O., and Pines, J. (2010). Progressive activation of CyclinB1-Cdk1 coordinates entry to mitosis. Dev. Cell 18, 533-543.
Ge, H., Qian, H., and Qian, M. (2008). Synchronized dynamics and non-equilibrium steady states in a stochastic yeast cell-cycle network. Math. Biosci. 211, 132-152.
Gilbert, D.A. (1974). The nature of the cell cycle and the control of cell proliferation. Curr. Mod. Biol. 5, 197-206.
Glass, L., and Kauffman, S.A. (1973). The logical analysis of continuous, non-linear biochemical control networks. J. Theor. Biol. 39, 103-129.
Goldbeter, A. (1991). A minimal cascade model for the mitotic oscillator involving cyclin and cdc2 kinase. Proc. Natl. Acad. Sci. USA 88, 9107-9111.

<a id='7a363cdf-c3dc-44c9-9bb8-7940918ef4e2'></a>

884

<a id='d5651bc0-e7f7-4de2-be00-79d27b99d395'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc.

<!-- PAGE BREAK -->

<a id='7f86e883-e92f-41c0-9447-6b0ed8e66076'></a>

Cell

<a id='a9098d67-d86b-4573-9a3a-31f819640b91'></a>

Goldbeter, A. (2002). Computational approaches to cellular rhythms. Nature 420, 238-245.
Goldbeter, A., and Guilmot, J.M. (1996). Arresting the mitotic oscillator and the control of cell proliferation: insights from a cascade model for cdc2 kinase activation. Experientia 52, 212-216.
Haase, S.B., and Reed, S.I. (1999). Evidence that a free-running oscillator drives G1 events in the budding yeast cell cycle. Nature 401, 394-397.
Hara, K., Tydeman, P., and Kirschner, M. (1980). A cytoplasmic clock with the same period as the division cycle in Xenopus eggs. Proc. Natl. Acad. Sci. USA 77, 462-466.
Hartwell, L.H., and Weinert, T.A. (1989). Checkpoints: controls that ensure the order of cell cycle events. Science 246, 629-634.
Holt, L.J., Krutchinsky, A.N., and Morgan, D.O. (2008). Positive feedback sharpens the anaphase switch. Nature 454, 353-357.
Kauffman, S., and Wille, J.J. (1975). The mitotic oscillator in Physarum polycephalum. J. Theor. Biol. 55, 47-93.
Li, B., Shao, B., Yu, C., Ouyang, Q., and Wang, H. (2010). A mathematical model for cell size control in fission yeast. J. Theor. Biol. 264, 771-781.
Li, F., Long, T., Lu, Y., Ouyang, Q., and Tang, C. (2004). The yeast cell-cycle network is robustly designed. Proc. Natl. Acad. Sci. USA 101, 4781-4786.
Mangla, K., Dill, D.L., and Horowitz, M.A. (2010). Timing robustness in the budding and fission yeast cell cycles. PLoS ONE 5, e8906.
Minshull, J., Sun, H., Tonks, N.K., and Murray, A.W. (1994). A MAP kinase-dependent spindle assembly checkpoint in Xenopus egg extracts. Cell 79, 475-486.
Mura, I., and Csikász-Nagy, A. (2008). Stochastic Petri Net extension of a yeast cell cycle model. J. Theor. Biol. 254, 850-860.
Murray, A.W., and Kirschner, M.W. (1989a). Cyclin synthesis drives the early embryonic cell cycle. Nature 339, 275-280.
Murray, A.W., and Kirschner, M.W. (1989b). Dominoes and clocks: the union of two views of the cell cycle. Science 246, 614-621.
Murray, A.W., Solomon, M.J., and Kirschner, M.W. (1989). The role of cyclin synthesis and degradation in the control of maturation promoting factor activity. Nature 339, 280-286.
Nakajima, M., Imai, K., Ito, H., Nishiwaki, T., Murayama, Y., Iwasaki, H., Oyama, T., and Kondo, T. (2005). Reconstitution of circadian oscillation of cyanobacterial KaiC phosphorylation in vitro. Science 308, 414-415.
Norel, R., and Agur, Z. (1991). A model for the adjustment of the mitotic clock by cyclin and MPF levels. Science 251, 1076-1078.
Novak, B., Csikasz-Nagy, A., Gyorffy, B., Chen, K., and Tyson, J.J. (1998). Mathematical model of the fission yeast cell cycle with checkpoint controls at the G1/S, G2/M and metaphase/anaphase transitions. Biophys. Chem. 72, 185-200.
Novak, B., and Tyson, J.J. (1993a). Modeling the cell division cycle: M-phase trigger, oscillations, and size control. J. Theor. Biol. 165, 101-134.
Novak, B., and Tyson, J.J. (1993b). Numerical analysis of a comprehensive model of M-phase control in Xenopus oocyte extracts and intact embryos. J. Cell Sci. 106, 1153-1168.
Novak, B., and Tyson, J.J. (1997). Modeling the control of DNA replication in fission yeast. Proc. Natl. Acad. Sci. USA 94, 9147-9152.
Novák, B., and Tyson, J.J. (2008). Design principles of biochemical oscillators. Nat. Rev. Mol. Cell Biol. 9, 981-991.
O'Neill, J.S., and Reddy, A.B. (2011). Circadian clocks in human red blood cells. Nature 469, 498-503.
O'Neill, J.S., van Ooijen, G., Dixon, L.E., Troein, C., Corellou, F., Bouget, F.Y., Reddy, A.B., and Millar, A.J. (2011). Circadian rhythms persist without transcription in a eukaryote. Nature 469, 554-558.
Obeyesekere, M.N., Tucker, S.L., and Zimmerman, S.O. (1992). Mathematical models for the cellular concentrations of cyclin and MPF. Biochem. Biophys. Res. Commun. 184, 782-789.
Okabe, Y., and Sasai, M. (2007). Stable stochastic dynamics in yeast cell cycle. Biophys. J. 93, 3451-3459.

<a id='9e369125-341f-41d6-b40d-89ab93bc3b75'></a>

Orlando, D.A., Lin, C.Y., Bernard, A., Wang, J.Y., Socolar, J.E., Iversen, E.S., Hartemink, A.J., and Haase, S.B. (2008). Global control of cell-cycle transcription by coupled CDK and network oscillators. Nature 453, 944-947.
Pomerening, J.R., Kim, S.Y., and Ferrell, J.E., Jr. (2005). Systems-level dissection of the cell-cycle oscillator: bypassing positive feedback produces damped oscillations. Cell 122, 565-578.
Pomerening, J.R., Sontag, E.D., and Ferrell, J.E., Jr. (2003). Building a cell cycle oscillator: hysteresis and bistability in the activation of Cdc2. Nat. Cell Biol. 5, 346-351.
Pomerening, J.R., Ubersax, J.A., and Ferrell, J.E., Jr. (2008). Rapid cycling and precocious termination of G1 phase in cells expressing CDK1AF. Mol. Biol. Cell 19, 3426-3441.
Russell, P., and Nurse, P. (1986). cdc25+ functions as an inducer in the mitotic control of fission yeast. Cell 45, 145-153.
Russell, P., and Nurse, P. (1987). Negative regulation of mitosis by wee1+, a gene encoding a protein kinase homolog. Cell 49, 559-567.
Rust, M.J., Markson, J.S., Lane, W.S., Fisher, D.S., and O'Shea, E.K. (2007). Ordered phosphorylation governs oscillation of a three-protein circadian clock. Science 318, 809-812.
Sel'kov, E.E. (1970). [2 alternative autooscillatory stationary states in thiol metabolism-2 alternative types of cell multiplication: normal and neoplastic]. Biofizika 15, 1065-1073.
Sha, W., Moore, J., Chen, K., Lassaletta, A.D., Yi, C.S., Tyson, J.J., and Sible, J.C. (2003). Hysteresis drives cell-cycle transitions in Xenopus laevis egg extracts. Proc. Natl. Acad. Sci. USA 100, 975-980.
Skotheim, J.M., Di Talia, S., Siggia, E.D., and Cross, F.R. (2008). Positive feedback of G1 cyclins ensures coherent cell cycle entry. Nature 454, 291-296.
Spellman, P.T., Sherlock, G., Zhang, M.Q., Iyer, V.R., Anders, K., Eisen, M.B., Brown, P.O., Botstein, D., and Futcher, B. (1998). Comprehensive identification of cell cycle-regulated genes of the yeast Saccharomyces cerevisiae by microarray hybridization. Mol. Biol. Cell 9, 3273-3297.
Srividhya, J., and Gopinathan, M.S. (2006). A simple time delay model for eukaryotic cell cycle. J. Theor. Biol. 241, 617-627.
Steuer, R. (2004). Effects of stochasticity in models of the cell cycle: from quantized cycle times to noise-induced oscillations. J. Theor. Biol. 228, 293-301.
Stricker, J., Cookson, S., Bennett, M.R., Mather, W.H., Tsimring, L.S., and Hasty, J. (2008). A fast, robust and tunable synthetic gene oscillator. Nature 456, 516-519.
Strogatz, S.H. (1994). Nonlinear dynamics and chaos: with applications to physics, biology, chemistry, and engineering (Cambridge, MA: Westview Press).
Tomita, J., Nakajima, M., Kondo, T., and Iwasaki, H. (2005). No transcription-translation feedback in circadian rhythm of KaiC phosphorylation. Science 307, 251-254.
Tsai, T.Y., Choi, Y.S., Ma, W., Pomerening, J.R., Tang, C., and Ferrell, J.E., Jr. (2008). Robust, tunable biological oscillations from interlinked positive and negative feedback loops. Science 321, 126-129.
Tyson, J.J. (1991). Modeling the cell division cycle: cdc2 and cyclin interactions. Proc. Natl. Acad. Sci. USA 88, 7328-7332.
Tyson, J., and Kauffman, S. (1975). Control of mitosis by a continuous biochemical oscillation: Synchronization; spatially inhomogeneous oscillations. J. Math. Biol. 1, 289-310.
Tyson, J.J., Chen, K.C., and Novak, B. (2003). Sniffers, buzzers, toggles and blinkers: dynamics of regulatory and signaling pathways in the cell. Curr. Opin. Cell Biol. 15, 221-231.
Yao, G., Lee, T.J., Mori, S., Nevins, J.R., and You, L. (2008). A bistable Rb-E2F switch underlies the restriction point. Nat. Cell Biol. 10, 476-482.
Zhang, Y., Qian, M., Ouyang, Q., Deng, M., Li, F., and Tang, C. (2006). A stochastic model of the yeast cell cycle network. Physica. D 219, 35-39.
Zwicker, D., Lubensky, D.K., and ten Wolde, P.R. (2010). Robust circadian clocks from coupled protein-modification and transcription-translation cycles. Proc. Natl. Acad. Sci. USA 107, 22540-22545.

<a id='d1d854e9-38db-421f-837d-ecf91ef0e26e'></a>

Cell 144, March 18, 2011 ©2011 Elsevier Inc. 885