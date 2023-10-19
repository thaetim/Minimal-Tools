import tkinter as tk
from window import Win
from tkinter import filedialog

# Constants for colors
BLACK = 'black'
DARK_GRAY = '#1f1f1f'
WHITE = 'white'

class TaskListApp:
    """Task list application."""

    def __init__(self, root: Win):
        """Initialize the task list application.

        Args:
            root (Win): The main application window.

        """
        self.root = root
        self.root.title("")

        # Internal tasks array
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        """Create application widgets and set up event bindings."""

        # Create an entry widget for task input
        self.entry = tk.Entry(self.root, bg=DARK_GRAY, fg=WHITE,
                              justify='left', highlightbackground=DARK_GRAY, relief='solid')
        self.entry.pack(fill='x')
        self.entry.bind('<Return>', self.add_task)

        # Create a listbox for displaying tasks
        self.task_list = tk.Listbox(self.root, bg=DARK_GRAY, fg=WHITE, selectbackground=DARK_GRAY,
                                    highlightbackground=DARK_GRAY, relief='solid', activestyle='none')
        self.task_list.pack(expand=True, fill='both')

        # Create bindings for task actions
        self.task_list.bind('<Double-Button-1>', self.delete_task)
        self.task_list.bind('<ButtonRelease-1>', self.toggle_done)

        # Create a right-click context menu and its options
        self.context_menu = tk.Menu(
            self.root, tearoff=0, bg=DARK_GRAY, fg=WHITE, relief='flat')
        self.context_menu.add_command(
            label="Save", command=self.save_tasks)
        self.context_menu.add_command(
            label="Load", command=self.load_tasks)
        self.task_list.bind("<Button-3>", self.show_context_menu)
        self.context_menu.add_command(
            label="Exit", command=self.root.close)
        self.task_list.bind("<Button-3>", self.show_context_menu)

        # Focus on entry widget so that input is immediately possible
        self.entry.focus_set()

    def add_task(self, _):
        """Add a task to the list of tasks.

        Args:
            _: Unused event argument.

        """
        # Get task text
        task_text = self.entry.get()

        if task_text:
            # Add task at the start of the internal list
            self.tasks.insert(0, task_text)

            # Add task at the top of the listbox
            self.task_list.insert(0, task_text)

            # Clear the entry widget
            self.entry.delete(0, 'end')

    def toggle_done(self, event):
        """Toggle the done status of a task.

        Args:
            event: Mouse event containing click information.

        """
        y = event.y
        nearest_item_index = self.task_list.nearest(y)

        # Listbox.nearest() returns -1 if the list is empty
        if nearest_item_index > -1:

            # Get the bounding box of the task listbox item
            task_geometry = self.task_list.bbox(nearest_item_index)

            # Check if the event (mouse click) happened on the task listbox item
            if task_geometry[2] and is_event_within_bbox(event, task_geometry, ignore_x=True):

                # Prevent toggling of the task if the window has been just dragged
                if not self.root.has_cursor_moved():

                    task = self.tasks[nearest_item_index]

                    # Toggle the task completion prefix in the internal tasks array
                    if not task.startswith('✓ '):
                        self.tasks[nearest_item_index] = '✓ ' + task
                    else:
                        self.tasks[nearest_item_index] = task[2:]

                    # Reflect the changes in the listbox
                    self.task_list.delete(nearest_item_index)
                    self.task_list.insert(nearest_item_index,
                                          self.tasks[nearest_item_index])

        # Set focus to the entry widget even if no task was toggled (handles dragging of empty task list)
        self.entry.focus_set()

    def delete_task(self, event):
        """Delete a task from the list.

        Args:
            event: Mouse event containing click information.

        """
        selected_index = self.task_list.nearest(event.y)
        if selected_index >= 0:
            # Disable toggle event handling
            self.task_list.unbind("<ButtonRelease-1>")

            # Delete the task item from the tasks array and the listbox
            self.tasks.pop(selected_index)
            self.task_list.delete(selected_index)

            # Enable event handling after a short delay
            self.root.after(100, self.enable_event_handling)

    def enable_event_handling(self):
        """Re-enable event handling after a short delay."""

        # Re-enable event handling after a short delay
        self.task_list.bind('<ButtonRelease-1>', self.toggle_done)

    def show_context_menu(self, event):
        """Display the context menu.

        Args:
            event: Mouse event containing the click position.

        """
        self.context_menu.post(event.x_root, event.y_root)

    def save_tasks(self):
        """Save tasks to a text file."""

        # Ask the user to select a file to save the tasks
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, "w") as file:
                    for task in self.tasks:
                        file.write(task + "\n")
            except Exception as e:
                print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """Load tasks from a text file."""
        
        # Ask the user to select a file to load tasks from
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.tasks = [line.strip() for line in file.readlines()]
                    self.task_list.delete(0, "end")  # Clear the listbox
                    for task in self.tasks:
                        self.task_list.insert("end", task)
            except Exception as e:
                print(f"Error loading tasks: {e}")

def is_event_within_bbox(event, bbox, ignore_x=False):
    """Check if the event is within a given bounding box.

    Args:
        event: Mouse event containing the click position.
        bbox: Bounding box (x, y, width, height).
        ignore_x: Flag to ignore the x-coordinate.

    Returns:
        bool: True if the event is within the bounding box, False otherwise.

    """
    x, y, width, height = int(bbox[0]), int(
        bbox[1]), int(bbox[2]), int(bbox[3])

    if ignore_x:
        # Check if the event's y coord is within the bounding box' height span
        return y <= event.y <= y + height
    else:
        # Check if the event's x and y coordinates are within the bounding box
        return x <= event.x <= x + width and y <= event.y <= y + height

if __name__ == "__main__":
    # Prepare the app
    root = Win()
    root.geometry("180x240")
    root.configure(bg="black")
    app = TaskListApp(root)

    # Keep the app always in the foreground
    root.attributes('-topmost', 1)

    # # Disallow resizing of the window
    # root.resizable(False, False)

    # Run the app
    root.mainloop()
