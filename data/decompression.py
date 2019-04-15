# coding=utf-8
import os
from util.utility import data_name_gen


def decompress(file_path, output_folder):
    """
    Decompress given file path to raw data.
    :param file_path: File to decompression.
    :param output_folder: Raw data to output destination.
    :return: True if success.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    file_name = os.path.basename(file_path)[:-3]  # Remove '.gz'
    output_file_path = os.path.join(output_folder, file_name)
    if os.path.exists(output_file_path):
        return True

    exe_path = '"C:\\Program Files\\7-Zip\\7z.exe"'
    cmd = '%s e -y -o%s %s' % (exe_path, output_folder, file_path)
    os.system(cmd)
    return True


def decompress_traffic_data(year, month, hour, interval=10):
    """
    Decompress downloaded data.
    :param year: Indicate begin and end year. ex: (2018, 2018)
    :param month: Indicate begin and end month. ex: (1, 12)
    :param hour: Indicate begin and end month. ex: (6, 9)
    :param interval: Data record intervals.
    """
    data_folder = os.path.dirname(os.path.abspath(__file__))
    for date, name in data_name_gen(year, month, hour, interval):
        file_path = os.path.join(data_folder, 'road_level_data', date, name)
        output_folder = os.path.join(data_folder, 'road_level_data_raw', date)
        decompress(file_path, output_folder)

