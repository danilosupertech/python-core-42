#!/usr/bin/env python3
"""Polymorphic Streams - Advanced data streaming system with polymorphism."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract base class for polymorphic data streams."""

    def __init__(self, stream_id: str) -> None:
        """Initialize stream with unique identifier."""
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if self._matches_criteria(item, criteria)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }

    @abstractmethod
    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if item matches filtering criteria."""
  


class SensorStream(DataStream):
    """Specialized stream for sensor data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize sensor stream."""
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.reading_sum = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor batch with aggregation."""
        if not data_batch:
            return "No sensor data to process"
        self.processed_count += len(data_batch)
        temps = [float(str(item).split(":")[1]) for item in data_batch
                 if "temp" in str(item).lower()]
        avg_temp = sum(temps) / len(temps) if temps else 0
        return f"{len(data_batch)} readings processed, avg temp: {avg_temp:.1f}°C"

    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if sensor reading matches criteria."""
        item_str = str(item).lower()
        if criteria == "critical":
            if "temp" in item_str:
                try:
                    temp = float(item_str.split(":")[1])
                    return temp > 30 or temp < 5
                except (ValueError, IndexError):
                    return False
        return True

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor stream statistics."""
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class TransactionStream(DataStream):
    """Specialized stream for financial transactions."""

    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream."""
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction batch with flow analysis."""
        if not data_batch:
            return "No transaction data to process"
        self.processed_count += len(data_batch)
        buys = sells = 0
        buy_total = sell_total = 0
        for item in data_batch:
            item_str = str(item).lower()
            if "buy" in item_str:
                buys += 1
                try:
                    buy_total += int(item_str.split(":")[1])
                except (ValueError, IndexError):
                    pass
            elif "sell" in item_str:
                sells += 1
                try:
                    sell_total += int(item_str.split(":")[1])
                except (ValueError, IndexError):
                    pass
        net = buy_total - sell_total
        self.net_flow = net
        symbol = "+" if net >= 0 else ""
        return f"{len(data_batch)} operations, net flow: {symbol}{net} units"

    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if transaction matches criteria."""
        item_str = str(item).lower()
        if criteria == "large":
            try:
                amount = int(item_str.split(":")[1])
                return amount > 100
            except (ValueError, IndexError):
                return False
        return True

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction stream statistics."""
        stats = super().get_stats()
        stats["type"] = self.stream_type
        stats["net_flow"] = self.net_flow
        return stats


class EventStream(DataStream):
    """Specialized stream for system events."""

    def __init__(self, stream_id: str) -> None:
        """Initialize event stream."""
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event batch with error detection."""
        if not data_batch:
            return "No event data to process"
        self.processed_count += len(data_batch)
        errors = sum(1 for item in data_batch if "error" in str(item).lower())
        self.error_count = errors
        return f"{len(data_batch)} events, {errors} error detected"

    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if event matches criteria."""
        item_str = str(item).lower()
        if criteria == "error":
            return "error" in item_str
        return True

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics."""
        stats = super().get_stats()
        stats["type"] = self.stream_type
        stats["error_count"] = self.error_count
        return stats


class StreamProcessor:
    """Orchestrates processing of multiple stream types polymorphically."""

    def __init__(self) -> None:
        """Initialize stream processor."""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream to the processor."""
        self.streams.append(stream)

    def process_all_streams(self, batches: Dict[int, List[Any]]) -> List[str]:
        """Process all streams through polymorphic interface."""
        results = []
        for idx, stream in enumerate(self.streams):
            if idx in batches:
                result = stream.process_batch(batches[idx])
                results.append(result)
        return results

    def filter_all_streams(
        self,
        batches: Dict[int, List[Any]],
        criteria: str
    ) -> List[List[Any]]:
        """Filter all streams with same criteria."""
        filtered = []
        for idx, stream in enumerate(self.streams):
            if idx in batches:
                result = stream.filter_data(batches[idx], criteria)
                filtered.append(result)
        return filtered


def demonstrate_polymorphic_streams() -> None:
    """Demonstrate polymorphic stream processing system."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_data}")
    result = sensor.process_batch(sensor_data)
    print(f"Sensor analysis: {result}")

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")
    trans_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_data}")
    result = transaction.process_batch(trans_data)
    print(f"Transaction analysis: {result}")

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    result = event.process_batch(event_data)
    print(f"Event analysis: {result}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches: Dict[int, List[Any]] = {
        0: ["temp:20.5", "humidity:70"],
        1: ["buy:50", "sell:75", "buy:100", "sell:60"],
        2: ["start", "process", "error"]
    }

    results = processor.process_all_streams(batches)
    print("Batch 1 Results:")
    print(f"- Sensor data: {results[0]}")
    print(f"- Transaction data: {results[1]}")
    print(f"- Event data: {results[2]}")

    print("\nStream filtering active: High-priority data only")
    sensor_filtered = sensor.filter_data(sensor_data, "critical")
    trans_filtered = transaction.filter_data(trans_data, "large")
    event_filtered = event.filter_data(event_data, "error")
    print(f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
          f"{len(trans_filtered)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    demonstrate_polymorphic_streams()
