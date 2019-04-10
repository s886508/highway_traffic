# coding=utf-8


def data_name_gen():
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31}

    hours = ['06', '07', '08', '09', '16', '17', '18', '19']

    interval = 10
    minutes = [m for m in range(0, 60) if m % interval == 0]

    date_gen = ('%s%02d%02d' % (str(year), month, day)
                for year in range(2018, 2019)
                for month in range(1, 13)
                for day in range(1, days[month] + 1))

    for date in date_gen:
        time_gen = ('%s%02d' % (hour, minute) for hour in hours for minute in minutes)
        for t in time_gen:
            yield (date, 'roadlevel_value_%s.xml.gz' % t)
