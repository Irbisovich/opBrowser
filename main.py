#opBrowser Beta v0.1

from bs4 import BeautifulSoup
import pyfiglet
import requests
import os

class OPBrowser:
    class Core:
        class ErrorRaiser(Exception):
            def __init__(self, message, error_code):
                super().__init__(message)
                self.message, self.error_code = message, error_code

            def __str__(self):
                return f"{self.message} (Error Code: {self.error_code})"

        def __init__(self, bios_enabled, version, version_name, browser_creator, browser_name):
            if bios_enabled == True:
                print('\n' + self.fixed_figlet_format('opBrowser', f'{version_name} v{version} Testing Bios', 'kban'))

                while True:
                    self.user = os.environ['USERNAME']
                    self.line = str(input(f'{self.user}: '))

                    try:
                        self.command, self.attribute = self.line.split(' ', 1)
                    except ValueError:
                        self.command = self.line

                    if self.command == 'info':
                        self.info = {
                            'browser_name': f'Browser name: {browser_name}',
                            'version': f'Version: {version}',
                            'browser_creator': f'Browser creator: {browser_creator}'
                        }

                        self.info_list = []
                        for info in self.info:
                            self.info_list.append(self.info[info])

                        self.info_list = '\n'.join(self.info_list)

                        print(f'\n{self.info_list}\n')

                    elif self.command == 'parse':
                        try:
                            self.protocol = self.attribute.split('//')[0]

                            if f'{self.protocol}//' in ['https://', 'http://']:
                                self.response = requests.get(self.attribute)
                            else:
                                try:
                                    self.response = requests.get('https://' + self.attribute)
                                except requests.exceptions.InvalidURL:
                                    self.response = requests.get('http://' + self.attribute)
                        except requests.exceptions.SSLError:
                            raise self.ErrorRaiser(f'Error! ({self.attribute} can\'t be opened.)', 4)

                        self.code = BeautifulSoup(self.response.text, 'lxml')

                        print(f'\n{self.code}\n')

                    elif self.command == 'quit':
                        quit()

                    elif self.command == 'help':
                        self.commands_info = {
                            'parse': '\'parse\': parsing site and prints code.',
                            'info': '\'info\': shows application info.',
                            'help': '\'help\': shows commands info.'
                        }

                        try:
                            if self.attribute in list(self.commands_info):
                                print(f'{self.commands_info[self.attribute]}')

                            else:
                                raise self.ErrorRaiser(f'Wrong attribute: command \'{self.attribute}\' don\'t exist!', 3)

                        except AttributeError:
                            self.commands_info_list = []
                            for command_info in self.commands_info:
                                self.commands_info_list.append(self.commands_info[command_info])

                            self.commands_info = '\n'.join(self.commands_info_list)

                            print(f'\n{self.commands_info}\n')

                    else:
                        raise self.ErrorRaiser('Wrong command!', 2)

            elif bios_enabled == False:
                pass

            else:
                raise self.ErrorRaiser('Incorrect option for Testing Bios!', 1)

        def fixed_figlet_format(self, text, small_text='', font='standard'):
            letters = []
            strings = []

            for letter in list(text):
                letters.append(pyfiglet.figlet_format(letter, font))

            string_num = 0

            while True:
                string = ''

                try:
                    for letter in letters:
                        for current_string in letter.split('\n')[string_num]:
                            string = string + current_string + ''

                    string_num += 1
                    strings.append(string)

                except IndexError:
                    strings[string_num - 4] = strings[string_num - 4] + ' ' + small_text
                    break

            return '\n'.join(strings)

    def __init__(self, bios_enabled=False, version='', version_name='', browser_creator='', browser_name=''):
        self.core = self.Core(bios_enabled, version, version_name, browser_creator, browser_name)

OPBrowser(True, 'Dev', 'Beta', 'IrbisX7', 'opBrowser')
