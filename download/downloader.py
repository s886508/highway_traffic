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
        return False

    response = requests.get(url)

    if response.status_code != 200:
        print('URL: %s cannot be connected' % url)
        return False

    with open(file_path, 'wb') as f:
        f.write(response.content)

    return True


def _read_downloaded():
    downloaded = set()
    path = 'D:/GitProjects/highway_traffic/data/road_level_data/downloaded.txt'
    if os.path.exists(path):
        with open(path, 'rb') as f:
            downloaded = set(f.readlines())
    return downloaded


def _write_downloaded(downloaded):
    with open('D:/GitProjects/highway_traffic/data/road_level_data/downloaded.txt', 'wa') as f:
        f.writelines(downloaded)


def _download_all_data():

    downloaded = _read_downloaded()

    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31}

    hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',]

    interval = 10
    minutes = [m for m in range(0, 60) if m % interval == 0]

    root_url = 'http://tisvcloud.freeway.gov.tw/history/roadlevel'
    root_path = 'D:/GitProjects/highway_traffic/data/road_level_data'

    for year in range(2013, 2014):
        for month in range(1, 13):
            for day in range(1, days[month] + 1):
                date = '%s%02d%02d' % (str(year), month, day)
                path = os.path.join(root_path, date)
                if date in downloaded:
                    continue

                downloaded.add(date)
                for hour in hours:
                    for minute in minutes:
                        url = '%s/%s/roadlevel_value_%s%02d.xml.gz' % (root_url, date, hour, minute)
                        print('Collecting data from %s' % url)
                        ret = retrieve_data(url, path)
                        print('Collecting data complete ret = %d' % ret)

                        random_time = random.randint(50, 60)
                        time.sleep(random_time)

                _write_downloaded(downloaded)


if __name__ == '__main__':
    _download_all_data()