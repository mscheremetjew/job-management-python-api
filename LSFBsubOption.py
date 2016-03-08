def enum(**enums):
    return type('Enum', (), enums)


class LSFBsubOption(object):
    def __init__(self, short_option, description, argument_required):
        self._short_option = short_option
        self._description = description
        self._argument_required = argument_required

    def get_short_option(self):
        return self._short_option

    def get_description(self):
        return self._description

    def get_argument_required(self):
        return self._argument_required


class QueueName(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)

class JobName(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)

class MinMaxProcessor(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)



queue_name = QueueName("-q", "Name of the queue you like to submit", True)
job_name = JobName("-J", "job_name", True)
processor = MinMaxProcessor("-n", "min_proc[,max_proc]", True)

LSFBsubOptions = enum(QUEUE_NAME=queue_name, JOB_NAME=job_name,MIN_MAX_PROCESSORS= processor)

print LSFBsubOptions.QUEUE_NAME.get_short_option()
print LSFBsubOptions.JOB_NAME.get_short_option()
print LSFBsubOptions.MIN_MAX_PROCESSORS.get_short_option()
