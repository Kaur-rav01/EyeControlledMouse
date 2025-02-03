import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    #print(landmark_points)
    frame_h,frame_w,_=frame.shape
    
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for i, landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            #print(x,y)
            cv2.circle(frame,(x,y),3,(0,255,255))
            if i==0:
                screen_x=screen_w*landmark.x
                screen_y=screen_h*landmark.y
                pyautogui.moveTo(screen_x,screen_y)
            left=[landmarks[145],landmarks[159]]
            for landmark in left:
                x=int(landmark.x*frame_w)
                y=int(landmark.y*frame_h)
                cv2.circle(frame,(x,y),3,(0,255,255))
            #print(left[0].y,left[1].y)
            if(left[0].y-left[1].y)<0.02:
                pyautogui.click()
                pyautogui.sleep(1)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
