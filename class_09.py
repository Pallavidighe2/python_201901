"""
1 know how -python absolute path # write file
2 file parsing with "with"
3 file parsing with generator
4 parse csv file
5 parse json file
6 parse xml file

"""

from os import path,makedirs

##1 Absolute path

###current absolute path

# file_path=r"c:\repos\Library"

current_file_path = path.abspath(__file__)
# print(current_file_path)
# print(path.dirname(current_file_path))
# print(path.basename(current_file_path))

### get current directory

current_directory = path.dirname(path.abspath(__file__))
print(current_directory)

### concate file path


# json_file_path = path.join(
#     current_directory, "test files", "CSV_files", "json"
# )
# print(json_file_path)
# if path.exists(json_file_path):
#     print("Hello json")
#
# xml_file_path = path.join(current_directory, "test files", "CSV_files", "xml")
# print(xml_file_path)
#
# if path.exists(xml_file_path):
#     print("hello xml")
#
# class_09 = path.join(current_directory, "test files", "CSV_files","class_09")
#
# if not path.exists(class_09):
#     makedirs(class_09)

text_file_path = path.join(current_directory, "test files", "CSV_files", "text")
print(text_file_path)

file_data="dfhudhkjdjksjdkd"


# file_obj=open(text_file_path,"w+")
# file_obj.writelines(file_data)
# file_obj.close()

# with open(text_file_path,"r+")as text_file_read:
#     data=text_file_read.readlines()
#     print(data)

# with open(text_file_path,"r+")as text_file_read:
#     for line in text_file_read:
#         print(line.replace("e","r"))

def generator_parse_file(file_path):
    with open(file_path,"r+")as text_file:
        for line in text_file:
            yield line.replace("\n"," ")

for i in generator_parse_file(text_file_path):
    print(i)

