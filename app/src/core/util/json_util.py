import json
import dataclasses
from datetime import datetime

class JsonUtil():
    @staticmethod    
    def parseObjectToJson(object):
        return json.dumps(object, cls=JSONEncoder)
            

class JSONEncoder(json.JSONEncoder):
    def default(self, object):
            if (dataclasses.is_dataclass(object)):
                return dataclasses.asdict(object)
            return super().default(object)
