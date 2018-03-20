import yaml
import os


CONCENTRATE_HOSTS_YML_PATH = os.path.expanduser(
        os.path.join('~', '.concentrate.hosts.yml'))


def run():
    with open('/etc/hosts', 'a+') as f:
        contents = f.read()
        print(contents)

        settings_dic = load_yaml(CONCENTRATE_HOSTS_YML_PATH)
        over_write_hosts = settings_dic['forbidden_hosts']
        joined_forbidden_hosts = ' '.join(over_write_hosts)
        forbidden_hosts_record = '127.0.0.1 ' + joined_forbidden_hosts
        f.write(forbidden_hosts_record)

        contents = f.read()
        print(contents)


def load_yaml(yaml_file):
    yaml_dic = {}
    with open(yaml_file) as raw_yaml:
        yaml_dic = yaml.load(raw_yaml.read())
    return yaml_dic


if __name__ == '__main__':
    run()
