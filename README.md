# Vix Editor

**Vix Editor** is a lightweight, terminal-based text editor built with Python. Inspired by the straightforward simplicity of **Windows Notepad**, the efficiency of **Windows Command Line** interactions, and the powerful modal editing philosophies found in **Vim**, Vix aims to provide a fast and intuitive text editing experience directly within your terminal. It allows users to seamlessly open existing files or create new ones on the fly.

---
## Features

* **Inspired Interface:** Combines the user-friendliness of Notepad with the robust capabilities often found in command-line editors.
* **Automatic File Creation:** If you try to open a file that doesn't exist, Vix will automatically create it for you.
* **Easy Saving:** Users can easily save their changes within the editor.
* **Lightweight & Fast:** Built with Python for minimal resource consumption and quick launch times.
* **Command-Line Native:** Edit files directly from your terminal with a simple command.
* **Cross-Platform (Linux):** Primarily designed for Linux environments.

---
## Prerequisites

Vix Editor is developed with Python 3 and requires the `tkinter` library for its graphical interface.

To install `tkinter`:

**On Ubuntu/Debian based systems:**

```Bash
sudo apt-get update
sudo apt-get install python3-tk
```

On Fedora based systems:
```Bash
sudo dnf install python3-tkinter
```
Installation
To install Vix Editor on your Linux system and use it as a command, follow these steps:
 * Clone the repository:
   Open your terminal and execute the following command to download the Vix Editor project to your local machine:
   ```Bash
   git clone https://github.com/VahramCode/VixEditor.git
   ```
   
 * Navigate into the project directory:
   Move into the newly cloned project folder:
   ```Bash
   cd VixEditor
   ```

 * Run the installation script:
   This script will handle copying the necessary Python editor files to /opt/vix and setting up the vix command in /usr/local/bin, making it accessible from any directory in your terminal.
   ```Bash
   chmod +x install.sh
   sudo ./install.sh
   ```

   You will be prompted for your sudo password during this process, as the script needs elevated privileges to place files in system directories.
   If the installation completes successfully, you will see a confirmation message in your terminal.
Usage
After Vix Editor is successfully installed, you can launch it from any location in your terminal using the vix command:
 * To open an existing file or create a new one:
   Simply provide the filename as an argument. If the file does not exist, Vix will create an empty file for you.
```Bash
   vix my_new_document.txt
```
 * To open a file at a specific path:
   You can also provide a full or relative path to a file.
   ```Bash
   vix /home/user/documents/notes.md
   ```
Contributing
(Optional: If you plan to accept contributions from others, add a section here explaining how they can contribute. For example: "Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.")

