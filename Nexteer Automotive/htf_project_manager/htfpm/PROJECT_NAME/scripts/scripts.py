import os
from htfpm.PROJECT_NAME.scripts.assets.TS_Name_000Y import ts_name_000y


def scripts(specification_name: str, project_folder_entered_name: str) -> None:
    '''
    This function creates a scripts folder.

    :param specification_name: the specification name is entered by the user
    :param project_folder_entered_name: the project folder path is being join with specification name
    '''
    selected_specification_path_scripts = os.path.join(project_folder_entered_name, 'scripts')

    os.makedirs(selected_specification_path_scripts)

    ts_name_000y(specification_name=specification_name, selected_specification_path_scripts=selected_specification_path_scripts)
