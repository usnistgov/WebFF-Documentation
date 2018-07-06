.. _Dihedral-Class2:

Class 2 Dihedral  
==================

Functional Form
---------------

The **class 2 dihedral potential** has the functional form:

:math:`E={{K}_{1,ijkl}}\left[ 1-\cos \left( {{\phi }_{ijkl}}-{{\phi }_{1,ijkl}} \right) \right]+{{K}_{2,ijkl}}\left[ 1-\cos \left( 2{{\phi }_{ijkl}}-{{\phi }_{2,ijkl}} \right) \right]`
:math:`\qquad +{{K}_{3,ijkl}}\left[ 1-\cos \left( 3{{\phi }_{ijkl}}-{{\phi }_{3,ijkl}} \right) \right]`

The force-field parameters for this potential and units are given by:

====================== ======================================== ================
**Equation Symbol**      **Parameter Definition**                 **Units**
---------------------- ---------------------------------------- ----------------
:math:`K_{1,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`K_{2,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`K_{3,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`\phi_{1,ijkl}`  Equilibrium Dihedral for atoms [i,j,k,l] degrees
:math:`\phi_{2,ijkl}`  Equilibrium Dihedral for atoms [i,j,k,l] degrees
:math:`\phi_{3,ijkl}`  Equilibrium Dihedral for atoms [i,j,k,l] degrees
====================== ======================================== ================


XML Schema
----------

The XML schema for the **class 2 dihedral potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Dihedral-Class2.png
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
| Dihedral coefficient for atoms [i,j,k,l]       | :math:`K_{1,ijkl}`    | K1                  |
+------------------------------------------------+-----------------------+---------------------+
| Dihedral coefficient for atoms [i,j,k,l]       | :math:`K_{2,ijkl}`    | K2                  |
+------------------------------------------------+-----------------------+---------------------+
| Dihedral coefficient for atoms [i,j,k,l]       | :math:`K_{3,ijkl}`    | K3                  |
+------------------------------------------------+-----------------------+---------------------+
| Equilibrium dihedral angle for atoms [i,j,k,l] | :math:`\phi_{1,ijkl}` | Phi1                |
+------------------------------------------------+-----------------------+---------------------+
| Equilibrium dihedral angle for atoms [i,j,k,l] | :math:`\phi_{2,ijkl}` | Phi2                |
+------------------------------------------------+-----------------------+---------------------+
| Equilibrium dihedral angle for atoms [i,j,k,l] | :math:`\phi_{3,ijkl}` | Phi3                |
+------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ==================================================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- ------------------------------------------------------------------
style                  Fixed           Class2
formula                Fixed           K1*[1-cos(Phi-Phi1)]+K2*[1-cos(2*Phi-Phi2)]+K3*[1-cos(3*Phi-Phi3)]
convention             Optional        Enumerations specified in schema
Kn-units               Required        Enumerations specified in schema
Phin-units             Required        Enumerations specified in schema
====================== =============== ==================================================================

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

1. `LAMMPS Class 2 Dihedral Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Class 2 Dihedral Potential: http://lammps.sandia.gov/doc/dihedral_class2.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

