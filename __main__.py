import sys
from .cli import parser
from .core import program


def main(argv=sys.argv):
    args = parser.parse_args()
    program(args)
