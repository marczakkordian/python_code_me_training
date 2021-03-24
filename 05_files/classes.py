# # 1
# filename = 'text.txt'
# try :
#     with open(filename, 'r', encoding='utf8') as file :
#         content = file.readlines()
#         print(content)
# except FileNotFoundError :
#     print('Error -no such file')
# # 3
with open('save.txt', 'w') as f:
  f.write('Line 1\n')
  f.write('Line 2\n')
  f.write('Line 3\n')
  f.write('Line 4\n')