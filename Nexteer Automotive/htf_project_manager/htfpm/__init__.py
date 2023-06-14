'''
This library is used to generate a specification example in the CORE folder and the project folder selected by the user.

Two operating modes are available:

1. Interactive with main()

2. Automation style with add_specification_to_core(), add_specification_to_project and add_components
'''
from htfpm.main import main

from htfpm.CORE.CORE import add_specification_to_core
from htfpm.PROJECT_NAME.PROJECT_NAME import add_specification_to_project
from htfpm.components.components import add_components
