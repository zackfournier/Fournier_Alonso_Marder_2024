# import os
#
# compilecommand='javac ./java/*java'
# os.system(compilecommand)
#
# makejarcommand = 'zip -r temp.jar ./java/*class'
# os.system(makejarcommand)

import os
import zipfile
import glob

import os
import zipfile
import glob

# Define the directory where you want to save the JAR file
directory = './java'

# # Compile Java files
# compilecommand = 'javac ./java/*.java'
# os.system(compilecommand)
# # Create JAR file
# jar_file_path = os.path.join(directory, 'temp.jar')
# with zipfile.ZipFile(jar_file_path, 'w') as jar:
#     for class_file in glob.glob('./java/*.class'):
#         jar.write(class_file, os.path.basename(class_file))


import os
import zipfile

# Change directory to 'code/bin'
os.chdir(directory + '/code/bin')

# Create a zip file in the desired location
with zipfile.ZipFile('../../model.jar', 'w', zipfile.ZIP_DEFLATED) as jar:
    # Iterate over all files in the current directory
    for foldername, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            # Create a complete file path by joining folder and file name
            file_path = os.path.join(foldername, filename)
            # Add the file to the zip file
            jar.write(file_path, os.path.relpath(file_path, '.'))

# Change back to the original directory
os.chdir('../../')