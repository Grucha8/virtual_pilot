import tkinter as tk
from functools import partial

class Application(tk.Frame):
    '''
    This is the Class for our main window
    '''
    def __init__(self, master=None, data=None):
        '''
        Constructor

        :param master:
        :param data: data needed for making frames and buttons
        '''
        super().__init__(master)

        self.frames = {}

        self.pack()
        self.create_widgets(data)

    def create_widgets(self, data):
        '''
        Create and set widgets

        :param data: data for creating widgets
        '''
        self.master.title("Pilot")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(self.master)
        for page in data:
            room_name, buttons = page

            frame = Frame(parent=container, controller=self, data=page)
            self.frames[room_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            # add menu command for this frame
            menubar.add_command(label=room_name, command=partial(self.show_frame, room_name))

        # add quit command
        menubar.add_command(label="Quit!", command=self.master.quit)

        self.master.config(menu=menubar)

    def show_frame(self, page_name):
        '''
        Helping function responsible for switching frames

        :param page_name: name to which page switch
        '''
        print("switching to frame: " + page_name)
        frame = self.frames[page_name]
        frame.tkraise()


# noinspection PyUnresolvedReferences
class Frame(tk.Frame):
    '''
    Class representing frames in our main window
    '''
    def __init__(self, parent, controller, data):
        '''
        Constructor

        :param parent: the parent should be the main Frame
        :param controller: who is controlling it (should be the main frame)
        :param data: data which is going to be written into this frame
        '''
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.buttons = []
        self.tag_names = []

        self.create_buttons(data)

    def create_buttons(self, data: dict):
        room_name, buttons = data

        i = 0
        for b_fun, b_name in buttons.items():
            tmp_lab = tk.Label(self, text=b_name)
            tmp_lab.grid(column=0, row=i)

            tmp_on_but, tmp_off_but = self.init_but_fun(b_fun)
            tmp_on_but.grid(column=3, row=i)
            tmp_off_but.grid(column=4, row=i)
            i += 1

        # for k, v in data.items():
        #     tmpL = tk.Label(self, text=v)
        #     tmpL.pack(side=tk.LEFT)
        #
        #     tmpB = tk.Button(self, text=k)
        #     tmpB.pack(side=tk.LEFT)
        #
        #     self.buttons.append(tmpB)
        #     self.tag_names.append(tmpL)

    def init_but_fun(self, button):
        # TODO change command for socekt function
        on_but = tk.Button(self, text='ON', command=partial(heh, f"{button} ON"))
        off_but = tk.Button(self, text='OFF', command=partial(heh, f"{button} OFF"))

        return [on_but, off_but]


def heh(text):
    print(text)


def init_gui(data):
    root = tk.Tk()
    return Application(master=root, data=data)
