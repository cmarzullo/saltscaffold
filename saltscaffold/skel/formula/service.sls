# -*- coding: utf-8 -*-
# vim: ft=sls
# Manage service for service ${formula_name}
{%- from "${formula_name}/map.jinja" import ${formula_name} with context %}

'${formula_name}-service not configured':
  test.succeed_without_changes

#${formula_name}_service:
#  service.running:
#    - name: ${formula_name}
#    - enable: True
#    - watch:
#        - file: ${formula_name}_config

