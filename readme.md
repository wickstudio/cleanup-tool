# Cleanup Tool

## Introduction
Cleanup Tool is a powerful by Wick Studio, user-friendly Python script designed to help users efficiently clean and manage their Windows systems. This tool provides a range of functionalities to remove unnecessary files, clear temporary directories, manage browser caches, and much more, all through an easy-to-use command-line interface.

## Features
- Interactive Command-Line Interface: Easy-to-navigate menu for selecting specific cleanup actions.
- Multiple Cleanup Options: Including temp directories, downloads folder, system log files, empty directories, and the recycle bin.
- Full Cleanup Option: A convenient feature to perform all cleanup tasks at once.
- Colorful Output: Enhanced readability and user experience using `colorama`.
- Custom ASCII Banner: A custom banner using `pyfiglet` for a unique touch.

## Installation
To install the Cleanup Tool, follow these steps :

1. Clone the repository:
   ```bash
   git clone https://github.com/wickstudio/cleanup-tool.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd cleanup-tool
   ```
3. Run the installation batch file (this will install required Python packages) :
   ```bash
   install.bat
   ```

## Usage
To use the tool, simply run the Python script :

```bash
start.bat
```

Follow the on-screen prompts to select the desired cleanup operation.

## Options
1. **Perform Full Cleanup** : Executes all available cleanup tasks.
2. **Clean Temp Directories** : Clears temporary files.
3. **Clean Downloads Folder** : Removes files from the Downloads folder based on specified criteria.
4. **Empty Recycle Bin** : Empties the Windows Recycle Bin.
5. **Clean System Log Files** : Deletes log files from the system directory.
6. **Clean Empty Directories** : Removes empty directories in the user profile.

## Caution
- It is recommended to **back up important data** before running any cleanup operation.
- Some cleanup operations require **administrative privileges**.
- Ensure to run the tool in an environment where accidental data loss would not be critical, especially for the first use.

## Contributing
Contributions to the Cleanup Tool are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. Please ensure to follow the existing code structure and style.

## License
Licensed under the [MIT License](LICENSE).

## Connect with Wick Studio

- [GitHub](https://github.com/wickstudio)
- [Discord](https://discord.gg/wicks)
- [YouTube](https://www.youtube.com/@wick_studio)

---

Enjoy the Cleanup Tool, and happy cleaning!