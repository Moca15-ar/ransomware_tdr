import os

# MOVES THE FILES TO ANOTHER FOLDER IN C:\ SO THEY ARE NOT ENCRYPTED ACCIDENTALLY


# the file that moves files has to be specified as __init__
# C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

rware_files = [] #list with all the files that make the ware work

if __name__=="__main__":
    global current_dir
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    # print(fulldir) --> c:\Users\RitaAlonsoCasablanca\Desktop\malware\ransomware_versions_test\python_function_test
    os.system('mkdir C:\Ransomware')
    
    for r in rware_files:
        fulldir = current_dir + '\\' + r #creates a path string by joining the current folder path and each file's name
        # print(a) --> c:\Users\RitaAlonsoCasablanca\Desktop\malware\ransomware_versions_test\python_function_test\ test.txt
        # fulldir = a.replace(' ', '') # eliminates the space in the path a
        print(fulldir) # --> c:\Users\RitaAlonsoCasablanca\Desktop\malware\ransomware_versions_test\python_function_test\test.txt
        os.system('move '+ fulldir + ' C:\Ransomware') # moves the file to the Ransomware folder 
        
