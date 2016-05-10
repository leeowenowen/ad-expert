import os
import sys

class FileUtil:
    @staticmethod
    def writeFile(path, content):
        with open(path, 'w') as output:
            output.write(content)