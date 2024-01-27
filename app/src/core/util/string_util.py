from typing import Any
import uuid
import hashlib

class StringUtil:
    @staticmethod
    def formatDocumentNumber(value: str) -> str:
        if len(value) == 11:
            return "{}.{}.{}-{}".format(value[:3], value[3:6], value[6:9], value[9:])
        else:
            return value
        
    @staticmethod
    def isEmpty(value: Any) -> bool:
        return not (value != None and value != "")

    # https://samos-it.com/posts/python-create-uuid-from-random-string-of-words.html
    @staticmethod
    def parseUUID(string: str) -> str:
        hex_string = hashlib.md5(string.encode("UTF-8")).hexdigest()
        return str(uuid.UUID(hex=hex_string))

    @staticmethod
    def validateUUID(stringUUID: str) -> bool:
        try:
            uuid.UUID(stringUUID)
            return True
        except ValueError as ex:
            return False

if __name__ == '__main__':
    print(StringUtil.parseUUID('password'))