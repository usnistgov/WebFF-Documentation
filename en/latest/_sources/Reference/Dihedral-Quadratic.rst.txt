.. _Dihedral-Quadratic:

Quadratic Dihedral  
==================

Functional Form
---------------

The **quadratic dihedral potential** has the functional form:

:math:`E = {K_{d,ijkl}} \cdot \left( {{\phi_{ijkl}} - {\phi_{0,ijkl}}} \right)^2`

The force-field parameters for this potential and units are given by:

====================== ======================================== ================
**Equation Symbol**      **Parameter Definition**                 **Units**
---------------------- ---------------------------------------- ----------------
:math:`K_{d,ijkl}`     Dihedral coefficient for atoms [i,j,k,l] energy/degrees^2
:math:`\phi_{0,ijkl}`  Equilibrium Dihedral for atoms [i,j,k,l] degrees
====================== ======================================== ================


XML Schema
----------

The XML schema for the **quadratic dihedral potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Dihedral-Quadratic.png
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
| Dihedral coefficient for atoms [i,j,k,l]       | :math:`K_{d,ijkl}`    | Kd                  |
+------------------------------------------------+-----------------------+---------------------+
| Equilibrium dihedral angle for atoms [i,j,k,l] | :math:`\phi_{0,ijkl}` | Phi0                |
+------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Quadratic
formula                Fixed           Kd*(Phi_Phi0)^2
convention             Optional        Enumerations specified in schema
Kd-units               Required        Enumerations specified in schema
Phi0-units             Required        Enumerations specified in schema
====================== =============== =======================================

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

1. `LAMMPS Quadratic Dihedral Potential`_.

2. `GROMACS Quadratic Dihedral Potential`_.

3. `Liquid XML Studio`_.

.. _LAMMPS Quadratic Dihedral Potential: http://lammps.sandia.gov/doc/dihedral_quadratic.html

.. _GROMACS Quadratic Dihedral Potential: http://manual.gromacs.org/documentation/2016.3/manual-2016.3.pdf

.. _Liquid XML Studio: https://www.liquid-technologies.com/

