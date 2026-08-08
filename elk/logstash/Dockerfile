FROM docker.elastic.co/logstash/logstash:9.5.0

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

ADD logstash.conf /usr/share/logstash/pipeline/logstash.conf
