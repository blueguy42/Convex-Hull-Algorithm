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
This is a simple program to find the convex hull, the smallest convex set, of a set of points in a 2D space by using <b>divide and conquer</b> approach. The input of the program is the <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris">iris</a> and <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine">wine</a> database available from scikit-learn's toy dataset. 

The program first divides the points into two sections separated by a line connecting the 2 furthest x-coordinate points, say p<sub>1</sub> with minimum x value and p<sub>n</sub> with maximum x value and the top section S<sub>1</sub> and bottom S<sub>2</sub>. Then, it finds a new point in a section for each 2 side with the greatest angle from the side's starting point. For S<sub>1</sub> it is p<sub>1</sub> and S<sub>2</sub> it is p<sub>n</sub>. 
This point then divides the section into further subsections which then recursively find their inner greatest angle points until there are no more points to be chosen. These greatest angle points become the points that make up the convex hull.

## Requirement and Installation

Install semua library yang dibutuhkan

atau dapat menjalankan
```
pip install -r requirements.txt
```

## How to Run

## Contact
This program was made by Ahmad Alfani Handoyo (13520023).

You can find and contact me via <a href="http://www.linkedin.com/in/ahmad-alfani-handoyo/">LinkedIn</a>, <a href="http://github.com/blueguy42">GitHub</a>, <a href="http://www.instagram.com/afanhandoyo/">Instagram</a>, or <a href="mailto:ahmadalfanihandoyo1@gmail.com">Email</a>