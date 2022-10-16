/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*/

package HomeworkInterface;

public class Laptop implements Priceable{
	String CPUName;

	Laptop(int cpu) {
		if (cpu == 1)
			CPUName = "Intel";
		else if (cpu == 2)
			CPUName = "AMD";
	}

	public int getPrice() {
		if (CPUName.equals("Intel"))
			return (55000);
		else
			return (52000);
	}

	public String getInfo()
	{
		return (CPUName + " Laptop " + getPrice() + " Baht");
	}
}
