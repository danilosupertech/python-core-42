#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stream_processor.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/04 00:00:00 by danicort          #+#    #+#              #
#    Updated: 2026/02/04 00:00:00 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Data Processor Foundation - Abstract polymorphic data processing system."""

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class for polymorphic data processing."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Specialized processor for numeric data."""

    def validate(self, data: Any) -> bool:
        """Validate if data is numeric."""
        try:
            if isinstance(data, (list, tuple)):
                return all(isinstance(x, (int, float)) for x in data)
            return isinstance(data, (int, float))
        except (TypeError, ValueError):
            return False

    def process(self, data: Any) -> str:
        """Process numeric data with aggregation."""
        if not self.validate(data):
            raise ValueError("Invalid numeric data provided")
        if isinstance(data, (list, tuple)):
            count = len(data)
            total = sum(data)
            avg = total / count if count > 0 else 0
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        return f"Processed single value: {data}"

    def format_output(self, result: str) -> str:
        """Format numeric output."""
        return result


class TextProcessor(DataProcessor):
    """Specialized processor for text data."""

    def validate(self, data: Any) -> bool:
        """Validate if data is text."""
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """Process text data with analysis."""
        if not self.validate(data):
            raise ValueError("Invalid text data provided")
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def format_output(self, result: str) -> str:
        """Format text output."""
        return result


class LogProcessor(DataProcessor):
    """Specialized processor for log entries."""

    def validate(self, data: Any) -> bool:
        """Validate if data is a log entry."""
        if not isinstance(data, str):
            return False
        valid_levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
        return any(level in data for level in valid_levels)

    def process(self, data: Any) -> str:
        """Process log entry with level detection."""
        if not self.validate(data):
            raise ValueError("Invalid log entry format")
        levels = ["CRITICAL", "ERROR", "WARNING", "DEBUG", "INFO"]
        level = "INFO"
        for lv in levels:
            if lv in data:
                level = lv
                break
        alert_level = "ALERT" if level in ["CRITICAL", "ERROR"] else "INFO"
        message = data.split(": ", 1)[1] if ": " in data else data
        return f"[{alert_level}] {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        """Format log output."""
        return result


def demonstrate_polymorphism() -> None:
    """Demonstrate polymorphic data processing."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_proc = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print(f"Validation: Numeric data verified")
    result = numeric_proc.process(numeric_data)
    print(f"Output: {result}")

    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print("Validation: Text data verified")
    result = text_proc.process(text_data)
    print(f"Output: {result}")

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print("Validation: Log entry verified")
    result = log_proc.process(log_data)
    print(f"Output: {result}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [numeric_proc, text_proc, log_proc]
    test_data: List[Any] = [
        [1, 2, 3],
        "System ready",
        "INFO: System ready"
    ]

    for idx, (proc, data) in enumerate(zip(processors, test_data), 1):
        try:
            result = proc.process(data)
            print(f"Result {idx}: {result}")
        except ValueError as e:
            print(f"Result {idx}: ERROR - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    demonstrate_polymorphism()
