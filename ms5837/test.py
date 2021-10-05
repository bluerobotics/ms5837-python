#!/usr/bin/python3

def main():
    from ms5837 import MS5837_02BA, MS5837_30BA
    from llog import LLogWriter

    device = "ms5837"
    parser = LLogWriter.create_default_parser(__file__, device)
    parser.add_argument("--bus", default=6, help="i2c bus")
    parser.add_argument('--bar02', action='store_true',
                        help='run test for Bar02 02BA model (default is Bar30 30BA model)')
    args = parser.parse_args()

    with LLogWriter(args.meta, args.output, console=args.console) as log:
        if args.bar02:
            ms = MS5837_02BA(args.bus)
        else:
            ms = MS5837_30BA(args.bus)

        if not ms.init():
            print(f'failed to init device')
            exit(1)

        def data_getter():
            ms.read()
            return f'{ms.pressure():.6f} {ms.temperature():.6f}'

        log.log_data_loop(data_getter, parser_args=args)

if __name__ == '__main__':
    main()
