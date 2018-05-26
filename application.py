'''
Module only for the gui class and socket management
'''

import tkinter as tk
from functools import partial
import socket

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

        # creating a dict for page managing
        self.frames = {}

        self.pack()
        self.create_widgets(data)
    # end def

    def create_widgets(self, data):
        '''
        Create and set widgets

        :param data: data for creating widgets
        '''
        self.master.title("Pilot")

        # creating a container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # a menu bar object
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
        # end for

        # add quit command
        menubar.add_command(label="Quit!", command=self.master.quit)

        self.master.config(menu=menubar)
    # end def

    def show_frame(self, page_name):
        '''
        Helping function responsible for switching frames

        :param page_name: name to which page switch
        '''
        # for debuging purposes
        print("switching to frame: " + page_name)
        frame = self.frames[page_name]
        frame.tkraise()
    # end def
# end class


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

        self.create_buttons(data)
    # end def

    def create_buttons(self, data: dict):
        '''
        Method for creating buttons and labels

        :param data: data for creating buttons and labels in frame
        '''
        room_name, buttons = data

        i = 0
        for b_fun, b_name in buttons.items():
            tmp_lab = tk.Label(self, text=b_name)
            tmp_lab.grid(column=0, row=i)

            tmp_on_but, tmp_off_but = self.init_but_fun(b_fun)
            tmp_on_but.grid(column=3, row=i)
            tmp_off_but.grid(column=4, row=i)
            i += 1
        # end for
    # end def

    def init_but_fun(self, button):
        '''
        Function to initialize buttons for frame

        :param button: id of device
        '''
        on_but = tk.Button(self, text='ON', command=partial(self.send_signal, button, 'on'))
        off_but = tk.Button(self, text='OFF', command=partial(self.send_signal, button, 'off'))

        return [on_but, off_but]
    # end def

    def send_signal(self, object_name, which):
        '''
        Method which sends UDP on a specific addres

        :param object_name: id of the device
        :param which: what signal on or off
        '''
        #which == on/off
        if which not in ['on', 'off']:
            print("wrong fun")
            return
        #end if

        msg = f'{which} {object_name}'
        ADDR = ("255.255.255.255", 2018)

        # creating, connecting and sending
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.sendto(bytes(msg, "utf-8"), ADDR)
        except socket.error:
            print("Could not be able to connect")
            s.close()
            return
        # end try

        s.close()
    # end def
# end class

def init_gui(data):
    '''
    Function used to initialize our gui
    :param data: data for interface
    :return: gui object
    '''
    root = tk.Tk()
    return Application(master=root, data=data)
# end def