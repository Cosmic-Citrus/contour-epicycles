# Repo:    contour-epicycles

The purpose of this code is to use math to make art. 

## Description

The geocentric model is a model of the Universe in which the Earth is the center of the Universe such that all other celestial bodies revolve around the Earth. Aristotle was a vociferous proponent of the geocentric model; Even though we know today that the Earth revolves around the Sun in an elliptical orbit of low eccentricity, the geocentric model prevailed for more than a millenium. 

The ancient Greeks noticed that some celestial bodies exhibited [apparent retrograde motion](https://en.wikipedia.org/wiki/Apparent_retrograde_motion), in which it [appears]((https://upload.wikimedia.org/wikipedia/commons/7/70/Apparent_retrograde_motion_of_Mars_in_2003.gif)) that the [celestial body is moving backwards](https://upload.wikimedia.org/wikipedia/commons/f/f0/The_astronomical_explanation_for_Mercury_retrograde.webm) in the nightsky as viewed from the perspective of an observer on Earth. The ancient Greeks incorporated [epicycles](https://upload.wikimedia.org/wikipedia/commons/f/fb/Epicycle_and_deferent.svg) - circles upon circles - into their geocentric model to account for apparent retrograde motion. With a sufficient number of epicycles, one can make any geocentric model fit. Similarly, any $y=f(x)$ path can be parameterized as the [sum of sines (or cosines)](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Fourier_series_and_transform.gif/640px-Fourier_series_and_transform.gif) - this is the essence of Fourier series. 

The concept of complex numbers is import to understand Fourier series. A complex number can be thought of as a vector containing a real component and imaginary component.

$z = x + iy$

  $\implies Re(z) = x$
  
  $\implies Im(z) = y$

The $xy$-plane can be transformed via polar coordinates:

$x = r \cos \theta$

$y = r \sin \theta$

where

$r$ is the radius of the circle from the origin to the point ($x$, $y$)

$\theta$ is the angle between the line segment from the origin to the point ($x$, $y$) with the line segment on the $x$-axis

Euler's formula states that

$e^{i \theta} = \cos \theta + i \sin \theta$


We can use this to transform $z$ into polar form

$z = x + iy \implies |z| = \sqrt{(x + iy) (x - iy)} = \sqrt{x^2 + y^2}$

$z = |z| (\cos \theta + i \sin \theta)$

$z = |z| e^{i \theta}$

The ($x$, $y$) coordinates form a closed path (or contour) from which epicycles are obtained. Given the path to an image file, this code leverages `scikit-image` to generate the contour outline. The `data` directory contains images of characters from ancient Egyptian mythology, a few characters from cartoons, a guitar, and the symbol of the number pi ($\pi$). Let us take the image of Genie from Disney's Aladdin as an example.


<div align="center">
  <img src="data/genie.png" alt="example-original_genie_image" width="327" />
</div>


<img title="" src="output/example_01-contours/genie-Contour.png" alt="example-genie_contour" data-align="center">


To generate the epicycles, we consider the contour to start at $\theta=0$ and end at $\theta=2 \pi$ - moving counter-clockwise; this monotonically increasing value of $\theta$ can be analogous to time $t$. To be clear, these are discrete (as opposed to continuous) steps; there are an equal number of values of $t$ as there are of ($x$, $y$) coordinates. The complex value of $z$ at some value $t$ in-between two consecutive steps ($t_{j} < t < t_{j+1}$) are be obtained by interpolation; I will refer to this interpolation function as $f$.

The Fourier transform (in continuous space) of a function $f$ - where $f$ is both complex and integrable - is given by

$\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-i 2 \pi \xi x} dx$

Since our steps our discrete, this code uses the discrete Fourier transform (DFT), which is given by





One can also view the epicycles of multiple connected circles tracing along the discrete Fourier transform (DFT) of the contour. 
![example-genie-epicycles](output/example_02-epicycles/genie-Epicycles.gif)

The input parameter `maximum_order` is required for indexing the discrete sums such that the number of circles is equal to `2 * maximum_order + 1` (negative indices + zero-index + positive indices). This DFT approximation to the contour becomes more accurate as `maximum_order` $\rightarrow$ $\infty$, though `maximum_order=10`  should be adequate for simple shapes and `maximum_order=20` should be adequate for more complicated shapes. One can also view how the discrete Fourier transform varies as a function of  `maximum_order`.
![example-genie_variable_order](output/example_03-variable_order/genie-VariableOrder.gif)

## Getting Started

### Dependencies

* Python 3.9.6
* numpy == 1.26.4
* matplotlib == 3.9.4
* scipy == 1.13.1
* scikit-image == 0.24.0
* pathlib (default)

### Executing program

* Download this repository to your local computer

* Modify `path_to_save_directory` and `paths_to_images` in  the following example codes
  
  * `src/example_01-contours.py`
  
  * `src/example_02-epicycles.py`
  
  * `src/example_03-variable_order.py`

* Change the value from `maximum_order=100` used  in the following example codes
  
  * `src/example_02-epicycles.py`
  
  * `src/example_03-variable_order.py`

* Run the example codes

## Version History

* 0.1
  * Initial Release

## License

This project is licensed under the Apache License - see the LICENSE file for details.
