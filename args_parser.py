import argparse
import textwrap
import sys


class ConsoleArgsParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(ConsoleArgsParser, self).__init__(*args, **kwargs)
        self.prog = 'Searching for duplicates'
        self.formatter_class = argparse.RawDescriptionHelpFormatter
        self.description = textwrap.dedent('''\
                      Script searches for duplicated files in all folders and subfolders.
                      BEWARE: Program has recursion depth 2. This was made because of the
                      computer performance. Certainly, you can use any recursion depth,
                      BUT if you have a lot of files to compare program run could take
                      too much time.\n
                      -----------------------------------------------------------------
                      If you want to stop the program press Ctrl+C.
                      ------------------------------------------------------------------
                      This program had been tested on Python 3.5.2.
                      ''')
        self.add_argument('folder', nargs='?',
                          help='Paste full path to folder, \
                          e.g /home/user/documents/,  in other case \
                          script will search for duplicates in current \
                          folder and all subfolders and shows the result on console screen',
                          action='store')
        self.add_argument('saving_dist', nargs='*',
                          help='Specify the full path to folder and filename\
                              e.g /home/user/documents/duplicates.txt, \
                              else result will be shown in terminal window',
                          type=argparse.FileType('w'), default=None)
        self.add_argument('--depth',
                          help='How deep is recursion must be,\
                              e.g --depth 3 \
                              (default: %(default)s)',
                          type=int, default=2)

    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)
