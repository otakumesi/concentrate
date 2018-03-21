import re
from itertools import filterfalse
from config import DEFAULT_USER_HOSTS_PATH, DEFAULT_RECORD_IDENTIFIER, Config


def core(args):
    conf = Config(DEFAULT_USER_HOSTS_PATH)
    EtcHostsModifier(conf.over_write_hosts)


class EtcHostsModifier:

    def __init__(self,
                 over_write_hosts,
                 identifier=DEFAULT_RECORD_IDENTIFIER):
        self.identifier = identifier
        self.over_write_hosts = over_write_hosts

    def forbidden_hosts_record(self):
        return self._build_hosts_record(self.over_write_hosts)

    def _build_forbidden_hosts_record(self, over_write_hosts):
        joined_forbidden_hosts = ' '.join(over_write_hosts)
        return '127.0.0.1 ' + joined_forbidden_hosts

    def write(self):
        with open('/etc/hosts', 'a+') as f:
            f.write(self.forbidden_hosts_record() + self.identifier)

    def clean(self):
        filtered_lines = self._etc_hosts_exclude_added_record()
        if not filtered_lines:
            with open('/etc/hosts', 'w') as f:
                f.writelines(filtered_lines)

    def _etc_hosts_exclude_added_record(self):
        return filterfalse(
            lambda line: re.search(DEFAULT_RECORD_IDENTIFIER, line),
            self._current_etc_hosts())

    def _current_etc_hosts(self):
        with open('/etc/hosts', 'r+') as f:
            return f.readlines()
