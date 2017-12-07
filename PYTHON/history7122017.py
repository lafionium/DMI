Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 5, in <module>
    import mathplotlib.pyplot as plt
ImportError: No module named mathplotlib.pyplot
>>> ================================ RESTART ================================
>>> 
>>> x
array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,
        5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ])
>>> type(x)
<type 'numpy.ndarray'>
>>> len(x)
19
>>> x[3]
1.5
>>> x[0] = 100
>>> x
array([ 100. ,    0.5,    1. ,    1.5,    2. ,    2.5,    3. ,    3.5,
          4. ,    4.5,    5. ,    5.5,    6. ,    6.5,    7. ,    7.5,
          8. ,    8.5,    9. ])
>>> i = 10
>>> x[i]
5.0
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
>>> print range.__doc__
range(stop) -> list of integers
range(start, stop[, step]) -> list of integers

Return a list containing an arithmetic progression of integers.
range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
When step is given, it specifies the increment (or decrement).
For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
These are exactly the valid indices for a list of 4 elements.
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(3,9)
[3, 4, 5, 6, 7, 8]
>>> range(3,9,2)
[3, 5, 7]
>>> ================================ RESTART ================================
>>> 
0 0.0 0.0
1 0.5 0.479425538604
2 1.0 0.841470984808
3 1.5 0.997494986604
4 2.0 0.909297426826
5 2.5 0.598472144104
6 3.0 0.14112000806
7 3.5 -0.35078322769
8 4.0 -0.756802495308
9 4.5 -0.977530117665
10 5.0 -0.958924274663
11 5.5 -0.70554032557
12 6.0 -0.279415498199
13 6.5 0.215119988088
14 7.0 0.656986598719
15 7.5 0.937999976775
16 8.0 0.989358246623
17 8.5 0.798487112623
18 9.0 0.412118485242
>>> ================================ RESTART ================================
>>> 
0 0.0 0.0
0.958851077208
1 0.5 0.479425538604
0.724090892407
2 1.0 0.841470984808
0.312048003592
3 1.5 0.997494986604
-0.176395119557
4 2.0 0.909297426826
-0.621650565443
5 2.5 0.598472144104
-0.914704272088
6 3.0 0.14112000806
-0.983806471499
7 3.5 -0.35078322769
-0.812038535237
8 4.0 -0.756802495308
-0.441455244714
9 4.5 -0.977530117665
0.0372116860039
10 5.0 -0.958924274663
0.506767898185
11 5.5 -0.70554032557
0.852249654743
12 6.0 -0.279415498199
0.989070972573
13 6.5 0.215119988088
0.883733221262
14 7.0 0.656986598719
0.562026756112
15 7.5 0.937999976775
0.102716539697
16 8.0 0.989358246623
-0.381742268
17 8.5 0.798487112623
-0.772737254763
18 9.0 0.412118485242

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 31, in <module>
    delta_y = y[i+1] - y[i]
IndexError: index out of bounds
>>> ================================ RESTART ================================
>>> 
0 0.0 0.0
0.958851077208
1 0.5 0.479425538604
0.724090892407
2 1.0 0.841470984808
0.312048003592
3 1.5 0.997494986604
-0.176395119557
4 2.0 0.909297426826
-0.621650565443
5 2.5 0.598472144104
-0.914704272088
6 3.0 0.14112000806
-0.983806471499
7 3.5 -0.35078322769
-0.812038535237
8 4.0 -0.756802495308
-0.441455244714
9 4.5 -0.977530117665
0.0372116860039
10 5.0 -0.958924274663
0.506767898185
11 5.5 -0.70554032557
0.852249654743
12 6.0 -0.279415498199
0.989070972573
13 6.5 0.215119988088
0.883733221262
14 7.0 0.656986598719
0.562026756112
15 7.5 0.937999976775
0.102716539697
16 8.0 0.989358246623
-0.381742268
17 8.5 0.798487112623
-0.772737254763
18 9.0 0.412118485242

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 31, in <module>
    delta_y = y[i+1] - y[i]
IndexError: index out of bounds
>>> y[19]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    y[19]
IndexError: index out of bounds
>>> ================================ RESTART ================================
>>> 
0 0.0 0.0 0.958851077208
1 0.5 0.479425538604 0.724090892407
2 1.0 0.841470984808 0.312048003592
3 1.5 0.997494986604 -0.176395119557
4 2.0 0.909297426826 -0.621650565443
5 2.5 0.598472144104 -0.914704272088
6 3.0 0.14112000806 -0.983806471499
7 3.5 -0.35078322769 -0.812038535237
8 4.0 -0.756802495308 -0.441455244714
9 4.5 -0.977530117665 0.0372116860039
10 5.0 -0.958924274663 0.506767898185
11 5.5 -0.70554032557 0.852249654743
12 6.0 -0.279415498199 0.989070972573
13 6.5 0.215119988088 0.883733221262
14 7.0 0.656986598719 0.562026756112
15 7.5 0.937999976775 0.102716539697
16 8.0 0.989358246623 -0.381742268
17 8.5 0.798487112623 -0.772737254763
18 9.0 0.412118485242

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 31, in <module>
    delta_y = y[i+1] - y[i]
