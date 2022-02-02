from datetime import datetime, timedelta


def round_down_datetime(dt: datetime, delta: timedelta):
    return datetime.fromtimestamp((dt.timestamp() // delta.seconds) * delta.seconds)


def round_up_datetime(dt: datetime, delta: timedelta):
    return round_down_datetime(dt, delta) + delta


def get_last_table(delta):
    return round_down_datetime(datetime.now(), delta).strftime('%Y-%m-%dT%H:%M')


def get_next_table(delta):
    return round_up_datetime(datetime.now(), delta).strftime('%Y-%m-%dT%H:%M')
