"""

"""


class BMICalculator(object):
    """

    """
    def __init__(self):
        self.weight = None
        self.height = None
        self.bmi = None
        self.ideal_weight = None
        self.response = dict()
        _dict = [
            {'message': "you are Obese Class 3",
                    'condition': self.is_obese_3},
            {'message': "you are Obese Class 3",
                    'condition': self.is_obese_2},
        ]

    def main(self):
        self.get_weight_input()
        if not self.weight:
            return self.response

        self.get_height_input()
        if not self.height:
            return self.response

        self.calculate_bmi()
        self.calculate_ideal_weight()
        # self.suggestion()

        return self.response

    def get_weight_input(self):
        try:
            self.weight = float(input("Enter your weight in Kg : "))
        except ValueError:
            self.response = {
                "status": False,
                "message": "Weight input is not float or integer"
            }

    def get_height_input(self):
        try:
            self.height = float(input("Enter your Height in meter : "))
        except ValueError:
            self.response = {
                "status": False,
                "message": "Height input is not float or integer"
            }

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def calculate_ideal_weight(self):
        self.ideal_weight = (self.height * 100) - 100

    def is_obese_3(self):
        return self.bmi > 40



    def suggestion(self):
        if self.ideal_weight < 120:
            print("Your Ideal Weight can not be calculated")

        if self.ideal_weight > 120:
            print("Your Ideal_Weight is : {}".format(self.ideal_weight))
        print("Your BMI is : {}".format(self.bmi))

        if self.bmi < 16:
            _suggestion = "You are Very Severly Underweight"

        elif 16 < self.bmi < 17:
            _suggestion = "You are Severly Underweight"

        elif 17 < self.bmi < 18.5:
            _suggestion = "You are Underweight"

        elif 18.5 < self.bmi < 25:
            _suggestion = "You are Normal in Weight"

        elif 25 < self.bmi < 30:
            _suggestion = "You are overweight"

        elif 30 < self.bmi < 35:
            _suggestion = "You are Obese class 1"

        elif 35 < self.bmi < 40:
            _suggestion = "You are Obese class 2"

        elif self.bmi > 40:
            _suggestion = "you are Obese Class 3"

        else:
            _suggestion = "You are simply tooooo fat."

        self.response = {
            'status': True,
            'suggestion': _suggestion
        }


print(BMICalculator().main())

suggestions_dict = {
    '>40': {'message': "you are Obese Class 3", 'condition': self.is_obese_3},
    '35-40': "you are Obese Class 3" ,
}