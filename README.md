# Sellix Python SDK 

![tag](https://img.shields.io/github/v/tag/sellix/python-sdk?sort=date&color=blueviolet)

## Introduction

Sellix public API for developers to access merchant resources

## Requirements

- python ^3.7

## Installation

Install the package through composer.

```
python3 -m pip install sellix-python-sdk
```

## Usage

```python
from sellix import Sellix

# pass <MERCHANT_NAME> only if you need to be authenticated as an additional store

client = Sellix("<YOUR_API_KEY>", "<MERCHANT_NAME>")

try:
    products = client.get_products()
except Sellix.SellixException as e:
    print(e)

```

## Documentation

[Sellix Developers API](https://developers.sellix.io)