# coding=utf-8
import os
import time
import requests
import random


def retrieve_data(url, path):
    """
    Get file from website and save to given path/
    :param url: Remote file to access.
    :param path: Save the file from remote to local.
    :return: True for download successfully.
    """

    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, url[url.rindex("/") + 1:])
    if os.path.exists(file_path):
        print('File is already downloaded')
        return 1

    while True:
        try:
            response = requests.get(url)
            break
        except:
            print("Connect error, will try again after 5 minutes")
            time.sleep(300)

    if response.status_code != 200:
        print('URL: %s cannot be connected' % url)
        return -1

    with open(file_path, 'wb') as f:
        f.write(response.content)

    return 0


def retrieve_all_data():
    from util.utility import data_name_gen

    root_url = 'http://tisvcloud.freeway.gov.tw/history/roadlevel'
    root_path = 'D:/GitProjects/highway_traffic/data/road_level_data'

    for date, name in data_name_gen():
        path = os.path.join(root_path, date)
        url = '%s/%s/%s' % (root_url, date, name)

        print('Collecting data from %s' % url)
        ret = retrieve_data(url, path)
        print('Collecting data complete ret = %d' % ret)

        if ret <= 0:
            random_time = random.randint(30, 40)
            time.sleep(random_time)
