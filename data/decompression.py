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
        raise FileNotFoundError

    exe_path = '"C:\\Program Files\\7-Zip\\7z.exe"'
    cmd = '%s e -o%s %s' % (exe_path, output_folder, file_path)
    os.system(cmd)
    return True


def decompress_all_data():
    for date, name in data_name_gen():
        file_path = os.path.join(os.getcwd(), 'road_level_data', date, name)
        output_folder = os.path.join(os.getcwd(), 'road_level_data_raw', date)
        decompress(file_path, output_folder)

