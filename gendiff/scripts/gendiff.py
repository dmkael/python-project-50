import argparse


parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference."
)
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument('-f', '--format')
args = parser.parse_args()

file1 = args.first_file
file2 = args.second_file
