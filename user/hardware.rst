Reference Hardware
==================

.. figure:: /images/RHP_0p1_1.jpg
   :align: center

The current Reference Hardware Platform is comprised of:

* `Intel NUC11TNHi5`_
* `LimeSDR-USB`_
* `Leo Bodnar Mini Precision GPS Reference Clock`_
* `sysmocom 1800 MHz 30W duplexer`_

GPSDO setup
-----------

.. figure:: /images/Leo_Bodnar_Mini_GPS_Configuration.jpg
   :align: center

The GPS reference needs to be configured before use and a Windows utility can be downloaded from the Leo Bodnar website.

The GPSDO should be configured with:

* 10000000 Hz output frequency
* 32mA output drive strength

Connection
----------

A block diagram can be seen below.

.. figure:: /images/RHP_0p1_Block_Diagram.svg
   :align: center

The Mini GPS Reference is powered via USB and this can be cabled to a NUC USB port, along with the SDR.

.. figure:: /images/Leo_Bodnar_Mini_GPS_Locked.jpg
   :align: center

The GPS reference is locked when its LED is constant and not flashing.

Minimal configuration
---------------------

It is possible to have a configuration:

#. Without a GPSDO
#. Without a duplexer

However, this will impact performance. 

Without a GPS locked external reference there may be sufficient frequency error to result in network instability. 

Without a duplexer there would be two antennas, one connected to receive and another to transmit. Such use will result in reduced RF performance, as there will be no receive filtering, meaning that the base station transmit signal may cause receive interference, along with any other out-of-band signals. Meanwhile the transmit output will not be filtered.


.. _Intel NUC11TNHi5: https://www.intel.co.uk/content/www/uk/en/products/sku/205594/intel-nuc-11-pro-kit-nuc11tnhi5/specifications.html
.. _LimeSDR-USB: https://wiki.myriadrf.org/LimeSDR-USB
.. _Leo Bodnar Mini Precision GPS Reference Clock: http://www.leobodnar.com/shop/index.php?main_page=product_info&products_id=301
.. _sysmocom 1800 MHz 30W duplexer: https://shop.sysmocom.de/1800-MHz-DCS-UMTS-LTE-Band-3-duplexer-30W/dx1800-kt30
