def opt_conv():
    
    rows, cols = input("Enter number of rows and colomns: ").split(",")
    rows, cols = int(rows), int(cols)
    
    M = np.random.randint(255, size=(rows, cols), dtype=np.int16)
    K = [-1, 0, 1]
    
    start = time.time()
    Dx = np.roll(M, -1, axis=1) - np.roll(M, 1, axis=1)
    Dx = Dx[:, 1:-1]
    end = time.time()
    print("Time to calculate Dx = " + str(end-start) + "s")

    start = time.time()
    Dy = np.roll(M, -1, axis=0) - np.roll(M, 1, axis=0)
    Dy = Dy[1:-1, :]
    end = time.time()
    print("Time to calculate Dy = " + str(end-start) + "s")
    
    Dx_min = np.min(Dx)
    Dx_max = np.max(Dx)
    print(Dx_min, Dx_max)

    Dy_min = np.min(Dy)
    Dy_max = np.max(Dy)
    print(Dy_min, Dy_max)
    
opt_conv()