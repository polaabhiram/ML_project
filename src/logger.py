import logging 
from datetime import datetime
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.txt")

logging.basicConfig(
    filename=os.path.join("/Users/abhiram/Documents/ML_Students_performance/logs/",filename),
    format="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

logging.info("kdjnv")

