"""
今天是2019年7月1日，星期一，今年的第181天，这一年49.59%的时间已流逝
"""
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP

from utils.time_convert import TimeConverter

tz = TimeConverter()

today = tz.str_to_date(tz.get_current_dt())


def everyday_notice(today: date = today):
    """
    :param today: 今天的日期
    :return:
    """
    chinese_digits = ['一', '二', '三', '四', '五', '六', '日']

    numbers = range(1, 8)

    num_to_chinese = dict(zip(numbers, chinese_digits))

    # 今年的第 几天
    tm_day = today.timetuple().tm_yday

    # 比例字符串 TODO
    proportion_str = str((tm_day - 1) / 365 * 100)

    proportion = Decimal(proportion_str).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

    # print(f"proportion : {proportion}")

    info_string = (
        f"今天是{today.year}年{today.month}月{today.day}日, 星期{num_to_chinese.get(today.isoweekday(), '')}, "
        f"今年的第{tm_day}天, "
        f"这一年{proportion}%的时间已流逝. "

    )
    return info_string


if __name__ == '__main__':
    print(everyday_notice())
    # print(get_cur_time())
    # print(get_cur_time(eastern))
    pass
