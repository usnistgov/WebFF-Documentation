.. _Angle-Class2:

Class2 Angle  
=============

Functional Form
---------------

The **class 2 angle potential** has the functional form:

:math:`E={{K}_{2,ijk}}{{\left( {{\theta }_{ijk}}-{{\theta }_{0,ijk}} \right)}^{2}}+{{K}_{3,ijk}}{{\left( {{\theta }_{ijk}}-{{\theta }_{0,ijk}} \right)}^{3}}+{{K}_{4,ijk}}{{\left( {{\theta }_{ijk}}-{{\theta }_{0,ijk}} \right)}^{4}}`

The force-field parameters for this potential and units are given by:

====================== ========================================================= ================
**Equation Symbol**    **Parameter Definition**                                  **Units**
---------------------- --------------------------------------------------------- ----------------
:math:`K_{2,ijk}`      Angle coefficient for atoms [i,j,k] (quadratic term)      energy/degrees^2
:math:`K_{3,ijk}`      Angle coefficient for atoms [i,j,k] (cubic term)          energy/degrees^3
:math:`K_{4,ijk}`      Angle coefficient for atoms [i,j,k] (quartic term)        energy/degrees^4
:math:`\theta_{0,ijk}` Equilibrium angle for atoms [i,j,k]                       degrees
====================== ========================================================= ================


XML Schema
----------

The XML schema for the **class 2 angle potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Angle-Class2.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+----------------------------------------------------------+------------------------+---------------------+
| **Parameter Definition**                                 | **Equation Symbol**    | **Schema Notation** |
+----------------------------------------------------------+------------------------+---------------------+
| Atom type of atom [i]                                    | :math:`i`              | AT-1                |
+----------------------------------------------------------+------------------------+---------------------+
| Atom type of atom [j]                                    | :math:`j`              | AT-2                |
+----------------------------------------------------------+------------------------+---------------------+
| Atom type of atom [k]                                    | :math:`k`              | AT-3                |
+----------------------------------------------------------+------------------------+---------------------+
| Angle coefficient for atoms [i,j,k] (quadratic term)     | :math:`K_{2,ijk}`      | K2                  |
+----------------------------------------------------------+------------------------+---------------------+
| Angle coefficient for atoms [i,j,k] (cubic term)         | :math:`K_{3,ijk}`      | K3                  |
+----------------------------------------------------------+------------------------+---------------------+
| Angle coefficient for atoms [i,j,k] (quartic term)       | :math:`K_{4,ijk}`      | K4                  |
+----------------------------------------------------------+------------------------+---------------------+
| Equilibrium angle for atoms [i,j,k]                      | :math:`\theta_{0,ijk}` | Theta0              |
+----------------------------------------------------------+------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ===========================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -----------------------------------------------------------
style                  Fixed           Class2
formula                Fixed           K2*(Theta-Theta0)^2+K3*(Theta-Theta0)^3+K4*(Theta-Theta0)^4
K-units                Required        Enumerations specified in schema
Theta0-units           Required        Enumerations specified in schema
====================== =============== ===========================================================

The specific attributes (attached to each set of parameters) are given by:

======================= =============== =============================================
**Specific Attributes** **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------------
precedence              Optional        Precedence of parameter set (where specified)
comment                 Optional        Comment attached to parameter set
version                 Optional        Version number of parameter set
reference               Optional        Reference attached to parameter set 
======================= =============== =============================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified. 

References
----------

1. `LAMMPS Class 2 Angle Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Class 2 Angle Potential: http://lammps.sandia.gov/doc/angle_class2.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

