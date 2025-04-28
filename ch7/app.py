# import subprocess
#
# result = subprocess.run(['echo', 'Hello from the child!'], capture_output=True, encoding='utf-8')
#
# # result.check_returncode()
# # print(result.stdout)
# # proc = subprocess.Popen(['sleep', '1'])
# # while proc.poll() is None:
# #     print('Working...')
# #
# # print('Exit status', proc.poll())
# # import time
# #
# # start = time.time()
# # sleep_procs = []
# # for _ in range(10):
# #     proc = subprocess.Popen(['sleep', '1'])
# #     sleep_procs.append(proc)
# #
# # for proc in sleep_procs:
# #     proc.communicate()
# #
# # end = time.time()
# # delta = end - start
# # # print(f'Finished in {delta:.3} seconds')
# # import os
# # def run_encrypt(data):
# #     env = os.environ.copy()
# #     env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
# #     proc = subprocess.Popen(['openssl', 'enc', '-des3', '-pass', 'env:password'], env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# #     proc.stdin.write(data)
# #     proc.stdin.flush()
# #     return proc
# #
# # procs = []
# # for _ in range(3):
# #     data = os.urandom(10)
# #     proc = run_encrypt(data)
# #     procs.append(proc)
#
# # for proc in procs:
# #     out, _ = proc.communicate()
# #     print(out[-10:])
# # def run_hash(input_stdin):
# #     return subprocess.Popen(['openssl', 'dgst', '-whirlpool', '-binary'], stdin=input_stdin, stdout=subprocess.PIPE)
# #
# # encrypt_procs = []
# # hash_procs = []
# # for _ in range(3):
# #     data = os.urandom(100)
# #
# #     encrypt_proc = run_encrypt(data)
# #     encrypt_procs.append(encrypt_proc)
# #
# #     hash_proc = run_hash(encrypt_proc.stdout)
# #     hash_procs.append(hash_proc)
# #     encrypt_proc.stdout.close()
# #     encrypt_proc.stdout = None
# #
# # for proc in encrypt_procs:
# #     proc.communicate()
# #     assert proc.returncode == 0
#
# # for proc in hash_procs:
# #     out, _ = proc.communicate()
# #     print(out[-10:])
# #     assert proc.returncode == 0
# # proc = subprocess.Popen(['sleep', '10'])
# # try:
# #     proc.communicate(timeout=0.1)
# # except subprocess.TimeoutExpired: 
# #     proc.terminate()
# #     proc.wait()
# #
# # print('Exit status', proc.poll())
# def factorize(number):
#     for i in range(1, number + 1):
#         if number % i == 0:
#             yield i
#
# import time
# #
# numbers = [2139079, 1214759, 1516637, 1852285]
# # start = time.time()
# #
# # for number in numbers:
# #     list(factorize(number))
# #
# # end = time.time()
# # delta = end -start
# # print(f'Took {delta:.3f} seconds')
# from threading import Thread
#
# class FactorizeThread(Thread):
#     def __init__(self, number):
#         super().__init__()
#         self.number = number
#
#     def run(self):
#         self.factors = list(factorize(self.number))
#
# start = time.time()
#
# threads = []
# for number in numbers:
#     thread = FactorizeThread(number)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# end = time.time()
# delta = end - start
# """ print(f'Took {delta:.3f} seconds') """
# import select
# import socket
#
# def slow_systematical():
#     select.select([socket.socket()], [], [], 0.1)
#
# start = time.time()
#
# for _ in range(5):
#     slow_systematical()
#
# end = time.time()
# delta = end - start
# # print(f'Took {delta:.3f} seconds')
# start = time.time()
# threads = []
# for _ in range(5):
#     thread = Thread(target=slow_systematical)
#     thread.start()
#     threads.append(thread)
#
# def compute_helicopter_location(index):
#     ...
#
# for i in range(5):
#     compute_helicopter_location(i)
#
# for thread in threads:
#     thread.join()
#
# end = time.time()
# delta = end - start
# # print(f'Took {delta:.3f} seconds')
# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def increment(self, offset):
#         self.count += offset
#
# def worker(sensor_index, how_many, counter):
#     for _ in range(how_many):
#         # Read from the sensor
#         ...
#         counter.increment(1)
#
# from threading import Thread
#
# how_many = 10**5
# counter = Counter()
#
# threads = []
# for i in range(5):
#     thread = Thread(target=worker, args=(i, how_many, counter))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# # expected = how_many * 5
# # found = counter.count
# # print(f'Counter should be {expected}, got {found}')
# # Running in a Thread A
# value_a = getattr(counter, 'count')
# # Context switch to Thread B
# value_b = getattr(counter, 'count')
# result_b = getattr(counter, 'count')
# result_b = value_b + 1
# setattr(counter, 'count', result_b)
# # Context switch back to Thread A
# result_a = value_a + 1
# setattr(counter, 'count', result_a)
#
# from threading import Lock
#
# class LockingCounter:
#     def __init__(self):
#         self.lock = Lock()
#         self.count = 0
#
#     def increment(self, offset):
#         with self.lock:
#             self.count += offset
#
# counter = LockingCounter()
#
# for i in range(5):
#     thread = Thread(target=worker, args=(i, how_many, counter))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# expected = how_many * 5
# found = counter.count
# # print(f'Counter should be {expected}, got {found}')
# def download(item):
#     ...
#
# def resize(item):
#     ...
#
# def upload(item):
#     ...
#
# from collections import deque
# from threading import Lock
#
# class MyQueue:
#     def __init__(self):
#         self.items = deque()
#         self.lock = Lock()
#
#     def put(self, item):
#         with self.lock:
#             self.items.append(item)
#
#     def get(self):
#         with self.lock:
#             return self.items.popleft()
#
# from threading import Thread
# import time
#
# class Worker(Thread):
#     def __init__(self, func, in_queue, out_queue):
#         super().__init__()
#         self.func = func
#         self.in_queue = in_queue
#         self.out_queue = out_queue
#         self.polled_count = 0
#         self.work_done = 0
#
#     def run(self):
#         while True:
#             self.polled_count += 1
#             try:
#                 item = self.in_queue.get()
#             except IndexError: 
#                 time.sleep(0.01)
#             else:
#                 result = self.func(item)
#                 self.out_queue.put(result)
#                 self.work_done += 1
#
# download_queue = MyQueue()
# resize_queue = MyQueue()
# upload_queue = MyQueue()
#
# done_queue = MyQueue()
# threads = [Worker(download, download_queue, resize_queue), Worker(resize, resize_queue, upload_queue), Worker(upload, upload_queue, done_queue)]
#
# for thread in threads:
#     thread.start()
#
# for _ in range(1000):
#     download_queue.put(object())
#
# # ALIVE = '*'
# # EMPTY = '_' 
# # class Grid:
# #     def __init__(self, height, width):
# #         self.height = height
# #         self.width = width
# #         self.rows = []
# #         for _ in range(self.height):
# #             self.rows.append([EMPTY] * self.width)
# #
# #     def get(self, y, x):
# #         return self.rows[y % self.height][x % self.width]
# #
# #     def set(self, y, x, state):
# #         self.rows[y % self.height][x % self.width] = state
# #
# #     def __str__(self):
# #         output = []
# #         for row in self.rows:
# #             output.append('|' + ''.join(row) + '|')
# #         return '\n'.join(output)
# #
# #
# # grid = Grid(5, 9)
# # grid.set(0, 3, ALIVE)
# # grid.set(1, 4, ALIVE)
# # grid.set(2, 2, ALIVE)
# # grid.set(2, 3, ALIVE)
# # grid.set(2, 4, ALIVE)
# # # print(grid)
# #
# # def count_neighbours(y, x, get):
# #     n_ = get(y - 1, x + 0)
# #     ne = get(y - 1, x + 1)
# #     e_ = get(y + 0, x + 1)
# #     se = get(y + 1, x + 1)
# #     s_ = get(y + 1, x + 0)
# #     sw = get(y + 1, x - 1)
# #     w_ = get(y + 0, x - 1)
# #     nw = get(y - 1, x - 1)
# #     neigbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
# #     count = 0
# #
# #     for state in neigbor_states:
# #         if state == ALIVE:
# #             count += 1
# #     return count
# #
# # def game_logic(state, neighbors):
# #     if state == ALIVE:
# #         if neighbors == ALIVE:
# #             if neighbors < 2:
# #                 return EMPTY
# #             elif neighbors > 3:
# #                 return EMPTY
# #     else:
# #         if neighbors == 3:
# #             return ALIVE
# #     return state
# #
# # def step_cell(y, x, get, set):
# #     state = get(y, x)
# #     neighbors = count_neighbours(y, x, get)
# #     next_state = game_logic(state, neighbors)
# #     set(y, x, next_state)
# #
# # def simulate(grid):
# #     next_grid = Grid(grid.height, grid.width)
# #     for y in range(grid.height):
# #         for x in range(grid.width):
# #             step_cell(y, x, grid.get, next_grid.set)
# #     return next_grid
# #
# # class ColumnPrinter:
# #     ...
# #
# # columns = ColumnPrinter()
# # for i in range(5):
# #     columns.append(str(grid))
# #     grid = simulate(grid)
# #
# # print(columns)
# # ALIVE = '*'
# # EMPTY = '_'
# #
# # class Grid:
# #     def __init__(self, height, width):
# #         self.height = height
# #         self.width = width
# #         self.rows = []
# #         for _ in range(self.height):
# #             self.rows.append([EMPTY] * self.width)
# #
# #     def get(self, y, x):
# #         return self.rows[y % self.height][x % self.width]
# #
# #     def set(self, y, x, state):
# #         self.rows[y % self.height][x % self.width] = state
# #
# #     def __str__(self):
# #         output = []
# #         for row in self.rows:
# #             output.append('|' + ''.join(row) + '|')
# #         return '\n'.join(output)
#
# # def count_neighbours(y, x, get):
# #     n_ = get(y - 1, x + 0)
# #     ne = get(y - 1, x + 1)
# #     e_ = get(y + 0, x + 1)
# #     se = get(y + 1, x + 1)
# #     s_ = get(y + 1, x + 0)
# #     sw = get(y + 1, x - 1)
# #     w_ = get(y + 0, x - 1)
# #     nw = get(y - 1, x - 1)
# #     neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
# #     count = 0
# #     for state in neighbor_states:
# #         if state == ALIVE:
# #             count += 1
# #     return count
# #
# # def game_logic(state, neighbors):
# #     if state == ALIVE:
# #         if neighbors < 2 or neighbors > 3:
# #             return EMPTY
# #         return ALIVE
# #     else:
# #         if neighbors == 3:
# #             return ALIVE
# #         return EMPTY
# #
# # def step_cell(y, x, get, set):
# #     state = get(y, x)
# #     neighbors = count_neighbours(y, x, get)
# #     next_state = game_logic(state, neighbors)
# #     set(y, x, next_state)
# #
# # def simulate(grid):
# #     next_grid = Grid(grid.height, grid.width)
# #     for y in range(grid.height):
# #         for x in range(grid.width):
# #             step_cell(y, x, grid.get, next_grid.set)
# #     return next_grid
# #
# # class ColumnPrinter:
# #     def __init__(self):
# #         self.columns = []
# #
# #     def append(self, grid_str):
# #         grid_lines = grid_str.split("\n")
# #         self.columns.append(grid_lines)
# #
# #     def __str__(self):
# #         if not self.columns:
# #             return ""
# #
# #         combined_lines = []
# #         for line_parts in zip(*self.columns):
# #             combined_lines.append("    ".join(line_parts))
# #
# #         return "\n".join(combined_lines)
# #
# # # Initialize and run simulation
# # grid = Grid(5, 9)
# # grid.set(0, 3, ALIVE)
# # grid.set(1, 4, ALIVE)
# # grid.set(2, 2, ALIVE)
# # grid.set(2, 3, ALIVE)
# # grid.set(2, 4, ALIVE)
# #
# # columns = ColumnPrinter()
# # for i in range(5):
# #     columns.append(str(grid))
# #     grid = simulate(grid)
# #
# # print(columns)
#
# from threading import Lock, Thread
#
# ALIVE = '*'
# EMPTY = '_'
#
# class Grid:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.rows = []
#         for _ in range(self.height):
#             self.rows.append([EMPTY] * self.width)
#
#     def get(self, y, x):
#         return self.rows[y % self.height][x % self.width]
#
#     def set(self, y, x, state):
#         self.rows[y % self.height][x % self.width] = state
#
#     def __str__(self):
#         output = []
#         for row in self.rows:
#             output.append('|' + ''.join(row) + '|')
#         return '\n'.join(output)
#
# class LockingGrid(Grid):
#     def __init__(self, height, width):
#         super().__init__(height, width)
#         self.lock = Lock()
#
#     def __str__(self):
#         with self.lock:
#             return super().__str__()
#
#     def get(self, y, x):
#         with self.lock:
#             return super().get(y, x)
#
#     def set(self, y, x, state):
#         with self.lock:
#             return super().set(y, x, state)
#
# async def count_neighbours(y, x, get):
#     n_ = get(y - 1, x + 0)
#     ne = get(y - 1, x + 1)
#     e_ = get(y + 0, x + 1)
#     se = get(y + 1, x + 1)
#     s_ = get(y + 1, x + 0)
#     sw = get(y + 1, x - 1)
#     w_ = get(y + 0, x - 1)
#     nw = get(y - 1, x - 1)
#     neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
#     count = 0
#     for state in neighbor_states:
#         if state == ALIVE:
#             count += 1
#     return count
#
# # def game_logic(state, neighbors):
# #     if state == ALIVE:
# #         if neighbors < 2 or neighbors > 3:
# #             return EMPTY
# #         return ALIVE
# #     else:
# #         if neighbors == 3:
# #             return ALIVE
# #         return EMPTY
#
# async def step_cell(y, x, get, set):
#     state = get(y,x)
#     neighbors = await count_neighbours(y, x, get)
#     next_state = await game_logic(state, neighbors)
#     set(y, x, next_state)
#
# # def simulate_threaded(grid):
# #     next_grid = LockingGrid(grid.height, grid.width)
# #
# #     threads = []
# #     for y in range(grid.height):
# #         for x in range(grid.width):
# #             args = (y, x, grid.get, next_grid.set)
# #             thread = Thread(target=step_cell, args=args)
# #             thread.start()
# #             threads.append(thread)
# #
# #     for thread in threads:
# #         thread.join()
# #
# #     return next_grid
# import asyncio
#
# async def simulate(grid):
#     next_grid = Grid(grid.height, grid.width)
#
#     tasks = []
#     for y in range(grid.height):
#         for x in range(grid.width):
#             task = step_cell(y, x, grid.get, next_grid.set)
#             tasks.append(task)
#
#     await asyncio.gather(*tasks)
#
#     return next_grid
#
# class ColumnPrinter:
#     def __init__(self):
#         self.columns = []
#
#     def append(self, grid_str):
#         grid_lines = grid_str.split("\n")
#         self.columns.append(grid_lines)
#
#     def __str__(self):
#         if not self.columns:
#             return ""
#
#         combined_lines = []
#         for line_parts in zip(*self.columns):
#             combined_lines.append("    ".join(line_parts))
#
#         return "\n".join(combined_lines)
#
# # grid = LockingGrid(5, 9)
# # grid.set(0, 3, ALIVE)
# # grid.set(1, 4, ALIVE)
# # grid.set(2, 2, ALIVE)
# # grid.set(2, 3, ALIVE)
# # grid.set(2, 4, ALIVE)
# #
# # columns = ColumnPrinter()
# # for i in range(5):
# #     columns.append(str(grid))
# #     grid = simulate_threaded(grid)
# #
# # # print(columns)
# # import contextlib
# # import io
# #
# # fake_stderr = io.StringIO()
# # with contextlib.redirect_stderr(fake_stderr):
# #     thread = Thread(target=game_logic, args=(ALIVE, 3))
# #     thread.start()
# #     thread.join()
# #
# # # print(fake_stderr.getvalue())
# # from queue import Queue
# #
# # class ClosableQueue(Queue):
# #     ...
# #
# # class StoppableWorker(Thread):
# #     ...
# #
# # in_queue = ClosableQueue()
# # out_queue = ClosableQueue()
# #
# # def game_logic_thread(item):
# #     y, x, state, neighbors = item
# #     try:
# #         next_state = game_logic(state, neighbors)
# #     except Exception as e:
# #         next_state = e
# #     return (y, x, next_state)
# #
# # threads = []
# #
# # for _ in range(5):
# #     thread = StoppableWorker(game_logic_thread, in_queue, out_queue)
# #     thread.start()
# #     threads.append(thread)
# #
# # class SimulationError(Exception):
# #     pass
# #
# # def simulate_pipeline(grid, in_queue, out_queue):
# #     for y in range(grid.height):
# #         for x in range(grid.width):
# #             state = grid.get(y, x)
# #             neighbors = count_neighbours(y, x, grid.get)
# #             in_queue.put((y, x, state, neighbors))
# #
# #     in_queue.join()
# #     out_queue.close()
# #
# #     next_grid = Grid(grid.height, grid.width)
# #     for item in out_queue:
# #         y, x, next_state = item
# #         if isinstance(next_state, Exception):
# #             raise SimulationError(y, x) from next_state
# #         next_grid.set(y, x, next_state)
# #
# #     return next_grid
# #
# # # simulate_pipeline(Grid(1, 1), in_queue, out_queue)
# # grid = Grid(5, 9)
# # grid.set(0, 3, ALIVE)
# # grid.set(1, 4, ALIVE)
# # grid.set(2, 2, ALIVE)
# # grid.set(2, 3, ALIVE)
# # grid.set(2, 4, ALIVE)
#
# # columns = ColumnPrinter()
# # for i in range(5):
# #     columns.append(str(grid))
# #     grid = simulate_pipeline(grid, in_queue, out_queue)
# #
# # print(columns)
# #
# # for thread in threads:
# #     in_queue.close()
# # for thread in threads:
# #     thread.join()
# # def count_neighbours_thread(item):
# #     y, x, state, get = item
# #     try:
# #         neighbors = count_neighbours(y, x, get)
# #     except Exception as e:
# #         neighbors = e
# #     return (y, x, state, neighbors)
# #
# # def game_logic_thread(item):
# #     y, x, state, neighbors = item
# #     if isinstance(neighbors, Exception):
# #         next_state = neighbors
# #     else:
# #         try:
# #             next_state = game_logic(state, neighbors)
# #         except Exception as e:
# #             next_state = e
# #         return (y, x, next_state)
# #
# # in_queue = ClosableQueue()
# # logic_queue = ClosableQueue()
# # out_queue = ClosableQueue()
# # threads = []
# #
# # for _ in range(5):
# #     thread = StoppableWorker(count_neighbours_thread, in_queue, logic_queue)
# #     thread.start()
# #     threads.append(thread)
# #
# # for _ in range(5):
# #     thread = StoppableWorker(game_logic_thread, logic_queue, out_queue)
# #     thread.start()
# #     threads.append(thread)
# #
# # def simulate_phased_pipeline(grid, in_queue, logic_queue, out_queue):
# #     for y in range(grid.height):
# #         for x in range(grid.width):
# #             state = grid.get(y, x)
# #             item = (y, x, state, grid.get)
# #             in_queue.put(item)
# #
# #     in_queue.join()
# #     logic_queue.join()
# #     out_queue.close()
# #
# #     next_grid = LockingGrid(grid.height, grid.width)
# #     for item in out_queue:
# #         y, x, next_state = item
# #         if isinstance(next_state, Exception):
# #             raise SimulationError(y, x) from next_state
# #         next_grid.set(y,x, next_state)
# #
# #     return next_grid
# #
# # grid = LockingGrid(5, 9)
# # grid.set(0, 3, ALIVE)
# # grid.set(1, 4, ALIVE)
# # grid.set(2, 2, ALIVE)
# # grid.set(2,3, ALIVE)
# # grid.set(2,4, ALIVE)
# #
# # columns = ColumnPrinter()
# # for i in range(5):
# #     columns.append(str(grid))
# #     grid = simulate_phased_pipeline(grid, in_queue, logic_queue, out_queue)
# #
# # print(columns)
# #
# # for thread in threads:
# #     in_queue.close()
# # for thread in threads:
# #     logic_queue.close()
# # for thread in threads:
# #     thread.join()
# from concurrent.futures import ThreadPoolExecutor
#
# async def game_logic(state, neighbors):
#     if state == ALIVE:
#         if neighbors < 2 or neighbors > 3:
#             return EMPTY
#         return ALIVE
#     else:
#         if neighbors == 3:
#             return ALIVE
#         return EMPTY
#
# def simulate_pool(pool, grid):
#     next_grid = LockingGrid(grid.height, grid.width)
#     futures = []
#     for y in range(grid.height):
#         for x in range(grid.width):
#             args = (y, x, grid.get, next_grid.set)
#             future = pool.submit(step_cell, *args)
#             futures.append(future)
#
#     for future in futures:
#         future.result()
#
#     return next_grid
#
# grid = LockingGrid(5,9)
# grid.set(0, 3, ALIVE)
# grid.set(1, 4, ALIVE)
# grid.set(2, 2, ALIVE)
# grid.set(2, 3, ALIVE)
# grid.set(2, 4, ALIVE)
#
# columns = ColumnPrinter()
# for i in range(5):
#     columns.append(str(grid))
#     grid = asyncio.run(simulate(grid))
#
# # print(columns)
# # with ThreadPoolExecutor(max_workers=10) as pool:
# #     for i in range(5):
# #         columns.append(str(grid))
# #         grid = simulate_pool(pool, grid)
# # with ThreadPoolExecutor(max_workers=10) as pool:
# #     task = pool.submit(game_logic, ALIVE, 3)
# #     task.result()
#
# # print(columns)
# # class EOFError(Exception):
# #     pass
# #
# # class ConnectionBase:
# #     def __init__(self, connection):
# #         self.connection = connection
# #         self.file = connection.makefile('rb')
# #
# #     def send(self, command):
# #         line = command + '\n'
# #         data = line.encode()
# #         self.connection.send(data)
# #
# #     def receive(self):
# #         line = self.file.readline()
# #         if not line:
# #             raise EOFError('Connection closed')
# #         return line[:-1].decode()
# #
# # import random
# #
# # WARMER = 'Warmer'
# # COLDER = 'Colder'
# # UNSURE = 'Unsure'
# # CORRECT = 'Correct'
# #
# # class UnkownCommandError(Exception):
# #     pass
# #
# # class Session(ConnectionBase):
# #     def __init__(self, *args):
# #         super().__init__(*args)
# #         self._clear_state(None, None)
# #
# #     def _clear_state(self, lower, upper):
# #         self.lower = lower
# #         self.upper = upper
# #         self.secret = None
# #         self.guesses = []
# #
# #     def loop(self):
# #         while command := self.receive():
# #             parts = command.split(' ')
# #             if parts[0] == 'PARAMS':
# #                 self.set_params(parts)
# #             elif parts[0] == 'NUMBER':
# #                 self.send_number()
# #             elif parts[0] == 'REPORT':
# #                 self.receive_report(parts)
# #             else:
# #                 raise UnkownCommandError(command)
# #
# #     def set_params(self, parts):
# #         assert len(parts) == 3
# #         lower = int(parts[1])
# #         upper = int(parts[2])
# #         self._clear_state(lower, upper)
# #
# #     def next_guess(self):
# #         if self.secret is not None:
# #             return self.secret
# #
# #         while True:
# #             guess = random.randint(self.lower, self.upper)
# #             if guess not in self.guesses:
# #                 return guess
# #
# #     def send_number(self):
# #         guess = self.next_guess()
# #         self.guesses.append(guess)
# #         self.send(format(guess))
# #
# #     def receive_report(self, parts):
# #         assert len(parts) == 2
# #         decision = parts[1]
# #
# #         last = self.guesses[-1]
# #         if decision == CORRECT:
# #             self.secret = last
# #
# #         print(f'Server: {last} is {decision}')
# #
# # import contextlib
# # import math
# #
# # class Client(ConnectionBase):
# #     def __init__(self, *args):
# #         super().__init__(*args)
# #         self._clear_state()
# #
# #     def _clear_state(self):
# #         self.secret = None
# #         self.last_distance = None
# #
# #
# #
# # @contextlib.asynccontextmanager
# # async def session(self, lower, upper, secret):
# #     print(f'Guess a number between {lower} and {upper}! Shhhhh, it\'s {secret}.')
# #     self.secret = secret
# #     await self.send(f'PARAMS {lower}')
# #     try:
# #         yield
# #     finally:
# #         self._clear_state()
# #         await self.send('PARAMS 0 -1')
# #
# # async def request_numbers(self, count):
# #     for _ in range(count):
# #         await self.send('NUMBER')
# #         data = await self.receive()
# #         yield int(data)
# #         if self.last_distance == 0:
# #             return
# #
# # async def report_outcome(self, number):
# #     new_distance = math.fabs(number - self.secret)
# #     decision = UNSURE
# #
# #     if new_distance == 0:
# #         decision = CORRECT
# #     elif self.last_distance is None:
# #         pass
# #     elif new_distance < self.last_distance:
# #         decision = WARMER
# #     elif new_distance > self.last_distance:
# #         decision = COLDER
# #
# #     self.last_distance = new_distance
# #
# #     await self.send(f'REPORT {decision}')
# #     return decision
# #
# # import socket
# # from threading import Thread
# # import asyncio
# #
# # def handle_connection(connection):
# #     with connection:
# #         session = Session(connection)
# #         try:
# #             session.loop()
# #         except EOFError: 
# #             pass
# #
# # async def handle_async_connection(reader, writer):
# #     session = AsyncSession(reader, writer)
# #     try:
# #         await session.loop()
# #     except EOFError: 
# #         pass
# #
# # def run_server(address):
# #     with socket.socket() as listener:
# #         listener.bind(address)
# #         listener.listen()
# #         while True:
# #             connection, _ = listener.accept()
# #             thread = Thread(target=handle_connection, args=(connection,),daemon=True)
# #             thread.start()
# #
# # async def run_async_server(address):
# #     server = await asyncio.start_server(handle_async_connection, *address)
# #     async with server:
# #         await server.serve_forever()
# #
# # # def run_client(address):
# # #     with socket.create_connection(address) as connection:
# # #         client = Client(connection)
# # #
# # #         with client.session(1, 5, 3):
# # #             results = [(x, client.report_outcome(x)) for x in client.request_numbers(5)]
# # #
# # #         with client.session(10, 15, 12):
# # #             for number in client.request_numbers(5):
# # #                 outcome = client.report_outcome(number)
# # #                 results.append((number, outcome))
# # #
# # #     return results
# # async def run_async_client(address):
# #     streams = await asyncio.open_connection(*address)
# #     client = AsyncClient(*streams)
# #
# #     async with client.session(1,5,3):
# #         results = [(x, await client.report_outcome(x)) async for x in client.request_numbers(5)]
# #
# #     async with client.session(10, 15, 12):
# #         async for number in client.request_numbers(5):
# #             outcome = await client.report_outcome(number)
# #             results.append(number, outcome)
# #
# #     _, writer = streams
# #     writer.close()
# #     await writer.wait_closed()
# #
# #     return results
# #
# # def main():
# #     address = ('127.0.0.1', 1234)
# #     server_thread = Thread(target=run_server, args=(address,), daemon=True)
# #     server_thread.start()
# #
# #     results = run_client(address)
# #     for number, outcome in results:
# #         print(f'Client: {number} is {outcome}')
# # async def main_async():
# #     address = ('127.0.0.1', 4321)
# #
# #     server = run_async_server(address)
# #     asyncio.create_task(server)
# #
# #     results = await run_async_client(address)
# #     for number, outcome in results:
# #         print(f'Client: {number} is {outcome}')
# #
# # asyncio.run(main_async())
# #
# # # main()
# # class AsyncConnectionBase:
# #     def __init__(self, reader, writer):
# #         self.reader = reader
# #         self.writer = writer
# #
# #     async def send(self, command):
# #         line = command + '\n'
# #         data = line.encode()
# #         self.writer.write(data)
# #         await self.writer.drain()
# #
# #     async def receive(self):
# #         line = await self.reader.readline()
# #         if not line:
# #             raise EOFError('Connection closed')
# #         return line[:-1].decode()
# #
# # class AsyncSession(AsyncConnectionBase):
# #     def __init__(self, *args):
# #         super().__init__(*args)
# #         self._clear_state(None, None)
# #
# #     def _clear_state(self, lower, upper):
# #         self.lower = lower
# #         self.upper = upper
# #         self.secret = None
# #         self.guesses = []
# #
# #     async def loop(self):
# #         while command := await self.receive():
# #             parts = command.split(' ')
# #             if parts[0] == 'PARAMS':
# #                 self.set_params(parts)
# #             elif parts[0] == 'NUMBER':
# #                 await self.send_number()
# #             elif parts[0] == 'REPORT':
# #                 self.receive_report(parts)
# #             else:
# #                 raise UnkownCommandError(command)
# #
# #     def set_params(self, parts):
# #         assert len(parts) == 3
# #         lower = int(parts[1])
# #         upper = int(parts[2])
# #         self._clear_state(lower, upper)
# #
# #     def next_guess(self):
# #         if self.secret is not None:
# #             return self.secret
# #
# #         while True:
# #             guess = random.randint(self.lower, self.upper)
# #             if guess not in self.guesses:
# #                 return guess
# #
# #     async def send_number(self):
# #         guess = self.next_guess()
# #         self.guesses.append(guess)
# #         await self.send(format(guess))
# #
# #     def receive_report(self, parts):
# #         assert len(parts) == 2
# #         decision = parts[1]
# #
# #         last = self.guesses[-1]
# #         if decision == CORRECT:
# #             self.secret = last
# #
# #         print(f'Server: {last} is {decision}')
# #
# # class AsyncClient(AsyncConnectionBase):
# #     def __init__(self, *args):
# #         super().__init__(*args)
# #         self._clear_state()
# #
# #     def _clear_state(self):
# #         self.secret = None
# #         self.last_distance = None
# class NoNewData(Exception):
#     pass
#
# # def readline(handle):
# #     offset = handle.tell()
# #     handle.seek(0, 2)
# #     length = handle.tell()
# #
# #     if length == offset:
# #         raise NoNewData
# #
# #     handle.seek(offset, 0)
# #   return handle.readline()
#
# import time
#
# # def tail_file(handle, interval, write_func):
# #     while not handle.closed:
# #         try:
# #             line = readline(handle)
# #         except NoNewData: 
# #             time.sleep(interval)
# #         else:
# #             write_func(line)
#
# from threading import Lock, Thread
#
# def run_threads(handles, interval, output_path):
#     with open(output_path, 'wb') as output:
#         lock = Lock()
#         def write(data):
#             with lock:
#                 output.write(data)
#
#     threads = []
#     for handle in handles:
#         args = (handle, interval, write)
#         thread = Thread(target=tail_file, args=args)
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
# # def confirm_merge(input_paths, output_path):
# #     ...
#
# # input_paths = ...
# # handles = ...
# # output_path = ...
# # run_threads(handles, 0.1, output_path)
# #
# # confirm_merge(input_paths, output_path)
#
# import asyncio
#
# async def run_tasks_mixed(handles, interval, output_path):
#     loop = asyncio.get_event_loop()
#
#     with open(output_path, 'wb') as output:
#         async def write_async(data):
#             output.write(data)
#
#         def write(data):
#             coro = write_async(data)
#             future = asyncio.run_coroutine_threadsafe(coro, loop)
#             future.result()
#
#         tasks = []
#         for handle in handles:
#             task = loop.run_in_executor(None, tail_file, handle, interval, write)
#             tasks.append(task)
#
#         await asyncio.gather(*tasks)
#
# # input_paths = ...
# # handles = ...
# # output_path = ...
# # asyncio.run(run_tasks_mixed(handles, 0.1, output_path))
# #
# # confirm_merge(input_paths, output_path)
# # async def tail_async(handle, interval, write_func):
# #     loop = asyncio.get_event_loop()
# #
# #     while not handle.closed:
# #         try:
# #             line = await loop.run_in_executor(None, readline, handle)
# #         except NoNewData: 
# #             await asyncio.sleep(interval)
# #         else:
# #             await write_func(line)
#
# # async def run_tasks(handles, interval, output_path):
# #     with open(output_path, 'wb') as output:
# #         async def write_async(data):
# #             output.write(data)
# #
# #         tasks = []
# #         for handle in handles:
# #             coro = tail_async(handle, interval, write_async)
# #             task = asyncio.create_task(coro)
# #             tasks.append(task)
# #
# #         await asyncio.gather(*tasks)
#
# # input_paths = ...
# # handles = ...
# # output_path = ...
# # asyncio.run(run_tasks(handles, 0.1, output_path))
# #
# # confirm_merge(input_paths, output_path)
# def tail_file(handle, interval, write_func):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#
#     async def write_async(data):
#         write_func(data)
#
#     coro = tail_async(handle, interval, write_async)
#     loop.run_until_complete(coro)
#
# input_paths = ...
# handles = ...
# output_path = ...
# run_threads(handles, 0.1, output_path)
#
# """ confirm_merge(input_paths, output_path) """
#
# # async def run_tasks(handles, interval, output_path):
# #     with open(output_path, 'wb') as output:
# #         async def write_async(data):
# #             output.write(data)
# #
# #         tasks = []
# #         for handle in handles:
# #             coro = tail_async(handle, interval, write_async)
# #             task = asyncio.create_task(coro)
# #             tasks.append(task)
# #
# #         await asyncio.gather(*tasks)
#
# async def run_tasks(handles, interval, output_path):
#     with open(output_path, 'wb') as output:
#         async def write_async(data):
#             output.write(data)
#
#         tasks = []
#         for handle in handles:
#             coro = tail_async(handle, interval, write_async)
#             task = asyncio.create_task(coro)
#             tasks.append(task)
#
#         await asyncio.gather(*tasks)
#
# import time
#
# async def slow_coroutine():
#     time.sleep(0.5)
#
# asyncio.run(slow_coroutine(), debug=True)
#
# from threading import Thread
#
# class WriteThread(Thread):
#     def __init__(self, output_path):
#         super().__init__()
#         self.output_path = output_path
#         self.output = None
#         self.loop = asyncio.new_event_loop()
#
#     def run(self):
#         asyncio.set_event_loop(self.loop)
#         with open(self.output_path, 'wb') as self.output_path: # type: ignore
#             self.loop.run_forever()
#
#         self.loop.run_until_complete(asyncio.sleep(0))
#
#     async def real_write(self, data):
#         self.output.write(data) # type: ignore
#
#     async def write(self, data):
#         coro = self.real_write(data)
#         future = asyncio.run_coroutine_threadsafe(coro, self.loop)
#         await asyncio.wrap_future(future)
#
#     async def real_stop(self):
#         self.loop.stop()
#
#     async def stop(self):
#         coro = self.real_stop()
#         future = asyncio.run_coroutine_threadsafe(coro, self.loop)
#         await asyncio.wrap_future(future)
#
#     async def __aenter__(self):
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(None, self.start)
#         return self
#
#     async def __aexit__(self, *_):
#         await self.stop()
#
# def readline(handle):
#     ...
#
# async def tail_async(handle, interval, write_func):
#     ...
#
# async def run_fully_async(handles, interval, output_path):
#     async with WriteThread(output_path) as output:
#         tasks = []
#         for handle in handles:
#             coro = tail_async(handle, interval, output_path)
#             task = asyncio.create_task(coro)
#             tasks.append(task)
#
#         await asyncio.gather(*tasks)
#
# def confirm_merge(input_paths, output_path):
#     ...
#
# input_paths = ...
# handles = ...
# output_path = ...
# asyncio.run(run_fully_async(handles, 0.1, output_path))
#
# confirm_merge(input_paths, output_path)
import time
from concurrent.futures import ProcessPoolExecutor

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    assert False, 'Not reachable'

NUMBERS = [
(1963309, 2265973), (2030677, 3814172),
(1551645, 2229620), (2039045, 2020802),
(1823712, 1924928), (2293129, 1020491),
(1281238, 2273782), (3823812, 4237281),
(3812741, 4729139), (1292391, 2123811),
]

# def main():
#     start = time.time()
#     results = list(map(gcd, NUMBERS))
#     end = time.time()
#     delta = end - start
#     print(f'Took {delta:.3f} seconds')
#
# if __name__ == '__main__':
#     main()
def main():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} seconds')

if __name__ == '__main__':
    main()
