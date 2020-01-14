import xlwt


def read_file(file_name):
    """
    Function that allow us to read file.
    :param file_name: Name of a file that we want to read.
    :return: Function returns open file on which we can execute:
    read() - load whole content of file into single string;
    readline() - reads a single line from the file; a newline character (\n) is left at the end of the string;
    readlines() - reads all the lines of a file in a list.
    """
    file = open(file_name, 'r')
    return file


def write_file(file_name, value=''):
    """
    Function that allow to save content from value parameter into file. File is going to be create/overwrite.
    :param file_name: Name of a file that we want to create/overwrite with new content.
    :param value: Content that we want to write into file. String. By default is is empty string.
    :return: No return functionality here.
    """
    file = open(file_name, 'w')
    file.write(value)
    file.close()


def append_file(file_name, value):
    """
    Function that allow to append file with a new content.
    :param file_name: Name of a file that we want to append with new content.
    :param value: Content that we want to add to end of our file. String
    :return: No return functionality here.
    """
    file = open(file_name, 'a')
    file.write(value)
    file.close()


def sql_result_to_excel(sql_result, file, sheet_name='Sheet1', column_number_for_style_list=[]):
    """
    Function that saves SQL result to Excel file (xls).
    :param sql_result: SQL result is defined as tuple with lists i.e.: ([1,2,3],[4,5,6], [7,8])
    :param file: File with extenstion that need to be created
    :param sheet_name: Name of createt sheet in the workbook. Optional one, by default it is 'Sheet1'.
    :return: No return functionality here.

    Available styles:
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    """
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheet_name, cell_overwrite_ok=False)
    for x, data in enumerate(sql_result):
        # print(x,data)
        for y, content in enumerate(data):
            # print(x, y, content)
                if y in column_number_for_style_list:
                    sheet.write(x, y, content, style1)
                else:
                    sheet.write(x, y, content)
    book.save(file)

# example how to use styles and other:
# https://github.com/python-excel/xlwt


def load_configs(file, sep='=', comment_char='#'):
    """
    Function responsible for loading data from configuration file.
    It loads data with format like:
    key = 'value'
    Please use single quotes for values!
    :param file: Path to configuration file.
    :param sep: Separator used to read data. By default it is "=".
    :param comment_char: Sign for comment, that is not going to be read by function. by default it is "#".
    :return: Dictionary with data read from configuration file.
    """
    configs = {}
    with open(file, 'r') as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                # value = key_value[1].strip().strip("'")
                value = sep.join(key_value[1:]).strip().strip("'")
                configs[key] = value
    return configs

