import tkinter as tk
from window import Win
from tkinter import filedialog

# colors
BLACK = 'black'
DARK_GRAY = '#1f1f1f'
WHITE = 'white'


class TaskListApp:
    def __init__(self, root: Win):
        self.root = root
        self.root.title("")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # create necessary widgets
        self.entry = tk.Entry(self.root, bg=DARK_GRAY, fg=WHITE,
                              justify='left', highlightbackground=DARK_GRAY, relief='solid')
        self.entry.pack(fill='x')
        self.entry.bind('<Return>', self.add_task)

        self.task_list = tk.Listbox(self.root, bg=DARK_GRAY, fg=WHITE, selectbackground=DARK_GRAY,
                                    highlightbackground=DARK_GRAY, relief='solid', activestyle='none')
        self.task_list.pack(expand=True, fill='both')

        # create bindings for task actions
        self.task_list.bind('<Double-Button-1>', self.delete_task)
        self.task_list.bind('<ButtonRelease-1>', self.toggle_done)

        # Create a right-click context menu
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

        # focus on entry widget so that input is immediately possible
        self.entry.focus_set()

    def add_task(self, _):
        # get task text
        task_text = self.entry.get()

        if task_text:
            # add task at the start of the internal list
            self.tasks.insert(0, task_text)

            # add task at the top of the listbox
            self.task_list.insert(0, task_text)

            # clear the entry widget
            self.entry.delete(0, 'end')

    def toggle_done(self, event):
        y = event.y
        nearest_item_index = self.task_list.nearest(y)

        # Listbox.nearest() returns -1 if empty of items
        if nearest_item_index > -1:
            task_geometry = self.task_list.bbox(nearest_item_index)
            if task_geometry[2] and is_event_within_bbox(event, task_geometry, ignore_x=True):
                if not self.root.has_cursor_moved():
                    task = self.tasks[nearest_item_index]
                    if not task.startswith('✓ '):
                        self.tasks[nearest_item_index] = '✓ ' + task
                    else:
                        self.tasks[nearest_item_index] = task[2:]
                    self.task_list.delete(nearest_item_index)
                    self.task_list.insert(nearest_item_index,
                                          self.tasks[nearest_item_index])

        # Set focus to the entry widget even if no task was toggled (handles dragging of empty tasklist)
        self.entry.focus_set()

    def delete_task(self, event):
        selected_index = self.task_list.nearest(event.y)
        if selected_index >= 0:
            # Disable toggle event handling
            self.task_list.unbind("<ButtonRelease-1>")

            # Delete the task item
            self.tasks.pop(selected_index)
            self.task_list.delete(selected_index)

            # Enable event handling after a short delay
            self.root.after(100, self.enable_event_handling)

    def enable_event_handling(self):
        # Re-enable event handling after a short delay
        self.task_list.bind('<ButtonRelease-1>', self.toggle_done)

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def save_tasks(self):
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
    x, y, width, height = int(bbox[0]), int(
        bbox[1]), int(bbox[2]), int(bbox[3])

    if ignore_x:
        # Check if the event's y coord is within the bounding box' height span
        return y <= event.y <= y + height
    else:
        # Check if the event's x and y coordinates are within the bounding box
        return x <= event.x <= x + width and y <= event.y <= y + height


if __name__ == "__main__":
    # prepare the app
    root = Win()
    root.geometry("180x240")
    root.configure(bg="black")
    app = TaskListApp(root)

    # keep the app always in the foreground
    root.attributes('-topmost', 1)

    # # disallow resizing of the window
    # root.resizable(False, False)

    # run the app
    root.mainloop()
