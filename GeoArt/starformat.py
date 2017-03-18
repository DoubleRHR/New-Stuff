'''A basic template for cool star shapes with Turtle'''
import turtle

wn = turtle.Screen()
sam = turtle.Turtle()
sam.color('black')

for i in range(n):
#range number(n) is the number of sides of the star
#turn degree(d) is the interior angle measure; basic format is 180-360/x
    sam.forward(200)
    sam.right(d)

turtle.done()
'''Some fun combinations I've found:n=14,d=(180-360/7);
n=18,d=(180-360/9);n=9,d=(180-360/18)'''
