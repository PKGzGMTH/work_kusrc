class	landmark
{
	public void	landmarkName()
	{
		System.out.println("This is no landmark yet.");
	}
}

class thaiLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Thailand's landmark is The Grand Palace.");
	}
}

class cambodiaLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Cambodia's landmark is Angkor Wat.");
	}
}

class vietnamLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("vietnam's landmark is Ha Long Bay.");
	}
}

class philippinesLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Philippines's landmark is Boracay.");
	}
}

class myanmarLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Myanmar's landmark is Bagan.");
	}
}

class malaysiaLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Malaysia's landmark is Kuala Lumpur.");
	}
}

class singaporeLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Singapore's landmark is Marina Bay Sands.");
	}
}

class laosLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Laos's landmark is Luang Prabang");
	}
}

class  indonesiaLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Indonesia's landmark is Komodo Island.");
	}
}

class bruneiLandmark extends landmark
{
	public void landmarkName()
	{
		System.out.println("Brunei's landmark is Kampong Ayer");
	}
}

class ex04
{
	public static void main (String [] argv)
	{
		landmark thailand = new thaiLandmark();
		landmark cambodia = new cambodiaLandmark();
		landmark vietnam = new vietnamLandmark();
		landmark philippines = new philippinesLandmark();
		landmark myanmar = new myanmarLandmark();
		landmark malaysia = new malaysiaLandmark();
		landmark singapore = new singaporeLandmark();
		landmark laos = new laosLandmark();
		landmark indonesia = new indonesiaLandmark();
		landmark brunei = new bruneiLandmark();

		thailand.landmarkName();
		cambodia.landmarkName();
		vietnam.landmarkName();
		philippines.landmarkName();
		myanmar.landmarkName();
		malaysia.landmarkName();
		singapore.landmarkName();
		laos.landmarkName();
		indonesia.landmarkName();
		brunei.landmarkName();
	}
}
