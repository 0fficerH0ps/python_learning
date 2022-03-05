# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# 1. import module_name
# 2. from module_name import function_name
# 3. from module_name import function_name as fn
# 4. import module_name as mn
# 5. from module_name import *


# import module_name

import make_cars
car_1 = make_cars.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_1)

# See cars_1-5 for all methods.

# Note to self: Make sure to add the .function_name() part of 
# the module_name.function_name()

# Tested, works 03/04/2022.