import os
import yaml

DEFAULT_USER_HOSTS_PATH = os.path.join('~', '.concentrate.hosts.yml')
DEFAULT_RECORD_IDENTIFIER = ' # WRITE_BY_CONCENTRATE'


class Config():
    def __init__(self, src_path):
        yaml_path = os.path.expanduser(src_path)
        self.yaml = self.__load_yaml(yaml_path)

    @property
    def dirty_hosts(self):
        return self.yaml.get('forbidden_hosts', [])

    @property
    def identifier(self):
        return DEFAULT_RECORD_IDENTIFIER

    def __load_yaml(self, yaml_file):
        yaml_dic = {}
        with open(yaml_file) as raw_yaml:
            yaml_dic = yaml.load(raw_yaml.read())
        return yaml_dic


def load(args):
    config = Config(src_path=DEFAULT_USER_HOSTS_PATH)
    return config
