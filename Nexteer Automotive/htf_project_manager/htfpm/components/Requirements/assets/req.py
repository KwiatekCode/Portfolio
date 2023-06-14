from contextlib import suppress
import os


def req(components_path_requirements: str) -> None:
    '''
    This function creates a req.py file with the content if it doesn't exist.

    :param components_path_requirements: the components path is being join with 'requirements'
    '''
    components_path_requirements_req = os.path.join(components_path_requirements, 'req.py')

    req_content = [
        'from typing import NamedTuple, List\n',
        '\n\nclass Req(NamedTuple):\n',
        '    requirements: List[str]\n',
        '    safety: str\n',
        '    softwareComponents: List[str]\n'
    ]

    with suppress(FileExistsError):
        with open(components_path_requirements_req, 'x') as Req:
            Req.writelines(req_content)
        print(f"\nSuccessfully created components folder")
