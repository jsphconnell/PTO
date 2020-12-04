import os

EvoCOP_results_dir = "EvoCOP_results_joe"
EvoCOP_results_output_filename = "EvoCOP_results_joe.dat"
assert not os.path.exists(EvoCOP_results_output_filename)

outfile = open(EvoCOP_results_output_filename, "w")

for filename in os.listdir(EvoCOP_results_dir):
    with open(os.path.join(EvoCOP_results_dir, filename), 'r') as f:  # open in readonly mode
        line = f.read()
        outfile.write(line)
    f.close()

outfile.close()