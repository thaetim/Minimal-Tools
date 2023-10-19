import tkinter as tk
import sys


class Win(tk.Tk):
    """Custom window class for the task list application."""

    click_pos = (0, 0)

    def __init__(self):
        """Initialize the window with specific settings and event bindings.

        This constructor sets up the window without window decorations, places it
        in the bottom right part of the screen, and binds mouse and keyboard events.

        """
        super().__init()

        # Disable window manager on the app's window
        super().overrideredirect(True)

        # Start the window in the bottom right part of the screen
        self._offsetx = self.winfo_screenwidth() - self.winfo_width - 200
        self._offsety = self.winfo_screenheight() - self.winfo_height - 200
        super().geometry(f"+{self._offsetx}+{self._offsety}")

        # Bind mouse events
        super().bind("<Button-1>", self.clickwin)
        super().bind("<B1-Motion>", self.dragwin)

        # Bind closing key
        super().bind("<Escape>", self.close)

    def dragwin(self, _):
        """Handle window dragging based on cursor movement.

        This function moves the window with the cursor as it's dragged.

        Args:
            _: Unused event argument.

        """
        x = super().winfo_pointerx() - self._offsetx
        y = super().winfo_pointery() - self._offsety
        super().geometry(f"+{x}+{y}")

    def clickwin(self, event):
        """Handle mouse click and track the click position on the screen.

        This function records the position of a mouse click on the screen and the window's
        offset to the cursor.

        Args:
            event: Mouse click event.

        """
        self.click_pos = (event.x_root, event.y_root)
        self._offsetx = super().winfo_pointerx() - super().winfo_rootx()
        self._offsety = super().winfo_pointery() - super().winfo_rooty()

    def has_cursor_moved(self):
        """Check if the cursor has moved since the last click.

        This function compares the current cursor position with the position of the last click
        to determine if the cursor has moved.

        Returns:
            bool: True if the cursor has moved, False otherwise.

        """
        return self.click_pos != (super().winfo_pointerx(), super().winfo_pointery())

    def close(self, _=None):
        """Exit the application.

        This function closes the application.

        Args:
            _: Unused event argument.

        """
        sys.exit()
