from pathlib import Path; import os

destination = Path('D:\DOWNLOADE') # chosen path, maybe later version will be with selected path, not a fixed one
with os.scandir(destination) as files:
    for file in files:
        file_size_kb = file.stat().st_size / 1024
        file_size_mb = file_size_kb / 1024
        file_size_gb = file_size_mb / 1024
        # print(file.name, '-', f'{file_size_kb:.2f} KB')
        if file_size_mb > 100 and file_size_gb < 1:
            print(file.name, '-', f'{file_size_mb:.2f} MB')
        if file_size_gb > 1:
            print(file.name, '-', f'{file_size_gb:.2f} GB')