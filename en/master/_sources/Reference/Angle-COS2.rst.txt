.. _Angle-COS2:

COS2 Angle  
=============

Functional Form
---------------

The **COS2 angle potential** has the functional form:

:math:`E={{K}_{a,ijk}}{{\left[ \cos \left( {{\theta }_{ijk}} \right)-\cos \left( {{\theta }_{0,ijk}} \right) \right]}^{2}}`

The force-field parameters for this potential and units are given by:

====================== ========================================================= ================
**Equation Symbol**    **Parameter Definition**                                  **Units**
---------------------- --------------------------------------------------------- ----------------
:math:`K_{a,ijk}`      Angle coefficient for atoms [i,j,k]                       energy
:math:`\theta_{0,ijk}` Equilibrium angle for atoms [i,j,k]                       degrees
====================== ========================================================= ================


XML Schema
----------

The XML schema for the **COS2 angle potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Angle-COS2.png
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
| Angle coefficient for atoms [i,j,k]                      | :math:`K_{a,ijk}`      | Ka                  |
+----------------------------------------------------------+------------------------+---------------------+
| Equilibrium angle for atoms [i,j,k]                      | :math:`\theta_{0,ijk}` | Theta0              |
+----------------------------------------------------------+------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           cosine/squared
formula                Fixed           Ka*[cos(Theta)-cos(Theta0)]^2
Ka-units               Required        Enumerations specified in schema
Theta0-units           Required        Enumerations specified in schema
====================== =============== =======================================

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

1. `LAMMPS cosine/squared Angle Potential`_.

2. `GROMACS Cosine Based Angle Potential`_ page 96.

3. `Liquid XML Studio`_.

.. _LAMMPS cosine/squared Angle Potential: http://lammps.sandia.gov/doc/angle_cosine_squared.html

.. _GROMACS Cosine Based Angle Potential: http://manual.gromacs.org/documentation/2016.3/manual-2016.3.pdf

.. _Liquid XML Studio: https://www.liquid-technologies.com/

