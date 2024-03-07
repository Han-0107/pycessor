import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Setting the pycessor')
    parser.add_argument('--ISA', type=str, default='risc-v', help='Choose the ISA')
    parser.add_argument('--bits', type=int, default=32, help='Set the bits of processor')
    parser.add_argument('--mode', type=str, default='inside', help='Choose the way to test')
    return parser.parse_args()


def examine_isa(args):
    if args.bits != 32 and args.bits != 64:
        print('The bits of processor are not available now!')
        sys.exit(2)
    if args.mode == 'outside':
        print('The outside mode is not available now!')
        sys.exit(3)
    if args.ISA != 'risc-v':
        print('The ISA is not available now!')
        sys.exit(1)
        