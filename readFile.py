# path = "/Users/lfxjtu/Dropbox/Fang Liu/Python/"
# Fully automated script to read all co-ordinates of the rectangles. Each rectangle is a bounding box for an object.
# Multiple bounding boxes can exist in an image
# Scripts reads all images of the data-set through cars.txt
# import copy
# from shutil import copyfile
file1 = "cars.txt"
file1_copy = "cars_copy.txt"

# copyfile(file1, file1_copy)

# with open(file1_copy, "r") as f:
#    for line in f:
#        print line

with open(file1_copy, "a") as f1, open(file1, "r") as f:
    for each_line in f:
        each_line = each_line.replace("\n", "=").strip()
        f1.write(each_line)

with open(file1_copy) as f:
    all_coords = f.read()
    # print("here's the first line:")
    print(all_coords)
    image_info = all_coords.split("=")
    print("coordinate_info: " + str(image_info))
    # print(image_info)
    n = len(image_info)
    # print n
    # print("The number of images are: ", n-1) #It returns one greater than the number of images because of an
    # additional = at the end
    # n = n - 1
    for i in range(0, n-1):
        temp = i + 1
        print("Image number " + str(temp))
        first_image = image_info[i]
        # we are going to use a loop here to replace 0 with i, where i would start from 0 and end at n-1
        box_info = first_image.split(":")

        b = len(box_info)
        # print("The number of boxes in the first_image is: ", b) #

        for j in range(0, b):
            first_box = box_info[j]
            box_coord = first_box.split(",")
            print box_coord
            output = "Top left = (" + box_coord[0] + ", " + box_coord[1] + "). Bottom right = (" + box_coord[2] + ", " + box_coord[3] + ")"
            print (output)

    # print(split_txt)
    # print(split_txt[0])
