# ICC-Rankings

# Python / Selenium

A Simple Python Code with Selenium, Web Scraping ICC team Rankings.


![Test Demo](preview.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium and Tabulate (optional).

```bash
pip3 install selenium
pip3 install tabulate
```

You need Webdriver installed : [Download Here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

```bash
# Make sure to Have Webdriver extracted at a specific path and add the path
PATH = "PATH_OF_THE_DRIVER_FILE"
driver = webdriver.Chrome(PATH)
```

## Usage

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from tabulate import tabulate
import time
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
