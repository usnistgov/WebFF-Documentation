.. _AtomType-Coarse-Grained:

Atom Type - Coarse Grained
==========================

XML Schema
----------

The XML schema for the **Atom Type - Coarse Grained** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/AtomType-Coarse-Grained.png
	:align: left

The general attributes (describing the entire set of atoms) are given by:

====================== =============== ===========================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -------------------------------------------
Nomenclature           Fixed           SMILES | SMARTS | CurlySMILES | SLN | InChi
comment                Optional        Comment attached to set of atoms
====================== =============== ===========================================

The specific attributes (attached to each atom description) are given by:

======================= =============== =======================================
**Specific Attributes** **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
Description             Required        Description of the atom
AtomicMass-CG           Required        Corresponding atomic mass of the atom
AtomicMSize-CG          Required        Corresponding atomic size of the atom
======================= =============== =======================================

The specific elements (contained within each instance of the atom template) are given by:

======================= =============== =======================================
**Specific Elements**   **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
CG-Name                 Required        Atom type name
CG_chemistry            Optional        Chemistry of the atom
======================= =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified.

References
----------

1. `Liquid XML Studio`_.

.. _Liquid XML Studio: https://www.liquid-technologies.com/