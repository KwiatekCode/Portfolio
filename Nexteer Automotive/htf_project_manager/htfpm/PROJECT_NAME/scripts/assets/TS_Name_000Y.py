import os


def ts_name_000y(specification_name: str, selected_specification_path_scripts: str) -> None:
    '''
    This function creates a TS_specification_name_000Y.py file with the content.

    :param specification_name: the specification name is entered by the user
    :param selected_specification_path_scripts: the project folder path is being join with 'scripts'

    '''
    entered_name_000y = "TS_" + specification_name + "_000Y.py"

    selected_specification_path_scripts_entered_name_000y = os.path.join(selected_specification_path_scripts, entered_name_000y)

    entered_name_000y_file_content = [
        ''
    ]

    with open(selected_specification_path_scripts_entered_name_000y, 'x') as name_000Y_file:
        name_000Y_file.writelines(entered_name_000y_file_content)
