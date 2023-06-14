import os


def project_specific(specification_name: str, selected_project: str, selected_specification_path_interface: str) -> None:
    '''
    This function creates a projectSpecific.py file with the content.

    :param specification_name: the specification name is entered by the user
    :param selected_project: the project folder is selected by the user
    :param selected_specification_path_interface: the project folder path is being join with 'interface'
    '''
    selected_specification_path_interface_project_specific = os.path.join(selected_specification_path_interface, 'projectSpecific.py')

    project_specific_content = [
        f'from ea4.CORE.{specification_name}.interface.protocol import {specification_name}ProjectSpecificTest\n',
        f'from ea4.{selected_project}.projectTest import ProjectTest\n',
        f'\n\nclass {specification_name}ProjectSpecific(ProjectTest, {specification_name}ProjectSpecificTest):\n',
        '    def fun(self):\n',
        '        self.report.condition(False, comment="I am your Fan!")\n'
    ]

    with open(selected_specification_path_interface_project_specific, 'x') as projectSpecific:
        projectSpecific.writelines(project_specific_content)
