# com.udacity.cf

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

processedRowsPerSecond is the most important one which I try to tuning. 

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Pls checck the below info:
1. spark.sql.shuffle.partitions: 5
2. spark.streaming.kafka.maxRatePerPartition: 20
3. spark.default.parallelism: 100
