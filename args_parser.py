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
        self.add_argument('--folder', nargs='?',
                          help='Paste full path to folder, in other case \
                          e.g --folder /home/user/documents/ \
                          script will search for duplicates in current folder and all subfolders \
                          (default: %(default)s)',
                          action='store', default='.')
        self.add_argument('--depth',
                          help='How deep is recursion must be,\
                              e.g --depht 3 \
                              (default: %(default)s)',
                          type=int, default=2)
        self.add_argument('--result',
                          help='Where script present a result: \
                              for file write --result file,\
                              else reault will be shown in terminal window\
                              (default: %(default)s)',
                          type=str, default='scr')

    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)
