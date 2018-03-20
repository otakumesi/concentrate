import os
import re
from itertools import filterfalse
from utils import load_yaml


def core(args):
    pass


class Concentrate:
    DEFAULT_HOSTS_PATH = os.path.join('~', '.concentrate.hosts.yml')
    DEFAULT_RECORD_IDENTIFIER = ' # WRITE_BY_CONCENTRATE'

    def __init__(self,
                 yaml_file_name=DEFAULT_HOSTS_PATH,
                 identifier=DEFAULT_RECORD_IDENTIFIER):
        self.identifier = identifier
        self.forbidden_hosts_record = self.__build_hosts_record(yaml_file_name)

    def write_etc_hosts(self):
        with open('/etc/hosts', 'a+') as f:
            f.write(self.forbidden_hosts_record + self.identifier)

    def clean(self):
        filtered_lines = self.__remove_concentrate_record()
        if not filtered_lines:
            with open('/etc/hosts', 'w') as f:
                f.writelines(filtered_lines)

    def __concentrate_record(self):
        return filterfalse(
            lambda line: re.search(Concentrate.ADD_RECORD_IDENTIFIER, line),
            self.__current_etc_hosts())

    def __current_etc_hosts(self):
        with open('/etc/hosts', 'r+') as f:
            return f.readlines()

    def __build_forbidden_hosts_record(self, yaml_file_name):
        yaml_path = os.path.expanduser(yaml_file_name)
        settings_dic = load_yaml(yaml_path)
        over_write_hosts = settings_dic['forbidden_hosts']
        joined_forbidden_hosts = ' '.join(over_write_hosts)
        return '127.0.0.1 ' + joined_forbidden_hosts
