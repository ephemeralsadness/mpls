from datetime import timedelta
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler:
    def __init__(self, delta: timedelta):
        self.scheduler = BackgroundScheduler(timezone='Asia/Vladivostok')
        self.delta = delta
        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())

    def add_job(self, func, args):
        self.scheduler.add_job(func=func,
                               trigger='interval',
                               seconds=self.delta.seconds,
                               args=args)
        return self
