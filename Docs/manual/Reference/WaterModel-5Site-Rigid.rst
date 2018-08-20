.. _WaterModel-5Site-Rigid:

5Site-Rigid Water Model  
=======================

Functional Form
---------------

The **5Site-Rigid water model** has the functional form:

:math:`E={{E}_{q}}+{{E}_{LJ}}`

or alternatively:

:math:`E=S\left( {{R}_{ij}} \right){{E}_{q}}+{{E}_{LJ}}`

The force-field parameters for this potential and units are given by:

================================== ======================================= ===============
**Equation Symbol**                **Parameter Definition**                **Units**
---------------------------------- --------------------------------------- ---------------
:math:`E_{q}`                      Charge potential energy                 energy
:math:`E_{LJ}`                     Lennard-Jones potential energy          energy
:math:`S\left( {{R}_{ij}} \right)` Switching function                      N/A
================================== ======================================= ===============


XML Schema
----------

The XML schema for the **5Site-Rigid water model** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/WaterModels-5Site-Rigid.png
	:align: center

The general sub-elements (the actual data set) are given by:

+-----------------------------------------+---------------------+
| **Parameter Definition**                | **Schema Notation** |
+-----------------------------------------+---------------------+
| Distance between O and H                | R_OH                |
+-----------------------------------------+---------------------+
| Distance between O and M                | R_OL                |
+-----------------------------------------+---------------------+
| Angle between HOH                       | Theta_HOH           |
+-----------------------------------------+---------------------+
| Angle between LOL                       | Theta_LOL           |
+-----------------------------------------+---------------------+
| Lennard-Jones parameter                 | A                   |
+-----------------------------------------+---------------------+
| Lennard-Jones parameter                 | B                   |
+-----------------------------------------+---------------------+
| Charge of L                             | q_L                 |
+-----------------------------------------+---------------------+
| Charge of H                             | q_H                 |
+-----------------------------------------+---------------------+
|                                         | R_L                 |
+-----------------------------------------+---------------------+
|                                         | R_ij                |
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
formula                Fixed           E=E_q+E_LJ
version                Optional        Version number of parameter set
comment                Optional        Comment attached to data set
A-units                Required        Enumerations specified in schema
B-units                Required        Enumerations specified in schema
R-units                Required        Enumerations specified in schema
Theta-units            Required        Enumerations specified in schema
sigma-units            Required        Enumerations specified in schema
epsilon-units          Required        Enumerations specified in schema
====================== =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified. 

References
----------

1. `SklogWiki page for TIP5P Water Model`_.

2. `Wiki page for Water Model`_.

3. `Liquid XML Studio`_.

.. _SklogWiki page for TIP5P Water Model: http://www.sklogwiki.org/SklogWiki/index.php/TIP5P_model_of_water

.. _Wiki page for Water Model: https://en.wikipedia.org/wiki/Water_model

.. _Liquid XML Studio: https://www.liquid-technologies.com/

