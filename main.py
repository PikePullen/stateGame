import turtle
import pandas

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50",
                                    prompt="What's another states name?").title()
    # print(f"answer_state: {answer_state}")

    if answer_state == "Exit":
        missing_states = []
        for state in set(data['state']):
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in set(data['state']):
        guessed_states.append(answer_state)

        selected_state_name = data.loc[data.state==answer_state,'state'].values[0]
        # print(f"selected_state_name: {selected_state_name}")

        selected_state_xpos = data.loc[data.state==answer_state,'x'].values[0]
        # print(f"selected_state_xpos: {selected_state_xpos}")

        selected_state_ypos = data.loc[data.state==answer_state,'y'].values[0]
        # print(f"selected_state_ypos: {selected_state_ypos}")

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(selected_state_xpos), int(selected_state_ypos))
        t.write(f"{selected_state_name} ({selected_state_xpos},{selected_state_ypos})")

# states to learn, names not in the guessed array