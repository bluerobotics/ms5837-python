#!/usr/bin/python3

import matplotlib.pyplot as plt

def generate_figures(log):
    footer = f'ms5837 test report'

    f, spec = log.figure(height_ratios=[1,1], suptitle=f'ms5837 data', footer=footer)
    plt.subplot(spec[1,:])
    log.error.ttable(rl=True)

    plt.subplot(spec[1,:])
    log.data.pressure.pplot(log.data.temperature)

def main():
    from llog import LLogReader
    from matplotlib.backends.backend_pdf import PdfPages
    from pathlib import Path

    parser = LLogReader.create_default_parser(__file__, 'ms5837')
    args = parser.parse_args()

    log = LLogReader(args.input, args.meta)

    generate_figures(log)

    if args.output:
        if Path(args.output).exists():
            print(f'WARN {args.output} exists! skipping ..')
        else:
            with PdfPages(args.output) as pdf:
                [pdf.savefig(n) for n in plt.get_fignums()]

    if args.show:
        plt.show()

if __name__ == '__main__':
    main()
