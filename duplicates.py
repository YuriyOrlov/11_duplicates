import os
from sys import argv
from args_parser import ConsoleArgsParser
import hashlib
import collections


def scantree(path, depth):
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False) and depth:
            yield from scantree(entry.path, depth - 1)
        else:
            yield entry


def hashfile(path, blocksize=65536):
    if os.path.isfile(path):
        try:
            file_for_hashing = open(path, 'rb')
        except FileNotFoundError:
            return None
        hasher = hashlib.md5()
        buff = file_for_hashing.read(blocksize)
        while len(buff) > 0:
            hasher.update(buff)
            buff = file_for_hashing.read(blocksize)
        file_for_hashing.close()
        return hasher.hexdigest()


def get_duplicates(file_paths):
    files_with_same_hashsum = collections.defaultdict(list)
    hashed_files_list = [(hashfile(path), path) for path in file_paths]
    [files_with_same_hashsum[hashsum].append(path) for hashsum, path in hashed_files_list if hashsum is not None]
    results = list(filter(lambda x: len(x) > 1, files_with_same_hashsum.values()))
    return results


def writing_duplicates_into_file(path_to_duplicates_list, filename):
    with open(filename, 'w') as duplicates:
        duplicates.write('\nDuplicates found\n\n')
        for block_of_files in path_to_duplicates_list:
            for file_with_path in block_of_files:
                duplicates.write('{}\n'.format(file_with_path))
            duplicates.write('\n')


def showing_duplicates_in_console(path_to_duplicates_list):
    print('\nDuplicates found\n')
    for block_of_files in path_to_duplicates_list:
        for file_with_path in block_of_files:
            print('{}'.format(file_with_path))
        print('\n')


if __name__ == '__main__':
    args_parser = ConsoleArgsParser()
    args = args_parser.parse_args()
    path_to_begin, recursion_limitation, form_of_result_representation = args.folder, args.depth, args.saving_dist
    files_from_subfolders = [path_to_file.path for path_to_file in scantree(path_to_begin, recursion_limitation)]
    duplicates_list = get_duplicates(files_from_subfolders)
    if duplicates_list and not form_of_result_representation:
        showing_duplicates_in_console(duplicates_list)
    elif duplicates_list and form_of_result_representation:
        filename_for_duplicated_files = form_of_result_representation[0].name
        writing_duplicates_into_file(duplicates_list, filename_for_duplicated_files)
        print('File «{}» created.'.format(filename_for_duplicated_files))
    else:
        print('No duplicates found.')
