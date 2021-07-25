# Parent image
FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy the dependencies into the image separately to take advantage of docker caching
# Need /app/app so relative imports in main.py work. Webserver will run app.main.
COPY ./requirements.txt ./app/

# Install the needed packages
RUN pip install -r ./app/requirements.txt

# Copy the remaining app files into the image
COPY . /app/

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]
