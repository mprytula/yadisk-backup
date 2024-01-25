from datetime import datetime
import os
from utils.extract_extension import extract_extension

class Backup:
    def __init__(self, file_name, target_path, dst_path):
        self.__path__ = target_path

        _, file_extension = os.path.splitext(target_path)
        timestamp = datetime.now().strftime('%d-%m-%Y')
        
        self.__dst_path__ = (
            dst_path + file_name + '-' 
            + timestamp + extract_extension(target_path)
        )

        print("[DESTINATION PATH] " + self.__dst_path__)

    def get_path(self):
        return self.__path__
    def get_dst_path(self):
        return self.__dst_path__