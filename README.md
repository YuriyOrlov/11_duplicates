# Anti-Duplicator

This program searches duplicated files in folders and subfolders according to the specified path. If folder hasn't been specified it searches files in all possible locations inside folder, where it is situated.

### Usage example

The first example of script launch on Linux Ubuntu 16.04 LTS, Python 3.5.2:

Here we will try to find duplicated files with recursion's depth 5 (default is 2) and make program show all files in terminal window.

```#!bash
$ python duplicates.py ~/Projects/test --depth 5  

Duplicates found

/home/yo_n/Projects/test/test3/test_file_2.txt
/home/yo_n/Projects/test/test2/test_file_2.txt
/home/yo_n/Projects/test/test1/test_file_2.txt


/home/yo_n/Projects/test/test2/test_file_1.txt
/home/yo_n/Projects/test/test1/test_file_3.txt
/home/yo_n/Projects/test/test1/test_file_1.txt


```

In the second example program will create a TXT file with all duplicated files with default recursion's depth.
File will be created in a folder where the program is located.

```#!bash
$ python duplicates.py ~/Projects/test ~/Projects/test_duplicate.txt
File «/home/user/Projects/test_duplicate.txt» created.
```

# Possible script commands

positional arguments:
  folder         Paste full path to folder, e.g /home/user/documents/, in
                 other case script will search for duplicates in current
                 folder and all subfolders and shows the result on console
                 screen
  saving_dist    Specify the full path to folder and filename e.g
                 /home/user/documents/duplicates.txt, else result will be
                 shown in terminal window

optional arguments:
  -h, --help     show this help message and exit
  --depth DEPTH  How deep is recursion must be, e.g --depth 3 (default: 2)

### BEWARE: 
Program has recursion depth 2. This was made because of the computer performance. Certainly, you can use any recursion depth, BUT if you have a lot of files to compare program run could take too much time.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
