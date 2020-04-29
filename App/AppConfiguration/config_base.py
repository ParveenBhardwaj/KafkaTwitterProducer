import json

class ConfigBase(object):
    def __init__(self, config_aggregation):
        self._config_aggregation = config_aggregation
        with open('App/config.json', 'r') as f:
            self._config = json.load(f)

    def get_property(self, property_name):
        if self._config_aggregation not in self._config.keys():
            return None
        if property_name not in self._config[self._config_aggregation].keys():
            return None
        return self._config[self._config_aggregation][property_name]