import tkinter as tk


class App:
    def __init__(self):
        self.toplevel = None

        self.main = tk.Tk()
        self.main.title("How to centralize a Tkinter Window")
        # self.main.resizable(False, False)
        self.jogar = None

        # row 0
        label_desc = tk.Label(self.main, font=("Arial", 20, "bold"),
                              text="This is a example of window in Tkinter \nwhich "
                                   "opens (Tkinter default) uncentralized.")
        label_desc.grid(row=0, column=0, padx=(30, 30), sticky="S")

        # row 1
        label_hint = tk.Label(self.main, fg="red", font=("Tahoma", 10, "italic"),
                              text="You can resize the window and click the centralize button as many times "
                                   "as you want.")
        label_hint.grid(row=1, column=0, sticky="N")

        # row 2
        button_centralize = tk.Button(self.main, text="Click to centralize!", font=("Tahoma", 12, "bold"),
                                      command=lambda: self.centralize_window(self.main))
        button_centralize.grid(row=2, column=0, sticky="N")

        # row 3
        label_new_window = tk.Label(self.main, text="Clicking the button below you can see a window that already starts"
                                                    "centered")
        label_new_window.grid(row=3, column=0, pady=(30, 0), sticky="S")

        # row 4
        button_new_window = tk.Button(self.main, text="Open new centered window", command=self.newWindow)
        button_new_window.grid(row=4, column=0, pady=0, sticky="N")

        for i in range(5):  # Ensure that the elements arranged when you resize the window
            self.main.grid_rowconfigure(i, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.main.mainloop()

    def newWindow(self):
        # self.main.withdraw()
        self.toplevel = tk.Toplevel(self.main)
        self.toplevel.title("A centralized window")
        # self.jogar.resizable(False, False)

        # row 0
        label_desc = tk.Label(self.toplevel, font=("Sans Serif Comic", 15, "italic"),
                              text="This is an automatic centralized Tkinter window.")
        label_desc.grid(row=0, column=1, sticky="WE")

        # row 1
        label_hint = tk.Label(self.toplevel, font=("Sans Serif Comic", 12, "bold"),
                              text="Note that it is necessary to use the 'update_idletasks()' before calling the "
                                   "centralizeWindow() method.")
        label_hint.grid(row=1, column=1, sticky="WE")

        self.toplevel.update_idletasks()  # Ensures the winfo_width method knows the correct window size
        # Needs to be used before centralizeWindow()
        self.centralize_window(self.toplevel)

    @staticmethod
    def centralize_window(tk_element):
        """Centralize a Tkinter window"""
        screen_width = tk_element.winfo_screenwidth()
        screen_height = tk_element.winfo_screenheight()
        window_width = tk_element.winfo_width()
        window_height = tk_element.winfo_height()

        width = (screen_width / 2) - (window_width / 2)
        height = (screen_height / 2) - (window_height / 2)
        height -= screen_height * 0.04  # Increment 4% in height value to discount windows taskbar (optional)

        width = int(width)
        height = int(height)
        tk_element.geometry("+{}+{}".format(width, height))  # geometry() does not accept float values


app = App()
