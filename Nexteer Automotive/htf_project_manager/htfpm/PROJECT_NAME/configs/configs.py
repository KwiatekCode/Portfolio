import os
from htfpm.PROJECT_NAME.configs.assets.config import config
from htfpm.PROJECT_NAME.configs.assets.configStub import config_stub


def configs(specification_name: str, selected_project: str, project_folder_entered_name: str) -> None:
    '''
    This function creates a configs folder.

    :param specification_name: the specification name is entered by the user
    :param selected_project: the project folder is selected by the user
    :param project_folder_entered_name: the project folder path is being join with specification name
    '''
    selected_specification_path_configs = os.path.join(project_folder_entered_name, 'configs')

    os.makedirs(selected_specification_path_configs)

    config(specification_name=specification_name, selected_project=selected_project, selected_specification_path_configs=selected_specification_path_configs)
    config_stub(specification_name=specification_name, selected_project=selected_project, selected_specification_path_configs=selected_specification_path_configs)
