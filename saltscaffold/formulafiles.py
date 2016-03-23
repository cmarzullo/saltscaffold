"""better way to create salt files"""
import os
import sys
from saltscaffold import formulafolders
import subprocess
from mako.template import Template

def create_files(formula_name, formula_root):
    """Creates all files for the formula scaffold"""
    root_dir = formulafolders.create_path(formula_root, formula_name + "-formula")

    write_file(formula_name, root_dir, None, "README.md", " +++")
    write_file(formula_name, root_dir, None, "LICENSE.txt", " +++")
    write_file(formula_name, root_dir, None, ".gitignore", " +++")
    write_file(formula_name, root_dir, None, ".kitchen.yml", " +++")
    write_file(formula_name, root_dir, None, ".kitchen-ci.yml", " +++")
    write_file(formula_name, root_dir, None, "pillar-custom.sls", " +++")
    write_file(formula_name, root_dir, None, "Gemfile", " +++")
    write_file(formula_name, root_dir, "formula", "defaults.yml", " +++")
    write_file(formula_name, root_dir, "formula", "map.jinja", " +++")
    write_file(formula_name, root_dir, "formula", "init.sls", " +++")
    write_file(formula_name, root_dir, "formula", "install.sls", " +++")
    write_file(formula_name, root_dir, "formula", "config.sls", " +++")
    write_file(formula_name, root_dir, "formula", "service.sls", " +++")
    write_file(formula_name, root_dir, "formula/files", "config.conf", " +++")
    write_file(formula_name, root_dir, "test/integration/default/serverspec", "_spec.rb", " +++")

def write_file(formula_name, formula_root, sub_dir, file_name, prefix):
    """Writes sample formula file"""

    # read in template
    if sub_dir is None:
        out_dir = sub_dir
        template_path = file_name
    else:
        out_dir = sub_dir.replace("formula", formula_name)
        template_path = os.path.join(sub_dir, file_name)
    
    template_prefix = os.path.join(os.path.dirname(__file__), "skel")
    template = Template(filename=os.path.join( template_prefix, template_path))

    path = get_file_path(formula_root, out_dir, file_name)
    with open(path, "w") as file_out:
        file_out.write(template.render(formula_name=formula_name))

    # print output
    print_file(path, prefix)

def print_file(path, prefix=" ++++++"):
    print(
    "create: {prefix} {path_}".format( prefix=prefix,path_=os.path.abspath(path)))

def get_file_path(root_dir, sub_dir, filename):
    if sub_dir == None: #In case we're writing directly to the root directory
        return os.path.normpath(os.path.join(root_dir, filename))
    
    # Otherwise, build out the appropriate path for the subdirectory
    path_ = formulafolders.create_path(root_dir, sub_dir)
    filepath = os.path.join(path_, filename)
    return os.path.normpath(filepath)

