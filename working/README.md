# List of exercises
Here I explain the exercise I did for the exam.

1. Exercises Q7 (Tic Tac Toe, file "L01_TicTacToe.py") and Q8 (Shopping Cart, file "L01_ShoppingCart.ipynb").
2. Exercise Q6, "Conway's game of Life", file "L02_GameOfLife.ipynb".
3. Exercises Q7 (Mandelbrot Set) and Q8 (Game of Life visualization), file "L03_matplotlib.ipynb".
4. Exercises Q5 (Planetary orbit) and Q6 (Condition number), file "L04_scipy.ipynb".
5. All the exercises, file "L05_mathematica.nb".
6. Exercises Q2 (Egocentric, see action "check_name.yml"), and Q5 (Latexdiff, folder "L06_git").
7. Exercises Q1 (Stock market) and Q3 (Scaling), file "L07_numba_multiprocessing.ipynb".
8. Exercise Q1 (I love pip, folder "DiegosTicTacToe") and Q2 (My own test, folder "L08_pytest" and action "testing.yml")

For the exercise of Lecture 6 on the github actions, I could not prevent the local commit, so I proceeded as follows. I set a branch protection rule to prevent everyone (i.e. me) from directly pushing to the main branch. Then I wrote an action that on push to a development branch automatically opens a pull request, verify if the check on the name in the readme file is successful, and in that case automerge to main branch and close the pull request. The same mechanism is applied to the tests of lecture 8.