import os
from htfpm.CORE.CORE import add_specification_to_core
from htfpm.PROJECT_NAME.PROJECT_NAME import add_specification_to_project
from htfpm.components.components import add_components


def main():
    '''
    This function is used to generate a specification example in the CORE folder and the project folder selected by the user.

    1. User enters the specification name - specification_name (ProjectNameTest1)
    2. User enters architecture path - architecture_path (C:/../hil_test_scritps/ea4)
    3. User chooses whether to create a specification in the CORE folder - core_input (Y)
    4. User chooses whether to create a specification in the project folder - project_input (Y)

    If he wants to, he must specify in which project folder he wants to create specifications by selecting from the list - entered_number (1)

    5. Creates a components folder with all contents if it doesn't exist.
    '''
    specification_name = input("Enter your new specification name: ")

    architecture_path = input("Enter project architecture path: (example: C:/../hil_test_scritps/ea4) ")

    while True:
        core_input = input(f"Do you want to create {specification_name} in CORE? Y/N ").lower()

        if core_input == "y":
            add_specification_to_core(specification_name=specification_name, architecture_path=architecture_path)
            print(f"Successfully created {specification_name} in CORE")
            break
        if core_input == "n":
            break

    while True:
        project_input = input(f"Do you want to create {specification_name} in PROJECT? Y/N ").lower()

        if project_input == "y":
            architecture_path_listdir = [entry for entry in os.listdir(architecture_path) if os.path.isdir(os.path.join(architecture_path, entry)) and not entry.startswith("_")]
            architecture_path_listdir.remove('CORE')

            # if '__pycache__' in architecture_path_listdir:
            #     architecture_path_listdir.remove('__pycache__')

            for i, folder_name in enumerate(architecture_path_listdir):
                print(str(i) + ". " + folder_name)

            entered_number = int(input("Pick your project folder: "))
            selected_project = architecture_path_listdir[entered_number]

            add_specification_to_project(specification_name=specification_name, selected_project=selected_project, architecture_path=architecture_path)
            print(f"Successfully created {specification_name} in {selected_project}")
            break

        if project_input == "n":
            break

    add_components(architecture_path=architecture_path)
