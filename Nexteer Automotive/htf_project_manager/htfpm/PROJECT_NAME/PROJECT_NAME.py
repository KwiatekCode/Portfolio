import os
from htfpm.PROJECT_NAME.configs.configs import configs
from htfpm.PROJECT_NAME.interface.interface import interface
from htfpm.PROJECT_NAME.README.Readme import readme
from htfpm.PROJECT_NAME.scripts.scripts import scripts


def add_specification_to_project(specification_name: str, selected_project: str, architecture_path: str) -> None:
    '''
    This function creates a specification folder with the name entered by the user in the project folder selected by the user.

    Creates a config folder in the newly created specification folder and
    creates all assets files with the content in the newly created config folder.

    Creates an interface folder in the newly created specification folder and
    creates all assets files with the content in the newly created interface folder.

    Creates an README folder in the newly created specification folder and
    creates a Readme.md file with the content in the newly created README folder.

    Creates a scripts folder in the newly created specification folder and
    creates all assets files with the content in the newly created scripts folder.

    :param specification_name: the specification name is entered by the user
    :param selected_project: the project folder is selected by the user
    :param architecture_path: the architecture path is entered by the user
    '''
    selected_project_path = os.path.join(architecture_path, selected_project)

    project_folder_entered_name = os.path.join(selected_project_path, specification_name)

    os.makedirs(project_folder_entered_name)

    configs(specification_name=specification_name, selected_project=selected_project, project_folder_entered_name=project_folder_entered_name)
    interface(specification_name=specification_name, selected_project=selected_project, project_folder_entered_name=project_folder_entered_name)
    readme(project_folder_entered_name=project_folder_entered_name)
    scripts(specification_name=specification_name, project_folder_entered_name=project_folder_entered_name)
