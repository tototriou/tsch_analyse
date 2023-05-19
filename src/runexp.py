import argparse
import subprocess

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Input file containing node IDs")
parser.add_argument("-s", "--sender", type=int, help="Number of sender nodes")
parser.add_argument("-c", "--coordinator", type=int,
                    help="Number of coordinator nodes")
# name of the file to be created
parser.add_argument("-n", "--name",  help="Input file containing node IDs")
args = parser.parse_args()


# Read node IDs from input file
with open(args.file) as f:
    nodes = [line.strip() for line in f]

# Build node list string for experiment submission
node_list = ""
for i in range(args.sender):
    node_list += f"-l strasbourg,m3,{nodes[i]},build/iotlab/m3/sender.iotlab "

for i in range(args.sender, args.sender + args.coordinator):
    node_list += f"-l strasbourg,m3,{nodes[i]},build/iotlab/m3/coordinator.iotlab "

# Submit experiment
subprocess.run(
    f"iotlab-experiment submit -n Ex4 -d 10 {node_list}", shell=True)

# Wait for experiment to start
subprocess.run("iotlab-experiment wait", shell=True)

# Run serial aggregator and save output to file
with open(args.name, "w") as f:
    subprocess.run("serial_aggregator", stdout=f, shell=True)
