<h1 align="center">Welcome to pydictxls</h1>

## :black_nib: Author

:bust_in_silhouette: **Haniel Zaiine**

* Github: [@hanielzaiine](https://github.com/hanielzaiine)

---

## Install dependencies

```sh
pip install openpyxl
```
Check [openpyxl](https://openpyxl.readthedocs.io/en/stable/) docs for more details. 

## :rocket: Usage

Given a list of objects
```sh
data = [
    {
        'name': 'Person1', 
        'age': 26, 
        'sex': 'Fermale', 
        'city': 'Goiania', 
        'country': 'GO',
        'state': 'Brasil',
        'meta_data': 'Meta'
    }
]
```
Choose wich values you wanna export to file. You can choose by dict key. 
```sh
values = ['name', 'age', 'sex', 'city', 'country', 'state']
```
<em>Note: No need all keys you need declare as ordered list. (How you wanna collums order)</em>

Generate you file
```sh
from pydictxl import gerenerate_data
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

gerenerate_data(data, values, ws, 1)
```
Where
```sh
:param data: list of objects (dicts)
:param values: list of keys
:param ws: file (worksheet)
:param 1: int, represent which line data will start.
```
---

## :handshake: Contributing

Contributions, issues and feature requests are welcome!<br />

---
## ✨ Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © current [Haniel Zaiine Côrtes - @hanielzaiine](https://github.com/hanielzaiine).

This project is [MIT](https://github.com/hanielzaiine/pydictxl/blob/main/LICENSE) licensed.