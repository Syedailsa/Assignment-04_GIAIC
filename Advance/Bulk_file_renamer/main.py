import os

def main():
    i = 0
    path = "C:/Users/A.K Com/OneDrive/Pictures/New folder/"

    for filename in os.listdir(path): # os.listdir() lists files in 
                                      # a directory

        #Creates a new file name 
        my_dest = 'img' + str(i) + '.jpg'

        #combines original folder path and its filename
        my_source = path + filename
        #combines folder path with its new filename
        my_dest = path + my_dest

        #os.rename() renames files.
        os.rename(my_source, my_dest)

        #update i for unique name of each file
        i += 1

main()

