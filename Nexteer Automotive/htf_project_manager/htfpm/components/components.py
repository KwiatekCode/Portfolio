import os
from htfpm.components.Requirements.requirements import requirements


def add_components(architecture_path: str) -> None:
    '''
    This function creates a components folder above the architecture path if it doesn't exist.

    Creates a requirements folder in the newly created components folder and
    creates a req.py file with the content in the newly created requirements folder.

    :param architecture_path: the architecture path is entered by the user
    '''
    above_architecture_path = os.path.dirname(architecture_path)

    components_path = os.path.join(above_architecture_path, 'components')

    os.makedirs(components_path, exist_ok=True)

    requirements(components_path=components_path)
