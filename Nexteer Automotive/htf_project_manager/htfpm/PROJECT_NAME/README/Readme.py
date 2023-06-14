import os


def readme(project_folder_entered_name: str) -> None:
    '''
    This function creates a README folder.

    :param project_folder_entered_name: the project folder path is being join with specification name
    '''
    selected_specification_path_readme = os.path.join(project_folder_entered_name, 'README')

    os.makedirs(selected_specification_path_readme)
