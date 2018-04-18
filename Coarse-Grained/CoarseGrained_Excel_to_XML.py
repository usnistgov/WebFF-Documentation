#Import Statements
import glob, os                           # Python standard library
import sys                                # Python standard library
# -------------------------------------------- convert .XLSX to .XML files
import xlrd                               # NEED to be installed
# -------------------------------------------- API
import requests                           # NEED to be installed
import webff as FF                        #webff python module (needs to be installed)
import xml.etree.ElementTree as ET        #Python standard library
def excel_xml(input, output): 
    # Read in file 
    excel_file_path = (input)
    xls_file = xlrd.open_workbook(excel_file_path)

    # Build in package


    # Specify the path to store the xml file (need to be changed if to create new document)
    output_file_path = (output)

    # Create the file root
    root = ET.Element("FF-CoarseGrained") 
    
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
        
    #Atom Types
    if  "AtomType-ATDL" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-ATDL")
        FF.ReadExcelAtomTypes_ATDL(sheet, root)
    if  "AtomType-CoarseGrained" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-CoarseGrained")
        FF.ReadExcelAtomTypes_CoarseGrained(sheet, root)   
	
    #Bond Potentials 
    if "BondPotential-Tabular" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-Tabular")
        FF.ReadExcelBondPotential_Tabular(sheet,sub_root) 
        
    #Angle Potentials
    if  "AnglePotential-Tabular" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-Tabular")
        FF.ReadExcelAnglePotential_Tabular(sheet,sub_root) 

    #Dihedral Potentials    
    if  "DihedralPotential-Tabular" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Tabular")
        FF.ReadExcelDihedralPotential_Tabular(sheet, sub_root) 
		
    #Non Bonded Potentials 
    if "NonBondPotential-Tabular" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-Tabular")
        FF.ReadExcelNonBondPotential_Tabular(sheet, sub_root)
	
    #Other information     
    if  "BondIncrements" in sheet_names: 
        sub_root = ET.SubElement(root, "BondIncrementTable")
        sheet = xls_file.sheet_by_name("BondIncrements")
        FF.ReadExcelBondIncrements(sheet, sub_root)   
    if  "EquivalenceTable" in sheet_names: 
        sub_root = ET.SubElement(root, "EquivalenceTable")
        sheet = xls_file.sheet_by_name("EquivalenceTable")
        FF.ReadExcelEquivalenceTable(sheet, sub_root)  
    if  "AutoEquivalenceTable" in sheet_names: 
        sub_root = ET.SubElement(root, "AutoEquivalenceTable")
        sheet = xls_file.sheet_by_name("AutoEquivalenceTable")
        FF.ReadExcelAutoEquivalenceTable(sheet, sub_root)  
    # Create a ElementTree, which is the structure corresponding to the Xml Document
    tree = ET.ElementTree(root)

    # Write it out
    tree.write(output_file_path)
    
if __name__ == "__main__":
    input = str((sys.argv[1]))
    output = str((sys.argv[2]))
    excel_xml(input, output)
