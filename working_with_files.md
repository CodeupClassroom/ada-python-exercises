# Working With Files

In this lesson, we'll explore how to read the contents of a file, as well as how
to create / modify files with Python.

We'll be using the `open` function throughout this lesson. The `open` function
gives us access to an object that represents a file on our hard disk.

We will focus on two arguments to the `open` function:

- The first argument is the file path that specifies where the file is that we
  want to manipulate. This can be either a relative or an absolute path.
- The second argument is optional, and specifies the mode in which we wish to
  open the file; we will either read the file's contents or write contents to a
  file.

| mode | description                                                              |
| ---- | -----------                                                              |
| `r`  | Open the file for reading (the default)                                  |
| `w`  | Open the file for writing. Will truncate any existing file contents      |
| `a`  | Open the file for writing. Will append to any existing contents.         |
| `x`  | Open the file for writing. Will give an error if the file already exists |

## Reading Files Contents

In the example below, we will open up a file and read the entire contents of the
file into a string variable.

```python
with open('myfile.txt') as f:
    file_contents = f.read()
```

Often times it is the case that we want to process a file's content line by line
(e.g. when we work with a csv file). We can do so by using the string's `.split`
method with the newline character.

```python
lines = file_contents.split('\n')
```

Here `lines` will be a list, and each element in the list will be a string that
is the contents of one line in the file.

This operation is so common that python provides a way to do it for us:

```python
with open('myfile.txt') as f:
    lines = f.readlines()
```

## Writing contents to a files

```python
file_contents = '''
one
two
three
'''

with open('myfile.txt', 'w') as f:
    f.write(file_contents)
```

## Exercises

1. Read the contents of your last exercise file into a variable.

    1. Print out every line in the file
    1. Print out every line in the file, but add a line numbers

1. Write some python code to create a grocery list.

    1. Create a variable named `grocery_list`. It should be a list, and the
       elements in the list should be a least 3 things that you need to buy from
       the grocery store.
    1. Create a function named `make_grocery_list`. When run, this function
       should write the contents of the `grocery_list` variable to a file named
       `my_grocery_list.txt`.
    1. Create a function named `show_grocery_list`. When run, it should show
       each item on the grocery list.
    1. Create a function named `buy_item`. It should accept the name of an item
       on the grocery list, and remove that item from the list.

