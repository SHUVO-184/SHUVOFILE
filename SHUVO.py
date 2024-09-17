import ctypes

try:
    # .so ফাইল লোড করা
    lib = ctypes.CDLL('./FILE_enc.cpython-311.so')
    print("Library loaded successfully")

    # যদি ফাইলের ভিতরে কোনো নির্দিষ্ট ফাংশন কল করতে চান:
    if hasattr(lib, 'some_function'):
        lib.some_function.argtypes = [ctypes.c_int]  # আর্গুমেন্ট টাইপ নির্ধারণ করুন (যদি প্রয়োজন হয়)
        lib.some_function.restype = ctypes.c_int      # রিটার্ন টাইপ নির্ধারণ করুন (যদি প্রয়োজন হয়)

        result = lib.some_function(42)  # ফাংশন কল করুন এবং আর্গুমেন্ট দিন
        print(f"Function returned: {result}")
    else:
        print("Function 'some_function' not found in the library")
except Exception as e:
    print(f"Error: {e}")
