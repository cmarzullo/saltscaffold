"""crappy way to create salt files"""
import os
from saltscaffold import formulafolders
from textwrap import dedent
import subprocess

def create_files(formula_name, root_dir):
    """Creates all files for the formula scaffold"""
    root_dir = formulafolders.create_path(root_dir, formula_name + '-formula')

    write_readme(formula_name, root_dir)
    write_gitignore(formula_name, root_dir)
    write_kitchenyml(formula_name, root_dir)
    write_pillarcustom(formula_name, root_dir)
    write_defaults(formula_name, root_dir)
    write_mapjinja(formula_name, root_dir)
    write_init(formula_name, root_dir)
    write_install(formula_name, root_dir)
    write_config(formula_name, root_dir)
    write_service(formula_name, root_dir)

def write_readme(formula_name, root_dir):
    """Writes sample README.md"""
    readme_path = get_file_path(root_dir, None, 'README.md')
    readme_content = get_readme_text(formula_name)
    with open(readme_path, "w") as readme_file:
        readme_file.write(readme_content)
    print_file(readme_path, " +++")

def write_gitignore(formula_name, root_dir):
    """Writes sample .gitignore"""
    gitignore_path = get_file_path(root_dir, None, '.gitignore')
    gitignore_content = get_gitignore_text(formula_name)
    with open(gitignore_path, "w") as gitignore_file:
        gitignore_file.write(gitignore_content)
    print_file(gitignore_path, " +++")

def write_kitchenyml(formula_name, root_dir):
    """Writes sample .kitchenyml"""
    kitchenyml_path = get_file_path(root_dir, None, '.kitchen.yml')
    kitchenyml_content = get_kitchenyml_text(formula_name)
    with open(kitchenyml_path, "w") as kitchenyml_file:
        kitchenyml_file.write(kitchenyml_content)
    print_file(kitchenyml_path, " +++")

def write_pillarcustom(formula_name, root_dir):
    """Writes sample pillar-custom.sls"""
    pillarcustom_path = get_file_path(root_dir, None, 'pillar-custom.sls')
    pillarcustom_content = get_pillarcustom_text(formula_name)
    with open(pillarcustom_path, "w") as pillarcustom_file:
        pillarcustom_file.write(pillarcustom_content)
    print_file(pillarcustom_path, " +++")

def write_defaults(formula_name, root_dir):
    """Writes sample defaults.yml"""
    defaults_path = get_file_path(root_dir, formula_name, 'defaults.yml')
    defaults_content = get_defaults_text(formula_name)
    with open(defaults_path, "w") as defaults_file:
        defaults_file.write(defaults_content)
    print_file(defaults_path, " +++")

def write_mapjinja(formula_name, root_dir):
    """Writes sample mapjinja.yml"""
    mapjinja_path = get_file_path(root_dir, formula_name, 'map.jinja')
    mapjinja_content = get_mapjinja_text(formula_name)
    with open(mapjinja_path, "w") as mapjinja_file:
        mapjinja_file.write(mapjinja_content)
    print_file(mapjinja_path, " +++")

def write_init(formula_name, root_dir):
    """Writes sample init.sls"""
    init_path = get_file_path(root_dir, formula_name, 'init.sls')
    init_content = get_init_text(formula_name)
    with open(init_path, "w") as init_file:
        init_file.write(init_content)
    print_file(init_path, " +++")

def write_install(formula_name, root_dir):
    """Writes sample install.sls"""
    install_path = get_file_path(root_dir, formula_name, 'install.sls')
    install_content = get_install_text(formula_name)
    with open(install_path, "w") as install_file:
        install_file.write(install_content)
    print_file(install_path, " +++")

def write_config(formula_name, root_dir):
    """Writes sample config.sls"""
    config_path = get_file_path(root_dir, formula_name, 'config.sls')
    config_content = get_config_text(formula_name)
    with open(config_path, "w") as config_file:
        config_file.write(config_content)
    print_file(config_path, " +++")

def write_service(formula_name, root_dir):
    """Writes sample service.sls"""
    service_path = get_file_path(root_dir, formula_name, 'service.sls')
    service_content = get_service_text(formula_name)
    with open(service_path, "w") as service_file:
        service_file.write(service_content)
    print_file(service_path, " +++")

def print_file(path, prefix=" ++++++"):
    print(
    "create: {prefix} {path_}".format( prefix=prefix,path_=os.path.abspath(path)))

def get_file_path(root_dir, sub_dir, filename):
    if sub_dir == None: #In case we're writing directly to the root directory
        return os.path.normpath(os.path.join(root_dir, filename))
    
    #Otherwise, build out the appropriate path for the subdirectory
    path_ = formulafolders.create_path(root_dir, sub_dir)
    filepath = os.path.join(path_, filename)
    return os.path.normpath(filepath)

