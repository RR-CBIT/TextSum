import os
from TextSum.logging import logger
from src.TextSum.entity import DataValidationConfig
import os
import zipfile

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_files_and_dirs_exist(self) -> bool:
        try:
            # Define the path to the edindata directory
            edindata_dir = os.path.join("artifacts", "data_ingestion", "edin_dataset")

            # Check if the edindata directory exists
            if not os.path.isdir(edindata_dir):
                raise FileNotFoundError(f"Directory does not exist: {edindata_dir}")

            # List all files and directories in the edindata directory
            all_files_and_dirs = set()
            for root, dirs, files in os.walk(edindata_dir):
                # Add directories to the list
                for dir in dirs:
                    all_files_and_dirs.add(os.path.relpath(os.path.join(root, dir), edindata_dir) + '/')
                # Add files to the list
                for file in files:
                    all_files_and_dirs.add(os.path.relpath(os.path.join(root, file), edindata_dir))

            # Check if all required files and directories are present
            missing_paths = [path for path in self.config.ALL_REQUIRED_FILES if path not in all_files_and_dirs]

            validation_status = len(missing_paths) == 0

            # Define the path for status.txt
            status_file_path = os.path.join("artifacts", "data_validation", "status.txt")

            # Write validation status to the status file
            with open(status_file_path, 'w') as f:
                if validation_status:
                    f.write("Validation Status: Success - All required files/directories are present.\n")
                else:
                    f.write(f"Validation Status: Failed - Missing files/directories: {', '.join(missing_paths)}\n")

            return validation_status

        except Exception as e:
            # Define the path for status.txt
            status_file_path = os.path.join("artifacts", "data_validation", "status.txt")
            
            # Write error status to the status file
            with open(status_file_path, 'w') as f:
                f.write(f"Validation Status: Error - {str(e)}\n")
            
            print(f"An error occurred during validation: {str(e)}")
            return False