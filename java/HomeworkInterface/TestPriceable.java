/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*/

package HomeworkInterface;

import java.util.Scanner;

public class TestPriceable {
	public static void main (String [] args)
	{
		int		input, cpu;
		Cart	cart = new Cart();
		java.util.Scanner	sc = new Scanner(System.in);
		for (int i = 0; i < 2; i++)
		{
			System.out.printf("\nSelect your item %d\n[1] Computer\n[2] Laptop\nSelect: ", i + 1);
			input = sc.nextInt();
			System.out.printf("\nSelect your CPU\n[1] Intel\n[2] AMD\nSelect: ");
			cpu = sc.nextInt();
			if (input == 1)
				cart.item[i] = new Computer(cpu);
			else if (input == 2)
				cart.item[i] = new Laptop(cpu);
			System.out.println("====================");
		}
		System.out.println("\n===== Summarize ====");
		System.out.println("1. " + cart.item[0].getInfo());
		System.out.println("2. " + cart.item[1].getInfo());
		System.out.printf("total price: %d Baht\n\n", cart.sumPrice());
	}
}
