import tkinter as tk
import yaml
import application


def make_the_data_better_for_this_prog(data):
    new_data = []
    for room in data:
        for k, v in room.items():
            if v is None:
                new_room = change_room(room, k)
                new_data.append((k, new_room))
                break

    return new_data


def change_room(room, k):
    r = dict(room)
    r.pop(k)
    return r


def yaml_parser(file_name):
    stream = open(file_name, 'r')
    data = yaml.load(stream)

    return data


def main():
    data = make_the_data_better_for_this_prog(yaml_parser('input.yaml'))
    print(data)

    k, v = data[0]
    print(k)
    print(v)

    app = application.init_gui(data)
    app.mainloop()


if __name__ == '__main__':
    main()