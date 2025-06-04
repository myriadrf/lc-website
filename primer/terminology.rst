Terminology and Key Functions
=============================

.. toctree::
   :maxdepth: 2
   :hidden:

To give it it’s full title a mobile network is a public land mobile network (PLMN). A historical name which today doesn’t quite reflect the fact that there are now many private cellular networks and those which operate out at sea. Mobile networks are identified by their PLMN ID or code, which is comprised of a Mobile Country Code (MCC) plus a Mobile Network Code (MNC). These should not be confused with dialling codes or number ranges and are instead network identifiers. 

Mobile networks are split at a high level into the radio access network (RAN) and core network. A RAN implements a particular radio access technology (RAT), such as GSM, UMTS, LTE or 5G NR. Most public mobile networks are multi-RAT, which is to say that they simultaneously support multiple radio access technologies, for obvious reasons.

A subscriber is identified by an International Mobile Subscriber Identity (IMSI), the first 4-5 digits of which are the PLMN ID of the subscriber home network. The IMSI, an encryption key and other network parameters are provisioned to both the core network and a SIM card or eSIM. Subscribers will of course be more familiar with the telephone number which they were allocated, or in mobile network parlance, their Mobile Station International Subscriber Directory Number (MSISDN). 

In mobile networks the subscriber device is referred to as the User Equipment (UE) and not mobile phone or similar, since it could equally be a cellular modem or a vehicle tracker etc. The base station meanwhile is named according to the access technology and in 4G networks it’s called an eNodeB, while a 5G base station is a gNodeB. These are sometimes shortened to eNB and gNB.

Cellular spectrum use is strictly regulated and carefully coordinated so as to minimise the risk of interference, with base station equipment configured to use a dedicated radio channel. With 4G networks this is known as the E-UTRA Absolute Radio Frequency Channel Number (EARFCN). 

With LTE the core network is provided by an Evolved Packet Core (EPC) and the equivalent in 5G networks is named the 5G Core (5GC). These are each in turn comprised of multiple network functions, which are designed in such a way as to enable mobile networks to scale to support a very large number of subscribers, and to provide support for features such as roaming.

A mobile network core will provide support for one or more packet data networks (PDNs), which are also configured in the UE and identified by setting the Access Point Name (APN) of the PDN.

We previously mentioned the IMS and how this is used to provide native voice and SMS support in 4G networks onwards. This is based on extensions to SIP, the signalling protocol used to support Voice-over-IP (VoIP) calling. 4G Voice-over-LTE (VoLTE) and 5G Voice-over-NR (VoNR) services are provided by IMS. The same IMS usually also supports SMS and may additionally provide other media services, such as video calling and conferencing.

It should be noted that the IMS is separate to the mobile network core, but depends upon it for access to subscriber records and billing functions. An IMS can also be used to support WiFi calling (VoWiFi), enabling native voice and SMS support in areas without network coverage. 

Voice and SMS support via fallback to 2G/3G is known as circuit-switched fallback (CSFB). This is mentioned as it may come up and answers the question of how voice calling and SMS worked with 4G networks prior to the widespread rollout — and eventual uptake — of VoLTE. However, support for this is not a priority since it would mean also running a 2G network, complete with its own core network and, perhaps more importantly, with it’s own frequency allocation also.

So just to recap:

* **Public Land Mobile Network (PLMN)**. Mobile network.
* **Mobile Country Code (MCC)**. Three digit country code.
* **Mobile Network Code (MNC)**. Two or three digit code unique within the country.
* **PLMN ID**. Mobile network identifier comprised of MCC + MNC.
* **Radio Access Technology (RAT)**. GMS (2G), UMTS (3G), LTE (4G) or 5G NR etc.
* **International Mobile Subscriber Identity (IMSI)**. Unique subscriber identifier.
* **Mobile Station International Subscriber Directory Number (MSISDN)**. Telephone number.
* **User Equipment (UE)**. Handset, cellular modem or other subscriber device.
* **eNodeB**. 4G base station.
* **E-UTRA Absolute Radio Frequency Channel Number (EARFCN)**. Radio channel.
* **Evolved Packet Core (EPC)**. LTE core network.
* **Packet Data Network (PDN)**. Data services network identified by its APN. 
* **IP Multimedia Subsystem (IMS)**. Used to provide native voice and SMS support.
* **Circuit-Switched Fallback (CSFB)**. In the absence of an IMS or with a UE which does not have VoLTE support or this is not configured, falling back to 2G/3G for voice and SMS. 
