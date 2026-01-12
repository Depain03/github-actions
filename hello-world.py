import argparse

def printhello(name): 
    print(f"Hello World, {name}!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print Hello World with a name')
    parser.add_argument('--name', type=str, help='Your name')
    args = parser.parse_args()

    printhello(args.name)
