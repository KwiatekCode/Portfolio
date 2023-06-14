import os
from htfpm.components.Requirements.assets.req import req


def requirements(components_path: str) -> None:
    '''
    This function creates a requirements folder if it doesn't exist.

    :param components_path: the path above the architecture path is being join with 'components'
    '''
    components_path_requirements = os.path.join(components_path, 'Requirements')

    os.makedirs(components_path_requirements, exist_ok=True)

    req(components_path_requirements=components_path_requirements)
