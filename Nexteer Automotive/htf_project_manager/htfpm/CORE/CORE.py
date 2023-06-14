import os
from htfpm.CORE.interface.interface import interface
from htfpm.CORE.README.Readme import readme
from htfpm.CORE.scripts.scripts import scripts


def add_specification_to_core(specification_name: str, architecture_path: str) -> None:
    '''
    This function creates a specification folder with the name entered by the user in the CORE folder.

    Creates an interface folder in the newly created specification folder and
    creates all assets files with the content in the newly created interface folder.

    Creates an README folder in the newly created specification folder and
    creates a Readme.md file with the content in the newly created README folder.

    Creates a scripts folder in the newly created specification folder and
    creates all assets files with the content in the newly created scripts folder.

    :param specification_name: the specification name is entered by the user
    :param architecture_path: the architecture path is entered by the user
    '''
    core_entered_architecture_path = os.path.join(architecture_path, 'CORE')

    core_path_entered_name = os.path.join(core_entered_architecture_path, specification_name)

    os.makedirs(core_path_entered_name)

    interface(specification_name=specification_name, core_path_entered_name=core_path_entered_name)
    readme(specification_name=specification_name, core_path_entered_name=core_path_entered_name)
    scripts(specification_name=specification_name, core_path_entered_name=core_path_entered_name)
