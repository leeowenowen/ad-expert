# coding:utf-8
import sys
import os
from string import Template

config_start = \
'''
<generatorConfiguration>
	<classPathEntry location="lib/mysql-connector-java-5.1.6-bin.jar" />
	<context id="DB2Tables" targetRuntime="MyBatis3">
		<plugin type="org.mybatis.generator.plugins.PaginationPlugin" />
		<plugin type="org.mybatis.generator.plugins.SerializablePlugin" />
		<commentGenerator>
			<property name="suppressDate" value="true" />
		</commentGenerator>
		<jdbcConnection driverClass="com.mysql.jdbc.Driver"
			connectionURL="$CONNECTION_URL"
			userId="$USER" password="$PASSWORD">
		</jdbcConnection>
		<javaTypeResolver>
			<property name="forceBigDecimals" value="false" />
		</javaTypeResolver>
		<javaModelGenerator targetPackage="$PACKAGE_NAME.dao.mysql.entity"
			targetProject="src/main/java">
			<property name="enableSubPackages" value="true" />
			<property name="trimStrings" value="true" />
		</javaModelGenerator>
		<sqlMapGenerator targetPackage="$PACKAGE_NAME.dao.mysql"
			targetProject="src/main/resources">
			<property name="enableSubPackages" value="true" />
		</sqlMapGenerator>
		<javaClientGenerator type="XMLMAPPER"
			targetPackage="$PACKAGE_NAME.dao.mysql" targetProject="src/main/java">
			<property name="enableSubPackages" value="true" />
		</javaClientGenerator>
'''
table_template =  \
'''
                <table tableName="$TABLE_NAME" domainObjectName="$OBJECT_NAME"
                        enableCountByExample="false" enableDeleteByExample="false"
                        enableSelectByExample="false" enableUpdateByExample="false">
                        <generatedKey column="id" identity="true" sqlStatement="mysql"
                                type="post" />
                </table>
'''
config_end =  \
'''
	</context>
</generatorConfiguration>
'''

def GenConfig(connect_url, user, password, package_name, tables, dest_path):
    template_config_start = Template(config_start)
    config = template_config_start.substitute(CONNECTION_URL=connect_url, USER=user,PASSWORD=password, PACKAGE_NAME=package_name)
    for table in tables:
     	name = table.name()
      	template_config_table = Template(table_template)
       	table_config = template_config_table.substitute(TABLE_NAME=name, OBJECT_NAME=name)
    	config += table_config
     	config += '\r\n'
    config += config_end

    with open(dest_path, 'w') as output:
        output.write(config)
  
  
