import os
import json
import chardet
from pathlib import Path


# Getting the file encoding
def encoding_detect(file_path: str):
    with open(file_path, 'rb') as file:
        raw_data = file.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']

    print(f'{encoding=} | {confidence=}')
    return encoding


# Function for converting the file to UTF-8
def convert_to_utf8(file_path):
    with open(file_path, 'r', encoding='UTF-16') as file:
        data = json.load(file)

    with open(file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f'File {file_path} successfully overwritten.')


# Converting each file to UTF-8
def convert_all_to_utf8():
    current_directory = Path.cwd()
    json_files = [file for file in os.listdir(current_directory) if file.endswith('.json')
                  and encoding_detect(file) == 'UTF-16']

    for file_name in json_files:
        file_path = os.path.join(current_directory, file_name)
        convert_to_utf8(file_path)


if __name__ == '__main__':
    convert_all_to_utf8()
