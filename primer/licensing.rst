Spectrum Licensing
==================

.. toctree::
   :maxdepth: 2
   :hidden:

The frequency bands available for private networks and the conditions attached to their usage vary from country to country. Therefore it is important to check what bands are available and the permitted RF power levels prior to assembling a system. Furthermore, licensing schemes may operate on a first come, first served basis and with limited spectrum available in areas such as cities. So in some cases it may be prudent to make an application before investing in equipment. 

Licences may also be provided for different classes of operation, such as low or medium power, which would impact the effective range. Unfortunately, there is no simple calculation for RF power vs. range and this depends upon additional factors such as the frequency band, channel bandwidth, SISO vs. MIMO, antenna type, and the radio environment made up of buildings, trees and other objects resulting in signals being attenuated and reflected. 

Conditions
----------

Some of the conditions which may be attached to a cellular spectrum licence are as follows:

**Geographical location**

This may be fixed coordinates or within some radius of a specified location.

**Deployment location**

Indoors or outdoors and with either of these the antenna height above ground may need to be specified, with effective limits on this also.

**Transmit channel centre frequency**

Allocated centre frequency for transmit (downlink).

**Receive channel centre frequency**

Allocated centre frequency for receive (uplink). Note that with FDD bands downlink and uplink will be on different frequencies, whereas with TDD bands the same frequency is used with both.

**Channel bandwidth**

The permitted RF channel bandwidth.

**Maximum power**

This is usually specified in terms of the equivalent isotropically radiated power (EIRP), which takes into account antenna cable losses and antenna gains. See the RF Basics section for further details.

**Synchronisation**

In some cases a synchronisation requirement may be specified, so as to reduce the possibility of interference with those operating networks in adjacent bands. This might involve ensuring that an eNodeB is configured to use a particular framing structure and with alignment to the UTC second boundary, which could be achieved using GNSS/GPS. Though such requirements are less common.

Example Schemes
---------------

Details of some example licensing schemes is provided below, but this is by no means comprehensive information and since they vary from country to country and are updated over time, for authoritative details please consult the website of your wireless regulatory body. 

When checking for available spectrum take care to ensure that it is compatible with your intended use. For example, while 1800 MHz spectrum can be used with 2G, 3G, 4G and 5G networks, a 3 MHz allocation would only be compatible with 2G and 4G network usage, since 3G networks use a 5 MHz wide channel, and with 5G the minimal channel bandwidth is 5 MHz.

United Kingdom
++++++++++++++

The UK wireless regulator has made a number of cellular bands available for use with private and community networks via its Shared Access scheme. This includes the aforementioned 1800 MHz allocation, along with spectrum in the 2300 MHz, 3.8-4.2 GHz and 26 GHz bands. Low and medium power licences are available, with the latter enabling much greater coverage, albeit with certain restrictions and being aimed more at use in rural areas. Licences are priced based on the amount of spectrum required and at the time of writing this starts at £80/site/year.

For further details see the Ofcom website.

Netherlands
+++++++++++

For some time it’s been possible in the Netherlands to operate private cellular networks which take advantage of 5 MHz of license exempt spectrum in the 1800 MHz band. Which is to say that no paperwork, permission or payment is required. An obvious downside to this is that spectrum is not dedicated and usage may be contended, but it sets a very low barrier to access and with a transmit power limit of 200mW EIRP, contention shouldn’t be a frequent problem, while still providing reasonable coverage. Spectrum has also been made available in the 3.6 GHz band for private 5G networks, although it appears as though this may be aimed at larger enterprise users.

For further details see the Rijksinspectie Digitale Infrastructuur website.

United States of America
++++++++++++++++++++++++

The USA has made provision for a significant amount of shared spectrum via the Citizens Broadband Radio Service (CBRS) band, a 150 MHz wide allocation spanning 3550-3700 MHz. Usage of which is split into three tiers, with incumbent (1), priority (2) and general authorised (3) access. The top tier includes grandfathered fixed satellite service users. Next are Priority Access Licences (PAL), which are geographical area based and assigned using competitive bidding. Finally there is General Authorised Access (GAA), which is open to the widest number of users.

CBRS spectrum is dynamically managed and PALs have priority use after incumbents, while GAA users have lowest priority. This is coordinated via a Spectrum Access System (SAS), with the FCC having approved a number of companies to administrate these, including Sony and Google. GAA users are not charged for spectrum access, but have to pay a subscription fee to the SAS provider. 

CBRS spectrum may be used with both LTE and 5G private networks.

For more details see the FCC website.
