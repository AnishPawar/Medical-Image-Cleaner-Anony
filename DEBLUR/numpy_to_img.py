import matplotlib

#use this function to save jpg file
def numpy_to_jpg(data, filename):
    img_name = filename +".jpg"
    matplotlib.image.imsave(img_name, data)
    print(filename + " was saved")
