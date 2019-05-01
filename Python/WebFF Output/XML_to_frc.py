#Importing libraries and modules
import xml.etree.ElementTree as ET
import glob, os                           # Python standard library
import sys                                # Python standard library
import WebFF as FF                        # Webff module
#Calls functions from the webff.py module to translate XML data into the .frc format
def xml_frc(input, output): 
    #parses the XMl tree and establishes the root
    tree = ET.parse(input)
    root = tree.getroot()
    #opens the output file
    f = open(output + '.frc', 'w+') 
    f.write("!"+str((root.find("./Force-Field-Header/Description")).text)+"\n\n" )
    f.write("#version	"+str((root.find("./Force-Field-Header/Force-Field-Name")).text)+"\n\n")   
	#creates a list of all top level (potential types) elements
    top_elements= (root.findall("*"))
    tags_elements = []
    for ele in top_elements:
        tags_elements.append(ele.tag)
    #Calls the appropriate webff.py function for each potential style present	
	#Atom Types
    if "AtomTypes" in tags_elements: 
        FF.XMLtoFrcAtomTypes(root, f)
	#Equivalence Tables
    if "EquivalenceTable" in tags_elements: 
        FF.XMLtoFrcEquivalenceTable(root, f)
	#Bond Potentials
    if "BondPotential" in tags_elements:
        if root.find("BondPotential/*").tag == "BondPotential-Harmonic": 
            FF.XMLtoFrcBondPotential_Harmonic(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Morse": 
            FF.XMLtoFrcBondPotential_Morse(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Class2": 
            FF.XMLtoFrcBondPotential_Class2(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-FENE": 
            FF.XMLtoFrcBondPotential_FENE(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Tabular": 
            FF.XMLToTableBondPotential_Tabular(root, f)
	#Angle Potentials
    if "AnglePotential" in tags_elements:
        if root.find("AnglePotential/*").tag == "AnglePotential-Harmonic": 
            FF.XMLtoFrcAnglePotential_Harmonic(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-COS2": 
            FF.XMLtoFrcAnglePotential_COS2(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-Cosine": 
            FF.XMLtoFrcAnglePotential_Cosine(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-CHARMM": 
            FF.XMLtoFrcAnglePotential_CHARMM(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-Class2": 
            FF.XMLtoFrcAnglePotential_Class2(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-Tabular": 
            FF.XMLToTableAnglePotential_Tabular(root, f)
			
	#Improper Potentials
    if "ImproperPotential" in tags_elements:
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CHARMM": 
            FF.XMLtoFrcImproperPotential_CHARMM(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-FourierSimple": 
            FF.XMLtoFrcImproperPotential_FourierSimple(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Class2": 
            FF.XMLtoFrcImproperPotential_Class2(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-COS2": 
            FF.XMLtoFrcImproperPotential_COS2(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CVFF": 
            FF.XMLtoFrcImproperPotential_CVFF(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Fourier": 
            FF.XMLtoFrcImproperPotential_Fourier(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Harmonic": 
            FF.XMLtoFrcImproperPotential_Harmonic(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Umbrella": 
            FF.XMLtoFrcImproperPotential_Umbrella(root, f)
	#Dihedral Potentials
    if "DihedralPotential" in tags_elements:
        if root.find("DihedralPotential/*").tag == "DihedralPotential-FourierSimple": 
            FF.XMLtoFrcDihedralPotential_FourierSimple(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Fourier": 
            FF.XMLtoFrcDihedralPotential_Fourier(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-CHARMM": 
            FF.XMLtoFrcDihedralPotential_CHARMM(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Harmonic": 
            FF.XMLtoFrcDihedralPotential_Harmonic(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Class2": 
            FF.XMLtoFrcDihedralPotential_Class2(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-OPLS": 
            FF.XMLtoFrcDihedralPotential_OPLS(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Quadratic": 
            FF.XMLtoFrcDihedralPotential_Quadratic(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Tabular": 
            FF.XMLToTableDihedralPotential_Tabular(root, f)
	#Non Bonded Potentials
    if "NonBondPotential" in tags_elements:
        if root.find("NonBondPotential/*").tag == "NonBond-LJ": 
            FF.XMLtoFrcNonBond_LJ(root, f)
        if root.find("NonBondPotential/*").tag == "NonBond-LJ-Rmin": 
            FF.XMLToFrcNonBondPotential_LJ_Rmin(root, f)
    if "BondIncrements" in tags_elements: 
        FF.XMLtoFrcBondIncrements(root, f)
    for ele in root.findall("./Force-Field-Header/Attachment"):
	if ele.tag == "Attachment":
	    FF.download(ele.find("./Reference").text)
    #closes the output file
    f.close()

#Allows this script to be called form the command line with input variables

if __name__ == "__main__":
# Usage: XML_to_frc.py
#
# Argument #1: XML file output from WebFF
# Argument #2: File name for converted output 
#
# Synopsis: The script reads force-field data in XML format and produces two
# output files. FF_NAME.frc contains the FF parameters and FF_NAME.tem 
# contains the atom types.
#
# Find argc size ... 
    argc = len(sys.argv)

# Test argc value ... 
    if argc == 3: 
        xml_file = str((sys.argv[1]))
        ff_filestring = str((sys.argv[2]))
    else:
        print("Usage: XML_to_frc.py FF_File.xml FF_NAME")
        sys.exit()

# Check for XML file existence and proceed ... 
    if os.path.isfile(sys.argv[1]): 
        print("Execute file conversion")
        xml_frc(xml_file, ff_filestring)
    else: 
        print("Error: Specified XML File does not exist")
        print("Usage: XML_to_frc.py FF_File.xml FF_NAME")
        sys.exit()