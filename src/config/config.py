import os
import json


class Config():
    DEFAULT_ENV = 'prod'

    @staticmethod
    def get_property(name):
        # define environment
        target = os.environ.get('TARGET', Config.DEFAULT_ENV)
        #target = os.environ['TARGET']  # another approach
        
        # read the proper json file
        path_to_config = f"./env_config/{target}.json"
        with open(path_to_config) as f:
            config_from_json = json.load(f)

        # get property name from parameter 'name'
        value = config_from_json.get(name)

        return value