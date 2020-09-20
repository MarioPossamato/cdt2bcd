*Have you ever wanted to port a Super Mario Maker 1 course to Super Mario Maker 2, but didn't want to go through all the trouble of placing every single block, item, and enemy?  Well it's your lucky day!*

# cdt2bcd
An extremely unfinished, experimental tool that attempts to convert data from a Super Mario Maker 1 course file to Super Mario Maker 2 bcd format.  

WARNING: This will *NOT* work with porting Super Mario Maker 1 courses to Super Mario Maker 2 yet, as it's extremely early in it's development, and is nowhere near finished! It's mostly just for experimentation at this point, but I will be working to get this working fully!
Update 7/16/2020: I started to rewrite this script (to clean up code, add more comments, etc.), and while I was looking through an SMM1 example course that I was using, and apparently SMM1 doesn't have the same type of tile data that SMM2 courses use.  Unfortunately, this means that unless I figure out a fix, (or someone who knows more about stuff than I do offers to lend a hand), this project may in fact not ever work... :(

## Pre-Requisites
[cdt2bcd](https://github.com/MarioPossamato/cdt2bcd/archive/master.zip)  
[Python 3.7](https://www.python.org/downloads/release/python-370/)  

## Running cdt2bcd
```usage: python3 cdt2bcd.py <main_area_input> <sub_area_input> <flag> <bcd_output>```  
```flag -d: does not encrypt the output bcd before it has been written out```  
```flag -e: encrypts the output bcd before it has been written out```  

## Where do I get help/support?
[My Discord Server](https://discord.gg/8wx8uQF)

## Where can I discuss development of this app?
[My Discord Server](https://discord.gg/8wx8uQF)

## Who gets credit for this?
- Mario Possamato for cdt2bcd
