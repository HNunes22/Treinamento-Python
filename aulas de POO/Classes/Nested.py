class Compute:
    def __init__(self, model, gpu_name, gpu_ram, gpu_cores):
        self.model = model
        self.gpu = self.GPU(gpu_name, gpu_ram, gpu_cores)

    def show_infos(self):
        print(f"COMPUTER\nModel: {self.model}\n{self.gpu.show_gpu_infos()}")

    class GPU:
        def __init__(self, gpu_name, gpu_ram, gpu_cores):
            self.name = gpu_name
            self.ram = gpu_ram
            self.cores = gpu_cores

        def show_gpu_infos(self):
            return  f"GPU name: {self.name}\nRAM: {self.ram} GB\nCORES: {self.cores}"



compute01 = Compute("Samsung", "Intel Corporation", 8, 16)

compute01.show_infos()