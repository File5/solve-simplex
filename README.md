# solve-simplex
Simple python script, which can solve linear programming tasks with simplex method. Step by step solution printing

## Simplex method (BigM method)

This script implements a very basic part of the BigM method, hence, only `<= (positive constant)` inequalities because
there is no support for artificial variables.

Although, this version can be easily extended if necessary - current implementation which refers to the solution
is around 120 lines.

It can solve problems like the following:
```
MAX Z = 3x1 + 3x2 + 4x3
subject to
x1 + 2x2 + x3 <= 420
2x1 + x2 + 3x3 <= 600
4x1 + 2x2 + x3 <= 900
and x1,x2,x3 >= 0
```
The output is
```
   +-------+--------+----+----+----+----+----+----+-------+
   | Basis | Values | x1 | x2 | x3 | x4 | x5 | x6 | THETA |
   +-------+--------+----+----+----+----+----+----+-------+
   |    x4 |    420 |  1 |  2 |  1 |  1 |  0 |  0 |   420 |
-->|    x5 |    600 |  2 |  1 |  3 |  0 |  1 |  0 |   200 |
   |    x6 |    900 |  4 |  2 |  1 |  0 |  0 |  1 |   900 |
   |  f(x) |      0 | -3 | -3 | -4 |  0 |  0 |  0 |       |
   +-------+--------+----+----+----+----+----+----+-------+
                                 ^
                                 |
                                 |

[0, 0, 0, 420, 600, 900]
0
(1, 3)
   +-------+--------+------+------+----+----+------+----+-------+
   | Basis | Values |   x1 |   x2 | x3 | x4 |   x5 | x6 | THETA |
   +-------+--------+------+------+----+----+------+----+-------+
-->|    x4 |    220 |  1/3 |  5/3 |  0 |  1 | -1/3 |  0 |   132 |
   |    x3 |    200 |  2/3 |  1/3 |  1 |  0 |  1/3 |  0 |   600 |
   |    x6 |    700 | 10/3 |  5/3 |  0 |  0 | -1/3 |  1 |   420 |
   |  f(x) |    800 | -1/3 | -5/3 |  0 |  0 |  4/3 |  0 |       |
   +-------+--------+------+------+----+----+------+----+-------+
                               ^
                               |
                               |

[0, 0, 200, 220, 0, 700]
800
(0, 2)
+-------+--------+-----+----+----+------+------+----+-------+
| Basis | Values |  x1 | x2 | x3 |   x4 |   x5 | x6 | THETA |
+-------+--------+-----+----+----+------+------+----+-------+
|    x2 |    132 | 1/5 |  1 |  0 |  3/5 | -1/5 |  0 |       |
|    x3 |    156 | 3/5 |  0 |  1 | -1/5 |  2/5 |  0 |       |
|    x6 |    480 |   3 |  0 |  0 |   -1 |    0 |  1 |       |
|  f(x) |   1020 |   0 |  0 |  0 |    1 |    1 |  0 |       |
+-------+--------+-----+----+----+------+------+----+-------+

[0, 132, 156, 0, 0, 480]
1020
None
```

You can check this [example](https://cbom.atozmath.com/CBOM/Simplex.aspx?q=sm&q1=3%603%60MAX%60Z%60x1%2cx2%2cx3%603%2c3%2c4%601%2c2%2c1%3b2%2c1%2c3%3b4%2c2%2c1%60%3c%3d%2c%3c%3d%2c%3c%3d%60420%2c600%2c900%60%60F%60false%60true%60false%60true%60false%60false%60true&do=1) for clarifications.
