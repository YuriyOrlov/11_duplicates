# Anti-Duplicator

This program searches duplicated files in folders and subfolders according to the specified path. If folder hasn't been specified it searches files in all possible locations inside folder, where it is situated.

### Usage example

First example of script launch on Linux Ubuntu 16.04 LTS, Python 3.5.2:

Here we will try to find duplicated files with recursion's depth 5 (default is 2) and make program show all files in terminal window.

```#!bash
$ python duplicates.py --folder ~/Projects/test --depth 5  

Duplicates found

~/Projects/test/test3/test_file_2.txt <---> ~/Projects/test/test2/test_file_2.txt
~/Projects/test/test3/test_file_2.txt <---> ~/Projects/test/test1/test_file_2.txt
~/Projects/test/test2/test_file_2.txt <---> ~/Projects/test/test1/test_file_2.txt
~/Projects/test/test2/test_file_1.txt <---> ~/Projects/test/test1/test_file_3.txt
~/Projects/test/test2/test_file_1.txt <---> ~/Projects/test/test1/test_file_1.txt
~/Projects/test/test1/test_file_3.txt <---> ~/Projects/test/test1/test_file_1.txt

```

In second example program will create a TXT file with all duplicated files with default recursion's depth.
File will be created in a folder where the program is located.

```#!bash
$ python duplicates.py --folder ~/Projects/test --result file
File «duplicated_files.txt» created.
```

# Possible script commands

  --folder [FOLDER]  Paste full path to folder, in other case e.g --folder
                     /home/user/documents/ script will search for duplicates
                     in current folder and all subfolders (default: .)

  --depth DEPTH      How deep is recursion must be, e.g --depth 5 (default: 2)

  --result RESULT    Where script present a result: for file write --result
                     file, else reault will be shown in terminal window
                     (default: scr)

## BEWARE: 
Program has recursion depth 2. This was made because of the computer performance. Certainly, you can use any recursion depth, BUT if you have a lot of files to compare program run could take too much time.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
