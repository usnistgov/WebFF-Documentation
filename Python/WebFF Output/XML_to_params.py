#Importing libraries and modules
import xml.etree.ElementTree as ET
import glob, os                           # Python standard library
import sys                                # Python standard library
import WebFF as FF                        # Webff module
#Calls functions from the webff.py module to translate XML data into the .params format
def xml_params(input, output): 
    #parses the XML tree and establishes the root
    tree = ET.parse(input)
    root = tree.getroot() 
    #Open the output file
    f = open(output + '.params', 'w+') 
    #creates a  list of all top level elements (potential types)
    top_elements= (root.findall("*"))
    tags_elements = []
    for ele in top_elements:
        tags_elements.append(ele.tag)
    f.write("* "+str((root.find("./Force-Field-Header/Force-Field-Name")).text)+"\n")
    #If the potential style is present calls the appropriate webff.py function on it
	#Non Bond Potentials
    if "NonBondPotential" in tags_elements:
        if root.find("NonBondPotential/*").tag == "NonBondPotential-LJ-Rmin": 
            FF.XMLToParamsNonBondPotential_LJ_Rmin(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-LJ": 
            FF.XMLToParamsNonBondPotential_LJ(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-LJ2": 
            FF.XMLtoParamsNonBond_LJ2(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-LJ-AB": 
            FF.XMLtoParamsNonBondPotential_LJ_AB(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-LJ2-AB": 
            FF.XMLtoParamsNonBondPotential_LJ2_AB(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-Class2": 
            FF.XMLtoParamsNonBondPotential_Class2(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-EnergyRenorm": 
            FF.XMLtoParamsNonBondPotential_EnergyRenorm(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-Mie": 
            FF.XMLtoParamsNonBondPotential_Mie(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-Soft": 
            FF.XMLtoParamsNonBondPotential_Soft(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-Tabular": 
            FF.XMLtoTableNonBondPotential_Tabular(root, f)
        if root.find("NonBondPotential/*").tag == "NonBondPotential-Weeks-Chandler-Anderson": 
            FF.XMLtoParamsNonBondPotential_Weeks_Chandler_Anderson(root, f)
	#Bond Potentials
    if "BondPotential" in tags_elements:
        if root.find("BondPotential/*").tag == "BondPotential-Harmonic":
            FF.XMLToParamsBondPotential_Harmonic(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Morse":
            FF.XMLToParamsBondPotential_Morse(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Class2": 
            FF.XMLtoParamsBondPotential_Class2(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-FENE": 
            FF.XMLtoParamsBondPotential_FENE(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Tabular": 
            FF.XMLToTableBondPotential_Tabular(root, f)
	#Angle Potentials
    if "AnglePotential" in tags_elements:
        if root.find("AnglePotential/*").tag == "AnglePotential-Harmonic": 
            FF.XMLToParamsAnglePotential_Harmonic(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-COS2": 
            FF.XMLToParamsAnglePotential_COS2(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-Cosine": 
            FF.XMLtoParamsAnglePotential_Cosine(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-CHARMM": 
            FF.XMLtoParamsAnglePotential_CHARMM(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-Class2": 
            FF.XMLtoParamsAnglePotential_Class2(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-Tabular": 
            FF.XMLToTableAnglePotential_Tabular(root, f)
	#Dihedral Potentials
    if "DihedralPotential" in tags_elements:
        if root.find("DihedralPotential/*").tag == "DihedralPotential-CHARMM": 
            FF.XMLToParamsDihedralPotential_CHARMM(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-FourierSimple": 
            FF.XMLToParamsDihedralPotential_FourierSimple(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Fourier": 
            FF.XMLToParamsDihedralPotential_Fourier(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Harmonic": 
            FF.XMLToParamsDihedralPotential_Harmonic(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Class2": 
            FF.XMLToParamsDihedralPotential_Class2(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-OPLS": 
            FF.XMLToParamsDihedralPotential_OPLS(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Quadratic": 
            FF.XMLToParamsDihedralPotential_Quadratic(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-Tabular": 
            FF.XMLToTableDihedralPotential_Tabular(root, f)
	#Improper Potentials
    if "ImproperPotential" in tags_elements:
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Harmonic":
            FF.XMLToParamsImproperPotential_Harmonic(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CHARMM":
            FF.XMLToParamsImproperPotential_CHARMM(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Class2":
            FF.XMLToParamsImproperPotential_Class2(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-COS2":
            FF.XMLToParamsImproperPotential_COS2(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CVFF":
            FF.XMLToParamsImproperPotential_CVFF(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Fourier":
            FF.XMLToParamsImproperPotential_Fourier(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Umbrella":
            FF.XMLToParamsImproperPotential_Umbrella(root, f)
	#Cross Potentials
    if "CrossPotential" in tags_elements: 
        if root.find("CrossPotential/*").tag == "CrossPotential-BondBond":
           FF.XMLtoParamsCrossPotential_BondBond(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-BondBond13":
           FF.XMLtoParamsCrossPotential_BondBond13(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-AngleAngle":
           FF.XMLtoParamsCrossPotential_AngleAngle(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-BondAngle":
           FF.XMLtoParamsCrossPotential_BondAngle(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-MiddleBondTorsion":
           FF.XMLtoParamsCrossPotential_MiddleBondTorsion(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-EndBondTorsion":
           FF.XMLtoParamsCrossPotential_EndBondTorsion(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-AngleTorsion":
           FF.XMLtoParamsCrossPotential_AngleTorsion(root, f)
        if root.find("CrossPotential/*").tag == "CrossPotential-AngleAngleTorsion":
           FF.XMLtoParamsCrossPotential_AngleAngleTorsion(root, f)
	#Atom Types
    if "AtomTypes" in tags_elements: 
        FF.XMLToParamsAtomTypes(root, f)
    for ele in root.findall("./Force-Field-Header/Attachment"):
	if ele.tag == "Attachment":
	    FF.download(ele.find("./Reference").text)
    #closes the output file
    f.close()
#Allows this script to be called form the command line with input variables
if __name__ == "__main__":
# Usage: XML_to_params.py
#
# Argument #1: XML file output from WebFF
# Argument #2: File name for converted output 
#
# Synopsis: The script reads force-field data in XML format and produces two
# output files. FF_NAME.params contains the FF parameters and FF_NAME.tem 
# contains the atom types.
#
# Find argc size ... 
    argc = len(sys.argv)

# Test argc value ... 
    if argc == 3: 
        xml_file = str((sys.argv[1]))
        ff_filestring = str((sys.argv[2]))
    else:
        print("Usage: XML_to_params.py FF_File.xml FF_NAME")
        sys.exit()

# Check for XML file existence and proceed ... 
    if os.path.isfile(sys.argv[1]): 
        print("Execute file conversion")
        xml_params(xml_file, ff_filestring)
    else: 
        print("Error: Specified XML File does not exist")
        print("Usage: XML_to_params.py FF_File.xml FF_NAME")
        sys.exit()
