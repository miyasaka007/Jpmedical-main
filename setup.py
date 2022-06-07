import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trash",
    version="0.0.2",
    author="naoto miyasaka",
    author_email="s2022064@stu.musashino-u.ac.jp",
    description='A package for visualization of total of amount of gavage, if people all over the world are Japnanese"',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plumchloride/kotonohatango-getter",
    project_urls={
        "Bug Tracker": "https://github.com/plumchloride/kotonohatango-getter",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['jptrash'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'kotonohagetter = kotonohagetter:main'
        ]
    },
)
