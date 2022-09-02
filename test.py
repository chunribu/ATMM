from manim import *
import atmm

print(atmm.func_list)

T = atmm.time_manager

class Demo(Scene):
    def construct(self):
        background = FullScreenRectangle()\
            .set_opacity(1)\
            .set_color([RED,WHITE,BLUE])
        
        line = Line(LEFT*7, RIGHT*7)\
            .set_color(BLACK)\
            .shift(DOWN)

        circle = Circle()\
            .shift(LEFT)

        square = Square()\
            .set_fill(GRAY, opacity=1)\
            .next_to(circle, RIGHT)

        self.play(
            background.animate(run_time=6, rate_func=rate_functions.linear)\
                .set_color([WHITE,TEAL,MAROON]),

            GrowFromEdge(line, LEFT, **T(total_time=6, func='linear')),

            circle.animate(**T(start=1, stop=2, total_time=6))\
                .set_fill(TEAL, opacity=1),

            Write(square, **T(start=3, stop=4, total_time=6))
        )
        self.wait()