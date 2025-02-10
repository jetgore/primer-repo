import requests
from bs4 import BeautifulSoup

def get_wordpress_version(url):
    try:
        response = requests.get(f'http://{url}/readme.html')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            version_tag = soup.find('br').next_sibling.strip()
            if version_tag:
                return version_tag
        return "No se pudo determinar la versión de WordPress."
    except requests.RequestException as e:
        return f"Error al conectar con el sitio: {e}"

def main():
    url = input("Ingrese la URL del sitio (sin 'http://'): ")
    version = get_wordpress_version(url)
    print(f"La versión de WordPress es: {version}")

if __name__ == '__main__':
    main()