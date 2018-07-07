============
Click Pacbar
============

.. image:: https://img.shields.io/pypi/v/click-pacbar.svg
        :target: https://pypi.python.org/pypi/click-pacbar

Helper method to turn the click.progressbar into a Pacman!


* Free software: MIT license


Features
--------

Same interface as `click.progressbar` (http://click.pocoo.org/6/utils/#showing-progress-bars), just use `pacbar`.

Made mostly for my personal use, so use at your own risk. Enjoy!

.. code-block:: python

    import time

    from pacbar import pacbar

    with pacbar(range(10)) as bar:
    for x in bar:
            time.sleep(1)

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
