from manim import *
import atmm

print(atmm.func_list)

class Demo(Scene):
    def construct(self):
        background = FullScreenRectangle()\
            .set_opacity(1)\
            .set_color([RED,WHITE,BLUE])

        circle = Circle()\
            .shift(LEFT)

        square = Square()\
            .set_fill(GRAY, opacity=1)\
            .next_to(circle, RIGHT)

        self.play(
            background.animate(run_time=5).set_color([GRAY,GREEN,TEAL]),

            circle.animate(run_time=5, rate_func=atmm.time_manager(
                start=1, stop=2, total_time=5, func='linear'
                )).set_fill(TEAL, opacity=1),

            Write(square, run_time=5, 
                rate_func=atmm.time_manager(
                    start=4, stop=5, total_time=5
                )
            )
        )
        self.wait()