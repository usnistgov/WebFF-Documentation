.. _NonBond-Mie:

Non-Bond Mie Potential  
================================

Functional Form
---------------

The **non-bond Mie potential** has the functional form:

:math:`E=C\epsilon \left[ {{\left( \frac{{{\sigma }_{ij}}}{{{R}_{ij}}} \right)}^{{{\gamma }_{rep}}}}-{{\left( \frac{{{\sigma }_{ij}}}{{{R}_{ij}}} \right)}^{{{\gamma }_{att}}}} \right]`

The force-field parameters for this potential and units are given by:

======================== ============================================= ===============
**Equation Symbol**      **Parameter Definition**                      **Units**
------------------------ --------------------------------------------- ---------------
:math:`\epsilon`         Potential well depth for atom [i]             energy/mol
:math:`\sigma`           Interatomic cut-off distance for atom [i]     length
:math:`{\gamma }_{rep}`  Exponent of repulsive term                    N/A
:math:`{\gamma }_{att}`  Exponent of attractive term                   N/A
======================== ============================================= ===============


XML Schema
----------

The XML schema for the **non-bond Mie potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-Mie.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-------------------------------------------+------------------------------+---------------------+
| **Parameter Definition**                  | **Equation Symbol**          | **Schema Notation** |
+-------------------------------------------+------------------------------+---------------------+
| Atom type of atom [i]                     | (implicit)                   | AT1                 |
+-------------------------------------------+------------------------------+---------------------+
| Atom type of atom [j]                     | (implicit)                   | AT2                 |
+-------------------------------------------+------------------------------+---------------------+
| Potential well depth for atom [i]         | :math:`\epsilon`             | epsilon             |
+-------------------------------------------+------------------------------+---------------------+
| Interatomic cut-off distance for atom [i] | :math:`\sigma`               | sigma               |
+-------------------------------------------+------------------------------+---------------------+
| Exponent of repulsive term                | :math:`{\gamma }_{rep}`      | m_rep               |
+-------------------------------------------+------------------------------+---------------------+
| Exponent of attractive term               | :math:`{\gamma }_{att}`      | n_att               |
+-------------------------------------------+------------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ===========================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -------------------------------------------
style                  Fixed           Mie
formula                Fixed           C*epsilon*[(sigma/R)^m_rep-(sigma/R)^n_att]
a_ij-units             Required        Enumerations specified in schema
r_c-units              Required        Enumerations specified in schema
====================== =============== ===========================================

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

1. `LAMMPS Mie Pair Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Mie Pair Potential: https://lammps.sandia.gov/doc/pair_mie.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

