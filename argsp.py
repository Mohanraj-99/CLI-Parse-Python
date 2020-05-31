# Import CLI Python  ArgumentParser
import argparse

# Parse is an object to class ArgumentParser
parser = argparse.ArgumentParser()

# List of Aruguments you need can be specified through add_arguments
parser.add_argument('--name',type=str,default='RM',help="Enter ur name")
parser.add_argument('--age',type=int,default=None,help="Enter ur age")

# Get the imput from CLI
args = parser.parse_args()

# Extract them
print(args.name)
print(args.age)


# @CLI python filename.py --name Mohanraj --age 18 --> If arguments are not gn, then default values are taken
