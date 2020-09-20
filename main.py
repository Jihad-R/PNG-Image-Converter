import os
from PIL import Image,ImageOps

print('-'*40)
print('\t\tPNG IMAGE CONVERTER\t\t')
print('-'*40+'\n')

# Get the name of the input and output folder
input_folder = input('Enter the Input folder name: ')
output_folder = input('Enter the Output folder name: ')

# Concatenate the inputed names with a '/'
infolder = input_folder + '/'
outfolder = output_folder + '/'

# a function used in producing the sepia palette/ filter
def make_linear_ramp(white):
    # putpalette expects [r,g,b,r,g,b,...]
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((int(r*i/255), int(g*i/255), int(b*i/255)))
    return ramp

# calling the above function and assigning it to sepia
sepia = make_linear_ramp((255, 240, 192))

#if the output folder doesn't exist create a new folder using the .makedirs method from the os module
if(not os.path.exists(outfolder)):
    os.makedirs(outfolder)
#function used to load the images
def Imgopening(infolder,outfolder):
    img = Image.open(f'{infolder}{filenames}')
    return img

#ask if the user wants to add a filter before converting the Images to PNG
ans = input('Do you want to add filters? Yes or No: ')

if(ans.lower() == 'yes'):
    filters = input("Please select a filter \n a-Sepia b-Invert c-GreyScale \n---------------\n ")
    if(filters.lower() == 'sepia' or filters.lower()=='a'):
        # a for loop to iterate with in each file in the input folder
        for filenames in os.listdir(infolder):
            #function invoking/calling
            img = Imgopening(infolder, outfolder)
            if img.mode != "L":
                img = img.convert("L")
            img = ImageOps.autocontrast(img)
            img.putpalette(sepia)
            img = img.convert("RGB")
            #split the filename to extract the filename without the file extension
            clean = os.path.splitext(filenames)[0]
            #saving image after adding the filter in the output folder specified earilier
            img.save(f'{outfolder}{clean}.png', 'png')
    elif(filters.lower() == 'invert' or filters.lower() == 'b'):
        for filenames in os.listdir(infolder):
            img = Imgopening(infolder, outfolder).convert("RGB")
            img = ImageOps.invert(img)
            img = img.convert("RGB")
            #split the filename to extract the filename without the file extension
            clean = os.path.splitext(filenames)[0]
            #saving image after adding the filter in the output folder specified earilier
            img.save(f'{outfolder}{clean}.png', 'png')
    elif(filters.lower() == 'greyscale' or filters.lower() =='c'):
        for filenames in os.listdir(infolder):
            img = Imgopening(infolder, outfolder).convert('LA')
            #split the filename to extract the filename without the file extension
            clean = os.path.splitext(filenames)[0]
            #saving image after adding the filter in the output folder specified earilier
            img.save(f'{outfolder}{clean}.png', 'png')

else:
    for filenames in os.listdir(infolder):
        # function invoking/calling
        img = Imgopening(infolder, outfolder)
        # split the filename to extract the filename without the file extension
        clean = os.path.splitext(filenames)[0]
        # saving image after adding the filter in the output folder specified earilier
        img.save(f'{outfolder}{clean}.png', 'png')
