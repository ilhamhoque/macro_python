import webbrowser
import keyboard
import time
import os


def safari():
    os.system("open /Applications/Safari.app https://github.com/ilhamhoque")


def firefox():
    controller = webbrowser.get('Firefox')
    controller.open('http://www.google.com')


def close_fx():
    cmd = """osascript -e 'quit app "Firefox"'"""

    def fx():
        os.system(cmd)

    fx()


def close_sf():
    cmd = """osascript -e 'quit app "Safari"'"""

    def sf():
        os.system(cmd)

    sf()


def open_discord():
    os.system("open /Applications/Discord.app")


def exit_discord():
    cmd = """osascript -e 'quit app "Discord"'"""

    def ds():
        os.system(cmd)

    ds()


def key():
    while True:
        try:
            if keyboard.is_pressed('tab+q'):  ### QUIT ###
                print('You Pressed A Key!')
                break

            elif keyboard.is_pressed("esc"):  ### keyboard pauses ###
                keyboard.wait("esc", callable(print("waiting")))  ### keyboard pause ###
                continue

            elif keyboard.is_pressed('control+e'):
                print("resume")
                continue

            elif keyboard.is_pressed('right shift+s'):  ### Safari open ###
                print("you have pressed s")
                print("opening safari")
                safari()
                time.sleep(1)
                continue

            elif keyboard.is_pressed('right shift+o'):  ### safari closing ###
                print("you have pressed o")
                print("closing down safari")
                close_sf()
                time.sleep(1)
                continue

            elif keyboard.is_pressed('right shift+f'):  ### open Firefox ###
                print("you have pressed f")
                print("opening firefox")
                firefox()
                time.sleep(1)
                continue

            elif keyboard.is_pressed('q'):  ### Firefox closing ###
                print("you have pressed t")
                print("closing down firefox")
                close_fx()
                time.sleep(1)
                continue

            elif keyboard.is_pressed('w'):
                time.sleep(2)
                if keyboard.is_pressed('e'):
                    time.sleep(1)
                    if keyboard.is_pressed('r'):
                        print("you have pressed w")
                        continue

            elif keyboard.is_pressed('right shift+d'):  ### discord open ###
                print("opening discord")
                open_discord()
                time.sleep(1)
                continue

            elif keyboard.is_pressed("right shift+a"):  ### discord close ###
                print("you have pressed a")
                print("\n")
                print("exiting Discord")
                exit_discord()
                time.sleep(1)
                continue

            elif keyboard.is_pressed('right shift+n'):
                print("you have pressed umn")
                continue

            elif keyboard.is_pressed(';'):
                print("00000")
                continue

            else:
                continue

        except KeyboardInterrupt:  ### Reboot ###
            print("Reboot")
            key()


a = input("you wanna do it ")  ### introduction ###
if a == "y":
    key()
else:
    quit()
