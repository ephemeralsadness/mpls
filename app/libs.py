from datetime import datetime, timedelta


def round_down_datetime(dt: datetime, delta: timedelta):
    return datetime.fromtimestamp((dt.timestamp() // delta.seconds) * delta.seconds)


def round_up_datetime(dt: datetime, delta: timedelta):
    return round_down_datetime(dt, delta) + delta
