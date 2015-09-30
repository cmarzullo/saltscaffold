
from nose.tools import *
from saltscaffold import formulafolders, formulafiles
import os
import shutil

target_dir = os.path.normpath(os.path.join(os.getcwd(),"testcruft"))

def setup():
    os.mkdir(target_dir) # temp dir for holding tests
    print("root test directory: {dir}".format(dir=target_dir))

def teardown():
    print("attempting to tear down: {dir}".format(dir=target_dir))
#    shutil.rmtree(target_dir)

def test_create_folder_path():
    sub_dir = "magicdir"
    expected_path = os.path.join(os.path.normpath(target_dir), sub_dir)
    resultant_path = formulafolders.create_path(target_dir, sub_dir)
    assert expected_path == resultant_path

def test_create_folders():
    formula_name = "waller"
    formulafolders.create_folders(formula_name, target_dir) # Create the formula folders
    
    assert_folder_exists(target_dir, formula_name + '-formula') # testcruft/waller-formula exists
    formula_root = os.path.join(target_dir, formula_name + '-formula')
   
    assert_folder_exists(formula_root, formula_name)            # testcruft/waller-formula/waller exists
    assert_folder_exists(formula_root, formula_name + '/files') # testcruft/waller-formula/waller exists

def test_create_files():
    formula_name = "salzburg"
    formulafolders.create_folders(formula_name, target_dir) # Create the formula folders
    formula_root = formulafolders.create_path(target_dir, formula_name + '-formula')
    
    # write out all the files in the root directory
    formulafiles.write_readme(formula_name, formula_root)
    formulafiles.write_gitignore(formula_name, formula_root)
    formulafiles.write_kitchenyml(formula_name, formula_root)
    formulafiles.write_pillarcustom(formula_name, formula_root)
    formulafiles.write_defaults(formula_name, formula_root)
    formulafiles.write_init(formula_name, formula_root)
    formulafiles.write_install(formula_name, formula_root)
    formulafiles.write_config(formula_name, formula_root)
    formulafiles.write_service(formula_name, formula_root)
    formulafiles.write_mapjinja(formula_name, formula_root)

    assert_file_exists(formula_root, None, 'README.md')
    assert_file_exists(formula_root, None, '.gitignore')
    assert_file_exists(formula_root, None, '.kitchen.yml')
    assert_file_exists(formula_root, None, 'pillar-custom.sls')
    assert_file_exists(formula_root, formula_name, 'defaults.yml')
    assert_file_exists(formula_root, formula_name, 'map.jinja')
    assert_file_exists(formula_root, formula_name, 'init.sls')
    assert_file_exists(formula_root, formula_name, 'install.sls')
    assert_file_exists(formula_root, formula_name, 'config.sls')
    assert_file_exists(formula_root, formula_name, 'service.sls')

def assert_file_exists(target_dir, sub_dir, filename):
    """Tests if a file exists  or not"""
    if sub_dir == None:
        assert os.path.exists(os.path.join(target_dir, filename))
    else:
        assert os.path.exists(os.path.join(os.path.join(target_dir, sub_dir), filename))


def assert_folder_exists(target_dir, sub_dir):
    """Tests to see if a particular folder exists"""
    assert os.path.exists(os.path.join(target_dir, sub_dir))
