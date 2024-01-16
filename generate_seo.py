import os

# Assuming you want the BASE_URL to be the name of the parent directory of the script
BASE_URL = 'https://' + os.path.basename(os.path.dirname(os.path.abspath(__file__))) + '/'

def get_html_paths():
    # Return relative paths for HTML files
    return [os.path.relpath(os.path.join(root, path), start=".") for root, _, paths in os.walk('.') for path in paths if path.endswith('.html') or path.endswith('.htm')]

def generate_file(filename, content):
    with open(f'./{filename}', 'w') as file:
        file.write(content)

html_paths_list = get_html_paths()

# Generating content for robots.txt, appending Disallow entries for SEO
robots_content = 'User-agent: *\n'
robots_content += '\n'.join([f"Allow: /{path}" for path in html_paths_list]) + '\n'
robots_content += f'Sitemap: {BASE_URL}sitemap.xml\n'
generate_file('robots.txt', robots_content)

# Generating XML content for sitemap.xml
urls = '\n'.join([f'  <url><loc>{BASE_URL}{path.replace(os.sep, "/")}</loc></url>' for path in html_paths_list])
sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>'''
generate_file('sitemap.xml', sitemap_content)
