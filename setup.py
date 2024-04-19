import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-marketing-urls",
    version="1.0.1",
    author="Laonan",
    author_email="hello@laonan.net",
    description="An app to generate marketing urls for Django projects. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laonan/django-marketing-urls",  # github url
    project_urls={
        "Bug Tracker": "https://github.com/laonan/django-marketing-urls/issues",
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude=("tests", "manage.py", "db.sqlite3")),
    zip_safe=True,
    install_requires=[
        'Django>=2.0.13',
        'urltoken>=1.0.0',
    ],
    python_requires=">=3.6",
)
