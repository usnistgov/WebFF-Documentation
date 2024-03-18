.. _Cross-MiddleBondTorsion:

Cross: Middle-Bond-Torsion  
==========================

Functional Form
---------------

The **Middle-Bond-Torsion Cross Potential** has the functional form:

:math:`E=\left( {{R}_{jk}}-{{R}_{2,jk}} \right)\left[ {{A}_{1,ijkl}}\cos \left( {{\phi }_{ijkl}} \right)+{{A}_{2,ijkl}}\cos \left( 2{{\phi }_{ijkl}} \right)+{{A}_{3,ijkl}}\cos \left( 3{{\phi }_{ijkl}} \right) \right]`

This term is part of the Class2 Dihedral Potential style. 

The force-field parameters for this potential and units are given by:

=================== ======================================================= ===============
**Equation Symbol** **Parameter Definition**                                **Units**
------------------- ------------------------------------------------------- ---------------
:math:`A_{1,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`A_{2,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`A_{3,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`R_{2,jk}`    Equilibrium bond length for atoms [j,k]                 length
=================== ======================================================= ===============


XML Schema
----------

The XML schema for the **Middle-Bond-Torsion Cross Potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Cross-MiddleBondTorsion.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+------------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                       | **Equation Symbol** | **Schema Notation** |
+------------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                          | :math:`i`           | AT-1                |
+------------------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                          | :math:`j`           | AT-2                |
+------------------------------------------------+---------------------+---------------------+
| Atom type of atom [k]                          | :math:`k`           | AT-3                |
+------------------------------------------------+---------------------+---------------------+
| Atom type of atom [l]                          | :math:`l`           | AT-4                |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`A_{1,ijkl}`  | A1                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`A_{2,ijkl}`  | A2                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`A_{3,ijkl}`  | A3                  |
+------------------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [j,k]        | :math:`R_{2,jk}`    | R2                  |
+------------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ------------------------------------------------
style                  Fixed           MiddleBondTorsion
formula                Fixed           (R-R2)*[A1*cos(Phi)+A2*cos(2*Phi)+A3*cos(3*Phi)]
A-units                Required        Enumerations specified in schema
R-units                Required        Enumerations specified in schema
====================== =============== ================================================

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

1. `LAMMPS Class2 Dihedral Potential w/ Middle-Bond-Torsion Cross term`_.

2. `SklogWiki COMPASS Force-Field`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Class2 Dihedral Potential w/ Middle-Bond-Torsion Cross term: http://lammps.sandia.gov/doc/dihedral_class2.html

.. _SklogWiki COMPASS Force-Field: http://www.sklogwiki.org/SklogWiki/index.php/COMPASS_force_field

.. _Liquid XML Studio: https://www.liquid-technologies.com/

