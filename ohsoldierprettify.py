# def organiser(path, file, format):
#     import os
#     f=open(file)
#     os.chdir(path)
#     i=1
#     for file1 in os.listdir(path):
#         if file1 not in f:
#             os.rename(file1, file1.capitalize())
#     for file2 in os.listdir(path):
#         if format in file2:
#             os.rename(f"{file2}", f"{i}.{format}")
#             i=i+1


# Main Solution...!
import os


def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1


soldier(r"C:\Users\AYeddula\OneDrive - DXC Production\Desktop\Python testing",
        r"C:\Users\AYeddula\OneDrive - DXC Production\Desktop\Pythonlang", ".png")

# To Get Access All The Images Present In The File..!
