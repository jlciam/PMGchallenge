# Short Answers #

1. If you needed to retrieve your .csv data from a multitude of 3rd party services (ie: Google sheets), 
how would you structure your code in such a way that you could add on additional inputs in the future?
```
  The usage of the arg parser was exactly for this reason. It allows for me to easily modify the expected input of the 
program in the future to accept flags or additional parameters. ArgParser is great for this reason. This also sets 
up the help flag so the documentation stays up to date as well with added parameters.
```

2. Are there any additional details that you could have used in order to make more effective design decisions? 
List any questions or clarifications you would have requested before beginning this project.
```
  Knowing the useage of the program rather than just the expected output is always important context, so I would have 
asked what the business use case of this program would have been. Also, since large data files are to be processed,
having an idea of the desired runtime expectations would be nice to have to run tests against.
```

3. If you were to pass this problem off to a junior developer, how would you approach structuring a project plan for them?
```
  If I were to pass this problem off to a junior developer, I would break it down into a series of tasks:
  
  First, I would have them focus on thinking of the basic test cases, reading in data from the files and handling bad 
inputs. They could just have the program print out the rows as is, or just count them if thats an easier step for them. 
I would note to them that they need to only account for one header between all the files and to expect the program to
access all rows besides the header, at least once.
  Then, their next task would be to figure out how to add the new file_name column to the header. I would recommend to them 
that its better to access one of the files twice rather than having to check if its a header row each time. That would 
then lead to printing out these rows they are accessing and adding on the file name of the file it came from.
  I would recommend they write up tests as they go through these. Tests to check inputs, tests to check they got the 
headers correctly, then last, test the expected output is as expected.

If they used something like pandas, I would let them know the downsides of using it, which is it can easily use up RAM for 
larger files so streaming the files one row at a time is a safer approach.
```

4. If 1 story point is a single work day, how many story points would you estimate it would take for the junior developer 
on this project?
```
  I would say 2 to 3 story points, depending on their familiarity with python and unittests module. I think their rate 
would depend on mid-/senior- dev being available to answer questions when they get stuck.
```

5. Are there any feature extensions that you would like to implement that are outside the base requirements? 
If so, list them here along with the requirements.
```
  Some feature extensions I could see being useful are:
  * Printing the result out to a output.csv file -- this would require creating an output file for the rows to be written.
  * Counting how many rows came from each file -- this would require a counter for each file that's saved and printed at the end.
```