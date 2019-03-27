#Import Statements
import glob, os                           # Python standard library
import sys                                # Python standard library
# -------------------------------------------- convert .XLSX to .XML files
import xlrd                               # NEED to be installed
# -------------------------------------------- API
import requests                           # NEED to be installed
import WebFF as FF                        #webff python module (needs to be installed)
import xml.etree.ElementTree as ET        #Python standard library
import xml.dom.minidom as xdm

def excel_xml(input, output): 
    # Read in file 
    excel_file_path = (input)
    xls_file = xlrd.open_workbook(excel_file_path)

    # Build in package


    # Specify the path to store the xml file (need to be changed if to create new document)
    output_file_path = (output)

    # Create the file root
    root = ET.Element("FF-WaterModels") 
    
    sheet_names = xls_file.sheet_names() 
    #Pick the Specified Potentials
    #Metadata
    sub_root = ET.SubElement(root, "Force-Field-Header")
    if  "Metadata" in sheet_names:
        sheet = xls_file.sheet_by_name("Metadata")
        FF.ReadExcelMetaData_Header(sheet,sub_root)
    if "Keywords" in sheet_names:
        sheet = xls_file.sheet_by_name("Keywords")
        FF.ReadExcelMetaData_Keywords(sheet,root)
    if "References" in sheet_names:
	    sheet = xls_file.sheet_by_name("References")
	    FF.ReadExcelMetaData_References(sheet,root)
        
    #Water Models 
    if "WaterModel-3Site-Rigid" in sheet_names:
        sub_root = ET.SubElement(root, "WaterModel")
        sheet = xls_file.sheet_by_name("WaterModel-3Site-Rigid")
        FF.ReadExcelWaterPotential_3Site(sheet,sub_root) 
    if "WaterModel-4Site-Rigid" in sheet_names:
        sub_root = ET.SubElement(root, "WaterModel")
        sheet = xls_file.sheet_by_name("WaterModel-4Site-Rigid")
        FF.ReadExcelWaterPotential_4Site(sheet,sub_root)
    if "WaterModel-5Site-Rigid" in sheet_names:
        sub_root = ET.SubElement(root, "WaterModel")
        sheet = xls_file.sheet_by_name("WaterModel-5Site-Rigid")
        FF.ReadExcelWaterPotential_5Site(sheet,sub_root)
        
    # Create a ElementTree, which is the structure corresponding to the Xml Document
    tree = ET.ElementTree(root)

    # Write it out
    tree.write(output_file_path)

    # Save into pretty print format
    xml = xdm.parse(output_file_path)
    with open(output_file_path, "w") as text_file:
	text_file.write(xml.toprettyxml().encode("UTF-8"))
	text_file.close()
    
if __name__ == "__main__":
    input = str((sys.argv[1]))
    output = str((sys.argv[2]))
    excel_xml(input, output)
