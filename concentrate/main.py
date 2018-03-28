import sys
import logging
import traceback
from concentrate import cli
from concentrate.core import program


def main():
    args = cli.get_args()
    try:
        exit_status = program(args)
        return sys.exit(exit_status)
    except Exception as e:
        error_type = type(e).__name__
        logging.error(traceback.format_exc())
        sys.stderr.write("{0}: {1}\n".format(error_type, e.message))
        sys.exit(1)
