class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if numbers.startswith("//"):
            delimiter, numbers = self._extract_custom_delimiter(numbers)
            numbers = numbers.replace(delimiter, ",")
        
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        
        return self._sum_numbers(num_list)
    
    def _extract_custom_delimiter(self, numbers: str) -> tuple:
        delimiter_part, numbers = numbers.split("\n", 1)
        delimiter = delimiter_part[2:]  # Extract delimiter after "//"
        return delimiter, numbers
    
    def _sum_numbers(self, num_list):
        return sum(int(num) for num in num_list if num)
