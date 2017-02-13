import cv2
import numpy as np
import VisionUtils


class FollowLine:
    def __init__(self, parent):
        self.rover = parent


    def isUpdate(self):
        pass

    def update(self):
        self.__findLines()

    def __findLines(self):


        img   = self.rover.camera.read()

        rImg  = VisionUtils.isolateColor(img,   [150, 50, 50],  [30, 255, 255])
        rGray = cv2.cvtColor(rImg, cv2.COLOR_BGR2GRAY)

        ret, rThresh = cv2.threshold(rGray, 50, 255, cv2.THRESH_BINARY)
        edges = cv2.Canny(rThresh, 20, 40)

        # cv2.imshow('t', rThresh)
        cv2.imshow('r', rThresh)
        cv2.imshow('e', edges)


        # # Test 1
        # lines = cv2.HoughLines(image=edges, rho=1, theta=np.pi/180, threshold=50) # 1, np.pi / 180, 200)
        # if lines is None:
        #     cv2.waitKey(3500)
        #     return
        #
        # for line in lines[:10]:
        #     for rho, theta in line:
        #         a = np.cos(theta)
        #         b = np.sin(theta)
        #         x0 = a * rho
        #         y0 = b * rho
        #         x1 = int(x0 + 1000 * (-b))
        #         y1 = int(y0 + 1000 * (a))
        #         x2 = int(x0 - 1000 * (-b))
        #         y2 = int(y0 - 1000 * (a))
        #
        #         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # print("Found lines: ", len(lines))

        # Test 2
        # Test 1


        print("Doing thing!")
        # lines = cv2.HoughLinesP(edges, 1, np.pi, threshold=25, minLineLength=50, maxLineGap=10)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=25, minLineLength=50, maxLineGap=50)

        if lines is not None:
            lines = lines[0].tolist()

            for x1, y1, x2, y2 in lines:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

            # Debug
            print("Lines:", len(lines))
            cv2.imshow('Edge', img)


        # lines = vertLines + horzLines

        # if lines is None:
        #     cv2.waitKey(3500)
        #     return

        # for line in lines[:10]:
        #     for rho, theta in line:
        #         a = np.cos(theta)
        #         b = np.sin(theta)
        #         x0 = a * rho
        #         y0 = b * rho
        #         x1 = int(x0 + 1000 * (-b))
        #         y1 = int(y0 + 1000 * (a))
        #         x2 = int(x0 - 1000 * (-b))
        #         y2 = int(y0 - 1000 * (a))
        #
        #         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)




        cv2.waitKey(5000)

