# import os

# def print_directory_contents(code):
#     """
#     Prints the contents of the specified directory.

#     :param directory_path: Path to the directory whose contents need to be printed.
#     """
#     try:
#         # List the contents of the directory
#         contents = os.listdir(directory_path)

#         print(f"Contents of directory '{directory_path}':")
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print(f"Error: Directory '{directory_path}' does not exist.")
#     except PermissionError:
#         print(f"Error: Permission denied to access '{directory_path}'.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Example usage
# directory_path = input("Enter the directory path: ")
# print_directory_contents(directory_path)


import os
director_path='code'
contents=os.listdirt(E)

for item in contents:
    print(item)