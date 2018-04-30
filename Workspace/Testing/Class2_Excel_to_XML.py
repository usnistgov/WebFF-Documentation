#Import Statements
import glob, os                           # Python standard library
import sys                                # Python standard library
# -------------------------------------------- convert .XLSX to .XML files
import xlrd                               # NEED to be installed
# -------------------------------------------- API
import requests                           # NEED to be installed
import WebFF as FF                        #webff python module (needs to be installed)
import xml.etree.ElementTree as ET        #Python standard library
def excel_xml(input, output): 
    # Read in file 
    excel_file_path = (input)
    xls_file = xlrd.open_workbook(excel_file_path)

    # Build in package


    # Specify the path to store the xml file (need to be changed if to create new document)
    output_file_path = (output)

    # Create the file root
    root = ET.Element("FF-Class2") 
    
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
    elif "BondPotential-Class2" in sheet_names:
        sub_root = ET.SubElement(root, "BondPotential")
        sheet = xls_file.sheet_by_name("BondPotential-Class2")
        FF.ReadExcelBondPotential_Class2(sheet,sub_root)
        
    #Angle Potentials
    if  "AnglePotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-Harmonic")
        FF.ReadExcelAnglePotential_Harmonic(sheet,sub_root) 
    elif  "AnglePotential-COS2" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-COS2")
        FF.ReadExcelAnglePotential_COS2(sheet, sub_root)
    elif  "AnglePotential-CHARMM" in sheet_names: 
        sub_root = ET.SubElement(root, "AnglePotential")
        sheet = xls_file.sheet_by_name("AnglePotential-CHARMM")
        FF.ReadExcelAnglePotential_CHARMM(sheet, sub_root)
    elif  "AnglePotential-Class2" in sheet_names: 
	sub_root = ET.SubElement(root, "AnglePotential")
	sheet = xls_file.sheet_by_name("AnglePotential-Class2")
	FF.ReadExcelAnglePotential_Class2(sheet, sub_root)

    #Dihedral Potentials    
    if  "DihedralPotential-CHARMM" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-CHARMM")
        FF.ReadExcelDihedralPotential_CHARMM(sheet, sub_root) 
    elif  "DihedralPotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Harmonic")
        FF.ReadExcelDihedralPotential_Harmonic(sheet, sub_root) 
    elif  "DihedralPotential-Quadratic" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Quadratic")
        FF.ReadExcelDihedralPotential_Quadratic(sheet, sub_root) 
    elif  "DihedralPotential-OPLS" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-OPLS")
        FF.ReadExcelDihedralPotential_OPLS(sheet, sub_root)  
    elif "DihedralPotential-FourierSimple" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-FourierSimple")
        FF.ReadExcelDihedralPotential_FourierSimple(sheet, sub_root)
    elif "DihedralPotential-Fourier" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Fourier")
        FF.ReadExcelDihedralPotential_Fourier(sheet, sub_root) 
    elif "DihedralPotential-Class2" in sheet_names: 
        sub_root = ET.SubElement(root, "DihedralPotential")
        sheet = xls_file.sheet_by_name("DihedralPotential-Class2")
        FF.ReadExcelDihedralPotential_Class2(sheet, sub_root) 


    # Improper Potentials 
    if "ImproperPotential-CVFF" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-CVFF")
        FF.ReadExcelImproperPotential_CVFF(sheet, sub_root) 
    elif  "ImproperPotential-COS2" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-COS2")
        FF.ReadExcelImproperPotential_COS2(sheet, sub_root) 
    elif  "ImproperPotential-Harmonic" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Harmonic")
        FF.ReadExcelImproperPotential_Harmonic(sheet, sub_root) 
    elif  "ImproperPotential-Fourier" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Fourier")
        FF.ReadExcelImproperPotential_Fourier(sheet, sub_root) 
    elif  "ImproperPotential-Umbrella" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Umbrella")
        FF.ReadExcelImproperPotential_Umbrella(sheet, sub_root)  
    elif  "ImproperPotential-CHARMM" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-CHARMM")
        FF.ReadExcelImproperPotential_CHARMM(sheet, sub_root) 
    elif  "ImproperPotential-Class2" in sheet_names: 
        sub_root = ET.SubElement(root, "ImproperPotential")
        sheet = xls_file.sheet_by_name("ImproperPotential-Class2")
        FF.ReadExcelImproperPotential_Class2(sheet, sub_root) 

	#Cross Potentials
    if "CrossPotential-BondBond" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-BondBond")
        FF.ReadExcelCrossPotential_BondBond(sheet, sub_root) 
    if  "CrossPotential-BondBond13" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-BondBond13")
        FF.ReadExcelCrossPotential_BondBond13(sheet, sub_root) 
    if  "CrossPotential-AngleAngle" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-AngleAngle")
        FF.ReadExcelCrossPotential_AngleAngle(sheet, sub_root) 
    if  "CrossPotential-BondAngle" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-BondAngle")
        FF.ReadExcelCrossPotential_BondAngle(sheet, sub_root) 
    if  "CrossPotential-MiddleBondTorsio" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-MiddleBondTorsio")
        FF.ReadExcelCrossPotential_MiddleBondTorsion(sheet, sub_root)  
    if  "CrossPotential-EndBondTorsion" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-EndBondTorsion")
        FF.ReadExcelCrossPotential_EndBondTorsion(sheet, sub_root) 
    if  "CrossPotential-AngleTorsion" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-AngleTorsion")
        FF.ReadExcelCrossPotential_AngleTorsion(sheet, sub_root)
    if  "CrossPotential-AngleAngleTorsio" in sheet_names: 
        sub_root = ET.SubElement(root, "CrossPotential")
        sheet = xls_file.sheet_by_name("CrossPotential-AngleAngleTorsio")
        FF.ReadExcelCrossPotential_AngleAngleTorsion(sheet, sub_root)
		
    #Non Bonded Potentials 
    if "NonBondPotential-Class2" in sheet_names: 
        sub_root = ET.SubElement(root, "NonBondPotential")
        sheet = xls_file.sheet_by_name("NonBondPotential-Class2")
        FF.ReadExcelNonBondPotential_LJClass2(sheet, sub_root)
	
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
