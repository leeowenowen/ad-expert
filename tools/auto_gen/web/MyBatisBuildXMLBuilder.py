#coding:utf-8

import os
import sys
from string import Template

template_string = \
'''\
<?xml version="1.0" encoding="UTF-8"?>
<project default="genfiles" basedir=".">
    <target name="genfiles" description="Generate the files">
        <taskdef name="mbgenerator" classname="org.mybatis.generator.ant.GeneratorAntTask" classpath="$CLASSPATH" />
        <mbgenerator overwrite="true" configfile="$PATH" verbose="false">
        </mbgenerator>
    </target>
</project>
'''
def Gen(class_path, config_file_path,build_xml_path):
    template = Template(template_string)
    content = template.substitute(CLASSPATH=class_path, PATH=config_file_path);
    with open(build_xml_path, 'w') as output:
        output.write(content)