{%- for task in cookiecutter.tasks.task_list %}
from luigi import {{task.task_inherits}}
{%- if task.task_parameters != "None" %}
{%- for param in task.task_parameters %}
from luigi import {{param.param_type}}
{%- endfor %}
{%- endif %}
{%- endfor %}

from pset_utils.luigi.task import *
from pset_utils.luigi.output import *
{%- for task in cookiecutter.tasks.task_list %}


class {{task.task_name}}({{task.task_inherits}}):
    __version__ = '1.0.0'
    {%- if task.task_parameters != "None" %}
    {%- for param in task.task_parameters %}
    {{param.param_name}} = {{param.param_type}}(default={{param.default_value}})
    {%- endfor %}
    {%- endif %}

    {%- if task.task_requires != "None" %}
    requires = Requires()
    {%- for req in task.task_requires %}
    {{req.req_name}} = Requirement({{req.req_class}})
    {%- endfor %}
    {%- endif %}

    {%- if task.task_outputs.salted %}
    output = SaltedOutput(base_dir="data", target_class={{task.task_outputs.target_class}})
    {%- else %}
    output = TargetOutput(base_dir="data", target_class={{task.task_outputs.target_class}})
    {%- endif %}

    def run(self):
        raise NotImplementedError
{%- endfor %}


