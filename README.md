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

## main.py

This file serves as the main entry point for running optimization methods on provided test functions.

- **Usage**: The main function executes various optimization methods on predefined test functions and prints the results.

## test.py

This file contains test functions used to evaluate the performance of optimization methods.

- **Test Functions**: Defines a set of quadratic, cubic, and quartic functions to be used for testing the optimization methods.
- **Method Evaluation**: Iterates through the test functions and optimization methods, recording the optimal solutions, function values, iterations, and execution times.
</details>

<details>
<summary>Ukrainian</summary>

## IntervalOptimizationMethods.py

У цьому файлі містяться класи та методи для методів оптимізації інтервалу.

- **Оптимізація золотого перетину**
  - Метод: `golden_ratio_optimization(func, a, b, tolerance)`
  - Опис: Реалізує метод оптимізації золотого перетину для пошуку мінімуму унімодальної функції в заданому інтервалі.
- **Оптимізація числами Фібоначчі**
  - Метод: `fibonacci_optimization(func, lower_bound, upper_bound, tolerance, n)`
  - Опис: Використовує метод пошуку числами Фібоначчі для поступового скорочення інтервалу пошуку функції.
- **Оптимізація методом бісекції**
  - Метод: `bisection_optimization(func, a, b, delta, epsilon)`
  - Опис: Реалізує метод бісекції для пошуку мінімуму функції шляхом повторного розділення інтервалу.

## PointOptimizationMethods.py

У цьому файлі містяться класи та методи для точкових методів оптимізації.

- **Метод Ньютона**
  - Метод: `newtons_method(f, x_k, precision, max_iterations)`
  - Опис: Реалізує метод Ньютона для знаходження коренів функції для оптимізації заданої функції.
- **Градієнтний спуск**
  - Метод: `gradient_method(fun, uk, max_iterations, tolerance, alpha, beta, max_value)`
  - Опис: Реалізує метод градієнтного спуску для знаходження мінімуму функції.
- **Випадковий пошук**
  - Метод: `random_search(fun_expr, x_k, tolerance, step_size, max_iterations, shrink_step)`
  - Опис: Використовує випадковий пошук для оптимізації функції шляхом випадкового дослідження простору рішень.

## main.py

Цей файл служить основним точкою входу для запуску методів оптимізації на заданих тестових функціях.

- **Використання**: Головна функція виконує різні методи оптимізації на заданих тестових функціях та виводить результати.

## test.py

У цьому файлі містяться тестові функції, які використовуються для оцінки продуктивності методів оптимізації.

- **Тестові функції**: Визначає набір квадратних, кубічних та квартичних функцій для тестування методів оптимізації.
- **Оцінка методів**: Ітерується через тестові функції та методи оптимізації, записуючи оптимальні рішення, значення функцій, ітерації та час виконання.

</details>