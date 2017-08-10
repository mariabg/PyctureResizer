#!/usr/bin/env python
from PIL import Image
from datetime import datetime
import os, sys, getopt

def main(argv):
    # Default parameter values
    outputName = ''
    reduction = 2
    zeroFill = 0
    picNumber = 1
    directory = os.getcwd()
    timer = False

    # Get customized parameters
    try:
        opts, args = getopt.getopt(argv, 'hto:r:z:s:p:')
    except getopt.GetoptError as err:
        # Warn about unrecognized parameters and exit
        print ("Ops... " + str(err))
        print "Run 'pycture.py -h' for help"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("# .====================================================.\n# |     value       |    char    |      default        |\n# |-----------------|------------|---------------------|\n# |    outputName   |     -o     |   keep filename     |\n# | reduction ratio |     -r     |         2           |\n# |     zeroFill    |     -z     |         0           |\n# |    picNumber    |     -s     |         1           |\n# |   path to sort  |     -p     |     working dir     |\n# |      timer      |     -t     |         -           |\n# |      help       |     -h     |         -           |\n# .====================================================/\n\n# Checkout the README for further information: https://github.com/mariabg/PyctureResizer")
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
        elif opt == '-p':
            if os.path.isdir(arg):
                directory = arg
            else:
                print("Ops! You entered a wrong path")
                sys.exit(2)
    if (timer):
        initTime = datetime.now()

    # picture resize
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpeg', '.jpg')):
            img = Image.open(filename)
            x = img.size[0]/reduction
            y = img.size[1]/reduction
            newImg = img.resize((x, y), Image.ANTIALIAS)
            # rename or keep the filename
            if outputName == '':
                # remove extension from filename
                name = filename.split('.')[0]
                out = name + "_" + str(picNumber).zfill(zeroFill)
            else:
                out = outputName + "_" + str(picNumber).zfill(zeroFill)
            newImg.save(out + ".JPEG")
            picNumber += 1

    print "Successful picture resize."
    if (timer):
        endTime = datetime.now()
        execTime = endTime - initTime
        print("Conversion time was " + str(execTime))

if __name__ == '__main__':
    main(sys.argv[1:])
