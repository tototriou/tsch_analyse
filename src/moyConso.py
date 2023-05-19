import argparse
import csv
import os
from glob import glob

def calculate_average_power(oml_file):
    with open(oml_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        power_values = []
        for row in reader:
            if len(row) == 8:
                try:
                    power = float(row[5])
                    power_values.append(power)
                except ValueError:
                    pass
        if len(power_values) > 0:
            average_power = sum(power_values) / len(power_values)
            return average_power
        else:
            return None

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", type=int, help="Experiment ID")
args = parser.parse_args()

# Get experiment ID
exp_id = args.id

# Create raw/log_conso/{id_exp} directories if they don't exist
os.makedirs(f"raw/log_conso/{exp_id}", exist_ok=True)


# Get list of .oml files in raw/log_conso/{id_exp} directory
oml_files = glob(f"raw/log_conso/{exp_id}/*.oml")

num_nodes = len(oml_files) - 1

# Calculate average power for each .oml file and write results to moy.txt f$with open(f"raw/log_conso/{exp_id}/moy.txt", 'w') as f:
    for oml_file in oml_files:
        average_power = calculate_average_power(oml_file)
        f.write(f"{os.path.basename(oml_file)}: {average_power}\n")

# Calculate overall average power and write result to conso{num_nodes}.txt $average_powers = [calculate_average_power(oml_file) for oml_file in oml_fil$overall_average_power = sum(average_powers) / len(average_powers)
num_nodes = len(oml_files) - 1
with open(f"raw/log_conso/{exp_id}/conso{num_nodes}.txt", 'w') as f:
    f.write(f"{overall_average_power}\n")
