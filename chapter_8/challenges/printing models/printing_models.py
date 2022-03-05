# 8-15. Printing Models: Put the functions for the example printing_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of printing_models.py, and modify the file to use the imported functions.

import printing_functions as py

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

py.print_models(unprinted_designs, completed_models)
py.show_completed_models(completed_models)

# Tested, works 03/04/2022.