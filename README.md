#  Hand Gesture Finger Counter with Arduino

A real-time **computer vision + embedded systems** project that detects the number of raised fingers using a webcam and controls LEDs on an Arduino via serial communication.

---

##  Project Overview

This project uses **MediaPipe Hands** and **OpenCV** to detect hand landmarks, count raised fingers, and send the result to an **Arduino**.
Each detected finger lights up a corresponding LED, creating a **touchless human–machine interface**.

---

##  Technologies Used

* Python

  * OpenCV
  * MediaPipe
  * PySerial
* Arduino (UNO or compatible)
* Serial Communication (USB)

---

##  How It Works

1. Webcam captures video frames
2. MediaPipe detects hand landmarks
3. Raised fingers are counted using landmark positions
4. The finger count is sent via serial (`0–5`)
5. Arduino reads the value and lights LEDs accordingly

---

##  Hardware Setup

* Arduino pins: **9, 10, 11, 12, 13**
* 5 LEDs (with resistors)
* USB connection to PC

---

##  How to Run

1. Upload the Arduino sketch to the board
2. Install Python dependencies:

   ```bash
   pip install opencv-python mediapipe pyserial
   ```
3. Update the correct serial port in the Python script
4. Run the Python program
5. Show your hand to the camera and control the LEDs 🎉

---

##  Limitations

* Thumb detection depends on hand orientation
* Works best with one hand and good lighting
* Demo / educational project (not production-ready)

---

##  Future Improvements

* Gesture-based commands (not only counting)
* LCD or servo motor control

---

##  License

MIT License
