import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Setting the pycessor')
    parser.add_argument('--ISA', type=str, default='risc-v', help='Choose the ISA')
    parser.add_argument('--bits', type=int, default=32, help='Set the bits of processor')
    parser.add_argument('--mode', type=str, default='inside', help='Choose the way to test')
    return parser.parse_args()
