class Mobile :

    def __init__(self,bat, clock, dualsim, fc, fourg, internM, mDept, mweight, ncores, pccam, pxheight, pxwith, ram, sch, scw,talktime,threeg,touchscreen, price):
        self.batt = bat
        self.clock = clock
        self.dualsim = dualsim
        self.fc = fc
        self.four_G = fourg
        self.inter_memo = internM
        self.m_dep = mDept
        self.m_weight = mweight
        self.n_cores = ncores
        self.pc_cam = pccam
        self.px_height = pxheight
        self.px_width = pxwith
        self.ram = ram
        self.sch = sch
        self.scw = scw
        self.talk_time = talktime
        self.three_G = threeg
        self.touchscreen = touchscreen
        self.price = price;

    def returnval(self) :
        return([[self.batt, self.clock, self.dualsim, self.fc, self.four_G, self.inter_memo, self.m_dep, self.m_weight, self.n_cores, self.pc_cam,
                 self.px_height, self.px_width, self.ram, self.sch, self.scw, self.talk_time, self.three_G, self.touchscreen]])
