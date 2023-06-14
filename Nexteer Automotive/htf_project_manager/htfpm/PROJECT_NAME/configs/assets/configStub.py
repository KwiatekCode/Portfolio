import os


def config_stub(specification_name: str, selected_project: str, selected_specification_path_configs: str) -> None:
    '''
    This function creates a configStub.yml file with the content.

    :param specification_name: the specification name is entered by the user
    :param selected_project: the project folder is selected by the user
    :param selected_specification_path_configs: the project folder path is being join with 'configs'
    '''
    selected_specification_path_configs_stub = os.path.join(selected_specification_path_configs, 'configStub.yml')

    config_stub_content = [
        f'projectName: {selected_project}\n',
        'testEnvironment: dSpace\n',
        '\nreport:\n',
        '  openInWebBrowser: true\n',
        '  openInFileExplorer: false\n',
        '\nenvironment:\n',
        '  controller: STUB\n',
        '#  aliasInfoFilePath: ..\..\..\\assets\environment\\aliasInfo.xlsx',
        '\ndiagnostics:\n',
        '#  dbFilePath: "path"\n',
        '  controller: STUB(CANOE)\n',
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

    with open(selected_specification_path_configs_stub, 'x') as configStub:
        configStub.writelines(config_stub_content)
