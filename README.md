# Wordcloud Python Project
This python program can be used to generate a "WordCloud" image from the given `sample_text`

## Tasks
- [x] Application to generate WordCloud
- [x] Creating container image for the app
- [ ] TODO: Upload the file wordcloud.png to GitHub or Cloud Storage
- [ ] TODO: Pass text as input argument to the script

## Executing the Script
### Method 1
- Add the input text in the variable `sample_text`
- Run below command to execute the program,
```
python3 -m pip install -r requirements.txt
python3 show_wordcloud.py 
```

### Method 2
**Docker Container method**
- Use the below commands to `build` and `run` the image locally
```
docker buildx build -f Dockerfile -t gsdockit/wordcloud:localtest .
docker run -d gsdockit/wordcloud:localtest
```
- While running as Docker container, the output file will be saved inside the container. 
- You can use the following command to copy the file from container to host machine
```
docker cp <ContainerID-NAME-or-HASH>:/app/wordcloud.png /host/path/target/location
```

- Get the container ID using the command below
```
$ docker container ls -a
CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS                     PORTS     NAMES
0defc9c86375   gsdockit/wordcloud:localtest   "python3 show_wordcl…"   3 minutes ago   Exited (0) 3 minutes ago             distracted_liskov
```

- Example 1: `docker cp 0defc9c86375:/app/wordcloud.png /home/wordcloud.png`
- Example 2: `docker cp <ContainerID-NAME-or-HASH>:/app/wordcloud.png .`
