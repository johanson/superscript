# SUPERSCRIPT for Pelican

Superscript for [Pelican](https://github.com/getpelican/pelican) finds ordinals ( 1st, 2nd, 3rd, 4th etc.) in the content and wraps them with an element(s) for better typography.

## Usage

To use this plugin, ensure the following are set in your pelicanconf.py file:
	
1) Enable the superscript plugin:

`PLUGINS = ['superscript']`
	
2) Configure the plugin:

* Decide whether want to use `<sup>` HTML element to wrap the ordinals:
	
```
SUPERSCRIPT = {
	'html_element': 'sup'
}
```

* Or `<span>` element:

```
SUPERSCRIPT = {
	'html_element': 'span'
}
```

3) Probably you want something like this in your CSS file:

```
sup, .superscript {
	font-size: .8em;
	line-height: 0;
	position: relative;
	top: -.4em;
	vertical-align: baseline;
}
```

Read about the [problems with Superscript and Subscript](http://htmldog.com/techniques/superscript/).