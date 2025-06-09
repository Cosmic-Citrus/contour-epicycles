from pathlib import Path
from skimage import measure, filters, io
import numpy as np


class BaseImageContourConfiguration():

	def __init__(self):
		super().__init__()
		self._path_to_image = None
		self._name = None
		self._x = None
		self._y = None
		self._z = None

	@property
	def path_to_image(self):
		return self._path_to_image
	
	@property
	def name(self):
		return self._name

	@property
	def x(self):
		return self._x
	
	@property
	def y(self):
		return self._y

	@property
	def z(self):
		return self._z
	
	@staticmethod
	def get_name_from_path(path_to_image):
		if not isinstance(path_to_image, str):
			raise ValueError("invalid type(path_to_image): {}".format(type(path_to_image)))
		image_name = Path(path_to_image).stem
		while True:
			if ("." in image_name) or ("/" in image_name):
				image_name = Path(image_name).stem
			else:
				break
		return image_name

	@staticmethod
	def center_about_origin(x, y):
		x -= np.min(x)
		x -= np.max(x) / 2
		y -= np.min(y)
		y -= np.max(y) / 2
		return x, y

	@staticmethod
	def get_contour(path_to_image, threshold, index_at_contour):
		colorized_image = io.imread(
			path_to_image)
		grayscale_image = np.mean(
			colorized_image,
			axis=2)
		binary_image = (
			grayscale_image > filters.threshold_otsu(
				grayscale_image))
		contours = measure.find_contours(
			binary_image,
			threshold)
		contour = contours[index_at_contour]
		return contour

class ImageContourConfiguration(BaseImageContourConfiguration):

	def __init__(self):
		super().__init__()

	def initialize(self, path_to_image, threshold, index_at_contour):
		if not isinstance(path_to_image, str):
			raise ValueError("invalid type(path_to_image): {}".format(type(path_to_image)))
		name = self.get_name_from_path(
			path_to_image=path_to_image)
		contour = self.get_contour(
			path_to_image=path_to_image,
			threshold=threshold,
			index_at_contour=index_at_contour)
		x = contour[:, 1]
		y = contour[:, 0] * -1
		x, y = self.center_about_origin(
			x=x,
			y=y)
		z = x + 1j * y
		self._path_to_image = path_to_image
		self._name = name
		self._x = x
		self._y = y
		self._z = z

##