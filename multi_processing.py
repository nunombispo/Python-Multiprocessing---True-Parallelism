import time
import multiprocessing as mp

def is_prime(n):
    """
    Check if the number n is prime.
    
    Args:
        n (int): The integer to check for primality.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    # Only need to check factors up to the square root of n.
    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    """
    Count prime numbers between start and end (exclusive).
    
    Args:
        start (int): The starting value of the range.
        end (int): The ending value of the range (exclusive).
    
    Returns:
        int: The number of prime numbers in the range.
    """
    count = 0
    for num in range(start, end):
        if is_prime(num):
            count += 1
    return count

def run_multiprocessing(ranges):
    """
    Process ranges in parallel using multiprocessing.
    
    Args:
        ranges (list of tuple): Each tuple contains the start and end of a range.
        
    Returns:
        list: Prime counts for each range.
    """
    # Determine the number of processes to match the CPU core count.
    processes = mp.cpu_count()
    with mp.Pool(processes=processes) as pool:
        # starmap lets us unpack each tuple as separate arguments
        results = pool.starmap(count_primes_in_range, ranges)
    return results

def main():
    # Define 20 ranges of 10,000 numbers each starting at 1,000,000.
    ranges = [(1000000 + i * 10000, 1000000 + (i + 1) * 10000) for i in range(20)]
    
    # --- Multiprocessing Execution ---
    start_time = time.time()
    multiprocessing_results = run_multiprocessing(ranges)
    multiprocessing_time = time.time() - start_time
    print("Multiprocessing Prime Counts per Range:")
    print(multiprocessing_results)
    print(f"Multiprocessing Execution Time: {multiprocessing_time:.4f} seconds\n")

if __name__ == '__main__':
    main()