IndexError: index out of bounds
>>> ================================ RESTART ================================
>>> 
0 0.0 0.0 0.958851077208
1 0.5 0.479425538604 0.724090892407
2 1.0 0.841470984808 0.312048003592
3 1.5 0.997494986604 -0.176395119557
4 2.0 0.909297426826 -0.621650565443
5 2.5 0.598472144104 -0.914704272088
6 3.0 0.14112000806 -0.983806471499
7 3.5 -0.35078322769 -0.812038535237
8 4.0 -0.756802495308 -0.441455244714
9 4.5 -0.977530117665 0.0372116860039
10 5.0 -0.958924274663 0.506767898185
11 5.5 -0.70554032557 0.852249654743
12 6.0 -0.279415498199 0.989070972573
13 6.5 0.215119988088 0.883733221262
14 7.0 0.656986598719 0.562026756112
15 7.5 0.937999976775 0.102716539697
16 8.0 0.989358246623 -0.381742268
17 8.5 0.798487112623 -0.772737254763
>>> ================================ RESTART ================================
>>> 
0 0.0 0.0 1 0.5 0.479425538604 2 1.0 0.841470984808 3 1.5 0.997494986604 4 2.0 0.909297426826 5 2.5 0.598472144104 6 3.0 0.14112000806 7 3.5 -0.35078322769 8 4.0 -0.756802495308 9 4.5 -0.977530117665 10 5.0 -0.958924274663 11 5.5 -0.70554032557 12 6.0 -0.279415498199 13 6.5 0.215119988088 14 7.0 0.656986598719 15 7.5 0.937999976775 16 8.0 0.989358246623 17 8.5 0.798487112623
>>> ================================ RESTART ================================
>>> 
>>> x
array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,
        5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ])
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 38, in <module>
    plt.plot(x,y_prim)
  File "/usr/lib/pymodules/python2.7/matplotlib/pyplot.py", line 2987, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 4137, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 317, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 295, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 237, in _xy_from_xy
    raise ValueError("x and y must have same first dimension")
ValueError: x and y must have same first dimension
>>> len(x)
19
>>> len(t_prim)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    len(t_prim)
NameError: name 't_prim' is not defined
>>> len(y_prim)
18
>>> x[:n-1]
array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,
        5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5])
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 51, in <module>
    y_prim2.append(delta_y_prim / delta_x)
NameError: name 'delta_y_prim' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 51, in <module>
    y_prim2.append(delta_y_prim / delta_x)
NameError: name 'delta_y_prim' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 51, in <module>
    y_prim2.append(delta_y_prim / delta_y)
NameError: name 'delta_y_prim' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 52, in <module>
    y_prim2.append(delta_y_prim / delta_y)
NameError: name 'y_prim2' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 53, in <module>
    plt.plot(x[:n-2],y_prim)
  File "/usr/lib/pymodules/python2.7/matplotlib/pyplot.py", line 2987, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 4137, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 317, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 295, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 237, in _xy_from_xy
    raise ValueError("x and y must have same first dimension")
ValueError: x and y must have same first dimension
>>> x
array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,
        5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ])
>>> y
array([ 0.        ,  0.47942554,  0.84147098,  0.99749499,  0.90929743,
        0.59847214,  0.14112001, -0.35078323, -0.7568025 , -0.97753012,
       -0.95892427, -0.70554033, -0.2794155 ,  0.21511999,  0.6569866 ,
        0.93799998,  0.98935825,  0.79848711,  0.41211849])
>>> y_prim
-0.38174226799988875
>>> detla_y

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    detla_y
NameError: name 'detla_y' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 48, in <module>
    plt.plot(x[:n-1],y_prim,y_prim2)
  File "/usr/lib/pymodules/python2.7/matplotlib/pyplot.py", line 2987, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 4137, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 317, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 279, in _plot_args
    raise ValueError('third arg must be a format string')
ValueError: third arg must be a format string
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/derivative.py", line 48, in <module>
    plt.plot(x[:n-1],y_prim,y_prim2)
  File "/usr/lib/pymodules/python2.7/matplotlib/pyplot.py", line 2987, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 4137, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 317, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 279, in _plot_args
    raise ValueError('third arg must be a format string')
ValueError: third arg must be a format string
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
