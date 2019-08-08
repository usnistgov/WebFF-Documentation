#Import Statements
import glob, os                           # Python standard library
import sys                                # Python standard library
# -------------------------------------------- convert .XLSX to .XML files
import xlrd                               # NEED to be installed
# -------------------------------------------- API
import requests                           # NEED to be installed
import WebFF as FF                        #webff python module (needs to be installed)
import xml.etree.ElementTree as ET        #Python standard library
import xml.dom.minidom as xdm             #Python standard library

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
    if "References" in sheet_names:
	    sheet = xls_file.sheet_by_name("References")
	    FF.ReadExcelMetaData_References(sheet,root)
        
    #Atom Types
    if  "AtomType-ATDL" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-ATDL")
        FF.ReadExcelAtomTypes_ATDL(sheet, root)
    if  "AtomType-CoarseGrained" in sheet_names: 
        sheet = xls_file.sheet_by_name("AtomType-CoarseGrained")
        FF.ReadExcelAtomTypes_CoarseGrained(sheet, root)   
	
    #Bond Potentials
    if "BondPotential-Harmonic" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-Harmonic")
        FF.ReadExcelBondPotential_Harmonic(sheet,sub_root)
    if "BondPotential-Tabular" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-Tabular")
        FF.ReadExcelBondPotential_Tabular(sheet,sub_root)
    if "BondPotential-FENE" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-FENE")
        FF.ReadExcelBondPotential_FENE(sheet,sub_root)
        
    #Angle Potentials
    if  "AnglePotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-Harmonic")
        FF.ReadExcelAnglePotential_Harmonic(sheet,sub_root)
    if  "AnglePotential-Cosine" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-Cosine")
        FF.ReadExcelAnglePotential_Cosine(sheet,sub_root)
    if  "AnglePotential-COS2" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-COS2")
        FF.ReadExcelAnglePotential_COS2(sheet,sub_root)
    if  "AnglePotential-Tabular" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-Tabular")
        FF.ReadExcelAnglePotential_Tabular(sheet,sub_root)

    #Dihedral Potentials
    if  "DihedralPotential-Quadratic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Quadratic")
        FF.ReadExcelDihedralPotential_Quadratic(sheet, sub_root)
    if  "DihedralPotential-Tabular" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Tabular")
        FF.ReadExcelDihedralPotential_Tabular(sheet, sub_root)
    if "DihedralPotential-Multiharmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Multiharmonic")
        FF.ReadExcelDihedralPotential_Multiharmonic(sheet, sub_root) 		
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
	    FF.ReadExcelNonBondPotential_LJ2AB(sheet, sub_root)	
    if "NonBondPotential-LJ96" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ96")
        FF.ReadExcelNonBondPotential_LJ96(sheet, sub_root)
    if "NonBondPotential-LJ962" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ962")
        FF.ReadExcelNonBondPotential_LJ962(sheet, sub_root)
    if "NonBondPotential-Tabular" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-Tabular")
        FF.ReadExcelNonBondPotential_Tabular(sheet, sub_root)
    if "NonBondPotential-WCA" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-WCA")
        FF.ReadExcelNonBondPotential_WCA(sheet, sub_root)
    if "NonBondPotential-Mie" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-Mie")
        FF.ReadExcelNonBondPotential_Mie(sheet, sub_root)
    if "NonBondPotential-EnergyRenorm" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-EnergyRenorm")
        FF.ReadExcelNonBondPotential_EnergyRenorm(sheet, sub_root)
    if "NonBondPotential-Soft" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-Soft")
        FF.ReadExcelNonBondPotential_Soft(sheet, sub_root)
    if "NonBondPotential-LJ-GROMACS" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-LJ-GROMACS")
        FF.ReadExcelNonBondPotential_LJGROMACS(sheet, sub_root)

    #Dissipative Potentials
    if "DissipativePotential-Langevin" in sheet_names: 
        sub_root = ET.SubElement(root, "DissipativePotential")
        sheet = xls_file.sheet_by_name("DissipativePotential-Langevin")
        FF.ReadExcelDissipativePotential_Langevin(sheet, sub_root)

    #Soft Potentials
    if "SoftPotential-DPD" in sheet_names:
        sub_root = ET.SubElement(root, "SoftPotential")
        sheet = xls_file.sheet_by_name("SoftPotential-DPD")
        FF.ReadExcelSoftPotential_DPD(sheet,sub_root)
    if "SoftPotential-SRP" in sheet_names:
        sub_root = ET.SubElement(root, "SoftPotential")
        sheet = xls_file.sheet_by_name("SoftPotential-SRP")
        FF.ReadExcelSoftPotential_SRP(sheet,sub_root)
	
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
        print("Usage: CoarseGrained_Excel_to_XML.py Excel_Input_File XML_Output_File")
        sys.exit()

# Check for Excel template file existence and proceed ... 
    if os.path.isfile(sys.argv[1]): 
        print("Execute file conversion")
        excel_xml(excel_file, xml_file)
    else: 
        print("Error: Specified Excel_Input_File does not exist")
        print("Usage: CoarseGrained_Excel_to_XML.py Excel_Input_File XML_Output_File")
        sys.exit()
