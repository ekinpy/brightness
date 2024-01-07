![Logo](https://raw.githubusercontent.com/ekinpy/brightness/main/brightness.png)

The effortless solution for managing screen brightness in Python.\
Linux support coming soon.

## Installing

```sh
pip install brightness
```

to test:

```sh
python -m brightness
```

## set()
```python
def set(value: int | float) -> None
```
Sets the screen brightness to the entered value.

## get()
```python
def get() -> (int | None)
```
Returns the screen brightness.

## increase()
```python
def increase(value: int) -> None
```
Increases the screen brightness by the entered value.

## decrease()
```python
def decrease(value: int) -> None
```
Decreases the screen brightness by the entered value.