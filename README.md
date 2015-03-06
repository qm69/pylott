---
    # Builtin values
    references:
        - references.md
        - abbreviations.md
        - footnotes.md

    destination: destination.html

    date_arry = reversed(res_draw[1].split('-'))
    res_balls = res_draw[4].split(',')
    tron_list = [res_draw[2], res_draw[3]]
    count_draw = dict(
        comp='unl',
        draw=int(res_draw[0], 10),
        date='{}.{}.{}'.format(*date_arry),
        tron=tron_list,
        results=res_balls
    )

    # Settings overrides
    settings:
        enabled_extensions:
        - extra
        - github
        - toc
        - headerid
        - smarty(smart_quotes=False) # smart quotes interferes with attr_list
        - meta
        - wikilinks
        - admonition
        - codehilite(guess_lang=False,pygments_style=github)
---