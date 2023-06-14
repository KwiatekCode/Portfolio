import os


def project_specific(specification_name, core_path_interface: str) -> None:
    '''
    This function creates a projectSpecific.py file with the content.

    :param specification_name: the specification name is entered by the user
    :param core_path_interface: the CORE path is being join with 'interface'
    '''
    core_path_interface_project_specific = os.path.join(core_path_interface, 'projectSpecific.py')

    project_specific_content = [
        'import importlib\n',
        'from typing import Type\n',
        '\nimport htf\n',
        f'\nfrom ea4.CORE.{specification_name}.interface.protocol import {specification_name}ProjectSpecificTest\n',
        '\nglobals().update({k: v for k, v in importlib.import_module(htf.config.custom.project_folder + ".projectSpecific").__dict__.items() if not k.startswith("_")})\n',
        f'\n{specification_name}ProjectSpecific: Type[{specification_name}ProjectSpecificTest]\n'
    ]

    with open(core_path_interface_project_specific, 'x') as projectSpecific:
        projectSpecific.writelines(project_specific_content)
