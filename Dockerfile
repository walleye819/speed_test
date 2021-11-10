FROM balenalib/raspberry-pi-debian-python:3.7.4

  # Create and set working directory
  RUN mkdir -p /code
  WORKDIR /code

  # Copy and install dependencies
  COPY Pipfile* /code/
  RUN pip install --upgrade pip
  RUN pip install pipenv
  RUN pipenv lock --keep-outdated --requirements > requirements.txt
  RUN pip install -r requirements.txt

  # Copy app source code
  COPY . /code/

  CMD ["python3", "/code/run.py"]
