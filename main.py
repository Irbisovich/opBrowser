#opBrowser Beta v0.1

import pyfiglet

class OPBrowser:
    class Core:
        class ErrorRaiser(Exception):
            def __init__(self, message, error_code):
                super().__init__(message)
                self.message, self.error_code = message, error_code

            def __str__(self):
                return f"{self.message} (Error Code: {self.error_code})"

        def __init__(self, bios_enabled):
            if bios_enabled == True:
                self.font = 'kban'

                print('\n' + self.fixed_figlet_format('opBrowser', 'Beta v0.1 Testing Bios', self.font))

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

    def __init__(self, bios_enabled=False):
        self.core = self.Core(bios_enabled)

OPBrowser(True)
