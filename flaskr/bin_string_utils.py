import struct
import base64


def string_to_bin(string):
    return base64.b64decode(string)


def columns_to_string(columns):
    bytes = b""
    for column in columns:
        for column in column:
            bytes = bytes + struct.pack('B', column)
    return str(base64.b64encode(bytes), "utf-8")


def string_to_columns(string, height=11):
    bytes = base64.b64decode(string)
    columns = []
    column = []
    for count, byte in enumerate(bytes):
        column.append(byte)
        if (count + 1) % height == 0:
            columns.append(column)
            column = []
    return columns


def get_column_at(data, column, height=11):
    return data[height*column:height + height * column]


def discard_first_column(data, height=11):
    return data[height:]
