import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
FIELDS_NAME = ("Статус", "Количество")

DT_FORMAT = "%Y-%m-%dT%H-%M-%S"
FILE_NAME = "status_summary_{time}.csv"
CUR_TIME = dt.datetime.now().strftime(DT_FORMAT)
