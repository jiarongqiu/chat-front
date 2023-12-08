# 
FROM python:3.11

# 
WORKDIR /code/frontend

# 
COPY ./requirements.txt /code/frontend/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/frontend/

# 
CMD ["python"]
