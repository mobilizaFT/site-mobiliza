from jinja2 import Environment, PackageLoader, Template
from content.ft_ensina.load_content import load_ft_ensina_videos
from content.ft_para_todos.load_content import load_ft_para_todos_posts
import logging
import config
import shutil
import os

def generate_main_pages():
	env = Environment(loader=PackageLoader('generator', f'template/'))
	configs = { item: getattr(config, item) for item in dir(config) if not item.startswith("__") }
	load_ft_ensina_videos(configs)
	load_ft_para_todos_posts(configs)
	for folder in config.MAINPAGES:
		for page in os.listdir(f'template/{folder}'):
			template = env.get_template(f'{folder}/{page}')
			index_html = template.render(configs)
			with open(f'{page}', 'w') as file:
				file.write(index_html)

if __name__ == '__main__':
	generate_main_pages()
