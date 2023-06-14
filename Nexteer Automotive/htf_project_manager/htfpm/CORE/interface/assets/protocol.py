import os


def protocol(specification_name, core_path_interface: str) -> None:
    '''
    This function creates a protocol.py file with the content.

    :param specification_name: the specification name is entered by the user
    :param core_path_interface: the CORE path is being join with 'interface'
    '''
    core_path_interface_protocol = os.path.join(core_path_interface, 'protocol.py')

    protocol_content = [
        'from abc import ABC\n',
        '\nfrom ea4.ea4Test import Ea4Test\n',
        f'\n\nclass {specification_name}ProjectSpecificTest(Ea4Test, ABC):\n',
        '    def fun(self):\n',
        '        raise NotImplementedError\n'
    ]

    with open(core_path_interface_protocol, 'x') as Protocol:
        Protocol.writelines(protocol_content)
