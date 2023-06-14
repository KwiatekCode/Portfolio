import os


def ts_name_0001(specification_name: str, core_path_scripts: str) -> None:
    '''
    This function creates a TS_specification_name_0001.py file with the content.

    :param specification_name: the specification name is entered by the user
    :param core_path_scripts: the CORE path is being join with 'scripts'
    '''
    entered_name_0001 = "TS_" + specification_name + "_0001.py"

    core_path_scripts_entered_name_0001 = os.path.join(core_path_scripts, entered_name_0001)

    entered_name_0001_file_content = [
        f'from ea4.CORE.{specification_name}.interface.inputs import TEST_INFO\n',
        f'from ea4.CORE.{specification_name}.interface.parameters import PARAM1\n',
        f'from ea4.CORE.{specification_name}.interface.signals import sig1\n',
        f'from ea4.CORE.{specification_name}.scripts.{specification_name}Test import {specification_name}Test, generateCaseId\n',
        f'\n\nclass Test({specification_name}Test):\n',
        '    def preStepsTestSpecific(self):\n',
        '        pass\n'
        '\n    def testSteps(self):\n',
        '        with self.report.block(name=generateCaseId(1, 1)):\n',
        '            self.fun()\n',
        '            sig1.physicalValue = PARAM1\n',
        '\n    def postStepsTestSpecific(self):\n',
        '        pass\n',
        '\n\nTest(**TEST_INFO[1]).run()\n'
    ]

    with open(core_path_scripts_entered_name_0001, 'x') as name_0001_file:
        name_0001_file.writelines(entered_name_0001_file_content)
