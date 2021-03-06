from big_ol_pile_of_manim_imports import *
class Intro(Scene):
    def construct(self):
        trianglea = Polygon(
            np.array([.5,.87,0]),
            np.array([1,0,0]),
            np.array([0,0,0]),
            fill_opacity = 0.75
        )

        linea1=Line([.5,.87,0],[0,0,0])
        linea11=Line([.5,.87,0],[0.25,0.43,0])
        linea12=Line([0,0,0],[0.25,0.43,0])
        lineb1= Line([0.19,1.4,0],[-0.62,0,0])
        lineb1a = Line([0.19, 1.4, 0], [-0.62, 0, 0],stroke_width=6.5)
        lineb2= Line([0.19,1.4,0],[.5,.87,0])
        lineb2a = Line([0.19, 1.4, 0], [.5, .87, 0],stroke_width=6.5)
        lineb3=Line([-0.62,0,0],[0,0,0])
        linec11=Line([0.9,1.57,0],[0.65,1.13,0])
        linec11a = Line([0.9, 1.57, 0], [.5,.87,0],stroke_width=6.5)
        linec12=Line([-0.4,-0.7,0],[-0.15,-0.27,0])
        linec13=Line([0.65,1.13,0],[-0.15,-0.27,0])
        linec2=Line([0.9,1.57,0],[2.21,-0.7,0])
        linec2a = Line([0.9, 1.57, 0], [2.21, -0.7, 0],stroke_width=6.5)
        linec3=Line([-0.4,-0.7,0],[2.21,-0.7,0])
        one=TexMobject("1")
        phi=TexMobject("\\phi")
        phisqr = TexMobject("\\phi^2")
        one.scale(0.5)
        one.move_to(trianglea, RIGHT*0.000001)
        phi.move_to(lineb1,LEFT*0.000001)
        phi.scale(0.5)
        phisqr.next_to(linec3, BOTTOM*0.0001)
        phisqr.scale(0.5)
        figure= VGroup(trianglea,one,linea1,lineb1,phi,lineb2,lineb3,linea11,linec11,linea12,linec12,lineb1,linec13,linec3,linec2,phisqr)
        m=VGroup(lineb1a, lineb2a,linec11a,linec2a)
        m.set_color(YELLOW)
        fm=VGroup(figure,m)
        fm.move_to(LEFT*.008+UP*0.7)
        fm.scale(1.9)
        title = TextMobject("Mathademia")
        title.next_to(fm, BOTTOM * 0.5)
        title.scale(2)
        title.set_color(DARK_BLUE)
        self.play(DrawBorderThenFill(trianglea), Write(one))
        self.play(Transform(linea1,lineb1),Write(phi))
        self.play(ShowCreation(lineb2),ShowCreation(lineb3))
        self.play(Transform(linea11,linec11),Transform(linea12,linec12),Transform(lineb1,linec13),ShowCreation(linec3),ShowCreation(linec2),Write(phisqr),FadeIn(m), Write(title))
        self.play(FadeOutAndShift(figure),FadeOutAndShift(m), FadeOutAndShift(title))
