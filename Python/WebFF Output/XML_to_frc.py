#Importing libraries and modules
import xml.etree.ElementTree as ET
import sys                                # Python standard library
import WebFF as FF                        # Webff module
#Calls functions from the webff.py module to translate XML data into the .frc format
def xml_frc(input, output, AToutput): 
    #parses the XMl tree and establishes the root
    tree = ET.parse(input)
    root = tree.getroot()
    #opens the output file
    f = open(output, 'w+') 
    f.write("!"+str((root.find("./Force-Field-Header/Description")).text)+"\n\n" )
    f.write("#version	"+str((root.find("./Force-Field-Header/Force-Field-Name")).text)+"\n\n")
    A = open(AToutput, 'w+') 
    A.write("!"+str((root.find("./Force-Field-Header/Description")).text)+"\n\n" )
    A.write("#version	"+str((root.find("./Force-Field-Header/Force-Field-Name")).text)+"\n\n")
    #creates a list of all top level (potential types) elements
    top_elements= (root.findall("*"))
    tags_elements = []
    for ele in top_elements:
        tags_elements.append(ele.tag)
    #Calls the appropriate webff.py function for each potential style present
	#Atom Types
    if "AtomTypes" in tags_elements: 
        if root.find("AtomTypes/*").tag == "AtomType-CoarseGrained":
            FF.XMLtoFrcAtomTypesCG(root, A)
	#Equivalence Tables
    if "EquivalenceTable" in tags_elements: 
        FF.XMLtoFrcEquivalenceTable(root, f)
	#Bond Potentials
    if "BondPotential" in tags_elements:
        if root.find("BondPotential/*").tag == "BondPotential-Harmonic": 
            FF.XMLtoFrcBondPotential_Harmonic(root, f)
        if root.find("BondPotential/*").tag == "BondPotential-Morse": 
            FF.XMLtoFrcBondPotential_Morse(root, f)
	#Angle Potentials
    if "AnglePotential" in tags_elements:
        if root.find("AnglePotential/*").tag == "AnglePotential-Harmonic": 
            FF.XMLtoFrcAnglePotential_Harmonic(root, f)
        if root.find("AnglePotential/*").tag == "AnglePotential-COS2": 
            FF.XMLtoFrcAnglePotential_COS2(root, f)
	#Improper Potentials
    if "ImproperPotential" in tags_elements:
        if root.find("ImproperPotential/*").tag == "ImproperPotential-CHARMM": 
            FF.XMLtoFrcImproperPotential_CHARMM(root, f)
        if root.find("ImproperPotential/*").tag == "ImproperPotential-FourierSimple": 
            FF.XMLtoFrcImproperPotential_FourierSimple(root, f)
	#Dihedral Potentials
    if "DihedralPotential" in tags_elements:
        if root.find("DihedralPotential/*").tag == "DihedralPotential-FourierSimple": 
            FF.XMLtoFrcDihedralPotential_FourierSimple(root, f)
        if root.find("DihedralPotential/*").tag == "DihedralPotential-CHARMM": 
            FF.XMLtoFrcDihedralPotential_CHARMM(root, f)
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
    A.close()
#Allows this script to be called form the command line with input variables
if __name__ == "__main__":
    input = str((sys.argv[1]))
    output = str((sys.argv[2]))
    AToutput = str((sys.argv[3]))
    xml_frc(input, output, AToutput)
