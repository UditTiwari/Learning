myfile = open('Input_output_basic_files/myfile.txt', mode ='r')

# contents = myfile.read()
contents = myfile.readlines()

print(contents)

myfile.close()



