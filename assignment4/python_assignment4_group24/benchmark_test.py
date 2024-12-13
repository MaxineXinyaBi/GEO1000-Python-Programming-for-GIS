import time
import subprocess
from tabulate import tabulate
import matplotlib.pyplot as plt


def python_test_time(n):
    start_time = time.perf_counter()
    subprocess.run(['python', 'nbody.py', str(n)], stdout=subprocess.DEVNULL)
    end_time = time.perf_counter()
    duration = end_time - start_time
    return duration


def cpp_test_time(n, mode):
    start_time = time.perf_counter()
    execute_path = f'cmake-build-{mode}/nbody.exe'
    subprocess.run([execute_path, str(n)], stdout=subprocess.DEVNULL)
    end_time = time.perf_counter()
    duration = end_time - start_time
    return duration


def main():
    data = []
    python_times = []
    cpp_debug_times = []
    cpp_release_times = []
    data_headers = ['Iteration', 'Python Run Time', 'CPP Debug Time', 'CPP Release Time']
    iterations = [500, 5000, 50000, 500000, 5000000]
    for n in iterations:
        python_time = python_test_time(n)
        cpp_time_debug = cpp_test_time(n, mode='debug')
        cpp_time_release = cpp_test_time(n, mode='release')
        python_times.append(python_time)
        cpp_debug_times.append(cpp_time_debug)
        cpp_release_times.append(cpp_time_release)
        data.append([n, f"{python_time:.4f}", f"{cpp_time_debug:.4f}", f"{cpp_time_release:.4f}"])

    print(tabulate(data, headers=data_headers))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    ax1.plot(iterations, python_times, 'ro-', label='Python', linewidth=2, markersize=8)
    ax1.plot(iterations, cpp_debug_times, 'yo-', label='CPP Debug', linewidth=2, markersize=8)
    ax1.plot(iterations, cpp_release_times, 'bo-', label='CPP Release', linewidth=2, markersize=8)
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Time (s)')
    ax1.set_title('Linear Scale Comparison')
    ax1.legend()
    ax1.grid(True)
    ax1.set_xscale('log')
    ax1.set_xticks(iterations)
    ax1.set_xticklabels([f'{i:,}' for i in iterations], rotation=45)

    ax2.plot(iterations, python_times, 'ro-', label='Python', linewidth=2, markersize=8)
    ax2.plot(iterations, cpp_debug_times, 'yo-', label='CPP Debug', linewidth=2, markersize=8)
    ax2.plot(iterations, cpp_release_times, 'bo-', label='CPP Release', linewidth=2, markersize=8)
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Time (s)')
    ax2.set_title('Log Scale Comparison')
    ax2.legend()
    ax2.grid(True)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xticks(iterations)
    ax2.set_xticklabels([f'{i:,}' for i in iterations], rotation=45)

    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()