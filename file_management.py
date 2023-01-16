import os 
import glob
import shutil



# -------------------------------------------------------------------------------------------------------------------------------------------------
# Capturing Date and time
# -------------------------------------------------------------------------------------------------------------------------------------------------

import time
date_v = time.strftime("%d_%m_%Y")
def time_v(): return time.strftime("%H_%M_%S")

# -------------------------------------------------------------------------------------------------------------------------------------------------
# Folder and Path Management
# -------------------------------------------------------------------------------------------------------------------------------------------------
path_og = os.getcwd()

def latest_file(path_aft):
    list_of_files = glob.glob(os.getcwd()+"/"+path_aft+"/*") # * means all 
    if (list_of_files == None):
        return []
    else:
        return max(list_of_files, key=os.path.getctime)


# ------------------------------------------------------    
def file_gen(depth, graph_save):
    file_found = 0
    # print("Current Working Directory: ", os.getcwd())
    
    
    os.chdir("Data")
    dir_list = os.listdir()
    # print("Current Working Directory: ", os.getcwd())
    if (len(dir_list) == 0):
        os.mkdir(date_v)
    else:
        for i in dir_list:
            if (i == date_v):
                file_found = 1
                # print("T")
                break
            
            else:
                print("Directory not found")
            
    
        if (file_found == 0):
            print("Files was not found")
            os.mkdir(date_v)
            print("Files were created")
    
    file_found = 0
    os.chdir(date_v)
    
    # print("Current Working Directory: ", os.getcwd())
    dir_list = os.listdir()
    if (len(dir_list) == 0):
        os.mkdir("z_"+str(depth))
    else:
        for i in dir_list:
            if (i == "z_"+str(depth)):
                file_found = 1
                break
            
            else:
                print("Directory not found")
            
    
        if (file_found == 0):
            print("Files was not found")
            os.mkdir("z_"+str(depth))
            print("Files were created")
        
    file_found = 0

    os.chdir("..")
    os.chdir("..")
    
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = "Data" + "/" + date_v + "/" + "z_"+str(depth) + "/" + graph_save + '.svg'
     
    # "Data" + date_v + "/" + "z_"+str(depth) + "/" + 
    
    # print("Current Working Directory: ", os.getcwd())

    return image_format, image_name