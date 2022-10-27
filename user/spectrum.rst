Spectrum Licensing
==================

In most parts of the world a spectrum licence will be required in order to operate an LTE network. Fortunately, while such licences were previously limited to a handful of network operators who paid huge sums for exclusive spectrum access, there are increasily schemes available which provide shared access at a relatively low cost. Examples of which include Ofcom Shared Access spectrum in the UK and CBRS band in the US.

The initial focus is on configutation for LTE Band 3 (1800 MHz) and the Ofcom Shared Access 3.3 MHz (x2 for uplink + downlink) allocation within this. Documentation will be updated over time to add details of licensing schemes in other countries. 

.. danger::
   LTE networks operate in licensed spectrum and operating equipment without a licence from the regulatory authority in your country is likely to be a crime punishable under applicable law.

Ofcom Shared Access (UK)
------------------------

`Ofcom Shared Access licenses`_ are currently available for the following bands:

* 1800 MHz band: 1781.7 to 1785 MHz paired with 1876.7 to 1880 MHz.
* 2300 MHz band: 2390 to 2400 MHz.
* 3800 to 4200 MHz band.
* 24.25-26.5 GHz. 

The only allocation of interest to us at present is in the 1800 MHz band, a.k.a. LTE Band 3. However, the 3800 to 4200 MHz band may also be of interest in future with 5G support. 

Note that the srsRAN stack does support 5G, but it would be a matter of appropriate hardware and software configuration, plus testing etc. 

Licenses are available in two variants:

* **Low power licence (24dBm EIRP max)**. This authorises users to deploy as many base stations as they require within a circular area with a radius of 50 metres as well as the associated fixed, nomadic or mobile terminals connected to the base stations operating within the area.
* **Medium power licence (42dBm EIRP max)**. This authorises a single base station and the associated fixed, nomadic or mobile terminals connected to the base station.

However, medium power licences are usually only available in rural designated areas. These are defined as:

* any location in England or Wales in an ONS 2011 Census Output Area which falls into categories D1, D2, E1, E2, F1 or F2 (i.e. “town and fringe” “villages” and “hamlets and isolated dwellings”);
* any location in Scotland which falls into categories 3-8 based on the Scottish Government's 8-fold Urban Rural Classification; and
* any location in Northern Ireland which falls into bands E-H of the Northern Ireland Statistics and Research Agency's settlement classification bands.

Rural-urban classification information is available from the `Office for National Statistics`_, but this is not the easiest to navigate. In any case, while an :doc:`/developer/hardware/rf/b3mpa` is in development, the current focus is on low power use and this is also perhaps the most practical.

Submitting an application
^^^^^^^^^^^^^^^^^^^^^^^^^

An application form can be downloaded from the Ofcom website linked above. The current cost for an 1800 MHz spectrum licence (3.3 MHz x 2 channel) is £80 per year/site. It can typically take anywhere from 4 - 8 weeks on average for an application to be processed.

The first two sections — *A. Applicaton purpose* and *B. Applicant details* — are self-explanatory. Note that licences can be issued to individuals or organisations, and numerous contact details sub-sections, e.g. those marked *where different from above*, can usually be left empty.

Section *C. Licence variation* is for changes to a previous licence and is usually left blank.

Section *D. Station details* is obviously important. The Grid Reference for *D.1 Site location* can be looked up via websites such as `UK Grid Reference Finder`_. While *D.3 Station name and address* should also correspond to the same location.

Section *E. Technical details - Low power use* should be completed as follows:

* *E.1a*. Leave empty.
* *E.1b*. Tick 1.8 GHz.
* *E.2*. Enter the antenna height above ground level.

Ignore section *F. Technical details - Medium (rural) power use*.

Enter appropriate details for section *G. Intended Use*. For example, "Spectrum will be used to operate a private LTE network."

.. note::
   A Medium Power licence may be applied for instead, but this would require entering additional details, such as the transmit power EIRP (max 42dBm) and receiver antenna gain. 
   
   We also would not recommend using the current LibreCellular configuration with a medium power RF amplifier, until further testing, measurement and optimisation has been carried out. 
   
.. _Ofcom Shared Access licenses: https://www.ofcom.org.uk/manage-your-licence/radiocommunication-licences/shared-access
.. _Office for National Statistics: https://www.ons.gov.uk/methodology/geography/geographicalproducts/ruralurbanclassifications/2011ruralurbanclassification
.. _UK Grid Reference Finder: https://gridreferencefinder.com/