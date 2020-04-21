import argparse

from . import play
from . import tables
from . import boat
from . import map


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sail Race.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Use -h/--help after subcommand for help on subcommand arguments.'
    )
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
    play.fill_argparser(subparsers.add_parser('play', help=play.DESCRIPTION))
    tables.fill_argparser(subparsers.add_parser('tables', help=tables.DESCRIPTION))
    boat.fill_argparser(subparsers.add_parser('boat', help=boat.DESCRIPTION))
    map.fill_argparser(subparsers.add_parser('map', help=map.DESCRIPTION))
    return parser.parse_args()


def main():
    args = parse_args()
    if args.subcommand == 'play':
        play.main(args)
    elif args.subcommand == 'tables':
        tables.main(args)
    elif args.subcommand == 'boat':
        boat.main(args)
    elif args.subcommand == 'map':
        map.main(args)
    else:
        raise(f"Unexpected subcommand { args.subcommand }")
