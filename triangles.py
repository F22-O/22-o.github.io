import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#create screen
pygame.init()
Screen_width=500
Screen_height=300
screen=pygame.display.set_mode((Screen_width,Screen_height), DOUBLEBUF|OPENGL)
pygame.display.set_caption('YourName')

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4,4,-3,3)

#draw
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #Red triangle
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex2f(0,0)
    glVertex2f(0,0.5)
    glVertex2f(-0.5,0.5)
    glEnd()
    #blue triangle
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    glVertex2f(0, 0)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5,0)
    glEnd()
    #green triangle
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2f(0, 0)
    glVertex2f(0.5,-0.5)
    glVertex2f(0,-0.5)
    glEnd()
    # mix blue , red and green triangle
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    glVertex2f(0, 0)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 1, 0)
    glVertex2f(-0.5, 0)
    glEnd()

run = True
init()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.flip()
pygame.quit()