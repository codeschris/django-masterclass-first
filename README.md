# django-masterclass-first

This is a masterclass repo where different developers work on a blog system with simple CRUD so they can learn the basics of Django.

## Setup

1. Clone the repository
2. Create a virtual environment

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - On Windows:

     ```bash
     source venv/Scripts/activate
     ```

   - on macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

5. Every time you update the dependencies/packages, run the command below to have the latest list of packages available for other developers. (Note: Ensure you're in a virtual environment)

   ```bash
   pip freeze > requirements.txt
   ```

## Contributions

After cloning, create your own branch with the conventional branch name `<gh-username>-develop`, e.g. `codeschris-develop`. Make your changes from the new branch and create a PR when submitting your changes to avoid conflicts.
