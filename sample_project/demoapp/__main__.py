import pandas as pd
import sys
import argparse

from .calculate import Calculate

def init_parser():
    parser = argparse.ArgumentParser(
        description='demoapp'
    )

    parser.add_argument(
        'csvfile',
        default=sys.stdin,
        type=argparse.FileType('r')
    )
    return parser

csvfile = init_parser().parse_args().csvfile
df = pd.DataFrame.from_csv(csvfile)

calculate = Calculate(df)
print(calculate.calculate())
