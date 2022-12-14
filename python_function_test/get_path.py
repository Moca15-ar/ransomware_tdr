from genericpath import isfile
import os


# os.listdir()  -----------> Returns a list of all files and folders in a directory
# os.scandir() 	-----------> Returns an iterator of all the objects in a directory including file attribute information
# pathlib.Path.iterdir()  -> Returns an iterator of all the objects in a directory including file attribute information


#----------------------------------os.listdir-------------------------------------

dir = os.listdir() #lists all the files in the working directory
# current output if printed: ['python_function_test', 'test_files', 'v1.0.0', 'v2.0.0']

print(dir)

dir2 = os.listdir('python_function_test') #can be done on current directory but not one up 
# current output if printed: ['get_path.py']
# dir2 = os.listdir(ransomware_versions_test) : output : FileNotFoundError: [WinError 3] El sistema no puede encontrar la ruta especificada: 'ransomware_versions_test'

print(dir2)

'''
# List all subdirectories (not the files inside)
basepath = 'python_function_test/'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)
# output: testdir
'''

#----------------------------------with + os.scandir-------------------------------------

with os.scandir('python_function_test') as entries: #doesnt create an array to store the names
    for entry in entries:
        if os.path.isfile(entry): #if its a file
            print(entry.name)
        

fil = []

with os.scandir('python_function_test') as entries: 
    for entry in entries:
        if os.path.isfile(entry):
            fil.append(entry.name) #with .name it uses only the name, if not, output=[<DirEntry 'get_path.py'>, <DirEntry 'test'>]

print(fil)
#we have a list with all the files in the directory

print('------------------------------')

#----------------------------------path from pathlib-------------------------------------

from pathlib import Path

entries = Path('python_function_test') #again it doesnt work with ransomware_versions_test dir 
print (entries)
for entry in entries.iterdir():
    print(entry.name)

fil2 = []

entries = Path('python_function_test')
for entry in entries.iterdir():
    fil2.append(entry.name)
print(fil2) #without filtering directories


'''
#----------------------------------os.walk(path)-------------------------------------

f = {} #define dictionary to store every path with its respective files
# f = {'filepath' : [files_in_the_path]}


def find_files(path):
    #print(path)
    # print(os.walk(path))
    
    for actual_path, directories, files_found in os.walk(path):
        # print(actual_path)
        # print(directories)
        # print(files_found)
        f[actual_path]=files_found

    #print(f)

# C:\\Users\\RitaAlonsoCasablanca\\Desktop\\2 BATX A

find_files("C:\\Users")

# output: dictionary with absolutely ALL the files (and the files inside directories) on a specyfied directory
# DO NOT RUN ON A MAJOR DIR (TAKES LONG TIME)

'''

#----------------------------------os.walk(path)-------------------------------------

