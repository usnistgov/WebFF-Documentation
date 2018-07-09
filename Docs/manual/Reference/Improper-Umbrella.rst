.. _Improper-Umbrella:

Umbrella Improper  
==================

Functional Form
---------------

The **umbrella improper potential** has the functional form:

:math:`E=\left\{ \begin{align} & \frac{1}{2}{{K}_{i,ijkl}}{{\left[ \frac{1+\cos \left( {{\omega }_{0,ijkl}} \right)}{\sin \left( {{\omega }_{0,ijkl}} \right)} \right]}^{2}}\left[ \cos \left( {{\omega }_{ijkl}} \right)-\cos \left( {{\omega }_{0,ijkl}} \right) \right],\text{ if }{{\omega }_{0,ijkl}}\ne 0 \\  & {{K}_{i,ijkl}}\left[ 1-\cos \left( {{\omega }_{ijkl}} \right) \right],\text{ if }{{\omega }_{0,ijkl}}=0 \\ \end{align} \right.`

The force-field parameters for this potential and units are given by:

======================= ============================================== ================
**Equation Symbol**      **Parameter Definition**                     **Units**
----------------------- ---------------------------------------------- ----------------
:math:`K_{i,ijkl}`      Improper coefficient for atoms [i,j,k,l]       energy
:math:`\omega_{0,ijkl}` Equilibrium improper angle for atoms [i,j,k,l] degrees
======================= ============================================== ================


XML Schema
----------

The XML schema for the **umbrella improper potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Improper-Umbrella.png
	:align: left

The relationship between the equation symbols and XML schema notations are given by:

+------------------------------------------------+-------------------------+---------------------+
| **Parameter Definition**                       | **Equation Symbol**     | **Schema Notation** |
+------------------------------------------------+-------------------------+---------------------+
| Atom type of atom [i]                          | :math:`i`               | AT-1                |
+------------------------------------------------+-------------------------+---------------------+
| Atom type of atom [j]                          | :math:`j`               | AT-2                |
+------------------------------------------------+-------------------------+---------------------+
| Atom type of atom [k]                          | :math:`k`               | AT-3                |
+------------------------------------------------+-------------------------+---------------------+
| Atom type of atom [l]                          | :math:`l`               | AT-4                |
+------------------------------------------------+-------------------------+---------------------+
| Improper coefficient for atoms [i,j,k,l]       | :math:`K_{i,ijkl}`      | Ki                  |
+------------------------------------------------+-------------------------+---------------------+
| Equilibrium improper angle for atoms [i,j,k,l] | :math:`\omega_{0,ijkl}` | w0                  |
+------------------------------------------------+-------------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== ===============================================================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- -------------------------------------------------------------------------------
style                  Fixed           Umbrella
formula                Fixed           0.5*K*[{1+cos(w0)}/sin(w0)]^2*[cos(w)-cos(w0)], w0 ≠ 0°; K*[1-cos(w)],  w0 = 0°
convention             Optional        Enumerations specified in schema
Ki-units               Required        Enumerations specified in schema
w0-units               Required        Enumerations specified in schema
====================== =============== ===============================================================================

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

1. `LAMMPS Umbrella Improper Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Umbrella Improper Potential: http://lammps.sandia.gov/doc/improper_umbrella.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

