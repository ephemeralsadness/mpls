from datetime import datetime, timedelta
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


def round_down_datetime(dt: datetime, delta: timedelta):
    return datetime.fromtimestamp((dt.timestamp() // delta.seconds) * delta.seconds)


def round_up_datetime(dt: datetime, delta: timedelta):
    return round_down_datetime(dt, delta) + delta


class Scheduler:
    def __init__(self, delta: timedelta):
        self.scheduler = BackgroundScheduler(timezone='Asia/Vladivostok')
        self.delta = delta
        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())

    def add_job(self, func):
        self.scheduler.add_job(func=func,
                               trigger='interval',
                               seconds=self.delta.seconds)
        return self
