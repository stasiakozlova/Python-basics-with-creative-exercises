import os

test_path = r'C:/Windows/help'
path = os.path.normpath(test_path)
print(path)

for dirpath, dirnames, filenames in os.walk(path):
    print(dirpath, dirnames, filenames)

print(os.path.getsize(path))
print(os.path.getsize(r'C:\Windows\help\mui\0419'))
print(os.path.getmtime(r'C:\Windows\help\mui\0419'))
