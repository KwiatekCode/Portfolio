import os


def parameters(selected_specification_path_interface: str) -> None:
    '''
    This function creates a parameters.py file with the content.

    :param selected_specification_path_interface: the project folder path is being join with 'interface'
    '''
    selected_specification_path_interface_parameters = os.path.join(selected_specification_path_interface, 'parameters.py')

    parameters_content = [
        'PARAM1 = 1\n',
        'PARAM2 = "two"\n'
    ]

    with open(selected_specification_path_interface_parameters, 'x') as Parameters:
        Parameters.writelines(parameters_content)
