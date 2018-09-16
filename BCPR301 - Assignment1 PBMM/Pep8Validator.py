import autopep8 as pep8
from os.path import abspath


class AutomatePep8:

    def validate_code(self):
        try:
            validated_code = pep8.fix_code(self, options={'verbose': 1})
            return validated_code
        except AttributeError:
            print("The input " + self + " is not a valid attribute")
        except Exception as e:
            (print(e))

    def validate_file(self):
        try:
            validated_file = pep8.fix_file(abspath(self))
            return validated_file
        except FileExistsError:
            print("The file in " + self + "does not seem to exist")
        except FileNotFoundError:
            print("The file " + self + " Could not be found in that file path")
        except Exception as e:
            print(e)


#if __name__ == "__main__":

    #Pepper = AutomatePep8
    #code = ('x.has_key(y)\n')
    #file = ("test_code2.py")
    #lol = Pepper.validate_code(code)
    #lolzers = Pepper.validate_file(file)
    #print(lolzers)
    #print(lol)



