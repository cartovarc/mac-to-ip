=========
MAC to IP
=========


.. image:: https://img.shields.io/pypi/v/mac_to_ip.svg
        :target: https://pypi.python.org/pypi/mac_to_ip

.. image:: https://api.travis-ci.com/cartovarc/mac-to-ip.svg?branch=master
        :target: https://travis-ci.com/github/cartovarc/mac-to-ip

.. image:: https://readthedocs.org/projects/mac-to-ip/badge/?version=latest
        :target: https://mac-to-ip.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Find ip addresses with known MAC addresses


* Free software: MIT license
* Documentation: https://mac-to-ip.readthedocs.io.

Dependencies
------------

.. code:: bash

        $ sudo apt-get install net-tools
        $ sudo apt-get install nmap


Install from PyPI
~~~~~~~~~~~~~~~~~

.. code:: bash

    $ pip install mac-to-ip


Usage example
-------------

.. code:: python

        from mac_to_ip import mac_to_ip

        device_macs = {
                "camera1": "00:A0:C9:14:C8:27",
                "camera2": "00:A0:C9:14:C8:28",
                "camera3": "00:A0:C9:14:C8:29"
        }

        print(mac_to_ip(device_macs))

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
