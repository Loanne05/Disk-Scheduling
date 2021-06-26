from matplotlib import pyplot as plt
import math
def run():
    sequence = list(map(int, input("Enter sequence (must be separated by space): ").split()))
    start = int(input("Enter Head Start: "))
    CYLINDER_MAX = 199
    #INPUTS: 98 183 37 122 14 124 65 67

    def SCAN(sequence, start, direction):
        temp = sequence.copy()
        left = []
        right = []
        x = []
        y = []
        x_approx = []
        y_approx = []
        headmovement = 0
        headmovement_approx = 0
        x.append(start)
        if (direction == "Left"):
            for i in temp:
                if i < start:
                    left.append(i)
                else:
                    right.append(i)
            left.sort(reverse=True)
            for i in left:
                x.append(i)
            x.append(0)
            right.sort()
            for i in right:
                x.append(i)

            x_approx.append(start)
            x_approx.append(min(x))
            x_approx.append(max(x))
            headmovement_approx = abs(start - 0)
            headmovement_approx = headmovement_approx + abs(0 - max(x))
            plt.title("SCAN SCHEDULING ALGORITHM (To the left)")
        elif (direction == "Right"):
            for i in temp:
                if i > start:
                    right.append(i)
                else:
                    left.append(i)
            right.sort()
            for i in right:
                x.append(i)
            x.append(CYLINDER_MAX)
            left.sort(reverse=True)
            for i in left:
                x.append(i)
            x_approx.append(start)
            x_approx.append(max(x))
            x_approx.append(min(x))
            headmovement_approx = abs(start - 199)
            headmovement_approx = headmovement_approx + abs(199 - min(x))
            plt.title("SCAN SCHEDULING ALGORITHM (To the right)")
        y_approx.append(0)
        size = len(x)
        for i in range(0, size):
            y.append(-i)
            if (x[i] == 0 or x[i] == 199):
                y_approx.append(-i)
            if i != (size - 1):
                headmovement = headmovement + abs(x[i] - x[i + 1])
            else:
                y_approx.append(-i)
        string = 'Headmovement = ' + str(headmovement) + ' cylinders'
        string2 = str(x)

        plt.plot(x, y, color="violet", markerfacecolor='red', marker='o', markersize=5, linewidth=2, label="SCAN")
        """plt.plot(x_approx, y_approx, dashes=[6, 2], color="blue", markerfacecolor='blue', marker='D', markersize=5,
                 linewidth=0.5, label="Approx SCAN")"""
        plt.ylim = (0, size)
        plt.xlim = (0, CYLINDER_MAX)
        plt.yticks([])

        plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
        plt.text(182.5, -12.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
        plt.show()

    SCAN(sequence,start,"Left")
    SCAN(sequence, start, "Right")