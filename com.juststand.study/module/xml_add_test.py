#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/30 下午4:10

import xml.etree.ElementTree as et

new_xml = et.Element('name_list')
name = et.SubElement(new_xml, 'name', attrib={'enrolled':'yes'})
age = et.SubElement(name, 'age', attrib={'checked':'no'})
sex = et.SubElement(name, 'sex')
age.text = '20'
sex.text = 'man'

file = et.ElementTree(new_xml)
file.write('test.xml', encoding='utf-8', xml_declaration=True)
et.dump(new_xml)