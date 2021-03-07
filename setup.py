import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
    'docassemble==1.2.39',
    'docassemble.base==1.2.39',
    'docassemble.demo==1.2.39',
    "3to2==1.1.1",
    "airtable-python-wrapper==0.15.1",
    "alembic==1.4.3",
    "aloe==0.2.0",
    "amqp==5.0.2",
    "ansicolors==1.1.8",
    "asn1crypto==1.4.0",
    "astunparse==1.6.3",
    "atomicwrites==1.4.0",
    "attrs==20.3.0",
    "azure-common==1.1.26",
    "azure-core==1.9.0",
    "azure-nspkg==3.0.2",
    "azure-identity==1.5.0",
    "azure-keyvault-secrets==4.2.0",
    "azure-storage-blob==12.6.0",
    "Babel==2.9.0",
    "bcrypt==3.2.0",
    "beautifulsoup4==4.9.3",
    "billiard==3.6.3.0",
    "bleach==3.3.0",
    "blinker==1.4",
    "boto==2.49.0",
    "boto3==1.16.25",
    "botocore==1.19.25",
    "cachetools==4.1.1",
    "celery==5.0.2",
    "certifi==2020.11.8",
    "cffi==1.14.4",
    "chardet==3.0.4",
    "click==7.1.2",
    "click-didyoumean==0.0.3",
    "click-repl==0.1.6",
    "colorama==0.4.4",
    "configparser==5.0.1",
    "convertapi==1.4.0",
    "crayons==0.3.1",
    "cryptography==3.3.2",
    "dnspython==1.16.0",
    "Docassemble-Flask-User==0.6.23",
    "docassemblekvsession==0.3",
    "docopt==0.6.2",
    "docutils==0.16",
    "docxcompose==1.3.0",
    "docxtpl==0.11.2",
    "et-xmlfile==1.0.1",
    "eventlet==0.29.1",
    "Flask==1.1.2",
    "Flask-Babel==2.0.0",
    "Flask-Cors==3.0.9",
    "Flask-Login==0.5.0",
    "Flask-Mail==0.9.1",
    "Flask-SocketIO==4.3.1",
    "Flask-SQLAlchemy==2.4.4",
    "Flask-WTF==0.14.3",
    "future==0.18.2",
    "gcs-oauth2-boto-plugin==2.7",
    "geographiclib==1.50",
    "geopy==2.0.0",
    "gherkin-official==4.1.3",
    "google-api-core==1.23.0",
    "google-api-python-client==1.12.8",
    "google-auth==1.23.0",
    "google-auth-httplib2==0.0.4",
    "google-auth-oauthlib==0.4.2",
    "google-cloud-core==1.4.3",
    "google-cloud-storage==1.33.0",
    "google-cloud-translate==3.0.1",
    "google-crc32c==1.0.0",
    "google-i18n-address==2.4.0",
    "google-reauth==0.1.0",
    "google-resumable-media==1.1.0",
    "googleapis-common-protos==1.52.0",
    "greenlet==0.4.17",
    "grpcio==1.33.2",
    "gspread==3.6.0",
    "guess-language-spirit==0.5.3",
    "httplib2==0.19.0",
    "humanize==3.1.0",
    "hyphenate==1.1.0",
    "idna==2.10",
    "importlib-metadata==3.1.0",
    "importlib-resources==3.3.0",
    "iniconfig==1.1.1",
    "iso8601==0.1.13",
    "isodate==0.6.0",
    "itsdangerous==1.1.0",
    "jdcal==1.4.1",
    "jeepney==0.6.0",
    "jellyfish==0.6.1",
    "Jinja2==2.11.2",
    "jmespath==0.10.0",
    "joblib==0.17.0",
    "keyring==21.5.0",
    "kombu==5.0.2",
    "libcst==0.3.14",
    "links-from-link-header==0.1.0",
    "lxml==4.6.2",
    "Mako==1.1.3",
    "Marisol==0.3.0",
    "Markdown==3.3.3",
    "MarkupSafe==1.1.1",
    "mdx-smartypants==1.5.1",
    "minio==6.0.0",
    "monotonic==1.5",
    "msrest==0.6.19",
    "mypy-extensions==0.4.3",
    "namedentities==1.5.2",
    "netifaces==0.10.9",
    "nltk==3.5",
    "nose==1.3.7",
    "num2words==0.5.10",
    "numpy==1.19.4",
    "oauth2client==4.1.3",
    "oauthlib==3.1.0",
    "openpyxl==3.0.5",
    "ordered-set==4.0.2",
    "packaging==20.4",
    "pandas==1.1.4",
    "passlib==1.7.4",
    "pathlib==1.0.1",
    "Docassemble-Pattern==3.6.1",
    "pdfminer.six==20201018",
    "phonenumbers==8.12.13",
    "Pillow==8.0.1",
    "pkginfo==1.6.1",
    "pluggy==0.13.1",
    "ply==3.11",
    "prompt-toolkit==3.0.8",
    "proto-plus==1.11.0",
    "protobuf==3.14.0",
    "psutil==5.7.3",
    "psycopg2-binary==2.8.6",
    "py==1.9.0",
    "pyasn1==0.4.8",
    "pyasn1-modules==0.2.8",
    "pycountry==20.7.3",
    "pycparser==2.20",
    "pycryptodome==3.9.9",
    "pycryptodomex==3.9.9",
    "pycurl==7.43.0.6",
    "Pygments==2.7.2",
    "PyJWT==1.7.1",
    "PyLaTeX==1.4.1",
    "pyOpenSSL==19.1.0",
    "pyotp==2.4.1",
    "pyparsing==2.4.7",
    "pyPdf==1.13",
    "PyPDF2==1.26.0",
    "pypdftk==0.4",
    "pypng==0.0.20",
    "PySocks==1.7.1",
    "pytest==6.1.2",
    "python-dateutil==2.8.1",
    "python-docx==0.8.10",
    "python-editor==1.0.4",
    "python-engineio==3.13.2",
    "python-http-client==3.3.1",
    "python-ldap==3.3.1",
    "python-socketio==4.6.0",
    "pytz==2020.4",
    "pyu2f==0.1.5",
    "PyYAML==5.3.1",
    "pyzbar==0.1.8",
    "qrcode==6.1",
    "rauth==0.7.3",
    "readme-renderer==28.0",
    "redis==3.5.3",
    "regex==2020.11.13",
    "reportlab==3.3.0",
    "repoze.lru==0.7",
    "requests==2.25.0",
    "requests-oauthlib==1.3.0",
    "requests-toolbelt==0.9.1",
    "retry-decorator==1.1.1",
    "rfc3339==6.2",
    "rfc3986==1.4.0",
    "rsa==4.6",
    "ruamel.yaml==0.16.12",
    "ruamel.yaml.clib==0.2.2",
    "s3transfer==0.3.3",
    "s4cmd==2.1.0",
    "scikit-learn==0.23.2",
    "scipy==1.5.4",
    "selenium==3.141.0",
    "SecretStorage==3.3.0",
    "sendgrid==6.4.7",
    "simplekv==0.14.1",
    "six==1.15.0",
    "sklearn==0.0",
    "SocksiPy-branch==1.1",
    "sortedcontainers==2.3.0",
    "soupsieve==2.0.1",
    "SQLAlchemy==1.3.20",
    "starkbank-ecdsa==1.1.0",
    "tailer==0.4.1",
    "docassemble-textstat==0.7.1",
    "threadpoolctl==2.1.0",
    "titlecase==1.1.1",
    "toml==0.10.2",
    "tqdm==4.53.0",
    "twilio==6.48.0",
    "twine==3.2.0",
    "typing-extensions==3.7.4.3",
    "typing-inspect==0.6.0",
    "tzlocal==2.1",
    "ua-parser==0.10.0",
    "uritemplate==3.0.1",
    "urllib3==1.26.2",
    "us==2.0.2",
    "user-agents==2.2.0",
    "uWSGI==2.0.19.1",
    "vine==5.0.0",
    "wcwidth==0.2.5",
    "webdriver-manager==3.2.2",
    "webencodings==0.5.1",
    "Werkzeug==1.0.1",
    "WTForms==2.1",
    "xfdfgen==0.4",
    "xlrd==1.2.0",
    "XlsxWriter==1.3.7",
    "xlwt==1.3.0",
    "zipp==3.4.0"
]

