# program to calculate distance between two points using Pythagorean Theorem

def Calculate_distance(x1,y1,x2,y2):
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    return distance
def main():
    x1 = float(input("Enter x-coordinates of first point:"))
    y1 = float(input("Enter y-coordinates of first point:"))
    x2 = float(input("Enter x-coordinates of second point:"))
    y2 = float(input("Enter y-coordinates of second point:"))

    distance = Calculate_distance(x1,y1,x2,y2)
    print(f"The distance between two points is:{distance}")
main()