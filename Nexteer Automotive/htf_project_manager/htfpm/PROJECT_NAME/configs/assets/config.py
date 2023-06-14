import os


def config(specification_name: str, selected_project: str, selected_specification_path_configs: str) -> None:
    '''
    This function creates a config.yml file with the content.

    :param specification_name: the specification name is entered by the user
    :param selected_project: the project folder is selected by the user
    :param selected_specification_path_configs: the project folder path is being join with 'configs'
    '''
    selected_specification_path_configs_file = os.path.join(selected_specification_path_configs, 'config.yml')

    config_content = [
        f'projectName: {selected_project}\n',
        'testEnvironment: dSpace\n',
        '\nreport:\n',
        '  openInWebBrowser: true\n',
        '  openInFileExplorer: false\n',
        '\nenvironment:\n',
        '  controller: CONTROL_DESK\n',
        '  aliasInfoFilePath: ..\..\..\\assets\environment\\aliasInfo.xlsx\n',
        '\ndiagnostics:\n',
        '#  dbFilePath: "path"\n',
        '  controller: CANOE\n',
        '  clientServerName: None\n',
        '  nexteerServerName: None\n',
        '  mutedTroubles:\n',
        '    ntcs: [\n',
        '    ]\n',
        '    dtcs: [\n',
        '    ]\n',
        '    comment: ""\n',
        '\ntest:\n',
        '  prepare: true\n',
        '  testerName: ""\n'
        '  crNumber: \'\'\n',
        f'  dirPath: ..\..\..\Core\{specification_name}\scripts\n',
        '  fileNames:\n',
        '    included: [\n',
        f'    TS_{specification_name}_*.py\n',
        '  ]\n',
        '\ncustom:\n',
        f'  project_folder: ea4.{selected_project}.{specification_name}.interface'
    ]

    with open(selected_specification_path_configs_file, 'x') as Config:
        Config.writelines(config_content)
