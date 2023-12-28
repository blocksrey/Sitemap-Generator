import os

BASE_URL = 'https://www.xholes.com/'

def get_html_paths():
	return [path[:-5] for _, _, paths in os.walk('./') for path in paths if path.endswith('.html')]

def generate_file(filename, content):
	with open(f'./{filename}', 'w') as file:
		file.write(content)

html_paths_list = get_html_paths()

robots_content = f'User-agent: *\nDisallow: /\n'
robots_content += "\n".join([f"Allow: /{path}" for path in html_paths_list]) + '\n'
robots_content += f'Sitemap: {BASE_URL}sitemap.xml'
generate_file('robots.txt', robots_content)

urls = [f'<url><loc>{BASE_URL}{path}</loc></url>' for path in html_paths_list] + [f'<url><loc>{BASE_URL}</loc></url>']
sitemap_content = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{" ".join(urls)}</urlset>'
generate_file('sitemap.xml', sitemap_content)