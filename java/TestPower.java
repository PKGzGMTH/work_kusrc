import java.util.Scanner;
public class TestPower
{
	static int power(int base, int power)
	{
		if (power > 0)
			return (base * power(base, power - 1));
		else
			return (1);
	}

	public static void main(String argv[])
	{
		int num1, num2;
		Scanner sc = new Scanner(System.in);
		System.out.printf("Enter a number 1: ");
		num1 = sc.nextInt();
		System.out.printf("Enter a number 2: ");
		num2 = sc.nextInt();
		System.out.printf("the result is %d\n", power(num1, num2));
	}
}
