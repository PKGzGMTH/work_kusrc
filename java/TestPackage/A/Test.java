/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*
* cd ..
* javac -d B .\B\Test.java
* java -cp B B.Test
*/

package A;
import java.util.Scanner;

public class Test
{
	public static void main(String argv[])
	{
		int num;
		A packageA = new A();
		Scanner sc = new Scanner(System.in);
		System.out.printf("Enter number: ");
		System.out.printf("%d\n", packageA.calculate(sc.nextInt()));
		packageA.say();
	}
}
