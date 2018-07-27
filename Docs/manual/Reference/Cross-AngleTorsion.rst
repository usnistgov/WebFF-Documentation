.. _Cross-AngleTorsion:

Cross: Angle-Torsion  
==================

Functional Form
---------------

The **Angle-Torsion Cross Potential** has the functional form:

:math:`E=\left( {{\theta }_{ijk}}-{{\theta }_{1,ijk}} \right)\left[ {{D}_{1,ijkl}}\cos \left( {{\phi }_{ijkl}} \right)+{{D}_{2,ijkl}}\cos \left( 2{{\phi }_{ijkl}} \right)+{{D}_{3,ijkl}}\cos \left( 3{{\phi }_{ijkl}} \right) \right]`
:math:`\qquad +\left( {{\theta }_{jkl}}-{{\theta }_{2,jkl}} \right)\left[ {{E}_{1,ijkl}}\cos \left( {{\phi }_{ijkl}} \right)+{{E}_{2,ijkl}}\cos \left( 2{{\phi }_{ijkl}} \right)+{{E}_{3,ijkl}}\cos \left( 3{{\phi }_{ijkl}} \right) \right]`

This term is part of the Class2 Dihedral Potential style. 

The force-field parameters for this potential and units are given by:

======================== ======================================================= ===============
**Equation Symbol**      **Parameter Definition**                                **Units**
------------------------ ------------------------------------------------------- ---------------
:math:`D_{1,ijkl}`       Cosine term coefficient for atoms [i,j,k,l]             energy/angle
:math:`D_{2,ijkl}`       Cosine term coefficient for atoms [i,j,k,l]             energy/angle
:math:`D_{3,ijkl}`       Cosine term coefficient for atoms [i,j,k,l]             energy/angle
:math:`E_{1,ijkl}`       Cosine term coefficient for atoms [i,j,k,l]             energy/angle
:math:`E_{2,ijkl}`       Cosine term coefficient for atoms [i,j,k,l]             energy/angle
:math:`E_{3,ijkl}`       Cosine term coefficient for atoms [i,j,k,l]             energy/angle
:math:`{\theta}_{1,ijk}` Equilibrium bond length for atoms [i,j]                 angle
:math:`{\theta}_{2,jkl}` Equilibrium bond length for atoms [k,l]                 angle
======================== ======================================================= ===============


XML Schema
----------

The XML schema for the **Angle-Torsion Cross Potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Cross-AngleTorsion.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+------------------------------------------------+-----------------------------+---------------------+
| **Parameter Definition**                       | **Equation Symbol**         | **Schema Notation** |
+------------------------------------------------+-----------------------------+---------------------+
| Atom type of atom [i]                          | :math:`i`                   | AT-1                |
+------------------------------------------------+-----------------------------+---------------------+
| Atom type of atom [j]                          | :math:`j`                   | AT-2                |
+------------------------------------------------+-----------------------------+---------------------+
| Atom type of atom [k]                          | :math:`k`                   | AT-3                |
+------------------------------------------------+-----------------------------+---------------------+
| Atom type of atom [l]                          | :math:`l`                   | AT-4                |
+------------------------------------------------+-----------------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`D_{1,ijkl}`          | D1                  |
+------------------------------------------------+-----------------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`D_{2,ijkl}`          | D2                  |
+------------------------------------------------+-----------------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`D_{3,ijkl}`          | D3                  |
+------------------------------------------------+-----------------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`E_{1,ijkl}`          | E1                  |
+------------------------------------------------+-----------------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`E_{2,ijkl}`          | E2                  |
+------------------------------------------------+-----------------------------+---------------------+
| Cosine term coefficient for atoms [i,j,k,l]    | :math:`E_{3,ijkl}`          | E3                  |
+------------------------------------------------+-----------------------------+---------------------+
| Equilibrium bond length for atoms [i,j]        | :math:`{\theta}_{1,ijk}`    | Theta1              |
+------------------------------------------------+-----------------------------+---------------------+
| Equilibrium bond length for atoms [k,l]        | :math:`{\theta}_{2,jkl}`    | Theta2              |
+------------------------------------------------+-----------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =================================================================================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -----------------------------------------------------------------------------------------------------------------
style                  Fixed           AngleTorsion
formula                Fixed           (Theta-Theta1)*[D1*cos(Phi)+D2*cos(2*Phi)+D3*cos(3*Phi)]+(Theta-Theta2)*[E1*cos(Phi)+E2*cos(2*Phi)+E3*cos(3*Phi)]
D-units                Required        Enumerations specified in schema
E-units                Required        Enumerations specified in schema
Theta-units            Required        Enumerations specified in schema
====================== =============== =================================================================================================================

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

1. `LAMMPS Class2 Dihedral Potential w/ Angle-Torsion Cross term`_.

2. `SklogWiki COMPASS Force-Field`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Class2 Dihedral Potential w/ Angle-Torsion Cross term: http://lammps.sandia.gov/doc/dihedral_class2.html

.. _SklogWiki COMPASS Force-Field: http://www.sklogwiki.org/SklogWiki/index.php/COMPASS_force_field

.. _Liquid XML Studio: https://www.liquid-technologies.com/

