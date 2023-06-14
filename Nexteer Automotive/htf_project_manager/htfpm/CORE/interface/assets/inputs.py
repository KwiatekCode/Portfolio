import os


def inputs(core_path_interface: str) -> None:
    '''
    This function creates an inputs.py file with the content.

    :param core_path_interface: the CORE path is being join with 'interface'
    '''
    core_path_interface_inputs = os.path.join(core_path_interface, 'inputs.py')

    inputs_content = [
            'import importlib\n', 
            'from collections import namedtuple\n', 
            'from typing import Dict \n', 
            '\nimport htf\n',
            'from htf.test.testAttributes import TestEnvironment\n', 
            '\nfrom components.Requirements.req import Req\n',
            '\nTEST_REQ: Dict[int, Req]\n',
            'globals().update({k: v for k, v in importlib.import_module(htf.config.custom.project_folder + ".requirements").__dict__.items() if not k.startswith("_")})\n',
            '\nInfo = namedtuple(\'Goal\', [\'goal\', \'allowedEnvironments\', \'sensorType\'])\n',
            '\nTEST_GOALS = {\n',
            '    1: Info(goal="templateGoal",\n',
            '            allowedEnvironments=[TestEnvironment.dSpace, ],\n',
            '            sensorType=\'templateSensor\')}\n',
            '\nTEST_INFO = {key: {"requirements": value.requirements,\n',
            '                   "goal": TEST_GOALS[key].goal,\n',
            '                   "allowedEnvironments": TEST_GOALS[key].allowedEnvironments}\n',
            '             for key, value in TEST_REQ.items()}\n'
            ]

    with open(core_path_interface_inputs, 'x') as Inputs:
        Inputs.writelines(inputs_content)
