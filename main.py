import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.screensize(725, 419)
screen.addshape(image)

turtle.shape(image)
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

data = pd.read_csv("50_states.csv")
state_list = data["state"].tolist()

guessed_states = []
current_score = 0
game_ongoing = True
question_title = "Guess the State"

while game_ongoing:
    answer_state = (screen.textinput(title=question_title, prompt="What is another state name?")).title()
    if answer_state == "Exit":
        break

    if state_list.count(answer_state) > 0:
        answer = (data[data.state == answer_state])
        answer_x_cor = int(answer.x)
        answer_y_cor = int(answer.y)
        answer_coordinates = (answer_x_cor, answer_y_cor)
        turtle.goto(answer_coordinates)
        turtle.write(arg=answer_state, move=False, align="Center", font=("arial", 8, "normal"))
        current_score += 1
        question_title = f"{current_score}/50 States Correct"
        guessed_states.append(answer_state)

for guess in guessed_states:
    state_list.remove(guess)

remaining_states = {
    "Remaining States": [],
    "X Coordinates": [],
    "Y Coordinates": []
}
remaining_states_list = []
remaining_states_x_list = []
remaining_states_y_list = []
for state in state_list:
    remaining_states_list.append(state)
    remaining_states["Remaining States"] = remaining_states_list
    state_data = data[data.state == state]
    remaining_states_x_list.append(int(state_data.x))
    remaining_states_y_list.append(int(state_data.y))
    remaining_states["X Coordinates"] = remaining_states_x_list
    remaining_states["Y Coordinates"] = remaining_states_y_list


print(remaining_states)
forgotten_data = pd.DataFrame(remaining_states)
forgotten_data.to_csv("forgotten_states.csv")

screen.exitonclick()
