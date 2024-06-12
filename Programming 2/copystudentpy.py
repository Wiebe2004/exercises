import os
import shutil

# Define the source and destination directories
source_dir = 'Prog2exercises'
dest_dir = 'Prog2exercises_copy'

# Iterate over all subdirectories in the source directory
for dirpath, dirnames, filenames in os.walk(source_dir):
    # Create the same directory structure in the destination directory
    structure = os.path.join(dest_dir, os.path.relpath(dirpath, source_dir))
    os.makedirs(structure, exist_ok=True)

    # If 'student.py' is in the list of files, copy it to the corresponding directory in the destination directory
    if 'student.py' in filenames:
        shutil.copy(os.path.join(dirpath, 'student.py'), structure)