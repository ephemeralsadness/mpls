# converts data from database tables to the list of data for aggregation
from app import db
from app.libs import round_down_datetime, round_up_datetime
from app.models import DataBit

import numpy as np
import json
from collections import defaultdict
from datetime import datetime


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


class MaxAG:
    def process(self, data):
        return max(data)

    def name(self):
        return 'max'


class MinAG:
    def process(self, data):
        return min(data)

    def name(self):
        return 'min'


class AverageAG:
    def process(self, data):
        return np.average(data)

    def name(self):
        return 'average'


def convert(delta):
    dt = datetime.now()
    ags = [
        QuantileAG(10.0),
        QuantileAG(90.0),
        QuantileAG(50.0),
        MaxAG,
        MinAG,
        AverageAG,
    ]

    lower_bound = round_down_datetime(dt, delta).timestamp()
    upper_bound = round_up_datetime(dt, delta).timestamp()
    data_bits = db.session.query(DataBit).filter(
        (lower_bound <= DataBit.timestamp) & (DataBit.timestamp < upper_bound)
    )

    values = defaultdict(list)
    plots = []
    for data_bit in data_bits:
        parsed_data = json.loads(data_bit.data)
        for label_name, data in parsed_data.items():
            values[data_bit.username, label_name].append(data)
    for ul, data in values.items():
        username, label_name = ul
        for ag in ags:
            plots.append((username, label_name, ag.process(data)))

    return plots


