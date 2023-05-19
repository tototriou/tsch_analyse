import argparse
import os
import subprocess
import shutil
from glob import glob

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", type=int, help="Experiment ID")
parser.add_argument("-n", "--num-graphs", type=int, default=None, help="Num$args = parser.parse_args()

# Get experiment ID and number of graphs to display
exp_id = args.id
num_graphs = args.num_graphs

# Create raw/log_conso/{id_exp} directories if they don't exist
os.makedirs(f"raw/log_conso/{exp_id}", exist_ok=True)

# Get list of .oml files in consumption directory
oml_files = glob(os.path.expanduser(f"~/.iot-lab/{exp_id}/consumption/*.oml$

# Print list of .oml files in consumption directory
print("Files in consumption directory:")
for oml_file in oml_files:
    print(f"  {oml_file}")

# Copy .oml files to raw/log_conso/{id_exp} directory
for oml_file in oml_files:
    shutil.copy(oml_file, f"raw/log_conso/{exp_id}")

# Get list of .oml files in raw/log_conso/{id_exp} directory
result_files = glob(f"raw/log_conso/{exp_id}/*.oml")

# Print list of .oml files in result_graph directory
print("Files in result_graph directory:")
for result_file in result_files:
    print(f"  {result_file}")

# Plot data for each .oml file
if num_graphs is not None:
    oml_files = oml_files[:num_graphs]

for oml_file in oml_files:
    file_name = os.path.basename(oml_file)
    plot_command = f"plot_oml_consum -p -i raw/log_conso/{exp_id}/{file_nam$    subprocess.run(plot_command, shell=True)
