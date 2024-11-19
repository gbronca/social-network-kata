from datetime import datetime


class Clock:
    def get_date() -> datetime:
        return datetime.now()
    
    def get_time_difference() -> str:
        raise NotImplementedError