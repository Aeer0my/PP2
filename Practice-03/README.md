# Practice 03 — Python Functions, Lambda, Classes & Inheritance

## Project Structure

```
Practice-03/
├── functions/
│   ├── basic_functions.py       # Function definitions, calls, docstrings
│   ├── function_arguments.py    # Positional, default, keyword arguments
│   ├── return_values.py         # Single/multiple return values, early return
│   └── args_kwargs.py           # *args, **kwargs, unpacking
├── lambda/
│   ├── lambda_basics.py         # Lambda syntax, ternary, IIFE
│   ├── lambda_with_map.py       # Transforming sequences with map()
│   ├── lambda_with_filter.py    # Filtering sequences with filter()
│   └── lambda_with_sorted.py    # Custom sorting with sorted()
├── classes/
│   ├── class_definition.py      # Class creation, objects, properties
│   ├── init_method.py           # __init__ constructor patterns
│   ├── class_methods.py         # Instance, class, and static methods
│   └── class_variables.py       # Class vs instance variables
├── inheritance/
│   ├── inheritance_basics.py    # Parent/child classes, isinstance()
│   ├── super_function.py        # super() in __init__ and methods
│   ├── method_overriding.py     # Overriding methods and __str__
│   └── multiple_inheritance.py  # Mixins, MRO, diamond problem
└── README.md
```

## Topics Covered

### Functions
- Defining and calling functions with `def`
- Positional, default, and keyword arguments
- `*args` for variable positional arguments
- `**kwargs` for variable keyword arguments
- Single and multiple return values
- Early return with guards
- Docstrings for documentation

### Lambda Expressions
- `lambda` syntax: `lambda args: expression`
- Using `map()` to transform every element in a sequence
- Using `filter()` to select elements matching a condition
- Using `sorted()` with a custom `key` function
- Multi-key sorting using tuples

### Classes & Objects
- `class` definition and object instantiation
- `__init__()` constructor for initialization
- Instance methods with `self`
- `@classmethod` and `@staticmethod`
- Class variables vs instance variables
- Mutable class variable pitfall and fix

### Inheritance
- Single inheritance with `class Child(Parent)`
- `super()` to call parent methods
- Method overriding for specialized behaviour
- Overriding `__str__` for readable output
- Multiple inheritance and mixins
- Method Resolution Order (MRO)
- Diamond inheritance solved by `super()`

## How to Run

```bash
# Run any file directly
python functions/basic_functions.py
python lambda/lambda_with_map.py
python classes/class_methods.py
python inheritance/multiple_inheritance.py
```

All files are self-contained and produce output when executed.
