# Recursive Web Crawler User Manual

*   This is the **user manual**, not the **programmer's manual**
    *   Keep your instructions at a user-friendly level.
*   Explain how to run the program
	The following line of code must be run to run this program. 
	```python -m pip install --user -r requirements.txt```

    *   What is the name of the main program file?
	crawler.py
    *   What command-line arguments are needed? 
	The program is run with up to two arguments: a URL, which is required, and a maximum depth, which is optional. The URL must be an absolute URL (absolute URL meaning the URL is in this format: scheme://hostname, with the scheme being either http or https) Relative URLs miss one or more of these parts.
	The maximum depth is how many URLs the program can visit for a particular page. For example, if the depth was two, the program would be allowed to visit the first two URLs on that page.	
	If maximum depth is not specified, the default value is 3.

*   What output does the program produce?
    *   What is shown when the program works correctly?
	The program will print URL of webpages visited with indentation indicating the depth or will print the error messages of webpages that did not work (the program will not crash from this). At the end, it will show the number of webpages visited (including failed ones) and the time it took to visit those webpages.
	Example of an output
	https://google.com
	    https://gmail.com
	Visited 2 websites in .6 seconds
	It should also be noted that when the user tries to kill the program through something like 'control-C', the program will print the amount of webpages and time taken, then exit;
    *   What is shown when an error is encountered
	Possible errors that could be printed include: 
	‘Usage Error: No arguments given. Please provide an absolute URL.’
		This error is caused by no arguments being given when the program is run, using the code ‘python crawler.py’. To not get this error, make sure to add an absolute URL. A valid command that showcases this is ‘python crawler.py https://google.com’ 
	‘Usage Error: URl must be absolute and start with http or https’
		This error is caused by an invalid URL (meaning that the URL given is not absolute), like ‘google.com’. Use the absolute URL, such as ‘https://google.com’ to avoid this error

    *   Provide examples of both!