class exercise(Scene):
    def construct(self):
        exercise_title=TextMobject("Exercise")
        exercise_title.set_color(DARK_BLUE)
        exercise_title.move_to(TOP*.8)
        problem_1=TexMobject("1) \\ \\textrm{Find all} \\ n \\ \\textrm{that satisfies the relation} \\ 7n+1|8n+55")
        problem_2=TexMobject("2) \\ \\textrm{Find the maximum value of} \\ n \\ \\textrm{such that} \\ n+25|(n+2)^2")
        problem_3=TexMobject("3) \\ \\textrm{Show that} \\ 2^{32}+1 \\ \\textrm{is divisible by} \\ 641")
        problem_4=TexMobject("4) \\ \\textrm{Prove that} \\ n^4+4^n \\ \\textrm{is always composite for} \\ n \\in \\mathbb{N} \\\ - \\textrm{IMO - 1964, P1}")
        problem_5=TexMobject("5) \\ \\textrm{If} \\ \\frac{a+1}{b}+\\frac{b+1}{a} \\ \\textrm{is a positive integer, then} \\ a+b \\geq (gcd(a,b))^2 \\\ - \\textrm{Spanish Mathematical Olympiad-1996}")
        problems=VGroup(problem_1, problem_2, problem_3, problem_4, problem_5)
        problems.scale(0.7)
        problems.to_edge(LEFT+TOP*0.7)
        problems.arrange(BOTTOM, buff=SMALL_BUFF, aligned_edge=LEFT)
        problem_3_top=problem_3.copy()
        problem_3_top.to_edge(LEFT + TOP * 0.7)
        s21=TexMobject("641|2^{32}+1")
        s22=TexMobject("641|","641","=640+1")
        s23=TexMobject("641|(5 \\times 2^7)^4-1")
        s24=TexMobject("\\Longrightarrow","641|","5^4","\\times", "2^{28}", "-1")
        s25=TexMobject("641|","5^4","+2^4")
        s2=VGroup(s21, s22,s23,s24,s25)
        s2.scale(0.7)
        s2.arrange(BOTTOM, buff=SMALL_BUFF, aligned_edge=LEFT)
        s2.move_to([-4, -0.5, 0])

        s21c=TexMobject("641|2^{32}+1")
        s22c=TexMobject("641|","5\\times 2^7+1 \\\*")
        s23c=TexMobject("641|(5 \\times 2^7)^4-1")
        s24c=TexMobject("\\Longrightarrow 641|","5^4","\\times", "2^{28}", "-1")
        s25c=TexMobject("641|","5^4","+2^4")
        s2c=VGroup(s21c, s22c,s23c,s24c,s25c)
        s2c.scale(0.7)
        s2c.arrange(BOTTOM, buff=SMALL_BUFF, aligned_edge=LEFT)
        s2c.move_to([-4, -0.5, 0])
        arrow21= Arrow(s22[1].get_right(),s21.get_right(), path_arc= 181*DEGREES, stroke_width=6)
        arrow21.set_color(YELLOW)
        s22r1=TexMobject("32=7\\times 4+4")
        s22r1.scale(0.7)
        s22r1.move_to([4, -0.5, 0])
        s23r21=TexMobject("a^4-1=(a^2+1)(a+1)(a-1)")
        s23r22=TexMobject("\\Longrightarrow a+1|a^4-1")
        s23r2=VGroup(s23r21,s23r22)
        s23r2.scale(0.7)
        s23r2.arrange(BOTTOM, buff=SMALL_BUFF, aligned_edge=LEFT)
        s23r2.move_to([4, -0.5, 0])
        s25r1=TexMobject("641|641")
        s25r2=TexMobject("641=5^4+2^4")
        s25r=VGroup(s25r1, s25r2)
        s25r.scale(0.7)
        s25r.arrange(BOTTOM, buff=SMALL_BUFF, aligned_edge=LEFT)
        s25r.move_to([4, -0.5, 0])
        s2f21=s24[1:].copy()
        s2f21.scale(1.428)
        s2f22=s25.copy()
        s2f22.scale(1.428)
        s2f23=TexMobject("\\Longrightarrow 641|5^4\\times 2^{28}+2^{32}")
        s2f24=TexMobject("\\Longrightarrow 641|5^4\\times 2^{28}+2^{32}-5^4 \\times 2^{28}+1")
        s2f25=TexMobject("\\Longrightarrow 641|2^{32}+1")
        s2f2=VGroup(s2f21,s2f22,s2f23,s2f24,s2f25)
        s2f2.scale(0.7)
        s2f2.arrange(BOTTOM, buff=SMALL_BUFF, aligned_edge=LEFT)
        s2f2.move_to([0, -0.5, 0])
        self.play(Write(exercise_title))
        self.wait()
        self.play(LaggedStartMap(
            FadeInFrom, problems, run_time=3,
        ))
        self.wait()
        self.play(FadeOut(problems), Transform(problem_3, problem_3_top), replace_mobject_with_target_in_scene=True)
        self.wait()
        self.play(Write(s21))
        self.wait()
        self.play(Write(s22[:2]))
        self.wait()
        self.play(ShowCreationThenDestruction(arrow21))
        self.wait()
        self.play(Write(s22[2]))
        self.wait()
        self.play(Transform(s22[1:], s22c[1]),replace_mobject_with_target_in_scene=True)
        self.wait()
        self.play(Write(s22r1))
        self.play(FadeOut(s22r1))
        self.wait()
        self.play(Write(s23r21))
        self.wait()
        self.play(Write(s23r22))
        self.wait()
        self.play(FadeOut(s23r2), Write(s23))
        self.wait()
        self.play(Write(s24))
        self.wait()
        self.play(Indicate(s24[2]))
        self.wait()
        self.play(Write(s25r1))
        self.wait()
        self.play(Write(s25r2))
        self.wait()
        self.play(Write(s25))
        self.wait()
        self.play(FadeOut(s2), FadeOut(s25r),FadeOut(s2c),Transform(s24[1:].copy(), s2f21),Transform(s25, s2f22),
                  replace_mobject_with_target_in_scene=True)
        self.wait()
        self.play(Write(s2f23))
        self.wait()
        self.play(Write(s2f24))
        self.wait()
        self.play(Write(s2f25))
        self.wait()