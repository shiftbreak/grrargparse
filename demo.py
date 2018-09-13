#!/usr/bin/python
from grrargparse import APIModule, get_instance


# define module
class TestModule(APIModule):

    # setup other fields
    help = "A module to concat files"
    name = "concat"

    def add_arguments(self):
        self.add_multi_file_option(letter="f",word="file",question="file to concat",var_name="files",help="one or more file(s) to concat",must_exist=True,must_not_exist=False,ask_for_titles=False)
        self.add_single_file_option(letter="o", word="output", question="Specify output file", var_name="outfile", help="Output File To Write", must_exist=False, must_not_exist=True, default_file="/tmp/out.txt")
        self.add_yn_option(letter="c", word="concat", question="concatenate", var_name="concatenate", help="Concatenate files", default_yn=APIModule.DEFAULT_Y)

        # other supported methods
        # self.add_folder_option()
        # self.add_yn_file_option()
        # self.add_text_option()
        # self.add_file_option()


    def do(self):

        to_concat = []

        # a multi valued argument
        for f in self.get_var("files"):
            to_concat.append(f)


        # a boolean argument
        if self.get_var("concatenate"):

            out_text = ""
            for f_name in to_concat:
                print("contactenating file:" + f_name)
                f = open(f_name,"r")
                text = f.read()
                out_text += text + "\n"

            out_file = open(self.get_var("outfile"),"w")
            print("Writing to specified output file: " +self.get_var("outfile"))
            out_file.write(out_text)
            print("files concatenated")


class DummyModule(APIModule):

    name = "dummy"
    help = "not necessary"

    def add_arguments(self):
        """
        no arguments to add
        """

    def do(self):
        print("dummmy module")



# instantiate the command line
cmd = get_instance()

# optionally specify global arguments that are required
#cmd.add_global_argument()

# register the defined module
cmd.register_module(TestModule)
cmd.register_module(DummyModule)

# tells grrargparse to automatically run this module (either specify this or run_all...)
#cmd.add_auto_module(TestModule)

# tells grrargparse to run all modules regardless of what is specified
cmd.run_all_modules()

# do nothing now as it will run automatically on exit.

