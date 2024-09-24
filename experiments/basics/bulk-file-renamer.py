import os

def bulk_rename(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, f"{prefix}{count}{os.path.splitext(filename)[1]}")
        os.rename(src, dst)
    print("Files renamed successfully.")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    prefix = input("Enter new filename prefix: ")
    bulk_rename(directory, prefix)

