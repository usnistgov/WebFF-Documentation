.. _NonBond-EnergyRenorm:

Non-Bond Energy Renormalization Potential  
=========================================

Functional Form
---------------

The **non-bond Energy Renormalization potential** has the functional form:

:math:`E=\left( {{\epsilon }_{A}}-{{\epsilon }_{g}} \right)\left[ \frac{1}{1+{{e}^{-k\left( T-{{T}_{T}} \right)}}} \right]+{{\epsilon }_{g}}`

The force-field parameters for this potential and units are given by:

======================== ============================================= ===============
**Equation Symbol**      **Parameter Definition**                      **Units**
------------------------ --------------------------------------------- ---------------
:math:`{\epsilon }_{A}`  Epsilon value in Arrhenius regime             energy/mol
:math:`{\epsilon }_{g}`  Epsilon value in glassy regime                energy/mol
:math:`k`                Temperature breadth of the transition         N/A
:math:`{T}_{T}`          Crossover point of sigmoidal function         temperature
======================== ============================================= ===============


XML Schema
----------

The XML schema for the **non-bond Energy Renormalization potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/NonBond-EnergyRenorm.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+-------------------------------------------+------------------------------+---------------------+
| **Parameter Definition**                  | **Equation Symbol**          | **Schema Notation** |
+-------------------------------------------+------------------------------+---------------------+
| Atom type of atom [i]                     | (implicit)                   | AT1                 |
+-------------------------------------------+------------------------------+---------------------+
| Atom type of atom [j]                     | (implicit)                   | AT2                 |
+-------------------------------------------+------------------------------+---------------------+
| Epsilon value in Arrhenius regime         | :math:`{\epsilon }_{A}`      | epsilon_A           |
+-------------------------------------------+------------------------------+---------------------+
| Epsilon value in glassy regime            | :math:`{\epsilon }_{g}`      | epsilon_g           |
+-------------------------------------------+------------------------------+---------------------+
| Temperature breadth of the transition     | :math:`k`                    | k_sig               |
+-------------------------------------------+------------------------------+---------------------+
| Exponent of attractive term               | :math:`{\gamma }_{att}`      | n_att               |
+-------------------------------------------+------------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ===========================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- -------------------------------------------
style                  Fixed           Mie
formula                Fixed           C*epsilon*[(sigma/R)^m_rep-(sigma/R)^n_att]
a_ij-units             Required        Enumerations specified in schema
r_c-units              Required        Enumerations specified in schema
====================== =============== ===========================================

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

1. `LAMMPS Mie Pair Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Mie Pair Potential: https://lammps.sandia.gov/doc/pair_mie.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

