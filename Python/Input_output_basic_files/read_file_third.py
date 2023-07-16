with open("Input_output_basic_files/myfile_two.txt",mode="r") as f:
    print(f.read())
    

#using APPEND("A")
# with open("Input_output_basic_files/myfile_two.txt",mode="a") as f:
#     print(f.write("\nFOUR ON FOURTH"))


#What write do if the file is not present it will create one else overwrite existing one
with open("Input_output_basic_files/write_third.txt",mode="w") as f:
    print(f.write('I CREATED THIS FILE'))
