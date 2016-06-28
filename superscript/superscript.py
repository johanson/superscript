# -*- coding: utf-8 -*-

import re
from pelican import signals
from logging import warning, info

def configure(generator):

	# To use this plugin, ensure the following are set in your pelicanconf.py file:
	# 
	# PLUGINS = ['superscript']
	# 
	# And whether want to use sup html element:
	# 
	# SUPERSCRIPT = {
	# 	'html_element': 'sup'
	# }
	# 
	# Or span element:
	# 
	# SUPERSCRIPT = {
	# 	'html_element': 'span'
	# }
	
	if 'SUPERSCRIPT' in generator.settings and 'html_element' in generator.settings['SUPERSCRIPT']:
		configure.element = generator.settings['SUPERSCRIPT']['html_element']
		signals.content_object_init.connect(scan)
	else:
		warning("SUPERSCRIPT enabled, but not configured!")

def convert(ordinal):

	# Probably you want something like that in your CSS file:
	# sup, .superscript {
	# 	font-size: .8em;
	# 	line-height: 0;
	# 	position: relative;
	# 	top: -.4em;
	# 	vertical-align: baseline;
	# }

	if configure.element == "sup":
		# 
		# The HTML Superscript Element (<sup>) defines a span of text that should be displayed, 
		# for typographic reasons, higher, and often smaller, than the main span of text.
		# 
		return '<sup>'+ ordinal + '</sup>'
	elif configure.element == "span":
		#  The problem with superscript (sup element) this is that, in a paragraph
		#  lines with superscript or subscript text will alter the height of that line, 
		#  resulting in an inconsistently spaced paragraph.
		#  Why you should use span instead of sup element:
		#  http://www.personal.psu.edu/ejp10/blogs/tlt/2007/02/beware_css_for_superscriptsubc.html
		return '<span class="superscript">'+ ordinal + '</span>'
	else:
		return ordinal

def scan(instance):

	content = instance._content

	if content is not None:
		
		# Positive Lookbehind - Assert that the regex below can be matched
		# [0-9] match a single character present in the list below
		# 0-9 a single character in the range between 0 and 9
		# (?:st|nd|rd|th) Non-capturing group
		# 1st Alternative: st
		# st matches the characters st literally (case sensitive)
		# 2nd Alternative: nd
		# nd matches the characters nd literally (case sensitive)
		# 3rd Alternative: rd
		# rd matches the characters rd literally (case sensitive)
		# 4th Alternative: th
		# th matches the characters th literally (case sensitive)

		superscripts = re.compile(r'(?<=[0-9])(?:st|nd|rd|th)')

		# Find and replace every match

		content = re.sub(superscripts, lambda m: convert(m.group(0)), content)

	instance._content = content

def register():
	signals.initialized.connect(configure)