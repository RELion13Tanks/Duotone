import sys
import cv2
import numpy as np
from PIL import Image

def apply_duotone_then_upscale(image_path, color1, color2, output_path, scale_factor=2):
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    print(f"Original image dimensions: {img.width}x{img.height}")
    
    # Create a blank image with the same size
    duotone = Image.new('RGB', img.size)
    
    # Apply duotone effect
    print("Applying duotone effect...")
    for x in range(img.width):
        for y in range(img.height):
            a = img.getpixel((x, y))
            r = int((color1[0] * (255 - a) + color2[0] * a) / 255)
            g = int((color1[1] * (255 - a) + color2[1] * a) / 255)
            b = int((color1[2] * (255 - a) + color2[2] * a) / 255)
            duotone.putpixel((x, y), (r, g, b))
    
    # Convert PIL Image to OpenCV format
    cv_image = cv2.cvtColor(np.array(duotone), cv2.COLOR_RGB2BGR)
    
    # Create a super resolution object
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    
    # Read the model
    path = "EDSR_x2.pb"  # Make sure this file is in the same directory as your script
    sr.readModel(path)
    
    # Set the model and scale
    sr.setModel("edsr", scale_factor)
    
    # Upscale the image
    print("Upscaling image...")
    upscaled = sr.upsample(cv_image)
    
    # Save the result
    cv2.imwrite(output_path, upscaled)
    print(f"Upscaled duotone image saved as {output_path}")
    print(f"Final image dimensions: {upscaled.shape[1]}x{upscaled.shape[0]}")

if __name__ == "__main__":
    if len(sys.argv) != 9:
        print("Usage: python duotone_opencv.py <input_image> <color1_r> <color1_g> <color1_b> <color2_r> <color2_g> <color2_b> <output_image>")
        sys.exit(1)
    
    input_image = sys.argv[1]
    color1 = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    color2 = (int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    output_image = sys.argv[8]
    
    apply_duotone_then_upscale(input_image, color1, color2, output_image)
