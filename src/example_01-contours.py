from contour_epicycles_configuration import ContourEpicyclesConfiguration


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
		contour_epicycle = ContourEpicyclesConfiguration()
		contour_epicycle.initialize_visual_settings()
		contour_epicycle.update_save_directory(
			path_to_save_directory=path_to_save_directory)
		contour_epicycle.initialize_contour(
			path_to_image=path_to_image,
			threshold=0.5,
			index_at_contour=0)
		contour_epicycle.view_image(
			is_show_contour=True,
			is_with_axes=True,
			figsize=(12, 7),
			is_save=is_save)

##