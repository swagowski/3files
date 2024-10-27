import os
def get_file_line_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for string in file)


def read_and_sort_files(file_names):
    files_info = []
    for file_name in file_names:
        file_path = os.path.join(file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            line_count = len(content)
            files_info.append((file_name, line_count, content))

    files_info.sort(key=lambda x: x[1])
    return files_info


def write_merged_file(output_file, files_info):
    with open(output_file, 'w', encoding='utf-8') as file:
        for file_name, line_count, content in files_info:
            file.write(f"{file_name}\n")
            file.write(f"{line_count}\n")
            file.writelines(content)


def main():
    file_names = ['C:\\Users\\semen\\PycharmProjects\\3files\\task\\1.txt', 'C:\\Users\\semen\\PycharmProjects\\3files\\task\\2.txt', 'C:\\Users\\semen\\PycharmProjects\\3files\\task\\3.txt']
    files_info = read_and_sort_files(file_names)
    write_merged_file('C:\\Users\\semen\\PycharmProjects\\3files\\task\\result.txt', files_info)


if __name__ == '__main__':
    main()


