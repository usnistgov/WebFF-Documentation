#Importing libraries and modules
import xml.etree.ElementTree as ET
import sys                                # Python standard library
import WebFF as FF                        # Webff module
#Calls functions from the webff.py module to translate XML data into the .params format
def xml_params(input, output): 
    #parses the XML tree and establishes the root
    tree = ET.parse(input)
    root = tree.getroot() 
    #Open the output file
    f = open(output, 'w+') 
    #creates a  list of all top level elements (potential types)
    top_elements= (root.findall("*"))
    tags_elements = []
    for ele in top_elements:
        tags_elements.append(ele.tag)
    f.write("* "+str((root.find("./Force-Field-Header/Force-Field-Name")).text)+"\n")
    #If the potential style is present calls the appropriate webff.py function on it
	#Non Bond Potentials
    if "NonBondPotential" in tags_elements:
        if root.find("NonBondPotential/*").tag == "NonBond-LJ-Rmin": 
            FF.XMLToParamsNonBondPotential_LJ_Rmin(root, f)
        if root.find("NonBondPotential/*").tag == "NonBond-LJ": 
            FF.XMLToParamsNonBondPotential_LJ(root, f)
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
	#Dihedral Potentials
    if "DihedralPotential" in tags_elements:
        if root.find("DihedralPotential/*").tag == "DihedralPotential-CHARMM": 
            FF.XMLToParamsDihedralPotential_CHARMM(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-FourierSimple": 
            FF.XMLToParamsDihedralPotential_FourierSimple(root, f)
	#Improper Potentials
    if "ImproperPotential" in tags_elements:
        if root.find("ImproperPotential/*").tag == "ImproperPotential-Harmonic":
            FF.XMLToParamsImproperPotential_Harmonic(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CHARMM":
            FF.XMLToParamsImproperPotential_CHARMM(root, f)
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
    input = str((sys.argv[1]))
    output = str((sys.argv[2]))
    xml_params(input, output)
