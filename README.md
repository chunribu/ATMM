# ATMM
Animation Time Manager for Manim

## Installation

From [PyPI](https://pypi.org/project/atmm/)

```
pip install atmm
```

## Usage

https://user-images.githubusercontent.com/57521167/187965141-a40d4239-1ad4-406b-945f-ca34f8d8979f.mp4

```python
from manim import *
import atmm

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
```

