FROM python:3.9

WORKDIR /code

RUN apt update
RUN apt install -y portaudio19-dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 9000

ENTRYPOINT export PATH="/bin:$PATH" &&\
    sh /code/app/entrypoint.sh
