.. _Soft-DPD:

DPD Soft
=============

Functional Form
---------------

The **DPD soft potential** has the functional form:

:math:`E={{A}_{ij}}\left( 1-\frac{{{R}_{ij}}}{{{R}_{c}}} \right)-\gamma {{\left( 1-\frac{{{R}_{ij}}}{{{R}_{c}}} \right)}^{2}}+\sigma \left( 1-\frac{{{R}_{ij}}}{{{R}_{c}}} \right)\alpha {{(\Delta T)}^{-\frac{1}{2}}}`

The force-field parameters for this potential and units are given by:

=================== ======================================= ===============
**Equation Symbol** **Parameter Definition**                **Units**
------------------- --------------------------------------- ---------------
:math:`A_{ij}`      Coefficient for conservative force      force
:math:`\gamma`      Coefficient for dissipative force       force/velocity
:math:`R_{c}`       Cutoff distance value                   length
=================== ======================================= ===============


XML Schema
----------

The XML schema for the **soft DPD potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Soft-DPD.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-----------------------------------------+---------------------+---------------------+
| **Parameter Definition**                | **Equation Symbol** | **Schema Notation** |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                   | :math:`i`           | AT-1                |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                   | :math:`j`           | AT-2                |
+-----------------------------------------+---------------------+---------------------+
| Coefficient for conservative force      | :math:`A_{ij}`      | a_ij                |
+-----------------------------------------+---------------------+---------------------+
| Coefficient for dissipative force       | :math:`\gamma`      | gamma               |
+-----------------------------------------+---------------------+---------------------+
| Cutoff distance value                   | :math:`R_{c}`       | r_c                 |
+-----------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ====================================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- --------------------------------------------------------------------
style                  Fixed           DPD
formula                Fixed           a_ij*(1-r/r_c)-gamma*(1-r/r_c)^2+sigma*(1-r/r_c)*alpha*deltaT^(-1/2)
a_ij-units             Required        Enumerations specified in schema
gamma-units            Required        Enumerations specified in schema
r_c-units              Required        Enumerations specified in schema
====================== =============== ====================================================================

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

1. `LAMMPS DPD Pair Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS DPD Pair Potential: http://lammps.sandia.gov/doc/pair_dpd.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

