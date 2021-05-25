# Class to organize x y and z values for different wavelengths. each new wavelength is a new object of the class wave_psf
# uncomment last sections to debug

class wave_psf:
    # object attributes.
    x_res = None
    y_res = None
    z_res = None
    lambeda = ''
    lat_res = float()
    axi_res = float()

    def __init__(self, wavelength):
        self.lambeda = wavelength
        self.x_res = list()
        self.y_res = list()
        self.z_res = list()

    def addvalues(self, *arg):
        if len(arg) == 3:
            x, y, z = arg
            self.x_res.append(x)
            self.y_res.append(y)
            self.z_res.append(z)
        elif len(arg) == 1:
            try:
                x, y, z = arg[0]
                self.x_res.append(x)
                self.y_res.append(y)
                self.z_res.append(z)
            except:
                print('error, pls give 3 values (the X, Y and Z resolution)')


        #print(self.x_res, self.y_res, self.z_res)

    def getmeans(self):
        self.lat_res = round( (sum(self.x_res) + sum(self.y_res)) / (len(self.x_res) + len(self.y_res)), 3)
        self.axi_res = round( sum(self.z_res) / len(self.z_res), 3)
        print(f"For wavelength {self.lambeda}, lateral resolution = {self.lat_res} and axial resolution = {self.axi_res}")

# tests are greyed out (atom color scheme). Estão comentadas bois. ná crise mano. tranqui
#a = wave_psf('445')
#a.addvalues(0.200, 0.200, 0.500)
#a.addvalues(0.202, 0.203, 0.534)
#a.addvalues((0.212, 0.213, 0.520))

#b = wave_psf('333')
#b.addvalues(0.300, 0.302, 0.600)
#b.addvalues(0.302, 0.304, 0.602)

#a.getmeans()
#b.getmeans()
