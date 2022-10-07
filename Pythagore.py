from cmath import pi
from manimlib import *

class Triangle1(Scene):
    def construct(self):
        
        Opening = Tex("A^2", "+", "B^2", "=", "C^2")
        #self.wait(4)
        self.play(Write(Opening))
        #self.wait(4)
        self.play(FadeOut(Opening, RIGHT))
        #triangle = Polygon([0, 0, 0], [1.25, 0, 0], [0, 1.25, 0])
        triangle = Polygon([0-1, 0-1, 0], [4-1, 0-1, 0], [0-1, 3-1, 0])
        triangle.set_fill(BLUE, opacity= 0.5)
        triangle.scale(0.5)
        #carre1 = Polygon([1.25, 0, 0], [0, 1.25, 0], [1.25, 2.5, 0], [2.5, 1.25, 0])
        #carre1 = Polygon([3-1, -1, 0], [0-1-1, 2, 0], [2, 4.5, 0], [5.5, 1.5, 0])
        #carre1 = Square(5).align_to(triangle)
        #carre1 = Square(5).align_to(triangle, DL)   
        carre1 = Square(5).shift([2, 1.5, 0]) 
        carre1.scale(0.5)
        carre1.rotate(5.6397)
        carre1.shift(LEFT*0.2)
        carre1.set_fill(RED, opacity= 0.5)
        

        carre2 = Square(3).shift((-0.75, 0.5, 0))
        carre2.scale(0.5)
        carre2.set_fill(GREEN, opacity= 0.5)
        carre3 = Square(4).shift([1, -1.25, 0])
        carre3.scale(0.5)
        carre3.set_fill(GREEN, opacity= 0.5)

        self.play(ShowCreation(triangle))
        #self.wait(2)
        self.play(ShowCreation(carre1))
        self.play(ShowCreation(carre2))
        self.play(ShowCreation(carre3))

        

        self.play(FadeOut(triangle))
        
        self.play(carre1.animate.shift(RIGHT*2).shift(DOWN*0.75).rotate(-5.6397))
        self.play(carre3.animate.shift(LEFT*5).shift(UP*1.75), 
                  carre2.animate.shift(DOWN*0.25))
        

        #for x in range(0, 4):
            #block1 = Polygon([0, 0, 0], [0, 0.417*x, 0], [-0.417, 0.417*x, 0], [-0.417, 0, 0])
            #block1.set_fill(GREEN, opacity= 1)
            #block1.
            # self.play(ShowCreation(block1))
            
        boxes=VGroup(*[Square() for s in range(0,9)])
        boxes.arrange_in_grid(n_rows=3, buff=0.05)
        boxes.scale(0.25)
        #boxes.shift(LEFT*0.62)
        #boxes.shift(UP*0.375)
        boxes.align_to(carre2, DL)
        boxes.set_fill(BLACK, opacity= 0.5)
        self.play(ShowCreation(boxes))

        boxes=VGroup(*[Square() for s in range(0,16)])
        boxes.arrange_in_grid(n_rows=4, buff=0.05)
        boxes.scale(0.25)
        #boxes.shift(LEFT*2.37)
        #boxes.shift(UP*0.375)
        boxes.align_to(carre3, DL)
        boxes.set_fill(BLACK, opacity= 0.5)
        self.play(ShowCreation(boxes))
        

        Text1 = Text("16")
        Text2 = Text("9")
        Text3 = Text("25")
        Text1.to_edge(DOWN).shift(LEFT*4).shift(UP*2)
        Text2.to_edge(DOWN).shift(LEFT*0.7).shift(UP*2)
        Text3.to_edge(DOWN).shift(LEFT*2.3).shift(UP*0.8)
        self.play(Write(Text1), Write(Text2))
        self.play(Write(Text3))  


        boxes1=VGroup(*[Square() for s in range(0,16)])
        boxes1.arrange_in_grid(n_rows=4, buff=0.05)
        boxes1.scale(0.25)
        #boxes.shift(LEFT*2.37)
        #boxes.shift(UP*0.375)
        boxes1.align_to(carre3, DL)
        boxes1.set_fill(WHITE, opacity= 0.5)

        boxes2=VGroup(*[Square() for s in range(0,9)])
        boxes2.arrange_in_grid(n_rows=3, buff=0.05)
        boxes2.scale(0.25)
        #boxes.shift(LEFT*0.62)
        #boxes.shift(UP*0.375)
        boxes2.align_to(carre2, DL)
        boxes2.set_fill(WHITE, opacity= 0.5)
        

        boxes3=VGroup(*[Square() for s in range(0,25)])
        boxes3.arrange_in_grid(n_rows=5, buff=0.05)
        boxes3.scale(0.245)
        #boxes.shift(LEFT*0.62)
        #boxes.shift(UP*0.375)
        boxes3.align_to(carre1, DL)
        boxes3.set_fill(WHITE, opacity= 0.5)

        self.play(
            ShowCreation(boxes1, run_time = 5),
            #ShowCreation(boxes2, run_time = 5),
            ShowCreation(boxes3, run_time = 5)
            )   
        

        #self.embed()
        


