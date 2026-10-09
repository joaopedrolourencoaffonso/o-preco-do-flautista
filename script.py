from PIL import Image

def make_white_transparent(image_path, output_path, tolerance=0):
    """
    Converts white pixels in an image to transparent.
    
    :param image_path: Path to the input image file.
    :param output_path: Path where the output PNG should be saved.
    :param tolerance: How close to pure white a pixel needs to be (0 to 255).
                      Use 0 for strict pure white. Use 10-30 if you have artifacts.
    """
    # Open the image and ensure it's in RGBA mode (Red, Green, Blue, Alpha)
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    
    # Calculate the minimum value a pixel component can have to be considered "white"
    threshold = 255 - tolerance

    for item in datas:
        # item is a tuple: (R, G, B, A)
        r, g, b, a = item[:4]
        
        # Check if Red, Green, and Blue are all above the threshold
        if r >= threshold and g >= threshold and b >= threshold:
            # Replace with a completely transparent pixel (0 alpha)
            new_data.append((255, 255, 255, 0))
        else:
            # Keep the original pixel color and alpha transparency
            new_data.append(item)

    # Update image data and save as PNG (JPEG does not support transparency)
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Successfully processed! Saved to {output_path}")

# --- Example Usage ---
# Replace 'input_image.jpg' with your file's name
input_file = ".\\img\\banner-2.png" 
output_file = ".\\img\\banner-3.png"

# Run the function (adjust tolerance if edges look choppy)
make_white_transparent(input_file, output_file, tolerance=15)
