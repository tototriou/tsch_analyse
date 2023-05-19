import argparse
import os
from glob import glob

def calculate_duty_cycle(oml_file, threshold):
    with open(oml_file, 'r') as f:
        occupied_count = 0
        total_count = 0
        for line in f:
            if line.startswith('content:'):
                break
        for line in f:
            row = line.split()
            if len(row) == 7:
                try:
                    rssi = float(row[6])
                    if rssi > threshold:
                        occupied_count += 1
                    total_count += 1
                except ValueError:
                    pass
        if total_count > 0:
            duty_cycle = occupied_count / total_count
            return duty_cycle
        else:
            return None

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", type=int, help="Experiment ID")
args = parser.parse_args()

# Get experiment ID and RSSI threshold
exp_id = args.id
threshold = -80

# Create raw/log_radio/{id_exp} directories if they don't exist
os.makedirs(f"raw/log_radio/{exp_id}", exist_ok=True)

# Get list of .oml files in raw/log_radio/{id_exp} directory
oml_files = glob(f"raw/log_radio/{exp_id}/*.oml")

# Calculate duty cycle for each .oml file and write results to duty_cycle.txt file
duty_cycles = []
with open(f"raw/log_radio/{exp_id}/duty_cycle.txt", 'w') as f:
    for oml_file in oml_files:
        duty_cycle = calculate_duty_cycle(oml_file, threshold)
        duty_cycles.append(duty_cycle)
        f.write(f"{os.path.basename(oml_file)}: {duty_cycle}\n")

# Calculate overall average duty cycle and write result to average_duty_cycle.txt file
with open(f"raw/log_radio/{exp_id}/average_duty_cycle.txt", 'w') as f:
    duty_cycles = [duty_cycle for duty_cycle in duty_cycles if duty_cycle is not None]
    if len(duty_cycles) > 0:
        overall_average_duty_cycle = sum(duty_cycles) / len(duty_cycles)
        f.write(f"Overall average duty cycle: {overall_average_duty_cycle}\n")
    else:
        f.write("No valid duty cycle data found\n")
