### Hexlet tests and linter status:
[![Actions Status](https://github.com/Albert-back-end/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Albert-back-end/python-project-49/actions)

Запись работы игры brain-even в asciinema
https://asciinema.org/a/m0dAR3InBXEFt52InkisR3Rga

Запись работы игры калькулятор в asciinema
https://asciinema.org/a/eT8qaYH630tJXVM4CwMJVTUSX

Запись работы игры НОД в asciinema
https://asciinema.org/a/legH02LehyD8SosVPeSfF2BI9

Запись игры арифмитическая прогрессия в asciinema
https://asciinema.org/a/Sy3hQt9IHuipNvxKi8gDeWrAW

Запись игры простое число в asciinema
https://asciinema.org/a/MJLOmwv8MKSwcDlaZaP87rxNo

# Brain Games
___

The training project "Brain Games" on the Python Development course on [Hexlet.io](https://ru.hexlet.io/programs/python).

[![Actions Status](https://github.com/IgorGakhov/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/IgorGakhov/python-project-lvl1/actions) [![Pylinter-on-push](https://github.com/IgorGakhov/python-project-lvl1/actions/workflows/pylinter-on-push.yml/badge.svg)](https://github.com/IgorGakhov/python-project-lvl1/actions/workflows/pylinter-on-push.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/84b4a56a97af7dbc636a/maintainability)](https://codeclimate.com/github/IgorGakhov/python-project-lvl1/maintainability)

### Built With
Languages, frameworks and libraries used in the implementation of the project:

[![](https://img.shields.io/badge/language-python-blue)](https://github.com/topics/python) [![](https://img.shields.io/badge/library-prompt-%23EE7D0D)](https://github.com/topics/prompt) [![](https://img.shields.io/badge/library-random-black)](https://github.com/topics/random) [![](https://img.shields.io/badge/library-math-success)](https://github.com/topics/math)

### Dependencies
List of dependencies, without which the project code will not work correctly:

- python = "^3.9"
- prompt = "^0.4.1"

## Description

**"Brain Games"** is a set of five console games based on the popular mobile brain-pumping apps. Each game asks questions that need to be answered correctly. After three correct answers, the game is considered to be completed. Wrong answers end the game and offer to play it again. Games:

**Games:**
- [X] Brain Even  - Answer "yes" if the number is even, otherwise answer "no"
- [X] Brain Calculator - Answer what is the result of the expression?
- [X] Brain GCD - Answer what is the greatest common divisor of given numbers.
- [X] Brain Progression - Answer what number is missing in the progression?
- [X] Brain Prime - Answer "yes" if given number is prime, otherwise answer "no".

You can call them with simple commands:
```bash
>> brain-even
>> brain-calc
>> brain-gcd
>> brain-progression
>> brain-prime
```

The first project is simultaneously the first full-fledged program outside of the Hexlet Environment. It introduces the basic steps needed to start any new project: installing the language (interpreter), setting up the environment (operating system, editor, linters), connecting additional libraries, creating a git repository. At this stage begins the in-depth work with the terminal. You will be introduced to Poetry, the utility for project management: installing and upgrading additional libraries, publishing packages, and much more. Here also comes the formation of the right engineering culture. One of the first tasks in the setup is to connect a linter (flake8), which automatically monitors the code style and finds potential errors. Another powerful element of real-world development is continuous integration (CI). Such systems are an integral part of any professional development. In Hexlet projects, continuous integration is connected to every project. Among the many systems, Github Actions is chosen as a free and Github-integrated build system.

The main issue in the project is the architecture. The architecture relies on basic principles of code organization: isolating side-effects, creating the right abstraction barriers (high modularity). A lot of questions arise here: "who is responsible for what?", "who interacts with the user?" "how does the game run?" and more. The architecture is a lot of work to do, even if you have some real development experience.

### Summary
* [Description](#description)
* [Installation](#installation)
  * [Python](#python)
  * [Poetry](#poetry)
  * [Project package](#project-package)
* [Usage](#usage)
  * [Demo](#demo)
  * [Brain Even](#video_game-brain-even)
  * [Brain Calculator](#video_game-brain-calc)
  * [Brain GCD](#video_game-brain-gcd)
  * [Brain Progression](#video_game-brain-progression)
  * [Brain Prime](#video_game-brain-prime)
* [Development](#development)
  * [Dev Dependencies](#dev-dependencies)
  * [Project Organization](#project-organization)
  * [Useful commands](#useful-commands)

___

## Installation

### Python
Before installing the package, you need to make sure that you have Python version 3.9 or higher installed:

```bash
# Windows, Ubuntu, MacOS:
>> python --version # or python -V
Python 3.9.0+
```
:warning: If a command without a version does not work, specify the Python version explicitly: ```python3 --version```.

If you have an older version installed, update with the following commands:

```bash
# Windows:
>> pip install python --upgrade
# Ubuntu:
>> sudo apt-get upgrade python3.X
# MacOS:
>> brew update && brew upgrade python
# * X - version number to be installed
```

If you don't have Python installed, you can download and install it from [the official Python website](https://www.python.org/downloads/). If you are an Ubuntu or MacOS user, then it is better to do this procedure through package managers. Open a terminal and run the command for your operating system:

```bash
# Ubuntu:
>> sudo apt update
>> sudo apt install python3.X
# MacOS:
# https://brew.sh/index_ru.html
>> brew install python3.X
# * X - version number to be installed
```

:exclamation: The configuration of assemblies of different versions of operating systems can vary greatly from each other, which makes it impossible to write a common instruction. If you're running an OS other than the above, or you're having errors after the suggested commands, search [Stack Overflow](https://stackoverflow.com/) for answers, maybe someone else has come across them before you! Setting up the environment is not easy! :slightly_smiling_face:

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more about this tool on [the official Poetry website](https://python-poetry.org/).

Poetry provides a custom installer that will install poetry isolated from the rest of your system by vendorizing its dependencies. This is the recommended way of installing poetry.

```bash
# Windows (WSL), Linux, MacOS:
>> curl -sSL https://install.python-poetry.org | python3 -
# Windows (Powershell):
>> (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
# If you have installed Python through the Microsoft Store, replace "py" with "python" in the command above.
```

:warning: On some systems, ```python``` may still refer to Python 2 instead of Python 3. The Poetry Team suggests a ```python3``` binary to avoid ambiguity.

:warning: By default, Poetry is installed into a platform and user-specific directory:

* ```~/Library/Application Support/pypoetry``` on *MacOS*.
* ```~/.local/share/pypoetry``` on *Linux/Unix*.
* ```%APPDATA%\pypoetry``` on *Windows*.

If you wish to change this, you may define the $POETRY_HOME environment variable:

```bash
>> curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
```

Add Poetry to your PATH.

Once Poetry is installed and in your $PATH, you can execute the following:

```bash
>> poetry --version
```

### Project package

To work with the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/IgorGakhov/python-project-lvl1.git
# clone via SSH:
>> git clone git@github.com:IgorGakhov/python-project-lvl1.git
```

It remains to move to the directory and install the package:

```bash
>> cd python-project-lvl1
>> poetry build
>> python3 -m pip install --user dist/*.whl
# If you have previously installed a package and want to update it, use the following command:
# >> python3 -m pip install --user --force-reinstall dist/*.whl
```

On *nix-like systems you can do this:

[![asciicast](https://asciinema.org/a/ANkzjhabSyRmyhKx8hcOwByDT.svg)](https://asciinema.org/a/ANkzjhabSyRmyhKx8hcOwByDT)

Finally, we can move on to using the project functionality!

___

## Usage

### Demo

#### :video_game: Brain Even:
`brain-even`

The user is shown a random number. And he has to answer yes if the number is even, or no if it is odd:

**Examples:**
```bash
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
>> Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.

Answer "yes" if the number is even, otherwise answer "no".
Question: 15
>> Your answer: no
Correct!
```

[![asciicast](https://asciinema.org/a/m0dAR3InBXEFt52InkisR3Rga.svg)](https://asciinema.org/a/m0dAR3InBXEFt52InkisR3Rga)

#### :video_game: Brain Calculator:
`brain-calc`

The user is shown a random mathematical expression, such as 87 + 48, which must be calculated and write down the correct answer.

**Examples:**
```bash
What is the result of the expression?
Question: 87 + 48
>> Your answer: 126
'126' is wrong answer ;(. Correct answer was '135'.

What is the result of the expression?
Question: 87 + 48
>> Your answer: 135
Correct!
```

[![asciicast](https://asciinema.org/a/eT8qaYH630tJXVM4CwMJVTUSX.svg)](https://asciinema.org/a/eT8qaYH630tJXVM4CwMJVTUSX)

#### :video_game: Brain GCD:
`brain-gcd`

The user is shown two random numbers, for example 25 and 50. The user must calculate and enter the greatest common divisor of these numbers.

**Examples:**
```bash
Find the greatest common divisor of given numbers.
Question: 25 50
>> Your answer: 5
'5' is wrong answer ;(. Correct answer was '25'.

Find the greatest common divisor of given numbers.
Question: 25 50
>> Your answer: 25
Correct!
```

[![asciicast](https://asciinema.org/a/oeA9mMA7gCGNoWR2nfMfruiGQ.svg)](https://asciinema.org/a/oeA9mMA7gCGNoWR2nfMfruiGQ)

#### :video_game: Brain Progression:
`brain-progression`

The user is shown a series of numbers with a missing number, forming an arithmetic progression. The player has to determine this number.

**Examples:**
```bash
What number is missing in the progression?
Question: 3 26 .. 72 95 118 141 164 187
>> Your answer: 43
'43' is wrong answer ;(. Correct answer was '49'.

What number is missing in the progression?
Question: 3 26 .. 72 95 118 141 164 187
>> Your answer: 49
Correct!
```

[![asciicast](https://asciinema.org/a/Sy3hQt9IHuipNvxKi8gDeWrAW.svg)](https://asciinema.org/a/Sy3hQt9IHuipNvxKi8gDeWrAW)

#### :video_game: Brain Prime:
`brain-prime`

The user is shown a random number. And he needs to answer yes if the number is prime, or no if it is composite:

**Examples:**
```bash
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 67
>> Your answer: no
'no' is wrong answer ;(. Correct answer was 'yes'.

Answer "yes" if given number is prime. Otherwise answer "no".
Question: 67
>> Your answer: yes
Correct!
```

[![asciicast](https://asciinema.org/a/MJLOmwv8MKSwcDlaZaP87rxNo.svg)](https://asciinema.org/a/MJLOmwv8MKSwcDlaZaP87rxNo)

___

## Development

### Dev Dependencies

List of dev-dependencies:
- flake8 = "^4.0.1"

### Project Organization

```bash
.
├── Makefile
├── README.md
├── brain_games
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── cli.cpython-312.pyc
│   │   └── engine.cpython-312.pyc
│   ├── cli.py
│   ├── games
│   │   ├── __pycache__
│   │   │   ├── calculator.cpython-312.pyc
│   │   │   ├── even_words.cpython-312.pyc
│   │   │   ├── gsd.cpython-312.pyc
│   │   │   ├── prime.cpython-312.pyc
│   │   │   └── progression.cpython-312.pyc
│   │   ├── calculator.py
│   │   ├── even_words.py
│   │   ├── gsd.py
│   │   ├── prime.py
│   │   └── progression.py
│   └── scripts
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── brain_calc.cpython-312.pyc
│       │   ├── brain_even.cpython-312.pyc
│       │   ├── brain_games.cpython-312.pyc
│       │   ├── brain_gsd.cpython-312.pyc
│       │   ├── brain_prime.cpython-312.pyc
│       │   └── brain_progression.cpython-312.pyc
│       ├── brain_calc.py
│       ├── brain_even.py
│       ├── brain_games.py
│       ├── brain_gsd.py
│       ├── brain_prime.py
│       └── brain_progression.py
├── dist
│   ├── brain_games-0.1.0-py3-none-any.whl
│   └── brain_games-0.1.0.tar.gz
├── poetry.lock
├── pyproject.toml
└── setup.cfg
```

### Useful commands

The commands most used in development are listed in the Makefile:

<dl>
    <dt><code>make package-install</code></dt>
    <dd>Installing a package in the user environment.</dd>
    <dt><code>make build</code></dt>
    <dd>Building the distribution of he Poetry package.</dd>
    <dt><code>make package-force-reinstall</code></dt>
    <dd>Reinstalling the package in the user environment.</dd>
    <dt><code>make lint</code></dt>
    <dd>Checking code with linter.</dd>
</dl>

___

**Thank you for attention!**

:man_technologist: Author: [@Albert-back-end](https://github.com/Albert-back-end)
