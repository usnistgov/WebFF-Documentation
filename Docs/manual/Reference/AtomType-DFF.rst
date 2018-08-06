.. _AtomType-DFF:

Atom Type - DFF
================

XML Schema
----------

The XML schema for the **Atom Type - DFF** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/AtomType-DFF.png
	:align: left

The general attributes (describing the entire set of atoms) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
Nomenclature           Fixed           DFF
comment                Optional        Comment attached to set of atoms
====================== =============== =======================================

The general elements (describing the entire set of atoms) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
DFFRelationTree        Optional        Multiline DFF relation tree
====================== =============== =======================================

The specific attributes (attached to each atom description) are given by:

======================= =============== =======================================
**Specific Attributes** **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
Description             Required        Description of the atom
Element                 Required        Corresponding element of the atom
AtomicNumber            Required        Corresponding atomic number of the atom
AtomicMass              Required        Corresponding atomic mass of the atom
======================= =============== =======================================

The specific elements (contained within each instance of the atom template) are given by:

======================= =============== =======================================
**Specific Elements**   **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
AtomType-Name           Required        Atom type name
Substructure            Required        Atom
Index                   Required        Index of atom entry
Coordination            Optional        Coordination of the atom
Ringsize                Optional        Ringsize of the atom
Aromatic                Optional        Aromatic (true/false)
FormalCharge            Optional        Formal charge of the atom
ElementsAllowed         Optional        Elements allowed in the atom
ElementsDisallowed      Optional        Elements disallowed in the atom
======================= =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified.

References
----------

1. `DFF User Manual`_.

2. `Liquid XML Studio`_.

.. _DFF User Manual: http://www.aeontechnology.com/Product_DFF.php

.. _Liquid XML Studio: https://www.liquid-technologies.com/