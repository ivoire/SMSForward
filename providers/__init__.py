import MobileFreeFr

def create(name, cfg):
    if name == 'mobile.free.fr':
        return MobileFreeFr.MobileFreeFr(cfg)
    else:
        raise NotImplementedError
