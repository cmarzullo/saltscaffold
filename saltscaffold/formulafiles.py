"""better way to create salt files"""
import os
from saltscaffold import formulafolders
import subprocess
from mako.template import Template

def create_files(formula_name, formula_root):
    """Creates all files for the formula scaffold"""
    root_dir = formulafolders.create_path(formula_root, formula_name + "-formula")

    write_file(formula_name, formula_root, None, "README.md", " +++")
    write_file(formula_name, formula_root, None, "LICENSE.txt", " +++")
    write_file(formula_name, formula_root, None, ".gitignore", " +++")
    write_file(formula_name, formula_root, None, ".kitchen.yml", " +++")
    write_file(formula_name, formula_root, None, ".kitchen-ci.yml", " +++")
    write_file(formula_name, formula_root, None, "pillar-custom.sls", " +++")
    write_file(formula_name, formula_root, "formula", "map.jinja", " +++")
    write_file(formula_name, formula_root, "formula", "init.sls", " +++")
    write_file(formula_name, formula_root, "formula", "install.sls", " +++")
    write_file(formula_name, formula_root, "formula", "config.sls", " +++")
    write_file(formula_name, formula_root, "formula", "service.sls", " +++")
    write_file(formula_name, formula_root, "formula/files", "config.conf", " +++")
    write_file(formula_name, formula_root, "test/integration/default/serverspec", "_spec.rb", " +++")

def write_file(formula_name, formula_root, sub_dir, file_name, prefix):
    """Writes sample formula file"""

    # read in template
    if sub_dir is None:
        out_dir = sub_dir
        template_path = file_name
    else:
        out_dir = sub_dir.replace("formula", formula_name)
        template_path = sub_dir + "/" + file_name
    
    template = Template(filename="saltscaffold/skel/" + template_path)

    # write out template
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
    
    #Otherwise, build out the appropriate path for the subdirectory
    path_ = formulafolders.create_path(root_dir, sub_dir)
    filepath = os.path.join(path_, filename)
    return os.path.normpath(filepath)

