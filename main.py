from tkinter import *
import random

# Global variables
times = 3
random_country = ""
country_facts_list = []

def check(country):
    global times, random_country, country_facts_list,label_two
    if random_country == country:
        label_two.config(text="You Won")
        label_three.pack_forget()
        restart_button.pack()  # Show restart button
        button_frame.pack_forget()
    else:
        if times > 1:
            update_fact()
            times -= 1
            label_three.config(text=f"number of tries: {str(times)}")
        else:
            label_two.config(text=f"You Lost, the country is \n {random_country}")
            label_three.pack_forget()
            restart_button.pack()  # Show restart button
            button_frame.pack_forget()

def update_fact():
    global random_country, country_facts_list,label_two
    current_index = country_facts_list.index(label_two["text"])
    next_index = (current_index + 1) % len(country_facts_list)
    label_two.config(text=country_facts_list[next_index])

def show_second_page():
    global random_country, country_facts_list, times,rabit_img,play_button,second_page_frame,label,label_tow,label_three,country_facts,restart_button,button_frame
    times = 3
    title.pack_forget()
    rabit_img.pack_forget()
    play_button.pack_forget()
    second_page_frame.pack()
    label.config(font=("Font", 30))
    label_two.config(font=("Font", 25))
    label_three.config(font=("Font", 20))
    random_country = random.choice(list(country_facts.keys()))
    country_facts_list = country_facts[random_country]
    random.shuffle(country_facts_list)
    label_two.config(text=country_facts_list[1])
    label_three.config(text=f"number of tries: {str(times)}")
    restart_button.pack_forget()
    label_two.pack(ipady=40, ipadx=100)
    button_frame.pack()

def restart_game():
    global times, country_facts_list,play_button,rabit_img,title,second_page_frame,label_three,label_two
    times = 3
    label_three.pack(ipady=4, ipadx=1)
    label_two.pack_forget()
    second_page_frame.pack_forget()
    title.pack(ipady=50, ipadx=10)
    rabit_img.pack()
    play_button.pack(pady=50)

