import sys
from .cli import parser


def main(argv=sys.argv):
    args = parser.parse_args()
