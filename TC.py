# Temperature Converter (with dropdown)
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from the source unit to Celsius
    if from_unit == 'Celsius':
        celsius = value
    elif from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5.0/9.0
    elif from_unit == 'Kelvin':
        celsius = value - 273.15

    # Convert from Celsius to the target unit
    if to_unit == 'Celsius':
        return celsius
    elif to_unit == 'Fahrenheit':
        return (celsius * 9.0/5.0) + 32
    elif to_unit == 'Kelvin':
        return celsius + 273.15
from gooey import Gooey, GooeyParser
@Gooey(program_name="Temperature Converter")
def main():
    parser = GooeyParser(description="Convert temperatures between different units.")
    parser.add_argument('value', type=float, help='Enter the temperature value to convert')
    parser.add_argument('from_unit', choices=['Celsius', 'Fahrenheit', 'Kelvin'], help='Select the unit to convert from')
    parser.add_argument('to_unit', choices=['Celsius', 'Fahrenheit', 'Kelvin'], help='Select the unit to convert to')
    args = parser.parse_args()
    result = convert_temperature(args.value, args.from_unit, args.to_unit)
    print(f'{args.value} {args.from_unit} is {result:.2f} {args.to_unit}')
    
if __name__ == '__main__':
    main()
# Temperature Converter (with dropdown)

    