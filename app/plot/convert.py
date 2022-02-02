# converts data from database tables to the list of data for aggregation
from datetime import datetime, timedelta
from app.libs import get_last_table
from app import engine


def convert(delta):
    table = get_last_table(delta)
    if engine.dialect.has_table(engine, table):
        pass
