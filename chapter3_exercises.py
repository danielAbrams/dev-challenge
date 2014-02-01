# Exercises for chapter 3:

# Name: Daniel Abrams

#Exercise 3.1

#repeat_lyrics()

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

#Error: NameError: name 'repeat_lyrics' is not defined
print ' '
print 'Exercise 3.2' 
print ' '

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

repeat_lyrics()

#error message:
#Traceback (most recent call last):
#  File "chapter3_exercises.py", line 7, in <module>
#    repeat_lyrics()
#NameError: name 'repeat_lyrics' is not defined

#it works as before, because no functions are called until repeat_lyrics()

print ' '
print 'Exercise 3.3'
print ' '
def right_justify(s):
	length = len(s)
	numSpaces = (70 - length)
	print (' '*numSpaces)+s

right_justify('Tom')
right_justify('Steve')

print ' '
print 'Exercise 3.4'
print ' '

def do_twice(f, i):
	f(i)
	f(i)

def print_twice(string):
	print string

do_twice(print_twice, 'spam')

def do_four(f, i):
	do_twice(f,i)
	do_twice(f,i)


do_four(print_twice, 'four')