def get_media_type(file_name):
    """
    Returns the media type of the file with the given name.
    """
    if file_name.lower().endswith((".gif", ".png", ".jpg", ".jpeg")):
        return "image/gif"
    elif file_name.lower().endswith((".pdf")):
        return "application/pdf"
    elif file_name.lower().endswith((".txt")):
        return "text/plain"
    elif file_name.lower().endswith((".zip")):
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    """
    Prompts the user for a file name, and prints the media type of the file.
    """
    file_name = input("Enter the name of the file: ")
    media_type = get_media_type(file_name)
    print(f"The media type of the file is {media_type}.")

if __name__ == "__main__":
    main()



