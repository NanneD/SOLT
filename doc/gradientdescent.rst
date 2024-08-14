.. _gradientdescent:

Gradient Descent
================

What is gradient descent?
-------------------------

Gradient descent is an iterative optimization algorithm that can be used to find a minimum of a function :math:`f(\theta)`. At each iteration, it takes a step in the direction of the *negative* gradient :math:`\nabla f(\theta)`. The algorithm can also be used to find a maximum. In that case, the algorithm should take a step in the direction of the gradient.

How does gradient descent work?
-------------------------------

The gradient descent algorithm is as follows:

.. topic:: Gradient Descent Algorithm

	**Input**: Choose starting value :math:`\theta_0`, learning rate :math:`\epsilon` and take :math:`i=0`.

	**Algorithm**:

	1. Calculate :math:`\nabla f(\theta_i)`.
	2. Update :math:`\theta_{i+1}=\theta_i-\epsilon \nabla f(\theta_i)`.
	3. (a) stop if :math:`i` large or :math:`|\theta_{i+1}-\theta_{i}|` small enough.
	   (b) else: update :math:`i` to :math:`i+1` and go back to (1).



Binder
------

If you want to experiment with the gradient descent algorithm, you can use the `provided Jupyter Notebook <https://github.com/NanneD/SOLT/blob/main/notebooks/GradientDescent.ipynb>`_. You can run the notebook directly in your browser by using Binder; simply click on the following button to open the notebook:

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/NanneD/SOLT/HEAD?labpath=notebooks%2FGradientDescent.ipynb