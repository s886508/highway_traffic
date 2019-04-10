# coding=utf-8
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(prog='app', description='Traffic Data Crawler and Analyzer')
    parser.add_argument('--download', help='Download highway traffic data from website', action='store_true')
    parser.add_argument('--decompress', help='Decompress downloaded files', action='store_true')
    args = parser.parse_args()

    if args.download:
        from download import downloader
        downloader.retrieve_all_data()
        exit(0)

    if args.decompress:
        from data import decompression
        decompression.decompress_all_data()
        exit(0)

    parser.print_help()
