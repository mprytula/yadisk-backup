import tarfile

def compress_file(file_path, output_path):
    with tarfile.open(output_path, "w:gz") as tar:
        tar.add(file_path, arcname=file_path.split("/")[-1])
