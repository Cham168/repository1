import functools
import shutil
import urllib.request
import string


def retry(attempts=5, desired_value=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    break
                elif i == attempts - 1:
                    print("Не вдалося досягнути бажаного значення.")
                    break
            return result
        return wrapper
    return decorator


@retry(attempts=3, desired_value=True)
def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)
    return True


def read_file(url):
    response = urllib.request.urlopen(url)
    lines = 0
    size = 0
    char_count = {}
    for line in response:
        lines += 1
        size += len(line)
        for char in line:
            if char in string.whitespace:
                continue
            char_count[char] = char_count.get(char, 0) + 1
    top_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)[:3]
    result = {'lines': lines, 'size': size, 'top_chars': top_chars}
    return result

if __name__ == '__main__':
    source_path = 'path/to/source/file.txt'
    destination_path = 'path/to/destination/file.txt'
    copy_file(source_path, destination_path)

    url = 'https://raw.githubusercontent.com/dscape/spell/master/test/resources/big.txt'
    file_info = read_file(url)
    print(f"Количество строк в файле: {file_info['num_lines']}")
    print(f"Размер файла в байтах: {file_info['size_bytes']}")
    print(f"Топ-3 символов в файле: {file_info['top_chars']}")
