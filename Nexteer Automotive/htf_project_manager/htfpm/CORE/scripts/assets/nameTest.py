import os


def name_test(specification_name: str, core_path_scripts: str) -> None:
    '''
    This function creates a specification_nameTest.py file with the content.

    :param specification_name: the specification name is entered by the user
    :param core_path_scripts: the CORE path is being join with 'scripts'
    '''
    entered_name_test = specification_name + "Test.py"

    core_path_scripts_entered_name_test = os.path.join(core_path_scripts, entered_name_test)

    entered_name_test_file_content = [
        f'from ea4.CORE.{specification_name}.interface.projectSpecific import {specification_name}ProjectSpecific\n',
        '\n\ndef generateCaseId(procId, caseNo):\n',
        '    return "TS_' + specification_name + '_{:04d}_{:02d}".format(procId, caseNo)\n',
        f'\n\nclass {specification_name}Test({specification_name}ProjectSpecific):\n',
        '    def dummy_method(self):\n',
        '        self.fun()\n'
    ]

    with open(core_path_scripts_entered_name_test, 'x') as nameTest_file:
        nameTest_file.writelines(entered_name_test_file_content)
