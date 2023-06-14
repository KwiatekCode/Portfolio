import os


def signals(selected_specification_path_interface: str) -> None:
    '''
    This function creates a signals.py file with the content.

    :param selected_specification_path_interface: the project folder path is being join with 'interface'
    '''
    selected_specification_path_interface_signals = os.path.join(selected_specification_path_interface, 'signals.py')

    signals_content = [
        'from htf import var\n',
        '\nsig1 = var["sig1"]\n',
        'sig2 = var["sig2"]\n'
    ]

    with open(selected_specification_path_interface_signals, 'x') as Signals:
        Signals.writelines(signals_content)
