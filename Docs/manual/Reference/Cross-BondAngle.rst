.. _Cross-BondAngle:

Cross: Bond-Angle  
=================

Functional Form
---------------

The **Bond-Angle Cross Potential** has the functional form:

:math:`E={{N}_{1,ijk}}\left( {{R}_{ij}}-{{R}_{1,ij}} \right)\left( {{\theta }_{ijk}}-{{\theta }_{0,ijk}} \right)+{{N}_{2,ijk}}\left( {{R}_{jk}}-{{R}_{2,jk}} \right)\left( {{\theta }_{ijk}}-{{\theta }_{0,ijk}} \right)`

This term is part of the Class2 Angle Potential style. 

The force-field parameters for this potential and units are given by:

========================= ========================================================== =====================
**Equation Symbol**       **Parameter Definition**                                   **Units**
------------------------- ---------------------------------------------------------- ---------------------
:math:`N_{1,ijk}`         Cross potential bond-angle coefficient for atoms [i,j,k]   energy/length/degrees
:math:`N_{2,ijk}`         Cross potential bond-angle coefficient for atoms [i,j,k]   energy/length/degrees
:math:`R_{1,ij}`          Equilibrium bond length for atoms [i,j]                    length
:math:`R_{2,jk}`          Equilibrium bond length for atoms [j,k]                    length
:math:`{\theta }_{0,ijk}` Equilibrium angle for atoms [i,j,k]                        degrees
========================= ========================================================== =====================


XML Schema
----------

The XML schema for the **Bond-Angle Cross Potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Cross-BondAngle.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+---------------------------------------------------------------+---------------------------+---------------------+
| **Parameter Definition**                                      | **Equation Symbol**       | **Schema Notation** |
+---------------------------------------------------------------+---------------------------+---------------------+
| Atom type of atom [i]                                         | :math:`i`                 | AT-1                |
+---------------------------------------------------------------+---------------------------+---------------------+
| Atom type of atom [j]                                         | :math:`j`                 | AT-2                |
+---------------------------------------------------------------+---------------------------+---------------------+
| Atom type of atom [k]                                         | :math:`k`                 | AT-3                |
+---------------------------------------------------------------+---------------------------+---------------------+
| Equilibrium angle for atoms [i,j,k]                           | :math:`{\theta }_{0,ijk}` | Theta0              |
+---------------------------------------------------------------+---------------------------+---------------------+
| Cross potential bond-angle coefficient for atoms [i,j,k]      | :math:`N_{1,ijk}`         | N1                  |
+---------------------------------------------------------------+---------------------------+---------------------+
| Cross potential bond-angle coefficient for atoms [i,j,k]      | :math:`N_{2,ijk}`         | N2                  |
+---------------------------------------------------------------+---------------------------+---------------------+
| Equilibrium bond length for atoms [i,j]                       | :math:`R_{1,ij}`          | R1                  |
+---------------------------------------------------------------+---------------------------+---------------------+
| Equilibrium bond length for atoms [j,k]                       | :math:`R_{2,jk}`          | R2                  |
+---------------------------------------------------------------+---------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -------------------------------------------------
style                  Fixed           BondAngle
formula                Fixed           N1*(R-R1)*(Theta-Theta0)+N2*(R-R2)*(Theta-Theta0)
N-units                Required        Enumerations specified in schema
Ri-units               Required        Enumerations specified in schema
Theta0-units           Required        Enumerations specified in schema
====================== =============== =================================================

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

1. `LAMMPS Class2 Angle Potential w/ Bond-Angle Cross term`_.

2. `SklogWiki COMPASS Force-Field`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Class2 Angle Potential w/ Bond-Angle Cross term: http://lammps.sandia.gov/doc/angle_class2.html

.. _SklogWiki COMPASS Force-Field: http://www.sklogwiki.org/SklogWiki/index.php/COMPASS_force_field

.. _Liquid XML Studio: https://www.liquid-technologies.com/

