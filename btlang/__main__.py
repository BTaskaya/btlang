from btlang.parser import get_parser
from btlang.compiler import Compiler

parser = get_parser()
compiler = Compiler()


def main(args):
    fname = args.pop()
    with open(fname) as f:
        content = f.read()

    tree = parser.parse(content)
    result = compiler.compile(tree)
    exec(result)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
