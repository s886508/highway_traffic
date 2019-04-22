# coding=utf-8
import os
from xml.etree import ElementTree
from road import RoadSection, TrafficData
from util.utility import data_name_gen


def parse_road_info(path):
    """
    Parse highway road section data.
    :param path: XML file path to parse.
    :return: map(section_id, RoadSection)
    """

    node_root = ElementTree.parse(path).getroot()

    info_dict = {}
    for node_child in node_root.findall('Infos/Info'):
        section = RoadSection(node_child.attrib)
        info_dict[section.section_id] = section
    return info_dict


def parse_traffic_data(path):
    """
    Parse collected highway traffic data.
    :param path: XML file path.
    :return: list of TrafficData
    """
    node_root = ElementTree.parse(path).getroot()

    collected = []
    for node_child in node_root.findall('Infos/Info'):
        collected.append(TrafficData(node_child.attrib))
    return collected


def read_traffic_data(year, month, hour, interval):
    """
    Read traffic data from XML by given time range.
    :param year: Indicate begin and end year. ex: (2018, 2018)
    :param month: Indicate begin and end month. ex: (1, 12)
    :param hour: Indicate begin and end month. ex: (6, 9)
    :param interval: Data record intervals.
    :return dict with key is date and list of data.s
    """

    data_folder = os.path.dirname(os.path.abspath(__file__))
    for date, name in data_name_gen(year, month, hour, interval):
        file_path = os.path.join(data_folder, '..', 'data', 'road_level_data_raw', date, name)
        parse_traffic_data(file_path)


if __name__ == '__main__':
    #path = os.path.join(os.getcwd(), '../data/road_level_info/roadlevel_info_0000.xml')
    #parse_road_info(path)
    read_traffic_data((2018, 2018), (1, 3), (6, 9), 10)

