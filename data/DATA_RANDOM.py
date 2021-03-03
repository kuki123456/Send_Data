import random
av=["5.120"+str(i) for i in range(1,11)]
ov=["TopN_OsVersion_19.90"+str(i) for i in range(1,11)]
pm=["TopN model 190"+str(i) for i in range(1,11)]
lt=[int(str(i)+"001000") for i in range(3,23) ]
di=["32424234d"+str(i) for i in range(1,11)]
av_iter_1=iter(av)
av_iter_2=iter(av)
ov_iter_1=iter(ov)
ov_iter_2=iter(ov)
pm_iter_1=iter(pm)
pm_iter_2=iter(pm)
lt_iter_1=iter(lt)
lt_iter_2=iter(lt)
di_iter_1=iter(di)
di_iter_2=iter(di)
# for i in range(1,21):
#     print(di_iter_1.__next__())
sv=["4.2."+str(i) for i in range(1,11)]
appmd5=["c4022c76-41b5-4aac-8113-0cac305ebaf8","b89f3d42-f514-4d09-9f82-0d15547fdff4","b348a6ef-a87a-423c-8bfd-fde0f405dece","59476b5e-974c-48d9-a445-77e02a16c13c","88fdd96a-5a59-44fa-bb13-e000054e3cd1"
        "273566b3-5f9d-4b51-834a-f4b34a71719f","c2734b91-3855-451d-99d5-c484d390be9c","c2734b91-3855-451d-99d5-c484d390be9c","738ba4a9-d12d-4d7a-9ad5-d5bba8e00ec0"]
class DATA_RANDOM(object):
    @classmethod
    def av_random(cls):
        return random.choice(av)
    @classmethod
    def ov_random(cls):
        return random.choice(ov)
    @classmethod
    def pm_random(cls):
        return random.choice(pm)
    @classmethod
    def sv_random(cls):
        return random.choice(sv)
    @classmethod
    def appmd5_random(cls):
        return random.choice(appmd5)
