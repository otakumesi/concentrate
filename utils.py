import yaml


def load_yaml(yaml_file):
    yaml_dic = {}
    with open(yaml_file) as raw_yaml:
        yaml_dic = yaml.load(raw_yaml.read())
    return yaml_dic
