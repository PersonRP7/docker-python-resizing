import subprocess
import argparse

parser = argparse.ArgumentParser(
    description = "Copy image to or from the thumbnail container."
)

parser.add_argument('-d', type = str, required = True, help = "-d(direction) -> to or from.")
parser.add_argument('-n', type = str, required = True, help = "-n(name) -> name of the file.")
args = vars(parser.parse_args())

to_variants = [
    "to", "To"
]

from_variants = [
    "From", 'from'
]

if args['d'] in to_variants:
    subprocess.run(
        f"docker cp ./{args['n']} thumbnail:/application"
    )
elif args['d'] in from_variants:
    subprocess.run(
        f"docker cp thumbnail:/application/{args['n']} ."
    )
