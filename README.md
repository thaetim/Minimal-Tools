# MINIMAL TOOLS

## Tasklist
A simple dark-themed task list window. Always in the foreground.

## Features and Usage

- **Draggable and Always On Top**: The application window is draggable, allowing you to place it anywhere on your screen, and it always stays in the foreground for easy access to your tasks.

- **Add and Remove Tasks**: You can add new tasks to your list by typing in the input field and pressing Enter. To remove a task, simply double-click on it.

- **Task Completion**: Mark tasks as completed by clicking on them. Clicking on a completed task will mark it as incomplete.

- **Context Menu**: Right-click on the window to access a context menu with options to exit the application, and save and load your tasks to a text file.

- **Close Application**: You can press the "Esc" key to quickly close the application.

Feel free to edit the colors in the code itself.

#### Requirements
1. Install [Python 3](https://www.python.org/downloads/).
2. Install tkinter:

        pip install tkinter

#### If you want it run with a keyboard shortcut
1. Install [AutoHotkey v1](https://www.autohotkey.com/download/).
2. Create and edit this *.ahk* script. Info about available [Hotkeys](https://www.autohotkey.com/docs/v1/Hotkeys.htm).

        #':: ; <- This creates a Win + ' keyboard shortcut (you can customize it)
            Run, "path\to\your\pythonw.exe" "path\to\your\tasklist.py"
        return

3. Run the script. Now the script will listen for the key combination specified in the .ahk script, and if so execute the `tasklist.py`

I recommend also adding the *.ahk* script to Windows' autostart:
1. WIN + R
2. Type in "shell:startup"
3. Put the script (or shortcut to it) in there.

## Customization

You can customize the application by modifying the script. You can change the colors, window size, or add additional features according to your requirements.

## License

This Task List Application is open-source software available under the [MIT License](https://mit-license.org/).

## Author

- [Maciej Stawarz](https://github.com/thaetim)

Feel free to contact the author with any questions or suggestions.

#### Future developments
Rewrite the app to use the styled `tkk`.