FROM continuumio/miniconda3:4.11.0

WORKDIR /app
RUN conda install -c pytorch faiss-gpu
RUN pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
CMD [ "sleep", "3600" ]