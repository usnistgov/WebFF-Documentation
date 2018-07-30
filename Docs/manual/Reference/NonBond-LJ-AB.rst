.. _NonBond-LJ-AB:

Non-Bond Lennard-Jones (AB Form) Potential
==========================================

Functional Form
---------------

The **non-bond Lennard-Jones (AB Form) potential** has the functional form:

:math:`E=\frac{{{A}_{ij}}}{R_{ij}^{12}}-\frac{{{B}_{ij}}}{R_{ij}^{6}}`

The force-field parameters for this potential and units are given by:

=================== ================================================ =====================
**Equation Symbol** **Parameter Definition**                         **Units**
------------------- ------------------------------------------------ ---------------------
:math:`A_{ij}`      General 12th power Lennard-Jones coefficient [i] energy*length^12/mol
:math:`B_{ij}`      General 6th power Lennard-Jones coefficient [i]  energy*length^6/mol
=================== ================================================ =====================


XML Schema
----------

The XML schema for the **non-bond Lennard-Jones (AB Form) potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-LJ-AB.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+--------------------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                               | **Equation Symbol** | **Schema Notation** |
+--------------------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                                  | (implicit)          | AtomType            |
+--------------------------------------------------------+---------------------+---------------------+
| General 12th power Lennard-Jones coefficient [i]       | :math:`A_{ij}`      | A                   |
+--------------------------------------------------------+---------------------+---------------------+
| General 6th power Lennard-Jones coefficient [i]        | :math:`B_{ij}`      | B                   |
+--------------------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Lennard-Jones (12-6) [A-B Form]
formula                Fixed           A/(R^12)-B/(R^6)
A--units               Required        Enumerations specified in schema
B-units                Required        Enumerations specified in schema
Combining-Rule         Required        Combining rule for mixed atom types
====================== =============== =======================================

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

1. `Amber 2017 Reference Manual`_ page 248.

2. `Wikipedia AMBER (Force-Fields)`_.

3. `Wikipedia Lennard-Jones Potential`_.

.. _Amber 2017 Reference Manual: http://ambermd.org/doc12/Amber17.pdf

.. _Wikipedia AMBER (Force-Fields): https://en.wikipedia.org/wiki/AMBER

.. _Wikipedia Lennard-Jones Potential: https://en.wikipedia.org/wiki/Lennard-Jones_potential

