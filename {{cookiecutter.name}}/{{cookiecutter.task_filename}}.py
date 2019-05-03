{%- for task in cookiecutter.tasks %}
from luigi import {{task.inherits_from}}
    {%- if task.parameters != "null" %}
        {%- for param in task.parameters %}
            {%- if param.classpath != "null" %}
from {{param.classpath}} import {{param.type}}
            {%- endif %}
        {%- endfor %}
    {%- endif %}
    {%- if task.requires != "null" %}
        {%- for req in task.requires %}
            {%- if req.classpath != "null" %}
from {{req.classpath}} import {{req.name}}
            {%- endif %}
        {%- endfor %}
    {%- endif %}
    {%- if task.requires != "None" %}
        {%- for out in task.outputs %}
            {%- if out.classpath != "null" %}
from {{out.classpath}} import {{out.name}}
            {%- endif %}
        {%- endfor %}
    {%- endif %}
{%- endfor %}
from pset_utils.luigi.task import *
from pset_utils.luigi.output import *
{%- for task in cookiecutter.tasks %}


class {{task.name}}({{task.inherits_from}}):
    __version__ = '1.0.0'
    _id = {{task.id}}
    {%- if task.parameters != "None" %}
        {%- for param in task.parameters %}
    {{param.name}} = {{param.type}}()
        {%- endfor %}
    {%- endif %}

    {%- if task.requires != "None" %}
    requires = Requires()
        {%- for req in task.requires %}
    {{req.name.lower()}} = Requirement({{req.name}})
        {%- endfor %}
    {%- endif %}

    {%- if task.outputs.salted %}
    output = SaltedOutput(base_dir="data", target_class={{task.outputs.name}})
    {%- else %}
    output = TargetOutput(base_dir="data", target_class={{task.outputs.name}})
    {%- endif %}

    # IMPLEMENT YOUR RUN
    def run(self):
        raise NotImplementedError
{%- endfor %}