def main():
    global title,times, random_country, country_facts_list,rabit_img,play_button ,second_page_frame,label,label_three,label_two,country_facts,restart_button,button_frame
    root = Tk()
    root.title("G Game")
    root.configure(bg="skyblue")
    root.geometry("500x500+300+100")

    cool_button_style = {
        "font": ("Arial", 30),
        "bg": "#4CAF50",
        "fg": "white",
        "borderwidth": 0,
        "highlightthickness": 0,
        "activebackground": "#45a049",
    }

    country_facts = {
        "iceland": ["the land of the ice and snow,the midnight sun and the hot springs flow!", "national dish Hákarl", "There are no trains"],
        "singapore": ["Chewing gum is illegal", "Garena", "Hainanese chicken rice is national dish"],
        "japan": ["national sport is sumo wrestling ", "birthplace of manga", "Home of anime"],
        "tunisia": ["national dish Couscous", "harissa", "Carthage"],
        "italy": ["all roads lead to our capital", "birthplace of lasagna,pasta and pizza", "vespa,ferrari,lambroghini"],
        "south korea": ["kpop&kdramas", "samsung", "national dish Kimish"],
        "canada": ["beaver national animal", "hockey national sport", "poutine national dish"],
        "new zeland": ["dosen't show up in worlds maps", "national sport rugby", "Mince Pie national dish"],
        "sweden": ["pewdiepie", "spotfiy", "ikea"],
        "finland": ["national dish perkele", "nokia", "saunas"]
    }

    random_country = random.choice(list(country_facts.keys()))
    country_facts_list = country_facts[random_country]
    random.shuffle(country_facts_list)

    # First page
    title = Label(root, text="Guessing Game", bg="skyblue", fg="purple")
    title.pack(ipady=50, ipadx=10)
    title.config(font=("Font", 30))

    image_rabit = PhotoImage(file="images/rabit.png")
    sized_rabit = image_rabit.subsample(2, 2)
    rabit_img = Label(root, image=sized_rabit)
    rabit_img.pack()

    play_button = Button(root, text="Play", width=4, height=1, **cool_button_style, command=show_second_page)
    play_button.pack(pady=50)

    # Second page
    second_page_frame = Frame(root, bg="skyblue")

    label = Label(second_page_frame, text="Guess The Country", bg="skyblue", fg="green")
    label.pack(ipady=50, ipadx=10)
    label_three = Label(second_page_frame, text=f"number of tries {times}", bg="skyblue", fg="red")
    label_three.pack(ipady=4, ipadx=1)
    label_two = Label(second_page_frame, text=country_facts_list[1], bg="skyblue", fg="purple", wraplength=500)
    label_two.pack(ipady=40, ipadx=100)

    # Create the second frame inside second_page_frame
    button_frame = Frame(second_page_frame, bg="skyblue")
    button_frame.pack()

    # Configure the layout manager for the button_frame
    button_frame.grid_rowconfigure(0, weight=1)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

    # Create and place the buttons inside the button_frame
    image_singapore = PhotoImage(file="images/sg.png")
    sized_singapore = image_singapore.subsample(2, 2)
    singapore_button = Button(button_frame, image=sized_singapore, command=lambda: check("singapore"))
    singapore_button.grid(row=0, column=0, padx=10, pady=10)

    image_iceland = PhotoImage(file="images/is.png")
    sized_flag_iceland = image_iceland.subsample(2, 2)
    iceland_button = Button(button_frame, image=sized_flag_iceland, command=lambda: check("iceland"))
    iceland_button.grid(row=0, column=1, padx=10, pady=10)

    image_tunisia = PhotoImage(file="images/tn.png")
    sized_tunisia = image_tunisia.subsample(2, 2)
    tunisia_button = Button(button_frame, image=sized_tunisia, command=lambda: check("tunisia"))
    tunisia_button.grid(row=0, column=2, padx=10, pady=10)

    image_japan = PhotoImage(file="images/jp.png")
    sized_japan = image_japan.subsample(2, 2)
    japan_button = Button(button_frame, image=sized_japan, command=lambda: check("japan"))
    japan_button.grid(row=0, column=3, padx=10, pady=10)

    image_canada = PhotoImage(file="images/ca.png")
    sized_canada = image_canada.subsample(2, 2)
    canada_button = Button(button_frame, image=sized_canada, command=lambda: check("canada"))
    canada_button.grid(row=0, column=4, padx=10, pady=10)

    image_korea = PhotoImage(file="images/kr.png")
    sized_korea = image_korea.subsample(2, 2)
    korea_button = Button(button_frame, image=sized_korea, command=lambda: check("south korea"))
    korea_button.grid(row=1, column=0, padx=10, pady=10)

    image_sweden = PhotoImage(file="images/se.png")
    sized_sweden = image_sweden.subsample(2, 2)
    sweden_button = Button(button_frame, image=sized_sweden, command=lambda: check("sweden"))
    sweden_button.grid(row=1, column=1, padx=10, pady=10)

    image_finland = PhotoImage(file="images/fi.png")
    sized_finland = image_finland.subsample(2, 2)
    finland_button = Button(button_frame, image=sized_finland, command=lambda: check("finland"))
    finland_button.grid(row=1, column=2, padx=10, pady=10)

    image_nz = PhotoImage(file="images/nz.png")
    sized_nz = image_nz.subsample(2, 2)
    nz_button = Button(button_frame, image=sized_nz, command=lambda: check("new zeland"))
    nz_button.grid(row=1, column=3, padx=10, pady=10)

    image_italy = PhotoImage(file="images/it.png")
    sized_italy = image_italy.subsample(2, 2)
    italy_button = Button(button_frame, image=sized_italy, command=lambda: check("italy"))
    italy_button.grid(row=1, column=4, padx=10, pady=10)

    restart_button = Button(second_page_frame, text="Restart", **cool_button_style, command=restart_game)

    root.mainloop()

if __name__ == "__main__":
    main()
