import argparse
import sys


# print(f"Arguments count: {len(sys.argv)}")
# print(sys.argv)
# for i, arg in enumerate(sys.argv):
#     print(f"Argument {i:>6}: {arg}")
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('-m', '--module', nargs='+', help='List of modules need to logging')

args = parser.parse_args()
print(args)
# Output:
    # python arg1.py  1 2 3 4
    # Namespace(integers=[1, 2, 3, 4])
# for it in args.integers:
#     print(it)
print(args.accumulate(args.integers))
