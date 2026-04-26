import os


def iter_dirs(sPath):
    for s_child in os.listdir(sPath):
        s_child_path = os.path.join(sPath, s_child)
        if os.path.isdir(s_child_path):
            iter_dirs(s_child_path)
        else:
            print(s_child_path)


iter_dirs(r"C:\Users\wjkao\PycharmProjects\pythonProject\面试_202601")
