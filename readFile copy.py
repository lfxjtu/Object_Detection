# path = "/Users/lfxjtu/Dropbox/Fang Liu/Python/"
# Fully automated script to read all coordinates of the rectangles. Each rectangle is a bounding box for an object.
# Multiple bounding boxes can exist in an image
# Scripts reads all images of the data-set through cars.txt

from shutil import copyfile
file0 = "cars.txt"
file1 = "cars_copy.txt"
copyfile(file0, file1)

with open(file1) as f:
    all_coords = f.read()
    # print("here's the first line:")
    #    print(all_coords)
    image_info = all_coords.split("=")
    #    print(image_info)
    n = len(image_info)
    print("there are " + str(n) + " images")
    # print("The number of images are: ", n-1)
    # It returns one greater than the number of images because of an additional = at the end
    #    n = n-1
    for i in range(0, n-1):
        # temp = i+1
        # print(i)
        output_s = "Image number " + str(i + 1)
        print (output_s)
        first_image = image_info[i]
        # we are going to use a loop here to replace 0 with i, where i would start from 0 and end at n-1
        box_info = first_image.split(":")

        b = len(box_info)
        print("The number of boxes in this image is: " + str(b - 1))
        for j in range(0, b - 1):
            first_box = box_info[j]
            box_coord = first_box.split(",")
            #            print("box coodinates are:" + str(box_coord))

            output = "Top left = (" + box_coord[0] + ", " + box_coord[1] + "). Bottom right = (" + box_coord[2] + ", " + box_coord[3] + ")"
            print("Box " + str(j+1) + ":")
            print (output)
    # print(split_txt)
    # print(split_txt[0])
