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


class JobDescription(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


class MinMaxProcessor(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


class MaxMemory(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


class ResourceRequirement(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


class StdOutputFile(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


class StdErrorOutputFile(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


class ProjectName(LSFBsubOption):
    def __init__(self, short_option, description, argument_required):
        super(self.__class__, self).__init__(short_option, description, argument_required)


queue_name = QueueName("-q", "Name of the queue you like to submit", True)
job_name = JobName("-J", "job_name", True)
job_desc = JobDescription("-Jd", "job_description", True)
processor = MinMaxProcessor("-n", "min_proc[,max_proc]", True)
max_memory = MaxMemory("-M", "memory limit", True)
resrc_requirement = ResourceRequirement("-R", "resource requirement, e.g. for memory 'rusage[mem=6000]'", True)
std_output_file = StdOutputFile("-o", "output_file", True)
std_error_output_file = StdErrorOutputFile("-e", "error_file", True)
project_name = ProjectName("-P", "project_name", True)

LSFBsubOptions = enum(QUEUE_NAME=queue_name, JOB_NAME=job_name, JOB_DESC=job_desc, MIN_MAX_PROCESSORS=processor,
                      MAX_MEMORY=max_memory, RESOURCE_REQUIREMENT=resrc_requirement, PROJECT_NAME=project_name,
                      STD_OUTPUT_FILE=std_output_file, STD_ERROR_OUTPUT_FILE=std_error_output_file)