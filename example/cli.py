import argparse
def parser():
    p = argparse.ArgumentParser()
    s = p.add_subparsers()
    s.add_parser("foo")
    return p
