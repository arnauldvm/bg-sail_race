import argparse

from . import play


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sail Race.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Use -h/--help after subcommand for help on subcommand arguments.'
    )
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
    play.fill_argparser(subparsers.add_parser('play', help=play.DESCRIPTION))
    return parser.parse_args()


def main():
    args = parse_args()
    if args.subcommand == 'play':
        play.main(args)
    else:
        raise(f"Unexpected subcommand { args.subcommand }")
