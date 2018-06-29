.. _Bond-Harmonic:

Harmonic Bond  
=============

Functional Form
---------------

The **harmonic bond potential** has the functional form:

:math:`E = {K_{ij}} \cdot \left( {{R_{ij}} - {R_{0,ij}}} \right)`

The parameter definitions and the relationship between the equation and XML schema notations are given by:

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

XML Schema
----------

The XML schema for the **harmonic bond potential** has the following representation (design mode representation):

.. image:: ../../images/Bond-Harmonic.png
	:align: left

References
----------

1. `LAMMPS Harmonic Bond Potential`_.

2. `GROMACS Harmonic Bond Potential`_ page 71.

.. _LAMMPS Harmonic Bond Potential: http://lammps.sandia.gov/doc/bond_harmonic.html

.. _GROMACS Harmonic Bond Potential: http://manual.gromacs.org/documentation/2016.3/manual-2016.3.pdf

