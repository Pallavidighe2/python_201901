def income_tax_calculaor():
    global Total_Income
    Total_Income = input("Enter your Total Annual income :  ")
    Total_Income = int(Total_Income)
    investment()


def investment():
    investment = input("user have investment then 'S' or 'N':  ")

    if investment == "N":
        tax_calculate_without_deduction()
    elif investment == "S":
        tax_calculate_with_deduction()


def tax_calculate_without_deduction():


    if Total_Income <= 250000:
        print("You don't pay any tax ")
    elif 250001 <= Total_Income <= 500000:
        A = Total_Income - 250000
        Tax1 = A * 0.05
        print("you have to pay Tax1 {}".format(Tax1))
    elif 500001 <= Total_Income <= 1000000:
        A = Total_Income - 250000
        B = A - 250000
        Tax2 = (B * 0.2) + 12500
        print("you have to pay Tax1 {}".format(Tax2))
    elif Total_Income >= 1000000:
        A = Total_Income - 250000
        B = A - 250000
        C = B - 500000
        Tax3 = (C * 0.3) + 100000 + 12500
        print("you have to pay Tax1 {}".format(Tax3))


def tax_calculate_with_deduction():

    deduction()
    taxable_income =  Total_Income-Total_Deduction
    taxable_income=int(taxable_income)
    print(taxable_income)
    if taxable_income <= 250000:
        print("You don't pay any tax ")
    elif 250001 <= taxable_income <= 500000:
        A = taxable_income - 250000
        Tax1 = A * 0.05
        print("you have to pay Tax1 {}".format(Tax1))
    elif 500001 <= taxable_income <= 1000000:
        A = taxable_income - 250000
        B = A - 250000
        Tax2 = (B * 0.2) + 12500
        print("you have to pay Tax1 {}".format(Tax2))
    elif taxable_income >= 1000000:
        A = taxable_income - 250000
        B = A - 250000
        C = B - 500000
        Tax3 = (C * 0.3) + 100000 + 12500
        print("you have to pay Tax1 {}".format(Tax3))
def deduction():
    global Total_Deduction
    Deduction_Under_80CCD()
    Deduction_Under_80C()
    Deduction_for_medicalim()
    Total_Deduction = x + NPS + mediclaim
    print(Total_Deduction)


def Deduction_Under_80C():
    print("YOur Deduction under 80C max 1,50,000")
    # Enter your dedection
    LIC = input("Enter the amount you invest for LIC : ")
    National_Saving_Certificate = input(
        "Enter the amount you invest for National_Saving_Certificate : ")
    Invetsment_In_PF = input(
        "Enter the amount you invest for Invetsment_In_PF : ")
    Tuition_Fee = input("Enter the amount you invest for Tuition_Fee : ")
    Mutual_Fund = input("Enter the amount you invest for Mutual_Fund : ")
    Bank_FD = input("Enter the amount you invest for Mutual_Fund : ")
    House_Loan_Repayment = input(
        "Enter the amount you invest for House_Loan_Repayment : ")
    Employee_PF = input("Enter the amount you invest for Employee_PF : ")
    Stamp_Duty = input("Enter the amount you invest for Stamp_Duty : ")
    Residential_Housing_Loan = input(
        "Enter the amount you invest for Residential_Housing_Loan : ")
    Sukanya_Samrudhhi_Scheme = input(
        "Enter the amount you invest for Sukanya_Samrudhhi_Scheme : ")

    list = [LIC, National_Saving_Certificate, Invetsment_In_PF, Bank_FD,
            House_Loan_Repayment, Employee_PF, Stamp_Duty,
            Residential_Housing_Loan, Sukanya_Samrudhhi_Scheme]

    print(list)
    global x
    x = 0
    for num in list:
        x = x + int(num)
    print("x = ", x)
    if x <=150000:
        print(x)
    else:
        x=150000
        print(x)

def Deduction_Under_80CCD():

    global NPS

    print("Additional deduction under 80CCD 50,000")

    NPS = int(input("Enter amount investment for NPS: "))

    if NPS <= 50000:
        print(NPS)
    else:
        NPS = 50000
        print(NPS)
def Deduction_for_medicalim():
    global  mediclaim
    print("investment under section 80 D max 15,000")
    mediclaim = int(input("Enter your mediclaim amount: "))
    if mediclaim <= 15000:
        print(mediclaim)
    else:
        mediclaim = 15000
        print(mediclaim)
income_tax_calculaor()