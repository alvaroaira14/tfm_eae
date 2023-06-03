import os
import shutil
import urllib.request

url = "https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz"
spark_zip_file = "../spark.tgz"

print("Downloading file...")
urllib.request.urlretrieve(url, spark_zip_file)
print("File downloaded successfully!")

spark_install_dir = "../"

shutil.unpack_archive(spark_zip_file, spark_install_dir)
print("Spark extracted successfully!")

spark_install_dir = "../spark-3.4.0-bin-hadoop3"
os.environ["SPARK_HOME"] = os.path.abspath(spark_install_dir)
os.environ["PATH"] += os.pathsep + os.path.join(os.environ["SPARK_HOME"], 'bin')
print("Spark setup completed")