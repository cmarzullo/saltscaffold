"""Creates the folder skeleton for a new salt formula"""
import os
from textwrap import dedent

def create_folders(formula_name, current_directory):
    """Creates all the required folders"""
    root_dir = create_path(current_directory, formula_name + '-formula')

    if os.path.exists(root_dir) and os.listdir(root_dir):
        # if the path exists and isn't empty raise an error
        err_msg = '''
            {directory} already exists and it is not empty.

            Please try a different formula name or root directory.

            '''.format(directory=root_dir)

        raise IOError(000, dedent(err_msg))
    else:
        make_folder(root_dir) # create the formula root directory

    dirnames = (formula_name, 
                formula_name + '/files',
                'test/integration/default/serverspec',
                'test/mockup/files')

    # create the rest of the directories needed
    for item in dirnames:
        directory = create_path(root_dir, item)
        make_folder(directory, ' +++')

def make_folder(path, prefix=''):
    """Creates the directory and print message"""
    os.makedirs(path)

    if os.path.exists(path) is False: # if we can't make directory
        err_msg = 'Unable to create root direcotry {path_}. Unknown error!'.format(path_=path)
        raise IOError(000, err_msg, '')

    print("create: {prefix} {path_}".format(
        prefix=prefix,
        path_=os.path.abspath(path)
        ))

def create_path(current_directory, new_folder_name):
    """Gets the absolute path of the new folder we're creating"""
    current_directory = os.path.abspath(current_directory)
    return os.path.join(current_directory, new_folder_name)

