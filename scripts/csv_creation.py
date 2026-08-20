import os
import shutil
import pandas as pd
import traceback
import tellurium as te
from pathlib import Path

### Snakemake ###
in_file = snakemake.input[0]
out_file = snakemake.output.result
final_model = snakemake.output.final_model
sample = snakemake.params.file

### generating_csv function to obtain the final csv for each model ###

def generating_csv(file, filename, table, final_path):
    
    data = {
          "filename": filename,
          "simulation": True,
          "error": ""
    }
    
    try:
        with open(file, "r") as f:
                antimony_str = f.read()

                rr = te.loadAntimonyModel(antimony_str)
                result = rr.simulate(0, 100, 200)

                data["simulation"] = True
                data["error"] = ""
        
    except Exception:
            data["simulation"] = False
            data["error"] = traceback.format_exc()

    pd.DataFrame([data]).to_csv(table, index=False)
    
    # copy the final models in the last repo.
    
    shutil.copy(in_file, final_path)
    
    return table, final_path


validation = generating_csv(in_file, sample, out_file, final_model)



