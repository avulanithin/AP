# Simple Interest Calculator using gooye
from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description="Simple Interest Calculator")
    parser.add_argument('principal', type=float, help='Enter the principal amount')
    parser.add_argument('rate', type=float, help='Enter the interest rate')
    parser.add_argument('time', type=float, help='Enter the time period')
    args = parser.parse_args()
    si = (args.principal * args.rate * args.time) / 100
    print(f'Simple Interest is: {si:.2f}')

if __name__ == '__main__':
    main()