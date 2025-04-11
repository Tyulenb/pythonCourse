global GLOBAL_VAR
GLOBAL_VAR = 10

def printGlobal():
    print(f"From some_module GLOBAL_VAR is {GLOBAL_VAR}")

def set_global(n):
    GLOBAL_VAR = n

printGlobal()
