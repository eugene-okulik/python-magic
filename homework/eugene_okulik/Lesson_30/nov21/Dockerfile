FROM python
RUN git clone https://github.com/eugene-okulik/cool_web_app.git
ENV COOL_PORT 8080
ENV COOL_IP 0.0.0.0
RUN mkdir logs
ENV COOL_LOG logs
RUN mkdir /usr/share/cool-app
RUN echo "This is a page from docker made by python-magic group" > /usr/share/cool-app/cool-text.txt
EXPOSE 8080/tcp
CMD ["python", "cool_web_app/run.py"]

