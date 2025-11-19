def write_file(file_name, file_content):
   """Create or overwrite a text file with the given content.

   The actual file path used is f"{file_name}.txt" to match the lab tests.
   """
   with open(f"{file_name}.txt", "w") as file:
       file.write(file_content)


def append_file(file_name, append_content):
   """Append the given content to an existing text file.

   The actual file path used is f"{file_name}.txt" to match the lab tests.
   """
   with open(f"{file_name}.txt", "a") as file:
       file.write(append_content)


def read_file(file_name):
   """Read and return the entire contents of the text file.

   The actual file path used is f"{file_name}.txt" to match the lab tests.
   """
   with open(f"{file_name}.txt", "r") as file:
       return file.read()
