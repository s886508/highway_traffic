# coding=utf-8


def data_name_gen(year, month, hour, interval=10):
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31}

    date_gen = ('%s%02d%02d' % (str(y), m, d)
                for y in range(year[0], year[1] + 1)
                for m in range(month[0], month[1] + 1)
                for d in range(1, days[m] + 1))

    hours = [h for h in range(hour[0], hour[1] + 1)]
    minutes = [m for m in range(0, 60) if m % interval == 0]

    for date in date_gen:
        time_gen = ('%02d%02d' % (hour, minute) for hour in hours for minute in minutes)
        for t in time_gen:
            yield (date, 'roadlevel_value_%s.xml.gz' % t)
