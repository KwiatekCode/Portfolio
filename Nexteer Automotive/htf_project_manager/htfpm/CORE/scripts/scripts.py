import os
from htfpm.CORE.scripts.assets.nameTest import name_test
from htfpm.CORE.scripts.assets.TS_Name_0001 import ts_name_0001


def scripts(specification_name: str, core_path_entered_name: str) -> None:
    '''
    This function creates a scripts folder.

    :param specification_name: the specification name is entered by the user
    :param core_path_entered_name: the CORE path is being join with specification name
    '''
    core_path_scripts = os.path.join(core_path_entered_name, 'scripts')

    os.makedirs(core_path_scripts)

    name_test(specification_name=specification_name, core_path_scripts=core_path_scripts)
    ts_name_0001(specification_name=specification_name, core_path_scripts=core_path_scripts)
