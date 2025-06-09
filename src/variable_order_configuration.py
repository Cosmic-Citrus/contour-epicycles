import numpy as np
from contour_epicycles_configuration import (
	ContourEpicyclesConfiguration,
	BaseContourEpicyclesConfiguration,
	ContourEpicyclesViewer)


class BaseMultipleContourEpicyclesConfiguration(BaseContourEpicyclesConfiguration):

	def __init__(self):
		super().__init__()
		self._variable_orders = None
		self._multiple_contour_epicycles = None

	@property
	def variable_orders(self):
		return self._variable_orders

	@property
	def multiple_contour_epicycles(self):
		return self._multiple_contour_epicycles
	
	@staticmethod	
	def f(*args, **kwargs):
		raise ValueError("this method exists only for the parent class for the inheritance purposes")

	@staticmethod
	def initialize_orders(*args, **kwargs):
		raise ValueError("this method exists only for the parent class for the inheritance purposes")

	@staticmethod
	def initialize_fourier_coefficients(*args, **kwargs):
		raise ValueError("this method exists only for the parent class for the inheritance purposes")

	@staticmethod
	def initialize_discrete_fourier_transform(*args, **kwargs):
		raise ValueError("this method exists only for the parent class for the inheritance purposes")

	def initialize_variable_orders(self, minimum_order, maximum_order):
		if not isinstance(minimum_order, (int, np.int64)):
			raise ValueError("invalid type(minimum_order): {}".format(type(minimum_order)))
		if not isinstance(maximum_order, (int, np.int64)):
			raise ValueError("invalid type(maximum_order): {}".format(type(maximum_order)))
		if minimum_order <= 0:
			raise ValueError("invalid minimum_order: {}".format(minimum_order))
		if maximum_order <= minimum_order:
			raise ValueError("minimum_order={} is not compatible with maximum_order={}".format(minimum_order, maximum_order))
		variable_orders = np.array(
			list(
				range(
					minimum_order,
					maximum_order + 1)))
		self._variable_orders = variable_orders

	def initialize_multiple_contour_epicycles(self, number_time_steps):
		multiple_contour_epicycles = list()
		for maximum_order in self.variable_orders:
			contour_epicycles = ContourEpicyclesConfiguration()
			contour_epicycles.initialize_visual_settings()
			contour_epicycles._contour = self.contour
			contour_epicycles._tau = self.tau
			contour_epicycles._t = self.t
			contour_epicycles.initialize_orders(
				maximum_order=maximum_order)
			contour_epicycles.initialize_fourier_coefficients()
			contour_epicycles.initialize_discrete_fourier_transform(
				number_time_steps=number_time_steps)
			multiple_contour_epicycles.append(
				contour_epicycles)
		self._multiple_contour_epicycles = multiple_contour_epicycles

class MultipleContourEpicyclesConfiguration(BaseMultipleContourEpicyclesConfiguration):

	def __init__(self):
		super().__init__()

	def initialize(self, path_to_image, minimum_order=1, maximum_order=100, number_time_steps=500, threshold=0.5, index_at_contour=0):
		self.initialize_visual_settings()
		self.initialize_contour(
			path_to_image=path_to_image,
			threshold=threshold,
			index_at_contour=index_at_contour)
		self.initialize_t()
		self.initialize_visual_settings()
		self.initialize_contour(
			path_to_image=path_to_image,
			threshold=threshold,
			index_at_contour=index_at_contour)
		self.initialize_t()
		self.initialize_variable_orders(
			minimum_order=minimum_order,
			maximum_order=maximum_order)
		self.initialize_multiple_contour_epicycles(
			number_time_steps=number_time_steps)

	def view_variable_order(self, fps=60, is_show_contour=False, is_with_axes=False, contour_color="black", dft_color="darkorange", figsize=None, is_save=False, extension=".mp4"):
		plotter = ContourEpicyclesViewer()
		plotter.initialize_visual_settings()
		plotter.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		plotter.view_variable_order(
			multiple_contour_epicycles=self,
			fps=fps,
			is_show_contour=is_show_contour,
			is_with_axes=is_with_axes,
			contour_color=contour_color,
			dft_color=dft_color,
			figsize=figsize,
			is_save=is_save,
			extension=extension)

##