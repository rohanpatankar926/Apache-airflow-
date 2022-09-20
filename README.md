# Apache-airflow-
1.Download docker application using `sudo apt-get install docker`
2.Now type `sudo docker build -t avnish327030/spark-hadoop-airflow`
3.`sudo docker tag avnish327030/spark-hadoop-airflow spark-hadoop-airflow`
4.PROJECT_DIR=$(pwd)
5.`docker run -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 8888:8888 \
    -p 9864:9864 \
    -p 8085:8085 \
    -p 8793:8793 \
    -p 8081:8081 \
    -v $PROJECT_DIR/notebook:/root/ipynb \
    -v $PROJECT_DIR/airflow:/home/airflow \
    -v $PROJECT_DIR/data:/data \
    spark-hadoop-airflow`
6.`http://localhost:8085/` run this into local browser and start building data pipelines using airflow :)
7.<a href="http://localhost:8085/">Namenode</a>  <a href="http://localhost:9864/">DataNode</a>  <a href="http://localhost:8088/">Hadoop cluster</a> <a href="http://localhost:8080/">Spark Master</a>  <a href="http://localhost:8888/">Jupyter Lab</a>
8.Thats it using airflow you can build entire data pipeline,retraining approach,etl pipelines and lots more.
9.Multiple operators are available such as PythonOperators,BashOperator,EmailOperator,PostgresOperator and much more.
