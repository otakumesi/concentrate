import re
from itertools import filterfalse
from config import load


def program(args):
    conf = load(args)
    etc_hosts = EtcHostsModifier(
            dirty_hosts=conf.dirty_hosts,
            identifier=conf.identifier)
    etc_hosts.run()


class EtcHostsModifier:
    ETC_HOSTS_DIR = '/etc/hosts'

    def __init__(self,
                 dirty_hosts,
                 identifier):
        self.identifier = identifier
        self.dirty_hosts = dirty_hosts

    def forbid_hosts_record(self):
        return self._build_forbidden_hosts_record(self.dirty_hosts)

    def _build_forbidden_hosts_record(self, dirty_hosts):
        joined_forbidden_hosts = ' '.join(dirty_hosts)
        return '127.0.0.1 ' + joined_forbidden_hosts

    def run(self):
        if not self.is_executed():
            self._write()
        else:
            self._clean()

    def _write(self):
        with open(self.ETC_HOSTS_DIR, 'a+') as f:
            f.write(self.forbid_hosts_record() + self.identifier)

    def _clean(self):
        filtered_lines = self._etc_hosts_exclude_added_record()
        if filtered_lines:
            with open(self.ETC_HOSTS_DIR, 'w') as f:
                f.writelines(filtered_lines)

    def is_executed(self):
        return re.search(self.identifier, self._current_etc_hosts)

    def _etc_hosts_exclude_added_record(self):
        return filterfalse(
            lambda line: re.search(self.identifier, line),
            self._current_etc_hosts_lines)

    @property
    def _current_etc_hosts_lines(self):
        with open(self.ETC_HOSTS_DIR, 'r+') as f:
            return f.readlines()

    @property
    def _current_etc_hosts(self):
        with open(self.ETC_HOSTS_DIR, 'r+') as f:
            return f.read()
