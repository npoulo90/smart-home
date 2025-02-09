# Use an official Java runtime as a parent image
FROM openjdk:8-jdk-slim

# Set environment variables
ENV SPARK_VERSION=3.1.2
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Install Spark
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz | tar xz -C /opt && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION $SPARK_HOME && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose ports
EXPOSE 8080 7077 4040

# Start Spark master
CMD ["sh", "-c", "$SPARK_HOME/sbin/start-master.sh && tail -f $SPARK_HOME/logs/*"]
