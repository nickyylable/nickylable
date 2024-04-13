import os

def rename_photos(directory):
    path = os.path.join(os.getcwd(), directory)
    files = os.listdir(path)
    files.sort()
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg'))]
    new_names = []
    for i, filename in enumerate(image_files, start=1):
        new_name = f"photo{i}.jpg"
        new_path = os.path.join(directory, new_name).replace('\\', '/')
        new_names.append(new_path)
        os.rename(os.path.join(path, filename), os.path.join(path, new_name))

    return new_names

photo_names = rename_photos("results7")
print(photo_names)
