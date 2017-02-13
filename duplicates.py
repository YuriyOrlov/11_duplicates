import os
from sys import argv
from itertools import combinations
from filecmp import cmp


def scantree(path, depth=5):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir(follow_symlinks=False) and depth:
            yield from scantree(entry.path, depth - 1)
        else:
            yield entry


def get_duplicates(files):
    files_comb = [item for item in combinations(files, 2)]
    combinations_list = [[file1, file2] for file1, file2 in files_comb if cmp(file1, file2, True)]
    return combinations_list


def has_input_length(argv):
    if len(argv) > 2:
        return argv[1], int(argv[2])
    elif len(argv) > 1:
        return argv[1], 5
    else:
        return '.', 5


if __name__ == '__main__':
    path_to_begin, recursion_limitation = has_input_length(argv)
    files_from_subfolders = [file.path for file in scantree(path_to_begin, recursion_limitation)]
    duplicates_list = get_duplicates(files_from_subfolders)
    if duplicates_list:
        print('\nDuplicates found\n')
        for file_with_path in duplicates_list:
            print('{} <---> {}'.format(file_with_path[0], file_with_path[1]))
    else:
        print('No duplicates found.')
