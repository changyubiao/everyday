"""
今天是2019年7月1日，星期一，今年的第181天，这一年49.59%的时间已流逝
"""
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from utils.time_convert import TimeConverter, days_in_year

tz = TimeConverter()

today = tz.str_to_date(tz.get_cur_datetime_str())


def everyday_notice(today: date = today):
    """
    :param today: 今天的日期
    :return:
    """
    chinese_digits = ['一', '二', '三', '四', '五', '六', '日']

    numbers = range(1, 8)

    num_to_chinese = dict(zip(numbers, chinese_digits))

    # 今年的第几天
    tm_day = today.timetuple().tm_yday

    # 一年有多少天
    total_days = days_in_year(today.year)
    # 比例字符串
    proportion_str = str((tm_day - 1) / total_days * 100)

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
    pass
