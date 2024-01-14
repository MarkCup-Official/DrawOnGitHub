def append_line_to_file(path, name, new):
    file_path = f'{path}/{name}'

    # 以追加模式打开文件，如果文件不存在则创建
    with open(file_path, 'a+') as file:
        file.seek(0, 2)
        file.write(new)