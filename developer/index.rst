Developer Documentation
=======================

.. toctree::
   :maxdepth: 2
   :hidden:

   hardware/ci/index
   software/ci/index
   hardware/rf/index

LibreCellular is set up as a project under `MyriadRF`_ and LibreCellular projects are hosted under the `MyriadRF GitHub`_ organisation. Discussion is hosted via the `MyriadRF Forums`_.

Documentation is generated using Sphinx and Read the Docs theme. At present the RST source is hosted in a single GitHub repo. Netlify is used for the build pipeline and web hosting.

The initial :doc:`/developer/hardware/ci/index` configuration has been built, see the menu on the left for details of subsystems and original components. CAD models, manufacturing files and graphics have been published to the `lc-ci-hardware`_ repo.

The current development focus is :doc:`/developer/software/ci/index` platform configuration.

At this stage of development there is not much opportunity to contribute, although ideas and questions are welcomed and should be directed to the forum. 

Once the CI platform is fully up and running contributions will be welcomed which improve test coverage. Following the first LibreCellular release, contributions to future releases will also be welcome.

.. _MyriadRF: https://myriadrf.org
.. _MyriadRF GitHub: https://github.com/myriadrf/
.. _MyriadRF Forums: https://discourse.myriadrf.org/c/projects/librecellular/ 
.. _lc-ci-hardware: https://github.com/myriadrf/lc-ci-hardware
