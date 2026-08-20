import shutil
import traceback
import tellurium as te

input_file = snakemake.input[0]
output_file = snakemake.output[0]
output_file2 = snakemake.output[1]

# Simulation and generation of the error for each model

def simulate_and_check(input, output):
    
    success = True
    error_message = ""

    try:
        with open(input, "r") as f:
            antimony_str = f.read()

        rr = te.loadAntimonyModel(antimony_str)
        rr.simulate(0,100,200)

        success = True
        error_message = ""


    except Exception as e:
        success = False
        error_message = traceback.format_exc()
    

    if success == True:
            with open(output, "w") as err:
                err.write(error_message)
    else:
        with open(output, "w") as err:
             err.write(error_message)

    return output

success = simulate_and_check(input_file, output_file)    

# copying the file inside the "simulated" repository, to work on that

shutil.copy(input_file, output_file2)




