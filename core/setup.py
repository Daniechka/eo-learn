import os
from setuptools import setup, find_packages


def parse_requirements(file):
    return sorted(set(
        line.partition('#')[0].strip()
        for line in open(os.path.join(os.path.dirname(__file__), file))
    ) - set(''))


def get_version():
    for line in open(os.path.join(os.path.dirname(__file__), 'eolearn', 'core', '__init__.py')):
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"').strip("'")
    return version


setup(name='eo-learn-core',
      version=get_version(),
      description='Core Machine Learning Framework at Sinergise',
      url='https://github.com/sentinel-hub/eo-learn',
      author='Sinergise EO research team',
      author_email='info@sinergise.com',
      license='MIT',
      packages=find_packages(),
      package_data={'eolearn': ['core/report_templates/report.html']},
      include_package_data=True,
      install_requires=parse_requirements("requirements.txt"),
      zip_safe=False)
