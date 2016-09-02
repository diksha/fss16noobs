# Exercise 3.1, 3.2

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

# Exercise 3.3

def right_justify(s):
    assert len(s) <= 70, "More than 70 chars in string" 
    print ' ' * (70 - len(s)) + s

right_justify('allen')

# Exercise 3.4

def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    print s
    print s

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

do_twice(print_twice, 'spam')

do_four(print_twice, 'spam')

# Exercise 3.5, Part 1

def do_Ntimes(f, n = 1):
    for i in xrange(n):
        f()

def draw_border():
    print '+', " ".join("-"*4), '+', " ".join("-"*4), '+'

def draw_row():
    print '|', " "*7, '|', " "*7, '|'

def draw_grid():
    do_Ntimes(draw_border, 1)
    do_Ntimes(draw_row, 4)
    do_Ntimes(draw_border, 1)
    do_Ntimes(draw_row, 4)
    do_Ntimes(draw_border, 1)
    
draw_grid()

# Exercise 3.5, Part 2

def do_Ntimes_large(f, n = 1):
    for i in xrange(n):
        f()

def draw_border_large():
    print " ".join("-"*4).join([' + ']*4)

def draw_row_large():
    print ' |', " "*7, '|', " "*7, '|', " "*7, '|'

def draw_grid_large():
    for i in xrange(9): 
        if i%2 == 0:
            do_Ntimes_large(draw_border_large, 1)
        else:
            do_Ntimes_large(draw_row_large, 4)
    
draw_grid_large()
