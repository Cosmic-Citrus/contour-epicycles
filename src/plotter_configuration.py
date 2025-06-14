import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from plotter_base_configuration import BasePlotterConfiguration


class BaseContourEpicyclesViewer(BasePlotterConfiguration):

	def __init__(self):
		super().__init__()

	@staticmethod
	def get_multiple_extensions(extension):
		if isinstance(extension, (tuple, list)):
			modified_extensions = extension[:]
		else:
			modified_extensions = [extension]
		return modified_extensions

	@staticmethod
	def get_save_name(contour_epicycles, plot_name, is_save):
		if is_save:
			save_name = "{}-{}".format(
				contour_epicycles.contour.name,
				plot_name.title().replace(
					" ",
					""))
		else:
			save_name = None
		return save_name

	@staticmethod
	def plot_contour(contour_epicycles, ax, contour_color, label=None, alpha=1):
		contour_handle = ax.plot(
			contour_epicycles.contour.x, ## real
			contour_epicycles.contour.y, ## imag
			color=contour_color,
			label=label,
			alpha=alpha)
		return ax, contour_handle

	@staticmethod
	def plot_discrete_fourier_transform(contour_epicycles, ax, dft_color, label=None, alpha=1):
		dft_handle = ax.plot(
			contour_epicycles.discrete_fourier_transform[:, 0], ## real
			contour_epicycles.discrete_fourier_transform[:, 1], ## imag
			color=dft_color,
			label=label,
			alpha=alpha)
		return ax, dft_handle

	@staticmethod
	def get_contour_label():
		label = "Contour of Image"
		return label

	@staticmethod
	def get_dft_label(contour_epicycles):
		label = "DFT\n" + r"$2 ({:,}) + 1 = {:,}$ Circles".format(
			contour_epicycles.maximum_order,
			contour_epicycles.number_circles)
		return label

	def plot_legend(self, fig, ax):
		handles, labels = ax.get_legend_handles_labels()
		leg = self.visual_settings.get_legend(
			fig=fig,
			ax=ax,
			handles=handles,
			labels=labels)
		return fig, ax, leg

	def autoformat_plot(self, contour_epicycles, ax, is_with_axes, limit_scale):
		
		def autoformat_axis_limits(contour_epicycles, ax, limit_scale):
			xlim = (
				limit_scale * np.min(
					contour_epicycles.contour.x),
				limit_scale * np.max(
					contour_epicycles.contour.x))
			ylim = (
				limit_scale * np.min(
					contour_epicycles.contour.y),
				limit_scale * np.max(
					contour_epicycles.contour.y))
			ax = self.visual_settings.autoformat_axis_limits(
				ax=ax,
				xlim=xlim,
				ylim=ylim)
			return ax

		def autoformat_axis_ticks_and_ticklabels(ax, is_with_axes):
			if is_with_axes:
				is_grid = True
				x_major_ticks = True
				y_major_ticks = True
				x_minor_ticks = True
				y_minor_ticks = True
				x_major_ticklabels = True
				y_major_ticklabels = True
				x_minor_ticklabels = False
				y_minor_ticklabels = False
			else:
				is_grid = False
				x_major_ticks = None
				y_major_ticks = None
				x_minor_ticks = None
				y_minor_ticks = None
				x_major_ticklabels = None
				y_major_ticklabels = None
				x_minor_ticklabels = None
				y_minor_ticklabels = None
			ax = self.visual_settings.autoformat_axis_ticks_and_ticklabels(
				ax=ax,
				x_major_ticks=x_major_ticks,
				y_major_ticks=y_major_ticks,
				x_minor_ticks=x_minor_ticks,
				y_minor_ticks=y_minor_ticks,
				x_major_ticklabels=x_major_ticklabels,
				y_major_ticklabels=y_major_ticklabels,
				x_minor_ticklabels=x_minor_ticklabels,
				y_minor_ticklabels=y_minor_ticklabels)
			if is_grid:
				ax = self.visual_settings.autoformat_grid(
					ax=ax,
					grid_color="gray")
			return ax

		def autoformat_axis_labels(contour_epicycles, ax, is_with_axes):
			modified_name = contour_epicycles.contour.name.replace(
				"_",
				" ")
			title = modified_name.title()
			if is_with_axes:
				xlabel = r"Re($z=x + iy$) $\in$ $\Re$"
				ylabel = r"Im($z=x + iy$) $\in$ $\Im$"
			else:
				xlabel = None
				ylabel = None
			ax = self.visual_settings.autoformat_axis_labels(
				ax=ax,
				xlabel=xlabel,
				ylabel=ylabel,
				title=title)
			return ax

		ax = autoformat_axis_limits(
			contour_epicycles=contour_epicycles,
			ax=ax,
			limit_scale=limit_scale)
		ax = autoformat_axis_ticks_and_ticklabels(
			ax=ax,
			is_with_axes=is_with_axes)
		ax = autoformat_axis_labels(
			contour_epicycles=contour_epicycles,
			ax=ax,
			is_with_axes=is_with_axes)
		if not is_with_axes:
			ax.axis(
				"off")
		return ax

