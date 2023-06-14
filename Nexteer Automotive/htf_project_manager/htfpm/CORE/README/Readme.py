import os
from htfpm.CORE.README.assets.Readme_file import readme_file


def readme(specification_name: str, core_path_entered_name: str) -> None:
    '''
    This function creates an README folder.

    :param specification_name: the specification name is entered by the user
    :param core_path_entered_name: the CORE path is being join with specification name
    '''
    core_path_readme = os.path.join(core_path_entered_name, 'README')

    os.makedirs(core_path_readme)

    readme_file(specification_name=specification_name, core_path_readme=core_path_readme)
