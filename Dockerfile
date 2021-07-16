FROM python:3.8.2


COPY logger_mount.py logger_mount.py
RUN mkdir app_logs

CMD ["python","logger_mount.py"]