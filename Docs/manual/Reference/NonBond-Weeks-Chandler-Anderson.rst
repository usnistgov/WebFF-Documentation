.. _NonBond-Weeks-Chandler-Anderson:

Non-Bond Weeks-Chandler-Anderson Potential  
==========================================

Functional Form
---------------

The **non-bond Weeks-Chandler-Anderson potential** has the functional form:

:math:`E=4\epsilon \left[ {{\left( \frac{{{\sigma }_{ij}}}{{{R}_{ij}}} \right)}^{12}}-{{\left( \frac{{{\sigma }_{ij}}}{{{R}_{ij}}} \right)}^{12}}+\frac{1}{4} \right]`

The force-field parameters for this potential and units are given by:

=================== ============================================= ===============
**Equation Symbol** **Parameter Definition**                      **Units**
------------------- --------------------------------------------- ---------------
:math:`\epsilon`    Potential well depth for atom [i]             energy/mol
:math:`\sigma`      Interatomic cut-off distance for atom [i]     length
=================== ============================================= ===============


XML Schema
----------

The XML schema for the **non-bond Weeks-Chandler-Anderson potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-Weeks-Chandler-Anderson.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-------------------------------------------+---------------------+---------------------+
| **Parameter Definition**                  | **Equation Symbol** | **Schema Notation** |
+-------------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                     | (implicit)          | AT-1                |
+-------------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                     | (implicit)          | AT-2                |
+-------------------------------------------+---------------------+---------------------+
| Potential well depth for atom [i]         | :math:`\epsilon`    | epsilon             |
+-------------------------------------------+---------------------+---------------------+
| Interatomic cut-off distance for atom [i] | :math:`\sigma`      | sigma               |
+-------------------------------------------+---------------------+---------------------+
| Interatomic cut-off distance for atom [i] | N/A                 | r_cut               |
+-------------------------------------------+---------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ================================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ------------------------------------------------
style                  Fixed           Weeks-Chandler-Anderson
formula                Fixed           4*epsilon*[((sigma/R)^-12)-((sigma/R)^-6)+(1/4)]
epsilon-units          Required        Enumerations specified in schema
sigma-units            Required        Enumerations specified in schema
====================== =============== ================================================

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

1. `The Journal of Chemical Physics 54, 5237 (1971); doi 10.1063/1.1674820`_.

2. `Liquid XML Studio`_.

.. _The Journal of Chemical Physics 54, 5237 (1971); doi 10.1063/1.1674820: https://aip.scitation.org/doi/pdf/10.1063/1.1674820/

.. _Liquid XML Studio: https://www.liquid-technologies.com/

