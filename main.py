import cv2 
import matplotlib.pyplot as plt 

# Load the image 
image = cv2.imread('man-photo.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Adjust the brightness and contrast 
    alpha = 1.2  # Contrast control (1.0 - 3.0)
    beta = 10    # Brightness control (0 - 100)

    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Apply gamma correction
    gamma = 1.5
    adjusted_image = cv2.pow(adjusted_image / 255.0, gamma)
    adjusted_image = (adjusted_image * 255).astype('uint8')

    # Plot the original image 
    plt.subplot(1, 3, 1) 
    plt.title("Original") 
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 

    # Plot the contrast adjusted image 
    plt.subplot(1, 3, 2) 
    plt.title("Brightness & Contrast") 
    plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))

    plt.show() 
