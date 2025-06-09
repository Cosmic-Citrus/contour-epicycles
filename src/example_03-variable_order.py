from variable_order_configuration import MultipleContourEpicyclesConfiguration


# is_save, path_to_save_directory = False, None
is_save, path_to_save_directory = True, "/Users/owner/Desktop/programming/contour_epicycles/output/"

paths_to_images = [
	"/Users/owner/Desktop/programming/contour_epicycles/data/harley_quinn.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/genie.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/guitar.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/joker.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/pi_symbol.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/caduceus.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/ankh.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/anubis.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/thoth_writing.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/thoth.png",
	"/Users/owner/Desktop/programming/contour_epicycles/data/khnum.png"]


if __name__ == "__main__":

	for path_to_image in paths_to_images:
		multiple_contour_epicycles = MultipleContourEpicyclesConfiguration()
		multiple_contour_epicycles.initialize(
			path_to_image=path_to_image,
			minimum_order=1,
			maximum_order=100,
			number_time_steps=1080)
		multiple_contour_epicycles.update_save_directory(
			path_to_save_directory=path_to_save_directory)
		multiple_contour_epicycles.view_variable_order(
			is_show_contour=True,
			is_with_axes=True,
			figsize=(12, 7),
			is_save=is_save,
			extension=".gif")

##