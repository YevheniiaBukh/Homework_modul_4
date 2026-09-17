import colorama
import sys
import pathlib

colorama.init()

def name_directory(path):
    for item in path.iterdir():
        if item.is_dir():
            print(colorama.Fore.MAGENTA + f"folder: {item.name}" )
            name_directory(item)
        else:
            print(colorama.Fore.GREEN + f"file: {item.name}")



directory= sys.argv[1]
path = pathlib.Path(directory)
name_directory(path)