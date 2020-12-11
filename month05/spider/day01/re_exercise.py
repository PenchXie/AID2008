import re
html = """
<div class="animal">
    <p class="name">
            <a title="Tiger"></a>
    </p>
    <p class="content">
            Two tigers two tigers run fast
    </p>
</div>
​
<div class="animal">
    <p class="name">
            <a title="Rabbit"></a>
    </p>
​
    <p class="content">
            Small white rabbit white and white
    </p>
</div>
"""
regex = '.*?title="(\w+?)".*?"content">\n\s+(.*?)\n\s+</p>'
r_list = re.findall(regex, html, re.S)
print(r_list)
