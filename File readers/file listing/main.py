from pathlib import Path

destination = Path('D:\DOWNLOADE')
# with os.scandir(destination) as files:
#     for file in files:
#         file_size_kb = file.stat().st_size / 1024
#         file_size_mb = file_size_kb / 1024
#         file_size_gb = file_size_mb / 1024
#         # print(file.name, '-', f'{file_size_kb:.2f} KB')
#         # if file_size_mb > 100 and file_size_gb < 1:
#         #     print(file.name, '-', f'{file_size_mb:.2f} MB')
#         if file_size_gb > 1:
#             print(file.name, '-', f'{file_size_gb:.2f} GB')

file_count = 0

files_only = [p for p in destination.rglob("*") if p.is_file()]
for file in files_only:
        file_size_kb = file.stat().st_size / 1024
        file_size_mb = file_size_kb / 1024
        file_size_gb = file_size_mb / 1024
        # print(file.name, '-', f'{file_size_kb:.2f} KB')
        if file_size_mb >= 100 and file_size_gb < 1:
            file_count += 1
            print(file.name, '-', f'{file_size_mb:.2f} MB', f'- File path: {Path(file).absolute()}')
        if file_size_gb >= 1:
            file_count += 1
            print(file.name, '-', f'{file_size_gb:.2f} GB', f'- File path: {Path(file).absolute()}')

print(f'Total files found: {file_count}')