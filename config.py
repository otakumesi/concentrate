import os
import yaml

DEFAULT_USER_HOSTS_PATH = os.path.join('~', '.concentrate.hosts.yml')
DEFAULT_RECORD_IDENTIFIER = ' # WRITE_BY_CONCENTRATE'


class Config():
    def __init__(self, src_path):
        yaml_path = os.path.expanduser(src_path)
        self.yaml = self.__load_yaml(yaml_path)

    def extract_forbidden_hosts(self):
        return self.yaml['forbidden_hosts']

    def __load_yaml(self, yaml_file):
        yaml_dic = {}
        with open(yaml_file) as raw_yaml:
            yaml_dic = yaml.load(raw_yaml.read())
        return yaml_dic
