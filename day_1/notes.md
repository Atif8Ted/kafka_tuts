- Books : Designing events-driven systems : concepts and patterns for streaming sevices with Apache Kafka - Ben StopFord
- Loosely coupled components should be target
- components should be plug and play.


---
# Flow of Data:
producer ---> kafka ---> consumers
- messages are stored in kafka for a configurable amount of time ( default:2 week)
- messages are immutable once they land in kafka.
- 