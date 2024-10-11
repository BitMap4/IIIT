# Tokeniser assignment

## Pre-requisites

- Python

## How to run

Run the following command in the same directory as the `run.sh` file:

```bash
./run.sh
```

This will update the output files in their respective folders if they exist already. If the output files do not exist, then they will be created.

Otherwise, each task can also be run individually. Make sure to stay in the same directory as the `tokeniser.py` and `run.sh` files.

```bash
python3 Task_<i>/code.py
```

## Assumptions

- If a "?" or a "." is encountered inside a quote, the line is split there into different sentences. For example- `He said "I am good. How are you?"` will be split into two sentences- `He said "I am good.` and `How are you?"`