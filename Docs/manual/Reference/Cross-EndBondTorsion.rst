.. _Cross-EndBondTorsion:

Cross: End-Bond-Torsion  
==================

Functional Form
---------------

The **End-Bond-Torsion Cross Potential** has the functional form:

:math:`E=\left( {{R}_{jk}}-{{R}_{1,jk}} \right)\left[ {{B}_{1,ijkl}}\cos \left( {{\phi }_{ijkl}} \right)+{{B}_{2,ijkl}}\cos \left( 2{{\phi }_{ijkl}} \right)+{{B}_{3,ijkl}}\cos \left( 3{{\phi }_{ijkl}} \right) \right]`
:math:`\qquad +\left( {{R}_{kl}}-{{R}_{3,kl}} \right)\left[ {{C}_{1,ijkl}}\cos \left( {{\phi }_{ijkl}} \right)+{{C}_{2,ijkl}}\cos \left( 2{{\phi }_{ijkl}} \right)+{{C}_{3,ijkl}}\cos \left( 3{{\phi }_{ijkl}} \right) \right]`

This term is part of the Class2 Dihedral Potential style. 

The force-field parameters for this potential and units are given by:

=================== ======================================================= ===============
**Equation Symbol** **Parameter Definition**                                **Units**
------------------- ------------------------------------------------------- ---------------
:math:`B_{1,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`B_{2,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`B_{3,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`C_{1,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`C_{2,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`C_{3,ijkl}`  Cosine term coefficient for atoms [i,j,k,l]             energy/length
:math:`R_{1,jk}`    Equilibrium bond length for atoms [i,j]                 length
:math:`R_{3,kl}`    Equilibrium bond length for atoms [k,l]                 length
=================== ======================================================= ===============


XML Schema
----------

The XML schema for the **End-Bond-Torsion Cross Potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Cross-EndBondTorsion.png
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
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`B_{1,ijkl}`  | B1                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`B_{2,ijkl}`  | B2                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`B_{3,ijkl}`  | B3                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`C_{1,ijkl}`  | C1                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`C_{2,ijkl}`  | C2                  |
+------------------------------------------------+---------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`C_{3,ijkl}`  | C3                  |
+------------------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [i,j]        | :math:`R_{1,ij}`    | R1                  |
+------------------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [k,l]        | :math:`R_{3,kl}`    | R3                  |
+------------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =================================================================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -------------------------------------------------------------------------------------------------
style                  Fixed           EndBondTorsion
formula                Fixed           (R-R1)*[B1*cos(Phi)+B2*cos(2*Phi)+B3*cos(3*Phi)]+(R-R3)*[C1*cos(Phi)+C2*cos(2*Phi)+C3*cos(3*Phi)]
B-units                Required        Enumerations specified in schema
C-units                Required        Enumerations specified in schema
R-units                Required        Enumerations specified in schema
====================== =============== =================================================================================================

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

1. `LAMMPS Class2 Dihedral Potential w/ End-Bond-Torsion Cross term`_.

2. `SklogWiki COMPASS Force-Field`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Class2 Dihedral Potential w/ End-Bond-Torsion Cross term: http://lammps.sandia.gov/doc/dihedral_class2.html

.. _SklogWiki COMPASS Force-Field: http://www.sklogwiki.org/SklogWiki/index.php/COMPASS_force_field

.. _Liquid XML Studio: https://www.liquid-technologies.com/

