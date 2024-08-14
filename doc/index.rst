:html_theme.sidebar_secondary.remove:

SOLT
====

| **Release** |release|
| **Date** |today|

SOLT (Stochastic Optimization Learning Tool) is a learning tool about gradient descent and stochastic optimization, and in particular the simultaneous perturbation stochastic approximation (SPSA) algorithm. This website contains information about gradient descent, SPSA and N-dimensional SPSA.

You can experiment with the various algorithms through Jupyter Notebooks that contain implementations of the algorithms. You can directly open the notebooks in a browser with Binder by clicking on the following button:

.. image:: https://mybinder.org/badge_logo.svg
    :align: center
    :target: https://mybinder.org/v2/gh/NanneD/SOLT/HEAD

| **License**
| The GNU Affero General Public License v3 (AGPL-3.0) license is used. For more information, please see the `GitHub repository <https://github.com/NanneD/SOLT>`_.

| **Contributing**
| Please see the README file on the `GitHub repository <https://github.com/NanneD/SOLT>`_ for information on how to contribute.

.. grid:: 1 2 2 2

    .. grid-item-card::
	:link: gradientdescent
        :width: 75%
        :link-type: ref
        :link-alt: Gradient Descent
        :img-background: _static/GD_logo.svg

    .. grid-item-card::
        :link: spsa
        :width: 75%
        :link-type: ref
        :link-alt: SPSA
        :img-background: _static/SPSA_logo.svg


.. toctree::
   :hidden:

   gradientdescent
   spsa