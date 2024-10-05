import cv2
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def enhance_image(image):
    # Convert OpenCV image (numpy array) to PIL Image
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Adjust brightness
    enhancer = ImageEnhance.Brightness(pil_img)
    brightened = enhancer.enhance(1.3)  # Increase brightness by 30%

    # Adjust contrast
    enhancer = ImageEnhance.Contrast(brightened)
    contrasted = enhancer.enhance(1.5)  # Increase contrast by 50%

    # Adjust saturation
    enhancer = ImageEnhance.Color(contrasted)
    enhanced_image = enhancer.enhance(1.5)  # Increase saturation by 50%

    return pil_img, enhanced_image

def capture_and_enhance():
    # Start the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image.")
            break

        # Display the live camera feed
        cv2.imshow('Press Space to Capture', frame)

        # Wait for the user to press Space (ASCII code 32)
        if cv2.waitKey(1) & 0xFF == 32:
            original, enhanced = enhance_image(frame)

            # Display both original and enhanced images using Matplotlib
            plt.figure(figsize=(10, 5))

            # Show Original Image
            plt.subplot(1, 2, 1)
            plt.title("Original Image")
            plt.imshow(original)

            # Show Enhanced Image
            plt.subplot(1, 2, 2)
            plt.title("Enhanced Image")
            plt.imshow(enhanced)

            # Display the images
            plt.show()
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Capture and enhance the image
capture_and_enhance()