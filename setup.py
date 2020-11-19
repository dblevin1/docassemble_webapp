import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

openpyxl_version = "2.5.14" if sys.version.startswith('3.5') else "3.0.0"
twine_version = "1.15.0" if sys.version.startswith('3.5') else "2.0.0"
install_requires = [
    'docassemble==1.1.102',
    'docassemble.base==1.1.102',
    'docassemble.demo==1.1.102',
    "3to2==1.1.1",
    "airtable-python-wrapper==0.12.0",
    "alembic==1.2.1",
    "amqp==2.5.1",
    "asn1crypto==1.2.0",
    "astunparse==1.6.2",
    "atomicwrites==1.3.0",
    "attrs==19.3.0",
    "azure-common==1.1.23",
    "azure-nspkg==3.0.2",
    "azure-storage==0.36.0",
    "Babel==2.7.0",
    "backports.csv==1.0.7",
    "bcrypt==3.1.7",
    "beautifulsoup4==4.8.1",
    "billiard==3.6.1.0",
    "bleach==3.1.4",
    "blinker==1.4",
    "boto==2.49.0",
    "boto3==1.10.2",
    "botocore==1.13.2",
    "cachetools==3.1.1",
    "celery[redis]==4.3.0",
    "certifi==2019.9.11",
    "cffi==1.13.1",
    "chardet==3.0.4",
    "cheroot==8.2.1",
    "CherryPy==18.3.0",
    "Click==7.0",
    "convertapi==1.1.0",
    "cryptography==3.2",
    "dnspython==1.16.0",
    "docutils==0.15.2",
    "docxcompose==1.0.2",
    "docxtpl==0.10.0",
    "et-xmlfile==1.0.1",
    "eventlet==0.25.1",
    "fdfgen==0.16.1",
    "feedparser==5.2.1",
    "Flask==1.1.1",
    "Flask-Babel==1.0.0",
    "Flask-Cors==3.0.8",
    "docassemblekvsession==0.2",
    "Flask-Login==0.4.1",
    "Flask-Mail==0.9.1",
    "Flask-SocketIO==4.2.1",
    "Flask-SQLAlchemy==2.4.1",
    "Flask-WTF==0.14.3",
    "Docassemble-Flask-User==0.6.22",
    "future==0.18.1",
    "gcs-oauth2-boto-plugin==2.5",
    "geographiclib==1.50",
    "geopy==1.20.0",
    "google-api-core==1.14.3",
    "google-api-python-client==1.7.11",
    "google-auth==1.22.1",
    "google-auth-httplib2==0.0.4",
    "google-auth-oauthlib==0.4.1",
    "google-cloud-core==1.0.3",
    "google-cloud-storage==1.20.0",
    "google-cloud-translate==2.0.0",
    "google-reauth==0.1.0",
    "google-resumable-media==0.4.1",
    "googleapis-common-protos==1.6.0",
    "greenlet==0.4.15",
    "grpcio==1.24.3",
    "gspread==3.3.0",
    "guess-language-spirit==0.5.3",
    "httplib2==0.18.0",
    "humanize==0.5.1",
    "idna==2.8",
    "importlib-metadata==0.23",
    "iso8601==0.1.12",
    "itsdangerous==1.1.0",
    "jaraco.functools==2.0",
    "jdcal==1.4.1",
    "jellyfish==0.5.6",
    "Jinja2==2.10.3",
    "jmespath==0.9.4",
    "joblib==0.14.0",
    "kombu==4.6.5",
    "links-from-link-header==0.1.0",
    "lxml==4.4.1",
    "Mako==1.1.0",
    "Marisol==0.3.0",
    "Markdown==3.1.1",
    "MarkupSafe==1.1.1",
    "mdx-smartypants==1.5.1",
    "minio==5.0.1",
    "monotonic==1.5",
    "more-itertools==7.2.0",
    "namedentities==1.5.2",
    "netifaces==0.10.9",
    "nltk==3.4.5",
    "numpy==1.17.3",
    "num2words==0.5.10",
    "oauthlib==3.1.0",
    "oauth2client==4.1.3",
    "openpyxl==" + openpyxl_version,
    "ordered-set==3.1.1",
    "packaging==19.2",
    "pandas==0.25.2",
    "passlib==1.7.1",
    "pathlib==1.0.1",
    "Pattern==3.6",
    "pdfminer.six==20200517",
    "phonenumbers==8.10.21",
    "Pillow==7.1.0",
    "pkginfo==1.5.0.1",
    "pluggy==0.13.0",
    "ply==3.11",
    "portend==2.5",
    "protobuf==3.10.0",
    "psutil==5.6.6",
    "psycopg2-binary==2.8.4",
    "py==1.8.0",
    "pyasn1==0.4.7",
    "pyasn1-modules==0.2.7",
    "pycountry==19.8.18",
    "pycparser==2.19",
    "pycryptodome==3.9.0",
    "pycryptodomex==3.9.0",
    "pycurl==7.43.0.3",
    "Pygments==2.4.2",
    "PyJWT==1.7.1",
    "PyLaTeX==1.3.1",
    "pyOpenSSL==19.0.0",
    "pyotp==2.3.0",
    "pyparsing==2.4.2",
    "pyPdf==1.13",
    "PyPDF2==1.26.0",
    "pypdftk==0.4",
    "Pyphen==0.9.5",
    "pypng==0.0.20",
    "PySocks==1.7.1",
    "pytest==5.2.2",
    "python-dateutil==2.8.0",
    "python-docx==0.8.10",
    "python-editor==1.0.4",
    "python-engineio==3.10.0",
    "python-ldap==3.2.0",
    "python-socketio==4.3.1",
    "pytz==2019.3",
    "pyu2f==0.1.4",
    "PyYAML==5.1.2",
    "pyzbar==0.1.8",
    "qrcode==6.1",
    "rauth==0.7.3",
    "readme-renderer==24.0",
    "redis==3.3.11",
    "reportlab==3.3.0",
    "repoze.lru==0.7",
    "requests==2.22.0",
    "requests-toolbelt==0.9.1",
    "retry-decorator==1.1.0",
    "rfc3339==6.2",
    "rsa==4.0",
    "ruamel.yaml==0.16.5",
    "ruamel.yaml.clib==0.2.0",
    "s3transfer==0.2.1",
    "s4cmd==2.1.0",
    "scikit-learn==0.21.3",
    "scipy==1.3.1",
    "simplekv==0.13.0",
    "six==1.12.0",
    "sklearn==0.0",
    "SocksiPy-branch==1.1",
    "sortedcontainers==2.1.0",
    "soupsieve==1.9.4",
    "SQLAlchemy==1.3.10",
    "tailer==0.4.1",
    "tempora==1.14.1",
    "textstat==0.5.6",
    "titlecase==0.12.0",
    "tqdm==4.36.1",
    "twilio==6.32.0",
    "twine==" + twine_version,
    "tzlocal==2.0.0",
    "ua-parser==0.8.0",
    "uritemplate==3.0.0",
    "urllib3==1.25.6",
    "us==1.0.0",
    "user-agents==2.1",
    "uWSGI==2.0.18",
    "vine==1.3.0",
    "wcwidth==0.1.7",
    "webencodings==0.5.1",
    "Werkzeug==1.0.0",
    "WTForms==2.1",
    "xlrd==1.2.0",
    "XlsxWriter==1.2.2",
    "xlwt==1.3.0",
    "zc.lockfile==2.0",
    "zipp==0.6.0",
    "sendgrid==6.1.1"
]

