# coding = uff-8


class RoadLevel:
    label = ''
    max_speed = 0
    min_speed = 0

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