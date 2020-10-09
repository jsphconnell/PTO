import os

TSP_results_dir = "TSP_results"
TSP_results_output_filename = "TSP_results.dat"
assert not os.path.exists(TSP_results_output_filename)

outfile = open(TSP_results_output_filename, "w")

for filename in os.listdir(TSP_results_dir):
    with open(os.path.join(TSP_results_dir, filename), 'r') as f:  # open in readonly mode
        line = f.read()
        outfile.write(line)
    f.close()

outfile.close()
