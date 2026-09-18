#-----Calculating the area and volume of multiple shapes------

import math


class shape:
    def get_area(self):
        pass
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("please enter a valid number")
                continue
            return value
        except ValueError:
            print("Wrond input,please enter a number")

def main():
    while True:
        print("_-_-Calculating Area and Volume_-_-")
        print("01.Calculate Area")
        print("02.Calculate Volume")

#--------Selecting the main option--

        main_choice=input("Enter your choice (1 or 2) :")
        if main_choice in ["1","2","02","01"]:
            main_choice = main_choice.lstrip("0")
            break
        else:
            print("Wrong input,please enter 1 or 2")
    if main_choice == "1":
        while True:
            print("Area Calculating")
            print("01.Rectangle")
            print("02.squre")
            print("03.circle")
            shape_choice = input("Enter Your choice :")
            if shape_choice == "1":
                while True:
                    width = get_positive_number("Enter width :")
                    height = get_positive_number("Enter height :")
                    Area = width * height
                    print(f"Rectanglr Area :{Area:.2f} ")
                    break
                #convert the resulting value to two decimal places

            elif shape_choice == "2":
                while True:
                    width = get_positive_number("Enter width :")
                    height = get_positive_number("Enter height :")
                    Area = width * height
                    print(f"Circle Area :{Area:.2f}")
                    break

            elif shape_choice == "3":
                while True:
                    radius = get_positive_number(number)
                    Area = math.pi * radius ** 2
                    print(f"Circle Area :{Area:.2f}")
                    break

            else:
                print("wrong input")

    elif main_choice == "2":
        while True:
            print("Volumr Calculation")
            print("01.Cube")
            print("02.Cylinder")
            print("03.Rectangle")
            shape_choice = input("Enter your choice :")

            if shape_choice == "1":
                side = get_positive_number("enter side :")
                value = side**3
                print(f"Cube Value :{value:.2f}")
                break

            elif shape_choice == "2":
                radius = get_positive_number("enter radius :")
                value = math.pi*radius**2
                print(f"Cylinder Value :{value:.2f}")
                break

            elif shape_choice == "3":
                width = get_positive_number("enter width :")
                height = get_positive_number("enter height :")
                length = get_positive_number("enter length :")
                value = width*height*length
                print(f"rectangle value :{value:.2f}")
                break

            else:
                print("wrong input")
    else:
        print("wrong input")
    print("Thank you ")


if __name__ == "__main__":
    main()






