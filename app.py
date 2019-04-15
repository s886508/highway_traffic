# coding=utf-8
from argparse import ArgumentParser


def parse_config_args(period, time):
    var = {}
    if period:
        p = period.split(':')
        var['year'] = (int(p[0].split('-')[0]), int(p[1].split('-')[0]))
        var['month'] = (int(p[0].split('-')[1]), int(p[1].split('-')[1]))
    if time:
        t = time.split(':')
        var['hour'] = (int(t[0]), int(t[1]))

    return var



if __name__ == '__main__':
    parser = ArgumentParser(prog='app', description='Traffic Data Crawler and Analyzer')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--download', help='Download highway traffic data from website', action='store_true')
    group.add_argument('-de', '--decompress', help='Decompress downloaded files', action='store_true')

    group_download = parser.add_argument_group('Configurations')
    group_download.add_argument('-p', '--period', help='ex: 2018-01:2018-12', type=str)
    group_download.add_argument('-r', '--hours', help='ex: 06:09', type=str)
    group_download.add_argument('-i', '--interval', help='Data stored interval', type=int, default=10)

    args = parser.parse_args()

    if args.download:
        var = parse_config_args(args.period, args.hours)
        from download import downloader
        downloader.retrieve_traffic_data(year=var['year'], month=var['month'], hour=var['hour'], interval=args.interval)
        exit(0)

    if args.decompress:
        var = parse_config_args(args.period, args.hours)
        from data import decompression
        decompression.decompress_traffic_data(year=var['year'], month=var['month'], hour=var['hour'], interval=args.interval)
        exit(0)

    parser.print_help()
