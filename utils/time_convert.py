import os
from datetime import date, datetime
import pytz
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

tz_info = os.getenv('TZ', default='Asia/Shanghai')

default_timezone = pytz.timezone(tz_info)


class TimeConverter:
    @staticmethod
    def get_cur_date_str(format_='%Y-%m-%d', timezone=default_timezone) -> str:
        """
        获取当前日期 并转换为 指定格式的字符串
        :param timezone: 时区
        :param format_: 日期格式，默认为 '%Y-%m-%d'
        :return: 格式化后的日期字符串
        """
        now = datetime.now(timezone)
        return now.strftime(format_)

    @staticmethod
    def get_cur_datetime_str(timezone=default_timezone) -> str:
        """
        2023-12-10 20:32:58
        :return:
        """
        return datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def str_to_date(date_str: str, format_='%Y-%m-%d %H:%M:%S') -> date:
        """
        将日期字符串转换为日期类型
        :param format_:
        :param date_str: 日期字符串，例如：'2023-03-17'
        :param format_: 日期字符串格式，默认为'%Y-%m-%d'
        :return: 日期类型，例如：datetime.date(2023, 3, 17)
        """
        return datetime.strptime(date_str, format_).date()

    @staticmethod
    def str_to_dt(date_str: str, format_='%Y-%m-%d %H:%M:%S') -> datetime:
        """
        将日期字符串转换为日期类型
        :param format_:
        :param date_str: 日期字符串，例如：'22023-12-12 07:37:30'
        :param format_: 日期字符串格式，默认为''%Y-%m-%d %H:%M:%S'
        :return: 日期类型，例如：datetime(2023, 3, 17)
        """
        return datetime.strptime(date_str, format_)


def days_in_year(year: int) -> int:
    """
    判断某年 有多少天
    :param year:
    :return:
    """
    # 创建一个日期对象，代表该年度的1月1日
    cur_year = datetime(year, 1, 1)
    # 将日期设为下一年度的1月1日
    next_year = datetime(year + 1, 1, 1)
    # 计算两个日期之间的时间差
    delta = next_year - cur_year
    return delta.days
