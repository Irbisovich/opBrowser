#opBrowser Beta v0.1

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
                        self.command, self.attribute = self.line.strip(' ')
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

    def __init__(self, bios_enabled=False, version='Dev', version_name='Beta', browser_creator='IrbisX7', browser_name='opBrowser'):
        self.core = self.Core(bios_enabled, version, version_name, browser_creator, browser_name)

OPBrowser(True)
