"""Local HTTP Share — Serve a folder on localhost with a directory listing, bind to loopback only."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='local_http_share',
        description='Serve a folder on localhost with a directory listing, bind to loopback only.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Local HTTP Share')
    print('A quick folder share on this PC.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
