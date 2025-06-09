import numpy as np
from scipy.integrate import quad
from image_contour_configuration import ImageContourConfiguration
from plotter_configuration import (
	BasePlotterConfiguration,
	ContourEpicyclesViewer)


class BaseContourEpicyclesConfiguration(BasePlotterConfiguration):

	def __init__(self):
		super().__init__()
		self._contour = None
		self._tau = None
		self._t = None
		self._t_interp = None
		self._number_circles = None
		self._maximum_order = None
		self._orders = None
		self._number_time_steps = None
		self._fourier_coefficients = None
		self._discrete_fourier_transform = None

	@property
	def contour(self):
		return self._contour
	
	@property
	def tau(self):
		return self._tau

	@property
	def t(self):
		return self._t
	
	@property
	def t_interp(self):
		return self._t_interp
	
	@property
	def number_circles(self):
		return self._number_circles
	
	@property
	def maximum_order(self):
		return self._maximum_order
	
	@property
	def orders(self):
		return self._orders

	@property
	def number_time_steps(self):
		return self._number_time_steps

	@property
	def fourier_coefficients(self):
		return self._fourier_coefficients
	
	@property
	def discrete_fourier_transform(self):
		return self._discrete_fourier_transform

	def f(self, t):
		x = np.interp(
			t,
			self.t,
			self.contour.x)
		y = np.interp(
			t,
			self.t,
			self.contour.y)
		z = x + 1j * y
		return z

	def initialize_contour(self, *args, **kwargs):
		contour = ImageContourConfiguration()
		contour.initialize(
			*args,
			**kwargs)
		self._contour = contour

	def initialize_t(self):
		tau = 2 * np.pi
		t = np.linspace(
			0,
			tau,
			self.contour.z.size)
		self._tau = tau
		self._t = t

	def initialize_orders(self, maximum_order):
		if not isinstance(maximum_order, (int, np.int64)):
			raise ValueError("invalid type(maximum_order): {}".format(type(maximum_order)))
		if maximum_order <= 0:
			raise ValueError("invalid maximum_order: {}".format(maximum_order))
		orders = np.array(
			list(
				range(
					-1 * maximum_order,
					maximum_order + 1)))
		number_circles = orders.size
		self._number_circles = number_circles
		self._maximum_order = maximum_order
		self._orders = orders

	def initialize_fourier_coefficients(self):

		def integrand(t, f_component):
			value = f_component(
				self.f(t) * np.exp(-1j * n * t)) / self.tau
			return value

		fourier_coefficients = list()
		for n in self.orders:
			real_component_at_coefficient = quad(
				lambda t : integrand(
					t,
					f_component=np.real),
				0,
				self.tau)[0]
			imag_component_at_coefficient = quad(
				lambda t : integrand(
					t,
					f_component=np.imag),
				0,
				self.tau)[0]
			coefficient = [
				real_component_at_coefficient,
				imag_component_at_coefficient]
			fourier_coefficients.append(
				coefficient)
		fourier_coefficients = np.array(
			fourier_coefficients)
		self._fourier_coefficients = fourier_coefficients

	def initialize_discrete_fourier_transform(self, number_time_steps):
		if not isinstance(number_time_steps, int):
			raise ValueError("invalid type(number_time_steps): {}".format(type(number_time_steps)))
		if number_time_steps <= 2:
			raise ValueError("invalid number_time_steps: {}".format(number_time_steps))
		t_interp = np.linspace(
			0,
			self.tau,
			number_time_steps)
		z = self.fourier_coefficients[:, 0] + 1j * self.fourier_coefficients[:, 1]
		discrete_fourier_transform = list()
		for t in t_interp:
			kernel = np.exp(
				-1j * self.orders * t)
			dft = np.sum(
				z * kernel[:])
			real_component_at_dft = np.real(
				dft)
			imag_component_at_dft = np.imag(
				dft)
			dft_component = [
				real_component_at_dft,
				imag_component_at_dft]
			discrete_fourier_transform.append(
				dft_component)
		discrete_fourier_transform = np.array(
			discrete_fourier_transform)
		self._t_interp = t_interp
		self._discrete_fourier_transform = discrete_fourier_transform
		self._number_time_steps = number_time_steps

class ContourEpicyclesConfiguration(BaseContourEpicyclesConfiguration):

	def __init__(self):
		super().__init__()

	def initialize(self, path_to_image, threshold=0.5, index_at_contour=0, maximum_order=10, number_time_steps=500):
		self.initialize_visual_settings()
		self.initialize_contour(
			path_to_image=path_to_image,
			threshold=threshold,
			index_at_contour=index_at_contour)
		self.initialize_t()
		self.initialize_orders(
			maximum_order=maximum_order)
		self.initialize_fourier_coefficients()
		self.initialize_discrete_fourier_transform(
			number_time_steps=number_time_steps)

	def view_image(self, is_show_contour=False, is_show_dft=False, is_with_axes=False, contour_color="darkorange", dft_color="steelblue", figsize=None, is_save=False):
		plotter = ContourEpicyclesViewer()
		plotter.initialize_visual_settings()
		plotter.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		plotter.view_image(
			contour_epicycles=self,
			is_show_contour=is_show_contour,
			is_show_dft=is_show_dft,
			is_with_axes=is_with_axes,
			contour_color=contour_color,
			dft_color=dft_color,
			figsize=figsize,
			is_save=is_save)

	def view_epicycles(self, fps=60, is_show_contour=False, is_show_dft=False, is_with_axes=False, contour_color="steelblue", dft_color="limegreen", curve_color="darkorange", radius_color="silver", circle_color="black", number_thetas=100, figsize=None, is_save=False, extension=".mp4"):
		plotter = ContourEpicyclesViewer()
		plotter.initialize_visual_settings()
		plotter.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		plotter.view_epicycles(
			contour_epicycles=self,
			fps=fps,
			is_show_contour=is_show_contour,
			is_show_dft=is_show_dft,
			is_with_axes=is_with_axes,
			contour_color=contour_color,
			dft_color=dft_color,
			curve_color=curve_color,
			radius_color=radius_color,
			circle_color=circle_color,
			number_thetas=number_thetas,
			figsize=figsize,
			is_save=is_save,
			extension=extension)

##