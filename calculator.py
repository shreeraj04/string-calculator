class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if numbers.startswith("//"):
            delimiter, numbers = self._extract_custom_delimiter(numbers)
            numbers = numbers.replace(delimiter, ",")

        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        
        # Convert string to list to check negative number
        num_list_int = [int(num) for num in num_list if num]
        self._check_for_negatives(num_list_int)

        return sum(num_list_int)
    
    def _extract_custom_delimiter(self, numbers: str) -> tuple:
        delimiter_part, numbers = numbers.split("\n", 1)
        delimiter = delimiter_part[2:]
        return delimiter, numbers
    
    def _check_for_negatives(self, num_list: list):
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
