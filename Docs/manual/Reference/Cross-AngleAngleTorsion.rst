.. _Cross-AngleAngleTorsion:

Cross: Angle-Angle-Torsion  
==================

Functional Form
---------------

The **Angle-Angle-Torsion Cross Potential** has the functional form:

:math:`E={{M}_{ijkl}}\left( {{\theta }_{ijk}}-{{\theta }_{1,ijk}} \right)\left( {{\theta }_{jkl}}-{{\theta }_{2,jkl}} \right)\cos \left( {{\phi }_{ijkl}} \right)`

This term is part of the Class2 Dihedral Potential style. 

The force-field parameters for this potential and units are given by:

======================== ======================================================= ===============
**Equation Symbol**      **Parameter Definition**                                **Units**
------------------------ ------------------------------------------------------- ---------------
:math:`M_{ijkl}`         Bond coefficient for atoms [i,j,k,l]                    energy
:math:`{\theta}_{1,ijk}` Equilibrium angle for atoms [i,j,k]                     degrees
:math:`{\theta}_{2,jkl}` Equilibrium angle for atoms [j,k,l]                     degrees
======================== ======================================================= ===============


XML Schema
----------

The XML schema for the **Angle-Angle-Torsion Cross Potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Cross-AngleAngleTorsion.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-----------------------------------------+-----------------------------+---------------------+
| **Parameter Definition**                | **Equation Symbol**         | **Schema Notation** |
+-----------------------------------------+-----------------------------+---------------------+
| Atom type of atom [i]                   | :math:`i`                   | AT-1                |
+-----------------------------------------+-----------------------------+---------------------+
| Atom type of atom [j]                   | :math:`j`                   | AT-2                |
+-----------------------------------------+-----------------------------+---------------------+
| Atom type of atom [k]                   | :math:`k`                   | AT-3                |
+-----------------------------------------+-----------------------------+---------------------+
| Atom type of atom [l]                   | :math:`l`                   | AT-4                |
+-----------------------------------------+-----------------------------+---------------------+
| Bond coefficient for atoms [i,j,k,l]    | :math:`M_{ijkl}`            | M                   |
+-----------------------------------------+-----------------------------+---------------------+
| Equilibrium angle for atoms [i,j,k]     | :math:`{\theta}_{1,ijk}`    | Theta1              |
+-----------------------------------------+-----------------------------+---------------------+
| Equilibrium angle for atoms [j,k,l]     | :math:`{\theta}_{2,jkl}`    | Theta2              |
+-----------------------------------------+-----------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           AngleAngleTorsion
formula                Fixed           M(Theta-Theta1)*(Theta-Theta2)*cos(Phi)
M-units                Required        Enumerations specified in schema
Theta-units            Required        Enumerations specified in schema
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

1. `LAMMPS Class2 Dihedral Potential w/ Angle-Angle-Torsion Cross term`_.

2. `SklogWiki COMPASS Force-Field`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Class2 Dihedral Potential w/ Angle-Angle-Torsion Cross term: http://lammps.sandia.gov/doc/dihedral_class2.html

.. _SklogWiki COMPASS Force-Field: http://www.sklogwiki.org/SklogWiki/index.php/COMPASS_force_field

.. _Liquid XML Studio: https://www.liquid-technologies.com/

