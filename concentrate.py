import yaml
import os
import re
from itertools import filterfalse


CONCENTRATE_HOSTS_YML_PATH = os.path.expanduser(
        os.path.join('~', '.concentrate.hosts.yml'))
ADD_RECORD_IDENTIFIER = ' # WRITE_BY_CONCENTRATE'


def run():
    # write_etc_hosts()
    remove_concentrate_record()


def init():
    pass


def current_etc_hosts():
    lines = []
    with open('/etc/hosts', 'r+') as f:
        lines = f.readlines()
    return lines


def write_etc_hosts():
    with open('/etc/hosts', 'a+') as f:
        settings_dic = load_yaml(CONCENTRATE_HOSTS_YML_PATH)
        over_write_hosts = settings_dic['forbidden_hosts']
        joined_forbidden_hosts = ' '.join(over_write_hosts)
        forbidden_hosts_record = '127.0.0.1 ' + joined_forbidden_hosts
        f.write(forbidden_hosts_record + ADD_RECORD_IDENTIFIER)


def remove_concentrate_record():
    filtered_lines = []
    with open('/etc/hosts', 'r+') as f:
        lines = f.readlines()
        filtered_lines = list(filterfalse(
                lambda line: re.search(ADD_RECORD_IDENTIFIER, line),
                lines))
    if not(filtered_lines):
        return
    with open('/etc/hosts', 'w') as f:
        f.writelines(filtered_lines)


def load_yaml(yaml_file):
    yaml_dic = {}
    with open(yaml_file) as raw_yaml:
        yaml_dic = yaml.load(raw_yaml.read())
    return yaml_dic


if __name__ == '__main__':
    run()
