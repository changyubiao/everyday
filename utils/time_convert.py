import os
from datetime import date, datetime
import pytz
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

tz_info = os.getenv('TZ', default='Asia/Shanghai')

default_timezone = pytz.timezone(tz_info)


class TimeConverter:
    @staticmethod
    def get_current_date(format_='%Y-%m-%d', timezone=default_timezone) -> str:
        """
        获取当前日期并转换为指定格式的字符串
        :param timezone:
        :param format_: 日期格式，默认为 '%Y-%m-%d'
        :return: 格式化后的日期字符串
        """
        now = datetime.now(timezone)
        return now.strftime(format_)

    @staticmethod
    def get_current_dt(timezone=default_timezone) -> str:
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
        :param date_str: 日期字符串，例如：'22023-12-12 07:37:30 '
        :param format_: 日期字符串格式，默认为''%Y-%m-%d %H:%M:%S'
        :return: 日期类型，例如：datetime(2023, 3, 17)
        """
        return datetime.strptime(date_str, format_)
