import yaml
from utils.ConfigData import ConfigData

class ConfigService:
    @classmethod
    def get_clientData_instance(cls, yaml_file):
        with open(yaml_file, 'r') as conf:
            data = yaml.safe_load(conf)
            targets = {key: value for key, value in data.items() if key.startswith('backup-')}
            return ConfigData(data['token'], targets, data['dst-directory'])
