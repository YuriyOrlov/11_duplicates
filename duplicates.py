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
    return [[file1, file2] for file1, file2 in files_comb if cmp(file1, file2, True)]


if __name__ == '__main__':
    files_from_subfolders = [file.path for file in scantree(argv[1] if len(argv) > 1 else '.', int(argv[2]) if len(argv) > 2 else 5)]
    duplicates_list = get_duplicates(files_from_subfolders)
    if duplicates_list:
        print('\nDuplicates found\n')
        for file_with_path in duplicates_list[0]:
            print('{}\n'.format(file_with_path))
    else:
        print('No duplicates found.')
