import cv2
import numpy as np

# Function to initialize the camera
def initialize_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Camera not detected.")
        return None
    return cap

# Function to process the frame
def process_frame(frame):
    
    
    # Convert to grayscale (example of processing)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # Thresholding (simple binary segmentation example)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    
    
    # Contour detection to find objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    # Draw bounding boxes around detected objects
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Here you can integrate a machine learning model to classify objects
    # For example: class_label = classify_item(frame[x:x+w, y:y+h])

    return frame, contours

# Function to sort items based on detection
def sort_item(contours):
    # Based on object detection and classification, control the sorting mechanism
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Example logic to sort based on the position of the object
        if x < 100:
            print("Move object to left side")
        elif x > 200:
            print("Move object to right side")
        else:
            print("Keep object in the middle")

# Main loop
def main():
    cap = initialize_camera()

    if cap is None:
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Process the frame to detect objects
        processed_frame, contours = process_frame(frame)

        # Perform sorting logic
        sort_item(contours)

        # Show the frame with object detection
        cv2.imshow("Conveyor Belt", processed_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