def get_init_text(formula_name):
    # TODO switch to a jinja template
    init_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=sls
        # Init {formula_name}
        {{%- from "{formula_name}/map.jinja" import {formula_name} with context %}}

        {{% if {formula_name}.enabled %}}
        include:
          - {formula_name}.install
          - {formula_name}.config
          - {formula_name}.service
        {{% else %}}
        '{formula_name}-formula disabled':
          test.succeed_without_changes
        {{% endif %}}
        """.format(formula_name=formula_name)

    return dedent(init_text)

def get_install_text(formula_name):
    # TODO switch to a jinja template
    install_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=sls
        # How to install {formula_name}
        {{%- from "{formula_name}/map.jinja" import {formula_name} with context %}}

        {formula_name}_pkg:
          pkg.installed:
            - name: {{{{ {formula_name}.pkg }}}}
        """.format(formula_name=formula_name)

    return dedent(install_text)

def get_config_text(formula_name):
    # TODO switch to a jinja template
    config_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=sls
        # How to configure {formula_name}
        {{%- from "{formula_name}/map.jinja" import {formula_name} with context %}}

        {formula_name}_config:
          file.managed:
            - name: '/tmp/{formula_name}.conf
            - source: salt://{formula_name}/files/{formula_name}_options.conf.j2
            - user: root
            - group : root
            - mode: 0600
            - template: jinja
            - local_string: 'test string please ignore'
        """.format(formula_name=formula_name)

    return dedent(config_text)

def get_service_text(formula_name):
    # TODO switch to a jinja template
    service_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=sls
        # Manage service for service {formula_name}
        {{%- from "{formula_name}/map.jinja" import {formula_name} with context %}}

        '{formula_name}-service not configured':
          test.succeed_without_changes

        #{formula_name}_service:
        #  service.running:
        #    - name: {formula_name}
        #    - enable: True
        #    - watch:
        #        - file: {formula_name}_config
        """.format(formula_name=formula_name)

    return dedent(service_text)

def get_defaults_text(formula_name):
    # TODO switch to a jinja template
    defaults_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=yaml
        # Defaults for {formula_name}

        {formula_name}:
          enable: true
          pkg: screen
        """.format(formula_name=formula_name)

    return dedent(defaults_text)

def get_mapjinja_text(formula_name):
    # TODO switch to a jinja template
    mapjinja_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=jinja
        # This file handles the merging of pillar data with the data from defaults

        {{## Start with  defaults from defaults.sls ##}}
        {{% import_yaml '{formula_name}/defaults.yaml' as default_settings %}}
        
        {{## 
        Setup variable using grains['os_family'] based logic, only add key:values here
        that differ from whats in defaults.yaml
        ##}}
        {{% set os_family_map = salt['grains.filter_by']({{
                'Debian': {{}},
                'Suse': {{}},
                'Arch': {{}},
                'RedHat': {{}},
          }}
          , grain="os_family"
          , merge=salt['pillar.get']('{formula_name}:lookup'))
        %}}
        {{## Merge the flavor_map to the default settings ##}}
        {{% do default_settings.{formula_name}.update(os_family_map) %}}
        
        {{## Merge in template:lookup pillar ##}}
        {{% set {formula_name} = salt['pillar.get'](
                '{formula_name}',
                default=default_settings.{formula_name},
                merge=True
            )
        %}}
        """.format(formula_name=formula_name)

    return dedent(mapjinja_text)

def get_pillarcustom_text(formula_name):
    # TODO switch to a jinja template
    pillarcustom_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=yaml
        # Custom Pillar Data for {formula_name}

        {formula_name}:
          enable: false
        """.format(formula_name=formula_name)

    return dedent(pillarcustom_text)

def get_kitchenyml_text(formula_name):
    # TODO switch to a jinja template
    kitchenyml_text = """
        # -*- coding: utf-8 -*-
        # vim: ft=yaml
        ---
        driver:
          name: vagrant
          customize: 
            memory: 1024

        provisioner:
          name: salt_solo
          salt_bootstrap_options: -P
          formula: {formula_name}
          state_top:
            base:
              "*":
                - {formula_name}
        
        platforms:
          - name: bento/debian-7.8
        
        suites:
          - name: default
        
          - name: custom
            provisioner:
              pillars-from-files:
                {formula_name}.sls: pillar-custom.sls
              pillars:
                top.sls:
                  base:
                    "*":
                      - {formula_name}
        """.format(formula_name=formula_name)

    return dedent(kitchenyml_text)

def get_gitignore_text(formula_name):
    gitignore_text = """
        .kitchen
        .kitchen.local.yml
        .vagrant
        """
    return dedent(gitignore_text)

def get_readme_text(formula_name):
    readme_text = """
        # {formula_name}-formula
        
        Purpose of formula. Include a short description of what the formula does.
        
        ## Available states
        
        Describe in a readable form the states this formula supports with examples how to use those states. 

        ## How to use test-kitchen on MacOSX
        
        Install and setup brew:
        ```
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        ```
        
        Install vagrant with brew:
        ```
        brew install cask
        brew cask install vagrant
        ```
        
        Install test-kitchen:
        ```
        sudo gem install test-kitchen
        sudo gem install kitchen-vagrant
        sudo gem install kitchen-salt
        ```
        
        Run a converge on the default configuration:
        ```
        kitchen converge default
        ```
    """.format(formula_name=formula_name)

    return dedent(readme_text)

