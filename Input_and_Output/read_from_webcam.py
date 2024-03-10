import cv2

# Open the default webcam (usually index 0)
#if we have other webcam we can specify them as 1,2,3 etc
video = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not video.isOpened():
    print("Error: Unable to open webcam.")
    exit()

# Loop to capture and display frames
while True:
    # Read frame from the webcam
    ret, frame = video.read()

    # Check if frame is successfully read
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Display the captured frame
    cv2.imshow("Webcam", frame)

    # Wait for a short delay between frames and check for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the video capture object and close the window
video.release()
cv2.destroyAllWindows()
