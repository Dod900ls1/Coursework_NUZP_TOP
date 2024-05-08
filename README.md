<details>
<summary>English</summary>

## IntervalOptimizationMethods.py

This file contains classes and methods for interval optimization techniques.

- **Golden Ratio Optimization**
  - Method: `golden_ratio_optimization(func, a, b, tolerance)`
  - Description: Implements the golden ratio optimization method to find the minimum of a unimodal function within a given interval.
- **Fibonacci Optimization**
  - Method: `fibonacci_optimization(func, lower_bound, upper_bound, tolerance, n)`
  - Description: Utilizes the Fibonacci search method to iteratively narrow down the search interval for function optimization.
- **Bisection Optimization**
  - Method: `bisection_optimization(func, a, b, delta, epsilon)`
  - Description: Implements the bisection method to find the minimum of a function by repeatedly bisecting the interval.

## PointOptimizationMethods.py

This file contains classes and methods for point-based optimization techniques.

- **Newton's Method**
  - Method: `newtons_method(f, x_k, precision, max_iterations)`
  - Description: Implements Newton's method for finding the roots of a function to optimize a given function.
- **Gradient Descent**
  - Method: `gradient_method(fun, uk, max_iterations, tolerance, alpha, beta, max_value)`
  - Description: Implements gradient descent optimization method for finding the minimum of a function.
- **Random Search**
  - Method: `random_search(fun_expr, x_k, tolerance, step_size, max_iterations, shrink_step)`
  - Description: Utilizes random search technique to optimize a function by randomly exploring the solution space.

## Graph_plotting.py
This file includes functions for reading and processing data from a CSV file, computing average times, and plotting bar charts, histograms, and boxplots.

## multi_optimization.py
This script performs optimization using both point and interval methods, saving the results to a CSV file. It also aggregates and saves the results in another CSV file.


## Data_analysis.py
This file contains functions for loading and preprocessing data, performing statistical tests, bootstrapping, and plotting histograms and boxplots.


### test.py
This script tests the optimization methods defined in the `PointOptimizationMethods` class.

</details>

<details>
<summary>Ukrainian</summary>

## IntervalOptimizationMethods.py

Цей файл містить класи та методи для методів оптимізації інтервалу.

- **Оптимізація золотим відношенням**
  - Метод: `golden_ratio_optimization(func, a, b, tolerance)`
  - Опис: Реалізує метод оптимізації золотим відношенням для знаходження мінімуму унімодальної функції в заданому інтервалі.
- **Оптимізація числами Фібоначчі**
  - Метод: `fibonacci_optimization(func, lower_bound, upper_bound, tolerance, n)`
  - Опис: Використовує метод пошуку числами Фібоначчі для поступового скорочення інтервалу пошуку функції.
- **Оптимізація методом бісекції**
  - Метод: `bisection_optimization(func, a, b, delta, epsilon)`
  - Опис: Реалізує метод бісекції для пошуку мінімуму функції шляхом повторного розділення інтервалу.

## PointOptimizationMethods.py

Цей файл містить класи та методи для точкових методів оптимізації.

- **Метод Ньютона**
  - Метод: `newtons_method(f, x_k, precision, max_iterations)`
  - Опис: Реалізує метод Ньютона для знаходження коренів функції для оптимізації заданої функції.
- **Градієнтний спуск**
  - Метод: `gradient_method(fun, uk, max_iterations, tolerance, alpha, beta, max_value)`
  - Опис: Реалізує метод градієнтного спуску для знаходження мінімуму функції.
- **Випадковий пошук**
  - Метод: `random_search(fun_expr, x_k, tolerance, step_size, max_iterations, shrink_step)`
  - Опис: Використовує випадковий пошук для оптимізації функції шляхом випадкового дослідження простору рішень.

## Graph_plotting.py
Цей файл включає функції для читання та обробки даних з файлу CSV, обчислення середніх часів та побудови стовпчикових діаграм, гістограм та бокс-плотів.

## multi_optimization.py
Цей скрипт виконує оптимізацію за допомогою як точкових, так і інтервальних методів, зберігаючи результати у файлі CSV. Також результати агрегуються та зберігаються у іншому файлі CSV.


## Data_analysis.py
Цей файл містить функції для завантаження та передобробки даних, виконання статистичних тестів, бутстрепу та побудови гістограм та бокс-плотів.


### test.py
У цьому скрипті проводяться тести методів оптимізації, визначених у класі `PointOptimizationMethods`.

</details>