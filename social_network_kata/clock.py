from datetime import datetime
from datetime import timedelta


class Clock:
    @staticmethod
    def get_date() -> datetime:
        return datetime.now()
