import argparse
def parser():
    p = argparse.ArgumentParser(prog="bug-example-3")
    s = p.add_subparsers()
    s.add_parser("foo")
    return p
