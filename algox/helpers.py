import os
import time
import random
import tracemalloc
import gc

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
GREY = "\033[90m" 
RESET = "\033[0m"


DEBUG = int(os.environ.get("DEBUG", 0))
N = int(os.environ.get("N",1024))

def animate(func):
	def wrapper(*args, **kwargs):
		if DEBUG == 0:
			for size, t, mem in func(*args, **kwargs):
				size_format = MAGENTA + func.__name__ + GREY + "_" + YELLOW + "N" +  GREY + "_" + RESET + CYAN + str(size) 
				time_format = "        " + GREY + f"{t*1000:.4f}" + RESET + " ms"
				mem_format = "        " + GREEN + f"{mem/1024:.2f} KiB"
				
				print(size_format, time_format, mem_format)
				time.sleep(0.1)
				
		elif DEBUG == 1:
			import matplotlib.pyplot as plt
			from matplotlib.animation import FuncAnimation
			
			sizes = []
			times = []
			for size, t, _ in func(*args, **kwargs):
				sizes.append(size)
				times.append(t)
			
			plt.style.use("ggplot")
			
			fig, ax = plt.subplots(figsize=(8, 5))
			fig.canvas.manager.set_window_title("dsaX")
			ax.set_title(f"Performance of {func.__name__}", fontsize=14, weight="bold")
			ax.set_xlabel("Input Size (N)", fontsize=12)
			ax.set_ylabel("Time (Seconds)", fontsize=12)
			ax.grid(True, alpha=0.3)
			
			line, = ax.plot([], [], linewidth=2.5, label=func.__name__)
			ax.legend()

			def update(frame):
				line.set_data(sizes[:frame], times[:frame])
				ax.set_xlim(0, max(sizes))
				ax.set_ylim(0, max(times) * 1.1)
				return line,
				
			# IMPORTANT: store animation in a variable
			anim = FuncAnimation(
			fig,
			update,
			frames=len(sizes),
			interval=50,
			blit=False
			)
			
			plt.tight_layout()
			plt.show()
		elif DEBUG == 2:
			import matplotlib.pyplot as plt
			from matplotlib.animation import FuncAnimation
			for size, t in func(*args, **kwargs):
				sizes.append(size)
				times.append(t)
			
			plt.style.use("ggplot")
			
			fig, ax = plt.subplots(figsize=(8, 5))
			fig.canvas.manager.set_window_title("dsaX")
			ax.set_title(f"Performance of {func.__name__}", fontsize=14, weight="bold")
			ax.set_xlabel("Input Size (N)", fontsize=12)
			ax.set_ylabel("Time (Seconds)", fontsize=12)
			ax.grid(True, alpha=0.3)
			
			line, = ax.plot([], [], linewidth=2.5, label=func.__name__)
			ax.legend()

			def update(frame):
				line.set_data(sizes[:frame], times[:frame])
				ax.set_xlim(0, max(sizes))
				ax.set_ylim(0, max(times) * 1.1)
				return line,
				
			# IMPORTANT: store animation in a variable
			anim = FuncAnimation(
			fig,
			update,
			frames=len(sizes),
			interval=50,
			blit=False
			)
			
			plt.tight_layout()
			plt.show()
	return wrapper

def timeit(func, *args, **kwargs):
	st = time.perf_counter() # perf_counter() highly accurate
	func(*args, **kwargs)
	et = time.perf_counter()
	
	t = (et - st) # Seconds 
	return t


def generate(lower=None, upper=None, step = 10, sort=False):
	if lower is None:
		lower = step
	if upper is None:
		upper = N
	
	sizes = [i for i in range(lower, upper + 1, step)]
	for size in sizes:
		arr = [random.randint(1, N * N) for _ in range(size)]
		if not sort:
			yield size, arr
		else:
			yield size, sorted(arr)

def copyargs(args):
	# Only copy lists, leave other arguments as-is
	return [arg.copy() if isinstance(arg, list) else arg for arg in args]


def memusage(func, *args):
	gc.collect()
	tracemalloc.start()
	_ = func(*args)
	_, peak = tracemalloc.get_traced_memory()
	tracemalloc.stop()
	return peak # in Bytes
	

def benchmark(func, *args):
	#args_time = copyargs(args)
	#args_mem  = copyargs(args)
	
	t = timeit(func, *args)
	peak = memusage(func, *args)
	
	return t, peak




