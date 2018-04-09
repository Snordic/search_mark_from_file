'''
Программа ищет в файле маркировки и сохраняет в файл
'''
import os
import sys


def save_file(opened_file, name_file, mark_search, path, first_line):
    dir_txt_name = 'result_txt' + '_' + os.path.basename(sourse)
    name_file_save = os.path.join(dir_txt_name, str(name_file) + '.txt')
    if not os.path.isdir(dir_txt_name):
        os.mkdir(dir_txt_name)
    with open(name_file_save, 'w') as f:
        f.write(first_line)
        while True:
            data = opened_file.readline()
            if mark_search in data or not data:
                break
            f.write(data)
    return data


def read_file(pth, mark):
    name_file = 'result_'
    value_file = 0
    with open(pth, 'r') as f:
        while True:
            first_read = f.readline()
            if not first_read:
                break
            if mark in first_read:
                while True:
                    name_save_file_txt = name_file + str(value_file)
                    result = save_file(opened_file=f,
                                       name_file=name_save_file_txt,
                                       mark_search=mark,
                                       path=pth,
                                       first_line=first_read)
                    if not result:
                        break
                    value_file += 1
                    first_read = result


def calculate_mark(list_mark):
    result = list_mark[0]
    for i in list_mark[1:]:
        result = result + ' ' + i
    return result


if __name__ == '__main__':
    result_mark = calculate_mark(list_mark=sys.argv[2:])
    read_file(pth=sys.argv[1], mark=result_mark)