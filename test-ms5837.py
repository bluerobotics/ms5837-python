#!/usr/bin/python3

from ms5837 import MS5837_02BA, MS5837_30BA
from llog import LLogWriter

device = 'ms5837'
parser = LLogWriter.create_default_parser(__file__, device)
parser.add_argument('--bar02', action='store_true',
                    help='run test for Bar02 02BA model (default is Bar30 30BA model)')
parser.add_argument('--bus', action='store', type=int, required=True)
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    MS5837 = MS5837_02BA if args.bar02 else MS5837_30BA
    ms = MS5837(args.bus)
    ms.init()
    
    def data_getter():
        ms.read()
        return f"{ms.pressure()} {ms.temperature()}"
    
    log.log_data_loop(data_getter, parser_args=args)
