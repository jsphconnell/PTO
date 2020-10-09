import os

GE_results_dir = "GE_results"
GE_results_output_filename = "GE_results.dat"
assert not os.path.exists(GE_results_output_filename)

outfile = open(GE_results_output_filename, "w")

for filename in os.listdir(GE_results_dir):
    with open(os.path.join(GE_results_dir, filename), 'r') as f:  # open in readonly mode
        line = f.read()
        outfile.write(line)
    f.close()

outfile.close()
