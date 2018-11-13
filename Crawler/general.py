import os


# Create directory for website
def create_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory")
        os.makedirs(directory)


# Create new file
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# Create queue and crawed files
def create_data_files(project_name, base_url):
    queue = project_name + "/queued.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

# Add data in the existing file (crawled, queued files)
def append_to_file(path, data):
    with open(path, "a") as file: # To refer to the file object
        file.write(data, "\n")

# Delete contents of file
def del_file_contents(path):
    with open(path, "w"):
        pass
