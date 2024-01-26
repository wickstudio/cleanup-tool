import os
import shutil
import tempfile
import winshell
import time
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

def delete_files_in_directory(directory, age_in_days=None, file_extension=None):
    now = time.time()
    for root, dirs, files in os.walk(directory):
        for name in files:
            if file_extension and not name.endswith(file_extension):
                continue
            file_path = os.path.join(root, name)
            if age_in_days is not None:
                file_age = now - os.stat(file_path).st_mtime
                if file_age < age_in_days * 86400:
                    continue
            try:
                os.remove(file_path)
                print(Fore.YELLOW + f"Deleted file: {file_path}")
            except OSError as e:
                print(Fore.RED + f"Error deleting {e.filename} - {e.strerror}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            if age_in_days is not None:
                dir_age = now - os.stat(dir_path).st_mtime
                if dir_age < age_in_days * 86400:
                    continue
            try:
                shutil.rmtree(dir_path)
                print(Fore.YELLOW + f"Deleted directory: {dir_path}")
            except OSError as e:
                print(Fore.RED + f"Error deleting {e.filename} - {e.strerror}")

def delete_empty_directories(directory):
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(Fore.GREEN + f"Empty directory removed: {dir_path}")

def cleanup_downloads_folder(age_in_days=30):
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    print(Fore.BLUE + f"Cleaning Downloads folder: Files older than {age_in_days} days")
    delete_files_in_directory(downloads_folder, age_in_days)

def cleanup_recycle_bin():
    print(Fore.MAGENTA + "Emptying the Recycle Bin")
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

def cleanup_system_log_files():
    log_files_path = os.path.join(os.environ['WINDIR'], 'Logs')
    print(Fore.CYAN + "Cleaning System Log Files")
    delete_files_in_directory(log_files_path, file_extension='.log')

def cleanup_temp_directories():
    print(Fore.GREEN + "Cleaning Temp directories")
    temp_dirs = [tempfile.gettempdir(), os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp')]
    for temp_dir in temp_dirs:
        delete_files_in_directory(temp_dir)
    print(Fore.GREEN + "Temp directories cleaned.")

def perform_full_cleanup():
    print(Fore.YELLOW + "Performing full cleanup...")
    cleanup_temp_directories()
    cleanup_downloads_folder()
    cleanup_recycle_bin()
    cleanup_system_log_files()
    delete_empty_directories(os.environ['USERPROFILE'])
    print(Fore.YELLOW + "Full cleanup completed.")

def main_menu():
    banner = pyfiglet.figlet_format("WICK STUDIO")
    print(Fore.CYAN + Style.BRIGHT + banner) 

    while True:
        print(Fore.YELLOW + "\nPC Cleanup Tool")
        print(Fore.GREEN + "1 : Perform Full Cleanup")
        print("2 : Clean Temp Directories")
        print("3 : Clean Downloads Folder")
        print("4 : Empty Recycle Bin")
        print("5 : Clean System Log Files")
        print("6 : Clean Empty Directories")
        print(Fore.RED + "0: Exit")

        choice = input(Fore.WHITE + "Enter your choice : ")

        if choice == "1":
            perform_full_cleanup()
        elif choice == "2":
            cleanup_temp_directories()
        elif choice == "3":
            cleanup_downloads_folder()
        elif choice == "4":
            cleanup_recycle_bin()
        elif choice == "5":
            cleanup_system_log_files()
        elif choice == "6":
            delete_empty_directories(os.environ['USERPROFILE'])
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
