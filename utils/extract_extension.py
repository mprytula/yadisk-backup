def extract_extension(filename):
    dot_position = filename.find('.')
    if dot_position != -1:
        return filename[dot_position:]
    else:
        return ""