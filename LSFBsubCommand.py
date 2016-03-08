class GenericJobCommand(object):
    def __init__(self, job_scheduler_command, *options):
        self._job_scheduler_command = job_scheduler_command
        self._options = options

    def get_job_scheduler_command(self):
        return self._job_scheduler_command

    def get_options(self):
        return self._options


class LSFBsubCommand(GenericJobCommand):
    WHITESPACE = " "

    def __init__(self, system_command, *lsf_options):
        super(self.__class__, self).__init__("bsub", lsf_options)
        self._system_command = system_command

    def get_command(self):
        command = (self.get_job_scheduler_command(), self.WHITESPACE, self._system_command)
        return "".join(command)
