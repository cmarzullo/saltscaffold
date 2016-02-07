# -*- coding: utf-8 -*-
# vim: ft=sls
# How to configure ${formula_name}
{%- from "${formula_name}/map.jinja" import ${formula_name} with context %}

${formula_name}_config:
  file.managed:
    - name: '/tmp/config.conf'
    - source: salt://${formula_name}/files/config.conf
    - user: root
    - group : root
    - mode: 0600
    - template: jinja
    - local_string: 'test string please ignore'

