###Valuation of the error coming from the Simulation Step###

# in order to count how many Antimony have been simulated after the conversion step ##

import pandas as pd

Error_file = snakemake.input[0]
out_csv = snakemake.output[0]


def evaluating_error(Error, output):

    with open(Error, "r") as f:

        content = f.read()

    value = 0 if not content else 1

    df = pd.DataFrame({"second Simulation": [value]})

    df.to_csv(output, index=False)

    return output

evaluation = evaluating_error(Error_file, out_csv)


            




