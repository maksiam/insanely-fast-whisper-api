from filecmp import dircmp
import tempfile
import os
import shutil
from typing import List


class TempFileManager:
    def __init__(self):
        self.paths: List[str] = []

    def create_temp_file(
        self, prefix: str = "tmp", suffix: str = "", dir: str = "files"
    ) -> str:
        """Create a temporary file and return its path."""
        temp_file = tempfile.NamedTemporaryFile(
            prefix=prefix, suffix=suffix, delete=False, dir=dir
        )
        self.paths.append(temp_file.name)
        temp_file.close()  # Close the file so it can be used by other parts of the program
        return temp_file.name

    def create_temp_dir(self, prefix: str = "tmp", dir: str = "./") -> str:
        """Create a temporary directory and return its path."""
        temp_dir = tempfile.mkdtemp(prefix=prefix, dir=dir)
        self.paths.append(temp_dir)
        return temp_dir

    def cleanup(self):
        """Delete all temporary files and directories."""
        for path in self.paths:
            if os.path.isdir(path):
                shutil.rmtree(path)  # Remove directory
            elif os.path.isfile(path):
                os.remove(path)  # Remove file
        self.paths.clear()


# Example usage
# if __name__ == "__main__":
#     temp_manager = TempFileManager()
#     temp_file_path = temp_manager.create_temp_file(prefix='example_', suffix='.txt')
#     temp_dir_path = temp_manager.create_temp_dir(prefix='example_dir_')

#     print(f"Temporary file created at: {temp_file_path}")
#     print(f"Temporary directory created at: {temp_dir_path}")

#     # Do something with the temp file and directory here...

#     # Cleanup all created temporary files and directories
#     temp_manager.cleanup()
