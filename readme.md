clone the repo. change directory to python-logs-docker and run the dockerfile

```docker build -t test .
docker run -v $PWD/myLogs:/app_logs test```

will create a fresh directory myLogs in the present working directory and write the logs there.