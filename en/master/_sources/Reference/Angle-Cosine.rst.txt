.. _Angle-Cosine:

Cosine Angle  
=============

Functional Form
---------------

The **cosine angle potential** has the functional form:

:math:`E={{K}_{a,ijk}}\left[ 1+\cos \left( {{\theta }_{ijk}} \right) \right]`

The force-field parameters for this potential and units are given by:

====================== ========================================================= ================
**Equation Symbol**    **Parameter Definition**                                  **Units**
---------------------- --------------------------------------------------------- ----------------
:math:`K_{a,ijk}`      Angle coefficient for atoms [i,j,k]                       energy
====================== ========================================================= ================


XML Schema
----------

The XML schema for the **cosine angle potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Angle-Cosine.png
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

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Cosine
formula                Fixed           Ka*[1+cos(theta)]
Ka-units               Required        Enumerations specified in schema
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

1. `LAMMPS Cosine Angle Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Cosine Angle Potential: http://lammps.sandia.gov/doc/angle_cosine.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

