import os  # Import the os module for working with file paths and directories
import hashlib  # Import the hashlib module for generating file hashes

def find_duplicate_files(directory):
    # Dictionary to store file hashes and their corresponding file paths
    file_hashes = {}

    # Loop through the files in the specified directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)  # Construct the full file path

        if os.path.isfile(filepath):  # Check if the path points to a file (not a directory)
            with open(filepath, "rb") as file:  # Open the file in binary read mode
                file_hash = hashlib.sha256(file.read()).hexdigest()  # Generate a SHA-256 hash of the file content

            # Check if the hash value is already in the dictionary
            if file_hash in file_hashes:
                file_hashes[file_hash].append(filepath)  # If duplicate, add the path to the list of paths
            else:
                file_hashes[file_hash] = [filepath]  # If not duplicate, create a new list with this path

    # Print the names of duplicate files
    for hash_value, paths in file_hashes.items():  # Iterate through the hash-value and path pairs
        if len(paths) > 1:  # If there's more than one path with the same hash (duplicate)
            print(" ".join(paths))  # Print the paths separated by spaces

if __name__ == "__main__":
    import sys

    # Check if the script was run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python find_duplicate_files.py <directory>")
    else:
        target_directory = sys.argv[1]  # Get the target directory from the command-line argument
        find_duplicate_files(target_directory)  # Call the function to find duplicate files
