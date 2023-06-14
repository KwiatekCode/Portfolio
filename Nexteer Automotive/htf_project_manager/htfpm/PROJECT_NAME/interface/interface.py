import os
from htfpm.PROJECT_NAME.interface.assets.parameters import parameters
from htfpm.PROJECT_NAME.interface.assets.projectSpecific import project_specific
from htfpm.PROJECT_NAME.interface.assets.requirements import requirements
from htfpm.PROJECT_NAME.interface.assets.signals import signals


def interface(specification_name: str, selected_project: str, project_folder_entered_name: str) -> None:
    '''
    This function creates an interface folder.

    :param specification_name: the specification name is entered by the user
    :param selected_project: the project folder is selected by the user
    :param project_folder_entered_name: the project folder path is being join with specification name
    '''
    selected_specification_path_interface = os.path.join(project_folder_entered_name, 'interface')

    os.makedirs(selected_specification_path_interface)

    parameters(selected_specification_path_interface=selected_specification_path_interface)
    project_specific(specification_name=specification_name, selected_project=selected_project, selected_specification_path_interface=selected_specification_path_interface)
    requirements(selected_specification_path_interface=selected_specification_path_interface)
    signals(selected_specification_path_interface=selected_specification_path_interface)
