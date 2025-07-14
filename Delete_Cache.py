import os
import sys
import time


def get_script_path():
    """
    Returns the absolute path of the directory where the Python script is located.
    """
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def delete_files_on_time(directory_path, prefix_archive, intervalo_segundos):
    """
    Deletes files in a specific directory that begin with a given prefix,
repeatedly at each time interval.

    Args:
        directory_path (str): The path to the directory where the files are located.
        file_prefix (str): The prefix that files must have to be deleted (e.g., "sga").
        interval_seconds (int): The time interval in seconds for checking and deleting.
    """
    while True:
        print(f"Verifyng archives with prefix '{prefix_archive}' on '{directory_path}' in {time.ctime()}...")
        founded_files = 0
        try:
            for archive_name in os.listdir(directory_path):
                complete_archive_path = os.path.join(directory_path, archive_name)

                # Verify if it is a file(and not directory) and if it start with prefix
                if os.path.isfile(complete_archive_path) and archive_name.startswith(prefix_archive):
                    try:
                        os.remove(complete_archive_path)
                        print(f"Archive '{archive_name}' delete successfully.")
                        founded_files += 1
                    except OSError as e:
                        print(f"Error to the delete this file '{archive_name}': {e}")
            
            if founded_files == 0:
                print(f"No file with prefix '{prefix_archive}' found in this cycle.")

        except FileNotFoundError:
            print(f"Error: The directory '{directory_path}' not found.")
        except Exception as e:
            print(f"An unexpected error occured to the list an directory: {e}")

        time.sleep(interval_in_seconds)


if __name__ == "__main__":
    # Sets a directory to monitor and which is the same as where the script is
    directory_to_monitor = get_script_path()
    
    # Sets the prefix of the files to be deleted
    prefix_from_files = "sga" 

    # Sets the time interval in minutes
    interval_in_minutes = 5
    interval_in_seconds = interval_in_minutes * 60

    print(f"Initialising the files delection with prefix '{prefix_from_files}' on '{directory_to_monitor}' every {interval_in_minutes} minutes.")
    print("Press Ctrl+C to stop script!.")

    try:
        delete_files_on_time(directory_to_monitor, prefix_from_files, interval_in_seconds)
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")