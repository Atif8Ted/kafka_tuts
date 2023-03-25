- Books : Designing events-driven systems : concepts and patterns for streaming sevices with Apache Kafka - Ben StopFord
- Loosely coupled components should be target
- components should be plug and play.


---
# Flow of Data:
producer ---> kafka ---> consumers
- messages are stored in kafka for a configurable amount of time ( default:2 week)
- messages are immutable once they land in kafka.

# What is a Kafka 'Topic'?
Kafka uses topics to organize messages,
similar to how a database uses tables for the same purpose.
Topics are identified by a unique name,
and messages are sent to and read from specific topics.
Whenever we want to store data in Kafka,
we need to specify to which 'topic' such data should be stored.

A 'topic' is basically the destination that will hold all the data.
If you are familiar with a message queue, think of the topic like the queue name.
If you are new to all of this, just think of the topic as a box where the messages are stored.