# Convex Hull Generator

Tugas Kecil 2 IF2211 Strategi Algoritma Semester II Tahun 2021/2022

Implementation of Convex Hull to Visualize <i>Linear Separability Dataset Test</i>
with <i>Divide and Conquer</i> Algorithm

## Table of Contents
* [General Information](#general-information)
* [Requirement and Installation](#requirement-and-installation)
* [How to Run](#how-to-run)
* [Contact](#contact)

## General Information
This is a simple program to find the convex hull, the smallest convex set, of a set of points in a 2D space by using <b>divide and conquer</b> approach. The input of the program is the <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris">iris</a> and <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine">wine</a> database available from scikit-learn's toy datasets. 

The program first divides the points into two sections separated by a line connecting the 2 furthest x-coordinate points, say p<sub>1</sub> with minimum x value and p<sub>n</sub> with maximum x value and the top section S<sub>1</sub> and bottom S<sub>2</sub>. Then, it finds a new point in a section for each 2 side with the greatest angle from the side's starting point. For S<sub>1</sub> it is p<sub>1</sub> and S<sub>2</sub> it is p<sub>n</sub>. 
This point then divides the section into further subsections which then recursively find their inner greatest angle points until there are no more points to be chosen. These greatest angle points become the corners of sides of the convex hull.

## Requirements and Installation
Python 3 is used to run the program so make sure it is installed. If it is not, download it first <a href="http://www.python.org/downloads/">here.</a>

Make sure ```python``` and ```pip``` is added to the PATH environment variable. If they are not, follow the guides <a href="http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages">here</a> and <a href="http://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command">here</a>.

If you have not installed the libraries <b>matplotlib</b>, <b>numpy</b>, <b>pandas</b>, and/or <b>scikit-learn</b> needed to run the program, install them first by using ```pip```.

Assuming you have cloned this repository (if not, follow the instructions in the next section), you can also install the libraries using this command in the root folder of the repository:
```
pip install -r requirements.txt
```

## How to Run
First, clone the repository:
```
git clone https://github.com/blueguy42/Convex-Hull-Algorithm.git
```
Make sure you are in the root directory of the repository.

Then, to run the program:
```
python src/main.py
```

You should be presented with the following print:
```
================================================
    WELCOME TO AFAN'S CONVEX HULL GENERATOR!
================================================

Made by:
13520023
Ahmad Alfani Handoyo

Choose dataset to use:
1. Iris dataset
2. Wine dataset
Your input (1-2): 
```
Type the number of the dataset you want to use, for example the `iris dataset` by typing 1:
```
Choose pair of attributes:
1. sepal length (cm) vs. sepal width (cm)
2. petal length (cm) vs. petal width (cm)
Your input (1-2):
```
Type the pair of attributes you want to find the convex hull for, for example picking `sepal length (cm) vs. sepal width (cm)` by typing 1. Then, type the name you want to give to the output image of the convex hull graph.
```
Output file name: output
Your convex hull graph of sepal length (cm) vs. sepal width (cm) has successfully been made at file output.png!
```
If for example the filename is output, then you can now go see the resulting graph of the convex hull in the file `test/output.png`.

Et Voilà!
![output](https://user-images.githubusercontent.com/70305222/155628870-f4d8e66e-efd0-4f5d-8c9b-f07f66fe5192.png)

You can proceed to choose to restart or end the program.

## Contact
This program was made by Ahmad Alfani Handoyo (13520023).

You can find and contact me via <a href="http://www.linkedin.com/in/ahmad-alfani-handoyo/">LinkedIn</a>, <a href="http://github.com/blueguy42">GitHub</a>, <a href="http://www.instagram.com/afanhandoyo/">Instagram</a>, or <a href="mailto:ahmadalfanihandoyo1@gmail.com">Email</a>
