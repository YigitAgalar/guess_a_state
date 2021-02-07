import turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_answers = []

writer = turtle.Turtle()
writer.hideturtle()
states = data["state"].to_list()
states_to_learn = []


while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f" {len(correct_answers)}/50 is correct",
                                    prompt="What's another states name ?").title()
    if answer_state in correct_answers:
        pass

    elif answer_state in states:
        answer = data[data["state"] == answer_state]
        correct_answers.append(answer_state)
        writer.penup()
        writer.goto(int(answer.x), int(answer.y))
        writer.write(answer_state)
    elif answer_state == "Exit":
        break

states_to_learn=[state for state in states if not state in correct_answers]

state_datas = pandas.DataFrame(states_to_learn)
state_datas.to_csv("states_to_learn.csv")

