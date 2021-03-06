.. _Dihedral-Harmonic:

Harmonic Dihedral  
==================

Functional Form
---------------

The **harmonic dihedral potential** has the functional form:

:math:`E={{K}_{d,ijkl}}\left[ 1+{{N}_{s}}\cos \left( N{{\phi }_{ijkl}} \right) \right]`

The force-field parameters for this potential and units are given by:

====================== ======================================== ================
**Equation Symbol**      **Parameter Definition**                 **Units**
---------------------- ---------------------------------------- ----------------
:math:`K_{d,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`N_{s}`          Determines sign convention (-1 or +1)    N/A
:math:`N`              Nonnegative integer coefficient          N/A
====================== ======================================== ================


XML Schema
----------

The XML schema for the **harmonic dihedral potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Dihedral-Harmonic.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+------------------------------------------------+-----------------------+---------------------+
| **Parameter Definition**                       | **Equation Symbol**   | **Schema Notation** |
+------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [i]                          | :math:`i`             | AT-1                |
+------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [j]                          | :math:`j`             | AT-2                |
+------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [k]                          | :math:`k`             | AT-3                |
+------------------------------------------------+-----------------------+---------------------+
| Atom type of atom [l]                          | :math:`l`             | AT-4                |
+------------------------------------------------+-----------------------+---------------------+
| Dihedral coefficient for atoms [i,j,k,l]       | :math:`K_{d,ijkl}`    | Kd                  |
+------------------------------------------------+-----------------------+---------------------+
| Determines sign convention (-1 or +1)          | :math:`N_{S}`         | Ns                  |
+------------------------------------------------+-----------------------+---------------------+
| Nonnegative integer coefficient                | :math:`N`             | N                   |
+------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Harmonic
formula                Fixed           Kd*[1+Ns*cos(N*Phi)]
convention             Optional        Enumerations specified in schema
Kd-units               Required        Enumerations specified in schema
====================== =============== =======================================

The specific attributes (attached to each set of parameters) are given by:

======================= =============== =============================================
**Specific Attributes** **Cardinality** **Definition**               
----------------------- --------------- ---------------------------------------------
comment                 Optional        Comment attached to parameter set
version                 Optional        Version number of parameter set
reference               Optional        Reference attached to parameter set 
======================= =============== =============================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified. 

References
----------

1. `LAMMPS Harmonic Dihedral Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Harmonic Dihedral Potential: http://lammps.sandia.gov/doc/dihedral_harmonic.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

