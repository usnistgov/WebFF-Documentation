.. _NonBond-Class2:

Non-Bond Lennard-Jones (Class 2 Form) Potential  
================================

Functional Form
---------------

The **non-bond Lennard-Jones (Class 2 Form) potential** has the functional form:

:math:`E=\epsilon \left[ 2{{\left( \frac{{R_{min}}}{{{R}_{ij}}} \right)}^{9}}-3{{\left( \frac{{R_{min}}}{{{R}_{ij}}} \right)}^{6}} \right]`

The force-field parameters for this potential and units are given by:

=================== ============================================= ===============
**Equation Symbol** **Parameter Definition**                      **Units**
------------------- --------------------------------------------- ---------------
:math:`\epsilon`    Potential well depth for atom [i]             energy/mol
:math:`R_{min}`     Interatomic cut-off distance for atom [i]     length
=================== ============================================= ===============


XML Schema
----------

The XML schema for the **non-bond Lennard-Jones (9-6 Form) potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-Class2.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                  | **Equation Symbol** | **Schema Notation** |
+-------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                     | (implicit)          | AtomType            |
+-------------------------------------------+---------------------+---------------------+
| Potential well depth for atom [i]         | :math:`\epsilon`    | epsilon             |
+-------------------------------------------+---------------------+---------------------+
| Interatomic cut-off distance for atom [i] | :math:`\sigma`      | sigma               |
+-------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Lennard-Jones (9-6) [Class 2 Form]
formula                Fixed           epsilon*[2*(Rmin/R)^9-3*(Rmin/R)^6]
epsilon-units          Required        Enumerations specified in schema
sigma-units            Required        Enumerations specified in schema
Combining-Rule         Required        Combining rule for mixed atom types
====================== =============== =======================================

The specific attributes (attached to each set of parameters) are given by:

======================= =============== =======================================
**Specific Attributes** **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
comment                 Optional        Comment attached to parameter set
version                 Optional        Version number of parameter set
reference               Optional        Reference attached to parameter set 
======================= =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified. 

References
----------

1. `LAMMPS Lennard-Jones Pair Potential Class 2`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Lennard-Jones Pair Potential Class 2: https://lammps.sandia.gov/doc/pair_class2.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

