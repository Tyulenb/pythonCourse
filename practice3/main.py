import mymodule
import mymodule

import some_module
print(f"GLOBAL_VAR from main is {some_module.GLOBAL_VAR}")
some_module.GLOBAL_VAR = 50
print(f"GLOBAL_VAR from main is {some_module.GLOBAL_VAR}")
'''
from some_module import GLOBAL_VAR

print(f"GLOBAL_VAR from main is {GLOBAL_VAR}")
GLOBAL_VAR = 50
print(f"GLOBAL_VAR from main is {GLOBAL_VAR}")
'''
import otherfile
otherfile.printOther()

some_module.printGlobal()
print(f"GLOBAL_VAR from main is {some_module.GLOBAL_VAR}")
otherfile.printOther()


