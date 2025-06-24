#10. Write a Python program to copy an image file (binary mode) from one location to another.
# Open source image in binary read mode
with open("cartoon.jpeg", "rb") as src:
    # Open destination image in binary write mode
    with open("copied_image.jpeg", "wb") as dest:
        dest.write(src.read())

print("Image copied successfully.")
