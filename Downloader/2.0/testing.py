import os; import subprocess; import time;
target_path = r'C:\Users\Потребител\Downloads'
link_input = input('Enter the link: ')

start = time.time()
subprocess.run(["yt-dlp", "-P", target_path, link_input])
with os.scandir(target_path) as it:
    final_list = [item.name for item in it if item.name.endswith(".webm") or item.name.endswith(".mkv")][0]
print(final_list)
# file_name = [i for i in os.listdir(target_path) if i.endswith(".webm") or i.endswith(".mkv")][0]
# print(file_name)
end = time.time()
print('Start:', start, 'End:', end)