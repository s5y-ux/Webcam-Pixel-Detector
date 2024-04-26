import cv2
import datetime
import os

def show_webcam_and_detect_red():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video camera!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Webcam Feed', frame)

        red_found = False

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red1 = (0, 70, 50)
        upper_red1 = (10, 255, 255)
        lower_red2 = (170, 70, 50)
        upper_red2 = (180, 255, 255)

        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
        red_mask = cv2.bitwise_or(mask1, mask2)

        if cv2.countNonZero(red_mask) > 0:
            print("Divergence detected: " + datetime.datetime.now().time().strftime("%H:%M:%S.%f"))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    os.system("clear")
    show_webcam_and_detect_red()
