# Repo:    contour-epicycles

The purpose of this code is to use math to make art. 

## Description

Most people today agree that Sun is the center of our Solar System - and that the Earth revolves around the Sun in an orbit that is slightly elliptical - but this perception was different in ancient times. Aristotle was a vociferous proponent of the geocentric model, in which the Earth was center of the Universe and all other celestial bodies - including the Sun - revolved around the Earth in orbits that were perfectly circular. Despite being an incorrect description of reality, the geocentric model prevailed for over a millenium. The ancient Greeks noticed that some celestial bodies exhibited [apparent retrograde motion](https://en.wikipedia.org/wiki/Apparent_retrograde_motion), in which it [appears]((https://upload.wikimedia.org/wikipedia/commons/7/70/Apparent_retrograde_motion_of_Mars_in_2003.gif)) that the observed [celestial bodies are moving backwards](https://upload.wikimedia.org/wikipedia/commons/f/f0/The_astronomical_explanation_for_Mercury_retrograde.webm) in the nightsky as viewed from the perspective of an observer on Earth. The ancient Greeks incorporated [epicycles](https://upload.wikimedia.org/wikipedia/commons/f/fb/Epicycle_and_deferent.svg) - circles upon circles - into their geocentric model to account for apparent retrograde motion. With a sufficient number of epicycles, one can make any geocentric model fit. Similarly, any $y=f(x)$ path can be parameterized as the [sum of sines (or cosines)](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Fourier_series_and_transform.gif/640px-Fourier_series_and_transform.gif) - this is the essence of Fourier series. 

![example-genie-epicycles](output/example_02-epicycles/genie-Epicycles.gif)


The concept of [complex numbers](https://upload.wikimedia.org/wikipedia/commons/5/5d/Imaginarynumber2.PNG) is import to understand Fourier series. A complex number can be thought of as a vector containing a real component and imaginary component.

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


To generate the epicycles, we consider the contour to start at $\theta=0$ and end at $\theta=2 \pi$ moving counter-clockwise; this monotonically increasing value of $\theta$ can be analogous to time $t$. The angle can vary in continuous space in principle, but is discrete in practice - there are an equal number of values of $t$ as there are of ($x$, $y$) coordinates. The complex value of $z$ at some value $t$ in-between two consecutive steps ($t_{j} < t < t_{j+1}$) are obtained by interpolation; I will refer to this interpolation function as $f$.

Any periodic function $f$ with period $L$ (meaning $f$ is complex and integrable) can be expressed as a Fourier series

$f(t) = \sum_{n=0}^{\infty} c_{n} e^{i \omega_{0} t}$

where

$\omega_{0} \equiv \frac{2 \pi}{L}$ is the fundamental angular frequency

$c_{n} = \frac{1}{L}\int_{0}^{L} f(t) e^{-i n \omega{0} t} dt$ are complex Fourier coefficients over one period

These complex Fourier coefficients determine the complex amplitude of the frequency component $n \omega_{0}$. For a non-periodic function, the Fourier transform is given by

$F(\omega) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} f(t) e^{-i \omega t} dt$

The inverse Fourier transform, which can reconstruct the time-domain signal $f(t)$ from the frequency-domain signal $F(\omega)$, is given by

$f(t) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} F(\omega) e^{i \omega t} d\omega$

When $f(t)$ is periodic with period $L$, then the Fourier coefficients are proportional to the sums of the weights of the harmonic frequencies $n\omega_{0}$.

$F(\omega) = 2 \pi \sum_{-\infty}^{\infty} c_{n} \delta(\omega - n\omega_{0})$

where

$\delta(\omega - n\omega_{0}) = 0$ if $\omega - n\omega_{0} \neq 0$

$\delta(\omega - n\omega_{0}) \rightarrow \infty$ if $\omega - n\omega_{0} = 0$

$\int_{-\infty}^{\infty} \delta(x) dx = 1$

This means that the Fourier transform of a periodic function is discrete and that the Fourier coefficients are scaled samples of the Fourier transform at harmonic frequencies.

To be clear, $F(n\omega_{0})$ is the Fourier transform of $f(t)$ over one period $L$. Because it is not feasible to compute an infinite number of Fourier coefficients $c_{n}$, a cut-off value $m$ (represented in the code as `maximum_order`) is chosen such that the 

$F(\omega) \approx \sum_{-m}^{m} f(t) e^{-i \omega t} \Delta t$

The discrete version of the Fourier transform is the discrete Fourier transform (DFT). A given value of $m$ corresponds to $2m+1$ terms in the summation. A finite value of $m$ means that this is only an approximation, but this approximation becomes exact as $m \rightarrow \infty$. A reasonable approximation can be obtained with $10 \leq m \leq 30$ for most shapes. The animation below shows how the approximation improves as $m$ increases up to $m=100$.


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
