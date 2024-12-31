Reference Hardware
==================

.. toctree::
   :maxdepth: 2
   :hidden:

   lab
   csran1

The LibreCellular project uses software-defined radio (SDR) for the LTE eNodeB (radio base station) and in particular the focus is on supporting the LimeSDR family of boards. However, it should be possible to use other SDR hardware which is supported by the srsRAN 4G project. 

An eNodeB is much more than just the SDR and along with this typically integrates a host computer, RF front-end (RFE) and filtering. The specifications for which may vary depending upon things such as the bandwidth, frequency band and RF power, which determines the range/coverage.

Reference hardware designs are provided for convenience, but should be considered as a starting point and may be modified to suit specific requirements.

- :doc:`lab`. A simple lab setup for testing and development.
- :doc:`csran1`. A more advanced LTE-FDD base station design.