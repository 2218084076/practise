import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')
settings = {
    "static_path": os.path.join(os.path.dirname(__file__),"static"),
    "debug":True,
}