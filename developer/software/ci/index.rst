CI Software
===========

The CI pipeline is driven by Jenkins and `OsmoGSMTester`_, a python-based framework which enables control of base stations, modems and other CI platform hardware, such as digitally controlled RF attenuation. 

CI test configuration is based heavily on that used by the `Osmocom Cellular Network Infrastructure`_ (CNI) project, which OsmoGSMTester is developed as part of and where it is used for testing GSM network software.

*With thanks to the Osmocom project and sysmocom for creating OsmoGSMTester and publishing CI configuration*.

Phase 1 Commissioning
---------------------

.. figure:: /images/osmo-gsm-tester_run-prod-111022.png
   :align: center

At this point the CI platform has been validated with a simple test configuration which:

1. Clones srsRAN with native LMS API support and builds this
2. Deploys software binaries plus eNodeB and EPC configuration to CIRAN1
3. Starts a self-contained LTE network with a single subscriber provisioned
4. Attaches a CIMODS8 modem to the LTE network
5. Executes a ping test to confirm end-to-end operation 

The above screenshot shows a network run and ping test passing, with this Jenkins project depending upon an earlier build project execution.

.. figure:: /images/osmo-gsm-tester_jobs-111022.png
   :align: center

*Note that some configuration still needs updating to replace "GSM" with "LTE" and "srslte" with "srsran".*

Resources
---------

Detailed documentation will be provided in due course, but in the meantime links are provided to software and configurations used.

* OsmoGSMTester: https://github.com/myriadrf/osmo-gsm-tester/tree/lc/main
 
  * Includes updates for more recent srsRAN version, LMS API support and others.

* Ofono: https://github.com/myriadrf/ofono/tree/osmo-gsm-tester

  * Mirror of sysmocom Ofono fork with patch to enable working with network namespaces. It's possible this will need additional patching in future.

* CI scripts: https://github.com/myriadrf/lc-ci/tree/lc/main

  * Fork of osmo-ci, with updates to reflect LibreCellular hardware and test requirements.

* srsRAN: https://github.com/myriadrf/srsRAN/tree/native_lime_22.04

  * Fork of srsRAN with native LMS API support (no SoapySDR layer)

Next steps
----------

The next steps include re-deploying software components using Ansible and Docker, since so far this has been manually installed and configured, and run without any containerisation.

Once sufficient familiarity has been gained with the software, decisions will need to be made regarding contributing patches upstream. For example, this may be appropriate with general fixes or improvements, but not with configuration which is specific to the CI hardware platform. 

.. _OsmoGSMTester: https://osmocom.org/projects/osmo-gsm-tester
.. _Osmocom Cellular Network Infrastructure: https://osmocom.org/projects/cellular-infrastructure


