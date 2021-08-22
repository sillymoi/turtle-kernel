from __future__ import print_function

from metakernel import MetaKernel
import sys

class TurtleKernel(MetaKernel):
    implementation = 'MetaKernel Echo'
    implementation_version = '1.0'
    language = 'turtle'
    language_version = '0.1'
    banner = "MetaKernel Echo Turtle - as useful as a parrot speaking turtle"
    language_info = {
        'mimetype': 'text/turtle',
        'name': 'turtle',
        'codemirror_mode': {
           'name': 'turtle'
        },
        'pygments_lexer': 'turtle',
        'version'       : "2007.02",
        'file_extension': '.ttl',
    }
    kernel_json = {
        'argv': [
            sys.executable, '-m', 'turtle_kernel', '-f', '{connection_file}'],
        'display_name': 'MetaKernel Turtle',
        'language': 'turtle',
        'name': 'turtle_kernel'
    }

    def get_usage(self):
        return "This is the turtle echo kernel."

    def do_execute_direct(self, code):
        self.Print("@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.")
        self.Print("@prefix exterms: <http://www.example.org/terms/>.")
        self.Print("<http://www.example.org/index.html> exterms:creation-date \"August 16, 1999\".")


    def repr(self, data):
        return repr(data)


if __name__ == '__main__':
    TurtleKernel.run_as_main()