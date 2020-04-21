import argparse

from . import play, tables, boat, map

subcommands = {_.NAME: _ for _ in [play, tables, boat, map]}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sail Race.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Use -h/--help after subcommand for help on subcommand arguments.'
    )
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
    for name, subcommand in subcommands.items():
        subcommand.fill_argparser(subparsers.add_parser(name, help=subcommand.DESCRIPTION))
    return parser.parse_args()


def main():
    args = parse_args()
    subcommand = subcommands[args.subcommand]
    subcommand.main(args)
