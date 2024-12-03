from datetime import datetime
from datetime import timedelta


class Clock:
    @staticmethod
    def get_date() -> datetime:
        return datetime.now()

    @staticmethod
    def get_time_difference(current_time, past_time) -> timedelta:
        return current_time - past_time
