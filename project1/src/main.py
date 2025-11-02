from wordcount import wordcount
from entropy import compute_entropy
from visualize import plot_zipf

def main():
    # Load both speeches
    lincoln_results, freq_lincoln = wordcount('gettysburg.txt')
    jfk_results, freq_jfk = wordcount('inaugural_address_jfk.txt')

    # Compute entropy
    H_lincoln = compute_entropy(freq_lincoln)
    H_jfk = compute_entropy(freq_jfk)

    # Plot results
    plot_zipf(freq_lincoln, freq_jfk,
              'Gettysburg Address (Lincoln)',
              'JFK Inaugural Address')

    # Print output
    print("\n==============================")
    print("  Shannon Entropy Comparison")
    print("==============================")
    print(f"Gettysburg Address: {H_lincoln:.3f} bits")
    print(f"JFK Inaugural Address: {H_jfk:.3f} bits\n")

if __name__ == "__main__":
    main()
