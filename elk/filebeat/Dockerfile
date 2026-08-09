ARG ELK_VERSION=9.5.0
FROM docker.elastic.co/beats/filebeat:${ELK_VERSION}

COPY filebeat.yml /usr/share/filebeat/filebeat.yml

USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml

USER filebeat
