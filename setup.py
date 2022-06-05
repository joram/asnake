#!/usr/bin/env python

from setuptools import find_packages, setup

packages = [
    "uvicorn",
    "gunicorn==20.1.0",
    "fastapi==0.75.0",
    "requests==2.27.1",
    "sentry_sdk==1.5.7",
    "python-environ==0.4.54",
    "environ",
]

test_packages = [
    "mock==4.0.3",
    "pytest==7.0.1",
    "pytest-cov",
    "pytest-asyncio",
    "responses",
    "starlette",
    "mock",
]

linting_packages = [
    "pre-commit==2.9.3",
    "black==22.3.0",
    "flake8==3.8.4",
    "flake8-bugbear==20.1.4",
    "flake8-builtins==1.5.3",
    "flake8-comprehensions==3.2.3",
    "flake8-tidy-imports==4.2.1",
    "flake8-import-order==0.18.1",
]

setup(
    name="Arthur's Sname",
    version="1.0",
    author="Arthur & John Oram",
    author_email="john@oram.ca",
    install_requires=packages,
    packages=find_packages(),
    extras_require={
        "dev": test_packages + linting_packages,
    },
)
