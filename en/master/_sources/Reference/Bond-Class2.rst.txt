.. _Bond-Class2:

Class2 Bond  
=============

Functional Form
---------------

The **class 2 bond potential** has the functional form:

:math:`E={{K}_{2,ij}}{{\left( {{R}_{ij}}-{{R}_{0,ij}} \right)}^{2}}+{{K}_{3,ij}}{{\left( {{R}_{ij}}-{{R}_{0,ij}} \right)}^{3}}+{{K}_{4,ij}}{{\left( {{R}_{ij}}-{{R}_{0,ij}} \right)}^{4}}`

The force-field parameters for this potential and units are given by:

=================== ================================================= ===============
**Equation Symbol** **Parameter Definition**                          **Units**
------------------- ------------------------------------------------- ---------------
:math:`K_{2,ij}`    Bond coefficient for atoms [i,j] (quadratic term) energy/length^2
:math:`K_{3,ij}`    Bond coefficient for atoms [i,j] (cubic term)     energy/length^3
:math:`K_{4,ij}`    Bond coefficient for atoms [i,j] (quartic term)   energy/length^4
:math:`R_{0,ij}`    Equilibrium bond length for atoms [i,j]           length
=================== ================================================= ===============


XML Schema
----------

The XML schema for the **class 2 bond potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Bond-Class2.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+---------------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                          | **Equation Symbol** | **Schema Notation** |
+---------------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                             | :math:`i`           | AT-1                |
+---------------------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                             | :math:`j`           | AT-2                |
+---------------------------------------------------+---------------------+---------------------+
| Bond coefficient for atoms [i,j] (quadratic term) | :math:`K_{2,ij}`    | K2                  |
+---------------------------------------------------+---------------------+---------------------+
| Bond coefficient for atoms [i,j] (cubic term)     | :math:`K_{3,ij}`    | K3                  |
+---------------------------------------------------+---------------------+---------------------+
| Bond coefficient for atoms [i,j] (quartic term)   | :math:`K_{4,ij}`    | K4                  |
+---------------------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [i,j]           | :math:`R_{0,ij}`    | R0                  |
+---------------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Class2
formula                Fixed           K2*(R-R0)^2+K3*(R-R0)^3+K4*(R-R0)^4
K-units                Required        Enumerations specified in schema
R0-units               Required        Enumerations specified in schema
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

1. `LAMMPS Class 2 Bond Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Class 2 Bond Potential: http://lammps.sandia.gov/doc/bond_class2.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

