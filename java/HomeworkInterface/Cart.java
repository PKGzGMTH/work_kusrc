/*
* Name : Pongsakorn Tippayasomdech
* ID : 6430200850
* Section : 830
*/

package HomeworkInterface;

public class Cart{
	Priceable[]	item = new Priceable[2];

	public int sumPrice()
	{
		return (item[0].getPrice() + item[1].getPrice());
	}
}
