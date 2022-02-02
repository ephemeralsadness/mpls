# converts data from database tables to the list of data for aggregation
from src import db
from src.libs import round_down_datetime, round_up_datetime
from src.models import DataBit, LabelPoint

import numpy as np
import json
from collections import defaultdict
from datetime import datetime, timedelta


class AG:
    def process(self, data):
        pass


class QuantileAG(AG):
    def __init__(self, q):
        self.q = q

    def process(self, data):
        return np.quantile(data, self.q)

    def name(self):
        return 'quantile-{}'.format(self.q)


class MaxAG(AG):
    def process(self, data):
        return max(data)

    def name(self):
        return 'max'


class MinAG(AG):
    def process(self, data):
        return min(data)

    def name(self):
        return 'min'


class AverageAG(AG):
    def process(self, data):
        return np.average(data)

    def name(self):
        return 'average'


def convert(delta):
    lower_bound = round_down_datetime(datetime.now() - delta, delta)
    ags = [
        QuantileAG(0.1),
        QuantileAG(0.9),
        QuantileAG(0.5),
        MaxAG(),
        MinAG(),
        AverageAG(),
    ]

    upper_bound = (lower_bound + delta).timestamp()
    lower_bound = lower_bound.timestamp()
    data_bits = db.session.query(DataBit).filter(
        (lower_bound <= DataBit.timestamp) & (DataBit.timestamp < upper_bound)
    )

    values = defaultdict(list)
    points = []
    for data_bit in data_bits:
        parsed_data = json.loads(data_bit.data)
        for label, data in parsed_data.items():
            values[data_bit.username, label].append(data)
    for ul, data in values.items():
        username, label = ul
        for ag in ags:
            x = upper_bound
            y = ag.process(data)
            points.append(LabelPoint(username, label + '.' + ag.name(), x, y))
    print('Points {}'.format(len(points)))

    for point in points:
        db.session.add(point)
    db.session.commit()



