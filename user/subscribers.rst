Provisioning Subscribers
========================

The Home Subscriber Server (HSS) is a central component of the LTE network. It is responsible for storing subscriber data such as IMSI, MSISDN and security keys. The HSS is used by the MME to authenticate subscribers and to retrieve subscriber data. The HSS is also used by the IMS. 

Not all HSS implementations are created equal and some may support only the minimum features required by an MME in order to provide a data service, while others may also support use with an IMS for VoLTE and SMS services, for example.

The  :doc:`/user/software/minimal` makes use of srsEPC and the HSS provided by this, while the  :doc:`/user/software/standard` utilises PyHSS. Hence the way that subscribers are provisioned and managed will differ between the two configurations.

srsEPC
------

srsEPC is a lightweight implementation of a complete LTE core network (EPC).  The srsEPC application runs as a single binary but provides the key EPC components of Home Subscriber Service (HSS), Mobility Management Entity (MME), Service Gateway (S-GW) and Packet Data Network Gateway (P-GW).

UE Database
^^^^^^^^^^^

Subscribers are provisioned via a CSV file. With the :doc:`/user/software/minimal` this file is located at `/etc/srsran/user_db.csv` and should contain one line per subscriber. The format of the file is as follows:

.. code-block:: bash

   andrew,mil,001010000045391,57c9ff6040528869b72fd823d6b3e656,opc,3787fdb1cdebfdca5fa3d2dfa02422f3,9001,000000000652,7,dynamic

The fields are as follows:

* **Name**. A useful label (not used by srsRAN)
* **Auth**. Authentication algorithm used by the UE.
* **IMSI**. UE's IMSI value.
* **Key**. UE's key (Ki).
* **OP Type**. Operator's code type, either OP or OPc.
* **AMF**. Authentication management field.
* **SQN**. UE's Sequence number for freshness of the authentication.
* **QCI**. QoS Class Identifier for the UE's default bearer.
* **IP alloc**. IP allocation strategy (dynamic or a valid IPv4 for static).

PyHSS
-----

.. figure:: /images/PyHSS_Swagger_1.jpg
   :align: center

PyHSS is a far more sophisticated HSS, supports use with an IMS as well as an MME, and additional features include an Equipment Identity Register (EIR), which can be used to lock SIM cards to a particular device or blacklist a device. It is managed via a RESTful API and unless the :code:`hss.yml` Ansible playbook has been modified, this will be available on port 8080.

To load the Swagger UI for the PyHSS API, open a web browser and navigate to *http://DOCKER_HOST:8080/docs*.

APNs
^^^^

If this is a new installation it will be neccessary to create at least one APN and two if you wish to support VoLTE/SMS.

Select apn -> Create new APN -> Try it out. In the payload section use the below JSON and then select Execute.

.. code-block:: json

   {
     "apn": "internet",
     "apn_ambr_dl": 0,
     "apn_ambr_ul": 0
   }

Take note of *apn_id* specified in the *Response body* under *Server response* for *internet* APN.

Then repeat the above step, but this time using the JSON payload:

.. code-block:: json

   {
     "apn": "ims",
     "apn_ambr_dl": 0,
     "apn_ambr_ul": 0
   }

Take note of *apn_id* specified in the *Response body* under *Server response* for *ims* APN.

Since these are the first created, the *apn_ids* are likely to be *1* and *2*.

Subscribers
^^^^^^^^^^^

In order to provision subscribers we need to first create a new AuC object, which is used to store the subscriber's security keys, before then creating a basic subscriber and an IMS subscriber. This last step can obviously be omitted if we don't have an IMS or the subscriber should not receive VoLTE/SMS service.

Select auc -> Create new AUC -> Try it out. In the payload section use the below example JSON, taking care to update ki, opc and imsis for your SIM, then select Execute.

.. code-block:: json

   {
     "ki": "57c9ff6040528869b72fd823d6b3e656",
     "opc": "3787fdb1cdebfdca5fa3d2dfa02422f3",
     "amf": "9001",
     "sqn": 0,
     "imsi": "001010000048862"
   }

Take note of *auc_id* specified in Response body under Server response.

Next select subscriber -> Create new SUBSCRIBER -> Try it out. In the payload section use the below example JSON, taking care to update the imsi, auc_id (from the previous step), default_apn and apn_list (from APN creation steps) for your SIM and then select Execute.

.. code-block:: json

   {
     "imsi": "001010000048862",
     "enabled": true,
     "auc_id": 1,
     "default_apn": 1,
     "apn_list": "1,2",
     "msisdn": "48862",
     "ue_ambr_dl": 0,
     "ue_ambr_ul": 0
   }

Finally, select ims_subscriber -> Create new IMS SUBSCRIBER -> Try it out. In the payload section use the below example JSON, taking care to to update the imsi, msisdn and msisdn_list for your SIM and then select Execute.

.. code-block:: json

   {
     "imsi": "001010000048862",
     "msisdn": "48862",
     "sh_profile": "string",
     "scscf_peer": "scscf.ims.mnc001.mcc001.3gppnetwork.org",
     "msisdn_list": "[48862]",
     "ifc_path": "default_ifc.xml",
     "scscf": "sip:scscf.ims.mnc001.mcc001.3gppnetwork.org:6060",
     "scscf_realm": "ims.mnc001.mcc001.3gppnetwork.org"
   }