setup(name='docassemble.webapp',
      version='1.2.39',
      python_requires='>=3.8',
      description=('The web application components of the docassemble system.'),
      long_description=read("README.md"),
      long_description_content_type='text/markdown',
      author='Jonathan Pyle',
      author_email='jhpyle@gmail.com',
      license='MIT',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages = ['docassemble'],
      install_requires = install_requires,
      zip_safe = False,
      package_data={'docassemble.webapp': ['alembic.ini', os.path.join('alembic', '*'), os.path.join('alembic', 'versions', '*'), os.path.join('data', '*.*'), os.path.join('data', 'static', '*.*'), os.path.join('data', 'static', 'favicon', '*.*'), os.path.join('data', 'questions', '*.*'), os.path.join('templates', 'base_templates', '*.html'), os.path.join('templates', 'flask_user', '*.html'), os.path.join('templates', 'flask_user', 'emails', '*.*'), os.path.join('templates', 'pages', '*.html'), os.path.join('templates', 'pages', '*.xml'), os.path.join('templates', 'pages', '*.js'), os.path.join('templates', 'users', '*.html'), os.path.join('static', 'app', '*.*'), os.path.join('static', 'yamlmixed', '*.*'), os.path.join('static', 'sounds', '*.*'), os.path.join('static', 'examples', '*.*'), os.path.join('static', 'fontawesome', 'js', '*.*'), os.path.join('static', 'fontawesome', 'css', '*.*'), os.path.join('static', 'office', '*.*'), os.path.join('static', 'bootstrap-fileinput', 'img', '*'), os.path.join('static', 'img', '*'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'locales', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'plugins', '*'), os.path.join('static', 'bootstrap-slider', 'dist', '*.js'), os.path.join('static', 'bootstrap-slider', 'dist', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fa', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*.js'), os.path.join('static', 'bootstrap-combobox', 'css', '*.css'), os.path.join('static', 'bootstrap-combobox', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', '*.md'), os.path.join('static', 'bootstrap', 'js', '*.*'), os.path.join('static', 'bootstrap', 'css', '*.*'), os.path.join('static', 'labelauty', 'source', '*.*'), os.path.join('static', 'codemirror', 'lib', '*.*'), os.path.join('static', 'codemirror', 'addon', 'search', '*.*'), os.path.join('static', 'codemirror', 'addon', 'display', '*.*'), os.path.join('static', 'codemirror', 'addon', 'scroll', '*.*'), os.path.join('static', 'codemirror', 'addon', 'dialog', '*.*'), os.path.join('static', 'codemirror', 'addon', 'edit', '*.*'), os.path.join('static', 'codemirror', 'addon', 'hint', '*.*'), os.path.join('static', 'codemirror', 'mode', 'yaml', '*.*'), os.path.join('static', 'codemirror', 'mode', 'markdown', '*.*'), os.path.join('static', 'codemirror', 'mode', 'javascript', '*.*'), os.path.join('static', 'codemirror', 'mode', 'css', '*.*'), os.path.join('static', 'codemirror', 'mode', 'python', '*.*'), os.path.join('static', 'codemirror', 'mode', 'htmlmixed', '*.*'), os.path.join('static', 'codemirror', 'mode', 'xml', '*.*'), os.path.join('static', 'codemirror', 'keymap', '*.*'), os.path.join('static', 'areyousure', '*.js'), os.path.join('static', 'popper', '*.*'), os.path.join('static', 'popper', 'umd', '*.*'), os.path.join('static', 'popper', 'esm', '*.*'), os.path.join('static', '*.html'), os.path.join('static', 'css', '*.*'), os.path.join('static', 'js', '*.*')]},
     )
