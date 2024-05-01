class Solution:
    def intToRoman(self, num):
        # Define mappings of Roman numeral symbols to their integer values
        roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        roman_numeral = ''
        
        # Iterate over the keys in descending order
        for integer in sorted(roman_map.keys(), reverse=True):
            # Subtract the largest possible multiple of the current integer value
            while num >= integer:
                roman_numeral += roman_map[integer]
                num -= integer
        
        return roman_numeral

solution = Solution()
print(solution.intToRoman(3))      # Output: "III"
print(solution.intToRoman(58))     # Output: "LVIII"
print(solution.intToRoman(1994))   # Output: "MCMXCIV"