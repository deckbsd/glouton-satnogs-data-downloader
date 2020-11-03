FROM python:3.7-alpine

RUN addgroup -S glouton && adduser -D -H -S glouton -G glouton

WORKDIR /glouton

# Bundle app source
COPY . .

# Install glouton module
RUN python3 setup.py install

RUN chown -R glouton:glouton /glouton

USER glouton

CMD "/bin/sh"
