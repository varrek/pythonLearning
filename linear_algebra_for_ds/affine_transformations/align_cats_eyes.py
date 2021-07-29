import numpy as np
import cv2
import pandas as pd
import glob
from pathlib import Path

desiredLeftEye = np.array([44, 64])
desiredRightEye = np.array([84, 64])
desiredFaceWidth = desiredFaceHeight = 128


def getEyeAngleAndDistance(rightEye, leftEye):
    dY = rightEye[0][1] - leftEye[0][1]
    dX = rightEye[0][0] - leftEye[0][0]
    angle = np.degrees(np.arctan2(dY, dX))
    dist = np.sqrt((dX ** 2) + (dY ** 2))
    return angle, dist


df = pd.read_csv('cats.csv')
for image in glob.iglob('./*.jpg', recursive=True):
    p = Path(image)
    name = p.name
    image = cv2.imread(image)
    cv2.imshow('original', image)
    leftEye = df[df['file'] == name][['x1', 'y1']].to_numpy()
    rightEye = df[df['file'] == name][['x2', 'y2']].to_numpy()
    angle, dist = getEyeAngleAndDistance(rightEye, leftEye)
    desiredDist = (desiredRightEye[0] - desiredLeftEye[0])
    # desiredDist *= desiredFaceWidth
    scale = desiredDist / dist
    center = ((leftEye[0][0] + rightEye[0][0]) / 2, (leftEye[0][1] + rightEye[0][1]) / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    tX = desiredFaceWidth * 0.5
    tY = desiredLeftEye[1]
    M[0, 2] += (tX - center[0])
    M[1, 2] += (tY - center[1])
    (w, h) = (desiredFaceWidth, desiredFaceHeight)
    rotated = cv2.warpAffine(image, M, (w, h), cv2.INTER_LINEAR)
    # cv2.imshow('processed', rotated)
    # cv2.waitKey(0)
    cv2.imwrite(f'{name}_128.jpg', rotated)