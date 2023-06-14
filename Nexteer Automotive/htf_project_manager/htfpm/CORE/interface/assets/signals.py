import os


def signals(core_path_interface: str) -> None:
    '''
    This function creates a signals.py file with the content.

    :param core_path_interface: the CORE path is being join with 'interface'
    '''
    core_path_interface_signals = os.path.join(core_path_interface, 'signals.py')

    signals_content = [
        'import importlib\n',
        '\nimport htf\n',
        'from htf.environment.variable.environmentVariable import EnvironmentVariable\n',
        '\nglobals().update({k: v for k, v in importlib.import_module(htf.config.custom.project_folder + ".signals").__dict__.items() if not k.startswith("_")})\n',
        '\nsig1: EnvironmentVariable\n',
        'sig2: EnvironmentVariable\n'
    ]

    with open(core_path_interface_signals, 'x') as Signals:
        Signals.writelines(signals_content)
