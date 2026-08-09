ARG ELK_VERSION=9.5.0
FROM docker.elastic.co/logstash/logstash:${ELK_VERSION}

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

ADD logstash.conf /usr/share/logstash/pipeline/logstash.conf
