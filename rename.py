import os

path = "C:/Users/Grim/Desktop/Aria on Insta/poze"


# Function to rename multiple files
def RenameFiles():
    i = 0

    for filename in os.listdir(path):
        dst = "poza_" + str(i) + ".jpg"
        src = 'C:/Users/Grim/Desktop/Aria on Insta/poze/' + filename
        dst = 'C:/Users/Grim/Desktop/Aria on Insta/poze_final/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    RenameFiles()
