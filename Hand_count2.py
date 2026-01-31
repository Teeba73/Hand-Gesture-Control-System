import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

finger_tips = [4, 8, 12, 16, 20]
finger_pips = [3, 6, 10, 14, 18]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_count = 0

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark

        # Thumb
        if lm[4].x > lm[3].x:
            finger_count += 1

        # Other fingers
        for tip, pip in zip(finger_tips[1:], finger_pips[1:]):
            if lm[tip].y < lm[pip].y:
                finger_count += 1

    cv2.putText(frame, f'Fingers: {finger_count}',
                (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
