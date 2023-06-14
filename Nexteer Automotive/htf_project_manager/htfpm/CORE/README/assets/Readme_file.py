import os


def readme_file(specification_name: str, core_path_readme: str) -> None:
    '''
    This function creates a Readme.md file with the content.

    :param specification_name: the specification name is entered by the user
    :param core_path_readme: the CORE path is being join with 'README'
    '''
    core_path_readme_file = os.path.join(core_path_readme, 'Readme.md')
    
    readme_content = [
        f'# {specification_name}:\n',
        '\n## 1. '
    ]

    with open(core_path_readme_file, 'x') as readme:
        readme.writelines(readme_content)
