try:
    import non_existent_module: 
except ImportError:
    print("Error: Module not found!")
