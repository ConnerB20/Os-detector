
from sys import platform

#Detect the OS
def print_OS():
    print("*********************************************************************")
    print("This is:")

def OS():
    if platform =="linux" or platform =="linux2":
        global OS
        OS = "Linux"
        return (OS)


    if platform == "darwin":
        global OS
        OS = "Apple"
        return (OS)        
    if platform =="win32":
        global OS
        OS = "Windows"
        return (OS)

OS()        
print_OS()
print (OS)