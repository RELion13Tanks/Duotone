	README!	
		
		This updated script includes the following changes:

	- Added an optional scale_factor parameter to the apply_duotone function.
	- Implemented image resizing using the LANCZOS resampling method, which generally provides good quality for upscaling.
	- Modified the main script to accept an optional scale factor as the last argument.
		
		Requiremnts:
	 
	  - python or python3
	  - pillow
	  
	If you have python installed but not pillow, you can get it with pip3 install pillow
	
=================================================================================================================================================================================================================================
	
		Duotone Usage:
	
	Make any image into a duotone one with RGB codes. You can also make grey scale ones by having all numbers being the same (Color1: 100 100 100 Color2: 0 0 0)
	First save the script as duotone.py, run the command in the format:
	python duotone.py <input_image> <color1_r> <color1_g> <color1_b> <color2_r> <color2_g> <color2_b> <output_image> [scale_factor]
	
	The script takes the following parameters:

	<input_image>: Path to the input image file
	<color1_r> <color1_g> <color1_b>: RGB values for the first color (0-255)
	<color2_r> <color2_g> <color2_b>: RGB values for the second color (0-255)
	<output_image>: Path for the output image file
	[scale_factor]: Scales image by a facortor of your choice. It will default to 1 (original size)

	Example: python3 duotone.py path/to/image 0 0 0 123 102 255 path/to/new/image
	
		Possible issues: 
		
	- If duotone tries to access a file instead of save a new one, manually create a copy of the image you want and put the path to it in to overwrite it.
	
	- You might have to be specific and put in the path to the script as well if your system can't find it and keeps giving you errors. (Don't give up, I swear it works!)

		Some things to keep in mind:

	Increasing resolution doesn't add new information to the image. It will make the image larger, but it may not necessarily improve the 
	perceived quality, especially for already high-resolution images. Large scale factors will significantly increase processing time and memory usage. 
	Be cautious when using very large scale factors, especially with already large images. The output file size will increase with higher resolutions.

	If you want to experiment with different upscaling methods or more advanced techniques, you might want to look into specialized image upscaling libraries 
	like waifu2x or machine learning-based solutions. However, these would require more complex setups and are beyond the scope of this simple script.
	
  
