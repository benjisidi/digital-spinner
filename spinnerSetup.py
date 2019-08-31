from distutils.core import setup
import py2exe

setup_dict = dict(

	console = [{
			"script":"spinner.py",
			"icon_resources": [(0, "spinner.ico")],
			}],
	)
setup(**setup_dict)
setup(**setup_dict)
