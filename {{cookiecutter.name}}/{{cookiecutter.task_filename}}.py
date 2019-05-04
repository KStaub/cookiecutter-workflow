{%- for task in cookiecutter.tasks.task_list %}
from luigi import {{task.inherits_from.split(".")[-1]}}
    {%- if task.parameters is defined %}
        {%- for param in task.parameters %}
            {%- if param.classpath is not none %}
from {{param.classpath}} import {{param.type}}
            {%- endif %}
        {%- endfor %}
    {%- endif %}
    {%- if task.requires is not none %}
        {%- if task.requires.classpath is not none %}
from {{task.requires.classpath}} import {{task.requires.name}}
        {%- endif %}
    {%- endif %}
    {%- if task.outputs is not none %}
        {%- if task.outputs.classpath is not none %}
from {{task.outputs.classpath}} import {{task.outputs.name}}
        {%- endif %}
    {%- endif %}
{%- endfor %}
from pset_utils.luigi.task import *
from pset_utils.luigi.output import *
{%- for task in cookiecutter.tasks.task_list %}


class {{task.name}}({{task.inherits_from.split(".")[-1]}}):
    """
    TODO
    """
    __version__ = '1.0.0'
    _id = {{task.id}}
    {%- if task.parameters is defined %}
        {%- for param in task.parameters %}
    {{param.name}} = {{param.type}}()
        {%- endfor %}
    {%- endif %}

    {%- if task.requires is not none %}
    requires = Requires()
    {{task.requires.name.lower()}} = Requirement({{task.requires.name}})
    {%- endif %}

    {%- if task.outputs.salted %}
    output = SaltedOutput(base_dir="data", target_class={{task.outputs.name}})
    {%- else %}
    output = TargetOutput(base_dir="data", target_class={{task.outputs.name}})
    {%- endif %}


    def run(self):
        """
        TODO
        Implement your task's run() here
        """
        raise NotImplementedError
{%- endfor %}


