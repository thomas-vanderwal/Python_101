#This library covers creating and interacting with configuration files.
# These files are generally used to store application or OS settings

from configparser import ConfigParser

def createConfig(path):
    config = ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", 'font_size', '10')
    config.set('Settings', 'font_style', 'Normal')
    config.set('Settings', 'font_info', 'You are using %(font)s at %(font_size)s pt')

    with open(path, 'w') as config_file:
        config.write(config_file)

if __name__ == '__main__':
    path = 'settings.ini'
    createConfig(path)
