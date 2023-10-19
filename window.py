import tkinter as tk
import sys


class Win(tk.Tk):
    click_pos = (0, 0)

    def __init__(self):
        super().__init__()

        # disable window manager on the app's window
        super().overrideredirect(True)

        # start the window in the bottom right part of the screen
        self._offsetx = int(0.8 * self.winfo_screenwidth())
        self._offsety = int(0.8 * self.winfo_screenheight())
        super().geometry(f"+{self._offsetx}+{self._offsety}")

        # bind mouse events
        super().bind("<Button-1>", self.clickwin)
        super().bind("<B1-Motion>", self.dragwin)

        # bind closing key
        super().bind("<Escape>", self.close)

    def dragwin(self, _):
        # move the window with the cursor
        x = super().winfo_pointerx() - self._offsetx
        y = super().winfo_pointery() - self._offsety
        super().geometry(f"+{x}+{y}")

    def clickwin(self, event):
        # Track the click position on the general screen
        self.click_pos = (event.x_root, event.y_root)
        self._offsetx = super().winfo_pointerx() - super().winfo_rootx()
        self._offsety = super().winfo_pointery() - super().winfo_rooty()

    def has_cursor_moved(self):
        # Compare the cursor positions at press and release
        return self.click_pos != (super().winfo_pointerx(), super().winfo_pointery())

    def close(self, _=None):
        sys.exit()
