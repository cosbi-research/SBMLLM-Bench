import re
import os
import pandas as pd

### Snakemake ###
in_file = snakemake.input[0]
out_file = snakemake.output[0]


# Evaluation of the number of reactions,floating species, boundary species, compartments and Global parameters by RegEx:

rere = re.compile(r"""^\s*(?:(?P<id>[A-Za-z_]\w*)(?:\s+in\s+(?P<comp>[A-Za-z_]\w*))?\s*:)?\s*(?P<lhs>[^;\r\n]*?)\s*(?P<arrow><->|->|=>)\s*(?P<rhs>[^;\r\n]*?)\s*;\s*(?P<rate>[^;\r\n]*\S[^;\r\n]*)\s*$""", re.X)

reboundarysp = re.compile(r"(?:(?<=species\s)|(?<=,\s))(\$\w+)(?=\sin\s[A-Za-z0-9_.]+)")

refloatsp = re.compile(r"(?:(?<=species\s)|(?<=,\s))(?<!\$)\b([A-Za-z0-9_.]+)\b(?=\s+in\s+[A-Za-z0-9_.]+)", re.X)

reCompart = re.compile(r"(?<=compartment\s)\b[a-zA-Z0-9_]+(?=,|;)|(?<=,\s)\b[a-zA-Z0-9_]+(?=;\n\s*compartment\s)|(?<=,\s)\b[a-zA-Z0-9_]+(?=;\n\s*species)", re.X)

reparams = re.compile(r".*\s=\s.*|//\sSpecies|//\sCompart|//\sVariable|//\sOther", re.X)

revarparams = re.compile(r"(?<=\bvar\b).*", re.X)

with open(in_file) as f:
    text = f.read()

Boundsp = re.findall(reboundarysp, text)
Floatsp = re.findall(refloatsp, text)
Comps = re.findall(reCompart, text)
all_init = reparams.findall(text)
var_par = revarparams.findall(text)

Total_species = int(len(Floatsp)) + int(len(Boundsp))

# Extraction of indexes to obtain the variable parameters
if "// Variable" in all_init:
     value1 = all_init.index("// Variable")
else:
     value1 = -1

if "// Other" in all_init:
     value2 = all_init.index("// Other")
else:
     value2 = -1

# initialize params safely
params = []

if value1 != -1 and value2 != -1 and value2 > value1:
     #both markers exist and in correct order
     for k in all_init[value1+1:value2]:
        cleaned = k.strip(" ;")
        params.append(cleaned)
else:
     # One or both markers are missing (or order is invalid)
     params = []

# Build variable List
variables = [item.strip(" ;") for s in var_par for item in s.split(",")]

# Final list of Global Parameters = params list + variable list 

final_param = params + variables
  
# Extraction of the reactions
                
reactions = []

with open(in_file) as f:
    for l in f:
            p1=rere.search(l)
            if p1 is not None:
                reactions.append(p1.group())
            

# table creation: => antimony_model | num Boundary sp. | num Floating sp | num reactions | num Compartments |

data= {
     "N° Species (Bound&Float)": Total_species,
     "N° Reactions": len(reactions),
     "N° Compartments":len(Comps),
     "N° Glob.Parameters": len(final_param),
}

filename = os.path.basename(in_file)

df = pd.DataFrame(data, index=[filename])

# Output CSV 

df.to_csv(out_file)

          