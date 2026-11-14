import argparse

from portfolio_provisioning_qual_20261113 import __version__


def main():
    parser = argparse.ArgumentParser(prog="portfolio_provisioning_qual_20261113")
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args()


if __name__ == "__main__":
    main()
