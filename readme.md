# Repo:    contour-epicycles

The purpose of this code is to use math to make art. 

## Description

The geocentric model is a model of the Universe in which the Earth is the center of the Universe such that all other celestial bodies revolve around the Earth. Aristotle was a vociferous proponent of the geocentric model; Even though we know today that the Earth revolves around the Sun in an elliptical orbit of low eccentricity, the geocentric model prevailed for more than a millenium. 

The ancient Greeks noticed that some celestial bodies exhibited [apparent retrograde motion](https://en.wikipedia.org/wiki/Apparent_retrograde_motion), in which it [appears]((https://upload.wikimedia.org/wikipedia/commons/7/70/Apparent_retrograde_motion_of_Mars_in_2003.gif)) that the [celestial body is moving backwards](https://upload.wikimedia.org/wikipedia/commons/f/f0/The_astronomical_explanation_for_Mercury_retrograde.webm) in the nightsky as viewed from the perspective of an observer on Earth. The ancient Greeks incorporated [epicycles](https://upload.wikimedia.org/wikipedia/commons/f/fb/Epicycle_and_deferent.svg) - circles upon circles - into their geocentric model to account for apparent retrograde motion. With a sufficient number of epicycles, one can make any geocentric model fit. Similarly, any $y=f(x)$ path can be parameterized as the [sum of sines (or cosines)](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Fourier_series_and_transform.gif/640px-Fourier_series_and_transform.gif) - this is the essence of Fourier series. 







Given the path to an image, this code leverages `scikit-image` to generate the contour outline of the image. In the `data` directory, there are images of characters from ancient Egyptian mythology, a few cartoon guitars, a guitar, and the symbol of the number pi ($\pi$). 


<img title="" src="data/genie.png" alt="example-original_genie_image" width="329" data-align="center">


<img title="" src="output/example_01-contours/genie-Contour.png" alt="example-genie_contour" data-align="center">


ADD DFT HERE


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
