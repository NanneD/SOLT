.. _spsa:

SPSA
====

What is SPSA?
-------------

Simultaneous Perturbation Stochastic Approximation (SPSA) is an algorithm developed by `Spall <https://www.jhuapl.edu/spsa/>`_. It can be used if noisy and unbiased measurements of the gradient :math:`g(\boldsymbol{\theta}`) are available. It can also be used if only (noisy) measurements of the loss function :math:`f(\boldsymbol{\theta})` are available.

The advantage of SPSA compared to other algorithms is that only two loss measurements are required to generate an update. Therefore, SPSA is scalable.

How does SPSA work?
-------------------

Let :math:`\eta_i \in (0, \infty)` be a perturbation vector and :math:`\Delta_i` be a random vector such that :math:`\{\Delta_i\}` is an iid sequence with :math:`\Delta_i(k)` and :math:`1/\Delta_i(k)` bounded and symmetric around zero. The components :math:`\Delta_i(k)` are mutually independent. In practice, often the following binary random variable is used for :math:`\Delta_i`:

.. math::

	\mathbb{P}(\Delta_i(j) = -1) = \frac{1}{2} = \mathbb{P}(\Delta_i(j) = 1),

for all :math:`i` and :math:`j`.


The SPSA algorithm is then as follows:

.. topic:: SPSA Algorithm

	**Input**: Choose starting value :math:`\theta_0`, learning rate :math:`\epsilon` and take :math:`i = 0`.

	**Algorithm**:

	1. Calculate :math:`(g_i^{SPSA}(\theta_i))(j) = \frac{f(\theta_i+\eta_i\Delta_i)-f(\theta_i-\eta_i\Delta_i)}{2\eta_i\Delta_i(j)}`. 
	2. Update :math:`\theta_{i+1} = \theta_{i} - \epsilon (g_i^{SPSA}(\theta_i))`.
	3. (a) stop if :math:`i` large or :math:`|\theta_{i+1}-\theta_{i}|` small enough.  
   	   (b) else: update :math:`i` to :math:`i+1` and go back to (1).

Binder
------

If you want to experiment with the SPSA algorithm, you can use the `provided Jupyter Notebook <https://github.com/NanneD/SOLT/blob/main/notebooks/SPSA.ipynb>`_. If you want to experiment with the N-dimensional version of the algorithm, then you can use `this Jupyter Notebook <https://github.com/NanneD/SOLT/blob/main/notebooks/SPSA-ND.ipynb>`_.

You can also run the notebooks directly in your browser by using Binder; simply click on the following button to open the SPSA notebook:

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/NanneD/SOLT/HEAD?labpath=notebooks%2FSPSA.ipynb
