from AlignmentDevRepa import *

attributes = ([(0,"edible",["edible=e", "poisonous=p"]),
    (1,"cap-shape",["bell=b","conical=c","convex=x","flat=f","knobbed=k","sunken=s"]),
    (2,"cap-surface",["fibrous=f","grooves=g","scaly=y","smooth=s"]),
    (3,"cap-color",["brown=n","buff=b","cinnamon=c","gray=g","green=r","pink=p","purple=u","red=e","white=w","yellow=y"]),
    (4,"bruises",["bruises=t","no=f"]),(5,"odor",["almond=a","anise=l","creosote=c","fishy=y","foul=f","musty=m","none=n","pungent=p","spicy=s"]),
    (6,"gill-attachment",["attached=a","descending=d","free=f","notched=n"]),
    (7,"gill-spacing",["close=c","crowded=w","distant=d"]),
    (8,"gill-size",["broad=b","narrow=n"]),
    (9,"gill-color",["black=k","brown=n","buff=b","chocolate=h","gray=g", "green=r","orange=o","pink=p","purple=u","red=e","white=w","yellow=y"]),
    (10,"stalk-shape",["enlarging=e","tapering=t"]),
    (11,"stalk-root",["bulbous=b","club=c","cup=u","equal=e","rhizomorphs=z","rooted=r","missing=?"]),
    (12,"stalk-surface-above-ring",["fibrous=f","scaly=y","silky=k","smooth=s"]),
    (13,"stalk-surface-below-ring",["fibrous=f","scaly=y","silky=k","smooth=s"]),
    (14,"stalk-color-above-ring",["brown=n","buff=b","cinnamon=c","gray=g","orange=o","pink=p","red=e","white=w","yellow=y"]),
    (15,"stalk-color-below-ring",["brown=n","buff=b","cinnamon=c","gray=g","orange=o", "pink=p","red=e","white=w","yellow=y"]),
    (16,"veil-type",["partial=p","universal=u"]),
    (17,"veil-color",["brown=n","orange=o","white=w","yellow=y"]),
    (18,"ring-number",["none=n","one=o","two=t"]),
    (19,"ring-type",["cobwebby=c","evanescent=e","flaring=f","large=l","none=n","pendant=p","sheathing=s","zone=z"]),
    (20,"spore-print-color",["black=k","brown=n","buff=b","chocolate=h", "green=r","orange=o","purple=u","white=w","yellow=y"]),
    (21,"population",["abundant=a","clustered=c","numerous=n","scattered=s","several=v","solitary=y"]),
    (22,"habitat",["grasses=g","leaves=l","meadows=m","paths=p","urban=u","waste=w","woods=d"])])

# names :: [(String, Map.Map String)]

def names():
    nn = []
    for (_,v,uu) in attributes:
        ww = sdict()
        for s in uu:
            xx = s.split('=')
            ww[xx[1]] = xx[0]
        nn.append((v,ww))
    return nn

# mushaa :: [String] -> Maybe Histogram

def mushaa(mush):
    nn = names()
    return llaa([(llss([(VarStr(v),ValStr(uu[u[0]])) for (u,(v,uu)) in zip(ss.split(','),nn)]),1) for ss in mush])

# mushIO :: Int -> IO (System, Histogram)

def mushIO():
    aa = mushaa(open('./agaricus-lepiota.data', 'r').readlines())
    uu = sys(aa)
    return (uu,aa)

def aahr(uu,aa):
    return hhhr(uu,aahh(aa))

def decomperIO(uu,vv,hr,wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed):
    return parametersSystemsHistoryRepasDecomperMaxRollByMExcludedSelfHighestFmaxIORepa(wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed,uu,vv,hr)

