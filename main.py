import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. Naming Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


#state = screen.textinput( title="Guess a State", prompt= " Type a State")

data_state = pandas.read_csv('50_states.csv')

def game_state():
    game_on = True
    while game_on:
        choice = turtle.textinput(title="State Game", prompt="Type a State")
        tr = data_state[(data_state['state'].apply(str.lower)) == choice]
        print(type(tr['x']))
        try:
            x = tr['x'].values[0]
            y = tr['y'].values[0]
        except IndexError:
            gg = turtle.textinput(title="Wrong Choice", prompt="Try Again? y or n ").lower()
            if gg == 'y':
                game_state()
            else:
                break
        ram = turtle.Turtle(shape='square')
        ram.penup()
        ram.hideturtle()
        ram.goto(x, y)
        ram.write(f"{choice}")


game_state()




