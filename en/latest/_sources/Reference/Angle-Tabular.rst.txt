.. _Angle-Tabular:

Tabular Angle
================

Tabular Form
---------------

The **tabular angle potential** has the parameters:

============= ================================================================================== ============
**Parameter** **Parameter Definition**                                                           **Units**
------------- ---------------------------------------------------------------------------------- ------------
N             Number of tabulated values                                                         N/A
------------- ---------------------------------------------------------------------------------- ------------
FP            Derivatives of the force at the innermost (fplo) and outermost (fphi) angles       force/angle
------------- ---------------------------------------------------------------------------------- ------------
EQ            Equilibrium angle                                                                  angle
============= ================================================================================== ============

The **tabular angle potential** has the tabulated values:

========= =============== ========== ===============
**index** **angle**       **energy** **derivative**
--------- --------------- ---------- ---------------
i_1       a_1             e_1        de_1
--------- --------------- ---------- ---------------
...       ...             ...        ...
--------- --------------- ---------- ---------------
i_N       a_N             e_n        de_N
========= =============== ========== ===============

XML Schema
----------

The XML schema for the **tabular angle potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Angle-Tabular.png
	:align: left

The relationship between the parameters/symbols and XML schema notations are given by:

+----------------------------------------------------+-----------------------+---------------------+
| **Parameter Definition**                           | **Parameter/Symbol**  | **Schema Notation** |
+----------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [i]                              | :math:`i`             | AT-1                |
+----------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [j]                              | :math:`j`             | AT-2                |
+----------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [k]                              | :math:`k`             | AT-3                |
+----------------------------------------------------+-----------------------+---------------------+
| Section identifying keyword                        | N/A                   | keyword             |
+----------------------------------------------------+-----------------------+---------------------+
| Number of tabulated values                         | N                     | N                   |
+----------------------------------------------------+-----------------------+---------------------+
| Derivative of the force at the innermost           | FP                    | fplo                |
+----------------------------------------------------+-----------------------+---------------------+
| Derivative of the force at the outermost           | FP                    | fphi                |
+----------------------------------------------------+-----------------------+---------------------+
| Equilibrium angle                                  | EQ                    | EQ                  |
+----------------------------------------------------+-----------------------+---------------------+
| Index                                              | index                 | index               |
+----------------------------------------------------+-----------------------+---------------------+
| Angle                                              | angle                 | angle               |
+----------------------------------------------------+-----------------------+---------------------+
| Energy                                             | energy                | energy              |
+----------------------------------------------------+-----------------------+---------------------+
| Derivate of energy                                 | derivative            | energy-diff         |
+----------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Tabular
angle-units            Required        Enumerations specified in schema
energy-units           Required        Enumerations specified in schema
energy-diff-units      Required        Enumerations specified in schema
comment                Optional        Comment attached to parameter set
version                Optional        Version number of parameter set
reference              Optional        Reference attached to parameter set 
====================== =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified. 

References
----------

1. `LAMMPS Tabular Angle Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Tabular Angle Potential: http://lammps.sandia.gov/doc/angle_table.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

