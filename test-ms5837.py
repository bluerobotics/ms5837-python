#!/usr/bin/python3

import argparse
from ms5837 import MS5837_02BA, MS5837_30BA
from pathlib import Path
import llog
import time

device = 'ms5837'
defaultMeta = Path(__file__).resolve().parent / f"{device}.meta"

parser = argparse.ArgumentParser(description=f'{device} test')
parser.add_argument('--bar02', action='store_true',
                    help='run test for Bar02 02BA model (default is Bar30 30BA model)')
parser.add_argument('--bus', action='store', type=int, required=True)
parser.add_argument('--frequency', action='store', type=int,
                    default=1, help="set the measurement frequency")
parser.add_argument('--meta', action='store', type=str, default=defaultMeta)
parser.add_argument('--output', action='store', type=str, default=None)
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    if args.bar02:
        ms = MS5837_02BA(args.bus)
    else:
        ms = MS5837_30BA(args.bus)
    ms.init()
  
    while True:
        try:
            ms.read()
            log.log(llog.LLOG_DATA, f"{ms.pressure()} {ms.temperature()}")
        except Exception as e:
            log.log(llog.LLOG_ERROR, e)
      
        if args.frequency:
            time.sleep(1.0/args.frequency)
