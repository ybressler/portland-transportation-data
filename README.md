# Portland Transportation Data
Mess around with some open data from the city of Portland.


---

# Getting Started
Here's how you install stuff.

### 1. Prerequisites
1. Poetry is installed
   * Check by running:
       ```shell
       poetry --version
       ```
   * Try upgrading:
       ```shell
       poetry self update
       ```
   * If it's not working, install poetry:
       ```shell
       pipx install poetry

       # Now upgrade poetry
       poetry self update
       ```
2. Python 3.11 is being used:
   * Check if `pyenv` is installed
      ```shell
      pyenv --version
      ```
   * If it's not installed, install it:
      ```shell
      brew install pyenv
      ```
   * Install python 3.11 with pyenv:
      ```shell
      pyenv install 3.11
      ```
   * This project is set to use python3.11, as configured in `.python-version`
     But if you wanted to set it anyways, you could run the following (
     from the project's directory):
      ```shell
      pyenv local 3.11
      ```

### 2. Install dependencies
Now you're ready to install stuff:
```shell
make setup
```

### 3. Install pre-commit:
```shell
pre-commit install
```

### 4. Run some tests:
```shell
poetry run pytest
```

### 5. TaDa! 🎉
Congratulations! You're all done!


---
