CONIO
=====

CONIO-A
-------

.. figure:: /images/CONIO-A_1280w.jpg

Remote console, reset and power control — controller (A) end.

This board is used in the :doc:`/developer/hardware/cicon` test controller and it connects to the APU2E4 single board computer (SBC). It provides 3x ports for connecting to SDR base stations, each carrying console serial and power/reset control, plus a fourth passthrough port for the SBC console.

The board design can be found in the `lc-conio repo`_.

CONIO-B
-------

.. figure:: /images/CONIO-B_1280w.jpg

Remote console, reset and power control — base station  (B) end.

This board is installed in the SDR base stations and interfaces with its SBC,
e.g. Intel NUC.

The board design can be found in the `lc-conio repo`_.

.. _lc-conio repo: https://github.com/myriadrf/lc-conio