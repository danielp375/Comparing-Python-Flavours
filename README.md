# Testing-Flavours-of-Python
A simple experiment to test which flavour of python is faster.  
<br />

# Flavours used
- CPython
- Anaconda
- PyPy
- Anaconda (Jupyter Labs)
<br />

# Dataset
We have used a mobile price dataset which shows the price of several mobile phone models along with it's characteristics.  
<br />

# Program
In the program, we use pandas to import the dataset and display it's details, first five columns and it's correlation.
The time function is used to calculate the time taken to run the program.  
<br />
<br />

# Step1: Using CPython
The first approach is to use the tradition cpython flavour to run the code.  
By running the program using cpython, the program took 0.84 seconds to run. 
  <br />

![cpython output](cpython_tm.jpg)  
<br />
<br />

# Step2: Using Anaconda on VS Code
The second approach uses Anaconda, run on VSCode.  
This approach took more time, taking 1.86 seconds.  
<br />

![anaconda output](anaconda_tm.jpg)  
<br />
<br />


# Step3: Using Anaconda on Jupyter labs
The third approach uses Jupyter labs to execute the program.  
This approach took the least time of 0.03 seconds.
<br />

![jupyter labs output](jlab_tm.jpg)  
<br />
<br />

# Step4: Using PyPy
The final approach was by using PyPy.  
This approach took the most time of 2.41 seconds
<br />

![pypy output](pypy_tm.jpg)  
<br />
<br />

# Conclusion
Thus we can conclude that from all the flavours of python used in this experiment, running python on Anaconda using Jupyter labs is the fastest.  
The flavours along with the time taken to execute the program are as follows:  
Flavours | Time (in seconds)
| :---: | :---:
CPython | 0.84
Anaconda | 1.86
Anaconda (Jupyter Labs) | 0.03
PyPy | 2.41 

