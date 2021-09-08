import time
# import moviepy.editor as mop

import cv2
import mediapipe as mp

from Face.FaceMeshModule import FaceMeshDetector
import hichemModule as hm
detector1 = hm.handDetector(detectionCon=0.6, maxHands=1)

tipIds = [4, 8, 12, 16, 20]
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()

# cap = cv2.VideoCapture('PoseVideos/12.mp4')
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)

pTime = 0
while True:
    success, img = cap.read()
    img2, faces = detector.findFaceMesh(img, True)
    if len(faces) != 0:
        print(faces[0])
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    results1 = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results1.pose_landmarks:
        mpDraw.draw_landmarks(img, results1.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results1.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Hichem", img)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
