- consumer are the kafka components that consume messages from kafka topic
- internally consumer consume messages from kafka topic partition
- ![img.png](img.png)
- Every consumer is always assigned to a consumer group
  - ![img_1.png](img_1.png)
- if no group_id is provided then random group id is assigned
- configuration needed by consumer
  - ![img_2.png](img_2.png)

### consumer Group
- logical grouping of one or more consumer
![img_3.png](img_3.png)
here c1 is the consumer
-![img_4.png](img_4.png)