# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
	The goal of this project is to make a program that prints links on webpages it visits. The way that this works is the user inputs a link, and possibly (not required) an maximum depth. If no arguments are provided, a usage error is printed. If the link is not provided, an error will be thrown (not by the libraries imported though). The program then prints the URL that the user provided, and searches that URL for any links. When a link is found, the link is printed, and the link is followed to a new webpage. The program then searches for more links on the newpage and follows the link to another webpage, as well as printing it, if it is a link it has not seen before (any link with any differences in characters besides different fragments are considered different links). The maximum depth comes into play by specifying how many links the crawler can click on for a webpage, with the default set at 3. For each level of depth reached, 4 spaces are printed before the URL is printed. If an invalid URL is reaches, the program simply backs out and moves on to the next URL. The original URL must be an absolute URL, and if a relative URL is given, a usage message is printed. After finishing, or being aborted, the program should print the amount of webpages visited, along with the time. Visited URLs are stored in a set so that they are not visited again.
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
	No global variables used. 
	Exceptions are handled properly.
	Runs as the instructions listed above.
	No smelly code. 
    *   List what you already know how to do.
	I know how to do recursive calls, and how to do increment variables while making recursive calls 
    *   Point out any challenges that you can foresee.
	I'm not quite sure how to incorporate the libraries, or how exception handling works
*   [ ] List all of the data that is used by the program, making note of where it comes from.
	The data generally comes from webpages from the internet, with the exception of the intial URL, which is provided by the user.
    *   Explain what form the output will take.
	Each URL visited will be printed to the console, with indentation corresponding to the depth
*   [ ] List the algorithms that will be used (but don't write them yet).
	crawl
	functions that handles command line arguments
*   [ ] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
	



  	  

Import necessary libraries 	  


This function does the actual crawling of the internet. It takes in a URL, max depth, and depth as parameters, and outputs different URLs visited to the console	  
	  	  
   Crawl function with parameters url,  max depth, and depth
	If depth is greater than max depth, return;
  	For depth iterations
		Print 4 spaces
Print url without newline 	  	  
    Try the following code if an exception is made, move on  	  
     A request is equal to get request
     Links array is equal to  links (tags with href) in a request	  	  	 
     Combine past URL with current URL to make an absolute URL
    If URL is a HTTP or HTTPS
Print the URL plus indentation corresponding the the current depth  	  	  
    	Visit URL  	  	  
    URL without fragment is equal to URL without fragment  	  	  
    Add URL without fragment to set     	  	  
   Use this function with the same parameters for every array in links, adding 1 to current depth for the position in array  	  	  
    return  	  	  
 

This is the main function. This function make sure that the command arguments given are valid, as well as calling the crawl function, and printing out how long the program took and number of webpages visited.	  
Main function	  	     	  	  
    if the system argument is less than 2  	  	  
        Print please give a valid argument	  	  
        exit  	  
    Else url is equal to the index of one in the arguments  
    If url does not have :// at an index that is not at the beginning or the end 	  	  
    	Print a usage error that URL is not absolute  	  	  

    If there is a 3rd argument on the command line
 Try to convert maxDepth into integer and make that max depth
On exception, maxDepth is equal to 3 	  
   Else maxDepth is equal to 3  	  	  


   A set is equal to a blank set
   Plural is equal to s if maxDepth is not equal to one, else plural is equal to a space  	  	  
    Print that Crawling from url to a maximum depth of maxDepth link plural	  	  

   Variable that says what time it is currently
  	  	  

    Try 
Crawl method with maxdepth, current depth of 0 and URL
    Catch keyboard interrupt

``Finally
Time spent equal current time minus variable that kept track of time above  	  
	Print time spent 
    	Print length of set	  	  



*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
	If no arguments are given, a usage error for that is given. example: simply running crawler.py
	If a bad URL is given, a usage error for that is given. example: running crawler.py usu.edu
	If there are too many arguments, nothing happens as long as the first argument that is given to the program to use is valid. example: running crawler.py https://usu.edu 4 yadayadayada
	If the 2nd argument is invalid, the default maxDepth will be used instead.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*
     


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.
	In this part, I ended up having to add the set as a parameter in crawl and calling it in main instead of it simply being crawl.
	In addition, I also ended up moving some of the code to the for loop in crawl.

## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.
	Got an indentation error after the 'except' on line 115
	Fixed by adding a line

	Got a usage error when I shouldn't have
	Fixed by changing the conditions for finding absolute URL

	I used chatGPT to help fix an error I was getting related to the Beautiful Soup library
	I was inputting a String for urls found on a webpage where it needed a list, so code was change to be a list
	
	I was unable to visit more than the first webpage
	Fixed by negating the condition for recursion in crawl

	Program crashed if there was only one argument
	Added an if statement that checked if there was more than one argument to accomodate this

	Program didn't follow the correct rule for depth
	Changed the recursion call to instead follow currentDepth instead of the i in the for loop
	


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work? I'm always a little confused by Recursion, and I don't quite understand how the libraries work
        *   If a bug is reported in a few months, how long would it take you to find the cause? Fairly quickly, but only because the program is small
    *   Will your documentation make sense to...
        *   ...anybody besides yourself? yes
        *   ...yourself in six month's time? yes
    *   How easy will it be to add a new feature to this program in a year? Fairly easy because the program is small
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware? should be
        *   ...the operating system? yes
        *   ...to the next version of Python? as long as something doesn't drastically change, yes
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
