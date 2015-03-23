Sample Markdown Cheat Sheet
=========================== 

This is a sample markdown file to help you write Markdown quickly :)

If you use the fabulous [Sublime Text 2/3 editor][ST] along with the [Markdown Preview plugin][MarkdownPreview], open your ST2 Palette with `CMD+⇧+P` then choose `Markdown Preview in browser` to see the result in your browser.

## Text basics
this is *italic* and this is **bold** .  another _italic_ and another __bold__

this is `important` text. and percentage signs : % and `%`

This is a paragraph with a footnote (builtin parser only). [^note-id]

Insert `[ TOC ]` without spaces to generate a table of contents (builtin parsers only).

## Indentation
> Here is some indented text
>> even more indented

## Titles
# Big title (h1)
## Middle title (h2)
### Smaller title (h3)
#### and so on (hX)
##### and so on (hX)
###### and so on (hX)
# TODO: write some function
# TODO: define ports 
# Big title (h1)
# BUG: smth wrong
# BUG: this code does not wor
## Example lists (1)

 - bullets can be `-`, `+`, or `*`

```python
date_arry = reversed(res_draw[1].split('-'))
    res_balls = res_draw[4].split(',')
    tron_list = [res_draw[2], res_draw[3]]
    count_draw = dict(
        comp='unl',
        draw=int(res_draw[0], 10),
        date='{}.{}.{}'.format(*date_arry),
        tron=tron_list,
        results=res_balls
```

        with indented text inside

 - bullet list 3
 + bullet list 4
 * bullet list 5
