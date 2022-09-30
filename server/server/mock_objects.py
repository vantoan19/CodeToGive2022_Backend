import json

mock_objects = None

with open("mock_data.json","r") as readfile:
    mock_objects = json.load()
