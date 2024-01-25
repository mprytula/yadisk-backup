from entity.Backup import Backup

# Возможно это модель, не знаю
class ConfigData:    
    def __init__(self, token, targets, destination):
        self.__token__ = token
        self.__destination__ = destination
        self.__backups__ = []

        for backup_name, backup_path in targets.items():
            self.__backups__.append(Backup(backup_name, backup_path, destination))
        
    def get_token(self):
        return self.__token__
    
    def get_backups(self):
        return self.__backups__
    
    def get_destination(self):
        return self.__destination__

    
    