#!/usr/bin/python

# Import the necessary modules
import pandas as pd
import xlrd
import os
import csv
import sys
import subprocess
from getpass import getpass
from jinja2 import Template



def GenerateConfigurationFile(filename, ConfigTemplateFilePath, ConfigOutputFolder ):

    current_folder_path, current_folder_name = os.path.split(os.getcwd())
    
    configOut_path =  ConfigOutputFolder     
    
    try:
        wb= pd.read_excel(filename)
        csv_as_string = wb.to_csv(index=False)
    except Exception as err:
        print("Error while reading Excel File. \n{}".format(err))

    device_data = csv.DictReader(csv_as_string.splitlines() )
     
    #csv_file = filename
    #device_data = csv.DictReader(open(csv_file))
    
    ConfigFiles = []

    for row in device_data:
        data = row

        #conffilename = configOut_path + "/" + row["store_number"] + ".conf"
        conffilename = configOut_path + "/" + row["Device_Name"] + ".json"
        ConfigFiles.append(conffilename)

        print('conffilename: ', conffilename)
        print('ConfigTemplateFilePath:', ConfigTemplateFilePath)
        print('filename: ', filename)
        
        with open(config_template_path + config_template_filename) as t_fh:
        #with open(ConfigTemplateFilePath) as t_fh:

            t_format = t_fh.read()

        template = Template(t_format)

        fout = open(conffilename, 'w')

        fout.write((template.render(data)))
        fout.close()

    return ConfigFiles