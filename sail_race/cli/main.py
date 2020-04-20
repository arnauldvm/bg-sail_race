import argparse

from . import play
from . import tables


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sail Race.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Use -h/--help after subcommand for help on subcommand arguments.'
    )
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
    play.fill_argparser(subparsers.add_parser('play', help=play.DESCRIPTION))
    tables.fill_argparser(subparsers.add_parser('tables', help=tables.DESCRIPTION))
    return parser.parse_args()


def main():
    args = parse_args()
    if args.subcommand == 'play':
        play.main(args)
    elif args.subcommand == 'tables':
        tables.main(args)
    else:
        raise(f"Unexpected subcommand { args.subcommand }")
