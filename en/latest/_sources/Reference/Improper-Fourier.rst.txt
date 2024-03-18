.. _Improper-Fourier:

Fourier Improper  
==================

Functional Form
---------------

The **Fourier improper potential** has the functional form:

:math:`E={{K}_{i,ijkl}}\left[ {{C}_{0,ijkl}}+{{C}_{1,ijkl}}\cos \left( {{\omega }_{ijkl}} \right)+{{C}_{2,ijkl}}\cos \left( 2{{\omega }_{ijkl}} \right) \right]`

The force-field parameters for this potential and units are given by:

====================== ============================================== ================
**Equation Symbol**      **Parameter Definition**                     **Units**
---------------------- ---------------------------------------------- ----------------
:math:`K_{i,ijkl}`     Improper coefficient for atoms [i,j,k,l]       energy
:math:`C_{0,ijkl}`     Real coefficient for cosine term #0 [i,j,k,l]  N/A
:math:`C_{1,ijkl}`     Real coefficient for cosine term #1 [i,j,k,l]  N/A
:math:`C_{2,ijkl}`     Real coefficient for cosine term #2 [i,j,k,l]  N/A
====================== ============================================== ================


XML Schema
----------

The XML schema for the **Fourier improper potential** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/Improper-Fourier.png
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
| Improper coefficient for atoms [i,j,k,l]       | :math:`K_{i,ijkl}`    | Ki                  |
+------------------------------------------------+-----------------------+---------------------+
| Real coefficient for cosine term #0 [i,j,k,l]  | :math:`C_{0,ijkl}`    | C0                  |
+------------------------------------------------+-----------------------+---------------------+
| Real coefficient for cosine term #1 [i,j,k,l]  | :math:`C_{1,ijkl}`    | C1                  |
+------------------------------------------------+-----------------------+---------------------+
| Real coefficient for cosine term #2 [i,j,k,l]  | :math:`C_{2,ijkl}`    | C2                  |
+------------------------------------------------+-----------------------+---------------------+

The general attributes (describing the entire data set) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value**               
---------------------- --------------- ---------------------------------------
style                  Fixed           Fourier
formula                Fixed           Ki*[C0+C1*cos(w)+C2*cos(2*w)]
convention             Optional        Enumerations specified in schema
Ki-units               Required        Enumerations specified in schema
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

1. `LAMMPS Fourier Improper Potential`_.

2. `Liquid XML Studio`_.

.. _LAMMPS Fourier Improper Potential: http://lammps.sandia.gov/doc/improper_fourier.html

.. _Liquid XML Studio: https://www.liquid-technologies.com/

