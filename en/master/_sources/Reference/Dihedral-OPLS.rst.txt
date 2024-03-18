.. _Dihedral-OPLS:

OPLS Dihedral  
==================

Functional Form
---------------

The **OPLS dihedral potential** has the functional forms:

:math:`E=\frac{1}{2}{{K}_{1,ijkl}}\left[ 1+\cos \left( {{\phi }_{ijkl}} \right) \right]+\frac{1}{2}{{K}_{2,ijkl}}\left[ 1-\cos \left( 2{{\phi }_{ijkl}} \right) \right]+\frac{1}{2}{{K}_{3,ijkl}}\left[ 1+\cos \left( 3{{\phi }_{ijkl}} \right) \right]`
:math:`\qquad +\frac{1}{2}{{K}_{4,ijkl}}\left[ 1-\cos \left( 4{{\phi }_{ijkl}} \right) \right]`

The force-field parameters for this potential and units are given by:

====================== ======================================== ================
**Equation Symbol**      **Parameter Definition**                 **Units**
---------------------- ---------------------------------------- ----------------
:math:`K_{1,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`K_{2,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`K_{3,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
:math:`K_{4,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy
====================== ======================================== ================


XML Schema
----------

The XML schema for the **OPLS dihedral potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Dihedral-OPLS.png
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
| Dihedral coefficient for atoms [i,j,k,l]       | :math:`K_{4,ijkl}`    | K4                  |
+------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ===========================================================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- ---------------------------------------------------------------------------
style                  Fixed           OPLS
formula                Fixed           0.5*{K1*[1+cos(Phi)]+K2*[1-cos(2*Phi)]+K3*[1+cos(3*Phi)]+K4*[1-cos(4*Phi)]}
convention             Optional        Enumerations specified in schema
Kn-units               Required        Enumerations specified in schema
====================== =============== ===========================================================================

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

1. `LAMMPS OPLS Dihedral Potential`_.

2. `GROMACS OPLS Dihedral Potential`_ page 81.

3. `Liquid XML Studio`_.

.. _LAMMPS OPLS Dihedral Potential: http://lammps.sandia.gov/doc/dihedral_opls.html

.. _GROMACS OPLS Dihedral Potential: http://manual.gromacs.org/documentation/2016.3/manual-2016.3.pdf

.. _Liquid XML Studio: https://www.liquid-technologies.com/

