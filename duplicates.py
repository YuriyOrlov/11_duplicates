import os
from sys import argv
import itertools
from filecmp import cmp
from args_parser import ConsoleArgsParser


def scantree(path, depth):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir(follow_symlinks=False) and depth:
            yield from scantree(entry.path, depth - 1)
        else:
            yield entry


def get_duplicates(files):
    files_comb = itertools.combinations(files, 2)
    return [[file1, file2] for file1, file2 in files_comb if cmp(file1, file2, True)]


def writing_duplicates_into_file(duplicates_list):
    with open('duplicated_files.txt', 'w') as duplicates:
        for file_with_path in duplicates_list:
            duplicates.write('{} <---> {}\n'.format(file_with_path[0], file_with_path[1]))


if __name__ == '__main__':
    args_parser = ConsoleArgsParser()
    args = args_parser.parse_args()
    path_to_begin, recursion_limitation, form_of_result_representation = args.folder, args.depth, args.result
    files_from_subfolders = [file.path for file in scantree(path_to_begin, recursion_limitation)]
    duplicates_list = get_duplicates(files_from_subfolders)
    if duplicates_list and (form_of_result_representation == 'scr'):
        print('\nDuplicates found\n')
        for file_with_path in duplicates_list:
            print('{} <---> {}'.format(file_with_path[0], file_with_path[1]))
    elif duplicates_list and (form_of_result_representation == 'file'):
        writing_duplicates_into_file(duplicates_list)
        print('File «duplicated_files.txt» created.')
    else:
        print('No duplicates found.')
