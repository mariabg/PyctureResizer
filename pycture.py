#!/usr/bin/env python
import os, sys, getopt, datetime
from PIL import Image, ImageFile

def main(argv):
    # Default parameter values
    outputName = cExtension = ''
    reduction = 2
    zeroFill = 0
    picNumber = 1
    directory = os.getcwd()
    timer = convert = False

    # Get customized parameters
    try:
        opts, args = getopt.getopt(argv, 'hto:r:z:s:c:')
    except getopt.GetoptError as err:
        # Warn about unrecognized parameters and exit
        print ("Ops... " + str(err))
        print "Run 'pycture.py -h' for help"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("# .====================================================.\n# |     value       |    char    |      default        |\n# |-----------------|------------|---------------------|\n# |    outputName   |     -o     |   keep filename     |\n# | reduction ratio |     -r     |         2           |\n# |     zeroFill    |     -z     |         0           |\n# |    picNumber    |     -s     |         1           |\n# |    converter    |     -c     | keep the same format|\n# |      timer      |     -t     |         -           |\n# |      help       |     -h     |         -           |\n# .====================================================/\n\n# Checkout the README for further information: https://github.com/mariabg/PyctureResizer")
            sys.exit(2)
        elif opt == '-t':
            timer = True
        elif opt == '-o':
            outputName = arg
        elif opt == '-r':
            reduction = int(arg)
        elif opt == '-z':
            zeroFill = int(arg)
        elif opt == '-s':
            picNumber = int(arg)
        elif opt == '-c':
            convert = True
            cExtension = arg
    if (timer):
        initTime = datetime.datetime.now()

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
            img = Image.open(filename)
            x = img.size[0]/reduction
            y = img.size[1]/reduction
            newImg = img.resize((x, y), Image.ANTIALIAS)

            # Avoid problems saving larger JPEG file with PIL and the optimize flag set
            ImageFile.MAXBLOCK = img.size[0] * img.size[1]

            if outputName == '':
                out = filename.split('.')[0] + "_" + str(picNumber).zfill(zeroFill)
            else:
                out = outputName + "_" + str(picNumber).zfill(zeroFill)
            if (convert == False):
                if filename.lower().endswith('.png'):
                    cExtension = 'png'
                elif filename.lower().endswith('.jpg'):
                    cExtension = 'jpg'
                else:
                    cExtension = 'jpeg'
            # quality option ignored for PNG files
            newImg.save(out + '.' + cExtension, quality=90, optimize=True)
            picNumber += 1

    print "Successful picture resize."
    if (timer):
        endTime = datetime.datetime.now()
        execTime = endTime - initTime
        print("Conversion time was " + str(execTime))

if __name__ == '__main__':
    main(sys.argv[1:])
