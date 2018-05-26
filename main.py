'''
In the first argument enter the input .yaml file

The only working .yaml format is the one in example

Specially used the '# end ' comments for code better reading

My code didn't worked for 255.255.255.255 address but for other worked
'''
import yaml
import application


def make_the_data_better_for_this_prog(data):
    '''
    Function for making the output of yaml.load better
    for app purposes
    :param data: yaml.load
    :return: list with better made dict
    '''
    new_data = []
    for room in data:
        for k, v in room.items():
            if v is None:
                new_room = change_room(room, k)
                new_data.append((k, new_room))
                break
            # end if
        # end for
    # end for

    return new_data
# end def


def change_room(room, k):
    r = dict(room)
    r.pop(k)
    return r
# end def


def id_data_corrupted(data):
    '''
    Function to check if in room is a device id without
    any label
    :param data: data from yaml file
    :return: True if everything is good, else False
    '''

    for room in data:
        # i is the counter how many keys have None value
        i = 0
        for k, v in room.items():
            if v is None:
                if i == 2:
                    return False
                # end if
                i += 1
            # end if
        # end for
    # end for
    return True
# end def



def yaml_parser(file_name):
    '''
    Function to open a file and then parse it content

    :param file_name: name of file
    :return: file content
    '''
    try:
        stream = open(file_name, 'r')
    except OSError:
        print("Cannot open file")
        exit(1)
    # end try

    data = yaml.safe_load(stream)

    if id_data_corrupted(data):
        print("Data in file is wrongly formatted")
        exit(1)
    # end if

    return data
# end def


def main():
    data = make_the_data_better_for_this_prog(yaml_parser('input.yaml'))

    k, v = data[0]
    print(k)
    print(v)

    app = application.init_gui(data)
    app.mainloop()
# end def


if __name__ == '__main__':
    main()
# end if