# coding=utf-8
import os
from xml.etree import ElementTree
from road import RoadSection


def parse(path):
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


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), '../data/road_level_info/roadlevel_info_0000.xml')
    parse(path)
