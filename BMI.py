#Create a BMI Calculator using Gooey where the user enters weight and height.
from gooey import Gooey, GooeyParser

@Gooey(program_name="BMI Calculator")
def main():
    parser = GooeyParser(description="BMI Calculator")
    parser.add_argument('weight', type=float, help='Enter your weight in kg')
    parser.add_argument('height', type=float, help='Enter your height in cm')
    args = parser.parse_args()

    # convert height from cm to meters
    height_m = args.height / 100
    bmi = args.weight / (height_m ** 2)

    print(f'Your BMI is {bmi:.2f}')

if __name__ == '__main__':
    main()
