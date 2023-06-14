import os


def parameters(core_path_interface: str) -> None:
    '''
    This function creates a parameters.py file with the content.

    :param core_path_interface: the CORE path is being join with 'interface'
    '''
    core_path_interface_parameters = os.path.join(core_path_interface, 'parameters.py')

    parameters_content = [
        'import importlib\n',
        '\nimport htf\n',
        '\nglobals().update({k: v for k, v in importlib.import_module(htf.config.custom.project_folder + ".parameters").__dict__.items() if not k.startswith("_")})\n',
        '\nPARAM1: int\n',
        'PARAM2: str\n'
    ]

    with open(core_path_interface_parameters, 'x') as Parameters:
        Parameters.writelines(parameters_content)
