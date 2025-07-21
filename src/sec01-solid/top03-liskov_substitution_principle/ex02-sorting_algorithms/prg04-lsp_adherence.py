from abc import ABC, abstractmethod
from typing import Optional
from collections.abc import Sequence


class SortingAlgorithm(ABC):
    """Interface for sorting algorithms"""
    @abstractmethod
    def sort(self, nums: Sequence[int | float]) -> Sequence[int | float]:
        """Sorts the sequence"""
        pass


class BubbleSort(SortingAlgorithm):
    """Bubble sort algorithm"""
    def sort(self, nums: Sequence[int | float]) -> Optional[Sequence[int | float]]:
        # Bubble sort logic
        pass


class QuickSort(SortingAlgorithm):
    """Quick sort algorithm"""
    def sort(self, nums: Sequence[int | float]) -> Optional[Sequence[int | float]]:
        # Quick sort logic
        pass



def sort_numbers(sorting_algorithm: SortingAlgorithm, nums: Sequence[int | float]):
    """Returns the sorted numbers by the given SortingAlgorithm"""
    sorting_algorithm.sort(nums)
    return nums


def driver():
    numbers = [5, 3, 8, 1, 2, 7, 4, 6]

    # Sort using Bubble Sort
    sorted_numbers = sort_numbers(BubbleSort(), numbers.copy())
    print("Sorted using Bubble Sort:", sorted_numbers)

    # Sort using Quick Sort
    sorted_numbers = sort_numbers(QuickSort(), numbers.copy())
    print("Sorted using Quick Sort:", sorted_numbers)


if __name__ == "__main__":
    driver()
    