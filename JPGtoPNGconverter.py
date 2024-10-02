# my version works but the file name is a number
# import sys
# import os
# from PIL import Image
# from pathlib import Path


# # grab first and second argument
# first_element = sys.argv[1]
# second_element = sys.argv[2]
# print(first_element)
# print(second_element)
# # check is new/ exists, if not create
# p = Path('/Users/mickeyarnold/Desktop/Coding_Projects/scripting_python')
# first_path = p / first_element
# second_path = p / second_element
 

# print(first_path.exists())
# print(second_path.exists())

# if not second_path.exists():
#   Path.mkdir(second_element)

# # loop through Pokedex, then convert images to png
# count = 0

# for child in first_path.iterdir():
#   count+=1
#   print(str(child))
#   child_str = str(child)
#   if '.jpg' in child_str:
#     print(True)
#     img = Image.open(child_str) 

#     img.save(f"{second_path}/{count}.png")
    

# answer key
import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
    

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}/{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')
