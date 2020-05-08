from markdown2 import markdown
from lxml import html
import os

def load_ft_para_todos_posts(dict):
    posts_dir = 'content/ft_para_todos/blog/'
    all_data = []
    filename = posts_dir + 'posts.md'
    content = html.fromstring(markdown(open(filename, 'r').read()))
    all_data.append({
        "authors": content.xpath('//h1/text()'),
        "dates": content.xpath('//h2/text()'),
        "titles": content.xpath('//h3/text()'),
        "briefings": content.xpath('//h4/text()'),
        "links": content.xpath('//h5/text()'),
        "actions": content.xpath('//h6/text()')
    })

    dict['FT_PARA_TODOS_CONTENT'] = all_data