Software Installation
=====================

.. toctree::
   :maxdepth: 2
   :hidden:

   minimal
   standard

There are two options when it comes to software installation: minimal and standard configurations. 

The :doc:`minimal` is the quickest way to get up and running. Software is installed via Ubuntu packages or from source and provides only a data service, with a minimal LTE Evolved Packet Core (EPC) where subscribers are provisioned via a CSV file. This configuration may be preferable where only a data service is required, with very basic requirements. It may also be used where there is an existing EPC to connect to and only the eNodeB is required.

The :doc:`standard` is much more complex and is installed using Ansible and Docker containers. This integrates a flexible Home Subscriber Server (HSS), EPC, IP Multimedia Subsystem (IMS), and eNodeB. Subscribers are managed via a RESTful API, there is much more configuration flexibility and the software stack is far more feature rich, with support for Voice-over-LTE (VoLTE) and SMS.
