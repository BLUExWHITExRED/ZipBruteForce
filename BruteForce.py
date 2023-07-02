import zipfile
from termcolor import cprint
import time


def loading_bar(delay):
        print("[", end="")
        for _ in range(40):
            time.sleep(delay)
            print("#", end="", flush=True)
        print("]")


print('')
print('')
cprint('               $$\      $$\                     $$\                            $$$$$$\                               $$\       ', "light_green")
cprint('               $$$\    $$$ |                    $$ |                          $$  __$$\                              $$ |      ', "light_green")
cprint('               $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$ |  $$\  $$$$$$\  $$\   $$\ $$ /  \__| $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\ ', "light_green")
cprint('               $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ | $$  |$$  __$$\ $$ |  $$ |$$ |      $$  __$$\ \____$$\ $$  _____|$$ | $$  |', "light_green")
cprint('               $$ \$$$  $$ |$$ /  $$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  $$ |$$ |      $$ |  \__|$$$$$$$ |$$ /      $$$$$$  / ', "light_green")
cprint('               $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |  $$ |$$ |  $$\ $$ |     $$  __$$ |$$ |      $$  _$$<  ', "light_green")
cprint('               $$ | \_/ $$ |\$$$$$$  |$$ |  $$ |$$ | \$$\ \$$$$$$$\ \$$$$$$$ |\$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ ', "light_green")
cprint('               \__|     \__| \______/ \__|  \__|\__|  \__| \_______| \____$$ | \______/ \__|      \_______| \_______|\__|  \__|', "light_green")
cprint('                                                                    $$\   $$ | ', "light_green")
cprint('                                                                    \$$$$$$  |    V.1.0 🆉🅸🅿', "light_green")
cprint('                                                                     \______/ ', "light_green")
print('')
print('                                          ', end='')
loading_bar(0.1)
print('                                          ', end='')
loading_bar(0.1)
print('                                          ', end='')
print('')
time.sleep(1)


def crack_zip(zip_file_param, charset_filename):
    with open(charset_filename) as f:
        for password in f:
            password = password.strip()
            print('$~', end='')
            cprint(password, "light_magenta")
            try:
                zip_file_param.extractall(pwd=password.encode())
                print('')
                print('#####################')
                cprint(f'       {password}', "red", "on_black", attrs=["bold"])
                print('#####################')
                print('')
                return password
            except Exception as e:
                pass

    print("Error")
    return None




# Example usage
zip_filename = input('         Zip directory: ')
charset_filename = input('          Password list directory: ')

with zipfile.ZipFile(zip_filename) as zip_file:
    cracked_password = crack_zip(zip_file, charset_filename)
