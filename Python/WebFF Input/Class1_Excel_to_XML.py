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
    root = ET.Element("FF-Class-I") 
    
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
        
    #Atom Types
    if  "AtomType-ATDL" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-ATDL")
        FF.ReadExcelAtomTypes_ATDL(sheet, root)
    if  "AtomType-DFF" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-DFF")
        FF.ReadExcelAtomTypes_DFF(sheet, root)
	if  "RelationTree-DFF" in sheet_names:
	    sheet = xls_file.sheet_by_name("RelationTree-DFF")
            FF.ReadExcelRelationTree_DFF(sheet, root)
    if  "AtomType-Generic" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-Generic")
        FF.ReadExcelAtomTypes_Generic(sheet, root)
    if  "Atom-Attributes-DFF" in sheet_names: 
        sheet = xls_file.sheet_by_name("Atom-Attributes-DFF")
        FF.ReadExcelAtomTypeAttributes_DFF(sheet, root)
    if  "Atom-Attributes-Generic" in sheet_names: 
        sheet = xls_file.sheet_by_name("Atom-Attributes-Generic")
        FF.ReadExcelAtomTypeAttributes_Generic(sheet, root)
    
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
        FF.ReadExcelAnglePotential_COS2(sheet, sub_root)
    if  "AnglePotential-CHARMM" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-CHARMM")
        FF.ReadExcelAnglePotential_CHARMM(sheet, sub_root) 


    #Dihedral Potentials    
    
    if  "DihedralPotential-CHARMM" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-CHARMM")
        FF.ReadExcelDihedralPotential_CHARMM(sheet, sub_root) 
    if  "DihedralPotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Harmonic")
        FF.ReadExcelDihedralPotential_Harmonic(sheet, sub_root) 
    if  "DihedralPotential-Quadratic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Quadratic")
        FF.ReadExcelDihedralPotential_Quadratic(sheet, sub_root) 
    if  "DihedralPotential-OPLS" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-OPLS")
        FF.ReadExcelDihedralPotential_OPLS(sheet, sub_root)  
    if "DihedralPotential-FourierSimple" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-FourierSimple")
        FF.ReadExcelDihedralPotential_FourierSimple(sheet, sub_root) 
    if "DihedralPotential-Fourier" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Fourier")
        FF.ReadExcelDihedralPotential_Fourier(sheet, sub_root)  
    if "DihedralPotential-Multiharmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Multiharmonic")
        FF.ReadExcelDihedralPotential_Multiharmonic(sheet, sub_root) 

    # Improper Potentials
    
    if "ImproperPotential-CVFF" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-CVFF")
        FF.ReadExcelImproperPotential_CVFF(sheet, sub_root) 
    if  "ImproperPotential-COS2" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-COS2")
        FF.ReadExcelImproperPotential_COS2(sheet, sub_root) 
    if  "ImproperPotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Harmonic")
        FF.ReadExcelImproperPotential_Harmonic(sheet, sub_root) 
    if  "ImproperPotential-Fourier" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Fourier")
        FF.ReadExcelImproperPotential_Fourier(sheet, sub_root) 
    if  "ImproperPotential-Umbrella" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Umbrella")
        FF.ReadExcelImproperPotential_Umbrella(sheet, sub_root)  
    if  "ImproperPotential-CHARMM" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-CHARMM")
        FF.ReadExcelImproperPotential_CHARMM(sheet, sub_root) 

    #Non Bonded Potentials
    
    if  "NonBondPotential-LJ" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ")
        FF.ReadExcelNonBondPotential_LJ(sheet, sub_root)  
    if  "NonBondPotential-LJ-Rmin" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ-Rmin")
        FF.ReadExcelNonBondPotential_LJRmin(sheet, sub_root)  
    if  "NonBondPotential-LJ-AB" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ-AB")
        FF.ReadExcelNonBondPotential_LJAB(sheet, sub_root)  
    if "NonBondPotential-LJ-96" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ-96")
        FF.ReadExcelNonBondPotential_LJ96(sheet, sub_root)
    if  "NonBondPotential-LJ2" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ2")
        FF.ReadExcelNonBondPotential_LJ2(sheet, sub_root)  
        
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
        print("Usage: Class1_Excel_to_XML.py Excel_Input_File XML_Output_File")
        sys.exit()

# Check for Excel template file existence and proceed ... 
    if os.path.isfile(sys.argv[1]): 
        print("Execute file conversion")
        excel_xml(excel_file, xml_file)
    else: 
        print("Error: Specified Excel_Input_File does not exist")
        print("Usage: Class1_Excel_to_XML.py Excel_Input_File XML_Output_File")
        sys.exit()