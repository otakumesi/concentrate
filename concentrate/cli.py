import sys
from argparse import ArgumentParser


DESCRIPTION = """
This is CLI tool resisting the temptetion what plays some of social media.
"""


def get_args(argv=sys.argv):
    parser = ArgumentParser(
        prog="concentrate",
        description=DESCRIPTION
    )

    # parser.add_argument('-u', action='update')

    return parser.parse_args()
