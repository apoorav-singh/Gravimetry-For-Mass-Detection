# This driver file is for Windows only 
# Replace the existing system('python file.py') file with system(python3 file.py)  

from os import *

# Removing older files
print("\n")

print("All your older data would be removed. Do you wish to continue?\n")

in_choice = input("(y/n): ")

if (in_choice == "y"):
    print("\n")
    print("Deleting older data files...")
    try: 
        remove("valz.npy")
        print("File valz.npy removed")

    except:
        print("file(s) not found")
        pass

    try: 
        remove("xx.npy")
        print("File xx.npy removed")

    except:
        print("file(s) not found")
        pass

    try: 
        remove("yy.npy")
        print("File yy.npy removed")

    except:
        print("file(s) not found")
        pass

    try:
        remove("k_xx.npy")
        print("File k_xx.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("k_yy.npy")
        print("File k_yy.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("k_z.npy")
        print("File k_z.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("mod_k.npy")
        print("File mod_k.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("fft_valz.npy")
        print("File fft_valz.npy removed")

    except:
        print("file(s) not found")
        pass

    try:
        print("\n")
        print("Generating Terrain value")
        
        in_pr = input("Enter 1 for prism and 0 for irregular surface: ")

        if (in_pr == "0"):
            system(r'python python_files/irregualar_prism.py')
        elif(in_pr == "1"):
            system(r'python python_files/single_prism.py')
        else:
            print("Wrong Choice. Program Terminated")
            exit()        

    except:
        print("Error: irregular_prism.py not found!")

    try:
        print("\n")
        system(r'python python_files/ggt1.py')
        

    except:
        print("Error: ggt1.py not found!")

    try:
        print("\n")
        print("Evaluating FFT")
        system(r'python python_files/fft_g.py')

    except:
        print("Error: fft_g.py not found!")       
        
else:
    print("Program Terminated1")

in_val = input("Do you wish to clean the data files generated (y/n): ")

if (in_val == "y"):
    print("\n")
    print("Deleting older data files...")
    try: 
        remove("valz.npy")
        print("File valz.npy removed")

    except:
        print("file(s) not found")
        pass

    try:
        remove("k_xx.npy")
        print("File k_xx.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("k_yy.npy")
        print("File k_yy.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("k_z.npy")
        print("File k_z.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("mod_k.npy")
        print("File mod_k.npy removed")

    except:
        print("file(s) not found")
        pass   

    try:
        remove("fft_valz.npy")
        print("File fft_valz.npy removed")

    except:
        print("file(s) not found")
        pass

    try: 
        remove("xx.npy")
        print("File xx.npy removed")

    except:
        print("file(s) not found")
        pass

    try: 
        remove("yy.npy")
        print("File yy.npy removed")
        print("\n")

    except:
        print("file(s) not found")
        print("\n")
        pass

else:
    print("\n")
    print("Program successfully executed.")   