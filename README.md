A small app for AGH python classes.

This app uses string interpolation so You must use Python 3.6+

It purpose is to parse a room electronic devices from a yaml file
and then create a window for operating (switching on and off) the devices

First argument of this prog must be the .yaml file. I have made three example files
where the third one is wrongly formatted.

Solution:
1) We are making a Tk object for our gui
2) Constructor is making each page (frame) from the data for yaml file
3)