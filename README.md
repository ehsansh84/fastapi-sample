To run unit tests:
```commandline
pytest -s tests/sensor.py  -W ignore::DeprecationWarning
```
Test coverage
```commandline
pytest --cov=main tests/sensor.py
```