import sys
import os

lines = 0
substring = "gosti-"

os.remove('parsedURL.txt')
for it in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
  filename = open('savedURL.txt',"r")
  for i,line in enumerate(filename):
    line = line.replace("\n", "")
    if i == it:
      if(line.count(substring) < 1):
        print(line)
        filetxt = open('parsedURL.txt', 'a')
        filetxt.write(line)
        filetxt.write('\n')
        filetxt.close()

  filename.close()



