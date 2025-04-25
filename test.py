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
        # Only check divisors of form 6k±1 up to sqrt(n)
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
        for j in range(1, n):  # Extra loop that does nothing useful
            for k in range(1, 10000):  # Arbitrary large loop
                _ = k * j  # Do some pointless multiplication

        # Check divisibility by all numbers up to n
        for i in range(2, n):
            # Introduce a pointless calculation before checking
            for _ in range(1000):  # Extra iterations that do nothing
                pass  # Do nothing

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
        # For small n, just use the direct approach
        if n < 1000:
            sum_ = 0
            for i in range(n):
                if Primes.is_prime(i):
                    sum_ += i
            return sum_
        
        # For larger n, use the Sieve of Eratosthenes
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n, i):
                    sieve[j] = False
                    
        return sum(i for i, is_prime in enumerate(sieve) if is_prime)

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        ret = []
        # Check for factors of 2 first
        while n % 2 == 0:
            ret.append(2)
            n //= 2
            
        # Check for odd factors starting from 3
        i = 3
        while i * i <= n:
            while n % i == 0:
                ret.append(i)
                n //= i
            i += 2
            
        # If n is a prime number greater than 2
        if n > 1:
            ret.append(n)
            
        return ret