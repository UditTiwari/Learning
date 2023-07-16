#using this we dont need to take care about close()

#Read mode
with open("Input_output_basic_files/myfile.txt", mode="r") as my_new_file:
    contents = my_new_file.read()
    print(contents)
    
#Write mode
with open("Input_output_basic_files/myfile.txt", mode="w") as my_new_file:
    contents = my_new_file.read()
    print(contents)