system.configuration [
	engine = python;
	handler = raspberry;
	gpioUse = true;
]
system.dataBind [
	save.Data(
		engine{}
		handler{}
		gpioUse{}
		Process.Settings.SaveTo['/home/pi/settings.ex']
		System.Log.SaveTo['/home/pi/log.ex']
		err.SaveTo['/home/pi/err.ex']
	)
]