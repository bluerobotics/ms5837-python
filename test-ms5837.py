#!/usr/bin/python3

import argparse
from ms5837 import MS5837_02BA, MS5837_30BA
import signal
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--bar02', action='store_true',
                    help='run test for Bar02 02BA model (default is Bar30 30BA model)')
parser.add_argument('--bus', action='store', type=int, required=True)
parser.add_argument('--frequency', action='store', type=int,
                    default=1, help="set the measurement frequency")
parser.add_argument('--output', action='store', type=str, default=None)
args = parser.parse_args()

if args.bar02:
    ms = MS5837_02BA(args.bus)
else:
    ms = MS5837_30BA(args.bus)
ms.init()

outfile = None

if args.output:
    outfile = open(args.output, "w")


def cleanup(_signo, _stack):
    if outfile:
        outfile.close()
    exit(0)


signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

while True:
    try:
        ms.read()
        output = f'{time.time()} 1 {ms.pressure()} {ms.temperature()}'
    except Exception as e:
        output = f"{time.time()} 0 {e}"
    print(output)
    if outfile:
        outfile.write(output + '\n')
    if args.frequency:
        time.sleep(1.0/args.frequency)
