# tests/test_distance.py
from ourfinalweek.distance import haversine

def test_of_haversine():
    assert haversine(2.380009, 48.865070, 13.43895252, 52.5144253) == 877.1052367861414