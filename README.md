# SBMLLM-Bench: from scientific literature to executable Systems Biology models

Systems Biology models are often described across equations, figures, tables, supplementary materials, and previous publications. Building them manually requires substantial biological and mathematical expertise.

**SBMLLM** was developed to accelerate this process: starting from **one or multiple scientific papers**, it can support the creation of a new executable model from scratch or the extension of an existing model. **SBMLLM-Bench** is the reproducible benchmark we use to quantify how well this automated approach performs.

> ### Need a new Systems Biology Model?
>
> Before rebuilding the knowledge contained in the literature manually, contact us:
> **[bioinformatics@cosbi.eu](mailto:bioinformatics@cosbi.eu)** · **[COSBI website and contact information](https://www.cosbi.eu/contact)**

## Table of contents

- [What can SBMLLM achieve?](#what-can-sbmllm-achieve)
- [Quick start](#quick-start)
- [Input data](#input-data)
- [Fabric patterns](#fabric-patterns)
- [Performance metrics](#performance-metrics)
- [Output](#output)

---

# What can SBMLLM achieve?

SBMLLM-Bench evaluates automatically generated models against expert-curated Systems Biology Models.

## Automated model generation

The best-performing configuration, **gemini-3.0-pro**, generated executable models for about **97% of papers**, recovered **86.95% of species** and **85.73% of reactions**, and reproduced the dynamics of **34.5% of models** according to the AAFE criterion.

![SBMLLM average performance](figures/radar_all_llms_raw_latest_inputR.png)

**Figure 1. SBMLLM average performance at automated model replication.** Performance differs substantially across LLMs, including models from the same provider.

## Use all available scientific evidence

A Systems Biology Model is rarely completely described in a single article. Important equations, parameters, assumptions, and experimental details may instead appear in supplementary information or related publications.

You can collect and convert these sources manually before using SBMLLM.

At **COSBI**, we already maintain a literature resource containing papers and their supplementary information in **Markdown format**, ready to be searched and used to inform a new Systems Biology Model. This allows information from multiple publications to be brought together without preparing every document individually.

The benchmark demonstrates the importance of this additional information: average dynamical reproducibility decreased from **23.3% to 8.7%** when supplementary materials were unavailable.

![Effect of supplementary materials](figures/aafe_input_R_suppl_yes_no.png)

**Figure 2. Supplementary materials contain crucial information.** Average reproducibility decreased from 23.3% to 8.7% when supplementary information was not available.

If you have a biological system or one or more relevant publications in mind, COSBI can use these literature resources together with **SBMLLM and expert curation** to create a new Systems Biology Model or extend an existing one.

---

# Quick start

The current workflow is configured for **Windows/PowerShell**.

## 1. Clone

```powershell
git clone https://github.com/cosbi-research/SBMLLM-Bench.git
cd SBMLLM-Bench
```

## 2. Create the environment with Mamba

```powershell
mamba env create -n sbmllm-bench -f env.yml
mamba activate sbmllm-bench
```

Check Snakemake:

```powershell
snakemake --version
```

## 3. Configure Fabric

SBMLLM-Bench uses [Fabric](https://github.com/danielmiessler/fabric) to communicate with the LLM.

See the [Fabric documentation](https://github.com/danielmiessler/fabric/blob/main/README.md) for installation and provider configuration.

```powershell
fabric --setup
fabric --listmodels
```

The workflow requires two patterns:

```text
Converter
Editor
```

Confirm that they are installed:

```powershell
fabric --listpatterns
```

## 4. Run

Check the workflow:

```powershell
snakemake -n
```

Then execute it:

```powershell
snakemake --cores 1
```

Start with one core to keep LLM requests sequential. Increase the number of cores according to your provider's rate limits.

---

# Input data

Each benchmark case requires:

```text
workdir/input_R/<paper>.md
workdir/expected_output_R/or<paper>.txt
workdir/SpeciesMap/<paper>_speciesMap.csv
```

### Publication

`workdir/input_R/<paper>.md`

The publications distributed with SBMLLM-Bench were converted to Markdown using **Landing.AI Agentic Document Extraction (ADE)**.

### Reference model

`workdir/expected_output_R/or<paper>.txt`

Expert-curated Antimony model used as the reference.

### Species map

`workdir/SpeciesMap/<paper>_speciesMap.csv`

Maps biologically equivalent species names between generated and reference models.

> Want to add a biological system that is not included in the benchmark?
>
> COSBI can build a **new Systems Biology Model from scratch** or **extend an existing model**, using evidence from one or multiple publications and supplementary sources.
>
> **[bioinformatics@cosbi.eu](mailto:bioinformatics@cosbi.eu)** · **[Contact COSBI](https://www.cosbi.eu/contact)**

---

# Fabric patterns

SBMLLM-Bench separates model generation from model repair.

## `Converter`

Receives the scientific paper and returns an Antimony model.

```markdown
# IDENTITY AND PURPOSE

You are an expert systems biologist.

Reconstruct the mathematical model described in the supplied scientific paper.

# INSTRUCTIONS

- Identify species, reactions, compartments, parameters and initial conditions.
- Recover kinetic laws and stoichiometry where available.
- Reconstruct the model described by the authors.
- Do not invent unsupported mechanisms.
- Produce valid executable Antimony.

# OUTPUT INSTRUCTIONS

Return only the Antimony model.
Do not include explanations or Markdown code fences.
```

The workflow calls:

```powershell
fabric -s -p Converter
```

## `Editor`

If simulation fails, the current model and the error are passed to the `Editor`:

```text
<CURRENT ANTIMONY MODEL>

==SIMULATION ERROR==

<ERROR MESSAGE>
```

Example:

```markdown
# IDENTITY AND PURPOSE

You are an expert Antimony model debugger.

Correct the supplied model using the simulation error.

# INSTRUCTIONS

- Fix syntax, undefined symbols, malformed reactions or execution errors.
- Preserve the biological structure whenever possible.
- Return the complete corrected model.

# OUTPUT INSTRUCTIONS

Return only valid Antimony.
Do not include explanations or Markdown code fences.
```

The workflow permits up to **two repair attempts**.

---

# Performance metrics

| Metric | Meaning | Better |
|---|---|---:|
| **1st simulation ratio** | Executable directly after generation | Higher |
| **2nd simulation ratio** | Executable after one repair | Higher |
| **3rd simulation ratio** | Executable after two repairs | Higher |
| **Species %** | Reference species recovered | Higher |
| **Arrow %** | Correct reactants, products and reaction direction | Higher |
| **Reaction %** | Reactions also matching stoichiometry | Higher |
| **Hamming distance** | Structural disagreement | Lower |
| **RMSRE** | Error in stoichiometric coefficients | Lower |
| **AAFE reproducibility** | Models reproducing reference dynamics | Higher |

## What is AAFE?

**AAFE (Absolute Average Fold Error)** measures how closely a generated simulation follows the dynamics of the reference model.

For a reference trajectory \(R_i\) and generated trajectory \(G_i\), SBMLLM-Bench computes:

\[
AAFE =
10^{
\frac{1}{n}
\sum_{i=1}^{n}
\left|
\log_{10}
\left(
\frac{G_i}{R_i}
\right)
\right|
}
\]

The comparison is therefore based on **fold difference**, rather than the ordinary numerical distance between the two curves.

- **AAFE = 1** means perfect agreement.
- **AAFE = 2** corresponds to an average two-fold discrepancy.
- **AAFE ≤ 2** is considered reproducible by SBMLLM-Bench.
- Higher values indicate increasingly different simulated dynamics.

The shaded region in the figure below visually highlights where the generated and ground-truth trajectories differ. The arrows show examples of these differences at individual time points. AAFE summarizes these deviations across the complete trajectory using their **relative fold difference**.

![AAFE difference](figures/aafe_difference.png)

**Figure 3. Illustration of the AAFE comparison.** Ground-truth and generated trajectories are compared at corresponding simulation time points. The shaded region highlights their separation, while AAFE summarizes the multiplicative discrepancy across the full time series. SBMLLM-Bench considers a shared trajectory reproducible when **AAFE ≤ 2**.

For each generated model, the benchmark compares variables that are present in both the generated and reference simulations. A model passes the AAFE reproducibility criterion when **at least one shared variable has AAFE ≤ 2**.

---

## Creativity and dynamical reproducibility

We also tested two creativity configurations:

- **lower creativity:** temperature `0.7`, Top-P `0.9`
- **higher creativity:** temperature `1.0`, Top-P `1.0`

Across the four models shown below, **lower creativity consistently increased the proportion of papers satisfying AAFE ≤ 2**. The magnitude of the improvement varied by LLM, with the largest visible gain for `deepseek-reasoner`.

![AAFE by creativity](figures/aafe_by_creativity.png)

**Figure 4. AAFE reproducibility under two creativity settings on 75 reproducible papers.** Lower creativity (`T=0.7, p=0.9`) produced a higher AAFE success rate for all four evaluated LLMs. The effect is model-dependent and is substantially larger for some models than others.

## Creativity and executable models

The effect of creativity on **simulation success** is much smaller.

Both creativity settings produced very similar executability rates for the strongest models. `gpt-5.2-pro` and `gemini-3.0-pro` generated executable models for approximately **96–97%** of the 75 papers after three attempts. `deepseek-reasoner` reached approximately **82%**, while `gemini-2.5-pro` was below **70%**.

Importantly, there is no single creativity setting that improves simulation success for every model: the differences are small and model-specific.

![Simulation success by creativity](figures/simulation_success_by_creativity.png)

**Figure 5. Simulation success after three attempts under two creativity settings.** Creativity has relatively little effect on executability for the highest-performing LLMs. The results suggest that newer, stronger models are less sensitive to this parameter for producing models that can be successfully executed.

---

# Output

The main benchmark result is:

```text
workdir/test_table.csv
```

It summarizes executability, species and reaction recovery, stoichiometric accuracy, dynamical reproducibility, and model size.