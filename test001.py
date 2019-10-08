list_1 = ['php', 'java', 'php', 'java', 'php', 'java', 'php', 'java', 'py', 'php', 'java', 'py']

lengh = len(list_1)

php = list_1.count('php')
java = list_1.count('java')
py = list_1.count('py')

percent_php = 360 / lengh * php
percent_java = 360 / lengh * java
percent_py = 360 / lengh * py
# print(percent_php)

from turtle import Turtle, Screen
from itertools import cycle

letter_frequencies = [('php', percent_php), ('java', percent_java), ('py', percent_py)]

COLORS = cycle(['yellow', 'green', 'red'])

RADIUS = 177
LABEL_RADIUS = RADIUS * 1.33
FONTSIZE = 18
FONT = ("Ariel", FONTSIZE, "bold")

# The pie slices

total = sum(fraction for _, fraction in letter_frequencies)  # data doesn't sum to 100 so adjust

baker = Turtle()  # because we're baking a pie
baker.penup()
baker.sety(-RADIUS)
baker.pendown()

for _, fraction in letter_frequencies:
    baker.fillcolor(next(COLORS))
    baker.begin_fill()
    baker.circle(RADIUS, fraction * 360 / total)
    position = baker.position()
    baker.goto(0, 0)
    baker.end_fill()
    baker.setposition(position)

# The labels

baker.penup()
baker.sety(-LABEL_RADIUS)

for label, fraction in letter_frequencies:
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    baker.write(label, align="center", font=FONT)
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)

baker.hideturtle()

screen = Screen()
# screen.exitonclick()


# import plotly.graph_objects as go
#
# labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
# values = [4500, 2500, 1053, 500]
#
# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
# fig.show()