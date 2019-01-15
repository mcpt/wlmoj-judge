from .base_executor import CompiledExecutor
from dmoj.judgeenv import env


class Executor(CompiledExecutor):
    ext = '.t'
    name = 'TUR'
    command = 'tprologc'
    test_program = '''\
var echo : string
get echo : *
put echo
'''

    def get_fs(self):
        return super(Executor, self).get_fs() + [self._code + 'bc']

    def get_compile_args(self):
        return [self.get_command(), self._code, '/opt/turing/']

    def get_cmdline(self):
        return ['/usr/local/bin/tprolog', self._code + 'bc']

    def get_executable(self):
        return None

    @classmethod
    def initialize(cls, sandbox=True):
#        if 'tprolog' not in env['runtime'] or 'tprologc' not in env['runtime'] or 'turing_dir' not in env['runtime']:
#            return False
        return super(Executor, cls).initialize(sandbox=sandbox)
