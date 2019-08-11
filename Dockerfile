FROM python:3
WORKDIR /glouton

# Bundle app source
COPY . .

# Install glouton module
RUN python3 setup.py install

CMD "/bin/bash"
