# -*- coding: utf-8 -*-
# vim: ft=sls
# Init ${formula_name}
{%- from "${formula_name}/map.jinja" import ${formula_name} with context %}
{# Below is an example of having a toggle for the state #}

{% if ${formula_name}.enabled %}
include:
  - ${formula_name}.install
  - ${formula_name}.config
  - ${formula_name}.service
{% else %}
'${formula_name}-formula disabled':
  test.succeed_without_changes
{% endif %}

