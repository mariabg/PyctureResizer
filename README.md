# PyctureResizer
This script makes a copy of every picture in the directory decreasing the image size. Several parameters can be apply to customize the output.

## Example
Run
```
  python pycture.py -o "2017_08_Barcelona" -r 4 -z 3 -s 96 -c png -t
```
or simply
```
  python pycture.py
```

## Parameters
| **Value** | **Description** | **Char** | **Default** |
| :--- | :---: | :---: | :---: |
| outputName | Output filename | `-o` | Keep the filename, adding numeration to avoid override |
| reduction ratio | Image size is divided by this number | `-r` | 2 |
| zeroFill | Pads with 0 those output filenames that don't reach an specific length | `-z` | 0 |
| picNumber | Starting number to name the pictures | `-s` | 1 |
| file format converter | Converts photos the given format. Accepts ```jpeg```, ```jpg``` and ```png```| `-c` | Keep the same format |
| timer | Prints the execution time once all the pictures are resized | `-t` | - |
| help | Displays information about the code | `-h` | - |


## Disclaimer
This is what I am currently using to store those pictures that I want to keep but don't have great value. I am not an expert at all on image processing and I can't ensure that this is the right way to do it. I am more than welcome to receive feedback about it, cheers! 🙆🏽
