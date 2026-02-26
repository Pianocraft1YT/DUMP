def welcome():
    global loop
    Potato_main.onclick(On_potato_click)
    loop = True
    Potato_welcome_writer.clear()
    potato_boost()
    update_potato_display()