.. _Improper-CHARMM

CHARMM Improper  
==================

Functional Form
---------------

The **CHARMM improper potential** has the functional forms:

:math:`E={{K}_{d,ijkl}}\left[ 1+\cos \left( N{{\phi }_{ijkl}}-{{\phi }_{0,ijkl}} \right) \right]`

:math:`E={{K}_{d,ijkl}}\left[ 1+\cos \left( N{{\phi }_{ijkl}}+{{\phi }_{0,ijkl}} \right) \right]`

The force-field parameters for this potential and units are given by:

====================== ============================================== ================
**Equation Symbol**      **Parameter Definition**                     **Units**
---------------------- ---------------------------------------------- ----------------
:math:`K_{d,ijkl}`     Improper coefficient for atoms [i,j,k,l]       energy
:math:`N`              Nonnegative integer coefficient                N/A
:math:`\phi_{0,ijkl}`  Equilibrium improper angle for atoms [i,j,k,l] degrees
====================== ============================================== ================


XML Schema
----------

The XML schema for the **CHARMM improper potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Improper-CHARMM.png
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
| Improper coefficient for atoms [i,j,k,l]       | :math:`K_{d,ijkl}`    | Kd                  |
+------------------------------------------------+-----------------------+---------------------+
| Nonnegative integer coefficient                | :math:`N`             | N                   |
+------------------------------------------------+-----------------------+---------------------+
| Equilibrium improper angle for atoms [i,j,k,l] | :math:`\phi_{0,ijkl}` | Phi0                |
+------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ==============================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- ----------------------------------------------
style                  Fixed           CHARMM
formula                Fixed           Kd*[1+cos(N*Phi-Phi0)], Kd*[1+cos(N*Phi+Phi0)]
convention             Optional        Enumerations specified in schema
Kd-units               Required        Enumerations specified in schema
Phi0-units             Required        Enumerations specified in schema
====================== =============== ==============================================

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

1. `Liquid XML Studio`_.

.. _Liquid XML Studio: https://www.liquid-technologies.com/

