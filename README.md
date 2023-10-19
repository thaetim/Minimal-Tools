# MINIMAL TOOLS

## Tasklist
A simple dark-themed task list.

## Features and Usage

- **Draggable & Always On Top**: The window is draggable, stays in the foreground.

- **Add & Remove Tasks**: Add tasks by typing and pressing Enter, double-click to remove.

- **Task Completion**: Click to mark tasks complete or incomplete.

- **Context Menu**: Right-click for options: exit, save, load tasks.

- **Quick Close**: Press "Esc" to exit.

#### Requirements
1. Install [Python 3](https://www.python.org/downloads/).
2. Install tkinter:

        pip install tkinter

#### How to run with any keyboard shortcut
1. Install [AutoHotkey v1](https://www.autohotkey.com/download/).
2. Create and edit this *.ahk* script. Info about available [Hotkeys](https://www.autohotkey.com/docs/v1/Hotkeys.htm).

        #':: ; <- This creates a Win + ' keyboard shortcut (you can customize it)
            Run, "path\to\your\pythonw.exe" "path\to\your\tasklist.py"
        return

3. Run the script. Now the script will listen for the key combination specified in the *.ahk* script, and if so execute the `tasklist.py`.

I recommend also adding the *.ahk* script to Windows' autostart:
1. WIN + R
2. Type in "shell:startup"
3. Put the script (or shortcut to it) in there.

## Customization

You can change the colors, window size, or add additional features by modifying the `tasklist.py` script.

## License

This is an open-source software available under the [MIT License](https://mit-license.org/).

#### Future developments
Rewrite using the styled `tkk`.
