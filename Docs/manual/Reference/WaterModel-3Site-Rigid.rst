.. _WaterModel-3Site-Rigid:

3Site-Rigid Water Model  
=======================

Functional Form
---------------

The **3Site-Rigid water model** has the functional form:

:math:`E={{E}_{q}}+{{E}_{LJ}}`

or alternatively:

:math:`E={{E}_{q}}+{{E}_{LJ}}+{{E}_{pol}}`

The force-field parameters for this potential and units are given by:

=================== ======================================= ===============
**Equation Symbol** **Parameter Definition**                **Units**
------------------- --------------------------------------- ---------------
:math:`E_{q}`       Charge potential energy                 energy
:math:`E_{LJ}`      Lennard-Jones potential energy          energy
:math:`E_{pol}`     Average polarization correction         energy
=================== ======================================= ===============


XML Schema
----------

The XML schema for the **3Site-Rigid water model** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/WaterModels-3Site-Rigid.png
	:align: center

The general sub-elements (the actual data set) are given by:

+-----------------------------------------+---------------------+
| **Parameter Definition**                | **Schema Notation** |
+-----------------------------------------+---------------------+
| Distance between O and H                | R_OH                |
+-----------------------------------------+---------------------+
| Angle between HOH                       | Theta_HOH           |
+-----------------------------------------+---------------------+
| Lennard-Jones parameter                 | A                   |
+-----------------------------------------+---------------------+
| Lennard-Jones parameter                 | B                   |
+-----------------------------------------+---------------------+
| Charge of O                             | q_O                 |
+-----------------------------------------+---------------------+
| Charge of H                             | q_H                 |
+-----------------------------------------+---------------------+
|                                         | EnergyDispersion    |
+-----------------------------------------+---------------------+
|                                         | sigma               |
+-----------------------------------------+---------------------+
|                                         | epsilon             |
+-----------------------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
name                   Required        The name
formula                Fixed           E=E_q+E_LJ | E=E_q+E_LJ+E_pol
version                Optional        Version number of parameter set
comment                Optional        Comment attached to data set
R_OH-units             Required        Enumerations specified in schema
Theta_HOH-units        Required        Enumerations specified in schema
A-units                Required        Enumerations specified in schema
B-units                Required        Enumerations specified in schema
sigma-units            Required        Enumerations specified in schema
epsilon-units          Required        Enumerations specified in schema
====================== =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified. 

References
----------

1. `SklogWiki page for TIP3P Water Model`_.

2. `Wiki page for Water Model`_.

3. `Liquid XML Studio`_.

.. _SklogWiki page for TIP3P Water Model: http://www.sklogwiki.org/SklogWiki/index.php/TIP3P_model_of_water

.. _Wiki page for Water Model: https://en.wikipedia.org/wiki/Water_model

.. _Liquid XML Studio: https://www.liquid-technologies.com/

