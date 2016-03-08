from LSFBsubOptions import LSFBsubOptions
from LSFBsubCommand import LSFBsubCommand

print LSFBsubOptions.QUEUE_NAME.get_short_option()
print LSFBsubOptions.JOB_NAME.get_short_option()
print LSFBsubOptions.MIN_MAX_PROCESSORS.get_short_option()

lsf_options = dict(queueName="queue",max_proc=4)
lsf_command = LSFBsubCommand("ls -l", lsf_options)
print lsf_command.get_command()

import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)
print(data["max_memory"])
