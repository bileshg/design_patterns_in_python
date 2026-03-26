from abc import ABC, abstractmethod
from typing import List


class SortingAlgorithm(ABC):
    """Interface for sorting algorithms"""

    @abstractmethod
    def sort(self, nums: List[int]) -> List[int]:
        """Sorts the List"""
        raise NotImplementedError


class BubbleSort(SortingAlgorithm):
    """Bubble sort algorithm"""

    def sort(self, nums: List[int]) -> List[int]:
        # Bubble sort logic
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


class QuickSort(SortingAlgorithm):
    """Quick sort algorithm"""

    def _partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def _quicksort(self, nums: List[int], low: int, high: int) -> List[int]:
        if low < high:
            pi = self._partition(nums, low, high)
            self._quicksort(nums, low, pi - 1)
            self._quicksort(nums, pi + 1, high)
        return nums

    def sort(self, nums: List[int]) -> List[int]:
        # Quick sort logic
        return self._quicksort(nums, 0, len(nums) - 1)


def sort_numbers(sorting_algorithm: SortingAlgorithm, nums: List[int]):
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
