import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if numbers.startswith("//"):
            delimiters, numbers = self._extract_custom_delimiter(numbers)
            for delimiter in delimiters:
                numbers = re.sub(re.escape(delimiter), ",", numbers) #replace all delimters with comma
        
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        
        # Convert string to list to check negative number
        num_list_int = [int(num) for num in num_list if num]
        num_list_int = [num for num in num_list_int if num <= 1000]
        self._check_for_negatives(num_list_int)

        return sum(num_list_int)
    
    def _extract_custom_delimiter(self, numbers: str) -> tuple:
        delimiter_part, numbers = numbers.split("\n", 1)
        delimiter_part = delimiter_part[2:]  # Remove the "//" part
        
        # Check if delimiters are enclosed in multiple sets of square brackets
        if delimiter_part.startswith("[") and "]" in delimiter_part:
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        else:
            # Single character delimiter without brackets
            delimiters = [delimiter_part]
        
        return delimiters, numbers
    
    def _check_for_negatives(self, num_list: list):
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

if __name__=="__main__":
    s = StringCalculator()
    s.add("//[*][%]\n1*2%3")