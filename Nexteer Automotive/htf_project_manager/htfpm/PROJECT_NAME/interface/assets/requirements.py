import os


def requirements(selected_specification_path_interface: str) -> None:
    '''
    This function creates a requirements.py file with the content.

    :param selected_specification_path_interface: the project folder path is being join with 'interface'
    '''
    selected_specification_path_interface_requirements = os.path.join(selected_specification_path_interface, 'requirements.py')

    requirements_content = [
        'from components.Requirements.req import Req\n',
        '\nTEST_REQ = {\n',
        '    1: Req(requirements=["1", "2"], safety="", softwareComponents=["tempComp v x.x.x"])\n',
        '}\n'
    ]

    with open(selected_specification_path_interface_requirements, 'x') as Requirements:
        Requirements.writelines(requirements_content)
