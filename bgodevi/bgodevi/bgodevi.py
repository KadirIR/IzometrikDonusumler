import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
 
kosenokta=[[0,0,0],
           [1,0,0],
           [1,1,0],
           [0,1,0],
           [0,0,1],
           [1,0,1],
           [1,1,1],
           [0,1,1],
           [1,1,0.5],
           [1,0.5,1],
           [0.5,1,1]
           ]
 
kupkenar=[
    (6,8),(6,9),(6,10),
    (8,9),(9,10),(10,8),
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7),
    (8,2),(9,5),(10,7)
]
 
ref_eksen=[
    [0,0,0],[2,0,0],
    [0,0,0],[0,2,0],
    [0,0,0],[0,0,2]
]
def matris_carpim(m,v):
    return [
        m[0][0]*v[0]+m[0][1]*v[1]+m[0][2]*v[2]+m[0][3]*v[3],
        m[1][0]*v[0]+m[1][1]*v[1]+m[1][2]*v[2]+m[1][3]*v[3],
        m[2][0]*v[0]+m[2][1]*v[1]+m[2][2]*v[2]+m[2][3]*v[3],
        m[3][0]*v[0]+m[3][1]*v[1]+m[3][2]*v[2]+m[3][3]*v[3]
    ]
 
def noktadonustur(nokta,donusum):
    donusmusnokta=[]
    for nokta in nokta:
        kordinatvektor=[nokta[0],nokta[1],nokta[2],1]
        sonuc=matris_carpim(donusum,kordinatvektor)
        donusmusnokta.append(sonuc[:3])
    return donusmusnokta
 
def kupciz(noktalar,renk):
    glColor3f(*renk)
    glBegin(GL_LINES)
    for baglanti in kupkenar:
        if 6 in baglanti:
            continue
        glVertex3f(*noktalar[baglanti[0]])
        glVertex3f(*noktalar[baglanti[1]])
    glEnd()
 
def eksenciz(eksen):
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(*eksen[0])
    glVertex3f(*eksen[1])
    glColor3f(0,1,0)
    glVertex3f(*eksen[2])
    glVertex3f(*eksen[3])
    glColor3f(0,0,1)
    glVertex3f(*eksen[4])
    glVertex3f(*eksen[5])
    glEnd()
 
def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(40,(display[0]/display[1]),0.1,50.0)
    glTranslatef(0,-2,-10)
    glRotatef(65,0,0,1)
    glRotatef(-20,0,1,0)
 
    izodonusum=[
        [0.707,0.707,0,0],
        [-0.408,0.408,0.816,0],
        [0.577,-0.577,0.577,0],
        [0,0,0,1]
    ]
    gercekkup=kosenokta
    zkaydir=[
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,2],
        [0,0,0,1]
    ]
    zkaydirilmis=noktadonustur(gercekkup,zkaydir)
    olcekle=[
        [0.5,0,0,0],
        [0,0.5,0,0],
        [0,0,0.5,0],
        [0,0,0,1]
    ]
    xykaydirma=[
        [1,0,0,2],
        [0,1,0,2.5],
        [0,0,1,0],
        [0,0,0,1]
    ]
 
    olceklendirilmis_kup=noktadonustur(gercekkup,olcekle)
    son_kup=noktadonustur(olceklendirilmis_kup,xykaydirma)
    izometrik_ekseni=noktadonustur(ref_eksen,izodonusum)
 
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
 
        izokup1=noktadonustur(gercekkup,izodonusum)
        izokup2=noktadonustur(zkaydirilmis,izodonusum)
        izokup3=noktadonustur(son_kup,izodonusum)
        kupciz(izokup1,(0.9,0.5,0.7))
        kupciz(izokup2,(0.8,0.4,0.1))
        kupciz(izokup3,(0.2,0.3,0.9))
        eksenciz(izometrik_ekseni)
 
        pygame.display.flip()
        pygame.time.wait(10)
 
main()
