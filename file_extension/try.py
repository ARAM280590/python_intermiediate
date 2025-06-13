import os #working with file directories
import json #at the end make a json file 
from collections import defaultdict #in cases where there is a new key give 0 default value 

folder_path = os.getcwd() #executing on current working directory,however folder_path can be any directory

def extension_based_sort(folder_path):
    files_distribution = defaultdict(int) 

    for file in os.listdir(folder_path):
        _,ext = os.path.splitext(file)
        files_distribution[ext]+=1
    sorted_files_distribution = dict(sorted(files_distribution.items(),reverse=True))
    output_path = os.path.join(folder_path,'file_extension.json')
    with open(output_path,'w') as f:
        json.dump(files_distribution,f,indent=4)
extension_based_sort(folder_path)  

