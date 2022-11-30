# WakeOnLAN

This is a program that aims to remotely turn on a computer that is physically turned off. For this purpose the program uses Wake on LAN packet (aka magic packet -> more here: https://en.wikipedia.org/wiki/Wake-on-LAN). The program is based on a console window (it is supposed to imitate a terminal).

The program is written in python and uses the following libraries

+ **colorama, termcolor** -> the ability to change the colors of the output
+ **mcstatus** -> library that checks if the port is running 
                       minecraft server
+ **sys, os** -> create and open files necessary for the program to work
+ **json** -> library for manipulating json files
+ **wakeonlan** -> creates Wake on LAN packets


The program stores server information in "**list.JSON**". If this server is not found in the folder where the program itself is, the program creates the folder with basic parameters. To edit the file, you can use the "edit" function of the program, which takes the information and converts it into the correct format, or you can edit it manually. 
