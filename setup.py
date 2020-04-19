from setuptools import setup, find_packages

setup(
    name='robotframework-testcase-generator',
    version='1.0.0',
    description='auto generate test case of RF with excel',
    license='MIT License',
    install_requires=["xlrd"],
    packages=['scripts'],
    include_package_data=True,
    author='Patrick Peng',
    author_email='pengjiahao97@gmail.com',
    url='https://github.com/pengjiahao97/robotframework-testcase-generator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
