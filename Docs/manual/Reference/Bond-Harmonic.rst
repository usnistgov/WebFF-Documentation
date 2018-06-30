.. _Bond-Harmonic:

Harmonic Bond  
=============

Functional Form
---------------

The **harmonic bond potential** has the functional form:

:math:`E = {K_{ij}} \cdot \left( {{R_{ij}} - {R_{0,ij}}} \right)`

The parameters and units are given by:

=================== ======================================= ===============
**Equation Symbol** **Parameter Definition**                **Units**
------------------- --------------------------------------- ---------------
:math:`K_{ij}`      Bond coefficient for atoms [i,j]        energy/length^2
:math:`R_{0,ij}`    Equilibrium bond length for atoms [i,j] length
=================== ======================================= ===============


XML Schema
----------

The XML schema for the **harmonic bond potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Bond-Harmonic.png
	:align: left

The parameter definitions and the relationship between the equation symbols and XML schema notations are given by:

+-----------------------------------------+---------------------+---------------------+
| **Parameter Definition**                | **Equation Symbol** | **Schema Notation** |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [i]                   | :math:`i`           | AT-1                |
+-----------------------------------------+---------------------+---------------------+
| Atom type of atom [j]                   | :math:`j`           | AT-2                |
+-----------------------------------------+---------------------+---------------------+
| Bond coefficient for atoms [i,j]        | :math:`K_{ij}`      | K                   |
+-----------------------------------------+---------------------+---------------------+
| Equilibrium bond length for atoms [i,j] | :math:`R_{0,ij}`    | R0                  |
+-----------------------------------------+---------------------+---------------------+


References
----------

1. `LAMMPS Harmonic Bond Potential`_.

2. `GROMACS Harmonic Bond Potential`_ page 71.

3. `Liquid XML Studio`_.

.. _LAMMPS Harmonic Bond Potential: http://lammps.sandia.gov/doc/bond_harmonic.html

.. _GROMACS Harmonic Bond Potential: http://manual.gromacs.org/documentation/2016.3/manual-2016.3.pdf

.. _Liquid XML Studio: https://www.liquid-technologies.com/