setup(name='docassemble.webapp',
      version='1.1.102',
      python_requires='>=3.5',
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
      package_data={'docassemble.webapp': ['alembic.ini', os.path.join('alembic', '*'), os.path.join('alembic', 'versions', '*'), os.path.join('data', '*.*'), os.path.join('data', 'static', '*.*'), os.path.join('data', 'static', 'favicon', '*.*'), os.path.join('data', 'questions', '*.*'), os.path.join('templates', 'base_templates', '*.html'), os.path.join('templates', 'flask_user', '*.html'), os.path.join('templates', 'flask_user', 'emails', '*.*'), os.path.join('templates', 'pages', '*.html'), os.path.join('templates', 'pages', '*.xml'), os.path.join('templates', 'users', '*.html'), os.path.join('static', 'app', '*.*'), os.path.join('static', 'yamlmixed', '*.*'), os.path.join('static', 'sounds', '*.*'), os.path.join('static', 'examples', '*.*'), os.path.join('static', 'fontawesome', 'js', '*.*'), os.path.join('static', 'fontawesome', 'css', '*.*'), os.path.join('static', 'office', '*.*'), os.path.join('static', 'bootstrap-fileinput', 'img', '*'), os.path.join('static', 'img', '*'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'locales', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'plugins', '*'), os.path.join('static', 'bootstrap-slider', 'dist', '*.js'), os.path.join('static', 'bootstrap-slider', 'dist', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fa', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*.js'), os.path.join('static', 'bootstrap-combobox', 'css', '*.css'), os.path.join('static', 'bootstrap-combobox', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', '*.md'), os.path.join('static', 'bootstrap', 'js', '*.*'), os.path.join('static', 'bootstrap', 'css', '*.*'), os.path.join('static', 'labelauty', 'source', '*.*'), os.path.join('static', 'codemirror', 'lib', '*.*'), os.path.join('static', 'codemirror', 'addon', 'search', '*.*'), os.path.join('static', 'codemirror', 'addon', 'display', '*.*'), os.path.join('static', 'codemirror', 'addon', 'scroll', '*.*'), os.path.join('static', 'codemirror', 'addon', 'dialog', '*.*'), os.path.join('static', 'codemirror', 'addon', 'edit', '*.*'), os.path.join('static', 'codemirror', 'addon', 'hint', '*.*'), os.path.join('static', 'codemirror', 'mode', 'yaml', '*.*'), os.path.join('static', 'codemirror', 'mode', 'markdown', '*.*'), os.path.join('static', 'codemirror', 'mode', 'javascript', '*.*'), os.path.join('static', 'codemirror', 'mode', 'css', '*.*'), os.path.join('static', 'codemirror', 'mode', 'python', '*.*'), os.path.join('static', 'codemirror', 'mode', 'htmlmixed', '*.*'), os.path.join('static', 'codemirror', 'mode', 'xml', '*.*'), os.path.join('static', 'codemirror', 'keymap', '*.*'), os.path.join('static', 'areyousure', '*.js'), os.path.join('static', 'popper', '*.*'), os.path.join('static', 'popper', 'umd', '*.*'), os.path.join('static', 'popper', 'esm', '*.*')]},
     )
