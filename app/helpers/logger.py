import structlog
import datetime


def add_timestamp(_, __, event_dict):
    event_dict["timestamp"] = str(datetime.date.today())
    return event_dict


def add_log_level(_, name, event_dict):
    event_dict["level"] = name
    return event_dict


def map_event_to_msg(_, __, event_dict):
    event_dict["msg"] = event_dict['event']
    event_dict['event'] = None
    return event_dict


structlog.configure(
    processors=[
        add_timestamp,
        add_log_level,
        structlog.processors.dict_tracebacks,
        structlog.processors.JSONRenderer(),

    ])

log = structlog.get_logger()