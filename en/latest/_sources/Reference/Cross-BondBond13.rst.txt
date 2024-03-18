.. _Cross-BondBond13:

Cross: Bond-Bond-13  
===================

Functional Form
---------------

The **Bond-Bond-13 Cross Potential** has the functional form:

:math:`E = {N} \left( {{R_{ij}} - {R_{1,ij}}} \right) \left( {{R_{kl}} - {R_{3,kl}}} \right)`

This term is part of the Class2 Dihedral Potential style. 

The force-field parameters for this potential and units are given by:

=================== ======================================================= ===============
**Equation Symbol** **Parameter Definition**                                **Units**
------------------- ------------------------------------------------------- ---------------
:math:`N`           Cross potential bond coefficient for atoms [i,j,k,l]    energy
:math:`R_{1,ij}`    Equilibrium bond length for atoms [i,j]                 length
:math:`R_{3,kl}`    Equilibrium bond length for atoms [k,l]                 length
=================== ======================================================= ===============


XML Schema
----------

The XML schema for the **Bond-Bond-13 Cross Potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Cross-BondBond13.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-----------------------------------------+---------------------+---------------------+
| **Parameter Definition**                | **Equation Symbol** | **Schema Notation** |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                   | :math:`i`           | AT-1                |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                   | :math:`j`           | AT-2                |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [k]                   | :math:`k`           | AT-3                |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [l]                   | :math:`l`           | AT-4                |
+-----------------------------------------+---------------------+---------------------+
| Bond coefficient for atoms [i,j,k,l]    | :math:`N`           | N                   |
+-----------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [i,j] | :math:`R_{1,ij}`    | R1                  |
+-----------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [k,l] | :math:`R_{3,kl}`    | R3                  |
+-----------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           BondBond13
formula                Fixed           N*(Rij-R1)*(Rkl-R3)
N-units                Required        Enumerations specified in schema
Ri-units               Required        Enumerations specified in schema
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

1. `LAMMPS Class2 Dihedral Potential w/ Bond-Bond-13 Cross term`_.

2. `SklogWiki COMPASS Force-Field`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Class2 Dihedral Potential w/ Bond-Bond-13 Cross term: http://lammps.sandia.gov/doc/dihedral_class2.html

.. _SklogWiki COMPASS Force-Field: http://www.sklogwiki.org/SklogWiki/index.php/COMPASS_force_field

.. _Liquid XML Studio: https://www.liquid-technologies.com/

