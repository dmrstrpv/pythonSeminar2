
import os


def rename_multiple_files():
    directory = "test_dir"
    for cnt, filename in enumerate(os.listdir(directory)):
        dst = f"Some_name{str(cnt)}.jpg"
        src = f"{directory}/{filename}"
        dst = f"{directory}/{dst}"
        os.rename(src, dst)


if __name__ == '__main__':
    rename_multiple_files()

