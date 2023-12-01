import sys
import time

sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
print("Downloading")
for n in range(10):
    print(".", end=' ', flush=True)
    if (n % 3) == 0:
        print("")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    time.sleep(1)