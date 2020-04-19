from setuptools import setup

setup(
    name='rf_case_generator',
    version='1.0.3',
    description='auto generate test case of RF with excel',
    license='MIT License',
    install_requires=["xlrd"],
    packages=['rf_case_generator'],
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
