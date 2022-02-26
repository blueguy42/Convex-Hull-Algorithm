# Convex Hull Generator

Tugas Kecil 2 IF2211 Strategi Algoritma Semester II Tahun 2021/2022

Implementation of Convex Hull to Visualize <i>Linear Separability Dataset Test</i>
with <i>Divide and Conquer</i> Algorithm

## Table of Contents
* [General Information](#general-information)
* [Requirement and Installation](#requirement-and-installation)
* [How to Run](#how-to-run)
* [Example Program Usage](#example-program-usage)
* [Contact](#contact)

## General Information
This is a simple library to find the convex hull, the smallest convex set, of a set of points in a 2D space by using <b>divide and conquer</b> approach. An accompanying program is available to use the library. The input of the program are the <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris">iris</a>, <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine">wine</a>, <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits">digits</a>, and <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine">breast cancer wisconsin</a> datasets available from scikit-learn's toy datasets. 

The algorithm first divides the points into two sections separated by a line connecting the 2 furthest x-coordinate points, say p<sub>1</sub> with minimum x value and p<sub>n</sub> with maximum x value and the top section S<sub>1</sub> and bottom S<sub>2</sub>. Then, it finds a new point in a section for each 2 side with the greatest angle from the side's starting point. For S<sub>1</sub> it is p<sub>1</sub> and S<sub>2</sub> it is p<sub>n</sub>. This point then divides the section into further subsections which then recursively find their inner greatest angle points until there are no more points to be chosen. These greatest angle points become the corners of sides of the convex hull.

The program shows the graph of the resulting convex hull and allows the user to save the graph to a PNG image in the `test` folder.

## Requirement and Installation
Python 3 is used to run the program and library so make sure it is installed. If it is not, download it first <a href="http://www.python.org/downloads/">here.</a>

Make sure ```python``` and ```pip``` is added to the PATH environment variable. If they are not, follow the guides <a href="http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages">here</a> and <a href="http://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command">here</a>.

If you have not installed the modules <b>matplotlib</b>, <b>numpy</b>, <b>pandas</b>, and <b>scikit-learn</b> needed to run the program and library, install them first by using ```pip```.
 Assuming you have cloned this repository (if not, follow the instructions in the next section), you can also install the modules using this command in the root folder of the repository:
```
pip install -r requirements.txt
```

## How to Run
First, clone the repository:
```
git clone https://github.com/blueguy42/Convex-Hull-Algorithm.git
```
The <b>convex hull</b> library is available for use at `src/myConvexHull.py`. 

If you want to run the accompanying program, make sure you are currently in the root directory of the repository.

Then, to run the program:
```
python src/main.py
```

## Example Program Usage
Once you run the program, you should be presented with the following print:
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
3. Digits dataset
4. Breast cancer wisconsin dataset
Your input (1-4): _
```
Type the number of the dataset you want to use, for example the `iris dataset` by typing 1:
```
Choose attribute for x:
1. sepal length (cm)
2. sepal width (cm)
3. petal length (cm)
4. petal width (cm)
Your input (1-4): _
```
Type the attribute for the x coordinate, for example picking `sepal length (cm)` by typing 1. 
```
Choose attribute for y (make sure it is different from 1. sepal length (cm)):
1. sepal length (cm)
2. sepal width (cm)
3. petal length (cm)
4. petal width (cm)
Your input (1-4): _
```
Type the attribute for the y coordinate that is different from the x coordinate, for example picking `sepal width (cm)` by typing 2. 

The graph of the convex hull of `sepal length (cm) vs. sepal width (cm)` will be shown. 
```
Showing convex hull graph of sepal length (cm) vs. sepal width (cm)
Make sure to close the graph pop-up so the program can continue!
```
Close the graph so the program can continue. You have the option to save the graph to an output image.
```
Would you like to save the convex hull graph? (Y/N): Y

Output file name: output
Your convex hull graph of sepal length (cm) vs. sepal width (cm) at output.png has successfully been made at folder test!
```
If for example the filename is <i>output</i>, then you can now go see the resulting graph of the convex hull in the file `test/output.png`.

Et Voilà!

![output](https://user-images.githubusercontent.com/70305222/155628870-f4d8e66e-efd0-4f5d-8c9b-f07f66fe5192.png)

You can proceed to choose another dataset or pair of attributes to analyze or end the program.

## Contact
This program was made by Ahmad Alfani Handoyo (13520023).

You can find and contact me via <a href="http://www.linkedin.com/in/ahmad-alfani-handoyo/">LinkedIn</a>, <a href="http://github.com/blueguy42">GitHub</a>, <a href="http://www.instagram.com/afanhandoyo/">Instagram</a>, or <a href="mailto:ahmadalfanihandoyo1@gmail.com">Email</a>
