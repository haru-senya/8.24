import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--user')
args = parser.parse_args()

print(f"Welcome, {args.user}!")