def mm_cm():
    value = int(input("enter value you want to convert from milimeter to centimeter: "))
    output=value/10
    print("value in centimeter is : {}".format(output))

def cm_mm():
    value = int(input("enter value you want to convert from centimeter to meter : "))
    output=value/100
    print("value in meter is : {}".format(output))

def milimeter_meter():
    value = int(input("enter value you want to convert from milimeter to meter : "))
    output=value/1000
    print("value in meter is : {}".format(output))
def meter_centimeter():

    value = int(input("enter value you want to convert from meter to  centimeter : "))
    output=value*100
    print("value in centicmeter is : {}".format(output))
def centimeter_milimeter():

    value = int(input("enter value you want to convert from centimeter to milimeter : "))
    output=value*10
    print("value in milimeter is : {}".format(output))
def meter_milimeter():
    value = int(input("enter value you want to convert from meter to  milimeter : "))
    output = value * 1000
    print("value in milimeter is : {}".format(output))

def converter():
    unit_converter = input ("user want to convert from mm to cm '1' \n cm to m'2'\n from mm to m then '3'\n from m to cm '4' \n cm to mm'5'\n from m to mm then '6' : ")

    if unit_converter =='1' :
        mm_cm()
    elif unit_converter == '2':
        cm_mm()
    elif unit_converter == '3':
        milimeter_meter()

    elif unit_converter =='4' :
        meter_centimeter()

    elif unit_converter =='5' :
        centimeter_milimeter()

    elif unit_converter =='6' :
        meter_milimeter()

converter()

repeat = input ("enter 'Yes'for continue: ")

if repeat == 'Yes':
    converter()
    converter()

