# -*- coding: utf-8 -*-
# vim: ft=sls
# How to install ${formula_name}
{%- from "${formula_name}/map.jinja" import ${formula_name} with context %}

${formula_name}_pkg:
  pkg.installed:
    - name: {{ ${formula_name}.pkg }}

