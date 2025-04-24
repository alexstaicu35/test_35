from typing import List


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        # Only need to check up to sqrt(n)
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def is_prime_ineff(n: int) -> bool:
        """Check if a number is prime (inefficiently)

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False

        # Introduce unnecessary calculations
        # Removed pointless loops that were only wasting CPU cycles and memory

        # Check divisibility by all numbers up to n
        # Optimized to only check up to the square root of n,
        # which is sufficient for primality testing
        for i in range(2, int(n**0.5) + 1):
            # Removed pointless loop that was doing nothing

            if n % i == 0:
                return False

        return True


@staticmethod
def sum_primes(n: int) -> int:
    """Sum of primes from 0 to n (exclusive)

    Args:
        n (int): Number to sum up to

    Returns:
        int: Sum of primes from 0 to n
    """
    # Use Sieve of Eratosthenes to identify all primes in one go
    if n <= 2:
        return 0
    
    # Initialize sieve array
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Mark non-prime numbers in the sieve
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Calculate sum of all identified primes
    return sum(i for i in range(n) if is_prime[i])

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        ret = []
        
        # Trial division by 2 first (optimization for even numbers)
        while n % 2 == 0:
            ret.append(2)
            n //= 2
        
        # Then only check odd numbers starting from 3
        i = 3
        while i * i <= n:  # Only check up to sqrt(n)
            if n % i == 0:
                ret.append(i)
                n //= i
            else:
                i += 2  # Skip even numbers
                
        # If n > 1, it is the last prime factor
        if n > 1:
            ret.append(n)
            
        return ret