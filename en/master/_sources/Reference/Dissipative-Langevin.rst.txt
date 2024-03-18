.. _Dissipative-Langevin:

Langevin Dissipative
====================

Functional Form
---------------

The **Langevin dissipative potential** has the functional form:

:math:`E=\gamma`

The force-field parameters for this potential and units are given by:

=================== ======================================= ===============
**Equation Symbol** **Parameter Definition**                **Units**
------------------- --------------------------------------- ---------------
:math:`\gamma`      Langevin thermostat                     mass/time
=================== ======================================= ===============


XML Schema
----------

The XML schema for the **Langevin dissipative potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Dissipative-Langevin.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-----------------------------------------+---------------------+---------------------+
| **Parameter Definition**                | **Equation Symbol** | **Schema Notation** |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                   | :math:`i`           | AT-1                |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                   | :math:`j`           | AT-2                |
+-----------------------------------------+---------------------+---------------------+
| Langevin thermostat                     | :math:`\gamma`      | gamma               |
+-----------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ====================================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- --------------------------------------------------------------------
style                  Fixed           Langevin
formula                Fixed           gamma
gamma-units            Required        Enumerations specified in schema
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

1. `Multiscale approach to equilibrating model polymer melts`_.

2. `Liquid XML Studio`_.

.. _Multiscale approach to equilibrating model polymer melts: https://journals.aps.org/pre/abstract/10.1103/PhysRevE.94.032502

.. _Liquid XML Studio: https://www.liquid-technologies.com/

