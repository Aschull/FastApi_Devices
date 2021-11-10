from datetime import datetime


def converte_data(dt):
    if isinstance(dt, datetime):
        return dt.isoformat()