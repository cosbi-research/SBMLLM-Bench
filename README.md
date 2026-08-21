# SBMLLM-Bench: from scientific literature to executable Systems Biology models

Systems Biology models are often described across equations, figures, tables, supplementary materials, and previous publications. Building them manually requires substantial biological and mathematical expertise.

**SBMLLM** was developed to accelerate this process: starting from **one or multiple scientific papers**, it can support the creation of a new executable model from scratch or the extension of an existing model. **SBMLLM-Bench** is the reproducible benchmark we use to quantify how well this automated approach performs.

> ### Need a new Systems Biology Model?
>
> Before rebuilding the knowledge contained in the literature manually, **contact us** @ [bioinformatics@cosbi.eu](mailto:bioinformatics@cosbi.eu) · [COSBI website and contact information](https://www.cosbi.eu/)  
>

## Table of contents

- [What can SBMLLM achieve?](#what-can-sbmllm-achieve)
- [Quick start](#quick-start)
- [Input data](#input-data)
- [Fabric patterns](#fabric-patterns)
- [Performance metrics](#performance-metrics)
- [Output](#output)

---

# What can SBMLLM achieve?

SBMLLM-Bench evaluates automated model generation against expert-curated reference models.

The benchmark shows that modern LLMs can already recover a substantial part of a published Systems Biology Model and, in many cases, generate an executable implementation.

## Automated model generation

The best-performing configuration, **gemini-3.0-pro**, generated executable models for about **97% of papers**, extracted **86.95% of species** and **85.73% of reactions**, and reproduced the dynamics of **34.5% of models** according to the benchmark AAFE criterion.

[![SBMLLM average performance](figures/radar_all_llms_raw_latest_inputR.png)](figures/radar_all_llms_raw_latest_inputR.png)

**Figure 1. SBMLLM average performance at automated model replication.** Among the evaluated configurations, gemini-3.0-pro generated executable models for ~97% of papers, recovered 86.95% of species and 85.73% of reactions, and achieved 34.5% dynamical reproducibility.

## Use all the available scientific evidence

A Systems Biology Model is rarely fully described in a single article. Important equations, parameter values, assumptions, and experimental details may be distributed across supplementary files or earlier publications.

You can collect and convert these documents manually before using SBMLLM.

At [**COSBI**](https://www.cosbi.eu/contact), however, we already maintain a literature resource in which **papers and their supplementary information are available in Markdown format**, ready to be searched and used as evidence when informing a new Systems Biology Model. This makes it possible to bring together information from multiple publications without having to prepare each document individually.

The benchmark results show why this matters: average dynamical reproducibility decreased from **23.3% to 8.7%** when supplementary materials were unavailable.

[![Effect of supplementary materials](figures/aafe_input_R_suppl_yes_no.png)](figures/aafe_input_R_suppl_yes_no.png)

**Figure 2. Supplementary materials contain crucial information.** Average reproducibility decreased from 23.3% to 8.7% when supplementary materials were not accessible across the evaluated LLMs.

If you already know the biological system you want to model, or have one or more relevant publications, **you do not need to collect and prepare the entire literature yourself**.

COSBI can use its existing literature resources together with SBMLLM and expert curation to build it.

---

# Quick start

The current workflow is configured for **Windows/PowerShell**.

## 1. Clone

```powershell id="w9mat1"
git clone https://github.com/cosbi-research/SBMLLM-Bench.git
cd SBMLLM-Bench
```

## 2. Create the environment with Mamba

```powershell id="4gmvce"
mamba env create -n sbmllm-bench -f env.yml
mamba activate sbmllm-bench
```

Check Snakemake:

```powershell id="2ega85"
snakemake --version
```

## 3. Configure Fabric

SBMLLM-Bench uses [Fabric](https://github.com/danielmiessler/fabric) to communicate with the LLM.

See the [Fabric documentation](https://github.com/danielmiessler/fabric/blob/main/README.md) for installation and provider configuration.

```powershell id="6w4ats"
fabric --setup
fabric --listmodels
```

The workflow requires two patterns:

```text id="rzae0p"
Converter
Editor
```

Confirm that they are installed:

```powershell id="wbrpbt"
fabric --listpatterns
```

## 4. Run

Check the workflow first:

```powershell id="mm9zxo"
snakemake -n
```

Then execute it:

```powershell id="21qmu7"
snakemake --cores 1
```

Start with one core to keep LLM requests sequential. Increase the number of cores according to the rate limits of your provider.

---

# Input data

Each benchmark case requires:

```text id="nfi4bx"
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
> [bioinformatics@cosbi.eu](mailto:bioinformatics@cosbi.eu) · [Contact COSBI](https://www.cosbi.eu/contact)

---

# Fabric patterns

SBMLLM-Bench separates **model generation** from **model repair**.

## `Converter`

Receives the scientific paper and returns an Antimony model.

```markdown id="pn8gnd"
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

Used by the workflow as:

```powershell id="62kb92"
fabric -s -p Converter
```

## `Editor`

Receives a model that failed simulation together with its error:

```text id="4jaapv"
<CURRENT ANTIMONY MODEL>

==SIMULATION ERROR==

<ERROR MESSAGE>
```

Example pattern:

```markdown id="py6xpj"
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

## Prompt settings also matter

Reducing creativity from `(1, 1)` to `(0.7, 0.9)` increased average performance by approximately **8%** and reduced stochasticity by **0.7%**, although the effect was not statistically significant (`p > 0.25`).

[![AAFE by creativity](figures/aafe_by_creativity.png)](figures/aafe_by_creativity.png)

**Figure 3. Effect of creativity on reproducibility.** Lower creativity improved average performance and reduced stochasticity in these experiments, although the observed difference was not statistically significant.

After three generation/repair attempts, the top-performing LLMs generated executable models for approximately **95% of papers**.

[![Simulation success by creativity](figures/simulation_success_by_creativity.png)](figures/simulation_success_by_creativity.png)

**Figure 4. Generation of executable models.** After three attempts, top-performing LLMs convert approximately 95% of papers into executable Systems Biology models. The influence of creativity tends to decrease for newer models.

---

# Output

The main benchmark result is:

```text id="tnfelp"
workdir/test_table.csv
```

It summarizes executability, species and reaction recovery, stoichiometric accuracy, dynamical reproducibility, and model size.
