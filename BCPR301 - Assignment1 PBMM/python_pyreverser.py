import os


class PythonReverse:

    def reverse(self):
        os.system("{pyreverse_file} {flags} {input_data_file}".format(
        #pyreverse_file="H:\\Ara\\Software\\Anaconda5.0.1VirEnvir\\Scripts\\pyreverse.exe",
        pyreverse_file="D:\\Mikescode\\Anaconda3\\Scripts\\pyreverse.exe",
        flags="-f ALL -m y -S",
        input_data_file=".\\" + self))
        #input_data_file=".\\test_code" + self + ".py"))

        os.rename("classes.dot", "test_code" + self + ".dot")


        os.system("{dot_file} {flags} {input_dot_file}".format(dot_file=".\\graphviz-2.38\\release\\bin\\dot.exe",
                                                       flags="-v -O -Tjpeg",
                                                       input_dot_file=".\\" + self + ".dot"))
                                                       #input_dot_file=".\\test_code" + self + ".dot"))

#if __name__ == "__main__":
   # PythonReverse.reverse(str(2))


