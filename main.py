import tkinter as tk


class PopupWindow(tk.Toplevel):
    def __init__(self, parent, count):
        super().__init__(parent, bg="black")
        self.overrideredirect(True)
        self.count = count

        tk.Label(
            self,
            textvariable=count,
            bg="green",
            fg="white",
            font=("helvetica", 12),
            width=3).pack(padx=5, pady=5)

        tk.Button(
            self,
            text=" Up ",
            command=lambda: self.increment(1),
            bg="black",
            fg="green").pack(padx=5, pady=5)

        tk.Button(
            self,
            text="Down",
            command=lambda: self.increment(-1),
            bg="black",
            fg="green").pack(padx=5, pady=5)

    def increment(self, amount):
        self.count.set(self.count.get() + amount)


class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Root Window")
        self.popups = []
        self.count = tk.IntVar(self, 20)

        tk.Label(self, textvariable=self.count, width=5) \
            .pack(padx=5, pady=5, side=tk.LEFT)

        tk.Button(self, text="Destroy All Popups", command=self.destroy_popups) \
            .pack(padx=5, pady=5, side=tk.LEFT)

        tk.Button(self, text="Create New Popup", command=self.popup) \
            .pack(padx=5, pady=5, side=tk.LEFT)

    def popup(self):
        """Create a popup window"""
        id = len(self.popups)
        popup = PopupWindow(self, self.count
        )
        self.popups.append(popup)
        x = (id % 5) * 120
        y = (id // 5) * 120
        popup.geometry(f"{120}x{120}+{x}+{y}")

    def destroy_popups(self):
        """Destroy all the popup windows"""
        for pop in self.popups:
            pop.destroy()
        self.popups = []


RootWindow().mainloop()
