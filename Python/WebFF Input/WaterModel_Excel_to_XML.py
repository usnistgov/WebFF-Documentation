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
		
    #Atom Types
    if  "AtomType-ATDL" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-ATDL")
        FF.ReadExcelAtomTypes_ATDL(sheet, root)
    if  "AtomType-Generic" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-Generic")
        FF.ReadExcelAtomTypes_Generic(sheet, root)
		
    #Bond Potentials 
    if "BondPotential-Harmonic" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-Harmonic")
        FF.ReadExcelBondPotential_Harmonic(sheet,sub_root) 
    if "BondPotential-Morse" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-Morse")
        FF.ReadExcelBondPotential_Morse(sheet,sub_root)
		
    #Angle Potentials
    if  "AnglePotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-Harmonic")
        FF.ReadExcelAnglePotential_Harmonic(sheet,sub_root)
    if  "AnglePotential-COS2" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-COS2")
        FF.ReadExcelAnglePotential_COS2(sheet,sub_root)
		
    #Non Bonded Potentials
    if "NonBondPotential-LJ" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ")
        FF.ReadExcelNonBondPotential_LJ(sheet, sub_root)
    if "NonBondPotential-LJ2" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ2")
        FF.ReadExcelNonBondPotential_LJ2(sheet, sub_root)	
    if "NonBondPotential-LJ2-AB" in sheet_names: 
	    sub_root = ET.SubElement(root, "NonBondPotential")
	    sheet = xls_file.sheet_by_name("NonBondPotential-LJ2-AB")
		
    #Other information     
    if  "BondIncrements" in sheet_names: 
        sub_root = ET.SubElement(root, "BondIncrementTable")
        sheet = xls_file.sheet_by_name("BondIncrements")
        FF.ReadExcelBondIncrements(sheet, sub_root)

        
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

# Find argc size ... 
    argc = len(sys.argv)

# Test argc value ... 
    if argc == 3: 
        excel_file = str((sys.argv[1]))
        xml_file = str((sys.argv[2]))
    else:
        print("Usage: WaterModel_to_XML.py Excel_Input_File XML_Output_File")
        sys.exit()

# Check for Excel template file existence and proceed ... 
    if os.path.isfile(sys.argv[1]): 
        print("Execute file conversion")
        excel_xml(excel_file, xml_file)
    else: 
        print("Error: Specified Excel_Input_File does not exist")
        print("Usage: Class1_Excel_to_XML.py Excel_Input_File XML_Output_File")
        sys.exit()