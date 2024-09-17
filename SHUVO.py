import ctypes

# .so ফাইল লোড করা
lib = ctypes.CDLL('./FILE_enc.cpython-311.so')

# এখন আপনি সেখানে থাকা ফাংশনগুলো কল করতে পারবেন
# উদাহরণ:
result = lib.some_function()  # 'some_function' হল সেই ফাংশন যা .so ফাইলে আছে
print(result)
