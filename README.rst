========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/test_mpi_pkg/badge/?style=flat
    :target: https://readthedocs.org/projects/test_mpi_pkg
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/test_mpi_pkg/test_mpi_pkg.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/test_mpi_pkg/test_mpi_pkg

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/test_mpi_pkg/test_mpi_pkg?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/test_mpi_pkg/test_mpi_pkg

.. |requires| image:: https://requires.io/github/test_mpi_pkg/test_mpi_pkg/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/test_mpi_pkg/test_mpi_pkg/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/test_mpi_pkg/test_mpi_pkg/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/test_mpi_pkg/test_mpi_pkg

.. |version| image:: https://img.shields.io/pypi/v/test_mpi_pkg.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/test_mpi_pkg

.. |wheel| image:: https://img.shields.io/pypi/wheel/test_mpi_pkg.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/test_mpi_pkg

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/test_mpi_pkg.svg
    :alt: Supported versions
    :target: https://pypi.org/project/test_mpi_pkg

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/test_mpi_pkg.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/test_mpi_pkg

.. |commits-since| image:: https://img.shields.io/github/commits-since/test_mpi_pkg/test_mpi_pkg/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/test_mpi_pkg/test_mpi_pkg/compare/v0.0.0...master



.. end-badges

A Distributed Deep Learning package for PyTorch.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install test_mpi_pkg

You can also install the in-development version with::

    pip install https://github.com/test_mpi_pkg/test_mpi_pkg/archive/master.zip


Documentation
=============


https://test_mpi_pkg.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
