import os


def myrename(path):
    file_list = os.listdir(path)
    for i, fi in enumerate(file_list):
        old_name = os.path.join(path, fi)
        new_name = os.path.join(path, "folder_"+str(i+174))
        os.rename(old_name, new_name)


if __name__ == "__main__":
    path = "F:\\job_exam\\after_crop\\181-203"
    myrename(path)