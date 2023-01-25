from pathlib import Path

#p1 = Path('./file1.txt')
p1 = Path('./newfile.txt')
print(type(p1))

# if file doesn't exist, create file and write Content3
if not p1.exists():
  with open(p1, 'w') as file:
    #print(file.read())
    file.write('Content3')

# print full file name
print(p1.name)
# print without extension
print(p1.stem)
# print only extension
print(p1.suffix)

# print out items in path
p2 = Path('./')
print(p2.iterdir())
for item in p2.iterdir():
  print(item)
  #print(type(item))


#print(list(p2.iterdir()))
