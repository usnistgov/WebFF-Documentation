.. _NonBond-Soft:

Non-Bond Soft Potential  
================================

Functional Form
---------------

The **non-bond Soft potential** has the functional form:

:math:`E={{A}_{ij}}\left[ 1+\cos \left( \frac{\pi R}{{{R}_{c}}} \right) \right]`

The force-field parameters for this potential and units are given by:

=================== ============================================= ===============
**Equation Symbol** **Parameter Definition**                      **Units**
------------------- --------------------------------------------- ---------------
:math:`A_{ij}`      Coefficient for atom [i]                      energy/mol
:math:`R_{c}`       Interatomic cut-off distance for atom [i]     length
=================== ============================================= ===============


XML Schema
----------

The XML schema for the **non-bond Soft potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-Soft.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                  | **Equation Symbol** | **Schema Notation** |
+-------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                     | (implicit)          | AT1                 |
+-------------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                     | (implicit)          | AT2                 |
+-------------------------------------------+---------------------+---------------------+
| Coefficient for atom [i]                  | :math:`A_{ij}`      | a_ij                |
+-------------------------------------------+---------------------+---------------------+
| Interatomic cut-off distance for atom [i] | :math:`R_{c}`       | r_c                 |
+-------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Soft
formula                Fixed           a_ij*[1+cos(pi*r/r_c)]
a_ij-units             Required        Enumerations specified in schema
r_c-units              Required        Enumerations specified in schema
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

1. `LAMMPS Soft Pair Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Soft Pair Potential: https://lammps.sandia.gov/doc/pair_soft.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

