import argparse

# create a parser
parser = argparse.ArgumentParser()

# """ positional arguments """
# # pass arguments
# parser.add_argument("x", type=int)
# parser.add_argument("y", type=int)

""" optional arguments """
# pass arguments
parser.add_argument("--x", type=int, required=True)
parser.add_argument("--y", type=int, default=0)

# get info
args = parser.parse_args()

print("type of x: ", type(args.x))
print("type of y: ", type(args.y))

print("x: ", args.x)
print("y: ", args.y)

#print("x + y:", args.x + args.y)