import os
from htfpm.CORE.interface.assets.inputs import inputs
from htfpm.CORE.interface.assets.parameters import parameters
from htfpm.CORE.interface.assets.projectSpecific import project_specific
from htfpm.CORE.interface.assets.protocol import protocol
from htfpm.CORE.interface.assets.signals import signals


def interface(specification_name: str, core_path_entered_name: str) -> None:
    '''
    This function creates an interface folder.

    :param specification_name: the specification name is entered by the user
    :param core_path_entered_name: the CORE path is being join with specification name
    '''
    core_path_interface = os.path.join(core_path_entered_name, 'interface')

    os.makedirs(core_path_interface)

    inputs(core_path_interface=core_path_interface)
    parameters(core_path_interface=core_path_interface)
    project_specific(specification_name=specification_name, core_path_interface=core_path_interface)
    protocol(specification_name=specification_name, core_path_interface=core_path_interface)
    signals(core_path_interface=core_path_interface)
