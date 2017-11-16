#Importing libraies and modules
import xml.etree.ElementTree as ET
import sys                                # Python standard library
import webff as FF                        # Webff module
#Calls functions from the webff.py module to translate XML data into the .frc format
def xml_frc(input, output): 
    #parses the XMl tree and establishes the root
    tree = ET.parse(input)
    root = tree.getroot() 
    #opens the output file
    f = open(output, 'w+') 
    f.write("!"+((root.find("./Force-Field-Header/Description")).text)+"\n\n" )
    f.write("#version	"+((root.find("./Force-Field-Header/Force-Field-Name")).text)+"\n\n")
    #creates a list of all top level (potential types) elements
    top_elements= (root.findall("*"))
    tags_elements = []
    for ele in top_elements:
        tags_elements.append(ele.tag)
    #Calls the appropratie webff.py function for each potential style present
    if "AtomTypes" in tags_elements: 
        FF.XMLtoFrcAtomTypes(root, f)
    if "EquivalenceTable" in tags_elements: 
        FF.XMLtoFrcEquivalenceTable(root, f)
    if "BondPotential" in tags_elements:
        if root.find("BondPotential/*").tag == "BondPotential-Harmonic": 
            FF.XMLtoFrcBondPotential_Harmonic(root, f)
    if "AnglePotential" in tags_elements:
        if root.find("AnglePotential/*").tag == "AnglePotential-Harmonic": 
            FF.XMLtoFrcAnglePotential_Harmonic(root, f)
    if "ImproperPotential" in tags_elements:
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CHARMM": 
            FF.XMLtoFrcImproperPotential_CHARMM(root, f)
    if "DihedralPotential" in tags_elements:
        if root.find("DihedralPotential/*").tag == "DihedralPotential-FourierSimple": 
            FF.XMLtoFrcDihedralPotential_FourierSimple(root, f)
    if "NonBondPotential" in tags_elements:
        if root.find("NonBondPotential/*").tag == "NonBond-LJ": 
            FF.XMLtoFrcNonBond_LJ(root, f)
    if "BondIncrements" in tags_elements: 
        FF.XMLtoFrcBondIncrements(root, f)
    #closes the output file
    f.close()
#Allows this script to be called form the command line with input variables
if __name__ == "__main__":
    input = str((sys.argv[1]))
    output = str((sys.argv[2]))
    xml_frc(input, output)
