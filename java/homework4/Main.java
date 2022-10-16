/*
 * This file is for test Triangle.java Square.java which extends Shape.java
 * by Write function Override the getArea() for each Shape.
 *
 * NAME: Pongsakorn Tippayasomdech
 * STUDENT ID: 6430200850
 * SECTION: 830
 *
 */

package homework4;

public class Main {
	public static double sumArea(Shape[] a) {
		double sum = 0;
		for (Shape s: a)
			sum += s.getArea();
		return (sum);
	}
	public static void main(String[] args) {
		Shape[] shapes = {
			new Triangle(4, 5),
			new Square(3)
		};
		System.out.println(sumArea(shapes));
	}
}