class ContourEpicyclesViewer(BaseContourEpicyclesViewer):

	def __init__(self):
		super().__init__()

	def view_image(self, contour_epicycles, is_show_contour, is_show_dft, is_with_axes, contour_color, dft_color, figsize, is_save):
		self.verify_visual_settings()
		if not isinstance(is_show_contour, bool):
			raise ValueError("invalid type(is_show_contour): {}".format(type(is_show_contour)))
		if not isinstance(is_show_dft, bool):
			raise ValueError("invalid type(is_show_dft): {}".format(type(is_show_dft)))
		if (not is_show_contour) and (not is_show_dft):
			raise ValueError("at least one of the following inputs should be True: 'is_show_contour', 'is_show_dft'")
		string_mapping = {
			"contour" : {
				"plot-name" : "Contour"},
			"dft" : {
				"plot-name" : "Discrete Fourier Transform"}}
		if (is_show_contour) and (not is_show_dft):
			plot_name = string_mapping["contour"]["plot-name"]
		elif (not is_show_contour) and (is_show_dft):
			plot_name = string_mapping["dft"]["plot-name"]
		else:
			plot_name = "{} vs {}".format(
				string_mapping["contour"]["plot-name"],
				string_mapping["dft"]["plot-name"])
		fig, ax = plt.subplots(
			figsize=figsize)
		ax.set_aspect(
			"equal")
		if is_show_contour:
			contour_label = self.get_contour_label()
			ax, contour_handle = self.plot_contour(
				contour_epicycles=contour_epicycles,
				ax=ax,
				contour_color=contour_color,
				label=contour_label)
		if is_show_dft:
			dft_label = self.get_dft_label(
				contour_epicycles=contour_epicycles)
			ax, dft_handle = self.plot_discrete_fourier_transform(
				contour_epicycles=contour_epicycles,
				ax=ax,
				dft_color=dft_color,
				label=dft_label)
		ax = self.autoformat_plot(
			contour_epicycles=contour_epicycles,
			ax=ax,
			is_with_axes=is_with_axes,
			limit_scale=1.05)
		fig, ax, leg = self.plot_legend(
			fig=fig,
			ax=ax)
		save_name = self.get_save_name(
			contour_epicycles=contour_epicycles,
			plot_name=plot_name,
			is_save=is_save)
		self.visual_settings.display_image(
			fig=fig,
			save_name=save_name)

	def view_epicycles(self, contour_epicycles, fps, is_show_contour, is_show_dft, is_with_axes, contour_color, dft_color, curve_color, radius_color, circle_color, number_thetas, figsize, is_save, extension):

		def plot_other_handles(contour_epicycles, curve_color, radius_color, circle_color):
			curve_handle, = ax.plot(
				list(),
				list(),
				color=curve_color,
				label="Epicycle Path")
			radius_handles, circle_handles = list(), list()
			for index_at_circle in range(contour_epicycles.number_circles):
				if index_at_circle == 0:
					radius_label = "Radii"
					circle_label = "Circles"
				else:
					radius_label = None
					circle_label = None
				radius_handle, = ax.plot(
					list(),
					list(),
					color=radius_color,
					label=radius_label)
				circle_handle, = ax.plot(
					list(),
					list(),
					color=circle_color,
					label=circle_label)
				radius_handles.append(
					radius_handle)
				circle_handles.append(
					circle_handle)
			return curve_handle, radius_handles, circle_handles

		def get_sorted_fourier_coefficients(contour_epicycles, unsorted_coefficients):
			## c_0, c_1, c_-1, c_2, c_-2, ..., c_n, c_-n
			fourier_coefficients_at_t = list()
			fourier_coefficients_at_t.append(
				unsorted_coefficients[contour_epicycles.maximum_order])
			for n in range(1, contour_epicycles.maximum_order):
				nth_coefficients_at_t = [
					unsorted_coefficients[contour_epicycles.maximum_order + n],
					unsorted_coefficients[contour_epicycles.maximum_order - n]]
				fourier_coefficients_at_t.extend(
					nth_coefficients_at_t)
			fourier_coefficients_at_t = np.array(
				fourier_coefficients_at_t)
			return fourier_coefficients_at_t
	
		def rotate_circles(contour_epicycles, t, thetas, x_curves, y_curves, curve_handle, radius_handles, circle_handles):
			complex_coefficients = contour_epicycles.fourier_coefficients[:, 0] + 1j * contour_epicycles.fourier_coefficients[:, 1]
			unsorted_coefficients = complex_coefficients * np.exp(
				contour_epicycles.orders * t * 1j)
			sorted_coefficients = get_sorted_fourier_coefficients(
				contour_epicycles=contour_epicycles,
				unsorted_coefficients=unsorted_coefficients)
			real_component_at_coefficients = np.real(
				sorted_coefficients)
			imag_component_at_coefficients = np.imag(
				sorted_coefficients)
			center_position = np.full(
				fill_value=0,
				shape=len([
					"x",
					"y"]),
				dtype=float)
			(h, k) = center_position
			for index_at_coefficient, x, y, z in zip(range(contour_epicycles.number_circles), real_component_at_coefficients, imag_component_at_coefficients, sorted_coefficients):
				radius = np.abs(z)
				circle_handles[index_at_coefficient].set_data(
					h + radius * np.cos(thetas),
					k + radius * np.sin(thetas))
				radius_handles[index_at_coefficient].set_data(
					[h, h + x],
					[k, k + y])
				h += x
				k += y
			x_curves.append(
				h)
			y_curves.append(
				k)
			curve_handle.set_data(
				x_curves,
				y_curves)
			handles = [
				curve_handle,
				*radius_handles,
				*circle_handles]
			return handles

		def animate(frame, contour_epicycles, thetas, x_curves, y_curves, curve_handle, radius_handles, circle_handles):
			t = contour_epicycles.t_interp[frame]
			handles = rotate_circles(
				contour_epicycles=contour_epicycles,
				t=t,
				thetas=thetas,
				x_curves=x_curves,
				y_curves=y_curves,
				curve_handle=curve_handle,
				radius_handles=radius_handles,
				circle_handles=circle_handles)
			return handles

		self.verify_visual_settings()
		fig, ax = plt.subplots(
			figsize=figsize)
		ax.set_aspect(
			"equal")
		contour_label = self.get_contour_label()
		dft_label = self.get_dft_label(
			contour_epicycles=contour_epicycles)
		if is_show_contour:
			ax, contour_handle = self.plot_contour(
				contour_epicycles=contour_epicycles,
				ax=ax,
				contour_color=contour_color,
				label=contour_label,
				alpha=0.5)
		if is_show_dft:
			ax, dft_handle = self.plot_discrete_fourier_transform(
				contour_epicycles=contour_epicycles,
				ax=ax,
				dft_color=dft_color,
				label=dft_label,
				alpha=0.5)
		curve_handle, radius_handles, circle_handles = plot_other_handles(
			contour_epicycles=contour_epicycles,
			curve_color=curve_color,
			radius_color=radius_color,
			circle_color=circle_color)
		ax = self.autoformat_plot(
			contour_epicycles=contour_epicycles,
			ax=ax,
			is_with_axes=is_with_axes,
			limit_scale=1.375)
		fig, ax, leg = self.plot_legend(
			fig=fig,
			ax=ax)
		thetas = np.linspace(
			0,
			contour_epicycles.tau,
			number_thetas)
		x_curves = list()
		y_curves = list()
		fargs = (
			contour_epicycles,
			thetas,
			x_curves,
			y_curves,
			curve_handle,
			radius_handles,
			circle_handles)
		anim = FuncAnimation(
			fig,
			animate,
			fargs=fargs,
			frames=range(
				contour_epicycles.number_time_steps))
		save_name = self.get_save_name(
			contour_epicycles=contour_epicycles,
			plot_name="Epicycles",
			is_save=is_save)
		modified_extensions = self.get_multiple_extensions(
			extension=extension)
		for modified_extension in modified_extensions:
			self.visual_settings.display_animation(
				anim=anim,
				fps=fps,
				save_name=save_name,
				extension=modified_extension)

	def view_variable_order(self, multiple_contour_epicycles, fps, is_show_contour, is_with_axes, contour_color, dft_color, figsize, is_save, extension):
		
		def animate(frame, multiple_contour_epicycles, dft_handle, text_handle):
			contour_epicycles = multiple_contour_epicycles.multiple_contour_epicycles[frame]
			dft_handle.set_data(
				contour_epicycles.discrete_fourier_transform[:, 0],
				contour_epicycles.discrete_fourier_transform[:, 1])
			text_handle.set_text(
				r"$2 ({:,}) + 1 = {:,}$ DFT Coefficients".format(
					contour_epicycles.maximum_order,
					contour_epicycles.number_circles))
			handles = [
				dft_handle,
				text_handle]
			return handles

		self.verify_visual_settings()
		fig, ax = plt.subplots(
			figsize=figsize)
		ax.set_aspect(
			"equal")
		if is_show_contour:
			contour_label = self.get_contour_label()
			ax, contour_handle = self.plot_contour(
				contour_epicycles=multiple_contour_epicycles,
				ax=ax,
				contour_color=contour_color,
				label=contour_label)
		dft_label = "DFT"
		dft_handle, = ax.plot(
			list(),
			list(),
			color=dft_color,
			label=dft_label)
		text_handle = ax.text(
			0.5,
			0.95,
			"",
			horizontalalignment="center",
			verticalalignment="top",
			transform=ax.transAxes,
			fontsize=self.visual_settings.text_size)
		ax = self.autoformat_plot(
			contour_epicycles=multiple_contour_epicycles,
			ax=ax,
			is_with_axes=is_with_axes,
			limit_scale=1.375)
		fig, ax, leg = self.plot_legend(
			fig=fig,
			ax=ax)
		fargs = (
			multiple_contour_epicycles,
			dft_handle,
			text_handle,)
		anim = FuncAnimation(
			fig,
			animate,
			fargs=fargs,
			frames=range(
				multiple_contour_epicycles.variable_orders.size))
		save_name = self.get_save_name(
			contour_epicycles=multiple_contour_epicycles,
			plot_name="Variable Order",
			is_save=is_save)
		modified_extensions = self.get_multiple_extensions(
			extension=extension)
		for modified_extension in modified_extensions:
			self.visual_settings.display_animation(
				anim=anim,
				fps=fps,
				save_name=save_name,
				extension=modified_extension)

##