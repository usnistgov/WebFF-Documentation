.. _NonBond-LJ-Rmin:

Non-Bond Lennard-Jones (Rmin Form) Potential  
============================================

Functional Form
---------------

The **non-bond Lennard-Jones (Rmin Form) potential** has the functional form:

:math:`E=\epsilon \left[ {{\left( \frac{{{R}_{\min ,ij}}}{{{R}_{ij}}} \right)}^{12}}-2{{\left( \frac{{{R}_{\min ,ij}}}{{{R}_{ij}}} \right)}^{6}} \right]`

The force-field parameters for this potential and units are given by:

=================== ============================================= ===============
**Equation Symbol** **Parameter Definition**                      **Units**
------------------- --------------------------------------------- ---------------
:math:`\epsilon`    Potential well depth for atom [i]             energy/mol
:math:`R_{min,ij}`  Interatomic cut-off distance for atom [i]     length
=================== ============================================= ===============


XML Schema
----------

The XML schema for the **non-bond Lennard-Jones (Rmin Form) potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-LJ-Rmin.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                  | **Equation Symbol** | **Schema Notation** |
+-------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                     | (implicit)          | AtomType            |
+-------------------------------------------+---------------------+---------------------+
| Potential well depth for atom [i]         | :math:`\epsilon`    | epsilon             |
+-------------------------------------------+---------------------+---------------------+
| Distance at the Lennard-Jones minimum [i] | :math:`R_{min,ij}`  | Rmin                |
+-------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Lennard-Jones (12-6) [Rmin Form]
formula                Fixed           epsilon*[(Rmin/R)^12-2*(Rmin/R)^6]
epsilon-units          Required        Enumerations specified in schema
Rmin-units             Required        Enumerations specified in schema
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

1. `Amber 2017 Reference Manual`_ page 248.

2. `Wikipedia AMBER (Force-Fields)`_.

3. `Wikipedia Lennard-Jones Potential`_.

.. _Amber 2017 Reference Manual: http://ambermd.org/doc12/Amber17.pdf

.. _Wikipedia AMBER (Force-Fields): https://en.wikipedia.org/wiki/AMBER

.. _Wikipedia Lennard-Jones Potential: https://en.wikipedia.org/wiki/Lennard-Jones_potential

