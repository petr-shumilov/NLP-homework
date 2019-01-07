# NLP-homework
## Start
```bash
docker build -t nlp .
docker run --name nlp -v $(pwd)/lemmatization:/app/lemmatization:rw --rm --entrypoint /bin/bash -it nlp
```
