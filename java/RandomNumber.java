/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*/
import java.lang.Math;
import java.util.Scanner;

public class RandomNumber
{
	public static void main (String args[])
	{
		Scanner sc = new Scanner(System.in);
		int	number = (int) (Math.random() * 100);
		int	predict = -1;
		while (predict != number)
		{
			System.out.printf("Enter your number: ");
			predict = sc.nextInt();
			if (predict < number)
				System.out.printf("\nMore than >>\n\n");
			else if (predict > number)
				System.out.printf("\nLess than <<\n\n");
			else
				System.out.printf("\nYou're correct :D\n");
		}
		sc.close();
	}
}
