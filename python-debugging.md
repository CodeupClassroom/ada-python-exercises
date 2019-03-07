# Why the &*#$ won't my code work?

At some point in time I'm sure every programmer has said
(/thought/mumbled/screamed) this. I know I have on way too many occasions. It's
important to know that everyone has this problem, and at times, this can be
**_extremely_** frustrating.

I'd like to share with you my own personal debugging process. I'll be using
Python as an example here, but these ideas I'm sure can apply to coding in
general.

*Note: This all totally works for me, individual results may vary, use at your
own risk, none of these statements are verfied by the FDA or any other relevant
government agency.*

Before I start (usually metaphorically, sometimes literally) banging my head on
the wall, this is what I ask myself:

## Is everything spelled correctly, is my syntax correct?

This is quite commonly the cause of many of my errors. Spelling errors can be
some of the hardest to debug; eyes get used to looking at the same code and
mispellings aren't as obvious to the person who wrote the code as they are to an
outside observer.

Syntax errors can be another frustrating problem to track down. I can't count
the number of times this scenario has happened to me.

1. Write some code that looks amazing.
1. Run the code and see a big long error message that might as well be in
   ancient aramaic for all it's usefulness.
1. Notice that the error gave me a line number in my `.py` file, check out that
   line and find nothing helpful

What I've learned from doing this over and over is a few things:

- all of my code looks amazing when I write it; I have to run it to find all the
  errors with it.

    Expanding on this: I believe its very important save and run your code very
    frequently. I'll change one, maybe two lines and run it again to see if it
    works, as opposed to writing/changing 40 lines and then being overwhelmed by
    at least 100 different error messages and not knowing where to even start.

- google your error messages. You're probably not the first person to encounter
  that error, and the results found on stackoverflow usually contain
  explanations that are much more helpful than the initial error message.

- use the line number of the error as a starting place. Check your code for
  errors a few lines above the given line number.

## Is my code even running?

I've spent countless hours tweaking functions, changing indices of for loops,
and rewriting if conditionals only to realize the code I've been working on
wasn't working because it never ran. To solve this I use a ton of `print`s. For
example:

```python
def my_function(param1, param2, param3):
    print('myFunction called!')
    if some_crazy_condition:
        print('some crazy condition is true!')
        # ...
    else:
        print('some crazy condition is false!')
        # ...

    for item in param3:
        print('Inside the for loop')
        print('item = {}'.format(item))
        if another_condition:
            print('Another condition was true!')

    print('end of my_function')

# ... other code
```

Initially I look to even see that the function I'm working on is properly
running. If I'm unsure about an if statement I'll throw a print in there to see
if my conditions are true. Working inside a loop sometimes it's helpful to print
in every iteration through. Maybe when I wrote the code I expected `i` to go
over 9000, but my print statements tell me it only goes to 4.

## Do my variables contain what I think they contain?

If you've spent any amount of time with Python you'll be well acquainted with
`TypeError`. This tends to creep up quite a bit, but it can be challenging to
see when it occurs. If my `print`s tell me what I think they should tell me, my
next thought is my variables. Again here I like to use a lot of `print`
statements. For example:

```python
def my_function(param1, param2, param3){
    print('my_function called!')
    print('param1 = {}'.format(param1))
    print('param2 = {}'.format(param2))
    print('param3 = {}'.format(param3))
```

Checking on variables periodically allows one to make sure a variable contains
what you think it contains. I've had countless silent errors caused from
thinking something was an list it was an list element and vice versa.
`print`ing variables helps us understand what is going on inside our code.

## Is my code doing what I think it's doing?

This is probably the most tricky question to answer. You could have perfect
syntax, spell everything correctly, have written perfect if conditions and for
loops, but your code *still* might not do what you want it to do. The solution
for this problem is a little more challenging. I like to sit and just think
about what I want my code to do. In plain english, explain what your code is
doing, and what you would like it to do. If this doesn't work, the next part
of this step is to talk through your code with someone else. Sometimes just
the process of explaining your code to someone else gives you the insight
you need to solve your problem.

---

If I go through this whole process and I still haven't figured out what's wrong,
I'll move to the final step of my debugging process

## walking away

Seriously, just get up and move around. Walk around the block, go get some
coffee, get your mind off of the code you're stuck on. The human brain is a very
strange thing; too many solutions have come to me when I was doing something
totally unrelated to coding. It also helps to not think about the code for a
little while and look at it again with fresh eyes.

## other general thoughts

- work on one thing at a time and verify it works before moving on to the next,
  don't try to solve everything at once.
  - eg one function or one if statement
- it's the best feeling in the world when you get a feature up and running, test
  it every which way, and finally remove the 16 different print statements in
  your code you were using to debug it
- print all the things!

Happy Coding!
