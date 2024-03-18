.. _Dihedral-Tabular:

Tabular Dihedral
================

Tabular Form
---------------

The **tabular dihedral potential** has the parameters:

============= ================================================================================== ============
**Parameter** **Parameter Definition**                                                           **Units**
------------- ---------------------------------------------------------------------------------- ------------
N             Number of tabulated values                                                         N/A
------------- ---------------------------------------------------------------------------------- ------------
NOF           Allows omission of forces (energy derivatives) in the table                        N/A
------------- ---------------------------------------------------------------------------------- ------------
DEGREES       Specify degrees as units for the angles                                            N/A
------------- ---------------------------------------------------------------------------------- ------------
RADIANS       Specify radians as units for the angles                                            N/A
------------- ---------------------------------------------------------------------------------- ------------
CHECKU        File to save interpolated energy table                                             N/A
------------- ---------------------------------------------------------------------------------- ------------
CHECKF        File to save interpolated force table                                              N/A
============= ================================================================================== ============

The **tabular dihedral potential** has the tabulated values:

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

The XML schema for the **tabular dihedral potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Dihedral-Tabular.png
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
| Allows omission of forces in the table             | NOF                   | NOF                 |
+----------------------------------------------------+-----------------------+---------------------+
| Specify degrees as units for the angles            | DEGREES               | angle-units         |
+----------------------------------------------------+-----------------------+---------------------+
| Specify radians as units for the angles            | RADIANS               | angle-units         |
+----------------------------------------------------+-----------------------+---------------------+
| File to save interpolated energy table             | CHECKU                | CHECKU              |
+----------------------------------------------------+-----------------------+---------------------+
| File to save interpolated force table              | CHECKF                | CHECKF              |
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

1. `LAMMPS Tabular Dihedral Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Tabular Dihedral Potential: http://lammps.sandia.gov/doc/dihedral_table.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

