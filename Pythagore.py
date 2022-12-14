from cmath import pi








from manimlib import *
 
class Triangle1(Scene):
    def construct(self):

        self.wait(2)
        Opening = Tex("A^2", "+", "B^2", "=", "C^2")
        self.wait(4)
        self.play(Write(Opening))
        self.wait(9)
        self.play(FadeOut(Opening, RIGHT))
        triangle = Polygon([0-1, 0-1, 0], [4-1, 0-1, 0], [0-1, 3-1, 0])
        triangle.set_fill(BLUE, opacity= 0.5)
        triangle.scale(0.5)
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
        self.play(ShowCreation(carre1))
        self.play(ShowCreation(carre2))
        self.play(ShowCreation(carre3))

        a = Text("A").scale(0.5).set_fill(BLACK, opacity = 1).move_to(carre3.get_center())
        a.shift(UP*0.75)
        b = Text("B").scale(0.5).set_fill(BLACK, opacity = 1).move_to(carre2.get_center())
        b.shift(RIGHT*0.5)
        c = Text("C").scale(0.5).set_fill(BLACK, opacity = 1)
        c.shift(RIGHT).shift(UP*0.85)
        
        self.play(Write(c))
        self.play(Write(a))
        self.play(Write(b))

        self.wait(8)
        self.play(FadeOut(triangle))
        self.play(FadeOut(a),FadeOut(b),FadeOut(c))
       
        self.play(carre1.animate.shift(RIGHT*2).shift(DOWN*0.75).rotate(-5.6397))
        self.play(carre3.animate.shift(LEFT*5).shift(UP*1.75), 
                  carre2.animate.shift(DOWN*0.25))
        

        for y in range(0, 3):
            for x in range(0, 3):
                block1 = Square(1)
                block1.scale(0.5)
                z = (3*y)+(x+1)
                block1.align_to(carre2, DL).shift(RIGHT*(x*0.5)).shift(UP*(y*0.5))
                block1.set_fill(GREEN, opacity= 1)
                text = Text(f'{z}').scale(0.5).move_to(block1.get_center())
                self.play(ShowCreation(block1), Write(text), run_time = 0.5)

        self.play(text.animate.scale(3).shift(DOWN*2).shift(LEFT*0.5))
        self.wait(4)
            
        for y in range(0, 4):
            for x in range(0, 4):
                block1 = Square(1)
                block1.scale(0.5)
                z = (4*y)+(x+1)
                block1.align_to(carre3, DL).shift(RIGHT*(x*0.5)).shift(UP*(y*0.5))
                block1.set_fill(GREEN, opacity= 1)
                text = Text(f'{z}').scale(0.5).move_to(block1.get_center())
                self.play(ShowCreation(block1), Write(text), run_time = 0.5)

        self.play(text.animate.scale(3).shift(DOWN*2.5).shift(LEFT*0.8))
        self.wait(6)
        
        
        for y in range(0, 5):
            for x in range(0, 5):
                block1 = Square(1)
                block1.scale(0.5)
                z = (5*y)+(x+1)
                block1.align_to(carre1, DL).shift(RIGHT*(x*0.5)).shift(UP*(y*0.5))
                block1.set_fill(GREEN, opacity= 1)
                text = Text(f'{z}').scale(0.5).move_to(block1.get_center())
                self.play(ShowCreation(block1), Write(text), run_time = 0.5)

        self.wait(4)
        self.play(text.animate.scale(3).shift(DOWN*3).shift(LEFT))
        Opening = Tex("16", "+", "9", "=", "25").shift(DOWN*2.5)
        Theorem = Tex("4^2", "+", "3^2", "=", "5^2").shift(DOWN*2.5)
        conclu = Tex("A^2", "+", "B^2", "=", "C^2").shift(DOWN*2.5)
        self.wait(4)
        self.play(Write(Opening))
        self.play(FadeOut(Opening, DOWN))
        self.play(FadeIn(Theorem, DOWN))
        self.wait(4)
        self.play(FadeOut(Theorem, DOWN))
        self.wait(3)
        self.play(FadeIn(conclu, DOWN))
        self.wait(3)
        self.play
        #self.embed()
        




