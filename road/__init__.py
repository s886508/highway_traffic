# coding = uff-8
import time


class RoadLevel:
    level = -1
    label = 'Unknown'
    max_speed = -99
    min_speed = -99

    @staticmethod
    def create(level):
        """
        Create RoadLevel instance.
        :param level: integer of level.
        :return: RoadLevel
        """
        if level == 1:
            return RoadLevel.lv1()
        if level == 2:
            return RoadLevel.lv2()
        if level == 3:
            return RoadLevel.lv3()
        if level == 4:
            return RoadLevel.lv4()
        return RoadLevel.invalid()

    @staticmethod
    def lv1():
        lv = RoadLevel()
        lv.label = '順暢'
        lv.max_speed = 200
        lv.min_speed = 80
        return lv

    @staticmethod
    def lv2():
        lv = RoadLevel()
        lv.label = '車多'
        lv.max_speed = 79
        lv.min_speed = 60
        return lv

    @staticmethod
    def lv3():
        lv = RoadLevel()
        lv.label = '車多'
        lv.max_speed = 59
        lv.min_speed = 40
        return lv

    @staticmethod
    def lv4():
        lv = RoadLevel()
        lv.label = '擁塞'
        lv.max_speed = 39
        lv.min_speed = 0
        return lv

    @staticmethod
    def invalid():
        return RoadLevel()

    def __str__(self):
        return 'Label: {0}, Min Speed: {1}, Max Speed: {2}'.format(self.label, self.min_speed, self.max_speed)


class RoadSection:
    section_id = -1
    section_label = ''
    point_start = -1
    point_end = -1
    km_from = -1
    km_to = -1
    location_path_id = -1
    type = -1  # 1.國道、2.快速公路(如西濱快速公路等)、3.省道、4.快速道路(如建國高架橋等)、5.市區道路、6.縣道、7.其它

    def __init__(self, dicts):
        self.section_id = dicts['routeid']
        self.section_label = dicts['roadsection']
        self.point_start = int(dicts['startlocationpoint'])
        self.point_end = int(dicts['endlocationpoint'])
        self.km_from = dicts['fromkm']
        self.km_to = dicts['tokm']
        self.location_path_id = dicts['locationpath']
        self.type = int(dicts['roadtype'])

    def __str__(self):
        return 'section_id: %s\n' \
               'section_label: %s\n' \
               'point_start: %d\n' \
               'point_end: %d\n' \
               'km_from: %s\n' \
               'km_to: %s\n' \
               'location_path_id: %s\n' \
               'type: %d\n' % (
               self.section_id, self.section_label, self.point_start, self.point_end, self.km_from, self.km_to,
               self.location_path_id, self.type)


class TrafficData:
    section_level = RoadLevel.invalid()
    travel_speed = -1  # km/h
    travel_time = -1   # seconds
    collect_time = ''  # 2018/09/18 15:41:00
    _time_format = '%Y/%m/%d %H:%M:%S'

    def __init__(self, dicts):
        self.section_level = RoadLevel.create(int(dicts['level']))
        self.travel_speed = int(dicts['value'])
        self.travel_time = int(dicts['traveltime'])
        self.collect_time = time.strptime(dicts['datacollecttime'], self._time_format)

    def __str__(self):
        return 'section_level: {0}\n' \
               'travel_speed: {1}\n' \
               'travel_time: {2}\n' \
               'collect_time: {3}\n'.format(self.section_level, self.travel_speed, self.travel_time,
                                            time.strftime(self._time_format, self.collect_time))
