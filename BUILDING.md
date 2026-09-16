# Building and Contributing to the Book

This project uses `ccsf-cpp17` as the shared development branch. The `main`
branch is kept pristine.

## macOS setup

### One-time Python and PreTeXt setup

From the repository root, create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pretext
pretext --version
```

The virtual environment is local to your computer. It should not be committed
to Git.

### Future sessions

Each time you open a new Terminal window, go to the repository and activate the
environment:

```bash
cd ~/thinkcpp
source .venv/bin/activate
```

## Building and viewing the book

Run these commands from the repository root:

```bash
pretext build web
pretext view web
```

The `web` target creates the ordinary web version of the book for local viewing
and web publication. It does not deploy the book automatically.

To save build output to a log file:

```bash
mkdir -p logs
pretext build web 2>&1 | tee logs/build-web.txt
```

When finished, deactivate the virtual environment if desired:

```bash
deactivate
```

## Git workflow

Do not make work commits directly on `ccsf-cpp17`. Create a personal branch
from it:

```bash
git switch ccsf-cpp17
git pull --rebase origin ccsf-cpp17
git switch -c ccsf-cpp17-my-branch
git push -u origin ccsf-cpp17-my-branch
```

Before beginning later work, update the personal branch with the latest shared
branch:

```bash
git switch ccsf-cpp17-my-branch
git fetch origin
git rebase origin/ccsf-cpp17
```

After making and testing changes:

```bash
git status
git diff --check
git add .
git commit -m "Describe the changes"
git push
```

Create a pull request on GitHub using:

```text
Base branch:    ccsf-cpp17
Compare branch: ccsf-cpp17-my-branch
```

After the pull request is merged, update the local shared branch:

```bash
git switch ccsf-cpp17
git pull --rebase origin ccsf-cpp17
```

Then update the personal branch before continuing work:

```bash
git switch ccsf-cpp17-my-branch
git rebase origin/ccsf-cpp17
```

## Windows note

On Windows, activate the virtual environment with:

```cmd
.venv\Scripts\activate
```

Build and view the book with:

```cmd
pretext build web
pretext view web
```

If the repository contains `build-web.bat`, it may be used instead of the
build command.
