import argparse

parser = argparse.ArgumentParser(description='Print Hello World with a name')
parser.add_argument('name', type=str, help='Your name')
args = parser.parse_args()

print(f"Hello World, {args.name}!")
